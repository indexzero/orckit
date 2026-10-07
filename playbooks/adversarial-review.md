# Adversarial review that terminates

Review is the doubt step made structural: CLAIM, EXTRACT, DOUBT, RECONCILE,
STOP. The loop below terminates by construction. It catches what green
suites miss.

## The packet (context hygiene)

A reviewer receives ONLY:
- the ARTIFACT: the full diff against the declared base
- the CONTRACT: the design-item text, any declared interface contract, and
  the RAILS of the run. For a behavior-changing artifact, an explicit
  intended-behavior statement, positive AND negative: what must change, and
  what must not
- the artifact paths it may read

Never the PR body. Never the commit messages. Never the reasoning of the
author. Authors defend. Reviewers attack. An author never reviews its own
output.

## Two reviewers, different blood

1. A FRESH reviewer of the same model family through the CLI. The model is
   pinned, with the context window named, and has a fallback floor.
2. A cross-model reviewer. If its binary is missing or errors, record that
   verbatim. Never skip in silence.

Both prompts carry this text, verbatim:

    An EMPTY findings list is a valid and successful outcome — if genuine
    scrutiny finds nothing, report NO FINDINGS. Do not manufacture findings
    to appear thorough.

Reviewers run in their OWN checkout, or their suite runs are serialized
with the author's. A reviewer that runs e2e in the live worktree of the
author produces phantom flakes. A scratch file of one reviewer trips the
hygiene checks of the other.

## RECONCILE (the half the supervisor does)

Classify every finding by reading the diff again. Never by deferring to the
reviewer OR the author:
- **contract-misread**: the reviewer misread the contract. Explain. Close.
- **actionable**: fix it. The severity decides whether it gates.
- **trade-off**: accepted with a justification. A major gets a human
  sign-off line and forces DRAFT posture until signed.
- **noise**: unreachable or unrealizable. SAY WHY, and verify the why with
  your own hands. A noise classification built on a false factual claim is
  itself a finding. Correct the record even when the verdict survives.

## STOP (the base case)

- A remediation re-review covers ONLY two things: closure of the prior
  findings, and defects the fixes introduced. Never a new full-scope hunt.
- The base case is a scoped re-review with zero new findings and every
  prior closed or signed. The ceiling is three remediation rounds. Then
  BLOCKED, with the finding that did not die and the three attempts.
- Never re-prompt a reviewer that reported NO FINDINGS.
- Audit for silent self-review. A genuine review contains verification work
  absent from the packet: its own repros, greps, mutation probes, or a fact
  the packet never stated. A paraphrase of the claims is not a review.

## Gate-side verification

Before a remediation gate closes, the supervisor runs at least one reviewer
repro again with its own hands. It proves that any mutation applied
(non-empty `git diff --stat`) before it trusts the tests that "caught" it.
A passing suite over an unapplied mutant proves nothing, and it happens
more easily than you think. A regex that matched nothing is enough.
