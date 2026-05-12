#!/usr/bin/env bash
# install-locally.sh — symlink the course-merger skill into ~/.claude/skills/
#
# After running this, Claude Code will discover the skill on next session start.
# Use this before there's a public marketplace listing.

set -euo pipefail

SKILL_DIR="$(cd "$(dirname "$0")/.." && pwd)"
TARGET_PARENT="$HOME/.claude/skills"
TARGET="$TARGET_PARENT/course-merger"

mkdir -p "$TARGET_PARENT"

if [ -e "$TARGET" ] || [ -L "$TARGET" ]; then
  echo ">>> Existing skill at $TARGET — replacing"
  rm -rf "$TARGET"
fi

ln -s "$SKILL_DIR" "$TARGET"
echo "installed: $TARGET → $SKILL_DIR"
echo ""
echo "Restart Claude Code (or wait for next session start) to pick up the skill."
echo "Verify with: ls -la $TARGET"
