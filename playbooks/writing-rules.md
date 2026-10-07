# The writing rules

Every run artifact is a procedure for a reader that cannot ask questions.
A subagent reads a dispatch once and acts. A new supervisor reads the
ledger after a compaction and resumes. A tired human reads a BLOCKED file
at the end of a day. None of them can ask what a sentence meant.

The kit therefore writes in Simplified Technical English, the controlled
language of ASD-STE100. The rules below are the structural half of that
standard, paraphrased for software. The official standard is a free
download at asd-ste100.org. A fuller skill-shaped treatment, with the slop
substitution table, is the `simple-english` skill many agent CLIs can load.

## Classify first

| | Procedural | Descriptive |
|---|---|---|
| Purpose | Tell the reader what to do | Explain what a thing is or does |
| Verb form | Imperative: "Run the suite." | Simple present, past, or future |
| Sentence limit | 20 words | 25 words |
| Unit | One instruction per sentence | One topic per paragraph, six sentences at most |

A dispatch is procedural. A problem statement is descriptive. A note inside
a procedure is descriptive. Do not mix the two in one passage.

## The rules that matter most

1. **One word, one meaning.** Pick one verb for the check-verify-confirm
   idea. The kit uses "make sure that" for the instruction and
   "verification" for the noun. Pick one noun for config-settings-options.
   Use no other word for that idea in the whole document.
2. **Approved modals: can, will, must.** Never `should`, `would`, `may`,
   `might`, or `could`. A requirement is `must`. A suggestion is stated as
   fact or deleted. An agent reads `should` as optional.
3. **Active voice.** Passive is legal in descriptive text only when the
   agent is unknown.
4. **Condition before command.** "If the build fails, read the log." Never
   "Read the log if the build fails."
5. **Keep the grammar.** Short sentences with articles and "that". Not
   telegraph style. "Make sure that the file exists" is right. "Ensure
   file exists" is wrong.
6. **No semicolon.** Write two sentences.
7. **No dash as punctuation.** An em dash or an en dash inside a sentence
   becomes a period, a comma, or a colon. A dash in a heading that acts as
   a separator is allowed.
8. **No contractions.**
9. **One new fact per sentence.** Give information gradually.
10. **A vertical list for complex text.** When a sentence carries three or
    more parallel items, make it a list.
11. **Delete slop.** "Leverage" is "use". "In order to" is "to". "Ensure"
    is "make sure that". "It is worth noting that" is deleted. "Simply",
    "just", "robust", and "seamlessly" are deleted.
12. **Count identifiers as one word.** A path, a command, or a quoted error
    in backticks counts as one word. Long identifiers do not break the
    sentence limit.

## Untouchables

Leave these exact, even where they break a rule:

- code blocks and inline code
- identifiers, CLI commands, flags, and file paths
- quoted error messages
- quoted prompts that an agent must receive verbatim
- product names
- numbers with units

## The self-check

Run `checks/prose-lint.sh` on the file. Then do what a script cannot:

1. Count the words in your three longest sentences. Split any over the
   limit.
2. Find every "if" and "when". Make sure that each one starts its sentence.
3. Find the verbs you did not pick in rule 1. Replace every hit.

## Where the rules bind

RAILS rule 27 binds every run artifact: the problem statement, the rails,
the supervisor, dispatches, results, ledger entries, questions, deviations,
commit bodies, and PR bodies. The kit templates obey the rules themselves.
A template that breaks them teaches the break to every run.
