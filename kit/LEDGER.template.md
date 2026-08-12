# LEDGER — templates for orchestration/ (the only memory)

> Memory lives in files, never in a mind. Give the gates a table with
> evidence paths; give decisions a pinned list; give events an append-only
> grammar; give every dispatch a verbatim file with its result beside it.
> When the form grows heavy, let a leaner one emerge — standing rules, a
> stack table, a task sequence — but never let the ledger thin to summary.

## orchestration/ layout

```
orchestration/
  STATE.md            phase, gates, loop counters, pinned decisions, dispatch registry
  LOG.md              append-only: timestamp EVENT detail (artifact paths inline)
  QUESTIONS.md        non-blocking questions + assumptions acted on (see QUESTIONS.template.md)
  DEVIATIONS.md       genuine deviations, terse (see DEVIATIONS.template.md)
  BACKLOG.md          minors, nits, out-of-checklist work (never gates)
  dispatches/         ONE directory, everything for a dispatch side-by-side
                      (prompts and results in separate dirs make scanning
                      eyes do extra work):
    D-###.md            the exact prompt — written FIRST, dispatched by
                        pointer ("Read this file"), so verbatim holds by
                        construction, not discipline; a summary is a rule
                        violation (skeleton: kit/dispatches/D-###.md)
    D-###.result.<shortname>.md
                        the subagent's report beside its prompt, never
                        summarized in place (spine + kind variants:
                        kit/dispatches/D-###.result.md)
    D-###.<artifact>.md supervisor-authored companions (dispositions,
                        findings-table extracts) pair by ID
  BLOCKED.md          exists ONLY when human input is required; the exact question
```

## STATE.md skeleton

```markdown
# STATE — <project> Ledger

**Last updated:** <ISO8601>
**Operating instruction:** <supervisor file> (adopted)
**Intent contract:** PROBLEM.STATEMENT.md (wins over recollection)
**Subagent model:** <pinned model>

## Phase
- **Current phase:** <P#/COMPLETE/BLOCKED>
- **Next action:** <one imperative sentence — the resume point>
- **Standing user directives:** <bulleted, verbatim-ish>

## Gates
| Gate | Status | Evidence |
|---|---|---|
| G1 (<definition>) | PASS/FAIL/— | <result path + "VERDICT: ..." quote> |

## Loop counters (ceiling 3 each)
- <loop name>: <n>/3 <notes>

## Pinned decisions
- <DECISION-FINAL artifacts by exact path; scaling decisions; anything a
  fresh supervisor must not re-litigate>

## Dispatch registry
| ID | Phase | Inputs | Result | Status |
|---|---|---|---|---|
| D-001 | P1 | <paths> | dispatches/D-001.result.<shortname>.md | DONE/RUNNING/CANCELLED — <one-line outcome> |
```

## LOG.md line grammar (append-only, newest last)

```
- <ISO8601> <EVENT> <detail with artifact paths>
```

Event vocabulary (keep it small and fixed): `INVOCATION-ZERO`, `DISPATCH`,
`RESULT`, `GATE`, `DECISION`, `INCIDENT` (stall/API error + how resumed),
`USER` (mid-run directive received), `CANCELLED`, `PREP` (context-hygiene
extraction), `ANNOUNCE`, `NOTE`, `ENV` (toolchain versions), `BRANCH`/`PR`.
The INCIDENT + resume-in-place entries are load-bearing: they are how a
future reader distinguishes a re-dispatch (prompt changed) from a resume
(context preserved).

## dispatches/D-###.md skeleton

```markdown
# D-### — <phase>: <task> [— replaces D-### if applicable]

Model: <pinned>. Dispatched: <date>. [Branch: <branch>.]
[What changed vs the replaced dispatch: <the corrected facts — this is where
stale-memory drift gets documented and killed>]

---
<the dispatch header from SUPERVISOR.template.md §1, filled in, then:>

HARD RULES (user directives, final):
- <verbatim standing directives that bind this dispatch>

VERIFIED FACTS (fetched <date>, cite sources):
- <API surfaces, versions, payload shapes the subagent must not "remember">

Scope:
1. <numbered, concrete>

Method: source-driven — fetch and cite primary docs; UNVERIFIED +
DEVIATIONS.md entries where sources are silent.

Verification before DONE: <exact commands; raw output tail pasted into report>

Scratch: <project>/sslop/<###>/ — never /tmp. Never delete from it.
Do not read/write: orchestration/ (except your Result), other agents' scratch.
```

## Result-file convention

One result per dispatch: `dispatches/D-###.result.<shortname>.md`, beside
its prompt (skeleton: `kit/dispatches/D-###.result.md` — spine
mandatory, kind sections free). Reports contain raw command output, not
summaries of it. The supervisor NEVER edits a result file; corrections are
new LOG entries. A resumed agent APPENDS a `## RESUME` section — never a
second result file. Gate-bearing kinds end with the `VERDICT:` line as the
file's final line (`tail -1` reads the gate).

## DONE-WHEN

- A fresh supervisor can resume from STATE.md alone without asking questions.
- Every gate row's evidence path exists and contains the quoted verdict.
- Every dispatch file would let you re-dispatch identically after total loss
  — checked by reading the dispatch files, not by trusting that you meant
  to paste the prompt. Compose-then-paste breeds summaries; the
  pointer-dispatch protocol in kit/dispatches/D-###.md makes verbatim
  structural, and after-the-fact reconstructions must carry the RETRO
  label.
- Every D-### has at least one `.result.` sibling (`ls dispatches/` shows
  the pairing at a glance — that is the point of the layout).
