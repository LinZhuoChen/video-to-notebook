#!/usr/bin/env bash
# build.sh — run the full video-to-notebook pipeline for the Frontier Notebook demo
#
# Reads courses.toml in this directory, crawls every entry, tags & clusters
# using ontology.yaml, builds the static site.
#
# v2.2+ bilingual support:
#   bash build.sh                 # zh only (default — backwards compatible)
#   bash build.sh --language en   # en only
#   bash build.sh --bilingual     # zh + en (two synthesize/explain passes
#                                 #          against the same crawl + tag + cluster)
#
# For --bilingual to make sense, the source courses must have transcripts that
# work for both target languages (e.g. English lectures → both languages can
# be regenerated from the same audio; otherwise pick the language that
# matches the source).

set -euo pipefail

HERE="$(cd "$(dirname "$0")" && pwd)"
PROJECT="$HERE/.video-to-notebook-project"
ONTOLOGY="$HERE/ontology.yaml"
COURSES="$HERE/courses.toml"

LANGUAGE="zh"
BILINGUAL=0

while [ $# -gt 0 ]; do
  case "$1" in
    --language)
      LANGUAGE="$2"
      shift 2
      ;;
    --language=*)
      LANGUAGE="${1#*=}"
      shift
      ;;
    --bilingual)
      BILINGUAL=1
      shift
      ;;
    -h|--help)
      sed -n '/^# build.sh/,/^$/p' "$0" | sed 's/^# \?//'
      exit 0
      ;;
    *)
      echo "unknown argument: $1" >&2
      exit 1
      ;;
  esac
done

if [ -z "${ANTHROPIC_API_KEY:-}" ]; then
  echo "error: ANTHROPIC_API_KEY is not set" >&2
  exit 1
fi

if ! command -v video-to-notebook >/dev/null 2>&1; then
  echo "error: video-to-notebook not on PATH. Install with: pip install video-to-notebook" >&2
  exit 2
fi

if ! command -v node >/dev/null 2>&1; then
  echo "error: node not on PATH. Need Node 20+." >&2
  exit 3
fi

mkdir -p "$PROJECT"
cd "$PROJECT"

if [ ! -d ".video-to-notebook" ]; then
  # Bilingual init: pick the *first* language; the second pass switches in-place.
  FIRST_LANG="$LANGUAGE"
  if [ "$BILINGUAL" = 1 ]; then
    FIRST_LANG="zh"  # arbitrary default; second pass will be en
  fi
  video-to-notebook init --language "$FIRST_LANG"
fi

# Parse courses.toml — extract slug + url pairs.
python3 <<PY > /tmp/cm-courses.txt
import tomllib
with open("$COURSES", "rb") as f:
    data = tomllib.load(f)
for c in data.get("course", []):
    slug = c["slug"]
    url = c["url"]
    platform = c.get("platform", "youtube")
    cookies = c.get("cookies_from", "")
    print(f"{slug}|{url}|{platform}|{cookies}")
PY

while IFS='|' read -r SLUG URL PLATFORM COOKIES; do
  echo ""
  echo "=== crawl: $SLUG ($PLATFORM) ==="
  EXTRA=""
  if [ -n "$COOKIES" ]; then
    EXTRA="--cookies-from $COOKIES"
  fi
  video-to-notebook crawl "$URL" --name "$SLUG" $EXTRA
done < /tmp/cm-courses.txt

echo ""
echo "=== tag ==="
video-to-notebook tag --ontology "$ONTOLOGY"

echo ""
echo "=== cluster ==="
video-to-notebook cluster --ontology "$ONTOLOGY"

# Helper: regenerate synthesize/explain content for the current language.
# (curriculum + synthesize + explain are in-session only — this script can't
# drive them. The build below picks up whatever's already in the DB.)
build_one() {
  local lang="$1"
  echo ""
  echo "=== build (language=$lang) ==="
  # Switch project language so the build writers route content to <lang>/
  sqlite3 .video-to-notebook/db.sqlite \
    "INSERT INTO build_meta (key, value) VALUES ('language', '$lang') \
     ON CONFLICT(key) DO UPDATE SET value=excluded.value;"
  video-to-notebook build
}

if [ "$BILINGUAL" = 1 ]; then
  build_one zh
  build_one en
else
  build_one "$LANGUAGE"
fi

echo ""
echo "DONE. Open: file://$PROJECT/site/dist/index.html"
echo "       Or: cd '$PROJECT' && video-to-notebook serve"
if [ "$BILINGUAL" = 1 ]; then
  echo ""
  echo "Note: --bilingual built both zh/ and en/ Astro content folders, but the"
  echo "synthesize/explain HTML fragments need to be generated separately for"
  echo "each language via an in-session agent (Claude Code or Codex). This"
  echo "script only swings the build_meta.language flag + reruns the writer."
fi
