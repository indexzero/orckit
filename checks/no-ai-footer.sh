#!/bin/sh
# no-ai-footer.sh <pr-number>
# Exit 0 iff the PR body carries no AI-attribution footer.
set -eu
pr="$1"
if gh pr view "$pr" --json body -q .body | grep -niE 'generated with|co-authored-by: (claude|gpt|gemini)|🤖'; then
  echo "AI footer found in PR #$pr body (above)" >&2
  exit 1
fi
exit 0
