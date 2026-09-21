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

### 2. Find the roadmap task (if present)

Check the plan file for a roadmap task ID. Plan files from `/01-plan-code` include one when the project has a roadmap at `docs/01-START/roadmap.md`:
- Look for "Roadmap task ID: [id]" or similar
- Read that task's done-when line in the roadmap, because that is the finish line for this build
- Keep the ID so you can tick the task off later

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

### 6. Tick the task off the roadmap (if applicable)

**If the plan had a roadmap task ID**, check the task's done-when line against what was built.

**If the done-when line is true:**

1. Run `date +%Y-%m-%d`, then in `docs/01-START/roadmap.md` change the task's `- [ ]` to `- [x]`, add `| done: <date>` at the end of its line, and update "Last updated". Edit the file in place. Tick a parent task only when all its subtasks are ticked.
2. Find the next unchecked task whose dependencies are all ticked.
3. Use AskUserQuestion to show next steps:

```
Question: "Task [ID] is ticked off the roadmap.

Next up:
**Task [Next ID]: [Next task name]** ([type])
[Done-when line]

What would you like to do?"
Options:
- Continue building: run /01-plan-code for the next task
- Review this code first: run /03-review-code
- See the whole roadmap: run /05-track-progress
- Take a break: I'll come back later
- Other
```

If the next task is not a `build` task, say so and point to `/05-track-progress`, which handles checks, brand, content, setup, legal, launch, and by-hand tasks. If the roadmap has a `check` task that depends on this one, recommend running it next, because a task someone else has not checked is not yet proven.

**If the done-when line is only partly true:** leave the box unticked, tell the user exactly what is still missing, and use AskUserQuestion to offer finishing it now or splitting the remainder into a new subtask in the roadmap (with a dated change-log line).

### 7. Handle implementation drift (if needed)

Sometimes what you build differs from the plan. That is normal, as long as the roadmap is updated to match so later tasks do not rest on a plan that is no longer true.

**Use AskUserQuestion if significant drift occurred:**

```
Question: "During implementation, we made some changes from the original plan:

[List the changes]

Should I update the roadmap so the remaining tasks account for them?"
Options:
- Yes, update the remaining tasks
- No, this was a one-time adjustment
- Let me review the changes first
- Other
```

**If they want to update tasks:** edit the affected tasks in `docs/01-START/roadmap.md` in place, show the user the before and after, update "Last updated", and add a dated line to the roadmap's change log saying what changed and why. If the change touches the alignment contract's objective or definition of done, say so and recommend re-running `/04-plan-roadmap` so the graph is approved again.

## Guidelines

- Always read docs/ and the plan for core context
- Let the code-guru handle LOGS.json parsing; read only what it references
- Follow the plan, and if deviating, discuss first
- One chunk at a time, and complete each before moving on
- Production-grade means error handling and edge cases
- Tick finished tasks off the roadmap so it always shows the true state of the project

## Output

When build is complete:

1. **Summary of what was implemented**
2. **List of files created/modified**
3. **How to test the feature**
4. **Any notes or considerations**
5. **Roadmap status** (if applicable):
   - Task ticked off
   - Next task that is ready

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
- Ship it: run /01-pre-commit
- Build the next task: run /01-plan-code
- Other
```
