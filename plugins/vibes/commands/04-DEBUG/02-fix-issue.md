---
description: Implement a fix for a diagnosed issue
argument-hint: Path to diagnosis file (e.g., docs/04-DEBUG/diagnosis-search-error.md) or direct issue description
---

# Fix phase

You are helping a vibe coder fix an issue in their code. This is surgery. Make the minimal, targeted changes needed to resolve the problem without introducing new issues.

Fix to implement: $ARGUMENTS

## Your role

**Use the AskUserQuestion tool for every question to the user. Never ask questions as plain text output.** The AskUserQuestion tool gives a guided, interactive experience with structured options. Every user question must go through this tool.

You orchestrate the fix implementation and manage the conversation. The fixer agent handles the actual code changes, while you coordinate and verify the approach makes sense.

**Use the Agent tool to launch the fixer agent for the actual fix.** Do not implement the fix yourself. That's what the fixer agent is for.

## Interactive experience (critical)

**Use the AskUserQuestion tool whenever you interact with the user.** This gives a guided, interactive experience:

Use AskUserQuestion to:
- Clarify the fix approach when multiple options exist
- Present trade-offs and ask which approach the user prefers
- Validate the fix scope before making changes
- Get approval before finalizing changes

Never assume the right approach. Ask to confirm.

## Project context

**Always read these files for core context:**
- `docs/01-START/` files: project requirements and architecture
- The diagnosis file (if provided)

These are stable project documentation, so always load them.

**Fallback if docs/01-START/ doesn't exist:**
If these files don't exist (common when using claude-vibes on an existing project), explore the codebase directly to understand the project's structure, patterns, and conventions.

**Fallback if no diagnosis file exists:**
If no diagnosis file exists and no direct issue description is provided, use AskUserQuestion to understand what needs to be fixed, or suggest running `/01-diagnose-issue` first for a thorough investigation.

## How to communicate

- Explain what you're changing and why in plain language
- Show the minimal change needed
- Warn if the fix might affect other areas
- Use AskUserQuestion for decisions about trade-offs

## Fix process

### 1. Load core context and diagnosis

If no input is provided, ask the user:
"What issue should I fix? Run `/01-diagnose-issue` first to investigate, or describe the issue directly: `/02-fix-issue the search breaks with special characters`"

If a diagnosis file path is provided, read it for the full analysis.
If a direct issue description is provided, treat it as a quick fix scenario.

### 2. Understand what needs fixing

From the diagnosis or description, confirm:
- What's the symptom? (visible problem)
- What's the root cause? (underlying issue)
- What files are affected?
- What's the proposed fix approach?

If anything is unclear, use AskUserQuestion to clarify.

### 3. Launch fixer (required)

**Use the Agent tool to launch the fixer agent.** Use `subagent_type: "claude-vibes:CODING:fixer"` with this prompt:

> Ultrathink about implementing this fix.
>
> **Issue:** [root cause from diagnosis]
> **Affected files:** [list from diagnosis]
> **Proposed approach:** [from diagnosis or user description]
>
> Check your project memory for related past fixes and codebase patterns before starting, and record what you learn before finishing.
>
> **Parse LOGS.json for relevant patterns (if it exists):**
> - Find how similar issues were fixed before
> - Identify project patterns to follow
> - Check for related code that might be affected
> - If LOGS.json doesn't exist, skip this and identify patterns from the existing codebase
>
> **Implement a minimal, targeted fix:**
> - Change only what's necessary
> - Follow existing project patterns
> - Don't over-engineer or add unrelated improvements
> - Handle edge cases that caused this bug
> - Add defensive checks where appropriate
>
> **Use AskUserQuestion during the fix:**
> - If there are multiple ways to fix the issue, ask which approach the user prefers
> - If the fix might affect other functionality, ask if that's acceptable
> - If you're unsure about the intended behavior after the fix, ask
> - If the fix is growing larger than expected, check in before continuing
> - Never assume the fix approach. Confirm with the user
>
> **Report back with:**
> - Specific LOGS.json entries that informed the approach
> - Exact changes made (files, line numbers, what changed)
> - Why this fix addresses the root cause
> - Any related code that might need attention
>
> Explain the fix in plain language.

### 4. Load references and verify

After the fixer returns:

**Read the specific references it identified:**
- Read LOGS.json entries it cited
- Review the changes made

**Verify the fix makes sense:**
- Does it address the root cause (not just the symptom)?
- Is it minimal and targeted?
- Does it follow project patterns?
- Could it introduce new issues?

If something seems off, discuss:
- "This fix is larger than expected. Here's why..."
- "I noticed a potential issue with this approach..."

### 5. Summarize changes

Present the fix clearly:

```
Here's what I fixed:

**The problem:**
[Root cause in plain language]

**The fix:**
[What was changed and why]

**Files modified:**
- `src/api/search.ts:45`: Added input validation
- `src/utils/sanitize.ts`: New helper function

**Why this works:**
[Brief explanation of how the fix addresses the root cause]
```

## Guidelines

- Always read docs/ and diagnosis for context
- Let the fixer parse LOGS.json; read only what it references
- Prefer minimal changes over sweeping rewrites
- Fix the root cause, not just the symptom
- Don't add unrelated improvements. Stay focused
- If the fix grows complex, discuss before proceeding

## Output

When fix is complete:

1. Summary of what was fixed
2. List of files modified with brief descriptions
3. Explanation of why this fix works
4. Any notes or caveats
5. Next step: "Run `/03-verify-fix` to confirm the fix works and check for regressions"

### Record fix patterns

In the fixer's prompt, ask it to record durable learnings in its project memory before it finishes:

1. **Fix patterns discovered:**
   - Effective fix approaches (e.g., "For race conditions in this codebase, use the mutex in utils/lock.ts")
   - Common fix recipes (e.g., "Input validation issues are best fixed at the API boundary, not deep in services")

2. **Codebase patterns discovered:**
   - Patterns you followed (e.g., "Error responses in this codebase always include {code, message, details}")
   - Conventions discovered (e.g., "All database operations use the transaction wrapper in db/utils.ts")

**Only record new findings**: approaches that will help fix similar issues faster. If nothing notable was discovered, skip this step.

If the user's review surfaced a lesson that every future session should know, offer to add it to the project's CLAUDE.md.

**Example observations to store:**
- "Fixing auth issues requires updating both the middleware and the session store"
- "The codebase uses soft deletes, so never use hard DELETE, use the archive() method instead"
- "API validation errors should return 422, not 400, per project convention"
