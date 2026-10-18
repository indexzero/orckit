# QUESTIONS.md: template

> An askable item is NOT a reason to stop. Make the best assumption. Record
> it. Continue. QUESTIONS.md is the one place the returning human reads to
> find every judgment call made in their absence. Each entry carries the
> assumption acted on, the impact if wrong, and the way to override it.

## Entry grammar

```markdown
## Q-### <the question, phrased so it can be answered in one line>

- **Context:** <where this arose, with the verbatim fragment if it came from spoken input>
- **Assumption acted on:** <what was decided and already built>
- **Why:** <one or two sentences>
- **Impact if wrong:** <what has to change. Low or high.>
- **How to override:** <the concrete edit or command that flips the decision>
- **Status:** OPEN | ANSWERED(<date, answer>) | MOOT(<why>)
```

## Rules

1. A question lands here at the moment the assumption is made, not at
   session end. A compaction can eat "I will write it later".
2. Every entry MUST have an assumption acted on. A question with no
   assumption is a BLOCKED state. That is a different file and a full stop.
3. In the final pass, order the entries by cost if wrong, highest first, so
   the human reads the expensive bets first.
4. Cross-link. An ambiguity row in PROBLEM.STATEMENT.md carries a Q-ref. A
   genuine contradiction discovered later graduates to DEVIATIONS.md, and
   the Q gets Status MOOT with a pointer.
5. **Close-out pass, required.** Before STATE goes COMPLETE, revisit every
   entry. Update the Status lines. Append what the run learned about each
   assumption: evidence gained, drills passed, costs revised. An assumption
   whose evidence changed mid-run, but whose entry still reads as day-one
   guesswork, misinforms the returning human.

## DONE-WHEN

- The returning human can review every judgment call in one sitting and
  override any of them with the instructions given.
- Zero questions that became decisions in silence, without an entry.
- The close-out pass ran. No Status line is stale against what the run
  learned.
