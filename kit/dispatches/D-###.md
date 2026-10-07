# D-###: dispatch file template (the file IS the prompt)

> The file IS the prompt. Compose-in-call then paste-back-later is where
> discipline dies. Write this file FIRST. Then dispatch by pointer. Then
> verbatim-on-disk is a property of construction. There is nothing to paste
> back and nothing to summarize, because this file is what the agent
> executes. The metadata block is fixed. The prompt below the scissors is
> yours. Let kind-shaped variance live there. It carries real value.

## The pointer-dispatch protocol (supervisor procedure)

1. Write `orchestration/dispatches/D-###.md` from the skeleton below. It
   declares the `shortname`, which names the result file
   (`D-###.result.<shortname>.md`, same directory, side by side on `ls`).
2. Dispatch with a pointer prompt that contains ZERO assignment content:

       You are subagent D-###. Read
       /abs/path/orchestration/dispatches/D-###.md now. Everything below
       its scissors marker is your entire assignment. Begin at its STEP 0.

3. NEVER edit this file after dispatch. A mid-flight correction is a NEW
   dispatch file (`replaces D-###`, with a what-changed block). The hash
   recorded in the result detects a violation.
4. If the agent cannot read files (remote, sandboxed), paste the full text
   below the scissors into the call. This file is still written first, so
   verbatim still holds.
5. A dispatch recorded after the fact MUST carry the `RETRO` label. Honest
   reconstruction is allowed. To impersonate the verbatim guarantee is not.
6. A dispatch written before the run begins, for the owner to read, carries
   status `PLANNED` in the registry until it is sent.
7. Supervisor-authored companion artifacts pair by name:
   `D-###.<artifact>.md` (for example `D-002.dispositions.md`,
   `D-001.findings-table.md`).

## Skeleton

```markdown
# D-### <kind>: <one-line task> [replaces D-###]

Kind/shortname: <research|review|closure|build|fix|verify|...>
Model: <exact model id>
Context-window: <positive integer> tokens
Reasoning: <host setting or not applicable>
Transport: <native fresh conversation or fresh CLI session>
Dispatched: <ISO8601> · <synchronous|background>
[What changed vs D-### (replaced): <the corrected facts, verbatim where possible>]
[RETRO: reconstructed from the dispatch call on <date>. Not covered by the
 verbatim-by-construction guarantee.]

----8<---- VERBATIM PROMPT. Everything below IS the assignment. It is
dispatched by pointer ("Read this file"), never by paraphrase. ----8<----

You are subagent D-### under a supervisor. This file is your entire
assignment. Work only within its scope.

STEP 0, before any work:
- Make sure that you are reading `orchestration/dispatches/D-###.md`.
  Compute its sha256. Record the first 8 hex characters.
- Create your result file `orchestration/dispatches/D-###.result.<shortname>.md`
  (skeleton: kit/dispatches/D-###.result.md) with that hash in its header.
  Keep it current as you work.
- If you received assignment text through ANY channel other than this file,
  copy that text verbatim under `## DISPATCH DRIFT` in your result. Note
  the drift in your Status line. The file on disk is the authority.

STEP 1, re-anchor, before any edit:
- Read the contract. For every `file:line` it cites, open the file at your
  base. Record in your result whether the location HOLDS, MOVED TO
  <new line>, or VANISHED.
- A vanished location is a `DEVIATIONS` note in your result. Never
  improvise in silence.
- Do not edit before this table exists.

Your final message must contain only the result path and a one-line status
(DONE / FAILED: reason). Do not ask the supervisor questions. If you are
blocked, write the one concrete question under `## BLOCKED` in your result
and exit FAILED.

Inputs (each annotated read-only or modify):
  <artifact paths>

VERIFIED FACTS (fetched <date>, cite sources. Never work from memory of
external APIs or tools):
  <the facts this dispatch depends on>
  <RE-ANCHOR every inherited claim, including BACKLOG riders and the
   framing of prior reviews, against the base of THIS dispatch. A rider
   that says "X is stale because Y landed" is false if Y has not landed at
   this base. Agents have caught supervisors on exactly this.>
  <If this dispatch permits NEW visual-golden files, add the
   baseline-regeneration workflow file of the project to the ownership
   scope. An example is the spec list of a snapshots workflow. Otherwise
   CI fails on the missing baselines for every platform the author did not
   run on.>

HARD RULES (standing user directives that bind this dispatch, near verbatim):
  - Scratch: <repo>/sslop/<###>/. Never /tmp. Never delete from it.
  - Do not read or write orchestration/ (except your dispatch and result
    pair), the scratch of other agents, or <project-specific exclusions>.
  - <git rules. Footer rules. Model and tooling mandates.>

Scope:
  1. <numbered, concrete>

Method: <source-driven or doubt-driven, as the kind requires>

Verification before DONE: <exact commands. The raw output tails go in the
evidence sections of the result.>
```

## DONE-WHEN (for an instantiated dispatch file)

- The scissors marker separates the metadata from the assignment. The
  pointer prompt works with no other context.
- The shortname is declared once. The Result path inside the prompt is
  derived from it.
- STEP 1 is present, and the contract it re-anchors is named.
- A post-hoc file carries RETRO. A replacement carries what-changed.
