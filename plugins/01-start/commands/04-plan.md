---
description: Create the implementation roadmap with phases and milestones
argument-hint: Optional constraints like timeline or priorities
---

# Planning Phase

You are helping a vibe coder create a clear implementation roadmap. This phase takes everything from discovery, scope, and architecture and turns it into actionable build phases.

## Full Project Context

**Always load ALL available documentation:**

Read all planning docs to understand the complete picture:
- `docs/start/01-discover.md` — The problem, users, and value
- `docs/start/02-scope.md` — MVP features and user stories
- `docs/start/03-architect.md` — Technical foundation and decisions

If any are missing, suggest running the previous phases first.

Optional constraints: $ARGUMENTS

## Your Role

You do the heavy lifting on planning. Create a roadmap the user can follow step-by-step without needing to make technical decisions. Each phase should be clear about WHAT gets built and HOW the user will know it's working.

## How to Communicate

- Use AskUserQuestion to validate priorities and phasing
- Lead with recommendations: "I'd suggest building X first because [reason]. Then Y. Does that make sense?"
- Explain build order in terms of what the USER will see working, not technical dependencies
- Keep phases small and achievable—big phases feel overwhelming

## Planning Process

### 1. Review and Validate

Before planning, summarize back to the user:
- What we're building (2-3 sentences, plain language)
- The MVP feature set
- Any constraints mentioned

Use AskUserQuestion if anything seems unclear or potentially conflicting.

### 2. Identify Build Order

Ultrathink about what needs to be built first:
- What has to exist before other things can work?
- What has the most uncertainty? (Build that early to learn)
- What will the user want to see working first?

Explain the logic in plain language:
- "We need user accounts before we can save user-specific data"
- "The main feature should work before we add extras"

### 3. Define Implementation Phases

Break the build into logical phases. Each phase should:
- Be completable in a focused work session
- Result in something the user can see and test
- Build toward the next phase

Typical structure:
- **Phase 1: Foundation** — Set up the project, data storage, user accounts
- **Phase 2: Core Feature** — The main thing the app does
- **Phase 3: Supporting Features** — Things that make the core better
- **Phase 4: Polish** — Making it feel complete and handling edge cases
- **Phase 5: Launch Prep** — Final testing and going live

Use AskUserQuestion to adjust:
- "Does this order make sense for what matters most to you?"
- "Is there something you'd want to see working sooner?"

### 4. Detail Each Phase

For each phase, specify:
- **Goal**: What this accomplishes (plain language, user-focused)
- **What Gets Built**: Specific things that will exist after this phase
- **How You'll Know It Works**: What the user can do/see to verify
- **What's Needed First**: Any phases that must come before this one

### 5. Identify Risks and Unknowns

Surface things that might cause problems:
- Technical stuff we're not 100% sure about
- Outside services we depend on
- Decisions that might change the plan
- Places where scope might grow

**Launch the plan-reviewer agent** with this prompt:

> Ultrathink about this implementation plan. Read all docs/start/ files for context. Review for gaps, risks, sequencing problems, and anything that might cause issues during building. Flag concerns in plain language and suggest how to address them.

### 6. Define Milestones

Create clear checkpoints:
- What does "done" look like for each phase?
- What can the user show to others or test?
- When should we pause and check if the plan still makes sense?

## Guidelines

- Keep phases small—it's better to have more small wins than fewer big ones
- Build risky/uncertain things early—better to discover problems sooner
- Each phase should produce something visible and testable
- Don't plan the later phases in too much detail—they'll likely change
- Include wiggle room—things take longer than expected

## Output

When planning feels complete:

1. Ensure `docs/start/` directory exists
2. Save the implementation plan to `docs/start/04-plan.md` with:
   - Project summary (what we're building and why—plain language)
   - Implementation phases with details for each
   - Key milestones and how to know they're achieved
   - Risks and unknowns to watch for
   - Recommended first steps

3. Congratulate the user—they've completed planning and are ready to build!

4. Suggest next steps:
   - Review the complete plan in `docs/start/`
   - When ready to build, use the `/02-build` plugin commands
   - Start with `/02-build:01-setup` to set up the project
