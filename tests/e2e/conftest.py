"""E2E test fixtures: spin up a real astro dev server against a seeded project."""
from __future__ import annotations

import os
import subprocess
import time
import urllib.request
from pathlib import Path

import pytest
from typer.testing import CliRunner

from course_merger.cli import app
from course_merger.db.session import connect


def _seed_corpus(project_root: Path) -> None:
    db = project_root / ".course-merger" / "db.sqlite"
    with connect(db) as conn:
        conn.execute(
            "INSERT INTO courses (id, slug, title, platform, source_url, added_at) "
            "VALUES (1, 'cs336', 'CS336', 'youtube', 'https://www.youtube.com/playlist?list=PLX', '2026-05-09'),"
            "(2, 'gpu-mode', 'GPU MODE', 'youtube', 'https://www.youtube.com/playlist?list=PLY', '2026-05-09')"
        )
        conn.execute(
            "INSERT INTO lectures (id, course_id, idx, title, video_url, transcript, status) "
            "VALUES (1, 1, 1, 'L1 Intro', 'https://www.youtube.com/watch?v=aaa', 't', 'ok'),"
            "(2, 2, 1, 'L1 CUDA basics', 'https://www.youtube.com/watch?v=bbb', 't', 'ok')"
        )
        conn.execute(
            "INSERT INTO chunks (id, lecture_id, idx, start_sec, end_sec, text) "
            "VALUES (1, 1, 0, 0, 60, 'CS336 talks about attention here'),"
            "(2, 2, 0, 0, 60, 'GPU MODE explains attention from CUDA angle')"
        )
        conn.execute(
            "INSERT INTO concepts (id, slug, canonical_name, ontology_source) "
            "VALUES (1, 'attention', 'Attention', 'seed')"
        )
        conn.execute(
            "INSERT INTO chunk_concepts (chunk_id, concept_id, confidence, tagger_model) "
            "VALUES (1, 1, 0.9, 'haiku:v1'),(2, 1, 0.88, 'haiku:v1')"
        )


@pytest.fixture(scope="session")
def astro_server(tmp_path_factory: pytest.TempPathFactory):
    """Start astro dev once per session; tear down at end."""
    project = tmp_path_factory.mktemp("e2e_project")
    cwd = os.getcwd()
    os.chdir(project)
    try:
        runner = CliRunner()
        runner.invoke(app, ["init"])
        _seed_corpus(project)
        runner.invoke(app, ["build", "--no-npm"])

        site = project / "site"
        subprocess.run(["npm", "install", "--silent"], cwd=site, check=True)
        proc = subprocess.Popen(
            ["npm", "run", "dev", "--", "--port", "4321"],
            cwd=site,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
        )

        ready = False
        for _ in range(60):
            try:
                with urllib.request.urlopen("http://localhost:4321/", timeout=1) as resp:
                    if resp.status == 200:
                        ready = True
                        break
            except Exception:
                time.sleep(0.5)
        if not ready:
            proc.kill()
            raise RuntimeError("astro dev did not become ready in 30s")

        yield "http://localhost:4321"

        proc.terminate()
        try:
            proc.wait(timeout=5)
        except subprocess.TimeoutExpired:
            proc.kill()
    finally:
        os.chdir(cwd)
