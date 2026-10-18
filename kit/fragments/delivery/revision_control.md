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

