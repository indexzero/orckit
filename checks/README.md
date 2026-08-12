# checks — the machine-checkable half of the rules

**A check that verifies the kit's own template rules ships with the kit.
A check that verifies a project's rules lives in the run.**

Every rule is tagged by who can check it: lint the form; review the truth.
The rules a script can check run at every gate, so agent and reviewer
attention is spent only where judgment is required. Each check is a small
shell script — arguments in, exit code out, offending evidence on stdout.
Wire them into gate verification, a pre-push hook, or CI. A check that
fails is a gate failure, not a conversation.

## Kit checks (ship here — each enforces a rule the kit itself declares)

| Check | Enforces | Declared in |
|---|---|---|
| `porcelain-baseline.sh <repo> <baseline-file>` | The main checkout's porcelain equals the pinned baseline — no contamination | `kit/RAILS.template.md` rule 3 |
| `trailer-present.sh <repo> <range>` | Every commit in the range ends with the attribution trailer | `kit/RAILS.template.md` rule 13 |
| `no-ai-footer.sh <pr-number>` | The PR body carries no AI-attribution footer | `kit/RAILS.template.md` rule 14 |
| `ownership-subset.sh <repo> <base> <allowed-file...>` | The diff is a subset of the dispatch's ownership list | `kit/dispatches/D-###.md` Scope |

## Run checks (live in your run home, not here)

When a run pays for a project-shaped check — a golden-coverage probe, a
snapshot-workflow spec-list guard, a mutant-applied proof — write it into
the run beside the rule it enforces, following
`example.check.template.sh`: name the rule in the header, take everything
project-specific as arguments, exit nonzero with the evidence on stdout.

We invite the graduation: when nothing project-shaped remains in a run
check — arguments only, house context gone — it was never really yours
alone. Bring it here by PR, citing the digest of the run that bred it
(see `lineage/`).
