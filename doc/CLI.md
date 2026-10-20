---
status: "proposal. No command is implemented. The spec is the design."
spec: orckit.usage.kdl
spec_format: "usage (https://usage.jdx.dev), KDL"
verified_with:
  - "usage-cli 5.1.0 (Homebrew)"
  - "usage-cli 7.0.2 (mise, through the cli:* tasks)"
generated_reference: doc/cli/reference.md
---

# orckit CLI: a proposed command set

> The kit assumes git, a POSIX shell, and an agent CLI that can read files
> and run commands. A CLI for the kit must earn its place against that
> baseline. This document proposes one, as a spec before any code. The
> spec gives every command a name, arguments, flags, help, and examples.
> Help, completions, reference docs, and an MCP description all render from
> the one file. Read the spec with the table below beside it.

## Why a spec, and why now

Two scripts in `create/` already carry hand-written flag parsers and help
text. The ledger, dispatch, check, and lineage conventions are file shapes
with no command in front of them. A supervisor reads them by `cat` and
`tail`. That works for a person. It gives an agent nothing to complete, no
exit code to branch on, and no help to read.

One pressure made the spec urgent. A public repository needs to cite a
private run note. Today the citation is a disk path or a run name, and
both are leaks. The `ref` command below is the answer. The rest of the
command set gives that answer a home.

The spec is written in the usage format for three reasons. The same file
is the parser, the help, the completions, and the docs. mise uses the same
format for its own CLI and for task arguments, so the kit stays inside one
toolchain. An agent can read the spec through `usage mcp` and learn the
command tree without a binary to run.

## Nouns

| Noun | Meaning | Where it lives |
|---|---|---|
| orckit | The public program: templates, checks, playbooks, `create/` scripts | This repository |
| orckits | The private data: one directory per run | `<user>/orckits`, created by `create/kits-repo` |
| run, run home | One instantiated kit, named `<owner>/<repo>/<YYYY>-<MM>-<slug>` | A directory in orckits with a `kit.json` |
| `kit.json` | Provenance and run config, version 2 | The run home, written by `create/kit` |
| ledger | The only memory: `STATE.md`, `LOG.md`, dispatches, results | `<run>/orchestration/` |
| dispatch | The file that is the prompt, `D-###.md`, with its result beside it | `<run>/orchestration/dispatches/` |
| check | A script that enforces one machine-checkable rule | `checks/` and `<run>/checks/` |
| digest | The sanitized `EVALS.md` of one run, the evidence an amendment cites | `lineage/evals/` |
| handle | An opaque citation of one private file, safe for public text | Minted by `orckit ref mint` |

## How a command finds its run

Most commands act on one run home. The run is resolved in this order:

1. the `--run` flag, as a path or as a run name relative to orckits
2. the `ORCKIT_RUN` environment variable
3. the nearest `kit.json` above the working directory

The orckits clone is resolved from `--orckits`, then `ORCKITS_HOME`, then
the sibling directory `../orckits` of the orckit checkout. That last
default is the one `create/kit` and `create/kits-repo` already use.

## The command table

Every command is tagged. `existing` means the command wraps a script or a
file convention the kit already has, and the cell names it. `new` means
the behavior does not exist yet in any form.

| Command | What it does | Status | Grounded in |
|---|---|---|---|
| `kits create` | Create `<user>/orckits` on GitHub, clone it, seed a README | existing | `create/kits-repo` |
| `kits ls` | List run homes, with phase and orckit commit | new | the `kit.json` convention |
| `kits path` | Print the resolved orckits clone | new | the `../orckits` default in `create/kit` |
| `new` | Instantiate `kit/` into a run home and write `kit.json` | existing | `create/kit`, README lifecycle step 1 |
| `new --profile` | Choose which templates instantiate | new | `kit.json` `inputs[]`, open question 1 |
| `status` | Phase, next action, gates, deliverables, BLOCKED | new | `kit/LEDGER.template.md` STATE.md skeleton |
| `resume` | Print or launch the re-entry pointer | existing | `kit/GOAL.template.md`, `playbooks/codex.md`, the run `AGENTS.md` |
| `ledger log` | Tail `LOG.md`, filter by EVENT | existing | `kit/LEDGER.template.md` LOG grammar |
| `ledger state` | Print `STATE.md` or one section | existing | `kit/LEDGER.template.md` STATE skeleton |
| `ledger blocked` | Print `BLOCKED.md`, exit 3 when it exists | existing | `kit/LEDGER.template.md` layout |
| `ledger verify` | Check the ledger DONE-WHEN: pairs, evidence paths, verdict lines, hashes | new | `kit/LEDGER.template.md` DONE-WHEN, result-file convention |
| `dispatch ls` | List dispatches with result siblings and registry status | existing | `ls dispatches/` as the template describes it |
| `dispatch new` | Write the next `D-###.md` from the skeleton | existing | `kit/dispatches/D-###.md` |
| `dispatch pointer` | Print the pointer prompt | existing | `kit/dispatches/D-###.md` protocol step 2 |
| `dispatch hash` | Print the sha256 and sha256-8 of a dispatch | existing | `kit/dispatches/D-###.md` STEP 0 |
| `dispatch verify` | Compare result header hashes to dispatch bytes | new | `kit/dispatches/D-###.result.md` spine |
| `check ls` | List kit checks and run checks | new | `checks/README.md` |
| `check porcelain` | Porcelain equals the baseline | existing | `checks/porcelain-baseline.sh` |
| `check trailer` | Every commit carries the trailer | existing | `checks/trailer-present.sh` |
| `check footer` | The PR body carries no AI footer | existing | `checks/no-ai-footer.sh` |
| `check ownership` | The diff is a subset of the ownership list | existing | `checks/ownership-subset.sh` |
| `check model` | Every dispatch pins model and window | existing | `checks/model-pinned.sh` |
| `check prose` | Prose obeys the writing rules | existing | `checks/prose-lint.sh` |
| `check run` | Run a project-shaped check from `<run>/checks/` | existing | `checks/README.md`, run checks |
| `check all` | Run every bound check with facts from the ledger | new | `checks/README.md`, gate verification |
| `grade` | Verify `EVALS.md` DONE-WHEN and count costs from the ledger | new | `kit/EVALS.template.md` DONE-WHEN |
| `lineage digest` | Draft a sanitized digest from `EVALS.md` | new | `lineage/README.md`, the digest template |
| `lineage verify` | Lint a digest for what it must not carry | new | `lineage/README.md` rule 3 |
| `lineage ls` | List digests and the amendments each carries | new | `lineage/evals/` |
| `upgrade` | Three-way move of kit inputs to a newer orckit commit | new | `kit.json` `gitHead` and `inputs[]` digests |
| `ref mint` | Mint an opaque handle for a private file | new | this document |
| `ref resolve` | Map a handle back to run and file | new | this document |
| `ref cat` | Print the file a handle names | new | this document |
| `ref open` | Open the file in an editor | new | this document |
| `ref ls` | List minted handles from the private index | new | this document |
| `ref scan` | Find handles and leaks in public text | new | this document, `lineage/README.md` rule 3 |
| `ref key init`, `rotate`, `ls` | Manage minting keys | new | this document |
| `doctor` | Verify tools, hosts, the orckits clone, and a key | new | the run `AGENTS.md` shared rules, `mise.toml` tools |
| `completion` | Print a shell completion script | new | usage `generate completion` |
| `usage` | Print the spec (hidden) | new | the mise convention `mise usage` |

Every write command is marked `effect="write"` in the spec. Every read
command is marked `effect="read"`. No command is destructive. `upgrade`
reports by default and writes only with `--apply`. That matches the kit
principle that irreversible operations go one at a time.

## Reference handles

### The problem

A kit amendment cites the run that bred it. A PR body cites the review
finding that motivated a fix. A lineage digest cites the ledger line that
proves a cost. Each of these citations points into a private orckits
clone. Each is a leak when written as a path:

- an absolute path names the machine and the user
- a run name `<owner>/<repo>/<YYYY>-<MM>-<slug>` names the target and the work
- a file name inside the run names the artifact kind and the dispatch id

The lineage rule already says a digest carries no absolute path and names
the run by slug alone. A rule with no mechanism is obeyed by discipline.
A handle makes it structural.

### The form

```text
pkg:orckits/<keyid>/<digest>[@<orckits-commit>][?lines=<a>-<b>]
```

- `pkg:orckits/` is the type. It says "a private run note" and nothing else.
- `<keyid>` is 8 hex characters: the SHA-256 of the minting key, truncated.
  It names which orckits clone family holds the mapping. It is optional.
- `<digest>` is 32 hex characters: `HMAC-SHA256(key, "<run name>\n<file path>")`,
  truncated to 128 bits. It is the handle proper.
- `@<orckits-commit>` is an optional short commit sha of the orckits
  repository. It pins the citation to the bytes at mint time.
- `?lines=<a>-<b>` is an optional line range.

Two examples, neutral and fictional:

```text
pkg:orckits/5e1c0a9b/3f6d2c8a9b7e4f01d2c3b4a5968778e9
pkg:orckits/5e1c0a9b/3f6d2c8a9b7e4f01d2c3b4a5968778e9@a1b2c3d?lines=40-58
```

The shape is a Package URL on purpose. vlurp fetches agent instructions
from `pkg:github/<owner>/<repo>@<ref>#<path>`. An orckits handle sits
beside it in a document and reads the same way: a type, a namespace, a
name, a version. The two differ in one property. A vlurp PURL is
transparent and resolves anywhere. An orckits handle is opaque and
resolves only where the key is. The PURL `#subpath` slot is unused,
because a subpath is exactly the thing the handle hides.

The `--format bare` form drops the `pkg:orckits/` prefix and gives
`<keyid>-<digest>`. It is for places where a URL is noise, such as a
commit trailer.

### Minting

`orckit ref mint <path>` resolves the path to a run name and a file path
inside the run. It computes the digest with the default key. It appends
one line to the private index `<orckits>/.orckit/refs.jsonl`:

```json
{"digest":"3f6d…","key":"5e1c0a9b","run":"acme/widgets/2026-01-example","file":"orchestration/LOG.md","minted":"2026-01-15T12:00:00Z"}
```

It commits the index, because every event is a commit. It prints the
handle. The index is a record of which private files have public
citations. That record is useful on its own. When a file is renamed, the
index says which public documents now dangle.

### Resolving

`orckit ref resolve <handle>` looks the digest up in the index. When the
index has no row, it recomputes the digest over every file in every run
home, with every key the clone holds. That scan is the fallback for a
handle minted on another clone before the index was pulled. It costs one
HMAC per file and finishes in seconds for thousands of files. `cat` and
`open` build on `resolve`. A pinned handle prints the bytes at the pinned
commit unless `--live` is given.

Keys live in the private repository under `.orckit/keys/<keyid>`. Every
clone of the private repository therefore resolves every handle. A rotated
key does not invalidate old handles, because old keys stay for resolution.
The key never leaves the private repository. A public repository holds
handles only.

### What the handle reveals

The handle is public text. Assume an adversary reads it. The handle reveals:

- that a private note exists and was cited
- the key id, when present: two handles with the same key id come from the
  same private store
- the orckits commit, when pinned: two handles with the same commit were
  minted from the same state of that store
- the line range, when present: the cited passage is at least that long
- the number of distinct citations in a document

The handle never reveals:

- the owner, the target repository, or the slug
- the file name, the dispatch id, or any path component
- the machine, the user, or the orckits clone path
- whether a guessed run name or file path is correct

The last line is the reason for the HMAC. The input space is small. The
owner is public. The target repository is often public. The slug is a
kebab-case phrase. The file names come from the kit and are fixed. A plain
hash of `<run name>\n<file path>` falls to a dictionary attack in minutes.
A keyed digest does not, because the attacker has no key.

### Threat model

| Adversary | Has | Learns from a handle | Mitigation |
|---|---|---|---|
| Public reader | The handle | A private note exists. Which key family. Which pinned commit, if any | By design. Omit `--pin` and `--no-keyid` when correlation matters |
| Public reader with a guess | The handle, a guessed run name and file | Nothing. The HMAC does not confirm a guess | The key stays private |
| Reader of a leaked index | `refs.jsonl` | Every mapping in the index | The index lives only in the private repository. `ref scan` stops it from entering a public one |
| Reader of a leaked key | A key, no index | Can confirm guesses by HMAC. Cannot invert a digest | Rotate. Old handles stay resolvable. New handles use the new key |
| Content-digest reader | A handle with `?sha256=` | Can confirm a guessed file content byte for byte | Off by default. Mint it only for files whose content is already public |
| Collaborator with the private repository | Everything | Everything | The intended reader |

Two residual risks are accepted. The count of handles in a document is
visible. A pinned commit sha is a stable identifier of a private state,
and two documents that pin the same sha are linked. Neither reveals
content. Both are stated here so that a minting agent reads them before
it chooses flags.

### Where handles appear

A handle is for text that leaves the private repository: a PR body, a
commit body, a lineage digest, a README. The dispatch pointer that an
agent receives on the same machine keeps using the absolute path, because
the agent must open the file. `orckit dispatch pointer` prints that path.
`orckit ref mint` never does.

`orckit ref scan` is the gate. It reads a public document and lists every
handle. It fails on every leak. A leak is an absolute path, an orckits
clone path, a run name, or the name of a run home this clone knows.
`lineage verify` calls the same scan with `--resolve`. The sanitization rule in
`lineage/README.md` becomes a check.

## How usage renders the spec

Four mise tasks in `mise.toml` render the spec with the usage CLI:

| Task | Does |
|---|---|
| `mise run cli:lint` | `usage lint -W orckit.usage.kdl` |
| `mise run cli:help -- <words>` | Builds a usage shebang stub from the spec and runs it with `--help` |
| `mise run cli:docs` | Writes `doc/cli/reference.md` |
| `mise run cli:completions -- <shell>` | Prints a bash, zsh, fish, nu, or powershell completion script |
| `mise run cli:json` | Prints the command tree as JSON |

The `cli:completions` task takes its own argument through a usage spec in
`mise.toml`, which is how mise tasks declare arguments. The generated
completion scripts call back into `usage complete-word` with the spec, so
dynamic candidates come from the top-level `complete` nodes. In the spec,
`<run>` completes from `orckit kits ls --names`, `<handle>` from
`orckit ref ls --handles`, `<check>` from `orckit check ls --names`, and
`<dispatch>` from `orckit dispatch ls --ids`.

The spec was verified with two versions of usage-cli. The Homebrew build
is 5.1.0. The build that mise installs for the tasks is 7.0.2. Both lint
the spec with zero errors and zero warnings. The spec declares
`min_usage_version "5.1"`. Three things about 5.1.0 shape the spec:

1. The `effect` attribute, `example` nodes, `env` on flags, `alias`, and
   top-level `complete` nodes are accepted. The `exit_code` and `output`
   nodes from the current spec reference are not. Exit codes are therefore
   documented in `long_help` text, not declared.
2. A `complete` node inside an `arg` is rejected. The top-level form binds
   by argument name, so every `<run>` argument shares one completer.
3. Help for a subcommand prints on stderr with exit 1 when rendered through
   `usage bash`. The text is correct. The `cli:help` task tolerates it.
   Version 7.0.2 prints the same help on stdout with exit 0.

## Open questions

1. **Profiles.** `new --profile` is in the spec with three names: `full`,
   `issue-sweep`, `toy`. The kit has one recorded shape, the issue sweep,
   in `kit/SUPERVISOR.template.md`. Whether a profile selects files, or
   sections within files, is undecided. `kit.json` version 3 is the likely
   home for the answer.
2. **Who commits.** `ref mint` and `upgrade --apply` commit in orckits.
   The supervisor owns ledger commits today. A CLI that commits on its
   own is a second writer. The alternative is `--no-commit` as the default
   and a printed `git commit` line. The spec takes the committing default
   because every event is a commit, and marks the choice here.
3. **Scan over index.** `ref resolve` falls back to a scan of every file
   with every key. A clone with many runs and many keys pays for it. An
   index that travels with the private repository avoids it. Whether the
   index is required, or a cache, is open.
4. **Handle length.** 128 bits of digest plus a key id is 41 characters
   before the prefix. A shorter digest raises collision risk inside one
   store. 96 bits is the floor worth testing.
5. **Hosts.** `resume --launch` and `doctor --host` name `codex` and
   `claude`. The host list belongs in the run, not in the spec. The
   choices are a placeholder until a run records a third host.
6. **`check all` facts.** The command reads gate facts from the ledger. The
   STATE.md skeleton has no field for the porcelain baseline path or the
   main checkout. The ledger template gains two fields, or `check all`
   takes them as flags.
7. **A `ref` for the public side.** A kit amendment cites a digest. A digest
   cites handles. Whether an amendment PR body cites handles directly, or
   only the digest, is a lineage policy question.

## Deliberately left out

- **Running agents.** No command dispatches a subagent, runs a review, or
  drives a gate. The supervisor is an agent reading `SUPERVISOR.md`. A CLI
  that drives the pipeline is a second supervisor. `resume --launch` goes
  as far as starting a host with the pointer, and no further.
- **Writing the ledger.** Every `ledger` command reads. `dispatch new` and
  `dispatch new --register` are the only writes under `orchestration/`,
  and both write files the protocol says to write first.
- **Skills.** `skills/README.md` is an inventory, not a loader. vlurp
  fetches skills by PURL. The kit does not need a second fetcher.
- **Merging and pushing.** `playbooks/rebase-after-squash.md` and
  `playbooks/ci-green-bar.md` are procedures for a human and a supervisor.
  Each step is irreversible and shown one at a time. A command that
  batches them removes the pause the playbooks exist to keep.
- **Filling templates.** `new` copies and records. The interview that
  fills `PROBLEM.STATEMENT.md` stays with the agent and the owner.
- **A hosted resolver.** A handle resolves only where the private clone
  is. A service that resolves handles is a second copy of the private
  mapping, and a target.
- **Implementation.** Nothing in this branch runs a command. The spec and
  this document are the deliverable.
