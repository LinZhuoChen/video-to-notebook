-- 0004: concept_explanations — rich illustrated HTML per concept.

CREATE TABLE IF NOT EXISTS concept_explanations (
  id              INTEGER PRIMARY KEY,
  concept_id      INTEGER NOT NULL UNIQUE REFERENCES concepts(id) ON DELETE CASCADE,
  html_fragment   TEXT NOT NULL,
  explainer       TEXT NOT NULL,
  generated_at    TEXT NOT NULL
);

CREATE INDEX IF NOT EXISTS idx_concept_explanations_concept ON concept_explanations(concept_id);
