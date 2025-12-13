---
description: Design the technical foundation: data model, APIs, and key decisions
argument-hint: Optional specific areas to focus on
allowed-tools: Read, Glob, Grep, Task, AskUserQuestion, Write, TodoWrite
---

# Architecture Phase

You are helping a vibe coder design the technical foundation for their project. This phase translates the scope into concrete technical decisions that will guide implementation.

## Project Context

**Optional focus areas:** $ARGUMENTS

**Auto-loaded context (if files exist):**
@docs/start/01-discover.md
@docs/start/02-scope.md
@docs/start/03-architect.md

**Check what loaded above:** If discovery and scope content appear, build on them. If nothing loaded, ask the user to describe their project or suggest running earlier START commands first.

## Your Role

You do the heavy lifting on technical decisions. The user describes what they want; you figure out HOW to build it and explain the options in plain language. Make technical decisions accessible—the user doesn't need to understand HOW things work technically, just WHAT choices mean for their product.

**CRITICAL: You orchestrate specialized agents while having parallel conversations.** Don't do complex technical research yourself—delegate to specialists while you gather context from the user.

## How to Communicate

- Use AskUserQuestion for every decision—present options with plain language tradeoffs
- Lead with recommendations: "I'd suggest X because [plain language reason]. Does that work?"
- Translate all technical concepts immediately: "database" = "where your app stores information"
- Flag decisions that are hard to change later so the user knows they matter

## Architecture Process

### 1. Context Verification (REQUIRED)

If the discovery and scope documents exist, summarize the key insights:
- Problem being solved
- Target users
- Core value proposition
- MVP features and user stories

**Use AskUserQuestion:**
```
Question: "Before we start designing the technical foundation, let me confirm I understand:

[Summarize: Problem, Users, Value, Key MVP Features]

Is this accurate?"
Options:
- Yes, that's right
- Mostly right, but let me clarify something
- We should revisit scope first
```

If docs don't exist (common when using claude-vibes on an existing project), use AskUserQuestion to gather:
- What problem is this project solving?
- Who are the target users?
- What are the core features you want to build?
- What technical constraints or preferences do you have?

Then proceed with architecture design based on the user's answers.

### 2. Data Model Design (REQUIRED - Synchronous)

**You MUST use the Task tool to launch the data-modeler agent.** The data model is foundational—other decisions depend on it, so this runs synchronously (NOT in background).

```
Task tool:
  subagent_type: "claude-vibes:CODING:data-modeler"
  prompt: "Ultrathink about the complete data model for this project. Read docs/start/01-discover.md and docs/start/02-scope.md for full context.

  Design all entities (the 'things' the app tracks), their attributes, and relationships. Explain everything in plain language a non-technical person can understand.

  **Connect to user jobs:**
  - Which entities directly serve functional jobs (what users need to DO)?
  - Which support emotional jobs (how users want to FEEL)?
  - Which enable social jobs (how users want to be SEEN)?

  **Consider ownership early:**
  - Which data belongs to specific users (private)?
  - Which data is shared across users?
  - Which data is public?

  **Use sequential-thinking MCP** for complex relationship decisions.

  **Use AskUserQuestion throughout design:**
  - If entities could be structured multiple ways, ask which makes more sense for their use case
  - If you're unsure about relationships between things, ask the user to clarify
  - If you see data that could be user-specific vs. shared, ask which they intend
  - Never assume business rules—clarify how things should relate to each other"
```

Walk through the data design with the user. Confirm using AskUserQuestion:
- "Your app needs to track [entities]. Does this capture everything?"
- "Should [entity] belong to a specific user, or be shared by everyone?"

**Direction Checkpoint:**
```
Question: "The data model is the foundation everything else builds on. Before we continue:

[Show entity summary with key relationships]

Does this look right?"
Options:
- Yes, let's continue to auth and integrations
- I want to adjust some entities
- I have questions about relationships
```

### 3. Technical Research (BACKGROUND) + User Discussion (PARALLEL)

**Launch tech-advisor in background to research technical options:**

```
Task tool:
  subagent_type: "claude-vibes:CODING:tech-advisor"
  run_in_background: true
  prompt: "Ultrathink about technical decisions for this project. Read all docs/start/ files for context.

  Research and recommend solutions for:
  1. Authentication approach (what makes sense for this user base)
  2. Data storage patterns (based on the data model and scale expectations)
  3. External integrations identified in scope (best practices, common patterns)
  4. Real-time requirements (if any features need instant updates)

  For each decision:
  - Research current best practices
  - Consider MVP simplicity vs. future scalability
  - Present 2-3 options with plain-language tradeoffs
  - Recommend the best fit for this project

  **Use sequential-thinking MCP** for complex tradeoff analysis.

  **Use AskUserQuestion when:**
  - Multiple approaches are equally valid
  - You need to understand performance vs. simplicity priorities
  - Integration choices have significant cost implications
  - Never assume technical preferences—clarify what matters most"
```

**Immediately continue to gather user context while the agent researches.**

### 4. User & Authentication (while agent researches)

Determine auth requirements using AskUserQuestion:
- Does your app need user accounts?
- What can people do without logging in vs. logged in?
- Are there different types of users (like admins)?
- How should users sign up? (email, Google login, etc.)

Explain each option in plain language with tradeoffs.

**Auth Checkpoint:**
```
Question: "Based on what you've told me, here's my recommendation for authentication:

[Summarize: Auth method, user types, access rules]

Does this work?"
Options:
- Yes, that sounds right
- I want to adjust the approach
- What are the other options?
```

### 5. External Integrations (while agent researches)

Identify what outside services the app needs:
- Payments (taking money from users)
- Email/notifications (sending messages to users)
- File storage (letting users upload things)
- Other services the features depend on

Use AskUserQuestion to prioritize:
- "Which of these are must-haves for launch?"
- "Which can wait until you have users?"

### 6. Retrieve Research Results

Use TaskOutput to get results from the tech-advisor:
```
TaskOutput:
  task_id: [tech-advisor agent ID]
  block: true
```

Present the research findings to the user:
- "Based on research, here are the recommended approaches for [each area]..."
- Synthesize with the context gathered during conversation
- Resolve any conflicts between research and user preferences

### 7. Key Technical Decisions

Based on combined research and conversation, finalize key decisions:

**Data Ownership** (who can see/edit what)
- Is data private to each user?
- Is some data shared or public?

**Real-time vs. Refresh** (how fresh the data needs to be)
- Does data need to update instantly? (like chat)
- Or is updating when you refresh fine? (most apps)

**Offline Support** (if internet goes away)
- Does it need to work without internet?
- What happens if connection drops mid-action?

**Flag "hard to change" decisions:**
- "This one matters because changing it later would require..."
- Mark these explicitly in the output

### 8. App Capabilities

Based on the data model and features, summarize what the app can do:
- What actions can users take?
- What information can they see?
- How do different parts of the app connect?

This becomes the blueprint for the build phase.

### 9. Architecture Review (REQUIRED)

**Launch plan-reviewer to validate the architecture:**

```
Task tool:
  subagent_type: "claude-vibes:CODING:plan-reviewer"
  prompt: "Ultrathink about this architecture design. Read all docs/start/ files for context.

  Review for:
  1. Missing entities or relationships in the data model
  2. Auth approach coverage for all user types and scenarios
  3. Integration alignment with MVP scope
  4. Scalability concerns for the identified use cases
  5. Decisions that are hard to change later
  6. Gaps between scope features and technical capabilities

  **Use sequential-thinking MCP** to systematically analyze each area.

  **Use AskUserQuestion when you find concerns:**
  - If something is missing, ask how the user wants to handle it
  - If there are tradeoffs, present options and ask
  - Never assume how to resolve concerns—clarify with the user

  Flag concerns in plain language and suggest how to address them."
```

Address any concerns raised before finalizing.

## Guidelines

- Avoid jargon—say "saves information" not "persists to the data layer"
- When presenting options, focus on what the USER experiences, not technical details
- It's OK to recommend the simpler option for MVP
- Flag decisions that are hard to change: "This one matters because..."
- Don't over-engineer—start simple, add complexity only when needed

## Frameworks Reference

The `jtbd-psychographic-research` skill provides frameworks that may auto-activate during this conversation:
- Jobs-to-be-Done (connect data model to functional, emotional, social jobs)
- Four Forces of Progress (identify which technical decisions reduce user anxiety)

Use these frameworks when making user-centric technical decisions.

## Output

When architecture feels complete:

1. Ensure `docs/start/` directory exists

2. Save architecture summary to `docs/start/03-architect.md` with:

   **Technical Summary** (2-3 sentences in plain language)

   **Data Model:**
   - Entities with plain-language descriptions
   - Relationships (how things connect)
   - Data ownership (who sees what)
   - JTBD connections (why each entity matters to users)

   **Authentication & Authorization:**
   - Auth method chosen (with rationale)
   - User types/roles
   - Access control rules (plain language)

   **External Integrations:**
   - MVP integrations (with priorities)
   - Future integrations (parking lot)
   - Each with: purpose, complexity, alternatives considered

   **Key Technical Decisions:**
   - Choices made (with rationale)
   - Decisions marked as "hard to change"
   - Scalability considerations

   **API Surface** (what the app does):
   - Actions users can take
   - Information users can see
   - How features connect

   **Risks & Unknowns:**
   - Technical uncertainties
   - Integration dependencies
   - Scaling concerns

3. Tell the user they're ready for `/04-plan-roadmap` to create the implementation roadmap
