"""YAML ontology loader: in-memory model of seed concepts with alias lookup."""
from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path

import yaml


@dataclass(frozen=True, slots=True)
class Concept:
    slug: str
    canonical_name: str
    description: str = ""
    aliases: tuple[str, ...] = field(default_factory=tuple)


@dataclass(frozen=True, slots=True)
class Ontology:
    concepts: tuple[Concept, ...]
    _by_slug: dict[str, Concept] = field(default_factory=dict, hash=False, compare=False)
    _by_alias: dict[str, Concept] = field(default_factory=dict, hash=False, compare=False)

    def by_slug(self, slug: str) -> Concept | None:
        return self._by_slug.get(slug)

    def find_by_alias(self, alias: str) -> Concept | None:
        return self._by_alias.get(alias.strip().lower())

    def top_n_slugs(self, n: int) -> list[str]:
        return [c.slug for c in self.concepts[:n]]


def load_ontology(path: Path) -> Ontology:
    """Load a YAML ontology file. Raises ValueError on duplicate slugs."""
    data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    raw = data.get("concepts", []) or []

    concepts: list[Concept] = []
    seen_slugs: set[str] = set()
    for entry in raw:
        slug = entry["slug"]
        if slug in seen_slugs:
            raise ValueError(f"duplicate slug in ontology: {slug!r}")
        seen_slugs.add(slug)
        concepts.append(
            Concept(
                slug=slug,
                canonical_name=entry["canonical_name"],
                description=entry.get("description", ""),
                aliases=tuple(entry.get("aliases", []) or []),
            )
        )

    by_slug = {c.slug: c for c in concepts}
    by_alias: dict[str, Concept] = {}
    for c in concepts:
        by_alias[c.canonical_name.strip().lower()] = c
        for alias in c.aliases:
            by_alias[alias.strip().lower()] = c

    return Ontology(
        concepts=tuple(concepts), _by_slug=by_slug, _by_alias=by_alias
    )
