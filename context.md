
Look at the open issue I made on indexzero/orckits and then give me some options about how to parameterize these kits. It's clear that certain files are going to be more / less important when I am doing certain tasks: 1. Doing a batch of work on an established project 2. Making something new that's a "toy"(ish) (e.g. a gist, or a one-off webpage) 3. Porting something to Rust etc etc. Before you begin look at the issue, read the plan it cites and help me refine this idea via the complexity idea I have already loosely established in \~/Git/indexzero/mad-science/README.md using \~/Git/addyosmani/agent-skills/skills/{interview-me,idea-refine}/SKILL.md  

I’ll read the open issue and its linked plan first, then compare them with the complexity model in `mad-science`. I’ll use the interview-me and idea-refine skills to help shape the options.
```
• Ran gh issue list --repo indexzero/orckits --state open --limit 30 --json number,title,body,url
  └ [{"body":"## Plan\n\nhttps://github.com/robertdcurrier/korean_food_safety/blob/main/PLAN.md\n\n","number":1,"title":"Upstream artifacts to consider","url":"https://github.com/indexzero/o…
• Ran cat /Users/cjr/Git/addyosmani/agent-skills/skills/interview-me/SKILL.md /Users/cjr/Git/addyosmani/agent-skills/skills/idea-refine/SKILL.md
  └ - [ ] A "Not Doing" list makes trade-offs explicit
    - [ ] The output is a concrete artifact (markdown one-pager), not just conversation
    - [ ] The user confirmed the final direction before any implementation work
• Ran cat /Users/cjr/Git/indexzero/mad-science/README.md && cat /Users/cjr/Git/addyosmani/agent-skills/skills/idea-refine/frameworks.md /Users/cjr/Git/addyosmani/agent-skills/skills/idea-ref…
  └ 7. **The "Not Doing" list does real work.** It's specific and reasoned. Each item is something you might *want* to do but shouldn't yet.
    
    8. **The skill adapts to context.** A codebase-aware example references actual architecture. A process idea generates zero-cost experiments instead of products. The framework stays the s…
• Ran git status --short && rg -n 'complex|scal|axes|template|pipeline|small|toy' README.md create/kit kit/SUPERVISOR.template.md kit/EVALS.template.md kit/TECHNICAL.DESIGN.template.md
  └ create/kit:272:     evals: { file: "EVALS.md", axes: $axes },
    create/kit:296:if [ -z "$axes" ]; then
    create/kit:297:  echo "  4. Set evals.axes in kit.json — the graded axes are this run's"
• Calling deja.recall
• Ran gh api repos/robertdcurrier/korean_food_safety/contents/PLAN.md --jq .content | base64 --decode
  └ guide: what the target is, what data and labels exist, the modelling
    ladder from climatology to gradient boosting, evaluation as the
    expert's job, and where Claude helps and where it does not.
• Called deja.recall
  └ 41 more match(es) — call recall again with offset=3.
    
    </deja-recall>
• Calling deja.recall_context
• Explored
  └ Read README.md, TECHNICAL.DESIGN.template.md, SUPERVISOR.template.md, kit, refinement-criteria.md
• Ran gh api repos/indexzero/orckits/issues/1/comments --jq '.[] | {body,html_url}'
  └ (no output)
• Called deja.recall_context
  └ 
    Got it, I'll add UCAN. It's a useful test case because UCAN handles *authorization delegation* between DIDs, not identity linking. If the map can't place it cleanly, that's the kind of m…
    </deja-recall>
• Called deja.recall_context
  └ I updated `README.md`, and hairball stays in `stage/2`: - **Stages section:** a new paragraph says the stage records maturity, not importance, and that importance lives in the PROMPT.md …
    
    </deja-recall>
```
I read [issue \#1](<https://github.com/indexzero/orckits/issues/1>), its linked [PLAN.md](<https://github.com/robertdcurrier/korean_food_safety/blob/main/PLAN.md>), and your mad-science README (/Users/cjr/Git/indexzero/mad-science/README.md:20).

deja-vu recalled: you separated maturity, scale, and importance — I’m preserving those as distinct dimensions.

**My hypothesis:** you want each task to get the smallest planning and supervision structure that lets agents finish it with little oversight. **Confidence: \~80%.** The main uncertainty is whether you want different starting templates, a kit that grows during work, or both.

The linked plan is useful because one document carries several responsibilities: intent, technical choices, boundaries, open decisions, and later changes in scope. It also distinguishes the demonstration from the larger predictive-model project. We can borrow that structure without copying its domain-specific content.

That suggests a useful distinction: **a responsibility can remain necessary even when its separate file disappears.** A toy still needs a definition of Done. It probably does not need separate problem-statement, design, supervisor, and ledger documents.

Your existing model gives us three dimensions:

- **Maturity:** idea → designed → tried → used → relied on → stable.
- **Scale:** whether one agent can finish unattended from one document.
- **Importance:** how much you value or need the result.

Your examples introduce another: **kind of work**. A Rust port and an issue batch can have similar scale but need different evidence. I would avoid putting all four dimensions into a single “complexity” score.

Here are three initial options to explore:

| Option | How it works | Main trade-off |
|---|---|---|
| **Named profiles** | Start with `toy`, `batch`, `port`, or `new-project`. Each selects documents, sections, and gates. | Easy to choose, but combinations such as “toy Rust port” need exceptions. |
| **Independent dimensions** | Describe the work’s kind, maturity, and coordination needs. Derive the required artifacts and evidence. | Handles combinations, but can become a configuration system that needs its own manual. |
| **Progressive expansion** | Start with one plan. Split out design, state, dispatches, and reviews when the work needs them. | Low initial overhead, but expansion needs clear triggers so missing structure does not become missing discipline. |

My tentative preference is **profiles as starting points, with progressive expansion**. Keep the dimensions explicit enough to explain the choice, without requiring a large manifest first.

For your examples, the emphasis would change like this:

- **Established-project batch:** existing issues can supply the requirements. Ownership, dependencies, current state, and integration evidence deserve more attention. Your design template already allows this (kit/TECHNICAL.DESIGN.template.md:3).
- **Toy or one-off:** one document can hold intent, boundaries, decisions, and executable Done criteria. Separate orchestration files become useful only when coordination or recovery requires them.
- **Rust port:** the central artifact is a behavior contract: what must remain equivalent, what can change, and how to demonstrate both. Rust tooling is secondary to that contract.

**First question:** Should a single `PROMPT.md` or `PLAN.md` become the smallest supported form of an orckit, or remain outside orckit entirely?

**My guess:** make it the smallest form, with a clear path to expand it. That preserves your existing toy boundary while letting the same intent and evidence survive as the work grows.
```
  Worked for 1m 51s • 11:45 AM
```
In theory if it had all the appropriate sections. I think we need to approach this as a fundamental packaging problem. If each kit has a kit.json then that can delegate the functional responsibility to a specific relative file for the kit instance. To help map this out, please enumerate all such functional responsibilities that exist in the current kit template into a table I can view here citing which file hold this responsibility  

I’ll map the current templates by functional responsibility and cite each source file. That will show what `kit.json` would need to route, regardless of how many files an instance uses.
```
• Ran git status --short && rg --files kit && rg -n '^#{1,5} |^\*\*[^*]+:\*\*|^[0-9]+[a-z]?\. ' kit && cat create/kit
  └   echo "     data contract; name them before work begins, and never rename one"
      echo "     mid-lineage."
    fi
• Ran cat kit/PROBLEM.STATEMENT.template.md kit/TECHNICAL.DESIGN.template.md kit/GOAL.template.md kit/SUPERVISOR.template.md
  └   one-line justification each.
    - The dispatch header block is present verbatim.
    - A new agent given only this file and the ledger can run the pipeline.
• Ran cat kit/LEDGER.template.md kit/QUESTIONS.template.md kit/DEVIATIONS.template.md kit/EVALS.template.md kit/ctx/README.template.md kit/skills/README.template.md kit/AGENTS.template.md 'k…
  └ - A stranger can read the gate outcome from `tail -1` (gate kinds) or from
      the Status line (non-gate kinds) without reading prose.
    - Every claim in the Status line is backed by a section below it.
• Explored
  └ Read LEDGER.template.md, RAILS.template.md, kit
```
Yes. That makes **functional responsibility → location within the kit instance** the packaging contract. Several responsibilities can point to the same file.

Below is an inventory of the current kit. The responsibility names are descriptive labels, not proposed `kit.json` keys. Links point to the source templates; instance filenames omit `.template`.

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

The inventory exposes three packaging details:

- **Some responsibilities already share a file.** `STATE.md` holds current state, decisions, and work tracking.
- **Some responsibilities span files.** Review policy, review findings, and review dispositions have different owners and update rules.
- **Some locations are collections.** Dispatches, results, context, and scratch need a directory or collection mapping rather than one fixed file.

Your proposed delegation already has a small precedent: **`kit.json` contains `evals.file`**. Extending that pattern would let an instance place intent, design, and completion criteria in one `PLAN.md`, while another instance assigns each responsibility a separate file. Section references would make those shared-file assignments precise.
```
  Worked for 1m 31s • 11:52 AM
```
This is useful. Now map each of these responsibilities into a one-level deep only hierarchy with an eye for HUMAN COMPREHENSION, not machine comprehension emulating the wisdom of Jef Raskin, W. Bradford Paley, Edward Tufte, Hick's Law (applied to conceptual mapping as defined in hippocampal neuroscience research on human memory \& recall rates), and the Shannon-Hartley theorem which underpins much of our endeavor towards a humane cognetics kit for orchestration that can be customized in an interoperable way where value can be retained \& shared across kits instead of all or nothing. Prior to creating your map you MUST perform cursory research on any concept that I called out above and explain why you think I brought these into your active context window  

I’ll research the concepts you named first and explain how I think they bear on this map. Then I’ll group the responsibilities into one level of categories, with labels a person can recognize and recall.
```
• Browsing the web
• Searched the web for Jef Raskin humane interface cognitive conscious locus attention habituation, W Bradford Paley information design cognitive task user representation, Edward Tufte infor…
• Browsing the web
• Searched the web for Hick 1952 On the rate of gain of information reaction time paper pdf, Constantinescu O Reilly Behrens 2016 organizing conceptual knowledge humans gridlike code Science…
• Browsing the web
• Opened https://books.google.com/books?id=D39vjmLfO3kC
• Browsing the web
• Searched the web for "W. Bradford Paley" "Interface and Mind", "W. Bradford Paley" "domain" "task" site:didi.com, "The Hippocampus Maps Concept Space" paper, Bower Clark Lesgold Winzenz 19…
```
The research points toward stable labels and meaningful relationships that stay visible across kits. One distinction matters: Hick’s law concerns choice time, hippocampal studies concern conceptual representation, and Shannon–Hartley concerns channel capacity. I’ll use them as complementary guides, without treating them as a formula for the ideal number of categories.
```
• Browsing the web
• Searched the web for Brad Paley Interface Mind 2009 pdf, W Bradford Paley information design cognitive engineering textarc
• Browsing the web
• Opened https://didi.co/education/
```
I think you brought these references into context to make **the kit’s organization itself a tool for thinking**. A person should carry their understanding from one kit to another, find what they need after an interruption, and reuse useful parts without adopting an entire process.

I did a cursory review of the named concepts. The design implications below are my interpretation of that research.

| Reference | What it contributes | Why I think you brought it here |
|---|---|---|
| **Jef Raskin** | Attention and habit are constraints on interface design. Repeated interactions become automatic, so consistency matters. [_The Humane Interface_, §2–3](<https://flylib.com/books/en/4.378.1.18/1/>) | Learning one kit should make the next kit easier. Stable names and locations let people attend to their work rather than reconstruct the kit’s organization. |
| **W. Bradford Paley** | His design methodology incorporates domain knowledge and draws on perception, language, and cognition. The representation should fit the subject and task. [_Interface and Mind_](<https://archive.dimacs.rutgers.edu/archive/Events/2009/abstracts/paley.html>) | The map should express recognizable concerns of doing work. “What needs my attention?” is a better organizing question than “Which template generated this file?” |
| **Edward Tufte** | Related information benefits from being visible together. Deep sequences of sparse screens make users reconstruct relationships from memory. [_iPhone interface design_](<https://www.edwardtufte.com/notebook/iphone-interface-design/>) | Keep the whole structure inspectable. Reduce administrative clutter while retaining meaningful distinctions and access to evidence. |
| **Hick’s law** | Hick studied choice reaction time and uncertainty among possible responses. This concerns the cost of choosing, rather than directly measuring long-term recall. [Hick, 1952](<https://journals.sagepub.com/doi/pdf/10.1080/17470215208416600>) | Give each category a recognizable purpose. Fewer headings help only if the reader can distinguish them; vague categories merely move uncertainty elsewhere. |
| **Conceptual maps and memory** | Theves and colleagues found hippocampal representations organized around conceptually relevant dimensions. Separately, Bower and colleagues found that hierarchical organization improved word-list recall. [Theves et al., 2020](<https://doellerlab.com/wp-content/uploads/2020/09/Theves-J-Neurosci-2020.pdf>), [Bower et al., 1969](<https://www.researchgate.net/publication/223321611_Hierarchical_Retrieval_Schemes_in_Recall_of_Categorized_Word_Lists>) | Group responsibilities by meaningful relationships so the category helps a person recover its contents. Preserve those relationships across kits, even when the files change. |
| **Shannon–Hartley theorem** | For a bandwidth-limited channel with additive white Gaussian noise, capacity is \\(C=B\\log\_2(1+S/N)\\). It describes reliable transmission under specified physical constraints. [Shannon, _Communication in the Presence of Noise_](<https://webusers.imj-prg.fr/~antoine.chambert-loir/enseignement/2018-19/shannon/shannon1949.pdf>) | I read this as a demand for efficient communication: preserve useful distinctions while reducing ambiguity and irrelevant material. Applying it to kit comprehension is an analogy, not a measured channel model of the brain. |

These ideas do not establish a numerical optimum for our categories. They suggest a test: **can someone predict where a responsibility belongs, find it, and retain that understanding when moving to another kit?**

I propose seven groups. Each answers a human question. The map has exactly one level beneath those groups, and all **36 responsibilities** from the inventory appear once.

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

The boundaries matter more than the number of groups:

| If I want to know… | I look in… |
|---|---|
| What the user considers success | **Purpose** |
| What evidence will permit us to declare completion | **Approach** |
| How an independent review must operate | **Rules** |
| Whether the required reviewer, model, and workspace are available | **Setup** |
| Which review assignment runs next | **Work** |
| Whether that review is complete or blocked | **Progress** |
| What the reviewer found and why we accepted or rejected it | **Evidence** |

This separates expectations, activity, state, and proof without adding another hierarchy level. Those distinctions also make partial reuse more practical.

For interoperability, I would treat **the individual responsibilities as the reusable units**. The seven groups provide human orientation. They do not require seven files, seven directories, or seven indivisible packages.

A small kit could map several responsibilities to sections of one `PLAN.md`. A batch kit could distribute the same responsibilities across issue references, assignments, and a ledger. Their readers would still encounter the same conceptual landmarks.

For example, a Rust-port kit could contribute its behavior-preservation policy and review method to another kit. Its benchmark evidence could travel with the relevant assumptions and provenance. The recipient would not need to adopt its model selection, execution transport, or complete workflow.

There is one limit to file delegation: **a path tells us where content lives, but its responsibility tells us how to interpret it.** Shared definitions of the responsibilities—and explicit relationships to the evidence or assumptions they depend on—are what would let value survive a change of packaging.

I would evaluate this map with concrete retrieval tasks: find an unresolved assumption, locate the completion evidence, and identify a reusable review policy. Measure the first category chosen, retrieval time, and errors; repeat after a delay and in a differently packaged kit. That would test whether these labels actually support comprehension and transfer.

/Users/cjr/src/tries/2026-09-30-hack-the-planet/library/The\\ Humane\\ Interface\\ --\\ Jef\\ Raskin\\ --\\ 2000\\ --\\ Addison\\ Wesley.epub  

I’ll use this copy as the primary source for Raskin’s ideas and check whether it changes the proposed map, especially the grouping, naming, and reuse of responsibilities.
