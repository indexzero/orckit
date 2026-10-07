# Changelog

## Unreleased

- Add a run `AGENTS.md` entry point and a Codex setup playbook.
- Make re-entry, skill loading, and fresh dispatch setup explicit across hosts.
- Accept provider-neutral model and context declarations. Remove implicit
  Claude window defaults. Exclude dispatch companions from the model check.
  Add offline regression coverage.

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
