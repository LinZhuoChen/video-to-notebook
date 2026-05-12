-- 0002: concept ontology, chunk-concept assignments, dirty-build tracking (Plan 2).

CREATE TABLE IF NOT EXISTS concepts (
  id              INTEGER PRIMARY KEY,
  slug            TEXT UNIQUE NOT NULL,
  canonical_name  TEXT NOT NULL,
  description     TEXT,
  ontology_source TEXT NOT NULL CHECK (ontology_source IN ('seed', 'discovered', 'user'))
);

CREATE TABLE IF NOT EXISTS concept_aliases (
  concept_id  INTEGER NOT NULL REFERENCES concepts(id) ON DELETE CASCADE,
  alias       TEXT NOT NULL,
  UNIQUE (alias)
);

CREATE TABLE IF NOT EXISTS chunk_concepts (
  chunk_id      INTEGER NOT NULL REFERENCES chunks(id) ON DELETE CASCADE,
  concept_id    INTEGER NOT NULL REFERENCES concepts(id) ON DELETE CASCADE,
  confidence    REAL NOT NULL,
  tagger_model  TEXT NOT NULL,
  PRIMARY KEY (chunk_id, concept_id)
);

CREATE INDEX IF NOT EXISTS idx_chunk_concept_concept ON chunk_concepts(concept_id);

CREATE TABLE IF NOT EXISTS build_meta (
  key    TEXT PRIMARY KEY,
  value  TEXT NOT NULL
);

-- proposed_tags: stage area for LLM-proposed concept names that don't match the ontology yet.
-- The `cluster` command consumes these and decides whether to merge/create/reject.
CREATE TABLE IF NOT EXISTS proposed_tags (
  id           INTEGER PRIMARY KEY,
  chunk_id     INTEGER NOT NULL REFERENCES chunks(id) ON DELETE CASCADE,
  raw_tag      TEXT NOT NULL,
  confidence   REAL NOT NULL,
  tagger_model TEXT NOT NULL,
  UNIQUE (chunk_id, raw_tag)
);
