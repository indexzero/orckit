## 2. Pipeline (parameterize it, and delete the gates the project does not earn)

- **P1 design review.** A fresh adversarial reviewer attacks the design
  doc. Gate G1: zero open blockers. Remediation loop ceiling 3. Pin
  DESIGN-FINAL.
- **P2 build.** One dispatch per component, in dependency order. Each gets
  DESIGN-FINAL and the interfaces of the built components (READMEs, not
  transcripts). Embed VERIFIED FACTS about external dependencies in the
  dispatch. Fetch first. Memory of external tools drifts, and dispatches
  die of it. Gate G2: clean install and the suite green, run again by the
  supervisor with its own hands.
- **P3 adversarial code review.** A fresh reviewer, generous runtime, a
  findings file. Gate G3: zero open blockers. Remediation loop ceiling 3.
  Each fix is verified by a named regression and the full suite. Reviewers
  run against their OWN checkout, or their suite runs are serialized with
  the author's. A reviewer that runs e2e in the live worktree of the author
  produces phantom flakes and scratch-file contamination. When a repro or a
  mutation check is run again at the gate, first PROVE that the mutation
  applied (non-empty `git diff --stat`). A green suite over an unapplied
  mutant proves nothing.
- **P4 final verification.** An independent verifier, a clean clone, raw
  output. Gate G4, DONE: the verifier is green and the DELIVERY notes are
  written, INCLUDING the loop counters spent and the waived majors. The
  cost of convergence is part of the report.

