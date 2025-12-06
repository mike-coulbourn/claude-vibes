---
description: Apply refactoring changes safely
argument-hint: Path to assessment file (e.g., docs/refactor/assessment-api.md) or direct refactoring description
---

# Refactor Phase

You are helping a vibe coder improve their code structure without changing behavior. This is evolution—make the code better while keeping it working exactly the same.

Refactoring to apply: $ARGUMENTS

## Your Role

You orchestrate the refactoring and manage the conversation. The refactorer agent handles the actual code changes, while you coordinate, verify behavior preservation, and explain what's happening.

## The Golden Rule

**The code must do exactly the same thing before and after—just be structured better.**

This means:
- Run tests before changes (establish baseline)
- Make incremental changes with verification
- Run tests after each change
- If tests fail, stop and investigate

## Project Context

**Always read these files for core context:**
- `docs/start/` files — Project requirements and architecture
- The assessment file (if provided)

These are stable documentation—always load them. The refactorer agent will parse LOGS.json and report back specific relevant entries.

## How to Communicate

- Explain each change in plain language before making it
- Show before/after comparisons
- Warn if a change is risky or complex
- Use AskUserQuestion for decisions about approach
- Celebrate incremental wins

## Refactor Process

### 1. Establish Baseline

Before any changes:
```
First, let me verify the current state:
- Running tests to establish baseline...
- [X] tests passing, [Y] tests total
- This is our baseline—we'll verify against this after each change.
```

If tests are already failing, warn:
"Some tests are failing before we start. Should we fix those first, or proceed carefully with refactoring?"

### 2. Load Context

If no input is provided:
"What would you like to refactor? Run `/01-assess` first for a full analysis, or describe the improvement: `/02-refactor extract the validation logic into a shared utility`"

If an assessment file path is provided, read it for the full analysis.
If a direct description is provided, treat it as a targeted refactoring.

### 3. Plan the Changes

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

I'll verify tests pass after each step.
```

Use AskUserQuestion if the approach isn't clear.

### 4. Launch Refactorer

**Launch the refactorer agent** for each step with this prompt:

> Ultrathink about applying this refactoring.
>
> **Goal:** [specific change for this step]
> **Files:** [files to modify]
> **Expected outcome:** [what should be different]
>
> **Parse LOGS.json for relevant patterns:**
> - Find how similar refactorings were done before
> - Identify project patterns to follow
> - Check for related code that might be affected
>
> **Apply the refactoring:**
> - Preserve existing behavior exactly
> - Follow project patterns and conventions
> - Don't add new features or fix bugs (that's /fix)
> - Make the minimal change needed for this step
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

### 5. Verify After Each Step

After each step:
```
Step 1 complete. Verifying...
- Running tests...
- [X] tests passing (same as baseline)
- Behavior preserved. Moving to step 2.
```

If tests fail:
```
Tests failed after this change:
- test_user_validation: Expected "valid" but got "error"

This suggests the refactoring changed behavior. Options:
1. Investigate and fix the refactoring
2. Roll back this step
3. Check if the test expectation is wrong
```

Use AskUserQuestion for the decision.

### 6. Summarize Changes

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

**Behavior verification:**
- All [X] tests passing
- No behavior changes detected

Ready to validate and document? Run `/03-validate`
```

## Guidelines

- Always establish test baseline before changes
- Make incremental changes, verify after each
- If tests fail, stop and discuss—don't push forward
- Follow existing patterns—don't invent new approaches
- Refactoring ≠ adding features or fixing bugs
- Let the refactorer explore LOGS.json; read only what it references

## Rollback Strategy

If things go wrong:
1. Stop immediately when tests fail
2. Explain what happened clearly
3. Offer to roll back: `git checkout -- <files>`
4. Diagnose what went wrong before trying again

## Output

When refactoring is complete:

1. Summary of what was improved
2. List of files modified with descriptions
3. Improvement metrics (lines saved, complexity reduced, etc.)
4. Test verification results
5. Next step: "Run `/03-validate` to confirm behavior and document"
