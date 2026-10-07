# GOAL command: template (idempotent re-entry point)

> Sessions are mortal. The command is not. Install it as
> `.claude/commands/goal.md` or the equivalent, so that a compaction, a
> stall, or a lost session is recovered by one command. Idempotence is the
> whole point. Read the state. Verify the claims. Advance. Persist. One
> re-enters the same way every time, and so cannot be lost.

```markdown
# /goal: Drive <project> to Completion

**Installation:** save as `.claude/commands/goal.md`. Safe to invoke
repeatedly: on session start, after compaction, after any stall, from a
hook.

## The goal

COMPLETE when, and only when, every line has a verified evidence path in
`orchestration/STATE.md`:

- [ ] <artifact 1 pinned or passing, with its evidence path>
- [ ] <suite green from a clean checkout>
- [ ] <review file: zero open blockers>
- [ ] <DEVIATIONS.md current. QUESTIONS.md current. BACKLOG holds the minors.>
- [ ] <final independent verification, raw output on file>
- [ ] <DELIVERY or EVALS notes written, including the loop counters spent>

## Procedure (every invocation, in order)

1. **Orient.** Read `orchestration/STATE.md` and the tail of `LOG.md`. If
   they are absent, this is invocation zero: initialize the ledger, adopt
   the supervisor instruction, begin at P1. Do not re-plan. The plan
   exists.
2. **Audit before you trust.** The ledger records claims. Verify the most
   recent one before you build on it. Run the suite the ledger says is
   green. A claim that fails is reverted in the ledger with a note, and its
   phase reopens. Unverified resumption is the primary corruption vector
   after a compaction.
3. **Advance.** Execute the next action in STATE.md. If it is stale,
   derive it from the supervisor pipeline. Take as many actions as the
   session allows. There is no per-invocation quota.
4. **Persist without pause.** After every dispatch, result, and gate,
   update STATE.md before anything else. Assume that the session ends
   without warning.
5. **Terminate correctly.** There are exactly two legitimate stops:
   - **COMPLETE.** The checklist is verified and the delivery notes are
     written. Say so, with paths.
   - **BLOCKED.** A ceiling is hit, or a decision belongs to a human. The
     question is on file. Say so, with the question inline.

   Everything else is a stall. Four things are prohibited:
   - ending with a progress summary and no action
   - asking permission for in-scope work
   - declaring success on partial evidence
   - deferring work that can run now
```

## DONE-WHEN

- The checklist is evidence-path-shaped. A stranger can verify each line.
- The audit step names the specific re-verification commands for this
  project.
