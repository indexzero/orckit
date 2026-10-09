### A recorded shape: the issue sweep

Some work is N small, independent, pre-specified items. An example is a
set of issues that each carry acceptance criteria, verification steps, and
a file list. For that work the pipeline scales down like this. The items ARE the designs,
so P1 becomes a re-anchor step inside each build dispatch (see
`kit/dispatches/D-###.md`, STEP 1). CI on the PR head is the clean
environment, so P4 becomes "all jobs green on the current head". Tracks
group by file contention. Items in one track run in sequence on stacked
branches, each worktree based on the branch below it. A launch gate is
"the PR below is open". Record the stack as a table in STATE.md. Record
the scaling decision in section 1 of the instantiated supervisor.

