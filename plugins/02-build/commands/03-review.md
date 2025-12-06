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

### 3. Launch Code Reviewer

**Launch the code-reviewer agent** with this prompt:

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

### 4. Load Specific References

After the code-reviewer returns:

**Read only the specific references it identified:**
- Read the exact LOGS.json entries it cited (by ID or content)
- Read the specific code files/sections it referenced

This gives you relevant build history without reading the entire LOGS.json.

### 5. Present Findings

Present the code-reviewer's findings clearly:

**If issues found:**
```
Review complete. Found 2 issues:

1. BLOCKING: SQL injection risk in search query
   File: src/api/search.ts:45
   Issue: User input passed directly to query
   Fix: Use parameterized query instead

2. SUGGESTION: Consider adding rate limiting
   File: src/api/auth.ts
   Issue: No protection against brute force
   Fix: Add rate limiting middleware

Overall: Good structure, patterns followed. Fix the security issue before shipping.
```

**If no issues:**
```
Review complete. Code is production-ready!

What's good:
- Clean error handling
- Follows established patterns
- Input validation in place
- Proper authorization checks

Ready to ship!
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
5. Next step: "Run `/03-ship/01-check` before committing"

**If failed:**
1. Clear list of blocking issues
2. How to fix each one
3. Offer to fix them
4. "Re-run `/03-review` after fixes"
