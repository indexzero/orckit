# DEVIATIONS.md — template

> Be terse: one paragraph per GENUINE deviation. Twenty-nine entries serve
> worse than five. Where the authority is merely silent, resolve in code
> comments with source citations — that is implementation, not deviation.

## What counts as a deviation

A deviation is a place where the delivered artifact **contradicts** its
governing authority (the design doc, the problem statement, a user
directive). Not: choices the authority left open (code comment), not bugs
(fix them), not future work (BACKLOG).

## Entry grammar

```markdown
**<authority §ref>: <what deviated, stated as the resolution> (<who wins>).**
<One terse paragraph: what the authority says; what reality turned out to be
(with the fetched/verified evidence and version pins); what was done instead;
why the authority's SUBSTANCE is preserved; where the change is recorded
(file, commit).>
```

The moves that make an entry earn its place:
- Lead with the resolution, not the confusion ("copied code wins (u64 BE,
  not u32 LE)").
- Pin versions ("autobee@1.0.10 was checked before resolving").
- Name the substance being preserved ("§8's substance is the UNIFORM weight"
  — deviate on the letter, honor the intent, say which is which).
- If the authority itself pre-authorizes the deviation ("on discrepancy the
  copied code wins and DEVIATIONS.md records it"), quote that.

## Rules

1. Terse. If an entry exceeds one paragraph, it is probably two deviations or
   half a design doc.
2. Every entry cites its evidence (fetched source, test, commit).
3. User-directed deviations are still deviations — record them with the
   directive quoted ("user mandate, <date>, emphatic").
4. The file is subject to a "gut it" pass at any time; verbose history lives
   in git, not in the file.

## DONE-WHEN

- Zero entries that merely narrate implementation choices.
- Every contradiction between artifact and authority has exactly one entry.
