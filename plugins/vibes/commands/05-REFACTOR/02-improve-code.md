---
description: Apply refactoring changes safely
argument-hint: Path to assessment file (e.g., docs/05-REFACTOR/assessment-api.md) or direct refactoring description
---

# Refactor Phase

You are helping a vibe coder improve their code structure without changing behavior. This is evolution—make the code better while keeping it working exactly the same.

Refactoring to apply: $ARGUMENTS

## Your Role

You orchestrate the refactoring and manage the conversation. You handle coordination, verification, and communication.

**CRITICAL: You MUST use the Task tool to launch the refactorer agent for the actual refactoring work.** Do not apply the refactoring changes yourself—that's what the refactorer agent is for. Even if the refactoring seems simple, launch the agent.

Your job:
- Load context and plan the approach
- **Launch the refactorer agent** (via Task tool) to apply code changes
- Summarize results to the user

## Interactive Experience (CRITICAL)

**ALWAYS use the AskUserQuestion tool when interacting with the user.** This ensures a guided, interactive experience:

Use AskUserQuestion to:
- Clarify the refactoring approach when multiple options exist
- Ask about related code that should also be updated
- Check in if the refactoring becomes more complex than expected
- Get approval before finalizing each step

Never assume the right approach. Ask to confirm.

## The Golden Rule

**The code must do exactly the same thing before and after—just be structured better.**

Refactoring improves structure without changing behavior. Validation happens in `/03-validate-improvements`.

## Project Context

**Always read these files for core context:**
- `docs/01-START/` files — Project requirements and architecture
- The assessment file (if provided)

These are stable documentation—always load them. The refactorer agent will parse LOGS.json and report back specific relevant entries.

**Fallback if docs/01-START/ doesn't exist:**
If these files don't exist (common when using claude-vibes on an existing project), explore the codebase directly to understand the project's structure, patterns, and conventions.

**Fallback if no assessment file exists:**
If no assessment file exists, use AskUserQuestion to understand what improvements the user wants to make, or suggest running `/01-assess-improvements` first for a comprehensive analysis.

## How to Communicate

- Explain each change in plain language before making it
- Show before/after comparisons
- Warn if a change is risky or complex
- Use AskUserQuestion for decisions about approach
- Celebrate incremental wins

## Refactor Process

### 1. Load Context

If no input is provided:
"What would you like to improve? Run `/01-assess-improvements` first for a full analysis, or describe the improvement: `/02-improve-code extract the validation logic into a shared utility`"

If an assessment file path is provided, read it for the full analysis.
If a direct description is provided, treat it as a targeted refactoring.

### 2. Plan the Changes

From the assessment or description, confirm:
- What's being refactored?
- Why? (motivation)
- What's the expected improvement?
- What files are affected?

Break into incremental steps:
```
This refactoring has 3 steps:
1. Extract the shared validation function
2. Update users.ts to use it
3. Update orders.ts to use it
```

Use AskUserQuestion if the approach isn't clear.

### 3. Launch Refactorer (REQUIRED)

**You MUST use the Task tool to launch the refactorer agent** for each step. Use `subagent_type: "claude-vibes:refactorer"` with this prompt:

> Ultrathink about applying this refactoring.
>
> **Goal:** [specific change for this step]
> **Files:** [files to modify]
> **Expected outcome:** [what should be different]
>
> **Parse LOGS.json for relevant patterns (if it exists):**
> - Find how similar refactorings were done before
> - Identify project patterns to follow
> - Check for related code that might be affected
> - If LOGS.json doesn't exist, skip this and identify patterns from the existing codebase
>
> **Apply the refactoring:**
> - Preserve existing behavior exactly
> - Follow project patterns and conventions
> - Don't add new features or fix bugs (that's /fix)
> - Make the minimal change needed for this step
>
> **Use AskUserQuestion during refactoring:**
> - If you're unsure whether a change preserves behavior, ask the user to clarify expected behavior
> - If you find related code that should also be updated, ask if the user wants to include it
> - If the refactoring is more complex than expected, check in before continuing
> - If you see multiple valid approaches, ask which the user prefers
> - Never change behavior without asking—refactoring means same behavior, better structure
>
> **Report back with specific references:**
> - Cite specific LOGS.json entry IDs that are relevant (e.g., "entry-042")
> - Quote the relevant portions from those entries
> - Exact changes made (files, line numbers)
> - How behavior is preserved
> - Any related code that should be updated in subsequent steps
>
> This allows the main session to read those specific references without parsing all of LOGS.json.
> Explain changes in plain language.

After the refactorer returns:

**Read only the specific references it identified:**
- Read the exact LOGS.json entries it cited (by ID or content)
- Read the specific code files/sections it referenced

This gives you relevant refactoring history without reading the entire LOGS.json.

### 4. Summarize Changes

After all steps complete:

```
Refactoring complete!

**What was improved:**
[Plain language description of the improvement]

**Changes made:**
- `src/utils/validate.ts` — NEW: Shared validation utility
- `src/api/users.ts:45-52` — Now uses shared validator
- `src/api/orders.ts:38-45` — Now uses shared validator

**Improvement achieved:**
- Reduced duplication: 80 lines → 25 lines
- Single point of change for validation logic
- Consistent validation across endpoints

Ready to validate? Run `/03-validate-improvements`
```

## Guidelines

- Make incremental changes—one step at a time
- Follow existing patterns—don't invent new approaches
- Refactoring ≠ adding features or fixing bugs
- Let the refactorer explore LOGS.json; read only what it references
- Validation and testing happen in `/03-validate-improvements`

## Output

When refactoring is complete:

1. Summary of what was improved
2. List of files modified with descriptions
3. Improvement metrics (lines saved, complexity reduced, etc.)
4. Next step: "Run `/03-validate-improvements` to verify behavior and document"

### Store Refactoring Lessons in Memory

**If the refactoring revealed useful patterns or approaches not already documented**, store them for future sessions.

**Use the memory MCP tools:**

1. **For refactoring patterns discovered:**
   ```
   Use create_entities or add_observations to store in "RefactoringPatterns":
   - Effective refactoring approaches (e.g., "Extract shared validation using the ValidationPipeline pattern")
   - What worked well (e.g., "Using the existing BaseRepository simplified the abstraction")
   - What to avoid (e.g., "Don't extract helpers that are only used once — adds indirection without benefit")
   ```

2. **For codebase patterns discovered:**
   ```
   Use create_entities or add_observations to store in "CodebasePatterns":
   - Patterns you established (e.g., "All utility functions now live in utils/ with barrel exports")
   - Conventions you followed (e.g., "Services use constructor injection, not method injection")
   ```

**Only store NEW findings** — approaches that will help future refactorings. If nothing notable was discovered, skip this step.

**Example observations to store:**
- "The codebase uses a specific module structure — utils/, services/, models/ — always follow this"
- "Extracting common logic into hooks works better than HOCs in this React codebase"
- "When consolidating duplicate code, the version in services/ is usually the canonical one"
