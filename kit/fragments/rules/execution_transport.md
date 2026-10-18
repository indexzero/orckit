### Transport: native subagents when available, a detached CLI when not

Some hosts can spawn a subagent inside the running session. Use that
facility when it can select the pinned model and meet the verified context
capacity in RAILS rule 26. It must also support a fresh conversation,
without inherited authoring history. The dispatch must fit the session lifetime.
A native subagent
gives you a completion signal and no shell mechanics, so it is the better
default for reviews, research, and short builds.

When these conditions fail, use a fresh non-interactive CLI session if available.
For work that must outlive the supervisor, use a process manager with verified
lifetime guarantees. A background shell job alone does not establish persistence.
Send process output to the scratch directory of the dispatch.
Record the transport and process or agent identifier in the LOG.
Poll the result and process status when no completion signal exists.
If no available transport meets the requirements, record BLOCKED.

For Codex native dispatch, select `fork_turns="none"` when that control exists.
Pass only the dispatch pointer. An instruction to forget inherited history
does not create a fresh reviewer. See orckit's `playbooks/codex.md`.

Either transport sends the same pointer prompt and obeys the same rails.
The dispatch file, not the transport, is the assignment.

Always add these to a dispatch:
- the scratch directory, never /tmp
- the verification before DONE, as the exact commands whose raw output
  must appear in the report
- the git rules: atomic commits, no AI attribution footer
- every standing user directive, verbatim

