"""Per-chapter synthesizer: collect prompts (chapter spec + source chunks),
apply results (HTML fragment file → state_dir/textbook/N.html)."""
from __future__ import annotations

import json
import shutil
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from course_merger.db.session import connect
from course_merger.synthesize.prompts import (
    SYNTHESIZER_VERSION,
    SYNTHESIZE_STYLE_GUIDE,
)


SCHEMA_VERSION = "1"
DEFAULT_SYNTHESIZER_ID = "claude-code-max:v1"


def collect_synthesize_prompts(
    *,
    db_path: Path,
    chapter_order_idx: int,
    max_source_chunks: int = 20,
) -> dict[str, Any]:
    """Build the envelope for synthesizing chapter N: chapter spec + relevant chunks."""
    with connect(db_path) as conn:
        chapter_row = conn.execute(
            """
            SELECT order_idx, module, title, blurb, primary_concept_slug,
                   related_concept_slugs
            FROM curriculum_chapters WHERE order_idx = ?
            """,
            (chapter_order_idx,),
        ).fetchone()
        if chapter_row is None:
            raise ValueError(f"no chapter at order_idx={chapter_order_idx}")

        order_idx, module, title, blurb, primary, related_json = chapter_row
        related = json.loads(related_json) if related_json else []
        all_slugs = [primary] + related

        placeholders = ",".join("?" for _ in all_slugs)
        chunk_rows = conn.execute(
            f"""
            SELECT DISTINCT chunks.id, courses.slug, lectures.idx,
                            lectures.title, lectures.video_url,
                            chunks.start_sec, chunks.text
            FROM chunks
            JOIN lectures ON lectures.id = chunks.lecture_id
            JOIN courses ON courses.id = lectures.course_id
            JOIN chunk_concepts cc ON cc.chunk_id = chunks.id
            JOIN concepts ON concepts.id = cc.concept_id
            WHERE concepts.slug IN ({placeholders})
            ORDER BY courses.slug, lectures.idx, chunks.idx
            LIMIT ?
            """,
            (*all_slugs, max_source_chunks),
        ).fetchall()

    source_chunks = [
        {
            "chunk_id": r[0],
            "course_slug": r[1],
            "lecture_idx": r[2],
            "lecture_title": r[3],
            "video_url": r[4],
            "start_sec": r[5],
            "text": r[6],
        }
        for r in chunk_rows
    ]

    return {
        "schema_version": SCHEMA_VERSION,
        "kind": "synthesize_prompts",
        "chapter": {
            "order_idx": order_idx,
            "module": module,
            "title": title,
            "blurb": blurb,
            "primary_concept_slug": primary,
            "related_concept_slugs": related,
        },
        "source_chunks": source_chunks,
        "style_guide": SYNTHESIZE_STYLE_GUIDE,
        "output_path_hint": f".course-merger/textbook/{order_idx}.html",
    }


def apply_synthesize_results(
    *,
    db_path: Path,
    state_dir: Path,
    results: dict[str, Any],
) -> None:
    """Read the synthesized HTML fragment, copy into state_dir/textbook/N.html,
    update curriculum_chapters row."""
    if results.get("schema_version") != SCHEMA_VERSION:
        raise ValueError(
            f"synthesize schema_version {results.get('schema_version')!r} unsupported"
        )
    if results.get("kind") != "synthesize_results":
        raise ValueError(
            f"synthesize kind {results.get('kind')!r} is not 'synthesize_results'"
        )

    chapter_order_idx = results["chapter_order_idx"]
    synthesizer = results.get("synthesizer", DEFAULT_SYNTHESIZER_ID)
    src_path = Path(results["html_fragment_path"])
    if not src_path.is_file():
        raise FileNotFoundError(f"html_fragment_path does not exist: {src_path}")

    with connect(db_path) as conn:
        row = conn.execute(
            "SELECT id FROM curriculum_chapters WHERE order_idx = ?",
            (chapter_order_idx,),
        ).fetchone()
        if row is None:
            raise ValueError(f"no chapter at order_idx={chapter_order_idx}")

        textbook_dir = state_dir / "textbook"
        textbook_dir.mkdir(parents=True, exist_ok=True)
        dst_name = f"{chapter_order_idx}.html"
        dst_path = textbook_dir / dst_name
        shutil.copyfile(src_path, dst_path)

        now = datetime.now(timezone.utc).isoformat()
        conn.execute(
            """
            UPDATE curriculum_chapters
            SET status='synthesized',
                synthesized_path=?, synthesized_at=?,
                curriculum_designer=?
            WHERE order_idx = ?
            """,
            (dst_name, now, synthesizer, chapter_order_idx),
        )
