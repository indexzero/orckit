# PROBLEM.STATEMENT.md — template

> Transliterate spoken requirements into a statement a stranger could act
> on. When the human is present, confirm it and mark it confirmed. When the
> human is absent, the statement must carry its own uncertainty honestly
> instead of borrowing confidence it does not have.

```markdown
# Problem Statement — <short name>

**Status:** UNCONFIRMED — acting on best interpretation (fire & forget).
**Sources:** <verbatim prompt | transcript | context files, with paths>
**Transliterated:** <date> by <agent>. On any conflict between this file and
the verbatim source, the verbatim source wins and this file gets corrected.
**Open interpretation risks:** see `orchestration/QUESTIONS.md` (Q-### refs inline below).

## Verbatim signal

<Quote the load-bearing phrases exactly as given, ugly grammar and all.
Spoken input is lossy; the original words are evidence, your paraphrase is
interpretation. Keep them separable.>

## Interpretation

<One or two paragraphs: what the human is actually trying to achieve, in
plain language, including the goal BEHIND the stated goal if one is visible.>

## Outcome

- <The artifact(s) that must exist when this is done, each with a path.>

## User

<Who this is for; how they will review (post-hoc? PR stack? reading files?);
what they care about more — process or outcome, speed or rigor.>

## Why now

<The trigger. Often explains scope better than the requirements do.>

## Success criteria

- <Checkable, evidence-path-shaped. "X exists at Y and does Z" not "X works".>

## Constraints

- <Hard rules from the source, each traceable to a verbatim phrase.>
- <House rules that apply (global CLAUDE.md, repo conventions).>

## Explicitly considered, not yet decided

- <Where the source says "consider both possibilities", list the
  possibilities HERE and defer the decision to the design doc. Do not
  smuggle a decision into the problem statement.>

## Out of scope

- <What a reasonable agent might build but should not.>

## Ambiguities and resolutions

| # | Ambiguity (verbatim fragment) | Resolution acted on | Q-ref |
|---|---|---|---|
| 1 | "<fragment>" | <best assumption> | Q-001 |

## Stopping rule

COMPLETE or BLOCKED only. Anything askable is NOT a reason to stop — make the
best assumption, record it in `orchestration/QUESTIONS.md`, continue.
```

## DONE-WHEN

- Every constraint traces to a verbatim fragment.
- Every ambiguity has a resolution AND a Q-ref; zero silent interpretations.
- A stranger reading only this file would build approximately the right thing.
- Deferred decisions are labeled as deferred, with the deciding artifact named.
