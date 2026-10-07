#!/bin/sh
# Offline regression cases for model-pinned.sh. Model ids are syntax fixtures.
set -eu
check_dir=$(CDPATH='' cd -- "$(dirname -- "$0")" && pwd)
scratch=$(mktemp -d "${TMPDIR:-/tmp}/orckit-model-pinned.XXXXXX")
trap 'rm -rf "$scratch"' EXIT HUP INT TERM
passed=0

expect() {
  expected=$1
  label=$2
  contents=$3
  printf '%s\n' "$contents" > "$scratch/D-001.md"
  actual=0
  sh "$check_dir/model-pinned.sh" "$scratch" > "$scratch/output" 2>&1 || actual=$?
  if [ "$actual" -ne "$expected" ]; then
    printf 'FAIL: %s (expected %s, got %s)\n' "$label" "$expected" "$actual"
    cat "$scratch/output"
    exit 1
  fi
  passed=$((passed + 1))
}

expect 0 'separate context field' 'Model: gpt-6-sol
Context-window: 128000 tokens'
expect 0 'short versioned model id' 'Model: o3
Context-window: 128000 tokens'
expect 0 'legacy suffix and metadata' 'Model: claude-opus-4-8[1m] · Dispatched: 2026-10-07'
expect 0 'legacy k suffix' 'Model: provider-model-2[200k]'
expect 1 'missing window' 'Model: gpt-6-sol'
expect 1 'implicit Claude window removed' 'Model: claude-fable-5-1'
expect 1 'short alias with suffix' 'Model: opus[1m]'
expect 1 'rolling model id' 'Model: provider-model-2-latest
Context-window: 128000 tokens'
expect 1 'placeholder' 'Model: <exact model id>
Context-window: <positive integer> tokens'
expect 1 'missing model' 'Context-window: 128000 tokens'
expect 1 'zero capacity' 'Model: gpt-6-sol
Context-window: 0 tokens'
expect 1 'negative capacity' 'Model: gpt-6-sol
Context-window: -128000 tokens'
expect 1 'zero suffix' 'Model: provider-model-2[0m]'
expect 1 'suffix in unrelated metadata' 'Model: opus · Note: [1m]'
expect 1 'duplicate model' 'Model: gpt-6-sol
Model: provider-model-2
Context-window: 128000 tokens'
expect 1 'duplicate window' 'Model: gpt-6-sol
Context-window: 128000 tokens
Context-window: 256000 tokens'
expect 1 'window in assignment cannot satisfy header' 'Model: gpt-6-sol
----8<---- VERBATIM PROMPT
Context-window: 128000 tokens'
expect 1 'model in legacy assignment cannot satisfy header' '# D-001
---
Model: provider-model-2[1m]'

printf 'companion without metadata\n' > "$scratch/D-001.dispositions.md"
printf 'result without metadata\n' > "$scratch/D-001.result.review.md"
printf 'blank template\n' > "$scratch/D-###.md"
expect 0 'companions and blanks excluded' 'Model: gpt-6-sol
Context-window: 128000 tokens'
printf 'Model: opus\n' > "$scratch/D-002.md"
expect 1 'all numbered prompts checked' 'Model: gpt-6-sol
Context-window: 128000 tokens'

actual=0
sh "$check_dir/model-pinned.sh" "$scratch/missing" > "$scratch/output" 2>&1 || actual=$?
[ "$actual" -eq 2 ] || { cat "$scratch/output"; exit 1; }
passed=$((passed + 1))
printf 'PASS: %s model pin regression cases\n' "$passed"
