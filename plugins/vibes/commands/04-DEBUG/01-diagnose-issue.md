---
description: Investigate an issue and understand what's wrong
argument-hint: Error message, symptom, or description of what's broken
---

# Diagnose Phase

You are helping a vibe coder understand what's wrong with their code. This is detective work—find the root cause before attempting any fix.

Issue to diagnose: $ARGUMENTS

## Your Role

**CRITICAL: ALWAYS use the AskUserQuestion tool for ANY question to the user. Never ask questions as plain text output.** The AskUserQuestion tool ensures a guided, interactive experience with structured options. Every single user question must go through this tool.

You orchestrate the investigation and manage the conversation. The diagnostician agent handles deep exploration, while you present findings in plain language and guide next steps.

**CRITICAL: You MUST use the Agent tool to launch the diagnostician agent for the investigation.** Do not investigate the issue yourself—that's what the diagnostician agent is for.

## Interactive Experience (CRITICAL)

**ALWAYS use the AskUserQuestion tool when interacting with the user.** This ensures a guided, interactive experience:

Use AskUserQuestion to:
- Clarify symptoms or scope when information is vague
- Present multiple hypotheses and ask which sounds right
- Validate findings before proceeding with fixes
- Get approval before documenting results

Never assume you fully understand the problem. Ask to confirm.

## Project Context

**Always read these files for core context:**
- `docs/01-START/` files — Project requirements and architecture
- Any error logs or stack traces the user provides

These are stable project documentation—always load them.

**Fallback if docs/01-START/ doesn't exist:**
If these files don't exist (common when using claude-vibes on an existing project), explore the codebase directly to understand the project's structure, patterns, and conventions. Use AskUserQuestion to gather context about the project's architecture and how components interact.

## How to Communicate

- Explain technical errors in plain language
- Be specific about what's broken and why
- Ask clarifying questions if the symptom is unclear
- Use AskUserQuestion to gather more details when needed

## Diagnosis Process

### 1. Load Core Context

Read docs/01-START/ files for project understanding.

### 2. Recall Past Learnings

The diagnostician agent you launch below keeps its own project memory and loads it automatically. When you write its prompt, tell it which topics to check its memory for:

- diagnostic knowledge — root causes and patterns from past debugging
- codebase patterns — how things work in this codebase
- implementation lessons — gotchas that might be causing issues

That knowledge helps in three ways: past root causes may hint at what's happening now, known gotchas might explain unexpected behavior, and pattern knowledge helps narrow down where issues originate.

**If nothing exists yet**, that's fine — it'll accumulate as you debug. Proceed to the next step.

### 3. Understand the Symptom

If `$ARGUMENTS` describes an issue, start there. If not, use AskUserQuestion:
- "What's happening that shouldn't be?"
- "What were you trying to do when this occurred?"
- "Any error messages you're seeing?"

Get enough detail to begin investigation.

### 4. Launch Diagnostician (REQUIRED)

**You MUST use the Agent tool to launch the diagnostician agent.** Use `subagent_type: "claude-vibes:CODING:diagnostician"` with this prompt:

> Ultrathink about diagnosing this issue.
>
> **Symptom:** [describe what's wrong based on user input]
>
> Check your project memory for related past diagnoses, codebase patterns, and implementation gotchas before starting, and record what you learn before finishing.
>
> **Parse LOGS.json for relevant history (if it exists):**
> - Find past fixes in the same `area` or with similar `tags`
> - Look for patterns in previous `rootCause` entries
> - Check if this symptom has occurred before
> - If LOGS.json doesn't exist, skip this and focus on direct codebase investigation
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

### 5. Load Specific References

After the diagnostician returns:

**Read only the specific references it identified:**
- Read the exact LOGS.json entries it cited
- Read the specific code files/sections it referenced

This gives you relevant context without parsing everything.

### 6. Present Preliminary Findings

Present findings as **preliminary observations that require validation**—not conclusions.

Do NOT assume any behavior is a "bug." What looks wrong might be intentional for reasons you don't understand yet.

If the root cause is unclear, be honest and ask for more information.

### 7. MANDATORY: Validate Diagnosis with User

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

### 8. Save Validated Diagnosis

**Only after the user has validated your diagnosis**, save it.

Save the diagnosis to `docs/04-DEBUG/diagnosis-<issue-name>.md`:

```markdown
# Diagnosis: [Brief Issue Title]

**Date:** [ISO timestamp]
**Symptom:** [What the user observed]

## Root Cause

[Detailed explanation of why this is happening]

## Affected Files

- `path/to/file.ts:line`: [what's wrong here]

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
4. Save validated diagnosis to docs/04-DEBUG/
5. Next step: "Run `/02-fix-issue docs/04-DEBUG/diagnosis-<name>.md` to implement the fix"

### Record Diagnostic Findings

In the diagnostician's prompt, ask it to record durable learnings in its project memory before it finishes:

1. **Root cause patterns discovered:**
   - Common root causes (e.g., "Race conditions often occur when X and Y happen simultaneously")
   - Symptom-to-cause mappings (e.g., "500 errors on /api/search usually trace to database timeouts")
   - Investigation shortcuts (e.g., "When auth fails, check token expiry first")

2. **Codebase-specific gotchas:**
   - Quirks discovered during investigation (e.g., "The cache invalidation is delayed by 5 seconds")
   - Non-obvious dependencies (e.g., "UserService depends on NotificationService being initialized first")

**Only record NEW findings**: insights that will help diagnose future issues faster. If nothing notable was discovered, skip this step.

If the user's review surfaced a lesson that every future session should know, offer to add it to the project's CLAUDE.md.

**Example observations to store:**
- "Null pointer exceptions in OrderService usually mean the user's cart was cleared mid-checkout"
- "The retry logic in ApiClient masks original errors — check logs for the root cause"
- "WebSocket disconnects are often caused by nginx timeout settings, not the app"
