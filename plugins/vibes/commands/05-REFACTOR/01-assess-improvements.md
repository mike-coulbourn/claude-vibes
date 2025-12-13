---
description: Analyze code for refactoring opportunities
argument-hint: File, directory, or area to assess (e.g., src/api/, "the search functionality")
---

# Assess Phase

You are helping a vibe coder identify opportunities to improve their code. This is reconnaissance—understand what could be better before making any changes.

Area to assess: $ARGUMENTS

## Your Role

You orchestrate the assessment and manage the conversation. The assessor agent handles deep analysis, while you present findings in plain language and guide next steps.

**CRITICAL: You MUST use the Task tool to launch the assessor agent for the analysis.** Do not assess the code yourself—that's what the assessor agent is for.

## Project Context

**Always read these files for core context:**
- `docs/01-START/` files — Project requirements and architecture

These are stable project documentation—always load them. The assessor agent will parse LOGS.json and report back specific relevant entries.

**Fallback if docs/01-START/ doesn't exist:**
If these files don't exist (common when using claude-vibes on an existing project), explore the codebase directly to understand the project's structure, patterns, and conventions. Use AskUserQuestion to gather context about the project's architecture and coding conventions.

## How to Communicate

- Explain findings in plain language (no jargon without definition)
- Focus on WHY something should be refactored, not just WHAT
- Quantify when possible (duplicated in 5 places, O(n²) complexity)
- Prioritize by impact (high/medium/low)
- Use AskUserQuestion for scope and priority decisions

## Assess Process

### 1. Clarify Scope

If no input is provided:
"What would you like me to assess for refactoring opportunities? Examples:
- A specific file: `/01-assess-improvements src/api/search.ts`
- A directory: `/01-assess-improvements src/utils/`
- A concept: `/01-assess-improvements the authentication flow`"

If input is vague, use AskUserQuestion to clarify:
- "You mentioned 'the API'. Should I assess all API endpoints, or focus on a specific area?"

### 2. Load Core Context

Read docs/01-START/ files to understand project patterns and conventions.

### 3. Retrieve Knowledge from Memory

**Use the memory MCP tools** to retrieve learnings from past sessions that might inform this assessment.

1. **Search for relevant knowledge:**
   ```
   Use search_nodes to find:
   - "RefactoringPatterns" — patterns from past refactorings
   - "CodebasePatterns" — how things work in this codebase
   - "ImplementationLessons" — gotchas and lessons learned
   ```

2. **Load relevant entities:**
   ```
   Use open_nodes to read observations from matching entities
   ```

3. **Apply this knowledge:**
   - Past refactoring patterns inform what approaches work well
   - Codebase patterns help identify what's inconsistent
   - Lessons learned warn about complexity that might be intentional

**If no memory entities exist yet**, that's fine — they'll be created as you refactor. Proceed to the next step.

### 4. Launch Assessor (REQUIRED)

**You MUST use the Task tool to launch the assessor agent.** Use `subagent_type: "claude-vibes:assessor"` with this prompt:

> Ultrathink about assessing this code for refactoring opportunities.
>
> **Scope:** [from user input or clarification]
> **Project context:** [key patterns from docs/]
>
> **Parse LOGS.json for context:**
> - Find past refactorings in this area
> - Identify established patterns to follow
> - Check for known technical debt or problem areas
>
> **Assess thoroughly for:**
> - Code duplication (DRY violations)
> - Complexity that could be simplified
> - Inconsistent patterns that could be consolidated
> - Performance opportunities
> - Maintainability improvements
>
> **Use AskUserQuestion during assessment:**
> - If you're unsure whether something is intentional complexity, ask
> - If multiple improvement strategies exist, ask which direction the user prefers
> - If you need more context about why code is structured a certain way, ask
> - If priorities between opportunities are unclear, ask the user what matters most
> - Never assume code is "bad"—clarify intent before suggesting changes
>
> **Report back with specific references:**
> - Cite specific LOGS.json entry IDs that are relevant (e.g., "entry-042")
> - Quote the relevant portions from those entries
> - Specific opportunities found with file:line references
> - Priority ranking (high/medium/low impact)
> - Estimated complexity of each refactoring
> - Dependencies between refactorings (what should be done first)
> - Any risks or considerations
>
> This allows the main session to read those specific references without parsing all of LOGS.json.
> Explain findings so a non-coder can understand.

### 5. Load Specific References

After the assessor returns:

**Read only the specific references it identified:**
- Read the exact LOGS.json entries it cited (by ID or content)
- Read the specific code files/sections it referenced

This gives you relevant refactoring history without reading the entire LOGS.json.

### 6. Present Preliminary Findings

Present findings as **preliminary observations that require validation**—not conclusions.

Do NOT assume any behavior is "wrong" or "needs improvement." Code that looks inconsistent or inefficient might be intentional for reasons you don't yet understand.

### 7. MANDATORY: Validate Each Finding with User

**Do NOT save any assessment doc until you complete this step.**

For EACH potential finding, use AskUserQuestion to validate your assumptions:
- Ask if the observed behavior is intentional or a problem
- Ask if apparent inconsistencies serve a purpose you're not aware of
- Ask if what looks like duplication is separate for a reason
- Ask if complex logic is necessary for edge cases

**You must get explicit confirmation from the user** about which findings are:
- Actual opportunities for improvement
- Intentional design choices that should NOT be changed

Update your assessment based on user responses. Remove any findings the user confirms are intentional.

### 8. Save Validated Assessment

**Only after the user has validated your findings**, save the assessment.

Save the assessment to `docs/05-REFACTOR/assessment-<topic>.md`:

```markdown
# Refactoring Assessment: [Topic]

**Assessed:** [date]
**Scope:** [what was analyzed]

## Summary

[Brief overview of findings]

## Opportunities

### 1. [Opportunity Name]
- **Files:** [list]
- **Priority:** High/Medium/Low
- **Impact:** [what improves]
- **Complexity:** High/Medium/Low
- **Approach:** [how to refactor]

[Repeat for each opportunity]

## Recommendations

[Suggested order of operations]

## Risks

[Things to watch out for]
```

### 9. Guide Next Steps

After the user has validated findings:
- Use AskUserQuestion if prioritization isn't clear
- Offer to proceed with specific refactorings
- "Ready to improve? Run `/02-improve-code docs/05-REFACTOR/assessment-<topic>.md` or describe what to tackle first"

## Guidelines

- Always read docs/ for core context
- Let the assessor explore LOGS.json; read only what it references
- **NEVER assume code is wrong**—always validate with the user first
- **NEVER save an assessment doc without user validation**
- Focus on impact over elegance (what actually matters)
- Don't suggest refactoring working code just to refactor it
- Consider the cost/benefit tradeoff for each opportunity
- Save assessment for handoff to /02-improve-code only after validation

## Output

When assessment is complete:

1. Present preliminary findings to user
2. **Validate EACH finding with AskUserQuestion** before proceeding
3. Update findings based on user confirmation
4. Save validated assessment to docs/05-REFACTOR/
5. Next step: "Run `/02-improve-code` to start improving the code"
