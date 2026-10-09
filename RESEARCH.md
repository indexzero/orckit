# Kit packaging research

## Initial options

| Option | How it works | Main trade-off |
|---|---|---|
| **Named profiles** | Start with `toy`, `batch`, `port`, or `new-project`. Each selects documents, sections, and gates. | Easy to choose, but combinations such as “toy Rust port” need exceptions. |
| **Independent dimensions** | Describe the work’s kind, maturity, and coordination needs. Derive the required artifacts and evidence. | Handles combinations, but can become a configuration system that needs its own manual. |
| **Progressive expansion** | Start with one plan. Split out design, state, dispatches, and reviews when the work needs them. | Low initial overhead, but expansion needs clear triggers so missing structure does not become missing discipline. |

## Functional responsibilities

| Functional responsibility | What it holds or governs | Current file or location |
|---|---|---|
| **Run identity and target** | Run name, creation time, target repository, optional subdirectory, and starting revision. | Generated `kit.json`, defined in create/kit:262. |
| **Kit provenance** | Source kit revision, input file hashes, uncommitted-input flags, and permission to publish input digests in lineage records. | Generated `kit.json`, defined in create/kit:263. |
| **Agent entry point** | Which instructions a supervisor or worker reads, how paths resolve, and how an unfinished scaffold becomes a usable run. | AGENTS.md (kit/AGENTS.template.md:1). |
| **Intent and source requirements** | Original user statements, their interpretation, intended users, motivation, and confirmation status. | PROBLEM.STATEMENT.md (kit/PROBLEM.STATEMENT.template.md:8). |
| **Scope and acceptance criteria** | Required outcomes, success criteria, constraints, exclusions, and decisions still open. | PROBLEM.STATEMENT.md (kit/PROBLEM.STATEMENT.template.md:30). |
| **Technical design and approach selection** | Background, research method, alternatives, observed behavior, trade-offs, and the selected solution. Can instead reference already specified work items. | TECHNICAL.DESIGN.md (kit/TECHNICAL.DESIGN.template.md:1). |
| **Performance, cost, and technical validation** | Benchmarks, resource costs, ground truth, accuracy, discrepancies, and evidence supporting the design. | TECHNICAL.DESIGN.md (kit/TECHNICAL.DESIGN.template.md:74). |
| **Artifact lifecycle and ownership** | Who writes, changes, and commits produced artifacts; what survives cleanup; how mutable files merge. | TECHNICAL.DESIGN.md — Operational policy (kit/TECHNICAL.DESIGN.template.md:92). |
| **Standing rules and their amendments** | Rules that bind every agent, plus recorded user directives that supersede those rules. | RAILS.md (kit/RAILS.template.md:11), including Amendments (kit/RAILS.template.md:180). |
| **Workspace preparation and isolation** | Worktree creation, starting revisions, bootstrap steps, permitted edit locations, and main-checkout cleanliness. | RAILS.md — Worktrees and bootstrap (kit/RAILS.template.md:23). |
| **Build and behavior-preservation policy** | Required suites, build prerequisites, visual baselines, coverage, and permitted behavior changes. | RAILS.md — Build, test, and goldens (kit/RAILS.template.md:53). |
| **Git integration and delivery policy** | Rebase procedures, generated-file handling, commit conventions, push restrictions, PR readiness, and merge conditions. | RAILS.md — Rebases; Git and PRs (kit/RAILS.template.md:72). |
| **Review and remediation policy** | Reviewer independence, findings severity, closure evidence, retry limits, waivers, and repro requirements. | RAILS.md — Reviews (kit/RAILS.template.md:100) and SUPERVISOR.md — Prime directives (kit/SUPERVISOR.template.md:19). |
| **Information-access boundaries** | Files agents cannot read, context that cannot enter the target repository, and separation between agent workspaces. | RAILS.md — Never commit, never read (kit/RAILS.template.md:132) and SUPERVISOR.md — Context hygiene (kit/SUPERVISOR.template.md:26). |
| **Model requirements and selection** | Model IDs, context capacity, reasoning configuration, fallback rules, and reasons for each work item’s model choice. | RAILS.md — Model (kit/RAILS.template.md:152) and TECHNICAL.DESIGN.md — Model per item (kit/TECHNICAL.DESIGN.template.md:68). |
| **Writing conventions** | Language and formatting requirements for run artifacts, commit messages, and PR descriptions. | RAILS.md — Writing (kit/RAILS.template.md:171), which delegates to the writing playbook and prose check. |
| **Execution workflow and process scale** | Phases, dependencies, gates, delegation, supervisor duties, and which process steps the run can omit. | SUPERVISOR.md (kit/SUPERVISOR.template.md:113). |
| **Agent execution transport** | Native versus CLI execution, fresh conversations, process lifetime, completion signals, and process tracking. | SUPERVISOR.md — Transport (kit/SUPERVISOR.template.md:81). |
| **Completion contract** | The evidence checklist that permits the whole run to become COMPLETE, plus legitimate stopping conditions. | GOAL.md — The goal (kit/GOAL.template.md:17). |
| **Resumption and recovery procedure** | How a new session reads state, verifies prior claims, selects the next action, and persists progress. | GOAL.md — Procedure (kit/GOAL.template.md:29). |
| **Current execution state** | Current phase, next action, gate outcomes, evidence pointers, and remediation counters. | `orchestration/STATE.md`, defined in LEDGER.md (kit/LEDGER.template.md:35). |
| **Durable decisions** | Pinned decisions, final design artifacts, and process-scaling choices that later sessions must preserve. | `orchestration/STATE.md` — Pinned decisions, defined in LEDGER.md (kit/LEDGER.template.md:58). |
| **Work and dependency registry** | Branch stacks, PR relationships, dispatch IDs, assignments, result locations, and task status. | `orchestration/STATE.md`, defined in LEDGER.md — Branch stack and Dispatch registry (kit/LEDGER.template.md:62). |
| **Event history** | Append-only records of decisions, dispatches, results, gates, incidents, user instructions, and environment changes. | `orchestration/LOG.md`, defined in LEDGER.md (kit/LEDGER.template.md:77). |
| **Individual work assignment** | Exact task instructions, inputs, ownership, constraints, verified facts, execution method, and required verification. Includes replacement and prompt-integrity rules. | `orchestration/dispatches/D-<id>.md`, defined by the dispatch template (kit/dispatches/D-\#\#\#.md:10). |
| **Individual work result and evidence** | Status, prompt hash, actual inputs, re-anchored references, raw evidence, findings, fixes, closure results, and gate verdicts. | `orchestration/dispatches/D-<id>.result.<kind>.md`, defined by the result template (kit/dispatches/D-\#\#\#.result.md:9). |
| **Supervisor dispositions** | Companion records such as findings tables and decisions about reviewer findings. | `D-<id>.<artifact>.md`, defined in the dispatch protocol (kit/dispatches/D-\#\#\#.md:31). |
| **Assumptions and unanswered questions** | Decisions made under uncertainty, reasons, consequences if wrong, override instructions, and eventual resolution. | QUESTIONS.md (kit/QUESTIONS.template.md:1). |
| **Deviations from the contract** | Evidence-backed records of contradictions between the delivered artifact and its governing instructions. | DEVIATIONS.md (kit/DEVIATIONS.template.md:7). |
| **Deferred work** | Minor findings, nits, and work outside the completion checklist. | `orchestration/BACKLOG.md`, named in LEDGER.md (kit/LEDGER.template.md:18). No dedicated template. |
| **Blocking decisions and escalation** | The exact decision that requires human input, or the failure that exhausted a remediation limit. | `orchestration/BLOCKED.md`, named in LEDGER.md (kit/LEDGER.template.md:32); worker `BLOCKED` sections and supervisor rules (kit/SUPERVISOR.template.md:38). |
| **Delivery record** | Final verification, delivery notes, remediation costs, and waived major findings. | `DELIVERY` notes referenced by SUPERVISOR.md (kit/SUPERVISOR.template.md:133) and GOAL.md (kit/GOAL.template.md:26). No dedicated template or fixed path. |
| **Kit evaluation and improvement** | Template verdicts, process costs, failures, proposed amendments, and the kinds of work the kit suits. | EVALS.md (kit/EVALS.template.md:1). `kit.json` already declares `evals.file` and `evals.axes`. |
| **Skill dependencies** | Required skills, their sources, discovery or explicit-read paths, and reasons for including them. | skills/README.md (kit/skills/README.template.md:1). |
| **Human-supplied context** | Manually adopted notes, feedback, and designs, with their provenance. | ctx/README.md (kit/ctx/README.template.md:1) and files in `ctx/`. |
| **Preserved working evidence** | Probe artifacts, process output, and other scratch material that supports results and survives the run. | `sslop/<dispatch-id>/`, governed by RAILS.md rule 24 (kit/RAILS.template.md:147). |

## Research references and interpretation

| Reference | What it contributes | Why I think you brought it here |
|---|---|---|
| **Jef Raskin** | Attention and habit are constraints on interface design. Repeated interactions become automatic, so consistency matters. [_The Humane Interface_, §2–3](<https://flylib.com/books/en/4.378.1.18/1/>) | Learning one kit should make the next kit easier. Stable names and locations let people attend to their work rather than reconstruct the kit’s organization. |
| **W. Bradford Paley** | His design methodology incorporates domain knowledge and draws on perception, language, and cognition. The representation should fit the subject and task. [_Interface and Mind_](<https://archive.dimacs.rutgers.edu/archive/Events/2009/abstracts/paley.html>) | The map should express recognizable concerns of doing work. “What needs my attention?” is a better organizing question than “Which template generated this file?” |
| **Edward Tufte** | Related information benefits from being visible together. Deep sequences of sparse screens make users reconstruct relationships from memory. [_iPhone interface design_](<https://www.edwardtufte.com/notebook/iphone-interface-design/>) | Keep the whole structure inspectable. Reduce administrative clutter while retaining meaningful distinctions and access to evidence. |
| **Hick’s law** | Hick studied choice reaction time and uncertainty among possible responses. This concerns the cost of choosing, rather than directly measuring long-term recall. [Hick, 1952](<https://journals.sagepub.com/doi/pdf/10.1080/17470215208416600>) | Give each category a recognizable purpose. Fewer headings help only if the reader can distinguish them; vague categories merely move uncertainty elsewhere. |
| **Conceptual maps and memory** | Theves and colleagues found hippocampal representations organized around conceptually relevant dimensions. Separately, Bower and colleagues found that hierarchical organization improved word-list recall. [Theves et al., 2020](<https://doellerlab.com/wp-content/uploads/2020/09/Theves-J-Neurosci-2020.pdf>), [Bower et al., 1969](<https://www.researchgate.net/publication/223321611_Hierarchical_Retrieval_Schemes_in_Recall_of_Categorized_Word_Lists>) | Group responsibilities by meaningful relationships so the category helps a person recover its contents. Preserve those relationships across kits, even when the files change. |
| **Shannon–Hartley theorem** | For a bandwidth-limited channel with additive white Gaussian noise, capacity is \\(C=B\\log\_2(1+S/N)\\). It describes reliable transmission under specified physical constraints. [Shannon, _Communication in the Presence of Noise_](<https://webusers.imj-prg.fr/~antoine.chambert-loir/enseignement/2018-19/shannon/shannon1949.pdf>) | I read this as a demand for efficient communication: preserve useful distinctions while reducing ambiguity and irrelevant material. Applying it to kit comprehension is an analogy, not a measured channel model of the brain. |

## Proposed one-level hierarchy

- **Purpose — What are we trying to achieve?**
  - Run identity and target
  - Intent and source requirements
  - Scope and acceptance criteria
  - Human-supplied context
- **Approach — How will we solve it, and what counts as done?**
  - Technical design and approach selection
  - Performance, cost, and technical validation
  - Artifact lifecycle and ownership
  - Completion contract
- **Rules — What agreements govern the work?**
  - Standing rules and their amendments
  - Build and behavior-preservation policy
  - Git integration and delivery policy
  - Review and remediation policy
  - Information-access boundaries
  - Writing conventions
- **Setup — What must be available to do the work?**
  - Agent entry point
  - Workspace preparation and isolation
  - Model requirements and selection
  - Skill dependencies
  - Agent execution transport
- **Work — What gets done, in what order?**
  - Execution workflow and process scale
  - Work and dependency registry
  - Individual work assignment
  - Resumption and recovery procedure
  - Deferred work
- **Progress — Where are we now, and what needs attention?**
  - Current execution state
  - Durable decisions
  - Event history
  - Assumptions and unanswered questions
  - Deviations from the contract
  - Blocking decisions and escalation
- **Evidence — What supports the result, and what can we learn?**
  - Kit provenance
  - Individual work result and evidence
  - Supervisor dispositions
  - Delivery record
  - Kit evaluation and improvement
  - Preserved working evidence

## Category boundaries

| If I want to know… | I look in… |
|---|---|
| What the user considers success | **Purpose** |
| What evidence will permit us to declare completion | **Approach** |
| How an independent review must operate | **Rules** |
| Whether the required reviewer, model, and workspace are available | **Setup** |
| Which review assignment runs next | **Work** |
| Whether that review is complete or blocked | **Progress** |
| What the reviewer found and why we accepted or rejected it | **Evidence** |
