# Adversarial review that terminates

Review is the doubt step made structural: CLAIM → EXTRACT → DOUBT →
RECONCILE → STOP. The loop below terminates by construction, and it
catches what green suites miss.

## The packet (context hygiene)

Reviewers receive ONLY:
- the ARTIFACT: the full diff against the declared base;
- the CONTRACT: the design-item text, any declared interface contract, and
  the run's RAILS — for a behavior-changing artifact, an explicit
  intended-behavior statement (positive AND negative: what must change,
  what must not);
- artifact paths they may read.

Never the PR body, never commit messages, never the author's reasoning.
Authors defend; reviewers attack. An author never reviews its own output.

## Two reviewers, different blood

1. A FRESH same-family reviewer via the CLI, model pinned with a fallback
   floor.
2. A cross-model reviewer. If its binary is missing or errors, record that
   verbatim rather than skipping silently.

Both prompts carry, verbatim: **"An EMPTY findings list is a valid and
successful outcome — if genuine scrutiny finds nothing, report NO FINDINGS.
Do not manufacture findings to appear thorough."**

Reviewers run in their OWN checkout, or their suite runs are serialized
with the author's. A reviewer executing e2e in the author's live worktree
produces phantom flakes; a reviewer's scratch file trips the other
reviewer's hygiene checks.

## RECONCILE (the supervisor's half)

Classify every finding by re-reading the diff — never by deferring to the
reviewer OR the author:
- **contract-misread** — the reviewer misread the contract; explain, close.
- **actionable** — fix it; severity decides whether it gates.
- **trade-off** — accepted with justification; majors get a human sign-off
  line and force DRAFT posture until signed.
- **noise** — unreachable or unrealizable; SAY WHY, and verify the why with
  your own hands (a noise classification built on a false factual claim is
  itself a finding — correct the record even when the verdict survives).

## STOP (the base case)

- Remediation re-reviews scope ONLY to (a) prior-finding closure and
  (b) defects introduced by the fixes — never a fresh full-scope hunt.
- Base case: a scoped re-review with zero new findings and all priors
  closed or signed. Ceiling: three remediation rounds, then BLOCKED with
  the finding that will not die and the three attempts.
- Never re-prompt a reviewer that reported NO FINDINGS.
- Audit for silent self-review: a genuine review contains verification work
  absent from the packet (its own repros, greps, mutation probes, a fact
  the packet never stated). A paraphrase of the claims is not a review.

## Gate-side verification

Before a remediation gate closes, the supervisor re-runs at least one
reviewer repro with its own hands — and proves any mutation actually
applied (non-empty `git diff --stat`) before trusting the tests that
"caught" it. A passing suite over an unapplied mutant is vacuous, and it
happens more easily than you think (a regex that matched nothing).
