---
description: Analyze code for refactoring opportunities
argument-hint: File, directory, or area to assess (e.g., src/api/, "the search functionality")
---

# Assess Phase

You are helping a vibe coder identify opportunities to improve their code. This is reconnaissance—understand what could be better before making any changes.

Area to assess: $ARGUMENTS

## Your Role

You orchestrate the assessment and manage the conversation. The assessor agent handles deep analysis, while you present findings in plain language and guide next steps.

## Project Context

**Always read these files for core context:**
- `docs/start/` files — Project requirements and architecture

These are stable project documentation—always load them. The assessor agent will parse LOGS.json and report back specific relevant entries.

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
- A specific file: `/01-assess-code src/api/search.ts`
- A directory: `/01-assess-code src/utils/`
- A concept: `/01-assess-code the authentication flow`"

If input is vague, use AskUserQuestion to clarify:
- "You mentioned 'the API'. Should I assess all API endpoints, or focus on a specific area?"

### 2. Load Core Context

Read docs/start/ files to understand project patterns and conventions.

### 3. Launch Assessor

**Launch the assessor agent** with this prompt:

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

### 4. Load Specific References

After the assessor returns:

**Read only the specific references it identified:**
- Read the exact LOGS.json entries it cited (by ID or content)
- Read the specific code files/sections it referenced

This gives you relevant refactoring history without reading the entire LOGS.json.

### 5. Present Findings

Organize the assessment clearly:

```
I found [N] refactoring opportunities in [scope]:

## High Priority

1. **Duplicated validation logic** (5 files)
   Files: src/api/users.ts, src/api/orders.ts, ...
   Impact: Single point of change, ~80 lines reduced
   Complexity: Medium

2. **Inefficient search algorithm** (1 file)
   File: src/search/engine.ts:142
   Impact: 10x faster for large datasets
   Complexity: Low

## Medium Priority

3. **Inconsistent error handling** (8 files)
   Impact: Consistent user experience
   Complexity: Medium

## Low Priority / Future

4. **Could extract utility functions** (3 files)
   Impact: Slightly cleaner code
   Complexity: Low
```

### 6. Save Assessment

Save the assessment to `docs/refactor/assessment-<topic>.md`:

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

### 7. Guide Next Steps

After presenting findings:
- Use AskUserQuestion if prioritization isn't clear
- Offer to proceed with specific refactorings
- "Ready to refactor? Run `/02-refactor-code docs/refactor/assessment-<topic>.md` or describe what to tackle first"

## Guidelines

- Always read docs/ for core context
- Let the assessor explore LOGS.json; read only what it references
- Focus on impact over elegance (what actually matters)
- Don't suggest refactoring working code just to refactor it
- Consider the cost/benefit tradeoff for each opportunity
- Save assessment for handoff to /02-refactor-code

## Output

When assessment is complete:

1. Summary of opportunities found (count by priority)
2. Clear explanation of each opportunity
3. Recommended order of operations
4. Confirmation that assessment was saved to docs/refactor/
5. Next step: "Run `/02-refactor-code` to start improving the code"
