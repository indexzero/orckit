# PROBLEM.STATEMENT.md: template

> Transliterate spoken requirements into a statement a stranger can act on.
> When the human is present, confirm it and mark it confirmed. When the
> human is absent, the statement must carry its own uncertainty, not borrow
> confidence it does not have.

```markdown
---
status: "UNCONFIRMED. Acting on the best interpretation (fire and forget)."
sources:
  - "<verbatim prompt, transcript, or context file, with its path>"
transliterated: "<date> by <agent>. If this file and the verbatim source conflict, the verbatim source wins and this file is corrected."
open_interpretation_risks: "see orchestration/QUESTIONS.md (Q-### refs inline below)"
---

# Problem Statement: <short name>

## Verbatim signal

<Quote the load-bearing phrases exactly as given, ugly grammar and all.
Spoken input is lossy. The original words are evidence. Your paraphrase is
interpretation. Keep them separable.>

## Interpretation

<One or two paragraphs. What the human wants to achieve, in plain
language. Include the goal BEHIND the stated goal if one is visible.>

## Outcome

- <The artifacts that must exist when this is done, each with a path.>

## User

<Who this is for. How they will review: after the fact, a PR stack, or
reading files. What they value more: process or outcome, speed or rigor.>

## Why now

<The trigger. It often explains scope better than the requirements do.>

## Success criteria

- <Checkable and evidence-path-shaped. "X exists at Y and does Z", not "X
  works".>

## Constraints

- <A hard rule from the source, traceable to a verbatim phrase.>
- <A house rule that applies: the global instructions, the repo
  conventions.>

## Explicitly considered, not yet decided

- <Where the source says "consider both possibilities", list the
  possibilities HERE. Defer the decision to the design doc. Do not smuggle
  a decision into the problem statement.>

## Out of scope

- <What a reasonable agent might build but must not.>

## Ambiguities and resolutions

| # | Ambiguity (verbatim fragment) | Resolution acted on | Q-ref |
|---|---|---|---|
| 1 | "<fragment>" | <best assumption> | Q-001 |

## Stopping rule

COMPLETE or BLOCKED only. An askable item is NOT a reason to stop. Make the
best assumption. Record it in `orchestration/QUESTIONS.md`. Continue.
```

## DONE-WHEN

- Every constraint traces to a verbatim fragment.
- Every ambiguity has a resolution AND a Q-ref. Zero silent
  interpretations.
- A stranger who reads only this file builds approximately the right
  thing.
- Deferred decisions are labeled as deferred, with the deciding artifact
  named.
