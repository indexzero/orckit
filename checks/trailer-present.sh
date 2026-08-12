#!/bin/sh
# trailer-present.sh <repo> <range>   e.g. trailer-present.sh . main..HEAD
# Exit 0 iff every commit in <range> carries a Co-Authored-By: trailer.
set -eu
repo="$1"; range="$2"
bad=0
for sha in $(git -C "$repo" rev-list "$range"); do
  if ! git -C "$repo" log -1 --format=%B "$sha" | grep -q '^Co-Authored-By:'; then
    echo "missing trailer: $(git -C "$repo" log -1 --oneline "$sha")"
    bad=1
  fi
done
exit "$bad"
