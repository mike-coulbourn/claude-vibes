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

### 5. Present Findings

Explain the diagnosis clearly:

```
Here's what I found:

**What's happening:**
[Plain language description of the visible problem]

**Why it's happening:**
[Root cause explanation - what's actually broken in the code]

**Where it's happening:**
- File: src/api/search.ts:45
- The issue: [specific code problem]

**How to fix it:**
[Proposed approach]
```

If the root cause is unclear, be honest:
- "I have a few theories but need more information..."
- "This could be one of two things. Can you tell me..."

### 6. Save Diagnosis

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
- Don't guess at the fix—understand the problem first
- If unsure, ask more questions
- Save diagnosis for handoff to `/02-fix-issue`

## Output

When diagnosis is complete:

1. Summary of what's broken and why (plain language)
2. Specific file locations and line numbers
3. Proposed fix approach
4. Path to saved diagnosis file
5. Next step: "Run `/02-fix-issue docs/fix/diagnosis-<name>.md` to implement the fix"
