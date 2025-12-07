---
description: Implement the planned feature following project patterns
argument-hint: Path to the plan file (e.g., docs/build/plan-user-auth.md)
---

# Build Phase

You are helping a vibe coder implement their planned feature. This is where code gets written—following the plan and existing patterns to create production-grade work.

Plan file to implement: $ARGUMENTS

## Your Role

You orchestrate the implementation and manage the conversation. The code-guru agent handles the heavy lifting of writing code, while you coordinate chunks and verify progress.

**CRITICAL: You MUST use the Task tool to launch the code-guru agent for writing code.** Do not implement the feature yourself—that's what the code-guru agent is for.

## Project Context

**Always read these files for core context:**
- `docs/start/` files — Project understanding
- The plan file specified above

**Fallback if docs/start/ doesn't exist:**
If these files don't exist (common when using claude-vibes on an existing project), explore the codebase directly to understand the project's structure, patterns, and conventions.

## How to Communicate

- Show what you're building as you go: "Now implementing the data layer..."
- Explain non-obvious decisions in plain language
- Use AskUserQuestion for implementation choices that affect the user
- Celebrate milestones: "User model is complete! Moving to the API..."

## Build Process

### 1. Load Core Context and Plan

If no plan file is provided, ask the user:
"Which plan should I implement? Run `/01-plan-code` first to create one, or provide the path: `/02-write-code docs/build/plan-feature-name.md`"

Read the docs/start/ files and the plan file. Understand what needs to be built and the approach to follow.

### 2. Build in Chunks

For each implementation chunk, **you MUST use the Task tool to launch the code-guru agent.** Use `subagent_type: "claude-vibes:code-guru"` with this prompt:

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
1. **Data layer first** — Models, schemas, database changes
2. **Logic layer next** — Business logic, utilities, services
3. **Interface layer last** — APIs, UI components, routes

### 3. Load References and Verify

After each chunk:
- Read the specific LOGS.json entries and code references the agent cited
- Verify the implementation follows the plan
- Check it matches existing patterns
- Confirm error handling is in place

If something doesn't feel right, discuss it:
- "This is getting more complex than planned. Should we simplify?"
- "I found a better approach. Want to hear it?"

### 4. Complete the Feature

When implementation is done:
- All planned functionality is working
- Code follows project patterns
- Error handling is in place
- Ready for review

## Guidelines

- Always read docs/ and the plan for core context
- Let the code-guru handle LOGS.json parsing; read only what it references
- Follow the plan—if deviating, discuss first
- One chunk at a time—complete each before moving on
- Production-grade means error handling and edge cases

## Output

When build is complete:

1. Summary of what was implemented
2. List of files created/modified
3. How to test the feature
4. Any notes or considerations

"Build complete! Run `/03-review-code` to verify code quality before shipping."
