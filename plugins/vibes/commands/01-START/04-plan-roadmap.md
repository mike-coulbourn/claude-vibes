---
description: Create the implementation roadmap with phases and milestones
argument-hint: Optional constraints like timeline or priorities
allowed-tools: Read, Glob, Grep, Task, AskUserQuestion, Write, TodoWrite
---

# Planning Phase

You are helping a vibe coder create a clear implementation roadmap. This phase takes everything from discovery, scope, and architecture and turns it into actionable build phases—AND sets up Taskmaster for intelligent task management.

## Full Project Context

**Optional constraints:** $ARGUMENTS

**Document status:**
- !`test -f docs/start/01-discover.md && echo "✓ Discovery document exists" || echo "✗ No discovery — ask user to describe project or suggest running /01-discover first"`
- !`test -f docs/start/02-scope.md && echo "✓ Scope document exists" || echo "✗ No scope — ask user to describe features or suggest running /02-scope first"`
- !`test -f docs/start/03-architect.md && echo "✓ Architecture document exists" || echo "✗ No architecture — ask user about technical decisions or suggest running /03-architect first"`
- !`test -f docs/start/04-plan-roadmap.md && echo "✓ Previous roadmap exists" || echo "○ No existing roadmap — fresh planning"`
- !`test -d .taskmaster/tasks && echo "✓ Taskmaster initialized" || echo "○ Taskmaster not initialized"`

Use this context to adapt your approach: if all docs exist, synthesize them; if docs are missing, gather context first; if Taskmaster is already initialized, offer to update rather than reinitialize.

**Auto-load project context:**
@docs/start/01-discover.md
@docs/start/02-scope.md
@docs/start/03-architect.md
@docs/start/04-plan-roadmap.md

## Your Role

You do the heavy lifting on planning. Create a roadmap the user can follow step-by-step without needing to make technical decisions. Each phase should be clear about WHAT gets built and HOW the user will know it's working.

**CRITICAL: You orchestrate specialized agents while having parallel conversations.** Don't validate the plan yourself—delegate to the plan-reviewer while you continue detailing phases with the user.

## How to Communicate

- Use AskUserQuestion for every decision—present options with plain language tradeoffs
- Lead with recommendations: "I'd suggest building X first because [reason]. Then Y. Does that make sense?"
- Explain build order in terms of what the USER will see working, not technical dependencies
- Keep phases small and achievable—big phases feel overwhelming

## Planning Process

### 1. Context Verification (REQUIRED)

If all planning docs exist, summarize the key insights:
- What we're building (problem and value proposition)
- Who we're building for (target users)
- MVP feature set
- Key technical decisions from architecture

**Use AskUserQuestion:**
```
Question: "Before I create your roadmap, let me confirm I understand the complete picture:

[Summarize: Problem, Users, MVP Features, Technical Foundation]

Is this accurate?"
Options:
- Yes, that's right
- Mostly right, but let me clarify something
- We should revisit earlier planning first
```

If docs don't exist (common when using claude-vibes on an existing project), use AskUserQuestion to gather:
- What is the project about and who are the users?
- What features need to be built (MVP scope)?
- What technical decisions have already been made?

Then proceed with roadmap planning based on the user's answers.

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

**Direction Checkpoint:**
```
Question: "Here's the build order I'd recommend:

[Show phases with brief descriptions]

Does this work for you?"
Options:
- Yes, this order makes sense
- I'd like to adjust the priority of some phases
- I have questions about specific phases
```

### 4. Detail Each Phase

For each phase, specify:
- **Goal**: What this accomplishes (plain language, user-focused)
- **What Gets Built**: Specific things that will exist after this phase
- **How You'll Know It Works**: What the user can do/see to verify
- **What's Needed First**: Any phases that must come before this one

### 5. Define Milestones

Create clear checkpoints:
- What does "done" look like for each phase?
- What can the user show to others or test?
- When should we pause and check if the plan still makes sense?

### 6. Plan Review (REQUIRED)

**You MUST use the Task tool to launch the plan-reviewer agent before saving:**

```
Task tool:
  subagent_type: "claude-vibes:CODING:plan-reviewer"
  prompt: "Ultrathink about this implementation roadmap. Read all docs/start/ files for complete context.

  **Use the sequential-thinking MCP tool** to systematically analyze:
  1. Phase sequencing — are dependencies correctly ordered?
  2. Scope alignment — does the roadmap match the MVP scope from 02-scope.md?
  3. Architecture compatibility — can the technical decisions from 03-architect.md support this build order?
  4. Risk identification — what could go wrong during implementation?
  5. Milestone clarity — are checkpoints testable and measurable?
  6. Estimation realism — are phases sized appropriately for focused work sessions?

  **Use AskUserQuestion when you find concerns:**
  - If phases could be reordered for better risk reduction, present options
  - If scope seems to have drifted from 02-scope.md, ask about priorities
  - If technical decisions seem incompatible with build order, flag and discuss
  - If milestones aren't measurable, suggest more concrete success criteria
  - Never assume how to resolve issues—clarify with the user

  Flag all concerns with severity (blocker vs. consideration) and suggest resolutions in plain language."
```

Address any concerns raised before proceeding to save.

### 7. Identify Risks and Unknowns

Surface things that might cause problems:
- Technical stuff we're not 100% sure about
- Outside services we depend on
- Decisions that might change the plan
- Places where scope might grow

## Guidelines

- Keep phases small—it's better to have more small wins than fewer big ones
- Build risky/uncertain things early—better to discover problems sooner
- Each phase should produce something visible and testable
- Don't plan the later phases in too much detail—they'll likely change
- Include wiggle room—things take longer than expected

## Frameworks Reference

The `jtbd-psychographic-research` skill provides frameworks that may auto-activate during this conversation:
- Jobs-to-be-Done (prioritize features that address core jobs first)
- Four Forces of Progress (reduce anxiety by building confidence-building features early)

Use these frameworks when deciding what to build first.

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

3. **Launch ai-writing-detector in background** while continuing to Taskmaster setup:

```
Task tool:
  subagent_type: "claude-vibes:TOOLKIT:ai-writing-detector"
  run_in_background: true
  prompt: "Review docs/start/04-plan-roadmap.md for AI writing patterns. Focus on:
  - Overly formal or stiff language
  - Generic phrases that could apply to any project
  - Lack of specific, concrete details

  Suggest refinements that make the document sound more natural and specific to this project."
```

### Step 2: Ask About Taskmaster Setup

**Check Taskmaster state from context injection above.**

**If Taskmaster is already initialized with tasks:**
```
Question: "Taskmaster is already set up with existing tasks. What would you like to do?"
Options:
- Update tasks from the new roadmap (regenerate)
- Keep existing tasks
- Show me the current tasks first
```

**If Taskmaster is not initialized:**
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

**If they decline:** Skip to Step 6 (congratulate without Taskmaster).

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
   - Check if `.taskmaster/` directory exists from context
   - If not, use the `initialize_project` Taskmaster tool

2. **Parse the PRD into tasks:**
   - Use the `parse_prd` Taskmaster tool with the PRD file path
   - This creates `.taskmaster/tasks/tasks.json` with structured tasks and dependencies

3. **Verify and show task overview:**
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
```

**If they choose "Expand later" (recommended):**
Proceed to Step 6. The `/02-BUILD:01-plan-code` command will handle expansion when you're about to work on each task — this gives better results because it can use codebase context.

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
```

### Step 6: Retrieve Background Results and Congratulate

**Retrieve ai-writing-detector results if available:**
```
TaskOutput:
  task_id: [ai-writing-detector agent ID]
  block: false
```

If the agent found issues, mention them briefly: "The document review suggested some refinements to make the language more natural. I can apply those now or you can review docs/start/04-plan-roadmap.md later."

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
2. When ready to build, run `/02-BUILD:01-plan-code [feature name]`

You can run `/04-plan-roadmap` again later if you want to set up Taskmaster."

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
