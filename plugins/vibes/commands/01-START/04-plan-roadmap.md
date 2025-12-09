---
description: Create the implementation roadmap with phases and milestones
argument-hint: Optional constraints like timeline or priorities
---

# Planning Phase

You are helping a vibe coder create a clear implementation roadmap. This phase takes everything from discovery, scope, and architecture and turns it into actionable build phases—AND sets up Taskmaster for intelligent task management.

## Full Project Context

**Always load ALL available documentation:**

Read all planning docs to understand the complete picture:
- `docs/start/01-discover.md` — The problem, users, and value
- `docs/start/02-scope.md` — MVP features and user stories
- `docs/start/03-architect.md` — Technical foundation and decisions

**Fallback if these files don't exist:**
If these files don't exist (common when using claude-vibes on an existing project), use AskUserQuestion to gather the necessary context:
- What is the project about and who are the users?
- What features need to be built (MVP scope)?
- What technical decisions have already been made?

Then proceed with roadmap planning based on the user's answers.

Optional constraints: $ARGUMENTS

## Your Role

You do the heavy lifting on planning. Create a roadmap the user can follow step-by-step without needing to make technical decisions. Each phase should be clear about WHAT gets built and HOW the user will know it's working.

**CRITICAL: You MUST use the Task tool to launch the plan-reviewer agent for reviewing the plan.** Do not skip the plan review—that's what the plan-reviewer agent is for.

## How to Communicate

- **Use AskUserQuestion for EVERY decision** — always provide 2-4 clear options
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

**Use AskUserQuestion to validate phasing:**
```
Question: "Here's the build order I'd recommend. Does this work for you?"
Options:
- Yes, this order makes sense
- I'd like to adjust the priority of some phases
- I have questions about specific phases
- Other
```

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

**You MUST use the Task tool to launch the plan-reviewer agent.** Use `subagent_type: "claude-vibes:plan-reviewer"` with this prompt:

> Ultrathink about this implementation plan. Read all docs/start/ files for context. Review for gaps, risks, sequencing problems, and anything that might cause issues during building. Flag concerns in plain language and suggest how to address them.
>
> **Use the sequential-thinking MCP tool** to systematically analyze:
> 1. Each phase's dependencies and prerequisites — are they correctly ordered?
> 2. Technical risks and unknowns — what could go wrong?
> 3. Scope creep potential — where might requirements expand?
> 4. Integration points between phases — are handoffs clear?
> 5. Resource and timeline realism — is this achievable?
>
> **Use AskUserQuestion when reviewing:**
> - If you find gaps that could be filled multiple ways, ask which approach fits their goals
> - If risks could be mitigated differently, present options and ask
> - If sequencing could go multiple directions, ask about priorities
> - Never assume how to resolve concerns—clarify with the user

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

### Step 1: Save Human-Readable Roadmap

1. Ensure `docs/start/` directory exists
2. Save the implementation plan to `docs/start/04-plan-roadmap.md` with:
   - Project summary (what we're building and why—plain language)
   - Implementation phases with details for each
   - Key milestones and how to know they're achieved
   - Risks and unknowns to watch for
   - Recommended first steps

### Step 2: Ask About Taskmaster Setup

**Use AskUserQuestion to confirm Taskmaster setup:**

```
Question: "I can set up Taskmaster to track your tasks and dependencies automatically. This will help you know exactly what to build next. Want me to set it up?"
Options:
- Yes, set up Taskmaster (recommended)
- No, I'll manage tasks manually
- What's Taskmaster? Tell me more first
```

**If they want more info:**
Explain briefly: "Taskmaster is a task management system that:
- Breaks your roadmap into trackable tasks
- Knows what to build next based on dependencies
- Tracks your progress across the whole project
- Handles changes when plans evolve mid-build

The `/02-BUILD` commands will use it automatically—you don't need to learn any new commands."

Then ask again if they want to set it up.

**If they decline:** Skip to Step 5 (congratulate without Taskmaster).

**If they accept:** Continue to Step 3.

### Step 3: Generate Taskmaster PRD

Create a PRD (Product Requirements Document) by synthesizing all `docs/start/` files into Taskmaster format.

**Save to `.taskmaster/docs/prd.txt`:**

```
# [Project Name]

## Project Overview
[From 01-discover.md: Problem statement, target users, value proposition]

## Target Users
[From 01-discover.md: User personas and their needs]

## Core Features

### Feature 1: [Name]
[From 02-scope.md: MVP features with user stories]
- User Story: As a [user], I want to [action] so that [benefit]
- Acceptance Criteria:
  - [ ] [Specific, testable criteria]
  - [ ] [More criteria]

### Feature 2: [Name]
[Continue for each MVP feature]

## Technical Requirements
[From 03-architect.md: Data model, auth approach, integrations, key decisions]

## Implementation Phases
[From the roadmap you just created: phases with dependencies]

### Phase 1: [Name]
- Dependencies: None
- Tasks:
  - [Specific task 1]
  - [Specific task 2]

### Phase 2: [Name]
- Dependencies: Phase 1
- Tasks:
  - [Specific task 1]
  - [Specific task 2]

[Continue for each phase]

## Success Criteria
[From 01-discover.md: How we know this is working]

## Out of Scope
[From 02-scope.md: Explicitly excluded items]
```

### Step 4: Initialize Taskmaster

**Use the Taskmaster MCP tools to set up task management:**

1. **Initialize Taskmaster** (if not already initialized):
   - Check if `.taskmaster/` directory exists
   - If not, use the `initialize_project` Taskmaster tool

2. **Parse the PRD into tasks:**
   - Use the `parse_prd` Taskmaster tool with the PRD file path
   - This creates `.taskmaster/tasks/tasks.json` with structured tasks and dependencies

3. **Show task overview and confirm:**
   - Use the `get_tasks` Taskmaster tool to retrieve all tasks
   - Present a summary of what was created

**Use AskUserQuestion to review the tasks:**

```
Question: "Taskmaster created [X] tasks from your roadmap. Here's a quick overview:

[Show first 3-5 tasks with their dependencies]

Does this breakdown look right?"
Options:
- Yes, looks good
- I'd like to see all the tasks first
- Some tasks need adjustment
- Other
```

**If they want to see all tasks:** Display the full task list, then ask again.

**If tasks need adjustment:** Use AskUserQuestion to understand what to change, then use Taskmaster tools to update.

### Step 5: Analyze Task Complexity

After tasks are created, run complexity analysis to identify which tasks may need breakdown.

1. **Run complexity analysis:**
   - Use Taskmaster's `analyze_project_complexity` tool
   - This evaluates each task and provides:
     - Complexity score (1-10)
     - Recommended number of subtasks
     - Reasoning for complex tasks

2. **Show complexity overview:**

**Use AskUserQuestion:**
```
Question: "I've analyzed the complexity of your tasks:

**Simple tasks (can implement directly):**
- Task 1: [name] — complexity 3/10
- Task 4: [name] — complexity 2/10

**Complex tasks (recommend breaking into subtasks):**
- Task 2: [name] — complexity 7/10, recommends 3 subtasks
- Task 5: [name] — complexity 8/10, recommends 4 subtasks

You can expand complex tasks now, or wait until you plan each one (recommended).

What would you like to do?"
Options:
- Expand later during planning (recommended)
- Expand all complex tasks now
- Show me the complexity details
- Other
```

**If they choose "Expand later" (recommended):**
Proceed to Step 6. The `/01-plan-code` command will handle expansion when you're about to work on each task — this gives better results because it can use codebase context.

**If they choose "Expand all now":**

Use Taskmaster's `expand_task` tool for each complex task (those with recommended subtasks > 0).

**Use AskUserQuestion after expansion:**
```
Question: "Expanded [X] complex tasks into subtasks:

- Task 2 → 3 subtasks created
- Task 5 → 4 subtasks created

Total tasks: [original count] → [new count with subtasks]

Does this look right?"
Options:
- Yes, looks good
- Show me the subtasks
- Some need adjustment
- Other
```

**If they want complexity details:** Show the full complexity report with reasoning for each task, then ask again.

3. **Show the recommended first task:**

**Use AskUserQuestion:**
```
Question: "Based on dependencies, here's the recommended first task:

**[Task Name]**
[Task description]
Complexity: [X]/10

Ready to start building?"
Options:
- Yes, let's do it! (I'll run /02-BUILD:01-plan-code)
- I want to review the full plan first
- I have questions before starting
- Other
```

### Step 6: Congratulate and Guide Next Steps

**With Taskmaster:**

"Planning complete! Here's what we created:

**Human Documentation** (in `docs/start/`):
- Discovery summary
- Scope and MVP features
- Architecture decisions
- Implementation roadmap

**Task Management** (in `.taskmaster/`):
- PRD document
- [X] structured tasks with dependencies
- First task ready: [task name]

**Next steps:**
Run `/02-BUILD:01-plan-code` — Taskmaster will recommend what to build based on dependencies!"

**Without Taskmaster:**

"Planning complete! Here's what we created:

**Human Documentation** (in `docs/start/`):
- Discovery summary
- Scope and MVP features
- Architecture decisions
- Implementation roadmap

**Next steps:**
1. Review the complete plan in `docs/start/`
2. When ready to build, run `/02-BUILD:01-plan-code [feature name]`"

## Taskmaster Integration Notes

**Why Taskmaster?**
- Tracks task dependencies automatically
- Knows what to build next based on what's complete
- Handles implementation drift (when plans change mid-build)
- Maintains project-wide progress visibility

**The user doesn't need to learn Taskmaster commands.** The `/02-BUILD` commands interact with it automatically. But if they want to check status manually, they can say:
- "Show tasks" — see all tasks and status
- "What's next?" — get the next recommended task
- "Show task 5" — see details of a specific task
