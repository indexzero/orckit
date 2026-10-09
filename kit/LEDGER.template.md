# LEDGER: templates for orchestration/ (the only memory)

> Memory lives in files, never in a mind. Give the gates a table with
> evidence paths. Give decisions a pinned list. Give events an append-only
> grammar. Give every dispatch a verbatim file with its result beside it.
> When the form grows heavy, let a leaner one emerge, such as standing
> rules, a stack table, or a task sequence. Never let the ledger thin to a
> summary.

## orchestration/ layout

```
orchestration/
  STATE.md            phase, gates, loop counters, pinned decisions, branch stack, dispatch registry
  LOG.md              append-only: timestamp EVENT detail (artifact paths inline)
  QUESTIONS.md        non-blocking questions and the assumptions acted on (see QUESTIONS.template.md)
  DEVIATIONS.md       genuine deviations, terse (see DEVIATIONS.template.md)
  BACKLOG.md          minors, nits, out-of-checklist work (never gates)
  dispatches/         ONE directory, everything for a dispatch side by side
                      (prompts and results in separate directories make a
                      scanning eye do extra work):
    D-###.md            the exact prompt. Written FIRST and dispatched by
                        pointer ("Read this file"), so verbatim holds by
                        construction, not by discipline. A summary is a
                        rule violation (skeleton: kit/dispatches/D-###.md)
    D-###.result.<shortname>.md
                        the report of the subagent beside its prompt, never
                        summarized in place (spine and kind variants:
                        kit/dispatches/D-###.result.md)
    D-###.<artifact>.md supervisor-authored companions (dispositions,
                        findings-table extracts) paired by ID
  BLOCKED.md          exists ONLY when human input is required: the exact question
```

## STATE.md skeleton

```markdown
# STATE: <project> Ledger

**Last updated:** <ISO8601>
**Operating instruction:** <supervisor file> (adopted)
**Intent contract:** PROBLEM.STATEMENT.md (wins over recollection)
**Subagent model:** <pinned, with the context window named>

@delivery.current_execution_state
@trust.durable_decisions
@delivery.active_work_assignments_and_their_status
```

The status vocabulary: `PLANNED` is a dispatch file written before the
run began, for the owner to read, and not yet sent. `RUNNING`, `DONE`, and
`CANCELLED` mean what they say.

@trust.event_history
## dispatches/D-###.md skeleton

```markdown
# D-### <phase>: <task> [replaces D-### if applicable]

Model: <exact model id>
Context-window: <positive integer> tokens
Reasoning: <host setting or not applicable>
Transport: <native fresh conversation or fresh CLI session>
Dispatched: <date>. [Branch: <branch>.]
[What changed vs the replaced dispatch: <the corrected facts. This is where
stale-memory drift gets documented and killed.>]

---
<the dispatch header from SUPERVISOR.template.md section 1, filled in, then:>

HARD RULES (user directives, final):
- <the verbatim standing directives that bind this dispatch>

VERIFIED FACTS (fetched <date>, cite sources):
- <API surfaces, versions, payload shapes the subagent must not "remember">

Scope:
1. <numbered, concrete>

Method: source-driven. Fetch and cite primary docs. Where a source is
silent, mark UNVERIFIED and write a DEVIATIONS.md entry.

Verification before DONE: <exact commands. The raw output tail goes in the report.>

Scratch: <project>/sslop/<###>/. Never /tmp. Never delete from it.
Do not read or write: orchestration/ (except your Result), the scratch of other agents.
```

## Result-file convention

One result per dispatch: `dispatches/D-###.result.<shortname>.md`, beside
its prompt (skeleton: `kit/dispatches/D-###.result.md`). The spine is
mandatory. The kind sections are free. A report contains raw command
output, not a summary of it. The supervisor NEVER edits a result file. A
correction is a new LOG entry. A resumed agent APPENDS a `## RESUME`
section. It never writes a second result file. A gate-bearing kind ends
with the `VERDICT:` line as the final line of the file, so `tail -1` reads
the gate.

## DONE-WHEN

- A new supervisor can resume from STATE.md alone without a question.
- Every evidence path in a gate row exists and contains the quoted verdict.
- Every dispatch file lets you re-dispatch identically after total loss.
  Check this by reading the dispatch files, not by trusting that you meant
  to paste the prompt. Compose-then-paste breeds summaries. The
  pointer-dispatch protocol in kit/dispatches/D-###.md makes verbatim
  structural. A reconstruction after the fact must carry the RETRO label.
- Every D-### has at least one `.result.` sibling. `ls dispatches/` shows
  the pairing at a glance. That is the point of the layout.
