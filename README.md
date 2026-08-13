# orckit

an orchestration kit that lives in git and evolves with you

orckit is the process layer for running fleets of coding agents against real
repositories. It turns spoken intent into confirmed problem statements,
supervisors into gated pipelines, code review into terminating adversarial
loops, and every decision into a resumable git ledger.

The kit treats **git as the database**. Your agents' context accrues in a
private companion repository with machine-grade history — commit-per-event,
one writer per file, horrible to read and near-perfect to resume from — while
your code repositories keep human-curated history. Two registers, on purpose.

The kit improves the way software does: every run ends by grading the kit
itself (`EVALS.md`), and grades become pull requests here.

## First step

**Make a private clone of this repository named `<your-user>/orckits`
(WITH AN S).** `create/kits-repo` does this for you; the rest of this
section is the manual shape.

- `orckit` (this repo, public) is the **program**: templates, skills, checks,
  playbooks. Fork it, PR it.
- `orckits` (your clone, private) is the **data**: one directory per run,
  named `<user>/<repo>/<YYYY>-<MM>-<slug>/`, holding that run's instantiated
  templates, ledger, dispatches, results, and scratch. Never PR run context
  upstream — only distilled amendments. And when your runs teach you
  something generic and provable, bring it back.

## What is in the kit

| Directory | What | Consumed by |
|---|---|---|
| `kit/` | The instantiable templates: problem statement, rails, supervisor, goal (re-entry), ledger, questions, deviations, evals, design doc, dispatch pairs | An agent instantiating a run home in your orckits |
| `skills/` | The skills slot — deliberately empty. A kit contains skills, but WHICH skills is unique to the kit, the run of that kit, and the user's overall context. Populate it when you instantiate | Any agent CLI that loads skills |
| `checks/` | The machine-checkable half of the rules, as scripts: porcelain baseline, trailer/footer, ownership subset | Gate verification; CI |
| `playbooks/` | Procedural knowledge that is neither template nor skill: rebasing over squash-merges, adversarial review, the CI-green merge bar | Supervisors and humans |
| `lineage/` | The provenance mechanism: how run digests become kit amendments. The digest slot is deliberately empty — which runs a kit descends from is unique to the user | Kit contributors |

## The lifecycle

1. **Instantiate.** In your private orckits, an agent copies `kit/` into
   `<user>/<repo>/<YYYY>-<MM>-<slug>/`, records the orckit commit sha it
   instantiated from, and fills `PROBLEM.STATEMENT.md` by interviewing you.
   `create/kit` does the copying and the recording; the interview stays yours.
2. **Review the scaffold.** The instantiated plan gets its own adversarial
   review before any code work — plans have bugs too.
3. **Run.** A supervisor session adopts `SUPERVISOR.md`, installs `/goal` as
   its re-entry command, and drives dispatches through gates. Every event is
   a commit in orckits. Sessions can die at any moment; the ledger is the
   only memory.
4. **Land.** Code merges into the target repo through your own curation —
   a squash-merge skill with hash-bound approvals is the proven shape. The
   two histories never mix registers.
5. **Grade.** The run ends with `EVALS.md`: what the kit got right,
   numbered diff-shaped amendments, honest costs. Distill it, sanitize it,
   and bring the amendments here with a `lineage/` entry — this is where
   your kit's evolution and everyone's meet.

## Principles

- **The ledger is the only memory.** Sessions compact; subagents are
  stateless. If it is not in the ledger before your next action, it did not
  happen.
- **Evidence or it did not happen.** A subagent's report is a claim. Gates
  close on artifacts the supervisor re-ran with its own hands — including
  re-executing at least one reviewer repro, and proving a mutation actually
  applied before trusting the tests that "caught" it.
- **Reviews terminate.** Adversarial review is recursive by nature, so it
  must have a base case: an EMPTY findings list is a valid, successful
  outcome. Never re-prompt a reviewer that found nothing. Ceiling three
  remediation rounds, then a human.
- **Context hygiene.** Reviewers get the artifact and the contract — never
  the authoring lineage. Authors defend; reviewers attack; neither sees the
  other's reasoning.
- **Irreversible operations go one at a time.** Force-pushes, retargets, and
  merges are shown — conflict, resolution, evidence — then executed, with a
  pause between. Parallelism is for isolated worktrees.
- **Lead with the blast radius.** When you ask a human to decide, the first
  thing they read is the bounded list of user-observable consequences —
  "that is the whole list" — not mechanism, severity labels, or item numbers.
- **Lint the form; review the truth.** Every rule is tagged by who can check
  it. The machine-checkable half lives in `checks/` and runs at gates; human
  and agent judgment is spent only where judgment is required.

## Status

Lessons flow in through `lineage/`. APIs — file names, section shapes, the
dispatch protocol — are stabilizing but not stable: expect them to move,
and when your runs prove a better shape, move it with us. The kit assumes
git, a POSIX shell, and an agent CLI that can read files and run commands;
nothing else.

## License

MIT
