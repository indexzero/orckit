#!/bin/sh
# ownership-subset.sh <repo> <base> <allowed-file...>
# Exit 0 iff every file changed vs <base> is in the allowed list.
set -eu
repo="$1"; base="$2"; shift 2
bad=0
for f in $(git -C "$repo" diff "$base" --name-only); do
  ok=0
  for a in "$@"; do [ "$f" = "$a" ] && ok=1 && break; done
  if [ "$ok" = 0 ]; then echo "out of scope: $f"; bad=1; fi
done
exit "$bad"
