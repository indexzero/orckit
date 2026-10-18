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

