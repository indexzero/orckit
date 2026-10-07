# TECHNICAL.DESIGN.DOCUMENT.md: template

> Some runs have items that are already specified, such as an issue sweep.
> For those, scale this file down to an index with six columns: item,
> track, owned files, suites, golden rule, and model. Record the scaling
> decision in the frontmatter. For a run that must decide an approach, use
> the full shape below.

```markdown
# **<Thing>: Technical Design**

**Author:** <name>
**Approvers:** [TBD]
**Reviewers:** [TBD]
**Status:** Draft | In Review | Approved

## Overview

<Three short paragraphs at most: the problem at scale, the punchline of the
analysis, and the recommended solution with its headline numbers. The
Overview is the whole doc for 80% of readers. It must carry the decision
on its own.>

## Background

<Why the naive mental model fails. Name the mismatch ("not a flaw in the
design of npm. A mismatch between the intended use of the tool and our
analytical requirements"). Quantify the expansion factor or the failure
mode.>

## Goals

* <Bulleted and verifiable. Include the measurement goals ("validate X
  against ground truth, at N%"), not only the build goals.>

## Non-Goals

* <Reinventing the wheel. Boiling the ocean. Say it.>
* <The adjacent systems you will NOT support.>

## Research Methodology

<Numbered: define, try everything (including what you must not), build
prototypes not theories, verify against ground truth, do the math (time,
memory, dollars). Keep a self-deprecating honesty about what failed. It
buys credibility for the recommendation.>

## Approaches Evaluated

### 1. <Naive approach>
**Approach (naive):** <one sentence, then "what can go wrong?">
**Observed Behavior:** <bulleted, measured>
**Assessment:** <one line, blunt>

### 2. <Workaround approach>
**Approach (hack it):** <with a small honest code block>
**Observed Behavior / Assessment:** …

### 3. <Alternatives> …

### N. 🏆 <Recommended approach>
**Approach:** <with the actual query or code>
**Key Advantages:** <bulleted. Include the known drawbacks in the same list
("noticeable lag in pre-computed data"). To hide them here costs the
Verification section its credibility.>
**Assessment:** <why optimal despite the drawbacks>

## Model per item

| Item | Build model | Why |
|---|---|---|
| <item> | <pinned id with the window named> | <the defect class the suites cannot see, or "default tier: a direct test catches the likely error"> |

## Performance Analysis

| Method | <scale target> | Time | Memory | Cost |
|---|---|---|---|---|

<Plus one concrete benchmark on a named, reproducible example.>

## Verification Methodology

<How you established ground truth, compared, and computed an accuracy
number. Include the discrepancy analysis: WHERE the recommended approach is
wrong, and why that is acceptable.>

## Recommended Solution: <name>

<A working reference implementation snippet and a path to the runnable
example in the repo.>

## Operational policy (REQUIRED. Do not skip.)

<The lifecycle of every artifact the solution produces. Who writes it. Who
commits it. What is ignored. What survives `git clean` or a branch
deletion. Who may mutate it, and when. The merge story for each mutable
file. If the solution writes files, this section exists. "Obvious" is not
an exemption. Lifecycle questions are where designs go blind first. An
analysis needs no ops section. A tool always does.>

## Cost Analysis

<Recommended versus the alternatives, including engineering time and
operational complexity, not only dollars. End with the ROI sentence.>

## Appendix: <production examples, edge-case catalogue>

## Conclusion

<Three paragraphs: the evidence supports X. To build custom is an
opportunity cost. The pragmatic choice. Written to be quotable by the
approver.>
```

## Adaptation notes for fire and forget

- Where a design doc has a human Approver, the approver of this doc is a
  **fresh adversarial-review dispatch** (see SUPERVISOR.template.md). Below
  some size threshold it is the own verification pass of the supervisor,
  recorded in the ledger.
- A "consider both possibilities" instruction from the problem statement
  lands in **Approaches Evaluated** as first-class approaches, each with an
  honest Assessment, even if one was doomed from the start.
- Every number you cannot measure in-session is labeled ESTIMATE. Every
  fact fetched from a primary source carries its citation (the
  source-driven rule).

## DONE-WHEN

- Exactly one 🏆 recommendation. Every alternative has a blunt Assessment.
- The deferred decisions from PROBLEM.STATEMENT.md are decided HERE, each
  traceable to an Approaches Evaluated entry.
- The spec-like sections (schemas, event names, file layouts) are precise
  enough that a build dispatch needs no other design input.
- The Model per item table names a pinned model and a reason for every
  item.
- The Operational policy section covers every artifact the solution
  produces, including derived and regenerable ones.
