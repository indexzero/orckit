# The CI-green merge bar

**Never squash-merge until ALL checks pass on the CURRENT head of the PR.**
This holds after a rebase or any push that moves the head. It holds even
when the rebase is provably identical in content. A content proof, such as
an own-files diff or a range-diff identity, is evidence for the *gate*. The
green run on the exact head is the bar for the *merge*. Approval of a
commit message is not approval to merge on red.

## Operating it

- After any force-push or retarget: run `gh pr checks <n>`, then
  `gh run watch <id> --exit-status` to completion. A watch is cheap and
  read-only. Run it in the background. Report the terminal state, not a
  prediction.
- **Silent CI is a failure mode, not a pass.** A push to a PR with a stale
  base branch can trigger no run at all. If there are zero check runs
  after five minutes, retarget. Then run `gh pr close/reopen` to trigger
  CI again.
- **Tell a flake from a defect before you rerun.** Read the log of the
  failed job first. The flake signature has three parts. A step fails on third-party
  infrastructure, such as a 503 on a CLI download. The code path is one
  the diff never touches. The same step passed on a sibling PR minutes
  earlier. Then
  `gh run rerun <id> --failed`. Rerun the failed jobs, not the world. Watch
  to green. A failure you did not read is a failure you are guessing
  about.
- **A missing visual baseline masquerades as a test failure.** The
  signature has two parts. The FIRST test that compares a new golden fails
  with "snapshot missing, writing actual". The NEXT one passes against the
  file it wrote. The cure is to generate the platform baselines through the
  regeneration workflow of the project. Make sure that the spec list of
  that workflow includes the new spec. It will not, unless someone added
  it.
