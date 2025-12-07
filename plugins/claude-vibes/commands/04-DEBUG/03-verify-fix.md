---
description: Verify a fix works and document it in LOGS.json
argument-hint: Optional specific files or areas to verify
---

# Verify Phase

You are helping a vibe coder confirm their fix works and doesn't break anything else. This is the quality gate—fixes that pass verification get documented in LOGS.json.

Specific area to verify: $ARGUMENTS

## Your Role

You orchestrate the verification and manage the conversation. The verifier agent handles thorough testing, while you present findings and manage the approval/documentation cycle.

**CRITICAL: You MUST use the Task tool to launch the verification agents.** Do not verify the fix yourself—that's what the verifier and tester agents are for.

## Project Context

**Always read these files for core context:**
- `docs/start/` files — Project requirements and architecture
- `docs/fix/diagnosis-*.md` — The diagnosis for this fix

These are stable documentation—always load them. The verifier agent will parse LOGS.json and report back specific relevant entries.

**Fallback if docs/start/ doesn't exist:**
If these files don't exist (common when using claude-vibes on an existing project), explore the codebase directly to understand the project's structure, patterns, and conventions.

**Fallback if no diagnosis file exists:**
If no diagnosis file exists, use `git diff` and `git log` to understand what was changed, and use AskUserQuestion to understand what the fix was supposed to accomplish.

## How to Communicate

- Be clear about what passed and what failed
- Explain any regressions in plain language
- Celebrate when everything works
- Use AskUserQuestion for decisions about edge cases

## Verify Process

### 1. Load Core Context

Read docs/start/ files and the most recent diagnosis file to understand what was fixed.

### 2. Identify What to Verify

If `$ARGUMENTS` specifies files/areas, focus there.

Otherwise, find the recent fix:
- Check `git diff` for uncommitted changes
- Read the most recent `docs/fix/diagnosis-*.md`
- Look at recently modified files

### 3. Launch Agents in Parallel (REQUIRED)

**You MUST use the Task tool to launch BOTH agents simultaneously** — they verify the fix from different angles and don't depend on each other. Use `subagent_type: "claude-vibes:verifier"` and `subagent_type: "claude-vibes:tester"`.

**Verifier Agent** (confirm fix works, check regressions):

> Ultrathink about verifying this fix.
>
> **What was fixed:** [from diagnosis file]
> **Files changed:** [from git diff or diagnosis]
>
> **Parse LOGS.json for context (if it exists):**
> - Find related past fixes to inform testing
> - Identify patterns that should be verified
> - Check for areas that commonly regress
> - If LOGS.json doesn't exist, skip this and focus on direct verification
>
> **Verify thoroughly:**
> - Test the specific issue that was fixed (does it work now?)
> - Run related tests (do existing tests still pass?)
> - Check for regressions (did we break anything else?)
> - Verify edge cases mentioned in the diagnosis
>
> **Use AskUserQuestion during verification:**
> - If you're unsure what "fixed" should look like, ask the user to describe expected behavior
> - If you find an edge case that wasn't covered, ask if it's important
> - If verification reveals unclear requirements, ask for clarification
> - If you're unsure whether a behavior change is acceptable, ask
>
> **Report back with specific references:**
> - Cite specific LOGS.json entry IDs that are relevant (e.g., "entry-042")
> - Quote the relevant portions from those entries
> - Specific test results (what passed, what failed)
> - Whether the original issue is resolved
> - Any regressions found
> - LOGS.json entry recommendation with:
>   - symptom, rootCause, summary, details, prevention
>   - files modified, tags, area
>
> This allows the main session to read those specific references without parsing all of LOGS.json.
> Be specific about verification results.

**Tester Agent** (write tests that prove the fix):

> Ultrathink about testing this fix to prove it works.
>
> **What was fixed:** [from diagnosis file]
> **Files changed:** [from git diff or diagnosis]
>
> **Your mission:**
> - Write tests that would have caught the original bug
> - Write tests that prove the fix works
> - Run the tests yourself—don't ask the user to run them
> - If tests fail, analyze and fix the issues
> - Iterate until all tests pass
> - Only fall back to manual testing instructions if automation is impossible
>
> **Test coverage should include:**
> - The exact scenario that caused the bug
> - Edge cases related to the fix
> - Regression tests to prevent the bug from returning
> - Integration points affected by the fix
>
> **Use AskUserQuestion during testing:**
> - If you're unsure what the correct behavior should be, ask
> - If tests reveal ambiguous requirements, ask for clarification
> - If you find additional bugs, ask about priority
> - If you need to understand the original bug better, ask the user to describe it
>
> **Report back with:**
> - Tests written that prove the fix works
> - Tests that would have caught the original bug
> - Test results (all passing or issues found)
> - Any additional bugs found during testing
> - Manual testing instructions (only if something couldn't be automated)
> - Confidence level that the fix is solid
>
> The vibe coder should just see results—you do the work.

### 4. Combine Results

After BOTH agents return:

**From Verifier:**
- Load specific LOGS.json entries it cited
- Note whether original issue is fixed
- Note any regressions found

**From Tester:**
- Note tests written and what they prove
- Note test results (passing/failing)
- Note confidence level

### 5. Present Combined Findings

**If all verifications pass:**
```
Verification & Testing Complete — Fix Confirmed!

VERIFICATION:
- Original issue: FIXED
- Related tests: All passing
- Regressions: None found

TESTING:
- Tests written: 6 (regression tests for the bug)
- Tests passing: 6/6
- This bug can't come back now!
- Confidence: HIGH

The fix is solid and ready to ship.
```

**If issues found:**
```
Verification & Testing Found Problems

VERIFICATION:
1. REGRESSION: Test 'userSearch' now fails
   File: tests/search.test.ts
   Expected: Results for "café"
   Got: Empty array

2. PARTIAL FIX: Original issue fixed for ASCII, but Unicode still fails
   File: src/api/search.ts:52

TESTING:
- Tests written: 4
- Tests passing: 2/4
- The bug still occurs in some scenarios

These need to be addressed before shipping.
```

Use AskUserQuestion for judgment calls:
- "The main issue is fixed, but I found an unrelated failing test. Should we fix that too or track it separately?"

### 6. Iterate if Needed

If issues exist:
1. Explain what's wrong clearly
2. Offer to go back and fix them
3. Re-run verification after fixes

"I found 1 regression. Want me to fix it now?"

### 7. Document in LOGS.json

**Only when verification passes** (no regressions, fix confirmed working):

Write to LOGS.json with this entry structure:
```json
{
  "id": "entry-<timestamp>",
  "timestamp": "<ISO timestamp>",
  "phase": "fix",
  "type": "fix",
  "area": "<domain area where bug occurred>",
  "symptom": "<what the user observed>",
  "rootCause": "<why it broke>",
  "summary": "<what was fixed>",
  "details": "<fuller description of the fix>",
  "prevention": "<how to prevent similar issues>",
  "patterns": ["<patterns followed in the fix>"],
  "files": ["<files modified>"],
  "tags": ["bug", "<error type>", "<area>"],
  "verifiedAt": "<ISO timestamp>",
  "verifyNotes": "<any notes from verification>"
}
```

Create or update LOGS.json in the project root.

## Guidelines

- Always read docs/ and diagnosis for context
- Let the verifier explore LOGS.json; read only what it references
- The original issue must be confirmed fixed
- Regressions must be fixed before shipping
- Only write to LOGS.json after passing verification

## LOGS.json Write Rules

**Only write to LOGS.json when:**
1. Verification passes (no regressions)
2. Original issue confirmed fixed
3. Fix is ready to ship

**Include in the entry:**
- Symptom (what user saw)
- Root cause (why it happened)
- What was fixed and how
- Prevention advice for future
- Files touched and searchable tags

## Output

When verification is complete:

**If passed:**
1. Summary of what was verified
2. Confirmation the fix works
3. Any accepted trade-offs
4. Confirmation that LOGS.json was updated
5. Next steps:
   - `/03-SHIP/01-pre-commit` — Run pre-commit checks
   - `/03-SHIP/02-commit` — Just commit locally
   - `/03-SHIP/03-push` — Commit and push
   - `/03-SHIP/04-pr` — Commit, push, and create PR

**If failed:**
1. Clear list of issues found
2. How to fix each one
3. Offer to fix them
4. "Re-run `/03-verify-fix` after fixes"
