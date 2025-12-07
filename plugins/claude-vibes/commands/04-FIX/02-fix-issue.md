---
description: Implement a fix for a diagnosed issue
argument-hint: Path to diagnosis file (e.g., docs/fix/diagnosis-search-error.md) or direct issue description
---

# Fix Phase

You are helping a vibe coder fix an issue in their code. This is surgery—make the minimal, targeted changes needed to resolve the problem without introducing new issues.

Fix to implement: $ARGUMENTS

## Your Role

You orchestrate the fix implementation and manage the conversation. The fixer agent handles the actual code changes, while you coordinate and verify the approach makes sense.

## Project Context

**Always read these files for core context:**
- `docs/start/` files — Project requirements and architecture
- The diagnosis file (if provided)

These are stable project documentation—always load them.

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

### 3. Launch Fixer

**Launch the fixer agent** with this prompt:

> Ultrathink about implementing this fix.
>
> **Issue:** [root cause from diagnosis]
> **Affected files:** [list from diagnosis]
> **Proposed approach:** [from diagnosis or user description]
>
> **Parse LOGS.json for relevant patterns:**
> - Find how similar issues were fixed before
> - Identify project patterns to follow
> - Check for related code that might be affected
>
> **Implement a minimal, targeted fix:**
> - Change only what's necessary
> - Follow existing project patterns
> - Don't over-engineer or add unrelated improvements
> - Handle edge cases that caused this bug
> - Add defensive checks where appropriate
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
