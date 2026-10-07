# Run orckit with Codex

The ledger, dispatch protocol, and gates apply to both Codex and Claude Code.
Host setup supplies instruction discovery, model selection, and filesystem access.

## Prepare the run

Use orckit's `create/kit` to scaffold a run in your private orckits clone.
It copies templates and records their digests.
It does not fill placeholders or install skills.
New scaffolds include `AGENTS.md`, which routes supervisor and worker roles.

Fill the templates and extract their fenced skeletons into working documents.
Use `LEDGER.md` to create `orchestration/STATE.md` and `orchestration/LOG.md`.
Put dispatches under `orchestration/dispatches/`. Resolve every path in the
run documents to the chosen layout. Keep scaffold blanks separate from live dispatches.
Record absolute paths for the run home, target checkout, worktrees, and scratch.
Review the completed scaffold before code work.

Launch the supervisor from the run home so Codex discovers its `AGENTS.md`.
If launching from a target worktree, explicitly name the run entry point:

```text
Read /absolute/path/to/private/run/AGENTS.md and resume this run as supervisor.
```

Codex discovers `AGENTS.md` along its working-directory ancestry.
Adding a writable directory does not load that directory's instructions.
Inspect existing overrides when checking which instructions apply.
See the [official instruction guide](https://learn.chatgpt.com/docs/agent-configuration/agents-md).

Keep private run pointers in orckits. Each worker must also follow the
target repository instructions. Pass the allowed contract paths in its dispatch.

## Re-entry and skills

Use `GOAL.md` as the authoritative re-entry procedure. A plain prompt to
read it works without installing a command. A Claude `/goal` wrapper can
point to the same file.

For optional Codex skill discovery, use `<run home>/.agents/skills/<name>/SKILL.md`.
Each skill needs `name` and `description` frontmatter.
The run's `skills/README.md` is an inventory, not a loader.
Record installation paths there. Workers launched from target worktrees need
their own discovery setup or explicit skill paths in the dispatch.
See the [official skills guide](https://learn.chatgpt.com/docs/build-skills).

## Model and context pins

Record the exact model id accepted by the host. Use a separate
`Context-window: <integer> tokens` field for the verified effective capacity.
Record its source, the host version, and the reasoning setting in the ledger.
Do not append Claude window syntax to a Codex model id.
Do not treat a configuration override as proof of server capacity.

`checks/model-pinned.sh` validates the declaration format. It cannot verify
model access, reasoning support, or the capacity available to a session.
Preflight those facts before dispatch. If a required pin cannot be met,
follow the recorded fallback ladder or mark that thread BLOCKED.

Older dispatches that relied on an implicit Claude window now need an
explicit window field or a supported window suffix. Model names alone
do not establish capacity.

## Fresh dispatches

Use native subagents when they meet SUPERVISOR's transport requirements.
When exposed, set `fork_turns="none"` and select the pinned model explicitly.
Send only the dispatch pointer. Verify the controls supported by the current host.
Never fork authoring conversation history into a reviewer.

A fresh `codex exec` session is the CLI alternative. Do not use
`resume` or `fork` to create an independent reviewer. Check `codex exec --help`
for the installed CLI before using this example. Set each variable to the
absolute path or model id recorded in the run:

```sh
codex exec \
  --cd "$dispatch_worktree" \
  --model "$dispatch_model" \
  --sandbox workspace-write \
  --add-dir "$run_home/orchestration/dispatches" \
  --add-dir "$dispatch_scratch" \
  --output-last-message "$dispatch_scratch/final.txt" \
  "You are subagent $dispatch_id. Read $dispatch_file now. Everything below its scissors marker is your entire assignment. Begin at its STEP 0." \
  >"$dispatch_scratch/process.log" 2>&1
```

Create the scratch directory before launch. Use the worktree prepared under
RAILS rule 1. The example runs synchronously. If work must survive the
supervisor session, use a process manager with verified persistence.
Record the process identifier and inspect its exit status and result file.
The final CLI message is a pointer. The result file holds gate evidence.
See the [official non-interactive guide](https://learn.chatgpt.com/docs/non-interactive-mode).

Writable roots permit filesystem operations. They do not enforce ownership
of individual dispatch files. Check the ownership rules at gates.
Workers write only their result and assigned artifacts. The supervisor owns
ledger updates and run commits. Grant the supervisor access to the private
run repository and the worktrees it manages.

## Preflight in a new host

- Verify that the supervisor reads the intended run entry point.
- Verify required skills from the actual launch directory.
- Verify model selection, reasoning settings, and available context capacity.
- Verify access to the dispatch, result directory, worktree, and scratch.
- Check target git metadata access if workers must create commits.
- Resolve the attribution trailer in RAILS rule 13 from the user's policy.
  If the host supplies none, do not invent an identity. Record an explicit
  run amendment and align the trailer gate with that policy.
- Run one bounded dispatch and verify its result hash and evidence paths.
- Re-enter through `GOAL.md` and verify the ledger's latest claim.

Record capability failures in the ledger. Continue independent work when
possible. Run instructions do not bypass host approvals or permission limits.
