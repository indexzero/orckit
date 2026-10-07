# lineage: where kit shapes come from

Every shape in your kit must be earned by a real run. Lineage is the
provenance ledger. It records which run taught which rule, so an amendment
carries its archaeology the way a commit message does. "Built in <run>
because <friction>" is the standard. A plausible recollection is not a
record.

This directory ships the mechanism, not the history. Which runs a kit
descends from is unique to the kit, to the runs of that kit, and to the
user. The full record lives in the private orckits of the user.

As patterns evolve, normalize them into a generic and provable improvement.
Then send that improvement upstream from your `<your-username>/orckits`
private repository.

## The rule

- Every run ends with an `EVALS.md` (see `kit/`). Distill it. Sanitize it.
  Add it here as `evals/<YYYY>-<MM>-<slug>.md`, in the shape of
  `evals/YYYY-MM-slug-name.template.md`.
- An amendment PR to the kit cites the digest that motivated it. No
  digest, no amendment. Friction reconstructed from memory is fiction.
- A digest is sanitized. The run is named by slug alone. It carries no
  verbatim private context, no absolute path, and nothing that says "this
  came from here."
- A scaffold-phase digest is allowed. If the friction was live while the
  run home was written, the digest can carry those items before the run
  starts, marked as staged. Confirm or strike each one at run end.
