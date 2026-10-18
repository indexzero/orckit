## LOG.md line grammar (append-only, newest last)

```
- <ISO8601> <EVENT> <detail with artifact paths>
```

The event vocabulary is small and fixed. Events are `INVOCATION-ZERO`,
`DISPATCH`, `RESULT`, `GATE`, `DECISION`, `INCIDENT`, `USER`, `CANCELLED`,
`PREP`, `ANNOUNCE`, `NOTE`, `ENV`, `BRANCH`, and `PR`.
An INCIDENT records a stall or API error and how the run resumed.
USER records a mid-run directive. PREP records context-hygiene extraction.
ENV records toolchain versions. The INCIDENT and resume-in-place entries carry
load. They are how a future reader tells a re-dispatch (the prompt
changed) from a resume (the context survived).
