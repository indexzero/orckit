# DEVIATIONS.md: template

> Be terse. One paragraph per GENUINE deviation. Twenty-nine entries serve
> worse than five. Where the authority is only silent, resolve it in a code
> comment with a source citation. That is implementation, not deviation.

## What counts as a deviation

A deviation is a place where the delivered artifact **contradicts** its
governing authority: the design doc, the problem statement, or a user
directive. Not a choice the authority left open (a code comment). Not a bug
(fix it). Not future work (BACKLOG).

## Entry grammar

```markdown
**<authority section>: <what deviated, stated as the resolution> (<who wins>).**
<One terse paragraph. What the authority says. What reality turned out to
be, with the fetched or verified evidence and the version pins. What was
done instead. Why the SUBSTANCE of the authority is preserved. Where the
change is recorded (file, commit).>
```

The moves that make an entry earn its place:
- Lead with the resolution, not the confusion ("copied code wins (u64 BE,
  not u32 LE)").
- Pin versions ("autobee@1.0.10 was checked before resolving").
- Name the substance preserved ("the substance of section 8 is the UNIFORM
  weight"). Deviate on the letter. Honor the intent. Say which is which.
- If the authority pre-authorizes the deviation ("on discrepancy the copied
  code wins and DEVIATIONS.md records it"), quote that.

## Rules

1. Terse. If an entry exceeds one paragraph, it is two deviations or half
   a design doc.
2. Every entry cites its evidence: a fetched source, a test, a commit.
3. A user-directed deviation is still a deviation. Record it with the
   directive quoted ("user mandate, <date>, emphatic").
4. The file is subject to a "gut it" pass at any time. Verbose history
   lives in git, not in the file.

## DONE-WHEN

- Zero entries that only narrate implementation choices.
- Every contradiction between artifact and authority has exactly one entry.
