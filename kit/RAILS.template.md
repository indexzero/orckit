# RAILS: template (standing directives that bind EVERY agent of a run)

> RAILS is the constitution. SUPERVISOR is the government. A rule that binds
> every agent lives in one standing file. That covers worktree hygiene, git
> discipline, the review protocol, and the never-touch lists. The file is
> repeated verbatim into every dispatch and cited by number at every gate.
> A rule an agent cannot cite by number is not obeyed. A rule an agent
> cannot amend is overridden in silence. Give the file both properties.

```markdown
# RAILS: standing directives that bind EVERY agent of this run (read-only)

These rules bind the supervisor and every subagent it dispatches. A
violation is a gate failure. Repeat rules 1 to 3 verbatim in every dispatch.

Run home: <absolute path in your orckits>
Target repo: <absolute path> (READ-ONLY reference checkout)
Design authority: <the decided plan, proposal, or issue>. Anchors WILL go
stale. Before you edit, make sure that each cited location still holds at
branch HEAD. A moved location is a re-anchor. A vanished location is a
DEVIATIONS entry. Never improvise in silence.

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

## Build, test, and goldens

5. Run the unit suites of every package your diff touches, in YOUR
   worktree. Paste the raw tails in your result.
6. If the harness serves prebuilt output, build before any e2e or preview
   run. A skipped build tests stale code in silence.
7. Visual goldens: <the regeneration platform and command that are ground
   truth>. Commit ONLY the goldens that changed. Never commit the output of
   a bulk regeneration wholesale.
7b. A golden claim needs a coverage check. Before you cite "zero golden
   diffs" for a surface, make sure that some golden renders that surface.
   Golden silence over a surface no golden renders is not evidence.
8. **Behavior preservation is the charter** (when it is). A pure refactor
   keeps goldens byte-identical and keeps every test passing UNMODIFIED.
   Sanctioned exceptions are listed here BY ITEM, never discovered. An
   unexpected golden diff is a finding to investigate. It is never a
   reason to regenerate.
9. One simplification per commit. Run the suite between commits.

## Rebases, after things land under you

10. Obey `playbooks/rebase-after-squash.md`. Predict conflicts from the
    UNFILTERED touched-file list of the landed change. Retarget the PR base
    BEFORE a force-push. A push to a PR with a stale base can trigger NO
    CI. Do irreversible operations one branch at a time. Show the conflict
    and the resolution. Verify them before the push.
11. <The files that must never be merged by hand, only regenerated, such as
    lockfiles and generated corpora, with their regeneration commands.>

## Git and PRs

12. NEVER push to the default branch or to any shared branch. Push ONLY
    your feature branch.
13. Commit style matches the repo history. Make atomic commits. End every
    commit message with the attribution trailer that the harness provides.
14. PR bodies carry no AI-attribution footer of any kind, if that is the
    house rule. State the house rule here either way. Reference the design
    authority section that licenses the change.
15. Cite only REAL issue and PR numbers. Verify each with `gh` before you
    cite it. A number quoted inside a code comment can be cited as "per
    the comment at <file:line>". It can belong to a different numbering
    space.
16. Gate rule for the PR itself: if all track gates PASS, mark the PR
    ready. If anything is waived, partial, or unverified, keep it DRAFT.
17. Merge only on green CI on the CURRENT head. This holds after a rebase
    too, even one with identical content.

## Reviews, mandatory for every track that produces a diff

18. Run two adversarial reviews of the final diff. Both are
    context-hygienic. A reviewer gets the diff and the contract, that is
    the design-item text and this file. A reviewer never gets the authoring
    lineage.
    a. A FRESH reviewer of the same model family through the CLI, model
       pinned.
    b. A cross-model reviewer. If its binary is absent, record that. Never
       skip in silence.
    Reviewers run against their OWN checkout, or their suite runs are
    serialized with the author's. Never concurrent in the live worktree of
    the author. Audit both outputs for silent self-review. If a reviewer
    finds a blocker, fix it, with a ceiling of three rounds, or end the
    thread as BLOCKED. Route each finding against branch HEAD before you
    act on it.
19. **Reviews terminate.** Give every reviewer this prompt, verbatim:

        An EMPTY findings list is a valid and successful outcome — if
        genuine scrutiny finds nothing, report NO FINDINGS. Do not
        manufacture findings to appear thorough.

    A re-review covers ONLY two things: closure of the prior findings, and
    defects that the fixes introduced. It is never a new full-scope hunt.
    The base case is a scoped re-review with zero new findings and every
    prior closed or waived. Never re-prompt a reviewer that reported NO
    FINDINGS.
20. Repro discipline: when the supervisor re-runs a repro or a mutation
    check from a reviewer, it first PROVES that the mutation applied. That
    means `git diff --stat` is not empty. A passing suite over a mutation
    that was not applied proves nothing.

## Never commit, never read

21. Never commit to the target repo: anything from this run home, plan
    files, <the project-specific list of files untracked by design>. The
    run home IS committable in your orckits.
22. <The files and directories no agent may read at all: active human
    design work, private specs.>

## Unattended discipline

23. If the owner is away, never ask. If an item is askable, make the best
    assumption. Record it under a QUESTIONS heading in your result, with
    the impact if wrong and the way to override. Continue. If a decision
    belongs to the owner alone, such as a merge or any destructive or
    shared action, write BLOCKED in your result and stop that thread only.
24. Scratch lives at `<run home>/sslop/<D-id>/`. Never use `/tmp`. Never
    delete from scratch.
25. Do not read or write `orchestration/`, except your own dispatch and
    result pair. Never read the scratch of another agent.

## Model

26. Pin every model: build agents and review CLIs. Record the exact model
    id in `Model:` and the effective window in `Context-window: <integer> tokens`.
    A supported model suffix such as `[1m]` also names the window.
    Record the window's source and the reasoning setting in the ledger.
    An alias such as `opus`, `auto`, or `latest` is not a pin.
    Verify the available window from the host or current provider documentation.
    Never invent a suffix or infer the window from the model family.
    A metadata field records capacity. It does not configure capacity.
    If the required capacity cannot be verified, record BLOCKED.
    Use a transport that can select the model and meet that capacity.
    See SUPERVISOR section 1, Transport. Give each pin a fallback ladder
    and a floor. Tier the model by the defect class the suites cannot see,
    and record the per-item table in the design doc. If a pinned model is
    not available at all, record that in the ledger and BLOCK. Never fall
    back in silence. `checks/model-pinned.sh` checks the declaration format.
    The supervisor verifies availability and capacity at dispatch time.

## Writing

27. Write every run artifact in Simplified Technical English. That covers
    this file, the supervisor, dispatches, results, ledger entries,
    questions, deviations, commit bodies, and PR bodies. The rules are in
    `playbooks/writing-rules.md`. `checks/prose-lint.sh` reads the half a
    machine can read. Commands, identifiers, paths, and quoted prompts are
    exempt and stay exact.

## Amendments

> An owner directive that supersedes a numbered rule is APPENDED here by
> the supervisor. It is never edited into the body. Each entry cites the
> directive verbatim and the rule it supersedes. Agents: an amendment
> overrides the body. Without this section, a superseded rule keeps winning
> over dispatches, because agents read RAILS as the higher authority.

- (none)
```

## DONE-WHEN (for an instantiation of this template)

- Every `<placeholder>` resolves to a project-specific fact. The baseline
  porcelain list is exact, not descriptive.
- Rules 1 to 3 are self-contained enough to repeat verbatim in dispatches.
- The sanctioned-exceptions list in rule 8 is enumerated by design item, or
  states "none".
- Rule 26 names the window pin per tier, and rule 27 names the writing
  rules.
- The Amendments section exists, even when empty.
