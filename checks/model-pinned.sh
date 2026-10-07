#!/bin/sh
# model-pinned.sh <dispatch-dir>
# Verifies: RAILS rule 26. Every dispatch file names a model with its
#           context window pinned.
# Usage:    model-pinned.sh orchestration/dispatches
# Exit:     0 = every D-*.md has a `Model:` line that names an explicit model
#           id and a window pin; nonzero = the offending files on stdout.
#
# A pin is one of:
#   - an explicit window suffix on the id, for example `claude-opus-4-8[1m]`
#   - a model whose window is 1M by default, listed in WIDE_BY_DEFAULT below
# An alias such as `opus` or `sonnet` is not a pin.
set -eu
dir="$1"
WIDE_BY_DEFAULT='claude-fable-5-1|claude-fable-5|claude-opus-5-5|claude-opus-5|claude-sonnet-5-5|claude-sonnet-5'
bad=0
for f in "$dir"/D-*.md; do
  [ -e "$f" ] || continue
  case "$f" in *.result.*) continue ;; esac
  line=$(grep -m1 '^Model:' "$f" || true)
  if [ -z "$line" ]; then
    echo "no Model line: $f"; bad=1; continue
  fi
  if printf '%s' "$line" | grep -qE '\[[0-9]+[mk]\]'; then continue; fi
  if printf '%s' "$line" | grep -qE "($WIDE_BY_DEFAULT)"; then continue; fi
  echo "model not pinned to a context window: $f"
  echo "  $line"
  bad=1
done
exit "$bad"
