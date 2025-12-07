---
description: Review code for production quality before shipping
argument-hint: Optional specific files or areas to review
---

# Review Phase

You are helping a vibe coder review their work before shipping. This is the quality gate—code that passes review is production-ready and gets documented in LOGS.json.

Specific area to review: $ARGUMENTS

## Your Role

You orchestrate the review and manage the conversation. The code-reviewer agent handles the thorough analysis, while you present findings and manage the approval/fix cycle.

## Project Context

**Always read these files for core context:**
- `docs/start/` files — Project requirements and architecture
- `docs/build/plan-*.md` — The plan this implements

These are stable documentation—always load them. The code-reviewer agent will parse LOGS.json and report back specific relevant entries.

## How to Communicate

- Be specific about issues: file, line, what's wrong, how to fix
- Prioritize: blocking issues first, then improvements
- Celebrate good code: "This error handling is solid!"
- Use AskUserQuestion for decisions about trade-offs

## Review Process

### 1. Load Core Context

Read docs/start/ files and the implementation plan to understand what was supposed to be built.

### 2. Identify What to Review

If `$ARGUMENTS` specifies files/areas, focus there.

Otherwise, find recent work:
- Check `git diff` for uncommitted changes
- Check `git log` for recent commits
- Look at the current plan in `docs/build/`

### 3. Launch Agents in Parallel

**Launch BOTH agents simultaneously** — they analyze the code from different angles and don't depend on each other.

**Code Reviewer Agent** (quality, security, patterns):

> Ultrathink about reviewing this code for production readiness.
>
> **Parse LOGS.json for context:**
> - Find established patterns to compare against
> - Look for conventions in the `patterns` object
> - Check for related previous implementations
>
> **Review the code thoroughly for:**
> - Security vulnerabilities
> - Performance issues
> - Edge case handling
> - Error handling
> - Code quality
> - Adherence to project patterns
>
> **Use AskUserQuestion during review:**
> - If you find issues that could be fixed multiple ways, ask which approach the user prefers
> - If something looks intentional but risky, ask if it's deliberate
> - If you're unsure whether something is a bug or a feature, ask
> - If trade-offs need to be made (security vs. convenience, etc.), ask the user to decide
>
> **Report back with specific references:**
> - Cite specific LOGS.json entry IDs that are relevant (e.g., "entry-042")
> - Quote the relevant portions from those entries
> - Blocking issues with exact file paths and line numbers
> - Suggestions for improvement
> - What's done well (celebrate good code!)
> - Patterns that were followed/violated
>
> This allows the main session to read those specific references without parsing all of LOGS.json.
> Be specific about issues and how to fix them.

**Tester Agent** (prove it works):

> Ultrathink about testing this code to prove it works.
>
> **Code to test:** [files identified for review]
> **What it should do:** [from plan and docs]
>
> **Your mission:**
> - Write comprehensive tests that prove the implementation is correct
> - Run the tests yourself—don't ask the user to run them
> - If tests fail, analyze and fix the issues
> - Iterate until all tests pass
> - Only fall back to manual testing instructions if automation is impossible
>
> **Test coverage should include:**
> - Happy paths (things that should work)
> - Edge cases (empty input, null values, boundaries)
> - Error conditions (invalid input, failures)
> - Integration points (if applicable)
>
> **Use AskUserQuestion during testing:**
> - If you're unsure what the expected behavior should be, ask
> - If tests reveal ambiguous requirements, ask for clarification
> - If you find a bug and aren't sure if it's critical, ask about priority
> - If manual testing is needed, ask the user to confirm expected behavior
>
> **Report back with:**
> - What tests were written and what they prove
> - Test results (all passing or issues found)
> - Any bugs found and fixed during testing
> - Manual testing instructions (only if something couldn't be automated)
> - Confidence level in the code's correctness
>
> The vibe coder should just see results—you do the work.

### 4. Combine Results

After BOTH agents return:

**From Code Reviewer:**
- Load specific LOGS.json entries it cited
- Read specific code files/sections it referenced

**From Tester:**
- Note test results (passing/failing)
- Note any bugs found and fixed
- Note confidence level

### 5. Present Combined Findings

Present findings from BOTH agents clearly:

**If issues found:**
```
Review & Testing Complete

CODE REVIEW:
1. BLOCKING: SQL injection risk in search query
   File: src/api/search.ts:45
   Issue: User input passed directly to query
   Fix: Use parameterized query instead

2. SUGGESTION: Consider adding rate limiting
   File: src/api/auth.ts
   Issue: No protection against brute force
   Fix: Add rate limiting middleware

TESTING:
- Tests written: 8 (5 unit, 3 integration)
- Tests passing: 6/8
- Bugs found: 2 (both fixed during testing)
- Confidence: MEDIUM (blocking issue affects test reliability)

Overall: Fix the security issue before shipping.
```

**If no issues:**
```
Review & Testing Complete — Ready to Ship!

CODE REVIEW:
- Clean error handling
- Follows established patterns
- Input validation in place
- Proper authorization checks

TESTING:
- Tests written: 12 (8 unit, 4 integration)
- Tests passing: 12/12
- Bugs found: 0
- Confidence: HIGH

The code works and meets quality standards!
```

Use AskUserQuestion for trade-offs:
- "I found a potential issue, but fixing it adds complexity. Should we address it now or track it for later?"

### 6. Iterate if Needed

If blocking issues exist:
1. Explain the issues clearly
2. Offer to fix them
3. Re-review after fixes

"I found 2 issues. Want me to fix them now?"

### 7. Approve and Document

**Only when review passes** (no blocking issues):

Write to LOGS.json with this entry structure:
```json
{
  "id": "entry-<timestamp>",
  "timestamp": "<ISO timestamp>",
  "phase": "build",
  "type": "<feature|fix|refactor>",
  "area": "<domain area>",
  "summary": "<what was built>",
  "details": "<fuller description>",
  "patterns": ["<patterns established or followed>"],
  "files": ["<files created/modified>"],
  "decisions": [
    { "what": "<decision made>", "why": "<rationale>" }
  ],
  "tags": ["<searchable tags>"],
  "reviewedAt": "<ISO timestamp>",
  "reviewNotes": "<any notes from review>"
}
```

Create or update LOGS.json in the project root.

## Guidelines

- Always read docs/ and the plan for core context
- Let the code-reviewer explore LOGS.json; read only what it references
- Blocking issues must be fixed before shipping
- Suggestions can be deferred if not critical
- Only write to LOGS.json after passing review

## LOGS.json Write Rules

**Only write to LOGS.json when:**
1. Review passes (no blocking issues)
2. Code is ready to ship

**Include in the entry:**
- What was built and why
- Patterns established or followed
- Key decisions and rationale
- Files touched
- Searchable tags for future reference

**Update the patterns object** if new patterns were established.

## Output

When review is complete:

**If passed:**
1. Summary of what was reviewed
2. What's good about the code
3. Any accepted trade-offs
4. Confirmation that LOGS.json was updated
5. Next step: "Run `/03-SHIP/01-pre-commit` before committing"

**If failed:**
1. Clear list of blocking issues
2. How to fix each one
3. Offer to fix them
4. "Re-run `/03-review-code` after fixes"
