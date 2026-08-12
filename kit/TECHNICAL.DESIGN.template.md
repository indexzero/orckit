# TECHNICAL.DESIGN.DOCUMENT.md — template

```markdown
# **<Thing> – Technical Design**

**Author:** <name>
**Approvers:** [TBD]
**Reviewers:** [TBD]
**Status:** Draft | In Review | Approved

## Overview

<3 short paragraphs max: the problem at scale, the punchline of the analysis,
and the recommended solution with its headline numbers. The Overview is the
whole doc for 80% of readers — it must carry the decision on its own.>

## Background

<Why the naive mental model fails. Name the mismatch ("not a flaw in npm's
design; a mismatch between the tool's intended use case and our analytical
requirements"). Quantify the expansion factor / failure mode.>

## Goals

* <Bulleted, verifiable, includes the measurement goals ("validate X against
  ground truth, achieving N%") not just build goals.>

## Non-Goals

* <Reinventing the wheel / boiling the ocean — say it explicitly.>
* <The adjacent systems you will NOT support.>

## Research Methodology

<Numbered: define → try everything (including what you shouldn't) → build
prototypes, not theories → verify against ground truth → do the math (time,
memory, dollars). Keep a self-deprecating honesty about what failed; it
buys credibility for the recommendation.>

## Approaches Evaluated

### 1. <Naive approach>
**Approach (naive):** <one sentence + "what could go wrong?">
**Observed Behavior:** <bulleted, measured>
**Assessment:** <one line, blunt>

### 2. <Workaround approach>
**Approach (hack it):** <with a small honest code block>
**Observed Behavior / Assessment:** …

### 3. <Alternatives> …

### N. 🏆 <Recommended approach>
**Approach:** <with the actual query/code>
**Key Advantages:** <bulleted — include the known drawbacks in the same list
("noticeable lag in pre-computed data"); hiding them here costs you the
Verification section's credibility>
**Assessment:** <why optimal despite drawbacks>

## Performance Analysis

| Method | <scale target> | Time | Memory | Cost |
|---|---|---|---|---|

<Plus one concrete benchmark on a named, reproducible example.>

## Verification Methodology

<How you established ground truth, compared, and computed an accuracy number.
Include the discrepancy analysis: WHERE the recommended approach is wrong and
why that is acceptable.>

## Recommended Solution: <name>

<A working reference implementation snippet + a link/path to the runnable
example in-repo.>

## Operational policy (REQUIRED — do not skip)

<The lifecycle of every artifact the solution produces: who writes it, who
commits it, what is ignored, what survives `git clean`/branch deletion, who
may mutate it and when, and what the merge story is for each mutable file.
If the solution writes files, this section exists; "obvious" is not an
exemption. Lifecycle questions — who mutates what, when, and how each
mutable file merges — are where designs go blind first: an analysis needs
no ops section, and a tool always does.>

## Cost Analysis

<Recommended vs alternatives, including engineering-time and operational
complexity, not just dollars. End with the ROI sentence.>

## Appendix: <production examples / edge-case catalogue>

## Conclusion

<Three paragraphs: evidence supports X; building custom is opportunity cost;
the pragmatic choice. Written to be quotable by the approver.>
```

## Adaptation notes for fire & forget

- Where a design doc would have a human Approver, this doc's approver is a
  **fresh adversarial-review dispatch** (see SUPERVISOR.template.md) or —
  below some size threshold — the supervisor's own verification pass, recorded
  in the ledger.
- "Consider both possibilities" instructions from the problem statement land
  in **Approaches Evaluated** as first-class approaches, each with an honest
  Assessment, even if one was clearly doomed from the start.
- Every number you cannot measure in-session is labeled ESTIMATE; every fact
  fetched from a primary source carries its citation (source-driven rule).

## DONE-WHEN

- Exactly one 🏆 recommendation; every alternative has a blunt Assessment.
- The deferred decisions from PROBLEM.STATEMENT.md are decided HERE, each
  traceable to an Approaches Evaluated entry.
- The spec-like sections (schemas, event names, file layouts) are precise
  enough that a build dispatch needs no other design input.
- The Operational policy section covers every artifact the solution
  produces, including derived/regenerable ones.
