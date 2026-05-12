#!/usr/bin/env bash
# build.sh — run the full course-merger pipeline for the Frontier Notebook demo
#
# Reads courses.toml in this directory, crawls every entry, tags & clusters
# using ontology.yaml, builds the static site.

set -euo pipefail

HERE="$(cd "$(dirname "$0")" && pwd)"
PROJECT="$HERE/.course-merger-project"
ONTOLOGY="$HERE/ontology.yaml"
COURSES="$HERE/courses.toml"

if [ -z "${ANTHROPIC_API_KEY:-}" ]; then
  echo "error: ANTHROPIC_API_KEY is not set" >&2
  exit 1
fi

if ! command -v course-merger >/dev/null 2>&1; then
  echo "error: course-merger not on PATH. Install with: pip install course-merger" >&2
  exit 2
fi

if ! command -v node >/dev/null 2>&1; then
  echo "error: node not on PATH. Need Node 20+." >&2
  exit 3
fi

mkdir -p "$PROJECT"
cd "$PROJECT"

if [ ! -d ".course-merger" ]; then
  course-merger init
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
  course-merger crawl "$URL" --name "$SLUG" $EXTRA
done < /tmp/cm-courses.txt

echo ""
echo "=== tag ==="
course-merger tag --ontology "$ONTOLOGY"

echo ""
echo "=== cluster ==="
course-merger cluster --ontology "$ONTOLOGY"

echo ""
echo "=== build ==="
course-merger build

echo ""
echo "DONE. Open: file://$PROJECT/site/dist/index.html"
echo "       Or: cd '$PROJECT' && course-merger serve"
