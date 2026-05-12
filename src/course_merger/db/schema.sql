-- Plan 1 subset. concepts/aliases/chunk_concepts/build_meta tables land in Plan 2.

CREATE TABLE IF NOT EXISTS courses (
  id          INTEGER PRIMARY KEY,
  slug        TEXT UNIQUE NOT NULL,
  title       TEXT NOT NULL,
  platform    TEXT NOT NULL CHECK (platform IN ('youtube', 'bilibili')),
  source_url  TEXT NOT NULL,
  added_at    TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS lectures (
  id            INTEGER PRIMARY KEY,
  course_id     INTEGER NOT NULL REFERENCES courses(id) ON DELETE CASCADE,
  idx           INTEGER NOT NULL,
  title         TEXT NOT NULL,
  video_url     TEXT NOT NULL,
  duration_sec  INTEGER,
  transcript    TEXT,
  status        TEXT NOT NULL CHECK (status IN ('ok', 'paywalled', 'no_subs', 'error')),
  UNIQUE (course_id, idx)
);

CREATE TABLE IF NOT EXISTS chunks (
  id          INTEGER PRIMARY KEY,
  lecture_id  INTEGER NOT NULL REFERENCES lectures(id) ON DELETE CASCADE,
  idx         INTEGER NOT NULL,
  start_sec   REAL NOT NULL,
  end_sec     REAL NOT NULL,
  text        TEXT NOT NULL,
  UNIQUE (lecture_id, idx)
);

CREATE INDEX IF NOT EXISTS idx_chunk_lecture ON chunks(lecture_id);
