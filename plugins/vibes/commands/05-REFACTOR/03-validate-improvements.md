---
description: Verify refactoring preserved behavior and document it
argument-hint: Optional specific files or areas to validate
---

# Validate Phase

You are helping a vibe coder confirm their refactoring preserved behavior and didn't break anything. This is the quality gate—refactorings that pass validation get documented in LOGS.json.

Specific area to validate: $ARGUMENTS

## Your Role

You orchestrate the validation and manage the conversation. The validator agent handles thorough testing, while you present findings and manage the documentation.

**CRITICAL: You MUST use the Task tool to launch the validation agents.** Do not validate the refactoring yourself—that's what the validator and tester agents are for.

## Interactive Experience (CRITICAL)

**ALWAYS use the AskUserQuestion tool when interacting with the user.** This ensures a guided, interactive experience:

Use AskUserQuestion to:
- Ask if subtle behavior changes are acceptable
- Clarify expected behavior when tests reveal ambiguity
- Present trade-offs when issues are found
- Get approval before documenting in LOGS.json

Never assume validation criteria. Ask to confirm.

## Project Context

**Always read these files for core context:**
- `docs/01-START/` files — Project requirements and architecture
- `docs/05-REFACTOR/assessment-*.md` — The assessment for this refactoring

These are stable documentation—always load them. The validator agent will parse LOGS.json and report back specific relevant entries.

**Fallback if docs/01-START/ doesn't exist:**
If these files don't exist (common when using claude-vibes on an existing project), explore the codebase directly to understand the project's structure, patterns, and conventions.

**Fallback if no assessment file exists:**
If no assessment file exists, use `git diff` and `git log` to understand what was changed, and use AskUserQuestion to understand what the refactoring was supposed to accomplish.

## How to Communicate

- Be clear about what passed and what failed
- Explain any behavior changes found (even subtle ones)
- Celebrate when everything works
- Use AskUserQuestion for judgment calls

## Validate Process

### 1. Load Context

Read docs/01-START/ files and the most recent assessment file to understand what was refactored and why.

### 2. Identify What to Validate

If `$ARGUMENTS` specifies files/areas, focus there.

Otherwise, find the recent refactoring:
- Check `git diff` for uncommitted changes
- Read the most recent `docs/05-REFACTOR/assessment-*.md`
- Look at recently modified files

### 3. Launch Agents in Parallel (REQUIRED)

**You MUST use the Task tool to launch BOTH agents simultaneously** — they validate the refactoring from different angles and don't depend on each other. Use `subagent_type: "claude-vibes:validator"` and `subagent_type: "claude-vibes:tester"`.

**Validator Agent** (confirm behavior preserved):

> Ultrathink about validating this refactoring.
>
> **What was refactored:** [from assessment or git diff]
> **Expected behavior:** Same as before—no functional changes
>
> **Parse LOGS.json for context (if it exists):**
> - Find related past refactorings
> - Identify patterns that should be verified
> - Check for areas that commonly have subtle behavior changes
> - If LOGS.json doesn't exist, skip this and focus on direct validation
>
> **Validate thoroughly:**
> - Run all related tests (do they still pass?)
> - Check for behavior preservation (does it do the same thing?)
> - Look for subtle changes (error messages, timing, edge cases)
> - Verify the improvement was achieved (is it actually better?)
>
> **Use AskUserQuestion during validation:**
> - If you find subtle behavior changes, ask if they're acceptable or problematic
> - If tests reveal unclear expected behavior, ask the user to clarify
> - If the improvement is hard to quantify, ask what success looks like to them
> - If you're unsure whether something is a regression, ask
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
> **Use AskUserQuestion during testing:**
> - If you're unsure what the original behavior was, ask the user to describe it
> - If tests reveal unclear requirements, ask for clarification
> - If you detect a behavior change, ask if it was intentional
> - If you're unsure which scenarios are important to test, ask
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
5. "Re-run `/03-validate-improvements` after fixes"

### Store Validation Insights in Memory

**If validation revealed useful patterns or insights not already documented**, store them for future sessions.

**Use the memory MCP tools:**

1. **For validation patterns discovered:**
   ```
   Use create_entities or add_observations to store in "ValidationPatterns":
   - Testing strategies that worked well (e.g., "For refactorings, compare before/after output for 10 representative inputs")
   - Subtle behavior areas (e.g., "String formatting in reports is sensitive — always diff the output")
   - What to watch for (e.g., "Refactoring async code often introduces subtle timing differences")
   ```

2. **For refactoring patterns:**
   ```
   Use create_entities or add_observations to store in "RefactoringPatterns":
   - Successful patterns (e.g., "Extracting to a strategy pattern preserved behavior cleanly")
   - Gotchas discovered (e.g., "The old code handled null differently than it appeared — preserve that quirk")
   ```

**Only store NEW findings** — insights that will help validate future refactorings. If nothing notable was discovered, skip this step.

**Example observations to store:**
- "Error message format matters to the frontend — don't change it during refactoring"
- "The order of keys in JSON responses is tested — sorting alphabetically breaks tests"
- "Performance tests should run before and after major refactorings to catch regressions"
