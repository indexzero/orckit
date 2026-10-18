# skills/: index

> The skills slot for this run. A kit contains skills, but WHICH skills is
> unique to the kit, to the run, and to the user. Fill this slot at
> instantiation, before any code work. Keep this index current.
> This inventory does not install or load a skill.

| Skill | Source | Host discovery path or explicit read path | Why it is in this run |
|---|---|---|---|
| _none yet_ | — | — | _fill during the interview_ |

For Codex, install run skills under `<run home>/.agents/skills/` when
launching from the run home. Each skill needs a `SKILL.md` with `name`
and `description` frontmatter. The plain `skills/` directory is storage.
For workers launched elsewhere, name required skill paths in their dispatch.
Verify discovery or explicit loading in that worker's environment.

## DONE-WHEN

- Every skill in this directory has a row, and every row has a why.
- Every required skill has a verified discovery path or an explicit read path.
- Each why traces to the problem statement or to an eval axis in kit.json.
  Never "seemed useful".
