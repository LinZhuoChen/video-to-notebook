#!/usr/bin/env bash
# build.sh — run the full video-to-notebook pipeline for the Frontier Notebook demo
#
# Reads courses.toml in this directory, crawls every entry, tags & clusters
# using ontology.yaml, builds the static site.

set -euo pipefail

HERE="$(cd "$(dirname "$0")" && pwd)"
PROJECT="$HERE/.video-to-notebook-project"
ONTOLOGY="$HERE/ontology.yaml"
COURSES="$HERE/courses.toml"

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
  video-to-notebook init
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

echo ""
echo "=== build ==="
video-to-notebook build

echo ""
echo "DONE. Open: file://$PROJECT/site/dist/index.html"
echo "       Or: cd '$PROJECT' && video-to-notebook serve"
