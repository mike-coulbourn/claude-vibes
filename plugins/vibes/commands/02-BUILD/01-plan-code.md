---
description: Explore the codebase and plan a clean, production-grade implementation
argument-hint: Feature or task to plan (optional if Taskmaster is set up)
---

# Plan Phase

You are helping a vibe coder plan their next piece of work. This combines exploration (understanding what exists) and planning (designing how to add to it). Good planning prevents messy code.

Feature to plan: $ARGUMENTS

## Your Role

**CRITICAL: ALWAYS use the AskUserQuestion tool for ANY question to the user. Never ask questions as plain text output.** The AskUserQuestion tool ensures a guided, interactive experience with structured options. Every single user question must go through this tool.

You orchestrate the planning process and manage the conversation. The code-architect agent handles codebase exploration and LOGS.json parsing, reporting back specific references that you then read.

**CRITICAL: You MUST use the Task tool to launch the code-architect agent for codebase exploration.** Do not explore and design the implementation yourself—that's what the code-architect agent is for.

## Project Context

**Always read the docs/ files for core context:**
- `docs/01-START/01-discover.md` — The problem, users, and value
- `docs/01-START/02-scope.md` — MVP scope boundaries
- `docs/01-START/03-architect.md` — Technical decisions and data model
- `docs/01-START/04-plan-roadmap.md` — Implementation roadmap

These are stable project documentation—always load them.

**Fallback if docs/01-START/ doesn't exist:**
If these files don't exist (common when using claude-vibes on an existing project), explore the codebase directly to understand the project's structure, patterns, and conventions. Use AskUserQuestion to gather context about the project's purpose, users, and architecture before proceeding.

## How to Communicate

- **Use AskUserQuestion for EVERY decision** — always provide 2-4 clear options
- Never launch agents until you've confirmed your understanding with the user
- Lead with recommendations: "Based on the existing patterns, I'd suggest..."
- Explain design decisions in plain language
- Flag anything that might be tricky or have alternatives

## Plan Process

### 1. Load Core Context

Read all available docs/01-START/ files for project understanding.

### 2. Retrieve Knowledge from Memory

**Use the memory MCP tools** to retrieve learnings from past sessions that aren't in docs.

1. **Search for relevant knowledge:**
   ```
   Use search_nodes to find:
   - "CodebasePatterns" — patterns discovered in this codebase
   - "ImplementationLessons" — gotchas and learnings from past builds
   ```

2. **Load relevant entities:**
   ```
   Use open_nodes to read observations from matching entities
   ```

3. **Apply this knowledge:**
   - Patterns inform what conventions to follow
   - Lessons warn about gotchas to avoid
   - This supplements the docs with experiential knowledge

**If no memory entities exist yet**, that's fine — they'll be created as you build. Proceed to the next step.

### 3. Check for Taskmaster

**Check if Taskmaster is set up** by looking for `.taskmaster/tasks/tasks.json`.

**If Taskmaster EXISTS:**

Use the Taskmaster MCP `next_task` tool to get the recommended next task based on dependencies.

**Use AskUserQuestion to confirm the task:**

```
Question: "Based on your project's dependencies, Taskmaster recommends this task next:

**Task [ID]: [Task Name]**
[Task description]

Dependencies completed: [list completed deps]

Should we plan this task?"
Options:
- Yes, let's plan this task
- Show me other available tasks first
- I want to work on something else
- Other
```

**If they want other tasks:** Use `get_tasks` to show available tasks with their status and dependencies. Let them pick.

**If they want something else:** Ask what they want to work on, then proceed with manual planning.

**If Taskmaster DOES NOT exist:**

Check if `$ARGUMENTS` was provided.

**If arguments provided:** Use that as the feature to plan.

**If no arguments:** Use AskUserQuestion:
```
Question: "What would you like to build next?"
Options:
- [Suggest based on docs/01-START/ if available]
- [Another suggestion]
- Let me describe what I want to build
- Other
```

### 4. Expand Complex Tasks (Taskmaster only)

**Skip this step if not using Taskmaster.** For manual tasks, proceed to Step 5.

After selecting a Taskmaster task, check if it needs expansion into subtasks.

**Step 3a: Check for existing subtasks**

Use `get_task` to see the task details. If subtasks already exist:

**Use AskUserQuestion:**
```
Question: "This task already has subtasks:

1. [Subtask 1] — [status]
2. [Subtask 2] — [status]
3. [Subtask 3] — [status]

Which subtask should we plan?"
Options:
- Subtask 1: [name]
- Subtask 2: [name]
- [etc.]
- Other
```

Then proceed to Step 4 with the selected subtask.

**Step 3b: Check complexity analysis**

If no subtasks exist, check if complexity analysis has been run for this task.

**If complexity data EXISTS:**

Look at two things:
1. The complexity score (1-10)
2. The **recommended subtask count** from the analysis

**If recommended subtasks = 0 OR complexity score < 4:**
The task is simple enough — skip expansion and proceed to Step 4.

**If recommended subtasks > 0:**

**Use AskUserQuestion:**
```
Question: "This task has been analyzed:

**Task [ID]: [Name]**
- Complexity score: [X]/10
- Taskmaster recommends: [Y] subtasks

Expanding into subtasks helps prevent context issues during implementation. Want to expand?"
Options:
- Yes, expand with research (recommended for unfamiliar areas)
- Yes, expand without research (faster)
- No, I'll handle it as one task
- Why is this task complex? (show analysis details)
```

**If they want details:** Show the complexity analysis reasoning, then ask again.

**If they decline expansion:** Note in the plan that this is a complex task being handled as one unit. Proceed to Step 4.

**If they choose to expand:**

1. Use Taskmaster's `expand_task` tool:
   - Include `--research` flag if they chose that option
   - The tool will create subtasks based on complexity recommendations

2. Show the generated subtasks:

**Use AskUserQuestion:**
```
Question: "Here are the subtasks created:

1. [Subtask 1] — [description]
2. [Subtask 2] — [description]
3. [Subtask 3] — [description]

Does this breakdown look right?"
Options:
- Yes, looks good — let's plan subtask 1
- I'd like to adjust some subtasks first
- Add a subtask for [specific area]
- Other
```

3. Make adjustments if needed using Taskmaster tools

4. **The first subtask becomes what we plan** — proceed to Step 4 with subtask 1

**If NO complexity data exists:**

**Use AskUserQuestion:**
```
Question: "This task hasn't been analyzed for complexity yet.

Complexity analysis identifies which tasks benefit from being broken into subtasks. Want me to analyze it?"
Options:
- Yes, analyze first (recommended)
- No, proceed without analysis
- What does complexity analysis do?
```

**If they want explanation:** "Complexity analysis uses AI to evaluate the task and recommend how many subtasks it should have. Tasks with many dependencies, unfamiliar technologies, or multiple concerns benefit from breakdown. Simple tasks get a recommendation of 0 subtasks."

**If they choose to analyze:** Use Taskmaster's `analyze_task_complexity` tool, then return to the "If complexity data EXISTS" flow above.

**If they skip analysis:** Proceed to Step 5 with the full task.

---

### 5. Understand the Task

Once you have a task or subtask to plan:

**Use AskUserQuestion to clarify until you fully understand:**
- What should this feature DO? (specific behavior, not just name)
- Who is it for? (which user type from docs/01-START/)
- What's the expected outcome when it's working?
- Any specific behaviors or edge cases you're already aware of?
- What's most important about this feature—speed, simplicity, flexibility?

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

### 6. Launch Code Architect (REQUIRED)

**You MUST use the Task tool to launch the code-architect agent.** Use `subagent_type: "claude-vibes:code-architect"` with this prompt:

> Ultrathink about implementing [feature/task].
>
> **Use the sequential-thinking MCP tool** to work through your design process methodically:
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
> - If you're unsure about any requirement, ask—never assume
>
> **Report back with specific references:**
> - Cite specific LOGS.json entry IDs that are relevant (e.g., "entry-042")
> - Quote the relevant portions from those entries
> - List exact file paths and line numbers for code patterns
> - Provide concrete code snippets from existing implementations
>
> This allows the main session to read those specific references without parsing all of LOGS.json.

### 7. Load Specific References

After the code-architect returns:

**Read only the specific references it identified:**
- Read the exact LOGS.json entries it cited (by ID or content)
- Read the specific code files/sections it referenced

This gives you relevant build history without reading the entire LOGS.json.

### 8. Review the Design

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

### 9. Finalize the Plan

Once the user approves, document the plan:

**Summary:**
- What we're building
- Why it matters
- Taskmaster task ID (if applicable)

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
- Flag complexity early—better to discuss than surprise
- The plan should be specific enough that `/02-write-code` can execute it

## Output

When planning is complete:

1. **Determine plan filename:**
   - If Taskmaster task: `docs/02-BUILD/plan-task-[id]-[name].md`
   - If manual: `docs/02-BUILD/plan-[feature-name].md`

2. **Save the plan** with:
   - Taskmaster task ID (if applicable)
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
