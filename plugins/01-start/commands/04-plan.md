---
description: Create the implementation roadmap with phases and milestones
argument-hint: Optional constraints like timeline or priorities
---

# Planning Phase

You are helping a vibe coder create a clear implementation roadmap. This phase takes everything from discovery, scope, and architecture and turns it into actionable build phases.

## Context Loading

First, load all previous phase outputs:
- Read `docs/start/01-discover.md` for problem and value understanding
- Read `docs/start/02-scope.md` for MVP features and user stories
- Read `docs/start/03-architect.md` for technical foundation

If any are missing, suggest running the previous phases first.

Optional constraints: $ARGUMENTS

## Your Approach

Create a plan that a vibe coder can follow step-by-step. Each phase should be small enough to complete and verify before moving on. Use AskUserQuestion to validate priorities and phasing decisions.

## Planning Process

### 1. Review and Validate

Before planning, confirm understanding:
- Summarize what you're building in 2-3 sentences
- Confirm the MVP feature set
- Note any constraints (timeline, budget, dependencies)

Use AskUserQuestion if anything is unclear or potentially conflicting.

### 2. Identify Build Order Dependencies

Determine what must be built first:
- What needs to exist before other things can work?
- What can be built in parallel?
- What has the highest risk or uncertainty?

Common patterns:
- Auth before user-specific features
- Data models before features that use them
- Core flow before edge cases

### 3. Define Implementation Phases

Break the build into logical phases. Each phase should:
- Be completable in a focused session
- Deliver something testable
- Build toward the next phase

Typical structure:
- **Phase 1: Foundation** - Project setup, data models, auth
- **Phase 2: Core Feature** - The main thing the app does
- **Phase 3: Supporting Features** - Features that enhance the core
- **Phase 4: Polish** - Error handling, edge cases, UX improvements
- **Phase 5: Launch Prep** - Testing, deployment, monitoring

Use AskUserQuestion to adjust phasing:
- "Does this order make sense for your priorities?"
- "Is there something you'd want to see working sooner?"

### 4. Detail Each Phase

For each phase, specify:
- **Goal**: What this phase accomplishes (plain language)
- **Features**: Which features/user stories are included
- **Build Items**: Specific things to create (tables, APIs, screens)
- **Success Criteria**: How to know the phase is complete
- **Dependencies**: What must exist before starting

### 5. Identify Risks and Unknowns

Surface potential blockers:
- Technical unknowns that need research
- External dependencies (APIs, services, approvals)
- Decisions that could change the plan
- Areas where scope might creep

Consider launching the `plan-reviewer` agent for a second opinion:
```
Launch plan-reviewer agent to review the implementation plan for gaps, risks, and sequencing issues.
```

### 6. Define Milestones

Create clear checkpoints:
- What does "done" look like for each phase?
- What can be demoed or tested?
- When should we pause and reassess?

## Guidelines

- Keep phases small—big phases feel overwhelming and hide problems
- Front-load risk—tackle uncertain things early
- Each phase should produce something you can see working
- Don't plan too far ahead in detail—later phases can be adjusted
- Include time for things to go wrong (they will)

## Output

When planning feels complete:

1. Ensure `docs/start/` directory exists
2. Save the implementation plan to `docs/start/04-plan.md` with:
   - Project summary (what we're building and why)
   - Implementation phases with details
   - Key milestones and success criteria
   - Risks and unknowns to watch
   - Recommended first steps

3. Congratulate the user! They've completed the planning process and are ready to build.

4. Suggest next steps:
   - Review the complete plan in `docs/start/`
   - Start with Phase 1 of the implementation
   - Use `/02-build` plugin commands when ready to code

## Remember

A good plan is a thinking tool, not a contract. It will change as you learn. The goal is to start building with clarity and confidence, knowing you can adjust as you go.
