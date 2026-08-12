# RAILS — template (standing directives binding EVERY agent of a run)

> RAILS is the constitution; SUPERVISOR is the government. Rules that bind
> *every* agent — worktree hygiene, git discipline, review protocol,
> never-touch lists — live in one standing file, repeated verbatim into
> every dispatch and cited by number at every gate. A rule one cannot cite
> by number will not be followed; a rule one cannot amend will be
> overridden in silence. Give the file both properties.

```markdown
# RAILS — standing directives binding EVERY agent of this run (read-only)

They bind the supervisor and every subagent it dispatches. Violations are
gate failures. Repeat §§1–3 verbatim in every dispatch.

Run home: <absolute path in your orckits>
Target repo: <absolute path> (READ-ONLY reference checkout)
Design authority: <the decided plan/proposal — anchors WILL go stale;
re-verify every cited location against branch HEAD before editing; a moved
finding is a re-anchor, a vanished finding is a DEVIATIONS entry, never a
silent improvisation).

## Worktrees / where edits happen

1. Create your worktree with: <the project's worktree command — one that
   runs the repo's pre-start/bootstrap steps; never raw `git worktree add`,
   never the harness's own isolation>.
2. ALL edits happen ONLY inside your worktree. The main checkout is
   READ-ONLY reference. Every subagent brief repeats this rule verbatim.
3. Before finishing: run `git -C <main checkout> status --porcelain` and
   paste the output in your result. The supervisor pins the live baseline
   (an exact list of expected untracked entries) at preflight; new entries
   beyond it are contamination — report it, do NOT "fix" the main checkout
   yourself.

## Fresh-worktree bootstrap

4. <gitignored things a fresh worktree lacks — vendor dirs, generated
   sources — and the exact bootstrap commands. Budget the minutes; never
   symlink shared state from the main checkout.>

## Build / test / goldens

5. Run the unit suites of every package your diff touches, in YOUR
   worktree, raw tails pasted in your result.
6. Build before any e2e/preview run if the harness serves prebuilt output —
   skipping the build silently tests stale code.
7. Visual goldens: <the regeneration ground-truth platform/command>. Commit
   ONLY goldens that genuinely changed; a bulk-regeneration workflow's
   output is never committed wholesale.
7b. A golden claim requires a coverage check: before citing "zero golden
   diffs" as evidence for a surface, verify some golden actually renders
   that surface. Golden silence over an unrendered surface is not evidence.
8. **Behavior preservation is the charter** (when it is): pure refactors
   keep goldens byte-identical and tests passing UNMODIFIED. Sanctioned
   exceptions are enumerated here BY ITEM, never discovered. An unexpected
   golden diff is a finding to investigate, never regen fodder.
9. One simplification per commit; run the suite between commits.

## Rebases (after things land under you)

10. Follow `playbooks/rebase-after-squash.md`: predict conflicts from the
    landed change's UNFILTERED touched-file list; retarget the PR base
    BEFORE force-pushing (a push to a PR with a stale base can trigger NO
    CI); irreversible operations one branch at a time, with the conflict
    and resolution shown and verified before the push.
11. <files that must never be merged, only regenerated — lockfiles,
    generated corpora — and their regeneration commands.>

## Git / PRs

12. NEVER push to the default branch or any shared branch. Push ONLY your
    feature branch.
13. Commit style matches repo history; atomic commits; end every commit
    message with the harness-provided attribution trailer.
14. PR bodies: no AI-attribution footer of any kind (if that is the house
    rule — state the house rule here either way). Reference the design
    authority section that licenses the change.
15. Cite only REAL issue/PR numbers, verified via `gh` before citing.
    Numbers quoted inside code comments may be cited as "per the comment at
    <file:line>" — they may belong to a different numbering space.
16. Gate rule for the PR itself: all track gates PASS → ready; anything
    waived, partial, or unverified → DRAFT.
17. Merge only on green CI on the CURRENT head — including after a
    provably content-identical rebase.

## Reviews (mandatory for every track that produces a diff)

18. Two adversarial reviews of the final diff, both context-hygienic (the
    reviewer gets the diff + the contract — the design-item text + this
    file — never authoring lineage):
    a. a FRESH same-family reviewer via the CLI, model pinned;
    b. a cross-model reviewer (record the binary's absence rather than
       skipping silently).
    Reviewers run against their OWN checkout, or their suite runs are
    serialized with the author's — never concurrent in the author's live
    worktree. Audit both outputs for silent self-review. Blockers: fix
    (ceiling 3) or end BLOCKED. Route each finding against branch HEAD
    before acting.
19. **Reviews terminate.** Prompt every reviewer with, verbatim: "An EMPTY
    findings list is a valid and successful outcome — if genuine scrutiny
    finds nothing, report NO FINDINGS. Do not manufacture findings to
    appear thorough." Re-reviews scope ONLY to (a) prior-finding closure
    and (b) defects introduced by the fixes — never a fresh full-scope
    hunt. Base case: a scoped re-review with zero new findings and all
    priors closed/waived. Never re-prompt a NO FINDINGS reviewer.
20. Repro discipline: when the supervisor re-runs a reviewer's repro or a
    mutation check, it first PROVES the mutation applied (`git diff --stat`
    is non-empty) — a passing suite over an unapplied mutant is vacuous.

## Never commit / never read

21. Never commit to the target repo: anything from this run home, plan
    files, <project-specific untracked-by-design list>. The run home IS
    committable in your orckits.
22. <files/directories no agent may read at all — active human design work,
    private specs.>

## Unattended discipline

23. If the owner is away: never ask. Askable → best assumption, recorded
    under a QUESTIONS heading in your result (impact-if-wrong,
    how-to-override), continue. Owner-only decisions (merges, anything
    destructive/shared) → BLOCKED in your result + stop that thread only.
24. Scratch: <run home>/sslop/<D-id>/ — never /tmp; never delete from it.
25. Do not read/write orchestration/ except your own dispatch + result
    pair; never another agent's scratch.

## Model

26. Pin every model (build agents, review CLIs) with an explicit fallback
    ladder and a floor. If the pinned model is unavailable entirely:
    ledger-record and BLOCK — never silently fall back.

## Amendments

> Owner directives that supersede a numbered rule are APPENDED here by the
> supervisor — never edited into the body — each entry citing the directive
> verbatim and the rule it supersedes. Agents: amendments override the
> body. (Without this section, a superseded rule keeps winning over
> dispatches, because agents read RAILS as the higher authority.)

- (none)
```

## DONE-WHEN (for an instantiation of this template)

- Every `<placeholder>` resolved to project-specific fact; the baseline
  porcelain list is exact, not descriptive.
- §§1–3 are self-contained enough to repeat verbatim in dispatches.
- The sanctioned-exceptions list (rule 8) is enumerated by design-item, or
  states "none".
- The Amendments section exists, even when empty.
