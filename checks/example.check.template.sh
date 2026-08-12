#!/bin/sh
# <name>.sh — <one line: the rule this check makes enforceable>
#
# Verifies: <the RAILS rule number or dispatch clause, quoted short>
# Usage:    <name>.sh <arg> <arg...>
#           Everything project-specific is an argument — paths, baselines,
#           allowed lists. A check with a hardcoded project fact is a run
#           check forever.
# Exit:     0 = the rule holds; nonzero = violation, with the offending
#           evidence on stdout (the evidence IS the report; a bare exit
#           code makes the gate argue).
#
# A check that fails is a gate failure, not a conversation. When nothing
# project-shaped remains in this file, it was never really yours alone —
# bring it to the kit by PR, citing the digest of the run that bred it
# (see lineage/).
set -eu

# 1. Gather the facts (git, gh, the filesystem — never memory).
# 2. Compare against the rule.
# 3. On violation: print the offending evidence, exit 1.
exit 0
