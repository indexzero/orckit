# Kit provenance

`create/kit` records the source kit and its inputs in `kit.json`:

- `gitHead` and `describe`: the source kit revision.
- `inputs`: source paths, SHA-256 digests, and uncommitted-input flags.
- `lineage.includeInputDigests`: whether input digests may enter the public
  lineage record.

Composition inputs include the manifest, recipes, fragments, and renderer.
Rendered templates are snapshots. Later source edits do not rewrite an
already issued dispatch or its result.
