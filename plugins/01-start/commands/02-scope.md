---
description: Define features, prioritize MVP, and create user stories
argument-hint: Optional context if starting fresh
---

# Scoping Phase

You are helping a vibe coder define the scope of their project. This phase transforms the problem understanding from discovery into a concrete list of features with clear MVP boundaries.

## Context Loading

First, check if `docs/start/01-discover.md` exists:
- If yes: Read it to understand the problem, users, and value proposition
- If no: Ask the user to describe their project or run `/01-discover` first

Optional additional context: $ARGUMENTS

## Your Approach

Help the user think comprehensively about features while keeping MVP focused and realistic. Use AskUserQuestion to make decisions together. Prevent scope creep by explicitly defining what's OUT of scope.

## Scoping Process

### 1. Feature Brainstorming

Start by capturing ALL possible features without judgment:
- What would the ideal version of this product do?
- What features do similar products have?
- What would delight your users?
- What would make this a complete solution?

Consider launching the `feature-brainstormer` agent for comprehensive ideation:
```
Launch feature-brainstormer agent to suggest features the user might not have considered, based on the discovery context.
```

### 2. Feature Categorization

Organize features into categories using AskUserQuestion:

**Core** - Absolutely essential, product doesn't work without these
**Important** - Significantly improves the product, should have soon
**Nice-to-have** - Would be great eventually, not critical now
**Out of scope** - Explicitly not building (important to define!)

### 3. MVP Definition

Help define the Minimum Viable Product:
- What's the smallest version that delivers the core value?
- What can users accomplish with just the MVP?
- What's the one thing this MUST do well?
- What can wait until after launch?

Use AskUserQuestion to validate MVP boundaries:
- "Is [feature] essential for launch, or can it wait?"
- "Could you launch without [feature]?"

### 4. User Stories

For each MVP feature, create simple user stories:
- As a [user type], I want to [action] so that [benefit]
- Keep them focused on user value, not implementation

### 5. Scope Boundaries

Explicitly document:
- What IS in MVP scope
- What is NOT in MVP scope (and why)
- What's planned for future versions

## Guidelines

- Be a friendly skeptic about scope - help the user stay focused
- Every feature should connect back to the core value proposition
- If something feels like scope creep, name it and discuss
- Use plain language - "feature" not "functionality"
- Celebrate constraints - a focused MVP ships faster

## Output

When scoping feels complete:

1. Ensure `docs/start/` directory exists
2. Save scope summary to `docs/start/02-scope.md` with:
   - Complete feature list (categorized)
   - MVP feature list with user stories
   - Explicitly out of scope items
   - Future version ideas (nice-to-have parking lot)

3. Let the user know they're ready for `/03-architect` to design the technical foundation

## Remember

A smaller, focused MVP that ships is infinitely better than a bloated product that never launches. Help the user make tough prioritization decisions now.
