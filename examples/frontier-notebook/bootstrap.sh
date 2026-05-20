#!/usr/bin/env bash
# bootstrap.sh — init + crawl only. No LLM, no API key required.
#
# This is the no-key half of the pipeline. It produces a populated SQLite DB
# with subtitles. After it finishes, follow `RUNBOOK.md` from inside a
# Claude Code or Codex session to drive tag → cluster → curriculum →
# synthesize → explain → build.
#
# If you have an ANTHROPIC_API_KEY and prefer a one-shot script, use
# `build.sh` instead — it includes the LLM steps via --use-api.
#
# Usage:
#   bash bootstrap.sh                # zh (default)
#   bash bootstrap.sh --language en  # en

set -euo pipefail

HERE="$(cd "$(dirname "$0")" && pwd)"
PROJECT="$HERE/.video-to-notebook-project"
COURSES="$HERE/courses.toml"

LANGUAGE="zh"

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
    -h|--help)
      sed -n '/^# bootstrap.sh/,/^$/p' "$0" | sed 's/^# \?//'
      exit 0
      ;;
    *)
      echo "unknown argument: $1" >&2
      exit 1
      ;;
  esac
done

if ! command -v video-to-notebook >/dev/null 2>&1; then
  echo "error: video-to-notebook not on PATH. Install with: pip install video-to-notebook" >&2
  exit 2
fi

if ! command -v yt-dlp >/dev/null 2>&1; then
  echo "error: yt-dlp not on PATH. Install with: pip install yt-dlp" >&2
  exit 3
fi

mkdir -p "$PROJECT"
cd "$PROJECT"

if [ ! -d ".video-to-notebook" ]; then
  video-to-notebook init --language "$LANGUAGE"
fi

# Parse courses.toml — extract slug | url | platform | cookies_from per row.
python3 <<PY > /tmp/cm-bootstrap-courses.txt
import tomllib
with open("$COURSES", "rb") as f:
    data = tomllib.load(f)
for c in data.get("course", []):
    print(f"{c['slug']}|{c['url']}|{c.get('platform', 'youtube')}|{c.get('cookies_from', '')}")
PY

while IFS='|' read -r SLUG URL PLATFORM COOKIES; do
  echo ""
  echo "=== crawl: $SLUG ($PLATFORM) ==="
  EXTRA=""
  if [ -n "$COOKIES" ]; then
    EXTRA="--cookies-from $COOKIES"
  fi
  video-to-notebook crawl "$URL" --name "$SLUG" $EXTRA
done < /tmp/cm-bootstrap-courses.txt

echo ""
echo "DONE. DB populated at: $PROJECT/.video-to-notebook/db.sqlite"
echo ""
echo "Next step — drive the LLM stages from inside Claude Code or Codex:"
echo "  see $HERE/RUNBOOK.md"
