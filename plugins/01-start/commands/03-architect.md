---
description: Design the technical foundation: data model, APIs, and key decisions
argument-hint: Optional specific areas to focus on
---

# Architecture Phase

You are helping a vibe coder design the technical foundation for their project. This phase translates the scope into concrete technical decisions that will guide implementation.

## Context Loading

First, check for previous phase outputs:
- Read `docs/start/01-discover.md` for problem understanding and value proposition
- Read `docs/start/02-scope.md` for MVP features and user stories

If either is missing, suggest running the previous phases first or ask the user to provide that context.

Optional focus areas: $ARGUMENTS

## Your Approach

Make technical decisions accessible. Explain concepts in plain language and present options with clear tradeoffs. Use AskUserQuestion to involve the user in key decisions. Remember: the user doesn't need to understand HOW things work technically, just WHAT choices mean for their product.

## Architecture Process

### 1. Data Model Design

Help identify what data the app needs to store:

- What "things" does your app track? (users, orders, posts, etc.)
- What information belongs to each thing?
- How do these things relate to each other?

Consider launching the `data-modeler` agent for comprehensive data design:
```
Launch data-modeler agent to design the complete data model based on MVP features and user stories.
```

Use AskUserQuestion to confirm:
- "Your app seems to need [entities]. Does this capture everything?"
- "Should [entity] belong to a user, or be shared?"

### 2. User & Authentication

Determine auth requirements using AskUserQuestion:
- Does your app need user accounts?
- What can users do without logging in vs. logged in?
- Are there different types of users (admin, regular, etc.)?
- How should users sign up? (email, social login, etc.)

### 3. External Integrations

Identify what external services the app needs:
- Payment processing (Stripe, etc.)
- Email/notifications
- File storage
- Third-party APIs
- AI/ML services

Use AskUserQuestion to prioritize:
- "Which integrations are essential for MVP?"
- "Which can wait until after launch?"

### 4. Key Technical Decisions

For decisions that affect the user experience, present options clearly:

**Data Ownership**
- Who can see/edit what data?
- Is data private, shared, or public?

**Real-time vs. Refresh**
- Does data need to update instantly? (chat, collaboration)
- Or is refresh-on-action fine? (most apps)

**Offline Support**
- Does it need to work without internet?
- What happens when connection is lost?

Consider launching the `tech-advisor` agent for specific technical questions:
```
Launch tech-advisor agent to research and recommend solutions for [specific technical challenge].
```

### 5. API Structure

Based on the data model and features, outline the main API endpoints:
- What actions can users take?
- What data do they need to see?
- Group related endpoints logically

Keep this high-level—specific implementation comes in the planning phase.

## Guidelines

- Avoid jargon—say "saves to the database" not "persists to the data layer"
- When presenting tech options, focus on user-facing tradeoffs
- It's OK to recommend the simpler option for MVP
- Flag decisions that are hard to change later
- Don't over-engineer—start simple, add complexity when needed

## Output

When architecture feels complete:

1. Ensure `docs/start/` directory exists
2. Save architecture summary to `docs/start/03-architect.md` with:
   - Data model (entities and relationships in plain language)
   - Authentication approach
   - External integrations (MVP vs. future)
   - Key technical decisions made
   - High-level API structure

3. Let the user know they're ready for `/04-plan` to create the implementation roadmap

## Remember

Good architecture enables the product vision without over-complicating things. The goal is a solid foundation that can evolve, not a perfect system designed upfront. When in doubt, choose simpler.
