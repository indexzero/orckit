# The CI-green merge bar

**Never squash-merge until ALL checks pass on the PR's CURRENT head** —
including after a rebase or any push that moves the head, and even when the
rebase is provably content-identical. Content proofs (own-files diffs,
range-diff identity) are evidence for the *gate*; the green run on the
exact head is the bar for the *merge*. Approval of a commit message is not
approval to merge on red.

## Operating it

- After any force-push or retarget: `gh pr checks <n>`, then
  `gh run watch <id> --exit-status` to completion. Watches are cheap and
  read-only; run them in the background and report the terminal state, not
  a prediction.
- **Silent CI is a failure mode, not a pass.** A push to a PR with a stale
  base branch can trigger no run at all. Zero check-runs after five
  minutes → retarget, then `gh pr close/reopen` to re-trigger.
- **Distinguish flake from defect before rerunning.** Read the failed job's
  log first. The flake signature: a step failing on third-party
  infrastructure (a 503 downloading a CLI), on a code path the diff never
  touches, that passed on a sibling PR minutes earlier. Then
  `gh run rerun <id> --failed` — rerun failed jobs, not the world — and
  watch to green. A failure you did not read is a failure you are guessing
  about.
- **Missing visual baselines masquerade as test failures.** The signature:
  the FIRST test comparing a new golden fails ("snapshot missing, writing
  actual") and the NEXT one passes against the file it just wrote. The
  cure is generating the platform baselines through the project's
  regeneration workflow — and checking that workflow's spec list actually
  includes the new spec, which it will not unless someone added it.
