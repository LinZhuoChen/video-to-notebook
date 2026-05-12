#!/usr/bin/env bash
# run-pipeline.sh — chain crawl/tag/cluster/build for a fresh corpus
#
# Usage:
#   bash run-pipeline.sh <project-dir> <ontology.yaml> <course-url> [<course-url> ...]
#
# Each course URL gets crawled into a slug derived from its playlist/video ID.
# Requires: course-merger installed, ANTHROPIC_API_KEY set, Node 20+ for build.

set -euo pipefail

if [ "$#" -lt 3 ]; then
  echo "usage: $0 <project-dir> <ontology.yaml> <course-url> [<course-url> ...]" >&2
  exit 1
fi

PROJECT_DIR="$1"
ONTOLOGY="$2"
shift 2

if [ -z "${ANTHROPIC_API_KEY:-}" ]; then
  echo "error: ANTHROPIC_API_KEY is not set" >&2
  exit 2
fi

if [ ! -f "$ONTOLOGY" ]; then
  echo "error: ontology file not found at $ONTOLOGY" >&2
  exit 3
fi

mkdir -p "$PROJECT_DIR"
cd "$PROJECT_DIR"

if [ ! -d ".course-merger" ]; then
  echo ">>> course-merger init"
  course-merger init
else
  echo ">>> reusing existing .course-merger/"
fi

for url in "$@"; do
  echo ">>> course-merger crawl $url"
  course-merger crawl "$url"
done

echo ">>> course-merger tag --ontology $ONTOLOGY"
course-merger tag --ontology "$ONTOLOGY"

echo ">>> course-merger cluster --ontology $ONTOLOGY"
course-merger cluster --ontology "$ONTOLOGY"

echo ">>> course-merger build"
course-merger build

echo ""
echo "DONE. Open site/dist/index.html or run 'course-merger serve'."
