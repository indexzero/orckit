# Run entry point

This directory is a private orckit run home. Resolve paths from this
directory, even when the target checkout is the working directory.

## Supervisor

When asked to start or resume this run, read `PROBLEM.STATEMENT.md`,
`RAILS.md`, `SUPERVISOR.md`, and `GOAL.md`. Follow the procedure in `GOAL.md`.
Read `orchestration/STATE.md` and `orchestration/LOG.md` if they exist.

If the scaffold still contains placeholders, finish instantiation first.
Use `LEDGER.md` to create the ledger files. Resolve all artifact paths in
the run instructions. Confirm the problem statement when the owner is present.
Review the scaffold before dispatching code work.

## Dispatched worker or reviewer

When given a dispatch pointer, read that file and follow its assignment.
Read only the run artifacts the dispatch allows. Do not adopt the
supervisor role or read its ledger. Write the result beside the dispatch.

## Shared rules

Keep run context in this private repository. Keep target code changes in
the worktree named by the dispatch. Follow target repository instructions
as well as the run rails. Record conflicts before affected work continues.

The skills index records dependencies. It does not install or load skills.
Verify that required skills and tools are available before dispatch.

Run instructions do not override host permissions or higher-priority
instructions. Record unavailable capabilities and the affected gate.
