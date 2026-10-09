# EVALS.md: template (grade the kit, not only the product)

> The cost of convergence is part of the report: loop counters spent,
> majors waived. Grade the templates, not only the product. The templates
> are the durable asset. The product is one sample of their output. A
> scaffold-phase section is allowed. If friction was live while the run
> home was written, stage those items before the run starts. Confirm or
> strike them at run end.

```markdown
# EVALS: <session/date>

## Verdict table

| Template | Used for | Verdict | Evidence |
|---|---|---|---|
| <name> | <artifact produced> | KEEP / MODIFY(<how>) / DROP | <what happened that proves it> |

## Cost of convergence

- Dispatches: <n> (<m> cancelled or replaced, with reasons)
- Loop counters spent: <per loop, n/3>
- Incidents: <API errors, stalls, user corrections, and whether the ledger
  made them recoverable>
- Inline work by the supervisor: <what, and whether the scaling decision
  predicted it>

## What the templates got right

<Specific moments where a template forced a better outcome than the default
behavior produces. Cite files and log lines.>

## What I would change

<Numbered, concrete edits to specific template files. Phrase each one so it
can be applied as a diff next session. Template bugs found by use are the
most valuable output of the session. Do not generalize them away. The ones
that survive sanitization are the next amendments of the kit.>

## Honest failures

<Where the process was theater: artifacts produced to satisfy the template
rather than to carry information. Name them. A kit that cannot name its own
theater grows more of it.>

## Viability

<Can you hand this kit to a new agent with a new goal tomorrow? What class
of goals does it fit: size, risk, reviewability? What is the minimum
project size below which the kit is overhead?>
```

## DONE-WHEN

- Every template has a verdict with evidence, including at least one
  MODIFY or DROP. A kit graded all-KEEP was not graded.
- The cost numbers are real counts from the ledger, not impressions.
