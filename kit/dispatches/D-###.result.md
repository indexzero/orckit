# D-###.result.<shortname>.md — result file template (spine + kind variants)

> The spine below is mandatory and identical for every kind; the variant
> sections are a starter vocabulary, and new shortnames are explicitly
> licensed — shape-variance in results carries real value, so give it room.
> The file lives beside its dispatch as
> `dispatches/D-###.result.<shortname>.md`, so one scanning `ls` sees
> prompt and result side by side.

## The invariant spine (every result, every kind)

```markdown
# D-### result — <kind>: <one-line what>

Dispatch: ./D-###.md (sha256-8: <hash computed at STEP 0 — binds this result
to the exact prompt bytes; a mismatch at read time means the dispatch was
edited post-hoc, which is a ledger violation, not a mystery>)
Agent/model: <model> · Started: <ISO8601> · Finished: <ISO8601>
Inputs actually read: <paths — divergence from the dispatch's input list is
itself a finding to state, not to hide>
Scratch: sslop/<###>/ (probe artifacts preserved, never deleted)

## Status

<EXACTLY one line:>
DONE — <one line>          | FAILED: <reason>          | BLOCKED

<kind-variant sections here — see vocabulary below>

[## RESUME — appended if the agent was resumed mid-flight (API error, stall):
 what was already done, what the resume added; hash re-stated. NEVER a
 second result file.]
[## BLOCKED — the one concrete question, with attempts already made]
[## DISPATCH DRIFT — verbatim text received outside the dispatch file]

VERDICT: <GATE>-PASS | <GATE>-FAIL
```

**Evidence rule (in force throughout):** raw command output or a path into
scratch; paraphrase is not evidence. "The tests pass" is a claim; a pasted
tail is a fact.

**Verdict rule:** gate-bearing kinds (review, closure, verify) end with the
`VERDICT:` line as the FINAL line of the file — `tail -1` reads the gate.
Non-gate kinds (research, build, fix) end with their last evidence section;
their Status line is the machine-readable summary.

## Kind-variant vocabulary (starter set; extend freely, spine is mandatory)

- **research** — `## Sources` (fetched URLs/paths, dated) · `## Facts`
  (numbered, dense, payload/schema-exact) · `## Unverified ⚠️` (a table of
  what could NOT be verified — absence of this section means "everything
  verified", so include it even when empty).
- **review** — `## Findings table` (id, severity BLOCKER/MAJOR/MINOR/NIT,
  where, claim attacked, evidence/repro path) · per-finding detail sections
  (BLOCKERs include proposed replacement text; repros live in scratch) ·
  `## Conformance checklist` (against the artifact's DONE-WHEN/contract).
- **closure** — `## Per-finding closure table` (CLOSED/NOT-CLOSED with the
  QUOTED artifact text that closes each) · `## Regressions` (R-# findings
  with severity — new defects introduced by the remediation itself).
- **build** — `## Built` (tree + what each piece is) · `## Silent-spec
  resolutions` (where the contract was silent; what was chosen; why minimal)
  · `## Raw verification` (the dispatch's verification-before-DONE commands,
  output tails pasted).
- **fix** — per-finding `## F-<id>` sections (cause, change, named
  regression test, HOW the regression was demonstrated failing pre-fix) ·
  `## Raw verification` (full suite tail + re-run of the reviewer's repros).
- **verify** — `## Clean-room procedure` (steps actually executed from
  scratch) · `## Raw output` (per step) — nothing else; a verifier that
  editorializes is reviewing, not verifying.

## DONE-WHEN

- Spine complete: hash recorded, inputs-actually-read stated, Status line
  in grammar, evidence raw.
- A stranger can determine the gate outcome from `tail -1` (gate kinds) or
  the Status line (non-gate kinds) without reading prose.
- Every claim in the Status line is backed by a section below it.
