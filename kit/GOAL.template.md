# GOAL command — template (idempotent re-entry point)

> Sessions are mortal; the command is not. Install as
> `.claude/commands/goal.md` (or equivalent) so that compaction, stalls, and
> session loss are recoverable by re-invoking one command. Idempotence is
> the whole point: read the state, verify the claims, advance, persist —
> one re-enters the same way every time, and so cannot be lost.

```markdown
# /goal: Drive <project> to Completion

**Installation:** save as `.claude/commands/goal.md`. Safe to invoke
repeatedly: on session start, after compaction, after any stall, from a hook.

## The goal

COMPLETE when, and only when, every line has a verified evidence path in
`orchestration/STATE.md`:

- [ ] <artifact 1 pinned/passing, evidence path>
- [ ] <suite green from clean checkout>
- [ ] <review file: zero open blockers>
- [ ] <DEVIATIONS.md current; QUESTIONS.md current; BACKLOG holds minors>
- [ ] <final independent verification, raw output on file>
- [ ] <DELIVERY/PERFORMANCE notes written, incl. loop counters spent>

## Procedure (every invocation, in order)

1. **Orient.** Read `orchestration/STATE.md` + tail of `LOG.md`. Absent →
   invocation zero: initialize the ledger, adopt the supervisor instruction,
   begin at P1. Do not re-plan; the plan exists.
2. **Audit before trusting.** The ledger records claims; verify the most
   recent one before building on it (re-run the suite the ledger says is
   green). A claim that fails re-verification is reverted in the ledger with
   a note and the phase reopens. Unverified resumption is the primary
   corruption vector after compaction.
3. **Advance.** Execute STATE.md's next action, or derive it from the
   supervisor pipeline if stale. As many actions as the session allows; no
   per-invocation quota.
4. **Persist relentlessly.** After every dispatch/result/gate: update
   STATE.md before anything else. Assume the session ends without warning.
5. **Terminate correctly.** Exactly two legitimate stops:
   - **COMPLETE** — checklist verified, delivery notes written. Say so, with paths.
   - **BLOCKED** — ceiling hit or human-only decision. The question is on
     file. Say so, with the question inline.

   Everything else is a stall. Prohibited: ending with a progress summary and
   no action taken; asking permission for in-scope work; declaring success on
   partial evidence; deferring long-running work ("can be run later": run it).
```

## DONE-WHEN

- The checklist is evidence-path-shaped (a stranger can verify each line).
- The audit step names the specific re-verification commands for this project.
