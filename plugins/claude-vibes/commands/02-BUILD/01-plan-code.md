---
description: Explore the codebase and plan a clean, production-grade implementation
argument-hint: Feature or task to plan
---

# Plan Phase

You are helping a vibe coder plan their next piece of work. This combines exploration (understanding what exists) and planning (designing how to add to it). Good planning prevents messy code.

Feature to plan: $ARGUMENTS

## Your Role

You orchestrate the planning process and manage the conversation. The code-architect agent handles codebase exploration and LOGS.json parsing, reporting back specific references that you then read.

## Project Context

**Always read the docs/ files for core context:**
- `docs/start/01-discover.md` — The problem, users, and value
- `docs/start/02-scope.md` — MVP scope boundaries
- `docs/start/03-architect.md` — Technical decisions and data model
- `docs/start/04-plan-roadmap.md` — Implementation roadmap

These are stable project documentation—always load them.

## How to Communicate

- **Use AskUserQuestion FIRST** to clarify requirements—don't assume you understand
- Never launch agents until you've confirmed your understanding with the user
- Lead with recommendations: "Based on the existing patterns, I'd suggest..."
- Explain design decisions in plain language
- Flag anything that might be tricky or have alternatives

## Plan Process

### 1. Load Core Context

Read all available docs/start/ files for project understanding.

### 2. Understand the Task

If `$ARGUMENTS` is provided, start there. If not, use AskUserQuestion:
- "What would you like to build next?"

**Use AskUserQuestion to clarify until you fully understand:**
- What should this feature DO? (specific behavior, not just name)
- Who is it for? (which user type from docs/start/)
- What's the expected outcome when it's working?
- Any specific behaviors or edge cases you're already aware of?
- What's most important about this feature—speed, simplicity, flexibility?

**Before proceeding, summarize back:**
"Here's what I understand: [summary]. Is that right, or should I adjust anything?"

Only proceed to code exploration after the user confirms your understanding.

### 3. Launch Code Architect

**Launch the code-architect agent** with this prompt:

> Ultrathink about implementing [feature/task].
>
> **Parse LOGS.json for relevant history:**
> - Find entries with matching `area` or `tags`
> - Identify established patterns in the `patterns` object
> - Extract relevant past decisions
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

### 4. Load Specific References

After the code-architect returns:

**Read only the specific references it identified:**
- Read the exact LOGS.json entries it cited (by ID or content)
- Read the specific code files/sections it referenced

This gives you relevant build history without reading the entire LOGS.json.

### 5. Review the Design

Now fully context-aware, present the design to the user:

"Here's how I'd build this:"
- What files to create/modify
- What patterns to follow (with specific examples)
- Key implementation decisions
- Potential risks or complexity

Use AskUserQuestion:
- "Does this approach make sense? Any concerns?"
- "Should I adjust anything before we build?"

### 6. Finalize the Plan

Once the user approves, document the plan:

**Summary:**
- What we're building
- Why it matters

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

1. Save the plan to `docs/build/plan-<feature-name>.md`
2. Summarize what will be built
3. Tell the user they're ready for `/02-write-code` to implement

"Plan complete! Run `/02-write-code` to start implementing."
