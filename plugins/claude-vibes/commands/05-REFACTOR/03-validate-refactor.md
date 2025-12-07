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

### 3. Launch Agents in Parallel

**Launch BOTH agents simultaneously** — they validate the refactoring from different angles and don't depend on each other.

**Validator Agent** (confirm behavior preserved):

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

**Tester Agent** (write tests that prove behavior is preserved):

> Ultrathink about testing this refactored code.
>
> **What was refactored:** [from assessment or git diff]
> **Expected behavior:** Exactly the same as before—refactoring changes structure, not behavior
>
> **Your mission:**
> - Write tests that verify the refactored code behaves identically to before
> - Focus on behavior, not implementation details
> - Run the tests yourself—don't ask the user to run them
> - If tests fail, analyze whether it's a behavior change or just a test issue
> - Iterate until all tests pass
> - Only fall back to manual testing instructions if automation is impossible
>
> **Test coverage should include:**
> - All public interfaces (same inputs = same outputs)
> - Edge cases that might behave differently after refactoring
> - Error handling (same errors thrown in same situations)
> - Side effects (same external effects: DB writes, API calls, etc.)
>
> **Report back with:**
> - Tests written that prove behavior is preserved
> - Test results (all passing or issues found)
> - Any behavior changes detected (these are bugs in refactoring!)
> - Manual testing instructions (only if something couldn't be automated)
> - Confidence level that behavior is truly preserved
>
> The vibe coder should just see results—you do the work.

### 4. Combine Results

After BOTH agents return:

**From Validator:**
- Load specific LOGS.json entries it cited
- Note whether behavior is preserved
- Note whether improvement was achieved

**From Tester:**
- Note tests written and what they prove
- Note test results (passing/failing)
- Note any behavior changes detected
- Note confidence level

### 5. Present Combined Findings

**If all validations pass:**
```
Validation & Testing Complete — Refactoring Verified!

VALIDATION:
- Tests: All passing (same as baseline)
- Behavior: Preserved—no functional changes detected
- Improvement: Achieved—reduced from 120 lines to 45 lines

TESTING:
- Tests written: 10 (behavior preservation tests)
- Tests passing: 10/10
- Behavior changes: None detected
- Confidence: HIGH

The refactoring is solid and ready to ship.
```

**If issues found:**
```
Validation & Testing Found Problems

VALIDATION:
1. BEHAVIOR CHANGE: Error message format changed
   File: src/api/users.ts:52
   Before: "Invalid email"
   After: "Email validation failed"
   This might affect frontend error handling.

2. TEST FAILURE: test_edge_case now fails
   File: tests/api.test.ts:142
   The refactoring changed how empty inputs are handled.

TESTING:
- Tests written: 8
- Tests passing: 5/8
- 3 behavior changes detected!

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
   - `/03-SHIP/01-pre-commit` — Run pre-commit checks
   - `/03-SHIP/02-commit` — Just commit locally
   - `/03-SHIP/03-push` — Commit and push
   - `/03-SHIP/04-pr` — Commit, push, and create PR

**If failed:**
1. Clear list of issues found
2. Whether they're behavior changes or test failures
3. How to fix each one
4. Offer to adjust the refactoring
5. "Re-run `/03-validate-refactor` after fixes"
