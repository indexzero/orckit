#!/bin/sh
# model-pinned.sh <dispatch-dir>
# Verifies the declaration format for RAILS rule 26, not model availability.
# Accepts an explicit versioned model id plus Context-window: N tokens,
# or a supported legacy suffix such as model-v1[1m]. No provider allowlist.
# Only numbered dispatch prompts are checked, never results or companions.
set -eu
[ "$#" -eq 1 ] && [ -d "$1" ] || {
  echo 'usage: model-pinned.sh <existing-dispatch-dir>' >&2
  exit 2
}
bad=0
for f in "$1"/D-*.md; do
  [ -f "$f" ] || continue
  printf '%s\n' "${f##*/}" | grep -Eq '^D-[0-9]+\.md$' || continue
  if ! awk -v file="$f" '
    /^----8<----/ || /^---[[:space:]]*$/ { exit }
    /^Model:/ {
      models++
      model = $0
      sub(/^Model:[[:space:]]*/, "", model)
      sub(/[[:space:]].*$/, "", model)
    }
    /^Context-window:/ {
      windows++
      window = $0
    }
    END {
      suffix = model ~ /\[[1-9][0-9]*[mk]\]$/
      sub(/\[[1-9][0-9]*[mk]\]$/, "", model)
      # This is syntax validation. The host must verify the actual id.
      valid_model = models == 1 && model ~ /^[[:alnum:]][[:alnum:]_.\/:+-]*[[:alnum:]]$/ && model ~ /[0-9]/ && model ~ /[[:alpha:]]/ && model !~ /(^|[-_.\/])(latest|auto|default)($|[-_.\/])/
      valid_window = windows == 1 && window ~ /^Context-window:[[:space:]]*[1-9][0-9]* tokens[[:space:]]*$/
      if (!valid_model || (windows ? !valid_window : !suffix)) {
        print "model or context window not pinned: " file
        exit 1
      }
    }
  ' "$f"; then
    bad=1
  fi
done
exit "$bad"
