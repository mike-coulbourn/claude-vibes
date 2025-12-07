---
description: Investigate an issue and understand what's wrong
argument-hint: Error message, symptom, or description of what's broken
---

# Diagnose Phase

You are helping a vibe coder understand what's wrong with their code. This is detective work—find the root cause before attempting any fix.

Issue to diagnose: $ARGUMENTS

## Your Role

You orchestrate the investigation and manage the conversation. The diagnostician agent handles deep exploration, while you present findings in plain language and guide next steps.

## Project Context

**Always read these files for core context:**
- `docs/start/` files — Project requirements and architecture
- Any error logs or stack traces the user provides

These are stable project documentation—always load them.

## How to Communicate

- Explain technical errors in plain language
- Be specific about what's broken and why
- Ask clarifying questions if the symptom is unclear
- Use AskUserQuestion to gather more details when needed

## Diagnosis Process

### 1. Load Core Context

Read docs/start/ files for project understanding.

### 2. Understand the Symptom

If `$ARGUMENTS` describes an issue, start there. If not, use AskUserQuestion:
- "What's happening that shouldn't be?"
- "What were you trying to do when this occurred?"
- "Any error messages you're seeing?"

Get enough detail to begin investigation.

### 3. Launch Diagnostician

**Launch the diagnostician agent** with this prompt:

> Ultrathink about diagnosing this issue.
>
> **Symptom:** [describe what's wrong based on user input]
>
> **Parse LOGS.json for relevant history:**
> - Find past fixes in the same `area` or with similar `tags`
> - Look for patterns in previous `rootCause` entries
> - Check if this symptom has occurred before
>
> **Investigate thoroughly:**
> - Trace error messages to their source
> - Check recent changes that might have caused this
> - Look for edge cases or missing validation
> - Test hypotheses by reading relevant code
>
> **Use AskUserQuestion during investigation:**
> - If you need more details about when/how the issue occurs, ask
> - If the symptom could have multiple causes, ask questions to narrow it down
> - If you find something unexpected that needs context, ask the user about it
> - If you're unsure whether something is a bug or expected behavior, ask
> - Never assume you understand the issue—clarify with the user
>
> **Report back with:**
> - Specific LOGS.json entries that are relevant (cite entry IDs)
> - Exact file paths and line numbers where the issue originates
> - Root cause analysis (why is this happening?)
> - Proposed fix approach
>
> Explain findings in plain language a non-coder can understand.

### 4. Load Specific References

After the diagnostician returns:

**Read only the specific references it identified:**
- Read the exact LOGS.json entries it cited
- Read the specific code files/sections it referenced

This gives you relevant context without parsing everything.

### 5. Present Preliminary Findings

Present findings as **preliminary observations that require validation**—not conclusions.

Do NOT assume any behavior is a "bug." What looks wrong might be intentional for reasons you don't understand yet.

If the root cause is unclear, be honest and ask for more information.

### 6. MANDATORY: Validate Diagnosis with User

**Do NOT save any diagnosis doc until you complete this step.**

Use AskUserQuestion to validate your understanding:
- Ask if the behavior you identified as "wrong" is actually unintended
- Ask if what looks like a bug might be intentional for specific use cases
- Ask if your understanding of the expected behavior is correct
- Confirm the root cause matches the user's understanding of the problem

**You must get explicit confirmation from the user** that:
- The identified behavior is actually a bug (not intended)
- Your root cause analysis is accurate
- The proposed fix approach makes sense

### 7. Save Validated Diagnosis

**Only after the user has validated your diagnosis**, save it.

Save the diagnosis to `docs/fix/diagnosis-<issue-name>.md`:

```markdown
# Diagnosis: [Brief Issue Title]

**Date:** [ISO timestamp]
**Symptom:** [What the user observed]

## Root Cause

[Detailed explanation of why this is happening]

## Affected Files

- `path/to/file.ts:line` — [what's wrong here]

## Proposed Fix

[Step-by-step fix approach]

## Related History

[Any relevant LOGS.json entries or past fixes]
```

Use a descriptive name derived from the issue (e.g., `diagnosis-search-500-error.md`).

## Guidelines

- Always read docs/ for core context
- Let the diagnostician explore LOGS.json; read only what it references
- **NEVER assume behavior is a bug**—always validate with the user first
- **NEVER save a diagnosis doc without user validation**
- Don't guess at the fix—understand the problem first
- If unsure, ask more questions
- Save diagnosis for handoff to `/02-fix-issue` only after validation

## Output

When diagnosis is complete:

1. Present preliminary findings to user
2. **Validate diagnosis with AskUserQuestion** before proceeding
3. Confirm root cause and fix approach with user
4. Save validated diagnosis to docs/fix/
5. Next step: "Run `/02-fix-issue docs/fix/diagnosis-<name>.md` to implement the fix"
