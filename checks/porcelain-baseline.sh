#!/usr/bin/env bash
# porcelain-baseline.sh <repo> <baseline-file>
# Exit 0 iff `git -C <repo> status --porcelain` equals <baseline-file> exactly.
set -eu
repo="$1"; baseline="$2"
actual="$(git -C "$repo" status --porcelain | sort)"
expected="$(sort "$baseline")"
if [ "$actual" = "$expected" ]; then exit 0; fi
echo "CONTAMINATION — porcelain differs from baseline:" >&2
diff <(printf '%s\n' "$expected") <(printf '%s\n' "$actual") >&2 || true
exit 1
