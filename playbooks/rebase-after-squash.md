# Rebasing children after a squash-merge

Squash-merging a parent rewrites its commits. Every child branch cut from
that parent still carries the originals, so the child's PR diff drags the
parent's ghost changes until one rebases past them. Follow the sequence in
order; it loses nothing.

## Per branch — never batched

Irreversible operations (force-push, retarget, merge) go **one branch at a
time**, each as a presented step: show the conflict and resolution, run the
proofs, push, pause. A loop over branches silently drops proof steps and
ships hand-resolved conflicts unshown. Parallelism is for isolated
worktrees, not shared refs.

1. **Rebase past the old parent:**
   `git rebase --onto origin/<default> <old-parent-head> <child-branch>`
2. **On conflict:** stop and look. Resolve with the file editor (not inline
   scripting), and prefer compositions pre-written in the dispatch ("their
   loop shape + our lookup"). If a hunk needs judgment beyond
   keep-both-composes, abort and escalate — a rebase is not the place to
   design.
3. **Prove the rebase changed nothing of the branch's own:**
   - If the new base did NOT advance the branch's files:
     `git diff <pre> <post> -- <its files>` must be EMPTY.
   - If it did (the diff "includes main's own advance"): use patch identity
     instead — `git range-diff <oldbase>..<pre> origin/<default>..<post>`;
     every commit `=`, or deltas confined to context lines around resolved
     hunks.
4. **Verify locally** (suite + checks) BEFORE pushing.
5. **Retarget the PR base BEFORE force-pushing.** A force-push to a PR still
   pointing at a stale base branch can trigger **no CI run at all** — zero
   check-runs, indefinitely. If CI is silent five minutes after a push:
   `gh pr close <n> && gh pr reopen <n>` re-triggers it (`reopened` is a
   default trigger). The close/reopen drops a draft flag; restore it.
6. **Push with `--force-with-lease`**, never bare `--force`.
7. **Merge only on green CI on the new head** — approval of a message is not
   approval to merge on red, and a content-identical rebase still re-runs CI.

## Never merge, always regenerate

Some files auto-merge silently wrong (lockfiles, generated corpora/indices).
List them in RAILS with their regeneration commands; on any rebase that
touches them, reset to base and regenerate instead of resolving.

## Two-lineage children

A branch that textually needs TWO unmerged parents gets a pushed
**integration base**: build the merge with plumbing
(`git merge-tree --write-tree A B` → `git commit-tree <tree> -p A -p B`),
push it as its own branch, and open the child's PR against it — the PR diff
then shows only the child's work. After both parents land, rebase the child
onto the default branch and retarget; the integration branch is disposable.
Works only when the parents' files are disjoint; verify with `merge-tree`
first.
