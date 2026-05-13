#!/usr/bin/env bash
# install-codex.sh — wire course-merger into the OpenAI Codex CLI.
#
# Codex CLI discovers project context two ways:
#   1. `AGENTS.md` in the current working directory (per-project instructions).
#   2. `~/.codex/AGENTS.md` (global instructions; merged with project AGENTS.md).
#
# This script handles both:
#   - When run inside a course-merger study project: symlinks the repo's
#     AGENTS.md into the cwd so Codex picks it up locally.
#   - When run with --global: writes a stanza into ~/.codex/AGENTS.md that
#     points Codex to the course-merger CLI conventions globally.
#
# Usage:
#   bash install-codex.sh             # symlink into cwd (project mode)
#   bash install-codex.sh --global    # append to ~/.codex/AGENTS.md (global)
#   bash install-codex.sh --help

set -euo pipefail

REPO_DIR="$(cd "$(dirname "$0")/../../.." && pwd)"
REPO_AGENTS="$REPO_DIR/AGENTS.md"
GLOBAL_AGENTS="$HOME/.codex/AGENTS.md"

usage() {
  cat <<EOF
install-codex.sh — wire course-merger into OpenAI Codex CLI

Usage:
  bash install-codex.sh             Symlink AGENTS.md into the cwd (project mode)
  bash install-codex.sh --global    Append a pointer to ~/.codex/AGENTS.md
  bash install-codex.sh --help

Prereqs:
  - Codex CLI installed (https://github.com/openai/codex)
  - course-merger CLI installed (\`pip install course-merger\`)

After install, start Codex from your study-project directory:
  cd my-study-site
  codex          # Codex reads AGENTS.md, knows how to drive course-merger
EOF
}

case "${1:-}" in
  -h|--help)
    usage
    exit 0
    ;;
  --global)
    mkdir -p "$(dirname "$GLOBAL_AGENTS")"
    if grep -q "course-merger" "$GLOBAL_AGENTS" 2>/dev/null; then
      echo ">>> ~/.codex/AGENTS.md already mentions course-merger — skipping."
      exit 0
    fi
    cat >> "$GLOBAL_AGENTS" <<EOF

## course-merger

When the user wants to crawl/merge open-courseware into a study site, drive the
\`course-merger\` CLI. Each LLM stage supports \`--print-prompts\` / \`--apply-results\`
(see $REPO_DIR/docs/AGENT_PROTOCOL.md for the JSON envelope schemas).

When writing results envelopes, set the agent-id to \`codex-cli:v1\`.

Reference repo: $REPO_DIR
EOF
    echo "appended course-merger pointer to $GLOBAL_AGENTS"
    echo ""
    echo "Now \`codex\` will know about course-merger from any directory."
    ;;
  ""|--project)
    if [ ! -f "$REPO_AGENTS" ]; then
      echo "error: $REPO_AGENTS does not exist." >&2
      exit 1
    fi
    if [ -f "AGENTS.md" ] && [ ! -L "AGENTS.md" ]; then
      echo "error: ./AGENTS.md exists and is not a symlink. Move it aside first." >&2
      exit 1
    fi
    if [ -L "AGENTS.md" ]; then
      rm "AGENTS.md"
    fi
    ln -s "$REPO_AGENTS" AGENTS.md
    echo "installed: ./AGENTS.md → $REPO_AGENTS"
    echo ""
    echo "Run \`codex\` here. Codex will read AGENTS.md and know how to drive"
    echo "the course-merger pipeline. Tell it something like:"
    echo ""
    echo "  > Crawl this YouTube playlist and tag using examples/ontology-llm.yaml"
    ;;
  *)
    echo "unknown argument: $1" >&2
    usage
    exit 1
    ;;
esac
