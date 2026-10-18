## Worktrees and where edits happen

1. Create worktrees with <the worktree tool of the project> and with
   nothing else. The tool must run the pre-start and bootstrap steps of the
   repo. Never use raw `git worktree add`. Never use the isolation feature
   of the harness. The default branch of the target goes stale in silence,
   and workers then build on the wrong tree. So, before the first worktree,
   the supervisor runs this once at preflight:
   `git -C <main checkout> pull --ff-only origin <default>`
   The supervisor records the resulting HEAD sha in `orchestration/STATE.md`.
   Then create your worktree with:
   <the exact command, with its base branch>
   Before you edit, make sure that `git -C <worktree> rev-parse --short HEAD`
   equals the recorded sha. For a stacked item, it must equal the tip of
   the branch the dispatch names as base. If it does not, stop and write
   BLOCKED.
2. ALL edits happen ONLY inside your worktree. The main checkout is a
   READ-ONLY reference. Every subagent brief repeats this rule verbatim.
3. Before you finish, run `git -C <main checkout> status --porcelain` and
   paste the output in your result. At preflight the supervisor pins the
   live baseline, which is an exact list of the expected untracked entries.
   Any entry beyond it is contamination. Report it. Do NOT repair the main
   checkout yourself.

## Bootstrap of a new worktree

4. <The gitignored things a new worktree lacks, such as vendor directories
   and generated sources, and the exact bootstrap commands. Budget the
   minutes. Never symlink shared state from the main checkout.>

