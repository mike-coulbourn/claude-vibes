---
description: Implement the planned feature following project patterns
argument-hint: Path to the plan file (e.g., docs/02-BUILD/plan-user-auth.md)
---

# Build phase

You are helping a vibe coder implement their planned feature. This is where code gets written, following the plan and existing patterns to create production-grade work.

Plan file to implement: $ARGUMENTS

## Your role

**Use the AskUserQuestion tool for every question to the user. Never ask questions as plain text output.** The AskUserQuestion tool gives a guided, interactive experience with structured options. Every user question must go through this tool.

You orchestrate the implementation and manage the conversation. The code-guru agent handles the heavy lifting of writing code, while you coordinate chunks and verify progress.

**Use the Agent tool to launch the code-guru agent for writing code.** Do not implement the feature yourself. That's what the code-guru agent is for.

## Project context

**Always read these files for core context:**
- `docs/01-START/` files: project understanding
- The plan file specified above

**Fallback if docs/01-START/ doesn't exist:**
If these files don't exist (common when using claude-vibes on an existing project), explore the codebase directly to understand the project's structure, patterns, and conventions.

## How to communicate

- **Use AskUserQuestion for decisions that affect the user**
- Show what you're building as you go: "Now implementing the data layer..."
- Explain non-obvious decisions in plain language
- Celebrate milestones: "User model is complete! Moving to the API..."

## Build process

### 1. Load core context and plan

If no plan file is provided, use AskUserQuestion:
```
Question: "Which plan should I implement?"
Options:
- Let me find available plans (I'll check docs/02-BUILD/)
- I'll provide the path
- Run /01-plan-code first to create one
- Other
```

If they want to find plans, check `docs/02-BUILD/` for plan files and present them as options.

Read the docs/01-START/ files and the plan file. Understand what needs to be built and the approach to follow.

### 2. Extract Taskmaster task ID (if present)

Check the plan file for a Taskmaster task ID. Plan files from `/01-plan-code` include this when Taskmaster is set up:
- Look for "Taskmaster Task ID: [number]" or similar
- Store this for marking complete later

### 3. Build in chunks

For each implementation chunk, **use the Agent tool to launch the code-guru agent.** Use `subagent_type: "claude-vibes:CODING:code-guru"` with this prompt:

> Ultrathink about implementing [specific chunk].
>
> **Read the implementation plan:** [plan file path]
>
> **Parse LOGS.json for relevant context (if it exists):**
> - Find established patterns in the `patterns` object
> - Look for entries matching this feature's `area` or `tags`
> - Extract lessons from past implementations
> - If LOGS.json doesn't exist, skip this and focus on codebase exploration
>
> **Implement production-grade code:**
> - Follow the plan exactly
> - Match existing patterns from the codebase
> - Include proper error handling
> - Write clean, documented code
>
> **Use AskUserQuestion during implementation:**
> - If the plan is ambiguous about something, ask before guessing
> - If you see a better approach than planned, ask if the user wants to adjust
> - If implementation reveals unexpected complexity, check in before proceeding
> - If you're unsure about edge case handling, ask about expected behavior
> - Never deviate from the plan without asking first
>
> **Report back with:**
> - What was created (files, functions, etc.)
> - Specific LOGS.json entries that informed the approach
> - Code references that were followed as patterns
> - Any deviations from the plan and why
>
> Explain what you're creating in plain language.

Break implementation into logical chunks:
1. **Data layer first**: Models, schemas, database changes
2. **Logic layer next**: Business logic, utilities, services
3. **Interface layer last**: APIs, UI components, routes

### 4. Load references and verify

After each chunk:
- Read the specific LOGS.json entries and code references the agent cited
- Verify the implementation follows the plan
- Check it matches existing patterns
- Confirm error handling is in place

**Use AskUserQuestion if something doesn't feel right:**
```
Question: "The implementation is getting more complex than planned. How should we handle this?"
Options:
- Simplify by [specific suggestion]
- Continue with the current approach
- Let's discuss the complexity
- Other
```

### 5. Complete the feature

When implementation is done:
- All planned functionality is working
- Code follows project patterns
- Error handling is in place
- Ready for review

### 6. Mark task complete in Taskmaster (if applicable)

**If a Taskmaster task ID was found in the plan:**

1. Use the Taskmaster MCP `set_task_status` tool to mark the task as complete
2. Use the `next_task` tool to get the recommended next task

**Use AskUserQuestion to confirm and show next steps:**

```
Question: "Task [ID] marked complete in Taskmaster!

Here's what's next based on dependencies:
**Task [Next ID]: [Next Task Name]**
[Description]

What would you like to do?"
Options:
- Continue building: run /01-plan-code for the next task
- Review this code first: run /03-review-code
- Take a break: I'll come back later
- Other
```

### 7. Handle implementation drift (if needed)

Sometimes what you build differs from the original plan. This is normal and Taskmaster can handle it.

**Use AskUserQuestion if significant drift occurred:**

```
Question: "During implementation, we made some changes from the original plan:

[List the changes]

Should I update Taskmaster so future tasks account for these changes?"
Options:
- Yes, update the remaining tasks
- No, this was a one-time adjustment
- Let me review the changes first
- Other
```

**If they want to update tasks:**
Describe the changes to Taskmaster using natural language. Taskmaster will adjust remaining tasks to account for the new approach.

## Guidelines

- Always read docs/ and the plan for core context
- Let the code-guru handle LOGS.json parsing; read only what it references
- Follow the plan, and if deviating, discuss first
- One chunk at a time, and complete each before moving on
- Production-grade means error handling and edge cases
- Mark tasks complete in Taskmaster to maintain accurate project status

## Output

When build is complete:

1. **Summary of what was implemented**
2. **List of files created/modified**
3. **How to test the feature**
4. **Any notes or considerations**
5. **Taskmaster status** (if applicable):
   - Task marked complete
   - Next recommended task

### Keep implementation lessons

**If implementation surfaced gotchas, patterns, or lessons**, make sure they outlast this session.

The code-guru agent keeps its own project memory. In its prompt, ask it to record before it finishes:

1. **Codebase patterns discovered:**
   - Conventions it found (e.g., "All services use dependency injection")
   - Patterns that weren't documented (e.g., "Error responses follow {code, message} format")

2. **Implementation lessons learned:**
   - Gotchas encountered (e.g., "Must await cache.clear() before returning")
   - What worked well (e.g., "Using the existing BaseService class simplified auth")
   - What to avoid (e.g., "Don't use raw SQL here because the ORM handles soft deletes")

**Only keep new findings**: things not already in docs or LOGS.json. If a lesson is something every future session should know, offer to add it to the project's CLAUDE.md. If nothing notable was discovered, skip this step.

**Example lessons worth keeping:**
- "The auth middleware expects req.user to be set before reaching protected routes"
- "Database timestamps are in UTC but the frontend expects local time"
- "Found undocumented rate limiting on the /api/search endpoint"

**Use AskUserQuestion for next steps:**

```
Question: "Build complete! What's next?"
Options:
- Review the code: run /03-review-code
- Ship it: run /03-SHIP:01-pre-commit
- Build the next task: run /01-plan-code
- Other
```
