# checks: the half of the rules a machine can check

**A check that verifies a template rule of the kit ships with the kit. A
check that verifies a rule of one project lives in the run.**

Every rule is tagged by who can check it. Lint the form. Review the truth.
The rules a script can check run at every gate, so agent and reviewer
attention goes only where judgment is needed. Each check is a small shell
script. Arguments go in. An exit code comes out. The offending evidence
goes to stdout. Wire them into gate verification, a pre-push hook, or CI.
A check that fails is a gate failure, not a conversation.

## Kit checks (they ship here, and each enforces a rule the kit declares)

| Check | Enforces | Declared in |
|---|---|---|
| `porcelain-baseline.sh <repo> <baseline-file>` | The porcelain of the main checkout equals the pinned baseline. No contamination. | `kit/RAILS.template.md` rule 3 |
| `trailer-present.sh <repo> <range>` | Every commit in the range ends with the attribution trailer | `kit/RAILS.template.md` rule 13 |
| `no-ai-footer.sh <pr-number>` | The PR body carries no AI-attribution footer | `kit/RAILS.template.md` rule 14 |
| `ownership-subset.sh <repo> <base> <allowed-file...>` | The diff is a subset of the ownership list of the dispatch | `kit/dispatches/D-###.md` Scope |
| `model-pinned.sh <dispatch-dir>` | Every dispatch names a model with its context window pinned | `kit/RAILS.template.md` rule 26 |
| `prose-lint.sh <file...>` | Prose obeys the writing rules: no semicolons, no dash punctuation, no "should", no contractions, sentences within the word limit | `kit/RAILS.template.md` rule 27, `playbooks/writing-rules.md` |

## Run checks (live in your run home, not here)

Some checks are project-shaped: a golden-coverage probe, a
snapshot-workflow spec-list guard, a mutant-applied proof. When a run pays
for one, write it into the run beside the rule it enforces. Use
`example.check.template.sh` as the shape. Name the rule in the header.
Take everything project-specific as an argument. Exit nonzero with the
evidence on stdout.

We invite the graduation. When nothing project-shaped remains in a run
check, that is arguments only and house context gone, it was never only
yours. Bring it here by PR. Cite the digest of the run that bred it (see
`lineage/`).
