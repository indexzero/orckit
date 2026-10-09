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

