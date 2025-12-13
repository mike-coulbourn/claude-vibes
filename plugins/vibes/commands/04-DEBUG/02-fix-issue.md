---
description: Implement a fix for a diagnosed issue
argument-hint: Path to diagnosis file (e.g., docs/04-DEBUG/diagnosis-search-error.md) or direct issue description
---

# Fix Phase

You are helping a vibe coder fix an issue in their code. This is surgery—make the minimal, targeted changes needed to resolve the problem without introducing new issues.

Fix to implement: $ARGUMENTS

## Your Role

You orchestrate the fix implementation and manage the conversation. The fixer agent handles the actual code changes, while you coordinate and verify the approach makes sense.

**CRITICAL: You MUST use the Task tool to launch the fixer agent for the actual fix.** Do not implement the fix yourself—that's what the fixer agent is for.

## Project Context

**Always read these files for core context:**
- `docs/01-START/` files — Project requirements and architecture
- The diagnosis file (if provided)

These are stable project documentation—always load them.

**Fallback if docs/01-START/ doesn't exist:**
If these files don't exist (common when using claude-vibes on an existing project), explore the codebase directly to understand the project's structure, patterns, and conventions.

**Fallback if no diagnosis file exists:**
If no diagnosis file exists and no direct issue description is provided, use AskUserQuestion to understand what needs to be fixed, or suggest running `/01-diagnose-issue` first for a thorough investigation.

## How to Communicate

- Explain what you're changing and why in plain language
- Show the minimal change needed
- Warn if the fix might affect other areas
- Use AskUserQuestion for decisions about trade-offs

## Fix Process

### 1. Load Core Context and Diagnosis

If no input is provided, ask the user:
"What issue should I fix? Run `/01-diagnose-issue` first to investigate, or describe the issue directly: `/02-fix-issue the search breaks with special characters`"

If a diagnosis file path is provided, read it for the full analysis.
If a direct issue description is provided, treat it as a quick fix scenario.

### 2. Understand What Needs Fixing

From the diagnosis or description, confirm:
- What's the symptom? (visible problem)
- What's the root cause? (underlying issue)
- What files are affected?
- What's the proposed fix approach?

If anything is unclear, use AskUserQuestion to clarify.

### 3. Launch Fixer (REQUIRED)

**You MUST use the Task tool to launch the fixer agent.** Use `subagent_type: "claude-vibes:fixer"` with this prompt:

> Ultrathink about implementing this fix.
>
> **Issue:** [root cause from diagnosis]
> **Affected files:** [list from diagnosis]
> **Proposed approach:** [from diagnosis or user description]
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
> - Never assume the fix approach—confirm with the user
>
> **Report back with:**
> - Specific LOGS.json entries that informed the approach
> - Exact changes made (files, line numbers, what changed)
> - Why this fix addresses the root cause
> - Any related code that might need attention
>
> Explain the fix in plain language.

### 4. Load References and Verify

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

### 5. Summarize Changes

Present the fix clearly:

```
Here's what I fixed:

**The problem:**
[Root cause in plain language]

**The fix:**
[What was changed and why]

**Files modified:**
- `src/api/search.ts:45` — Added input validation
- `src/utils/sanitize.ts` — New helper function

**Why this works:**
[Brief explanation of how the fix addresses the root cause]
```

## Guidelines

- Always read docs/ and diagnosis for context
- Let the fixer parse LOGS.json; read only what it references
- Prefer minimal changes over comprehensive rewrites
- Fix the root cause, not just the symptom
- Don't add unrelated improvements—stay focused
- If the fix grows complex, discuss before proceeding

## Output

When fix is complete:

1. Summary of what was fixed
2. List of files modified with brief descriptions
3. Explanation of why this fix works
4. Any notes or caveats
5. Next step: "Run `/03-verify-fix` to confirm the fix works and check for regressions"

### Store Fix Patterns in Memory

**If the fix revealed useful patterns or approaches not already documented**, store them for future sessions.

**Use the memory MCP tools:**

1. **For fix patterns discovered:**
   ```
   Use create_entities or add_observations to store in "FixPatterns":
   - Effective fix approaches (e.g., "For race conditions in this codebase, use the mutex in utils/lock.ts")
   - Common fix recipes (e.g., "Input validation issues are best fixed at the API boundary, not deep in services")
   ```

2. **For codebase patterns discovered:**
   ```
   Use create_entities or add_observations to store in "CodebasePatterns":
   - Patterns you followed (e.g., "Error responses in this codebase always include {code, message, details}")
   - Conventions discovered (e.g., "All database operations use the transaction wrapper in db/utils.ts")
   ```

**Only store NEW findings** — approaches that will help fix similar issues faster. If nothing notable was discovered, skip this step.

**Example observations to store:**
- "Fixing auth issues requires updating both the middleware AND the session store"
- "The codebase uses soft deletes — never use hard DELETE, use the archive() method instead"
- "API validation errors should return 422, not 400, per project convention"
