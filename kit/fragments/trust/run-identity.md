# Run identity and output target

`create/kit` records this run's identity in `kit.json`:

- `slug`: the run name.
- `instantiatedAt`: the creation time in UTC.
- `target.type` and `target.url`: the target repository.
- `target.directory`: the optional subdirectory in scope.
- `target.gitHead`: the target's starting revision, when reachable.

Use the run manifest to identify the effort and its starting state.
