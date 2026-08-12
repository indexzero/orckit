# QUESTIONS.md — template

> Anything askable is NOT a reason to stop: make the best assumption,
> record it, continue. QUESTIONS.md is the one place the returning human
> reads to find every judgment call made in their absence — each entry
> carrying the assumption acted on, the impact if wrong, and the way to
> override it.

## Entry grammar

```markdown
## Q-### — <the question, phrased so it can be answered in one line>

- **Context:** <where this arose; verbatim fragment if from spoken input>
- **Assumption acted on:** <what was decided and already built>
- **Why:** <one or two sentences>
- **Impact if wrong:** <what has to change; cheap or expensive>
- **How to override:** <the concrete edit/command that flips the decision>
- **Status:** OPEN | ANSWERED(<date, answer>) | MOOT(<why>)
```

## Rules

1. A question lands here at the moment the assumption is made, not at
   session end (compaction can eat "I'll write it later").
2. Every entry MUST have an assumption acted on. A question with no
   assumption is a BLOCKED state, which is a different file and a full stop.
3. Order by cost-if-wrong descending in the final pass, so the human reads
   the expensive bets first.
4. Cross-link: ambiguity rows in PROBLEM.STATEMENT.md carry Q-refs; genuine
   contradictions discovered later graduate to DEVIATIONS.md and the Q gets
   Status: MOOT with a pointer.
5. **Close-out pass (required):** before STATE goes COMPLETE, revisit every
   entry — update Status lines and append what the run since learned about
   each assumption (evidence gained, drills passed, costs revised). An
   assumption whose supporting evidence changed mid-run but whose entry
   still reads as day-one guesswork misinforms the returning human.

## DONE-WHEN

- The returning human can review every judgment call in one sitting and
  override any of them with the instructions given.
- Zero questions that silently became decisions without an entry.
- The close-out pass ran: no Status line is stale relative to what the run
  learned.
