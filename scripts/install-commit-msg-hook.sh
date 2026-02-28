#!/bin/sh
# Install commit-msg hook that strips "Made-with: Cursor" from commit messages
HOOK_SRC="$(dirname "$0")/commit-msg.hook"
HOOK_DEST="$(git rev-parse --git-dir)/hooks/commit-msg"
if [ -f "$HOOK_SRC" ]; then
  cp "$HOOK_SRC" "$HOOK_DEST"
  chmod +x "$HOOK_DEST"
  echo "Installed commit-msg hook (strips Made-with: Cursor)"
else
  echo "Error: $HOOK_SRC not found"
  exit 1
fi
