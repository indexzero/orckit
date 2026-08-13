# lineage — where kit shapes come from

Every shape your kit as it evolves should be earned by a real run, and lineage 
is the provenance ledger: which run taught which rule, so amendments carry their
archaeology the way commit messages do. "Built in <run> because <friction>"
is the standard — a plausible recollection is not a record.

This directory ships the mechanism, not the history. Which runs a kit
descends from is unique to the kit, the runs of that kit, and the user's
overall context; the full record lives in the user's private orckits.

As patterns evolve we invite you to normalize them into a generic and provable
improvement that you can upstream from your `<your-username>/orckits` private
repository.

## The rule

- Every run ends with an `EVALS.md` (see `kit/`). Distill it,
  sanitize it, and add it here as
  `evals/<YYYY>-<MM>-<slug>.md`, following
  `evals/YYYY-MM-slug-name.template.md`.
- An amendment PR to the kit cites the digest that motivated it. No
  digest, no amendment — friction reconstructed from memory is fiction.
- Digests are sanitized: runs named by slug alone, no verbatim private
  context, no absolute paths, nothing that says "this came from here."
