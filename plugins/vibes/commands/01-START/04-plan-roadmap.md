---
description: Scope the whole project with the graph-engineering skill and save the approved graph as the roadmap every later command follows
argument-hint: Optional constraints like timeline or priorities
allowed-tools: Read, Glob, Grep, Agent, Skill, AskUserQuestion, Write, Edit, Bash(date:*)
---

# Planning phase

You are helping a vibe coder create a clear implementation roadmap. This phase takes everything from discovery, scope, and architecture and turns it into phases, then saves every task in the project as a checklist that later commands read and tick off, which is what keeps the project from drifting.

## Full project context

**Optional constraints:** $ARGUMENTS

**Auto-loaded context (if files exist):**
@docs/01-START/01-discover.md
@docs/01-START/02-scope.md
@docs/01-START/03-architect.md
@docs/01-START/04-plan-roadmap.md
@docs/01-START/roadmap.md

**Check what loaded above:** If discovery, scope, and architecture content appear, synthesize them into a roadmap. If some docs are missing, ask the user to describe the missing context or suggest running earlier START commands first.

**Existing roadmap:** If `docs/01-START/roadmap.md` loaded above, this project already has a task checklist. Update it rather than starting over, and keep every ticked task ticked.

## Your role

**Use the AskUserQuestion tool for every question to the user. Never ask questions as plain text output.** The AskUserQuestion tool gives a guided, interactive experience with structured options. Every user question must go through this tool.

You do the heavy lifting on planning. Create a roadmap the user can follow step-by-step without needing to make technical decisions. Each phase should be clear about what gets built and how the user will know it's working.

**Think step by step (ultrathink)** for any complex reasoning, phase sequencing, or dependency analysis. This ensures systematic, thorough thinking. Ultrathink through build order before presenting conclusions.

## How to communicate

- Use AskUserQuestion for every decision, and present options with plain language tradeoffs
- Lead with recommendations: "I'd suggest building X first because [reason]. Then Y. Does that make sense?"
- Explain build order in terms of what the user will see working, not technical dependencies
- Keep phases small and achievable, because big phases feel overwhelming

## Planning process

### 1. Context verification (required)

If all planning docs exist, summarize the key insights:
- What we're building (problem and value proposition)
- Who we're building for (target users)
- MVP feature set
- Key technical decisions from architecture

**Use AskUserQuestion:**
```
Question: "Before I create your roadmap, let me confirm I understand the complete picture:

[Summarize: Problem, Users, MVP Features, Technical Foundation]

Is this accurate?"
Options:
- Yes, that's right
- Mostly right, but let me clarify something
- We should revisit earlier planning first
```

If docs don't exist (common when using claude-vibes on an existing project), use AskUserQuestion to gather:
- What is the project about and who are the users?
- What features need to be built (MVP scope)?
- What technical decisions have already been made?

Then proceed with roadmap planning based on the user's answers.

### 2. Gather what the graph needs

Collect, do not decide. The `graph-engineering` skill owns the build order, the checks, and the approval points, so this step only makes sure it starts with the full picture.

**A project is more than its code.** List every piece of work that has to happen for the project to succeed, and give each one a type:

- `build`: code, planned and written with the BUILD commands
- `brand`: name, positioning, voice, visuals (the BRAND commands)
- `content`: copy, scripts, images, documentation (the TOOLKIT commands)
- `research`: market, competitor, or technical questions that must be answered first
- `setup`: accounts, domains, hosting, payments, app store listings, analytics
- `legal`: terms, privacy policy, business entity, licences
- `launch`: announcements, outreach, pricing pages, support channels
- `manual`: anything only the user can do, such as signing a contract or recording a video

Ask the user about the non-code work with AskUserQuestion, because discovery and scope documents rarely mention it. A roadmap that lists only code leaves the rest of the project untracked.

Also note, without resolving them:
- Dependencies you already know about ("user accounts have to exist before anything is saved per user")
- What the user has already ruled out or deferred in `02-scope.md`
- Constraints on time, money, access, and permissions
- Risks and unknowns: technical uncertainty, outside services the project depends on, decisions that might change the plan, and places where scope could grow

## Guidelines

- Keep phases small, because it's better to have more small wins than fewer big ones
- Build risky/uncertain things early, because it's better to discover problems sooner
- Each phase should produce something visible and testable
- Don't plan the later phases in too much detail, since they'll likely change
- Include wiggle room, because things take longer than expected

## Frameworks reference

The `jtbd-psychographic-research` skill provides frameworks that may auto-activate during this conversation:
- Jobs-to-be-Done (prioritize features that address core jobs first)
- Four Forces of Progress (reduce anxiety by building confidence-building features early)

Use these frameworks when deciding what to build first.

## Natural writing

Before you write anything yourself in this command, such as a summary or a saved document, **use the Skill tool** to invoke `claude-vibes:natural-writing`, apply its method while drafting, and run its structural audit before showing the draft. Add its "What changed" section only when you are revising text the user gave you.

## Output

When planning feels complete:

### Step 1: Save the reasoning

1. Ensure `docs/01-START/` directory exists

2. Save `docs/01-START/04-plan-roadmap.md` as the narrative behind the plan:
   - Project summary (what we're building and why, in plain language)
   - Why the phases are in this order
   - Key milestones and how to know they're achieved
   - Risks and unknowns to watch for

Keep task lists out of this file. Task state lives only in `roadmap.md` (Step 3), and if the two ever disagree, `roadmap.md` wins.

### Step 2: Engineer the project graph

**Use the Skill tool** to invoke `claude-vibes:graph-engineering`, with the whole project as its objective. The skill aligns with the user, then designs the smallest useful graph of jobs, with real dependencies, separate checks, and human approval points, and it stops when the user approves the graph. It designs the work and never runs it.

Give the skill everything already settled so it confirms instead of re-asking: the discovery, scope, and architecture documents, the phases and milestones from this session, and the work types from step 3. Tell it that:
- The graph covers all the work in the project, including brand, content, research, setup, legal, launch, and things the user does by hand, as well as code.
- Each job needs one owner: a named command (for example `01-plan-code` then `02-write-code`, or `02-create-tagline`), or "you, by hand" with the steps.
- Each job's output must be something the user can check for themselves.
- Reviews are separate jobs with a different owner from the work they check, for example `03-review-code` after a build job.
- Human approval points go before anything expensive or hard to undo: spending money, publishing, legal commitments, deleting or migrating data, contacting customers.

Let the skill run its full process, including its alignment contract and its own audit of the graph. Do not shorten it, and do not start any job.

**If the skill judges the project too simple for a graph**, which it is designed to do, say so plainly and write the phases and tasks straight into the template in Step 3, leaving out the Graph and Decisions sections.

### Step 3: Save the approved graph as the roadmap

Once the user approves the graph, save it to `docs/01-START/roadmap.md`, so that each job leaves a record later sessions can inspect. `/01-plan-code`, `/02-write-code`, and `/05-track-progress` all read this file before doing anything, and tick jobs off as they finish.

**If `roadmap.md` already exists**, edit it in place with Edit and never replace it with Write. Keep every `- [x]` line with its date, and keep the whole change log. Add new tasks, note removed ones in the change log, and append a dated line. Use the template below only when the file does not exist.

**Dates:** run `date +%Y-%m-%d` before writing any date. Never guess it.

```markdown
# Roadmap: [Project name]

Every command reads this file before it works and ticks tasks off when they are done. Change it on purpose, and note why in the change log at the bottom.

Last updated: [YYYY-MM-DD]

## Alignment contract

What we agreed this project is, before anyone starts. If a new idea changes this, the plan gets redone, not patched.

- Objective: [what the project is for]
- Done means: [the terminal result and how success is judged]
- Optimize for: [what matters most, in the user's order]
- In scope: [...]
- Decisions that stay with you: [...]
- Constraints: [time, money, access, permissions]

## Graph

Who does what, and in what order. `check` lines are someone else marking the work, and `gate` lines are decisions only you can make.

[The approved mermaid diagram from graph-engineering. Label each node with its task ID and its plain role name, so the diagram and the checklist match]

## Decisions

[One line per material decision from the graph: what it decides, who owns it, what evidence settles it, and what would change it]

## How this runs

- Shared state: every command reads this file first and writes its result back here.
- Execution level: [the level graph-engineering recommended]

## Phase 1: [Name]

Goal: [plain-language goal]
Done when: [what the user can see or do]

- [ ] 1.1 [Task] | type: build | how: 01-plan-code, then 02-write-code | done when: [checkable output]
- [ ] 1.2 [Review of 1.1] | type: check | how: 03-review-code | depends on: 1.1 | done when: [checkable output]
- [ ] 1.3 [Task] | type: setup | how: you, by hand ([the steps]) | depends on: 1.1, 1.2 | gate: your approval before starting | done when: [checkable output]

## Later

[Good ideas that are deliberately not in this version]

## Not doing

[The contract's non-goals and anything else ruled out, each with its reason, so they do not creep back in]

## Change log

- [YYYY-MM-DD]: Roadmap created from the approved graph.
```

**Line format.** The other commands parse these lines, so keep to it exactly:
- One line per task: `- [ ] <id> <task> | type: <type> | how: <owner> | depends on: <id>, <id> | gate: <approval needed> | done when: <output>`. Leave out `depends on` and `gate` when a task has none.
- No `|` and no line break inside a field. Use a comma instead.
- IDs are `<phase>.<number>`. A subtask takes its parent's ID plus a letter (`2.3a`), and the parent is ticked only when all its subtasks are.
- Types are `build`, `brand`, `content`, `research`, `setup`, `legal`, `launch`, `manual`, and `check`.
- A finished task becomes `- [x] ... | done: <YYYY-MM-DD>`.
- A `check` that fails is unticked again, along with the task it reviewed, and gets `| note: failed <YYYY-MM-DD>, <what failed>`.
- Every job in the approved graph appears as exactly one task, including its skeptic and review jobs (`check`) and its human approval points (`gate`). If you cannot write a done-when line for a job, it is too vague, so take it back to the graph.

**If the project has an old Taskmaster folder** (`.taskmaster/tasks/tasks.json` exists): read the file directly. Older files look like `{"tasks": [...]}` and newer ones wrap the list in a tag, such as `{"master": {"tasks": [...]}}`. Give the task list to the graph-engineering step as existing context. When saving, tick tasks whose status is `done`, put `deferred` ones under "Later" and `cancelled` ones under "Not doing", treat them as `build` unless the title says otherwise, and ask the user for a done-when line where one cannot be inferred. If the file will not parse, say so and carry on without it. Leave the `.taskmaster/` folder untouched.

### Step 4: Independent review of the saved roadmap

**Use the Agent tool to launch the plan-reviewer agent:**

```
Agent tool:
  subagent_type: "claude-vibes:CODING:plan-reviewer"
  prompt: "Review the saved roadmap at `docs/01-START/roadmap.md` against its alignment contract and against the other docs/01-START/ files. ultrathink

  Check:
  1. Coverage: does every feature in 02-scope.md, and every kind of non-code work the project needs, appear as a task?
  2. Dependencies: is anything ordered before something it needs?
  3. Architecture: can the decisions in 03-architect.md support this order?
  4. Done-when lines: can the user check each one for themselves?
  5. Checks and gates: does every build task have a separate check, and does an approval gate sit before anything expensive or hard to undo?
  6. Size: does each task fit in one focused session?

  Report concerns with severity (blocker or consideration) and a suggested fix in plain language. Do not edit the roadmap."
```

Take each blocker to the user with AskUserQuestion, then edit the roadmap in place and add a dated change-log line for what changed.

### Step 5: Congratulate

"Your project is fully planned.

**Documentation** (in `docs/01-START/`):
- 01-discover.md: the problem and who it is for
- 02-scope.md: what is in and out
- 03-architect.md: the technical foundation
- 04-plan-roadmap.md: why the plan is shaped this way
- roadmap.md: the approved graph as a checklist of every task, which every command keeps up to date

**What to do next:**
Run `/05-track-progress` at any time to see where the project stands and what comes next, whatever kind of task it is. When the next task is code, run `/01-plan-code` and it will pick that task up from the roadmap."
