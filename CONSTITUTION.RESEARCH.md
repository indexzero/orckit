# Constitution research

- **Charter – Foundational context. Read me first**
   - Questions
      - What are we trying to achieve? For who? Why?
      - What are the operating principles & working agreements between us?
      - What are the operating principles & working agreements between you & your team?
      - Do you have any questions or concerns about how I have specified how will work together?
      - All else being equal, when you are unsure about something how will we work together? And what counts as done
      - Does the work fit any pre-existing examples of successful delivery that can serve as additional guardrails?
   - Parameters & Output Templates
      - Initial Human-supplied context & scope
      - Distilled intent, source requirements & acceptance criteria
      - Technical design and approach selection
      - Performance, cost, and technical validation
      - Completion contract
   - Static Context
      - Human Review and Remediation Policy
- **Workflow – What is the order work gets done, and what must be available for each step?**
   - Questions
      - What must you do before starting work? And how do you clean up?
   - Context Scopes
      - Workflow selection (defines phases)
      - Per phase
         - Mechanics
            - Agent entry point
            - Workspace preparation and isolation
            - Agent execution transport
         - Skill dependencies
         - Model requirements & selection
         - Artifacts and dependency registry (e.g. starting from two sentences but cannot code until PLAN.md exists)
      - Execution workflow and process scale
      - Individual work assignment
      - Resumption and recovery procedure
      - Deferred work
- **Delivery – How will you deliver the work from end-to-end?**
   - Questions
      - How will you track progress for others to see?
      - How will we agree together that the work is done?
      - What do you do when you must make an assumption alone or deviate from our agreement(s)?
   - Context Scopes
      - Current execution state
      - Work assignments & their status
      - Build and behavior-preservation policy
      - Revision control integration and delivery policy (git, jj, etc.)
      - Adversarial review and remediation policy
      - Assumptions and unanswered questions
      - Deviations from any agreement in any other file
      - Blocking decisions and escalation
- **Trust - How can I trust that followed the rules we agreed to?**
   - Questions
      - How can I trust that the operator used this kit faithfully?
      - How can I trust that you are where you say you are in the work?
      - How can I see what decisions you made?
   - Context Scopes
      - Run identity & output target: target repository or artifact, relevant subdirectory, and starting revision
      - Kit provenance
      - Individual work result and evidence
      - Durable decisions
      - Event history
      - Supervisor dispositions
      - Delivery & escalation record
      - Kit evaluation and improvement
      - Preserved working evidence
- **Rules – What cross-cutting agreements or standards must govern the work & how it is accomplished?**
   - Questions
      - What are we missing in this kit when taken into consideration with the work as you now understand it?
      - What rules did the work reveal we need in the future?
      - What rules would be a better fit in one of the established sections above?
      - How can I be sure you will respect my writing style everywhere?
   - Context Scopes
      - Global Workflow Defaults
         - Information-access boundaries
         - Mechanics
            - Agent entry point
            - Workspace preparation and isolation
            - Agent execution transport
         - Model requirements & selection
         - Skill dependencies
         - Tool dependencies
         - System dependencies (e.g. `jq`, etc)
         - Artifacts and dependency registry (e.g. cannot start anything until external process completes)
      - Standing rules and their amendments
      - Writing conventions

## Reading the foundation

The opening list reproduces the saved [CONSTITUTION.md](CONSTITUTION.md). The supporting research below is organized around that foundation. The listed scopes describe responsibilities and content; they do not require a separate file for each item.

The Charter describes a parameterized process: given initial human context and working agreements, produce distilled requirements, a design, technical validation, and a completion contract. Its “Parameters & Output Templates” and “Static Context” distinguish what a particular effort supplies or produces from its surrounding agreements.

The lambda-calculus-like interpretation is abstraction and application: a kit describes a reusable operation; supplying its parameters gives that operation a particular application. This is a design interpretation, not a claim that the kit already defines a formal calculus or execution language.

| Section | Role in the process | Distinction to preserve |
|---|---|---|
| **Charter** | Establish inputs, expected outputs, and foundational agreements. | An output template describes content to produce; it does not imply that content already exists. |
| **Workflow** | Describe how content is produced, its dependencies, and the requirements for each phase. | A content dependency graph describes what must be available for a step. |
| **Delivery** | Track and govern execution, including assignments, status, review, integration, and completion. | An assignment and its status describe a particular execution of the workflow. |
| **Trust** | Preserve identity, provenance, decisions, history, and evidence supporting claims about the work. | Evidence supports a status claim and remains available for inspection. |
| **Rules** | Supply shared constraints, defaults, writing conventions, and amendments. | Global defaults can be referenced by phases; which settings can be overridden remains a design decision. |

Workflow's artifact dependencies and Delivery's work tracking serve different purposes. “The design requires distilled requirements” describes a content dependency. “An agent is assigned to produce the design and is blocked” describes execution. The original inventory combined aspects of both under “Work and dependency registry”; the foundation separates them.

“Individual work assignment” remains in Workflow, while “Work assignments & their status” appears in Delivery. The working interpretation is that Workflow defines an assignment's structure and requirements, while Delivery tracks actual assignments and their status.

## Functional responsibilities mapped to the foundation

All 36 responsibilities from [RESEARCH.md](RESEARCH.md) are retained below for traceability. Their original names and descriptions identify the existing kit responsibilities; the second column maps them to the new foundation. Supporting details remain definitions of those responsibilities, rather than additional foundation bullets.

Existing source paths refer to the current kit templates and generator. Generated instance filenames omit `.template`. These locations describe existing storage, not a required layout for future kits.

| Original responsibility | Home in the foundation | What it holds or governs | Existing kit source |
|---|---|---|---|
| **Human-supplied context** | Charter — Initial Human-supplied context & scope | Manually adopted notes, feedback, and designs, with their provenance. | ctx/README.md (kit/ctx/README.template.md:1) and files in `ctx/`. |
| **Intent and source requirements** | Charter — Distilled intent, source requirements & acceptance criteria | Original user statements, their interpretation, intended users, motivation, and confirmation status. | PROBLEM.STATEMENT.md (kit/PROBLEM.STATEMENT.template.md:8). |
| **Scope and acceptance criteria** | Charter — Initial context & scope; distilled acceptance criteria | Required outcomes, success criteria, constraints, exclusions, and decisions still open. | PROBLEM.STATEMENT.md (kit/PROBLEM.STATEMENT.template.md:30). |
| **Technical design and approach selection** | Charter — Technical design and approach selection | Background, research method, alternatives, observed behavior, trade-offs, and the selected solution. Can instead reference already specified work items. | TECHNICAL.DESIGN.md (kit/TECHNICAL.DESIGN.template.md:1). |
| **Performance, cost, and technical validation** | Charter — Performance, cost, and technical validation | Benchmarks, resource costs, ground truth, accuracy, discrepancies, and evidence supporting the design. | TECHNICAL.DESIGN.md (kit/TECHNICAL.DESIGN.template.md:74). |
| **Completion contract** | Charter — Completion contract; applied during Delivery | The evidence checklist that permits the whole run to become COMPLETE, plus legitimate stopping conditions. | GOAL.md — The goal (kit/GOAL.template.md:17). |
| **Review and remediation policy** | Charter — Human Review and Remediation Policy; Delivery — Adversarial review and remediation policy | Reviewer independence, findings severity, closure evidence, retry limits, waivers, and repro requirements. | RAILS.md — Reviews (kit/RAILS.template.md:100) and SUPERVISOR.md — Prime directives (kit/SUPERVISOR.template.md:19). |
| **Execution workflow and process scale** | Workflow — Workflow selection; execution workflow and process scale | Phases, dependencies, gates, delegation, supervisor duties, and which process steps the run can omit. | SUPERVISOR.md (kit/SUPERVISOR.template.md:113). |
| **Agent entry point** | Workflow — Per phase / Mechanics; Rules — Global Workflow Defaults | Which instructions a supervisor or worker reads, how paths resolve, and how an unfinished scaffold becomes a usable run. | AGENTS.md (kit/AGENTS.template.md:1). |
| **Workspace preparation and isolation** | Workflow — Per phase / Mechanics; Rules — Global Workflow Defaults | Worktree creation, starting revisions, bootstrap steps, permitted edit locations, and main-checkout cleanliness. | RAILS.md — Worktrees and bootstrap (kit/RAILS.template.md:23). |
| **Agent execution transport** | Workflow — Per phase / Mechanics; Rules — Global Workflow Defaults | Native versus CLI execution, fresh conversations, process lifetime, completion signals, and process tracking. | SUPERVISOR.md — Transport (kit/SUPERVISOR.template.md:81). |
| **Skill dependencies** | Workflow — Per phase; Rules — Global Workflow Defaults | Required skills, their sources, discovery or explicit-read paths, and reasons for including them. | skills/README.md (kit/skills/README.template.md:1). |
| **Model requirements and selection** | Workflow — Per phase; Rules — Global Workflow Defaults | Model IDs, context capacity, reasoning configuration, fallback rules, and reasons for each work item’s model choice. | RAILS.md — Model (kit/RAILS.template.md:152) and TECHNICAL.DESIGN.md — Model per item (kit/TECHNICAL.DESIGN.template.md:68). |
| **Individual work assignment** | Workflow — Individual work assignment; Delivery — Work assignments & their status | Exact task instructions, inputs, ownership, constraints, verified facts, execution method, and required verification. Includes replacement and prompt-integrity rules. | `orchestration/dispatches/D-<id>.md`, defined by the dispatch template (kit/dispatches/D-\#\#\#.md:10). |
| **Resumption and recovery procedure** | Workflow — Resumption and recovery procedure | How a new session reads state, verifies prior claims, selects the next action, and persists progress. | GOAL.md — Procedure (kit/GOAL.template.md:29). |
| **Deferred work** | Workflow — Deferred work | Minor findings, nits, and work outside the completion checklist. | `orchestration/BACKLOG.md`, named in LEDGER.md (kit/LEDGER.template.md:18). No dedicated template. |
| **Current execution state** | Delivery — Current execution state | Current phase, next action, gate outcomes, evidence pointers, and remediation counters. | `orchestration/STATE.md`, defined in LEDGER.md (kit/LEDGER.template.md:35). |
| **Work and dependency registry** | Delivery — Work assignments & their status; Workflow — Content dependencies | Branch stacks, PR relationships, dispatch IDs, assignments, result locations, and task status. | `orchestration/STATE.md`, defined in LEDGER.md — Branch stack and Dispatch registry (kit/LEDGER.template.md:62). |
| **Build and behavior-preservation policy** | Delivery — Build and behavior-preservation policy | Required suites, build prerequisites, visual baselines, coverage, and permitted behavior changes. | RAILS.md — Build, test, and goldens (kit/RAILS.template.md:53). |
| **Git integration and delivery policy** | Delivery — Revision control integration and delivery policy | Rebase procedures, generated-file handling, commit conventions, push restrictions, PR readiness, and merge conditions. | RAILS.md — Rebases; Git and PRs (kit/RAILS.template.md:72). |
| **Assumptions and unanswered questions** | Delivery — Assumptions and unanswered questions | Decisions made under uncertainty, reasons, consequences if wrong, override instructions, and eventual resolution. | QUESTIONS.md (kit/QUESTIONS.template.md:1). |
| **Deviations from the contract** | Delivery — Deviations from any agreement in any other file | Evidence-backed records of contradictions between the delivered artifact and its governing instructions. | DEVIATIONS.md (kit/DEVIATIONS.template.md:7). |
| **Blocking decisions and escalation** | Delivery — Blocking decisions and escalation | The exact decision that requires human input, or the failure that exhausted a remediation limit. | `orchestration/BLOCKED.md`, named in LEDGER.md (kit/LEDGER.template.md:32); worker `BLOCKED` sections and supervisor rules (kit/SUPERVISOR.template.md:38). |
| **Run identity and target** | Trust — Run identity & output target | Run name, creation time, target repository, optional subdirectory, and starting revision. | Generated `kit.json`, defined in create/kit:262. |
| **Kit provenance** | Trust — Kit provenance | Source kit revision, input file hashes, uncommitted-input flags, and permission to publish input digests in lineage records. | Generated `kit.json`, defined in create/kit:263. |
| **Individual work result and evidence** | Trust — Individual work result and evidence | Status, prompt hash, actual inputs, re-anchored references, raw evidence, findings, fixes, closure results, and gate verdicts. | `orchestration/dispatches/D-<id>.result.<kind>.md`, defined by the result template (kit/dispatches/D-\#\#\#.result.md:9). |
| **Durable decisions** | Trust — Durable decisions | Pinned decisions, final design artifacts, and process-scaling choices that later sessions must preserve. | `orchestration/STATE.md` — Pinned decisions, defined in LEDGER.md (kit/LEDGER.template.md:58). |
| **Event history** | Trust — Event history | Append-only records of decisions, dispatches, results, gates, incidents, user instructions, and environment changes. | `orchestration/LOG.md`, defined in LEDGER.md (kit/LEDGER.template.md:77). |
| **Supervisor dispositions** | Trust — Supervisor dispositions | Companion records such as findings tables and decisions about reviewer findings. | `D-<id>.<artifact>.md`, defined in the dispatch protocol (kit/dispatches/D-\#\#\#.md:31). |
| **Delivery record** | Trust — Delivery & escalation record | Final verification, delivery notes, remediation costs, and waived major findings. | `DELIVERY` notes referenced by SUPERVISOR.md (kit/SUPERVISOR.template.md:133) and GOAL.md (kit/GOAL.template.md:26). No dedicated template or fixed path. |
| **Kit evaluation and improvement** | Trust — Kit evaluation and improvement | Template verdicts, process costs, failures, proposed amendments, and the kinds of work the kit suits. | EVALS.md (kit/EVALS.template.md:1). `kit.json` already declares `evals.file` and `evals.axes`. |
| **Preserved working evidence** | Trust — Preserved working evidence | Probe artifacts, process output, and other scratch material that supports results and survives the run. | `sslop/<dispatch-id>/`, governed by RAILS.md rule 24 (kit/RAILS.template.md:147). |
| **Information-access boundaries** | Rules — Global Workflow Defaults / Information-access boundaries | Files agents cannot read, context that cannot enter the target repository, and separation between agent workspaces. | RAILS.md — Never commit, never read (kit/RAILS.template.md:132) and SUPERVISOR.md — Context hygiene (kit/SUPERVISOR.template.md:26). |
| **Standing rules and their amendments** | Rules — Standing rules and their amendments | Rules that bind every agent, plus recorded user directives that supersede those rules. | RAILS.md (kit/RAILS.template.md:11), including Amendments (kit/RAILS.template.md:180). |
| **Writing conventions** | Rules — Writing conventions | Language and formatting requirements for run artifacts, commit messages, and PR descriptions. | RAILS.md — Writing (kit/RAILS.template.md:171), which delegates to the writing playbook and prose check. |
| **Artifact lifecycle and ownership** | Open placement — not explicit in the foundation list | Who writes, changes, and commits produced artifacts; what survives cleanup; how mutable files merge. | TECHNICAL.DESIGN.md — Operational policy (kit/TECHNICAL.DESIGN.template.md:92). |

Artifact lifecycle and ownership has no explicit bullet in the saved foundation. It remains an open placement here rather than being silently added to the user's list.

Tool dependencies and system dependencies are explicit additions in the foundation under Rules. The original inventory had no separate rows for them. Human review and adversarial review now have separate homes. Revision control policy is also broader than the original Git-specific name.

## Finding a responsibility

| If I want to know… | I look in… |
|---|---|
| What initial context the human supplies | **Charter — Parameters & Output Templates** |
| What requirements, design, and validation content must be produced | **Charter — Parameters & Output Templates** |
| What counts as done | **Charter — Completion contract** |
| What human review agreement applies | **Charter — Static Context** |
| Which content must exist before another step can proceed | **Workflow — Artifacts and dependency registry** |
| What mechanics, skills, and models a phase needs | **Workflow — Per phase**, with defaults in **Rules** |
| What an individual assignment must contain | **Workflow — Individual work assignment** |
| Who is assigned, and whether their work is complete or blocked | **Delivery — Work assignments & their status** |
| How the run resumes after interruption | **Workflow — Resumption and recovery procedure** |
| How adversarial review and remediation must operate | **Delivery — Adversarial review and remediation policy** |
| How assumptions, deviations, and blockers are handled | **Delivery** |
| What the reviewer found and why findings were accepted or rejected | **Trust — Work results and supervisor dispositions** |
| What evidence supports the completion claim | **Trust — Delivery record and supporting evidence** |
| Which decisions must survive a new session | **Trust — Durable decisions** |
| Which shared standards, dependencies, and writing conventions apply | **Rules** |

## Parameterizing and packaging the foundation

The packaging contract remains **functional responsibility → relative location within a kit instance**, declared through `kit.json`. Several responsibilities can point to sections of one file. A responsibility that produces many artifacts can point to a collection. The existing `evals.file` field provides a small precedent.

Locations let a reader or tool resolve content. Shared meanings and declared dependencies let that content remain useful across kits. A toy can hold the Charter's outputs in one `PLAN.md`; another kit can assign separate files while preserving their meanings and dependency relationships.

The earlier options are now ways to configure the same foundation. They do not replace the responsibility-to-location contract.

| Option | How it applies to the foundation | Main trade-off |
|---|---|---|
| **Named presets** | A `toy`, `batch`, or `port` preset supplies initial parameters, output templates, workflow choices, and defaults. | Easy to start, but combinations such as a toy Rust port need composable choices. |
| **Independent dimensions** | Maturity, scale, importance, and kind of work inform which outputs, workflow steps, and evidence requirements receive emphasis. | Supports combinations, but configuration can become harder to understand than the work itself. |
| **Progressive expansion** | Add needed outputs or workflow steps and split files as the work grows, while retaining responsibility meanings and existing content. | Low initial overhead, but changes to the dependency graph and completion contract must remain understandable. |

Maturity, scale, importance, and kind of work remain distinct. A single complexity score would hide differences that affect what the kit needs to produce and verify.

## Research references and interpretation

These interpretations apply the earlier cursory research to the new foundation. None of these sources establishes an optimal number of sections for this kit. The Raskin entry incorporates the selected sections subsequently read from the supplied EPUB.

| Reference | What it contributes | Application to this foundation |
|---|---|---|
| **Jef Raskin** | Consistent operations support habit; content can provide retrieval cues; capabilities can be acquired incrementally. In §4-4, Raskin connects Hick's and Fitts' laws with Shannon–Hartley. [*The Humane Interface*, §§3-5, 4-4-2, 5-3, 5-7, 5-8, and 6-2](</Users/cjr/src/tries/2026-09-30-hack-the-planet/library/The Humane Interface -- Jef Raskin -- 2000 -- Addison Wesley.epub>) | Keep the meaning of inputs, outputs, and responsibilities recognizable across kits. Let people reuse a review procedure or output template without adopting an entire kit. Keep the content dependency graph inspectable without forcing repeated menu traversal. |
| **W. Bradford Paley** | His design methodology incorporates domain knowledge and draws on perception, language, and cognition. The representation should fit the subject and task. [*Interface and Mind*](https://archive.dimacs.rutgers.edu/archive/Events/2009/abstracts/paley.html) | Express the actual work: what context is supplied, what content must be produced, how production depends on other content, and what demonstrates trustworthy execution. |
| **Edward Tufte** | Related information benefits from being visible together. Deep sequences of sparse screens make users reconstruct relationships from memory. [*iPhone interface design*](https://www.edwardtufte.com/notebook/iphone-interface-design/) | Keep the five sections and their relationships inspectable together. A reader should be able to compare required content, actual progress, and supporting evidence. |
| **Hick's law** | Hick studied choice reaction time and uncertainty among possible responses. This concerns the cost of choosing, rather than directly measuring long-term recall. [Hick, 1952](https://journals.sagepub.com/doi/pdf/10.1080/17470215208416600) | Make each organizing question distinct. More nesting or fewer visible choices does not automatically make a responsibility easier to find. |
| **Conceptual maps and memory** | Theves and colleagues found hippocampal representations organized around conceptually relevant dimensions. Separately, Bower and colleagues found that hierarchical organization improved word-list recall. [Theves et al., 2020](https://doellerlab.com/wp-content/uploads/2020/09/Theves-J-Neurosci-2020.pdf), [Bower et al., 1969](https://www.researchgate.net/publication/223321611_Hierarchical_Retrieval_Schemes_in_Recall_of_Categorized_Word_Lists) | Preserve meaningful relationships across kits: supplied context, generated content, execution, and evidence. Test whether readers retain those distinctions after interruption and when switching kits. |
| **Shannon–Hartley theorem** | For a bandwidth-limited channel with additive white Gaussian noise, capacity is $C=B\log_2(1+S/N)$. It describes reliable transmission under specified physical constraints. [Shannon, *Communication in the Presence of Noise*](https://webusers.imj-prg.fr/~antoine.chambert-loir/enseignement/2018-19/shannon/shannon1949.pdf) | Preserve useful distinctions while reducing ambiguous labels and irrelevant material. Its application to kit comprehension is an analogy, not a measured channel model of the brain. |

## Questions for refinement

- Where should artifact lifecycle and ownership live in the foundation?
- Does the distinction between assignment structure in Workflow and actual assignments in Delivery express the intended boundary?
- Which global defaults may a phase override, and how are overrides represented?
- What makes a content dependency ready: presence, conformance to an output template, review, or a requirement declared by the consuming step?

These are design questions, not new responsibility bullets. A useful evaluation is to ask someone to locate required content, an assignment's status, an unresolved assumption, and completion evidence. Record their first section choice, retrieval time, and errors; repeat after a delay and in a differently packaged kit.
