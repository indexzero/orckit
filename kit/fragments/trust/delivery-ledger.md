# D-###.result.<shortname>.md: result file template (spine and kind variants)

> The spine below is mandatory and identical for every kind. The variant
> sections are a starter vocabulary. New shortnames are licensed.
> Shape-variance in results carries real value, so give it room. The file
> lives beside its dispatch as `dispatches/D-###.result.<shortname>.md`, so
> one scanning `ls` sees prompt and result side by side.

## The invariant spine (every result, every kind)

```markdown
# D-### result <kind>: <one-line what>

Dispatch: ./D-###.md (sha256-8: <the hash computed at STEP 0. It binds this
result to the exact prompt bytes. A mismatch at read time means the
dispatch was edited after the fact. That is a ledger violation, not a
mystery.>)
Agent/model: <model> · Started: <ISO8601> · Finished: <ISO8601>
Inputs actually read: <paths. A divergence from the input list of the
dispatch is itself a finding to state, not to hide.>
Scratch: sslop/<###>/ (probe artifacts preserved, never deleted)

## Status

<EXACTLY one line:>
DONE: <one line>          | FAILED: <reason>          | BLOCKED

## Re-anchor

| Cited location | State | Notes |
|---|---|---|
| <file:line> | HOLDS / MOVED TO <line> / VANISHED | <one line> |

<kind-variant sections here. See the vocabulary below.>

[## RESUME: appended if the agent was resumed mid-flight (API error, stall).
 What was already done. What the resume added. The hash restated. NEVER a
 second result file.]
[## BLOCKED: the one concrete question, with the attempts already made]
[## DISPATCH DRIFT: verbatim text received outside the dispatch file]

VERDICT: <GATE>-PASS | <GATE>-FAIL
```

**Evidence rule, in force throughout:** raw command output, or a path into
scratch. A paraphrase is not evidence. "The tests pass" is a claim. A pasted
tail is a fact.

**Verdict rule:** a gate-bearing kind (review, closure, verify) ends with
the `VERDICT:` line as the FINAL line of the file, so `tail -1` reads the
gate. A non-gate kind (research, build, fix) ends with its last evidence
section. Its Status line is the machine-readable summary.

## Kind-variant vocabulary (starter set. Extend freely. The spine is mandatory.)

- **research**: `## Sources` (fetched URLs and paths, dated). `## Facts`
  (numbered, dense, exact in payload and schema). `## Unverified ⚠️` (a
  table of what could NOT be verified. An absent section means "everything
  verified", so include it even when empty).
- **review**: `## Findings table` (id, severity BLOCKER/MAJOR/MINOR/NIT,
  where, claim attacked, evidence or repro path). Per-finding detail
  sections (a BLOCKER includes the proposed replacement text. Repros live
  in scratch). `## Conformance checklist` (against the DONE-WHEN or the
  contract of the artifact).
- **closure**: `## Per-finding closure table` (CLOSED/NOT-CLOSED with the
  QUOTED artifact text that closes each). `## Regressions` (R-# findings
  with severity: new defects the remediation itself introduced).
- **build**: `## Built` (tree, and what each piece is). `## Silent-spec
  resolutions` (where the contract was silent, what was chosen, why
  minimal). `## Raw verification` (the verification-before-DONE commands of
  the dispatch, output tails pasted).
- **fix**: per-finding `## F-<id>` sections (cause, change, the named
  regression test, HOW the regression was shown to fail before the fix).
  `## Raw verification` (the full suite tail, and a re-run of the repros of
  the reviewer).
- **verify**: `## Clean-room procedure` (the steps executed from scratch).
  `## Raw output` (per step). Nothing else. A verifier that editorializes
  is reviewing, not verifying.

## DONE-WHEN

- The spine is complete: hash recorded, inputs-actually-read stated,
  Status line in grammar, re-anchor table present, evidence raw.
- A stranger can read the gate outcome from `tail -1` (gate kinds) or from
  the Status line (non-gate kinds) without reading prose.
- Every claim in the Status line is backed by a section below it.
