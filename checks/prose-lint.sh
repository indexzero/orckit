#!/bin/sh
# prose-lint.sh <file...>
# Verifies: RAILS rule 27 and playbooks/writing-rules.md. Prose carries no
#           semicolon, no em dash or en dash as punctuation, no "should", no
#           contraction, and no sentence longer than 25 words.
# Usage:    prose-lint.sh kit/*.md playbooks/*.md
# Exit:     0 = clean; nonzero = each violation on stdout as file:line: rule.
#
# Skipped: fenced code blocks whose info string is not `markdown` (a
# markdown fence is a template body and IS prose), indented code, table
# rows, and inline code. A heading, a blank line, or a list marker ends a
# sentence. Headings are exempt from the dash rule, because a title may
# carry a dash as a separator.
set -eu
bad=0
for f in "$@"; do
  awk -v file="$f" '
    BEGIN { skip = 0; buf = "" }
    function flush() { buf = buf ". " }
    /^```/ {
      if (skip) { skip = 0; next }
      if ($0 ~ /^```markdown/) { next }
      skip = 1; next
    }
    skip { next }
    /^    / { next }
    /^[[:space:]]*\|/ { next }
    /^[[:space:]]*$/ { flush(); next }
    /^#/ { flush() }
    /^[[:space:]]*([-*]|[0-9]+\.|[0-9]+[a-z]\.) / { flush() }
    {
      line = $0
      gsub(/`[^`]*`/, "X", line)
      gsub(/\*\*/, "", line)
      if (line ~ /;/) { print file ":" NR ": semicolon"; bad = 1 }
      if (line !~ /^#/ && line ~ /[—–]/) { print file ":" NR ": dash as punctuation"; bad = 1 }
      if (tolower(line) ~ /(^|[^a-z])should([^a-z]|$)/) { print file ":" NR ": should"; bad = 1 }
      if (line ~ /[A-Za-z]'\''(ll|re|ve|d|t|m)([^A-Za-z]|$)/) { print file ":" NR ": contraction"; bad = 1 }
      if (line ~ /^#/) { next }
      buf = buf " " line
      if (line ~ /[>\]:]$/) { flush() }
    }
    END {
      n = split(buf, s, /[.!?][[:space:]]+/)
      for (i = 1; i <= n; i++) {
        gsub(/^[[:space:]]+|[[:space:]]+$/, "", s[i])
        if (s[i] == "") continue
        w = split(s[i], words, /[[:space:]]+/)
        if (w > 25) { print file ": sentence over 25 words (" w "): " substr(s[i], 1, 80) "..."; bad = 1 }
      }
      exit bad
    }
  ' "$f" || bad=1
done
exit "$bad"
