# Digest: issue-sweep (2026-10)

> Staged at the scaffold phase. The run has not started. Each amendment
> below names the friction that was live while the run home was written,
> and the evidence that survives sanitization. The run confirms or strikes
> each item at its end, and this digest is then updated in place.

Shape of the run: ten build dispatches planned, one per pre-specified
issue, in seven tracks grouped by file contention. Two reviewers per track:
a same-family CLI reviewer and a cross-model reviewer. Ten draft PRs, each
to leave draft on green CI. No merges by the run. Contamination check:
the empty porcelain baseline. Waived items: none yet.

## Kept on purpose (validated under load)

1. **The pointer-dispatch protocol.** The owner asked to read every
   dispatch before the run began. Because the file is the prompt, there
   was something to read. A compose-in-call design has nothing to show
   before the call.
2. **The scaling decision in the supervisor.** Ten small pre-specified
   items earned no design-review phase. The decision is recorded in one
   paragraph, and the ledger can defend it.
3. **QUESTIONS.md at the moment of assumption.** Four entries were written
   during the scaffold, each with an override. The owner answered one
   before the run started, which is the intended loop.

## Amendments (applied to the kit in this PR)

1. **`kit/RAILS.template.md` rule 26: pin the context window with the
   model.** Friction: the owner directed that every subagent run on a
   1M-context model. The harness subagent tool offered a model alias with
   no window pin, so it could not honor the directive. The run moved every
   subagent to the CLI with an explicit id, and a live probe proved the CLI
   accepts the window suffix. The rule now says that an alias is not a pin.
   It says that the model is tiered by the defect class the suites cannot
   see. The per-item table lives in the design doc. The supervisor
   template gains a Transport section. Use the native subagent facility of
   the harness when it can pin the window and the dispatch fits the life of
   the session. Use a detached CLI process when either fails.
2. **`kit/RAILS.template.md` rule 1: the default branch goes stale in
   silence.** Friction: a prior session in the target repo recorded three
   workers that branched off an eleven-commit-old default branch. Each
   built on the wrong tree with green tests. The rule now has the
   supervisor fast-forward the default branch once at preflight and record
   HEAD. Every subagent compares its worktree HEAD before its first edit. The rule also names the worktree tool, so a raw command cannot
   satisfy it.
3. **`kit/dispatches/D-###.md`: re-anchor is STEP 1 with a recorded
   table.** Friction: every issue in the run cites `file:line` locations
   that were true when written. The template kept re-anchoring as a
   reminder inside VERIFIED FACTS. A reminder is not a gate. The skeleton
   now has STEP 1 with the states HOLDS, MOVED TO, and VANISHED. It also
   has the sentence "Do not edit before this table exists." The result skeleton has the matching
   table.
4. **`kit/LEDGER.template.md`: `PLANNED` status and a branch-stack
   table.** Friction: ten dispatches were written before P0 for the owner
   to read. The registry had no word for a written, unsent prompt. The
   stacked branches had no home in STATE.md. Both now exist in the
   skeleton.
5. **`kit/SUPERVISOR.template.md` section 2: a recorded shape for the
   issue sweep.** Friction: the template said to delete the gates a project
   does not earn. It gave no worked shape. The run had to invent one:
   items are the designs, CI on the head is the clean environment, tracks
   group by file contention, launch gates are "the PR below is open".
   That shape is now a named subsection.
6. **`checks/model-pinned.sh`.** Friction: rule 26 is a form rule a script
   can read, and the run had no script. The check fails any dispatch whose
   Model line lacks an explicit id with a window pin.
7. **The writing rules, adopted by the kit itself.** Friction: the
   instantiated templates carried dashes, semicolons, and sentences over
   25 words into the run files. A measured pass had to remove them from
   seven files and ten dispatches. The kit now has `playbooks/writing-rules.md`,
   RAILS rule 27, `checks/prose-lint.sh`, and a principle in the README.
   Every kit file was rewritten under the rules, so the next instantiation
   starts clean.

## Honesty carried forward

- The run has not run. Items 1 to 6 are guards against failures the kit
  has seen or that the owner named, not failures this run caught. The run
  is the test. If the window pin and the preflight pull prevent nothing
  measurable, this digest must say so at run end.
- The prose check is a lint, not a reading. It cannot see a sentence that
  is short and still unclear. The self-check in the playbook is the half a
  person must do.
- The largest cost center at the scaffold was rewriting prose that the
  templates themselves had taught. Amendment 7 halves that for the next
  run without a weaker gate.
