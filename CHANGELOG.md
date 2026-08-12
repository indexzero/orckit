# Changelog

## 0.1.0 (2026-08)

- `kit/`: the run templates — problem statement, rails, supervisor, goal,
  ledger, questions, deviations, performance, design doc, and the
  dispatch/result pair.
- `checks/`: the four kit checks (porcelain baseline, trailer, AI footer,
  ownership subset), each enforcing a rule the kit itself declares, plus
  the template for run checks.
- `playbooks/`: rebase-after-squash, adversarial-review, ci-green-bar.
- `lineage/`: the mechanism by which run digests become kit amendments,
  and the digest template.
- `skills/`: the slot, empty by design — a kit contains skills, but which
  skills is unique to the kit, the run, and the user's context.

Run homes instantiated from this kit record this repository's commit sha.
