# orckit

An orchestration kit that lives in git and evolves with you.

orckit is the process layer for fleets of coding agents that work against
real repositories. It turns spoken intent into a confirmed problem statement.
It turns a supervisor into a gated pipeline. It turns code review into an
adversarial loop that terminates. It turns every decision into a git ledger
that a new session can resume from.

The kit treats **git as the database**. The context of your agents accrues
in a private companion repository with machine-grade history: one commit per
event, one writer per file. That history is hard to read and easy to resume
from. Your code repositories keep human-curated history. The two registers
are separate on purpose.

The kit improves the way software does. Every run ends with a grade of the
kit itself (`EVALS.md`). Grades become pull requests here.

## First step

**Make a private clone of this repository named `<your-user>/orckits`, WITH
AN S.** `create/kits-repo` does this for you. The rest of this section is
the manual shape.

- `orckit`, this public repo, is the **program**: templates, skills, checks,
  playbooks. Fork it. Send pull requests.
- `orckits`, your private clone, is the **data**: one directory per run,
  named `<user>/<repo>/<YYYY>-<MM>-<slug>/`. It holds the instantiated
  templates, the ledger, the dispatches, the results, and the scratch of
  that run. Never send run context upstream. Send only distilled
  amendments. When a run teaches you something generic and provable, bring
  it back here.

## What is in the kit

| Directory | What | Consumed by |
|---|---|---|
| `kit/` | Markdown recipes for the run templates, with reusable content under `fragments/{charter,workflow,delivery,trust,rules}/` | `create/kit` composes these into a run home |
| `skills/` | The skills slot. It is empty on purpose. A kit contains skills, but WHICH skills is unique to the kit, the run, and the user. Fill it at instantiation | Any agent CLI that loads skills |
| `checks/` | The half of the rules a machine can check, as scripts: porcelain baseline, trailer, footer, ownership subset, model pin, prose | Gate verification. CI |
| `playbooks/` | Procedures that are neither template nor skill: rebases over squash merges, adversarial review, the CI-green merge bar, the writing rules | Supervisors and humans |
| `lineage/` | The provenance mechanism: how run digests become kit amendments. The digest slot is empty on purpose. Which runs a kit descends from is unique to the user | Kit contributors |

## The lifecycle

1. **Instantiate.** In your private orckits, an agent composes `kit/` into
   `<user>/<repo>/<YYYY>-<MM>-<slug>/`. It records the orckit commit sha it
   came from. It fills `PROBLEM.STATEMENT.md` by interviewing you.
   `create/kit` renders the templates and records their source inputs.
   The interview stays yours.
2. **Review the scaffold.** The instantiated plan gets its own adversarial
   review before any code work. Plans have bugs too.
3. **Run.** A supervisor session adopts `SUPERVISOR.md`, uses `GOAL.md` as
   its re-entry procedure, and drives dispatches through gates. Every event
   is a commit in orckits. A session can die at any moment. The ledger is
   the only memory.
4. **Land.** Code merges into the target repo through your own curation. A
   squash-merge skill with hash-bound approvals is the proven shape. The
   two histories never mix registers.
5. **Grade.** The run ends with `EVALS.md`: what the kit got right,
   numbered diff-shaped amendments, honest costs. Distill it. Sanitize it.
   Bring the amendments here with a `lineage/` entry. This is where the
   evolution of your kit and everyone's kit meet.

## Composing a kit

[kit.example.json](kit.example.json) binds responsibilities to Markdown
fragments. Its five groups follow [CONSTITUTION.md](CONSTITUTION.md).
Each binding is a relative file path or an ordered list of paths.
Paths in the manifest resolve from the manifest's directory.

The current templates are composition recipes. For example,
`kit/dispatches/D-###.md` contains `@trust.supervisor_ledger`, and
`kit/dispatches/D-###.result.md` contains `@trust.delivery_ledger`.
The referenced formats belong to their respective ledgers. Policy fragments
define the instructions that those records capture during execution.

Render a recipe or validate the bindings with Python 3.9 or later:

```sh
python3 create/compose.py kit/RAILS.template.md
python3 create/compose.py --check
python3 checks/composition.test.py
```

A standalone `@charter.completion_contract` line includes the selected
fragment. A standalone `@./cost-analysis.md` line includes a physical file
relative to the containing document. Both forms can nest. Only the five
constitution groups are responsibility namespaces. Indented references and
`@@` lines remain literal. References are textual directives, including
inside the Markdown fences used by the existing templates.

The renderer preserves inclusion order and permits shared fragments in
different branches. Missing bindings, missing files, cycles, and references
outside the manifest directory fail with a source location. It does not
substitute placeholders or execute workflow steps.

Change a binding to select another fragment. Workflow bindings can select
the same fragments as Rules defaults or supply a different file. Bindings
are explicit. The renderer does not infer inheritance or resolve conflicting
policies. Some legacy recipes use physical references to preserve the
placement of parts of a responsibility. Those references select that file
directly and do not follow a replacement manifest binding.

`create/kit` requires Git, jq, and Python 3.9 or later. Interactive use also
requires gum. It renders the recipes before creating the run home, retains
fragment sources, and records the manifest and renderer in provenance.
The generated `kit.json` includes bindings relative to the run home.
Rendered templates are snapshots: editing source fragments later does not
rewrite existing run instructions or issued dispatches.

The initial extraction retains the current instructions and numbered rules.
The rendered content was compared against all 14 existing templates.
Identity, provenance, dependency, and backlog fragments also expose concerns
that previously appeared only in the generator or in layout descriptions.

## Using Codex

Follow [the Codex playbook](playbooks/codex.md) for launch commands, skill
discovery, model pins, and fresh reviewer sessions. New run homes include
an `AGENTS.md` entry point. To resume from a target worktree, tell Codex:

```text
Read /absolute/path/to/private/run/AGENTS.md and resume this run as supervisor.
```

The same ledger and dispatch files work with Claude Code. Command wrappers
and skill installation belong to the host. The run records which host
capabilities each dispatch requires.

## Principles

- **The ledger is the only memory.** Sessions compact. Subagents are
  stateless. If it is not in the ledger before your next action, it did
  not happen.
- **Evidence, or it did not happen.** A report from a subagent is a claim.
  A gate closes on artifacts the supervisor ran again with its own hands.
  That includes one reviewer repro, and proof that a mutation applied
  before the tests that "caught" it count.
- **Reviews terminate.** Adversarial review is recursive by nature, so it
  must have a base case. An EMPTY findings list is a valid, successful
  outcome. Never re-prompt a reviewer that found nothing. The ceiling is
  three remediation rounds, then a human.
- **Context hygiene.** A reviewer gets the artifact and the contract, never
  the authoring lineage. Authors defend. Reviewers attack. Neither sees the
  reasoning of the other.
- **Irreversible operations go one at a time.** A force-push, a retarget,
  or a merge is shown with its conflict, its resolution, and its evidence.
  Then it runs. Then a pause. Parallelism is for isolated worktrees.
- **Lead with the blast radius.** When you ask a human to decide, open
  with the bounded list of consequences a user can observe. End that list
  with "that is the whole list." Mechanism, severity labels, and item
  numbers come after.
- **Lint the form. Review the truth.** Every rule is tagged by who can
  check it. The half a machine can check lives in `checks/` and runs at
  gates. Human and agent judgment is spent only where judgment is needed.
- **Write for a tired reader.** Every run artifact is a procedure for a
  reader that cannot ask questions. The kit writes in Simplified Technical
  English: short sentences, one word per meaning, active voice, condition
  before command, no `should`. See `playbooks/writing-rules.md`.

## Status

Lessons flow in through `lineage/`. The APIs, that is file names, section
shapes, and the dispatch protocol, are stabilizing but not stable. Expect
them to move. When your runs prove a better shape, move it with us. The kit
uses git, a POSIX shell, and an agent CLI that can read files and run
commands. Scaffolding dependencies are listed under Composing a kit.

## License

MIT
