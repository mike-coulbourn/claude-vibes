---
description: Verify refactoring preserved behavior and document it
argument-hint: Optional specific files or areas to validate
---

# Validate Phase

You are helping a vibe coder confirm their refactoring preserved behavior and didn't break anything. This is the quality gate—refactorings that pass validation get documented in LOGS.json.

Specific area to validate: $ARGUMENTS

## Your Role

You orchestrate the validation and manage the conversation. The validator agent handles thorough testing, while you present findings and manage the documentation.

## Project Context

**Always read these files for core context:**
- `docs/start/` files — Project requirements and architecture
- `docs/refactor/assessment-*.md` — The assessment for this refactoring

These are stable documentation—always load them. The validator agent will parse LOGS.json and report back specific relevant entries.

## How to Communicate

- Be clear about what passed and what failed
- Explain any behavior changes found (even subtle ones)
- Celebrate when everything works
- Use AskUserQuestion for judgment calls

## Validate Process

### 1. Load Context

Read docs/start/ files and the most recent assessment file to understand what was refactored and why.

### 2. Identify What to Validate

If `$ARGUMENTS` specifies files/areas, focus there.

Otherwise, find the recent refactoring:
- Check `git diff` for uncommitted changes
- Read the most recent `docs/refactor/assessment-*.md`
- Look at recently modified files

### 3. Launch Validator

**Launch the validator agent** with this prompt:

> Ultrathink about validating this refactoring.
>
> **What was refactored:** [from assessment or git diff]
> **Expected behavior:** Same as before—no functional changes
>
> **Parse LOGS.json for context:**
> - Find related past refactorings
> - Identify patterns that should be verified
> - Check for areas that commonly have subtle behavior changes
>
> **Validate thoroughly:**
> - Run all related tests (do they still pass?)
> - Check for behavior preservation (does it do the same thing?)
> - Look for subtle changes (error messages, timing, edge cases)
> - Verify the improvement was achieved (is it actually better?)
>
> **Report back with specific references:**
> - Cite specific LOGS.json entry IDs that are relevant (e.g., "entry-042")
> - Quote the relevant portions from those entries
> - Test results (passed/failed counts)
> - Behavior verification (same/different)
> - Any subtle changes detected
> - Improvement confirmation (was the goal achieved?)
> - LOGS.json entry recommendation with:
>   - motivation, approach, improvement, guideline
>   - files modified, tags, area
>
> This allows the main session to read those specific references without parsing all of LOGS.json.
> Be specific about validation results.

### 4. Load Specific References

After the validator returns:

**Read only the specific references it identified:**
- Read the exact LOGS.json entries it cited (by ID or content)
- Read the specific code files/sections it referenced

This gives you relevant validation history without reading the entire LOGS.json.

### 5. Present Findings

**If all validations pass:**
```
Validation complete! The refactoring is solid.

What I verified:
- Tests: [X] passed, 0 failed (same as baseline)
- Behavior: Preserved—no functional changes detected
- Improvement: Achieved—[specific improvement metrics]

The refactoring is ready to ship.
```

**If issues found:**
```
Validation found problems:

1. BEHAVIOR CHANGE: Error message format changed
   File: src/api/users.ts:52
   Before: "Invalid email"
   After: "Email validation failed"
   This might affect frontend error handling.

2. TEST FAILURE: test_edge_case now fails
   File: tests/api.test.ts:142
   The refactoring changed how empty inputs are handled.

These need to be addressed before shipping.
```

Use AskUserQuestion for judgment calls:
- "The error message changed slightly but tests pass. Is this intentional?"
- "Found a subtle timing difference. Want me to investigate further?"

### 6. Iterate if Needed

If issues exist:
1. Explain what's wrong clearly
2. Offer to go back and adjust the refactoring
3. Re-run validation after fixes

"I found 1 behavior change. Should I adjust the refactoring to preserve the original behavior?"

### 7. Document in LOGS.json

**Only when validation passes** (no behavior changes, tests pass, improvement achieved):

Write to LOGS.json with this entry structure:
```json
{
  "id": "entry-<timestamp>",
  "timestamp": "<ISO timestamp>",
  "phase": "refactor",
  "type": "refactor",
  "area": "<domain area>",

  "motivation": "<why refactoring was needed>",
  "approach": "<how it was refactored>",
  "summary": "<one-line description>",
  "details": "<fuller description of the improvement>",
  "improvement": "<what got better - metrics if possible>",
  "guideline": "<lesson for future development>",

  "patterns": ["<patterns applied>"],
  "files": ["<files modified>"],
  "tags": ["refactor", "<type>", "<area-tags>"],
  "validatedAt": "<ISO timestamp>",
  "validateNotes": "<any notes from validation>"
}
```

Add to the global LOGS.json at project root.

## Guidelines

- Always read docs/ and assessment for context
- Let the validator explore LOGS.json; read only what it references
- Behavior must be exactly preserved (refactoring ≠ changing)
- Tests must all pass before shipping
- Improvements should be measurable when possible
- Only write to LOGS.json after passing validation

## LOGS.json Write Rules

**Only write to LOGS.json when:**
1. All tests pass (same as baseline)
2. No behavior changes detected
3. Improvement was achieved
4. Refactoring is ready to ship

**Include in the entry:**
- Motivation (why we refactored)
- Approach (how we did it)
- Improvement (what got better)
- Guideline (lesson for future)
- Files touched and searchable tags

## Output

When validation is complete:

**If passed:**
1. Summary of what was validated
2. Confirmation behavior is preserved
3. Improvement metrics achieved
4. Confirmation that LOGS.json was updated
5. Next steps:
   - `/03-ship/01-check` — Run pre-commit checks
   - `/03-ship/02-commit` — Just commit locally
   - `/03-ship/03-push` — Commit and push
   - `/03-ship/04-pr` — Commit, push, and create PR

**If failed:**
1. Clear list of issues found
2. Whether they're behavior changes or test failures
3. How to fix each one
4. Offer to adjust the refactoring
5. "Re-run `/03-validate` after fixes"
