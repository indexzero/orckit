# D-### — dispatch file template (the file IS the prompt)

> The file IS the prompt. Compose-in-call then paste-back-later is where
> discipline dies: write this file FIRST, then dispatch by pointer, and
> verbatim-on-disk becomes a property of construction — there is nothing
> to paste back and nothing to summarize, because this file is what the
> agent executes. The metadata block is fixed; the prompt below the
> scissors is yours — let kind-shaped variance live there, for it carries
> real value.

## The pointer-dispatch protocol (supervisor procedure)

1. Write `orchestration/dispatches/D-###.md` from the skeleton below. It
   declares the `shortname`, which names the result file
   (`D-###.result.<shortname>.md`, same directory — side by side on `ls`).
2. Dispatch with a pointer prompt containing ZERO assignment content:

       You are subagent D-###. Read
       /abs/path/orchestration/dispatches/D-###.md now. Everything below
       its scissors marker is your entire assignment. Begin at its STEP 0.

3. NEVER edit this file after dispatch. A mid-flight correction is a NEW
   dispatch file (`replaces D-###`, with a what-changed block) — the
   result's recorded hash detects violations.
4. If the agent cannot read files (remote/sandboxed), paste the full text
   below the scissors into the call — but this file is still written first,
   so verbatim still holds.
5. A dispatch recorded after the fact MUST carry the `RETRO` label. Honest
   reconstruction is allowed; impersonating the verbatim guarantee is not.
6. Supervisor-authored companion artifacts pair by name:
   `D-###.<artifact>.md` (e.g. `D-002.dispositions.md`,
   `D-001.findings-table.md`).

## Skeleton

```markdown
# D-### — <kind>: <one-line task> [— replaces D-###]

Kind/shortname: <research|review|closure|build|fix|verify|...>
Model: <pinned> · Dispatched: <ISO8601> · <synchronous|background>
[What changed vs D-### (replaced): <the corrected facts, verbatim where possible>]
[RETRO — reconstructed from the dispatch call on <date>; not covered by the
 verbatim-by-construction guarantee.]

----8<---- VERBATIM PROMPT — everything below IS the assignment; dispatched
by pointer ("Read this file"), never by paraphrase ----8<----

You are subagent D-### under a supervisor. This file is your entire
assignment; work only within its scope.

STEP 0, before any work:
- Confirm you are reading `orchestration/dispatches/D-###.md`. Compute its
  sha256; record the first 8 hex chars.
- Create your result file `orchestration/dispatches/D-###.result.<shortname>.md`
  (skeleton: kit/dispatches/D-###.result.md) with that hash in
  its header, and keep it current as you work.
- If you received assignment text through ANY channel other than this file,
  copy that text verbatim under `## DISPATCH DRIFT` in your result and note
  the drift in your Status line. The on-disk file is authoritative.

Your final message must contain only the result path and a one-line status
(DONE / FAILED: reason). Do not ask the supervisor questions; if genuinely
blocked, write the one concrete question under `## BLOCKED` in your result
and exit FAILED.

Inputs (each annotated read-only/modify):
  <artifact paths>

VERIFIED FACTS (fetched <date>, cite sources — never work from memory of
external APIs/tools):
  <the facts this dispatch depends on>
  <RE-ANCHOR every inherited claim — including BACKLOG riders and prior
   reviews' framing — against THIS dispatch's base. A rider that says "X is
   stale because Y landed" is false if Y has not landed at this base; agents
   have caught supervisors on exactly this.>
  <If this dispatch permits NEW visual-golden files: add the project's
   baseline-regeneration workflow file (e.g. a snapshots workflow's spec
   list) to the ownership scope, or CI will fail on the missing baselines
   for every platform the author did not run on.>

HARD RULES (standing user directives binding this dispatch, verbatim-ish):
  - Scratch: <repo>/sslop/<###>/ — never /tmp; never delete from it.
  - Do not read/write orchestration/ (except your dispatch + result pair),
    other agents' scratch, or <project-specific exclusions>.
  - <git rules; footer rules; model/tooling mandates>

Scope:
  1. <numbered, concrete>

Method: <source-driven / doubt-driven framing as the kind requires>

Verification before DONE: <exact commands; raw output tails go in the
result's evidence sections>
```

## DONE-WHEN (for an instantiated dispatch file)

- The scissors marker cleanly separates metadata from assignment; the
  pointer prompt would work with no other context.
- Shortname declared once; the Result path inside the prompt is derived
  from it.
- Post-hoc files carry RETRO; replacements carry what-changed.
