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
@docs/01-START/01-discover.md
@docs/01-START/02-scope.md
@docs/01-START/03-architect.md

**Check what loaded above:** If discovery and scope content appear, build on them. If nothing loaded, ask the user to describe their project or suggest running earlier START commands first.

## Your Role

You do the heavy lifting on technical decisions. The user describes what they want; you figure out HOW to build it and explain the options in plain language. Make technical decisions accessible—the user doesn't need to understand HOW things work technically, just WHAT choices mean for their product.

**CRITICAL: You orchestrate specialized agents while having parallel conversations.** Don't do complex technical research yourself—delegate to specialists while you gather context from the user.

**CRITICAL: Use the sequential-thinking MCP server** for any complex reasoning, technical tradeoff analysis, or architectural decisions. This ensures systematic, thorough thinking. Ultrathink through technical choices before presenting conclusions.

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

### 2. Project Structure Decision (REQUIRED)

Before diving into technical details, determine how the codebase will be organized.

**Use AskUserQuestion:**
```
Question: "How do you want to organize your codebase?

Based on your project scope, I'd recommend [X] because [reason — consider team size, deployment needs, complexity]."
Options:
- Monorepo — frontend and backend together (recommended for small teams)
- Separate repos — frontend and backend in different repositories
- Frontend only — using a backend-as-a-service (Supabase, Firebase, Xano, etc.)
- I'm not sure — help me decide
```

**Recommendation logic:**
- **Monorepo**: Best for solo developers, small teams, or when frontend and backend share types/contracts. Simpler deployment, easier code sharing.
- **Separate repos**: Better for larger teams, different deployment cycles, or when frontend/backend use very different tech stacks.
- **Frontend only + BaaS**: Great for MVPs, reduces backend complexity, lets you focus on user experience.

### 3. Frontend Approach & Design Status (REQUIRED)

Understanding the frontend approach ensures architecture supports it properly.

**Use AskUserQuestion:**
```
Question: "How are you planning to build the frontend?"
Options:
- Traditional coded frontend (React, Vue, Next.js, etc.)
- Nocode/low-code platform (Lovable, v0, Webflow, Framer, etc.)
- AI-generated UI that I'll customize
- Hybrid — nocode prototype, then coded version
- No frontend — this is an API/backend-only project
```

**Follow up on design status:**
```
Question: "What's the current status of your UI/UX design?"
Options:
- Complete — ready to build from (Figma, Sketch, mockups, etc.)
- In progress — still being refined
- Not started — will design after architecture
- No formal design — building/designing as I go
```

**Workflow implications based on answers:**

**For nocode/AI platforms (Lovable, v0, etc.):**
- Architecture focuses on API design and data contracts
- The platform handles frontend architecture decisions
- Ensure backend APIs are well-documented for integration

**For coded frontend with design ready:**
- Can proceed with full frontend architecture (components, state, styling)
- Note design tool for BUILD phase reference

**For coded frontend with design in progress or not started:**
```
Question: "Design decisions often affect frontend architecture. I'd recommend:

1. **Proceed with backend architecture now** — frontend architecture when design is ready
2. **Pause and finalize design first** — then do full architecture together
3. **Continue with full architecture** — accept some frontend decisions may change

What works best for your timeline?"
Options:
- Backend now, frontend architecture later (recommended)
- Pause for design
- Continue with everything
```

**For API-only projects:**
- Skip frontend architecture entirely
- Focus on API design, documentation, and contracts

**What this captures for the roadmap:**
- Whether frontend development is in scope
- When frontend work should be sequenced
- What backend needs to expose for frontend integration

### 4. Data Model Design (REQUIRED - Synchronous)

**You MUST use the Task tool to launch the data-modeler agent.** The data model is foundational—other decisions depend on it, so this runs synchronously (NOT in background).

```
Task tool:
  subagent_type: "claude-vibes:CODING:data-modeler"
  prompt: "Ultrathink about the complete data model for this project. Read docs/01-START/01-discover.md and docs/01-START/02-scope.md for full context.

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

### 5. Technical Research (BACKGROUND) + User Discussion (PARALLEL)

**Launch tech-advisor in background to research technical options:**

```
Task tool:
  subagent_type: "claude-vibes:CODING:tech-advisor"
  run_in_background: true
  prompt: "Ultrathink about technical decisions for this project. Read all docs/01-START/ files for context.

  Research and recommend solutions for:
  1. Authentication approach (what makes sense for this user base)
  2. Data storage patterns (based on the data model and scale expectations)
  3. External integrations identified in scope (best practices, common patterns)
  4. Real-time requirements (if any features need instant updates)
  5. Frontend stack (if coded frontend is planned):
     - Framework recommendation based on project needs
     - Component library options
     - State management approach
     - Styling strategy

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

### 6. User & Authentication (while agent researches)

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

### 7. External Integrations (while agent researches)

Identify what outside services the app needs:
- Payments (taking money from users)
- Email/notifications (sending messages to users)
- File storage (letting users upload things)
- Other services the features depend on

Use AskUserQuestion to prioritize:
- "Which of these are must-haves for launch?"
- "Which can wait until you have users?"

### 8. Retrieve Research Results

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

### 9. Key Technical Decisions

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

### 10. Frontend Architecture (if applicable)

**Skip this section if:**
- The user chose "No frontend" or "API-only project" in section 3
- The user chose nocode/AI platform (Lovable, v0, etc.) — those platforms handle frontend architecture
- Design is not ready and user chose to defer frontend architecture

**For coded frontends with design ready, cover these decisions:**

**Component Architecture:**
```
Question: "For your UI components, what approach do you prefer?"
Options:
- Use a component library (shadcn/ui, Radix, MUI, Chakra)
- Build custom components from scratch
- Start with a library, customize as needed (recommended)
- I'm not sure — what do you recommend?
```

**State Management:**
```
Question: "How should your app manage shared data across screens?"
Options:
- Keep it simple — use built-in state (React Context, Vue reactivity)
- Use a state library (Redux, Zustand, Pinia) for complex state
- Server-first — fetch fresh data each time (React Query, SWR)
- I'm not sure — what fits my app?
```

**Styling Approach:**
```
Question: "How do you want to style your app?"
Options:
- Tailwind CSS (utility classes, fast development)
- CSS Modules (scoped styles, traditional CSS)
- Styled-components or CSS-in-JS
- Whatever the component library uses
```

**Rendering Strategy (for Next.js, Nuxt, etc.):**
```
Question: "How should pages load? (This affects speed and SEO)"
Options:
- Server-rendered (SSR) — fresh data, good for SEO
- Static (SSG) — fastest, but content doesn't change often
- Client-rendered (CSR) — simpler, but slower initial load
- Hybrid — different pages use different approaches (recommended)
```

**Note these decisions for the roadmap.** Frontend architecture can be revisited during BUILD phase if design evolves.

### 11. App Capabilities

Based on the data model and features, summarize what the app can do:
- What actions can users take?
- What information can they see?
- How do different parts of the app connect?

This becomes the blueprint for the build phase.

### 12. Architecture Review (REQUIRED)

**Launch plan-reviewer to validate the architecture:**

```
Task tool:
  subagent_type: "claude-vibes:CODING:plan-reviewer"
  prompt: "Ultrathink about this architecture design. Read all docs/01-START/ files for context.

  **Use the sequential-thinking MCP server** to systematically analyze each review area. This ensures thorough, structured reasoning.

  Review for:
  1. Missing entities or relationships in the data model
  2. Auth approach coverage for all user types and scenarios
  3. Integration alignment with MVP scope
  4. Scalability concerns for the identified use cases
  5. Decisions that are hard to change later
  6. Gaps between scope features and technical capabilities
  7. Frontend architecture completeness (if applicable):
     - Are frontend decisions documented or appropriately deferred?
     - Does the API design support the planned frontend approach?
     - Is design integration workflow clear for BUILD phase?

  **Use AskUserQuestion throughout:**
  - If something is missing, ask how the user wants to handle it
  - If there are tradeoffs, present options and ask
  - If you find risks, explain in plain language and ask about priorities
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

1. Ensure `docs/01-START/` directory exists

2. Save architecture summary to `docs/01-START/03-architect.md` with:

   **Technical Summary** (2-3 sentences in plain language)

   **Project Structure:**
   - Codebase organization (monorepo, separate repos, frontend-only)
   - Rationale for the choice

   **Frontend Approach & Design Status:**
   - Frontend approach (coded, nocode, AI-generated, hybrid, none)
   - Design status and tool (if applicable)
   - When frontend architecture will be finalized (if deferred)

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

   **Frontend Architecture** (if applicable):
   - Component approach (library, custom, hybrid)
   - State management strategy
   - Styling approach
   - Rendering strategy (SSR, SSG, CSR, hybrid)
   - Or note: "Deferred until design is ready" / "Handled by nocode platform"

   **Risks & Unknowns:**
   - Technical uncertainties
   - Integration dependencies
   - Scaling concerns

3. Tell the user they're ready for `/04-plan-roadmap` to create the implementation roadmap
