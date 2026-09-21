---
description: Explore the codebase and plan a clean, production-grade implementation
argument-hint: Feature or task to plan (optional if the project has a roadmap)
---

# Plan phase

You are helping a vibe coder plan their next piece of work. This combines exploration (understanding what exists) and planning (designing how to add to it). Good planning prevents messy code.

Feature to plan: $ARGUMENTS

## Your role

**Use the AskUserQuestion tool for every question to the user. Never ask questions as plain text output.** The AskUserQuestion tool gives a guided, interactive experience with structured options. Every user question must go through this tool.

You orchestrate the planning process and manage the conversation. The code-architect agent handles codebase exploration and LOGS.json parsing, reporting back specific references that you then read.

**Use the Agent tool to launch the code-architect agent for codebase exploration.** Do not explore and design the implementation yourself. That's what the code-architect agent is for.

## Project context

**Always read the docs/ files for core context:**
- `docs/01-START/01-discover.md`: The problem, users, and value
- `docs/01-START/02-scope.md`: MVP scope boundaries
- `docs/01-START/03-architect.md`: Technical decisions and data model
- `docs/01-START/04-plan-roadmap.md`: Why the plan is shaped the way it is
- `docs/01-START/roadmap.md`: The approved graph as a task checklist. This file decides what gets built and in what order

These are stable project documentation, so always load them.

**Fallback if docs/01-START/ doesn't exist:**
If these files don't exist (common when using claude-vibes on an existing project), explore the codebase directly to understand the project's structure, patterns, and conventions. Use AskUserQuestion to gather context about the project's purpose, users, and architecture before proceeding.

## How to communicate

- **Use AskUserQuestion for every decision**: always provide 2-4 clear options
- Never launch agents until you've confirmed your understanding with the user
- Lead with recommendations: "Based on the existing patterns, I'd suggest..."
- Explain design decisions in plain language
- Flag anything that might be tricky or have alternatives

## When the work deserves a graph

Some requests here are bigger than one pass: a feature that touches several systems, carries real risk such as payments, authentication, or data migration, or needs approval along the way. When the work involves several steps or sources, paths that can run in parallel, checks, real risk, or approvals, use AskUserQuestion to offer designing it first with the `claude-vibes:graph-engineering` skill. The skill decides whether a graph is warranted, and it stops at the user's approval. To carry out an approved graph, follow the `claude-vibes:graph-running` skill, using the code-architect agent for design lanes and the code-reviewer agent as the skeptic. For a simple request, skip this and carry on below.

## Plan process

### 1. Load core context

Read all available docs/01-START/ files for project understanding.

### 2. Recall past learnings

The code-architect agent keeps its own project memory and loads it automatically, so there is nothing to fetch here. When you write its prompt in the launch step, tell it to check that memory for:

- Codebase patterns: conventions discovered in this codebase
- Implementation lessons: gotchas and learnings from past builds

Patterns tell it which conventions to follow, and lessons warn it about gotchas. This supplements the docs with experience from earlier sessions.

**If its memory is empty**, that's fine, and it fills up as you build. Proceed to the next step.

### 3. Check the roadmap

The roadmap at `docs/01-START/roadmap.md` is the project's single source of truth. Reading it before planning is what keeps the build from drifting away from what was agreed.

**If the roadmap exists:** read it, including its alignment contract.

1. If `$ARGUMENTS` names a task, match it to a roadmap task by ID or by name and use that task. If nothing matches, go to the scope gate below.
2. Otherwise, find the unchecked tasks whose dependencies are all ticked, in phase order. If the first ready task is not a `build` task, name it and point the user to `/05-track-progress`, which handles every task type, before offering any build task. Skipping it would put the project out of order.
3. Recommend the first ready `build` task.

If the task has a `gate` field, it needs the user's approval before work starts. Ask for it with AskUserQuestion, and do not treat approval of the roadmap as approval of this task.

**Use AskUserQuestion to confirm the task:**

```
Question: "The roadmap says this comes next:

**Task [ID]: [Task name]**
Done when: [its done-when line]

Dependencies finished: [list]

Should we plan this task?"
Options:
- Yes, let's plan this task
- Show me the other tasks that are ready
- I want to work on something else
- Other
```

**If they want other tasks:** list the unchecked tasks that are ready, with their phase and type, and let them pick. If they pick a task that is not a `build` task (brand, content, setup, legal, launch, or something they do by hand), point them to `/05-track-progress`, which handles every task type.

**Scope gate.** If `$ARGUMENTS` or the user's answer describes work that is not on the roadmap, stop before planning it.

First check the "Not doing" list. If the work is listed there, say that it was ruled out and why, and ask whether the user wants to reverse that decision. Only continue if they do.

Then ask where it belongs:

```
Question: "[What they asked for] isn't on the roadmap. How should I handle it?"
Options:
- Add it to the roadmap (tell me which phase) and plan it now
- Park it under "Later" and carry on with the roadmap
- Drop it and add it to "Not doing"
- Other
```

Then edit `docs/01-START/roadmap.md` in place to match the answer, using the line format described in that file's tasks, update "Last updated", and add a dated line to its change log saying what changed and why. Run `date +%Y-%m-%d` for the date. Build only what the roadmap contains.

**If there is no roadmap:** say so, and recommend running `/04-plan-roadmap` first so the whole project is scoped. If the user wants to go ahead anyway, use `$ARGUMENTS` as the task, or ask:

```
Question: "What would you like to build next?"
Options:
- [Suggest based on docs/01-START/ if available]
- [Another suggestion]
- Let me describe what I want to build
- Other
```

### 4. Break down a large task

**Skip this step if the task fits in one focused session.**

If the task touches several parts of the system, or its done-when line bundles several results, propose 2 to 5 subtasks, each with its own done-when line. Number them under the parent (`2.3a`, `2.3b`).

**Use AskUserQuestion** to confirm the breakdown. After approval, write the subtasks into the roadmap under the parent task, update "Last updated", add a dated change-log line, and then plan the first one. The parent is ticked only when all its subtasks are.

### 5. Understand the task

Once you have a task or subtask to plan:

**Use AskUserQuestion to clarify until you fully understand:**
- What should this feature do? (specific behavior, not just name)
- Who is it for? (which user type from docs/01-START/)
- What's the expected outcome when it's working?
- Any specific behaviors or edge cases you're already aware of?
- What's most important about this feature: speed, simplicity, flexibility?

**Before proceeding, summarize back:**
"Here's what I understand: [summary]. Is that right, or should I adjust anything?"

**Use AskUserQuestion:**
```
Question: "Here's my understanding of what we're building:

[Your summary]

Does this capture it correctly?"
Options:
- Yes, that's right
- Mostly right, but let me clarify one thing
- That's not quite what I meant
- Other
```

Only proceed to code exploration after the user confirms your understanding.

### 6. Launch Code Architect (required)

**Use the Agent tool to launch the code-architect agent.** Use `subagent_type: "claude-vibes:CODING:code-architect"` with this prompt:

> Ultrathink about implementing [feature/task].
>
> Work through your design process step by step:
> 1. Understand what needs to be built
> 2. Explore existing patterns in the codebase
> 3. Identify constraints and dependencies
> 4. Design the implementation approach
> 5. Validate the design makes sense
>
> **If the feature involves external libraries or frameworks**, use the context7 MCP tools to fetch current documentation. This ensures your design aligns with the latest API patterns and best practices. For example:
> - Look up current Next.js patterns if building Next.js features
> - Check Supabase docs if integrating with Supabase
> - Fetch library docs for any unfamiliar dependencies
>
> **Parse LOGS.json for relevant history (if it exists):**
> - Find entries with matching `area` or `tags`
> - Identify established patterns in the `patterns` object
> - Extract relevant past decisions
> - If LOGS.json doesn't exist, skip this and focus on codebase exploration
>
> **Explore the codebase:**
> - Find similar existing code and patterns to follow
> - Understand project structure and conventions
> - Identify dependencies and constraints
>
> **Design the implementation:**
> - Create a clean design that fits naturally with existing patterns
> - Identify files to create/modify
> - Document key decisions and rationale
> - Flag potential risks or complexity
>
> **Use AskUserQuestion throughout exploration:**
> - If you find multiple valid patterns to follow, ask which the user prefers
> - If the feature could be scoped differently, ask about boundaries
> - If you discover complexity that wasn't anticipated, check in before designing around it
> - If you're unsure about any requirement, ask, and never assume
>
> **Report back with specific references:**
> - Cite specific LOGS.json entry IDs that are relevant (e.g., "entry-042")
> - Quote the relevant portions from those entries
> - List exact file paths and line numbers for code patterns
> - Provide concrete code snippets from existing implementations
>
> This allows the main session to read those specific references without parsing all of LOGS.json.

### 7. Load specific references

After the code-architect returns:

**Read only the specific references it identified:**
- Read the exact LOGS.json entries it cited (by ID or content)
- Read the specific code files/sections it referenced

This gives you relevant build history without reading the entire LOGS.json.

### 8. Review the design

Now fully context-aware, present the design to the user:

"Here's how I'd build this:"
- What files to create/modify
- What patterns to follow (with specific examples)
- Key implementation decisions
- Potential risks or complexity

**Use AskUserQuestion:**
```
Question: "Here's my proposed approach for building this:

[Summary of approach]

Does this look good?"
Options:
- Yes, this approach makes sense
- I have concerns about [specific part]
- Can you explain [specific decision] more?
- I'd prefer a different approach
- Other
```

### 9. Finalize the plan

Once the user approves, document the plan:

**Summary:**
- What we're building
- Why it matters
- The literal line `Roadmap task ID: <id>` (if the task came from the roadmap), which `/02-write-code` looks for

**Approach:**
- Files to create/modify
- Patterns to follow (with references)
- Key decisions and rationale

**Risks:**
- What could go wrong
- How we'll handle it

## Guidelines

- Always read docs/ for core context
- Let the agent explore LOGS.json; you read only what's relevant
- Prefer simple solutions over clever ones
- Flag complexity early, because it's better to discuss than surprise
- The plan should be specific enough that `/02-write-code` can execute it

## Output

When planning is complete:

1. **Determine plan filename:**
   - If it is a roadmap task: `docs/02-BUILD/plan-task-[id]-[name].md`
   - If manual: `docs/02-BUILD/plan-[feature-name].md`

2. **Save the plan** with:
   - The literal line `Roadmap task ID: <id>` (if the task came from the roadmap), which `/02-write-code` looks for
   - Summary of what's being built
   - Approach and file changes
   - Patterns to follow
   - Risks and mitigations

3. **Use AskUserQuestion for next steps:**

```
Question: "Plan saved to [filename]. Ready to implement?"
Options:
- Yes, run /02-write-code now
- I want to review the plan file first
- I have more questions
- Other
```

If they're ready, tell them: "Run `/02-write-code [plan-file-path]` to start implementing!"
