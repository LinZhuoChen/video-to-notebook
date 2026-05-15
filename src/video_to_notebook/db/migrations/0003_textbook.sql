-- 0003: curriculum chapters for Plan 6 (textbook generator).

CREATE TABLE IF NOT EXISTS curriculum_chapters (
  id                    INTEGER PRIMARY KEY,
  order_idx             INTEGER UNIQUE NOT NULL,
  module                TEXT NOT NULL,
  title                 TEXT NOT NULL,
  blurb                 TEXT NOT NULL,
  primary_concept_slug  TEXT NOT NULL,
  related_concept_slugs TEXT NOT NULL DEFAULT '[]',
  curriculum_designer   TEXT NOT NULL,
  status                TEXT NOT NULL DEFAULT 'planned'
                          CHECK (status IN ('planned', 'synthesized', 'failed')),
  synthesized_path      TEXT,
  synthesized_at        TEXT
);

CREATE INDEX IF NOT EXISTS idx_curriculum_order ON curriculum_chapters(order_idx);
