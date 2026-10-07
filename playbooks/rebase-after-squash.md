# Rebasing children after a squash-merge

A squash-merge of a parent rewrites its commits. Every child branch cut from
that parent still carries the originals. The PR diff of the child drags the
ghost changes of the parent until one rebases past them. Obey the sequence
in order. It loses nothing.

## Per branch, never batched

An irreversible operation (force-push, retarget, merge) goes **one branch at
a time**. Each one is a presented step. Show the conflict and the
resolution. Run the proofs. Push. Pause. A loop over branches drops proof steps in
silence and ships hand-resolved conflicts unshown. Parallelism is for
isolated worktrees, not shared refs.

1. **Rebase past the old parent:**
   `git rebase --onto origin/<default> <old-parent-head> <child-branch>`
2. **On conflict, stop and look.** Resolve with the file editor, not inline
   scripting. Prefer the compositions pre-written in the dispatch ("their
   loop shape plus our lookup"). If a hunk needs judgment beyond
   keep-both-composes, abort and escalate. A rebase is not the place to
   design.
3. **Prove that the rebase changed nothing of the branch's own:**
   - If the new base did NOT advance the files of the branch:
     `git diff <pre> <post> -- <its files>` must be EMPTY.
   - If it did (the diff "includes the own advance of main"): use patch
     identity instead. `git range-diff <oldbase>..<pre> origin/<default>..<post>`.
     Every commit is `=`, or the deltas are confined to context lines around
     resolved hunks.
4. **Verify locally** (suite and checks) BEFORE you push.
5. **Retarget the PR base BEFORE the force-push.** A force-push to a PR that
   still points at a stale base branch can trigger **no CI run at all**.
   That means zero check runs, indefinitely. If CI is silent five minutes
   after a push, run `gh pr close <n> && gh pr reopen <n>`. That triggers
   CI again, because `reopened` is a default trigger. The close and reopen
   drops a draft flag. Restore it.
6. **Push with `--force-with-lease`**, never bare `--force`.
7. **Merge only on green CI on the new head.** Approval of a message is not
   approval to merge on red. A content-identical rebase still runs CI
   again.

## Never merge, always regenerate

Some files auto-merge wrong in silence: lockfiles, generated corpora,
indices. List them in RAILS with their regeneration commands. On any rebase
that touches them, reset to base and regenerate instead of resolving.

## Two-lineage children

A branch that textually needs TWO unmerged parents gets a pushed
**integration base**. Build the merge with plumbing
(`git merge-tree --write-tree A B`, then `git commit-tree <tree> -p A -p B`).
Push it as its own branch. Open the PR of the child against it. The PR diff
then shows only the work of the child. After both parents land, rebase the
child onto the default branch and retarget. The integration branch is
disposable. This works only when the files of the parents are disjoint.
Verify that with `merge-tree` first.
