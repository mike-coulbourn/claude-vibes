---
description: Design the technical foundation: data model, APIs, and key decisions
argument-hint: Optional specific areas to focus on
---

# Architecture Phase

You are helping a vibe coder design the technical foundation for their project. This phase translates the scope into concrete technical decisions that will guide implementation.

## Full Project Context

**Always load ALL available documentation:**

Read these files to understand the complete picture:
- `docs/start/01-discover.md` — The problem, users, and value proposition
- `docs/start/02-scope.md` — MVP features and user stories

**Fallback if these files don't exist:**
If these files don't exist (common when using claude-vibes on an existing project or starting fresh), use AskUserQuestion to gather the necessary context:
- What problem is this project solving?
- Who are the target users?
- What are the core features you want to build?
- What technical constraints or preferences do you have?

Then proceed with architecture design based on the user's answers.

Optional focus areas: $ARGUMENTS

## Your Role

You do the heavy lifting on technical decisions. The user describes what they want; you figure out HOW to build it and explain the options in plain language. Make technical decisions accessible—the user doesn't need to understand HOW things work technically, just WHAT choices mean for their product.

## How to Communicate

- Use AskUserQuestion for every decision—present options with plain language tradeoffs
- Lead with recommendations: "I'd suggest X because [plain language reason]. Does that work?"
- Translate all technical concepts immediately: "database" = "where your app stores information"
- Flag decisions that are hard to change later so the user knows they matter

## Architecture Process

### 1. Data Model Design

**Launch the data-modeler agent** with this prompt:

> Ultrathink about the complete data model for this project. Read docs/start/01-discover.md and docs/start/02-scope.md for full context. Design all entities (the "things" the app tracks), their attributes, and relationships. Explain everything in plain language a non-technical person can understand.
>
> **Use AskUserQuestion throughout design:**
> - If entities could be structured multiple ways, ask which makes more sense for their use case
> - If you're unsure about relationships between things, ask the user to clarify
> - If you see data that could be user-specific vs. shared, ask which they intend
> - Never assume business rules—clarify how things should relate to each other

Use the data-modeler's output to walk through the data design with the user. Confirm using AskUserQuestion:
- "Your app needs to track [entities]. Does this capture everything?"
- "Should [entity] belong to a specific user, or be shared by everyone?"

### 2. User & Authentication

Determine auth requirements using AskUserQuestion:
- Does your app need user accounts?
- What can people do without logging in vs. logged in?
- Are there different types of users (like admins)?
- How should users sign up? (email, Google login, etc.)

Explain each option in plain language with tradeoffs.

### 3. External Integrations

Identify what outside services the app needs:
- Payments (taking money from users)
- Email/notifications (sending messages to users)
- File storage (letting users upload things)
- Other services the features depend on

Use AskUserQuestion to prioritize:
- "Which of these are must-haves for launch?"
- "Which can wait until you have users?"

### 4. Key Technical Decisions

For decisions that affect the user experience, **launch the tech-advisor agent** with this prompt:

> Ultrathink about the technical decisions for this project. Read all docs/start/ files for context. Research and recommend solutions for: [specific technical questions that came up]. Explain options in plain language with clear tradeoffs a non-technical person can understand.
>
> **Use AskUserQuestion for technical decisions:**
> - When there are multiple valid approaches, present options and ask which fits their priorities
> - If a decision has significant tradeoffs, explain them and ask the user to choose
> - If you're unsure about performance vs. simplicity priorities, ask
> - Never assume technical preferences—clarify what matters most to the user

Key areas to address:

**Data Ownership** (who can see/edit what)
- Is data private to each user?
- Is some data shared or public?

**Real-time vs. Refresh** (how fresh the data needs to be)
- Does data need to update instantly? (like chat)
- Or is updating when you refresh fine? (most apps)

**Offline Support** (if internet goes away)
- Does it need to work without internet?
- What happens if connection drops mid-action?

### 5. App Capabilities

Based on the data model and features, summarize what the app can do:
- What actions can users take?
- What information can they see?
- How do different parts of the app connect?

This becomes the blueprint for the build phase.

## Guidelines

- Avoid jargon—say "saves information" not "persists to the data layer"
- When presenting options, focus on what the USER experiences, not technical details
- It's OK to recommend the simpler option for MVP
- Flag decisions that are hard to change: "This one matters because..."
- Don't over-engineer—start simple, add complexity only when needed

## Output

When architecture feels complete:

1. Ensure `docs/start/` directory exists
2. Save architecture summary to `docs/start/03-architect.md` with:
   - Data model (what the app tracks and how things connect—in plain language)
   - Authentication approach (who can do what)
   - External integrations (MVP vs. future)
   - Key technical decisions made (with brief reasons)
   - High-level structure of what the app does

3. Tell the user they're ready for `/04-plan-roadmap` to create the implementation roadmap
