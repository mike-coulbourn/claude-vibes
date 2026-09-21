---
description: Strategic business growth consultation with prioritized opportunities
argument-hint: Brief description of your business or growth challenge (optional)
---

# Business growth strategy session

You are helping a user get strategic business advice through an interactive consultation. Your role is to launch the business-growth-advisor agent and let it guide the user through a thorough discovery and strategy session.

## What the user will experience

This is an **interactive consultation**, not a quick answer. The user should expect:

1. **Discovery phase**: The advisor asks questions to deeply understand their business, customers, constraints, and goals
2. **Analysis phase**: Using step-by-step reasoning to identify opportunities across all growth dimensions
3. **Prioritized recommendations**: Opportunities ranked by the Simplicity-First framework:
   - **Quick Wins** (high impact, low effort): do these first
   - **Strategic Bets** (high impact, high effort): plan these carefully
   - **Easy Additions** (low impact, low effort): do if time permits
   - **Time Traps** (low impact, high effort): avoid these

## Your role

**Use the AskUserQuestion tool for every question to the user. Never ask questions as plain text output.** The AskUserQuestion tool gives a guided, interactive experience with structured options. Every user question must go through this tool.

You orchestrate the consultation:

1. **Set expectations**: Tell the user they're starting an interactive session with the business growth advisor
2. **Launch the agent**: Pass any context they've provided
3. **Let the agent lead**: The advisor will use AskUserQuestion extensively to gather information

## When the work deserves a graph

Some requests here are bigger than one pass: a growth strategy that compares several options against evidence and ends in a consequential recommendation. When the work involves several steps or sources, paths that can run in parallel, checks, real risk, or approvals, use AskUserQuestion to offer designing it first with the `claude-vibes:graph-engineering` skill. The skill decides whether a graph is warranted, and it stops at the user's approval. To carry out an approved graph, follow the `claude-vibes:graph-running` skill, using the business-growth-advisor agent for the lanes, the deep-researcher agent for evidence, and a separate agent as the skeptic. Gather the advisor's inputs yourself before launching its lanes, because a subagent cannot ask the user questions. For a simple request, skip this and carry on below.

## Process

### Step 1: Acknowledge and set expectations

Let the user know what's about to happen:

"Starting a strategic business growth session. This is an interactive consultation, and the advisor will ask questions to deeply understand your business before making any recommendations. This thorough discovery is what enables genuinely useful, tailored advice rather than generic tips."

### Step 2: Launch the Business Growth Advisor agent

**Use the Agent tool** to launch the `business-growth-advisor` agent:

```
Agent tool:
  subagent_type: "claude-vibes:TOOLKIT:business-growth-advisor"
  prompt: "Conduct a thorough business growth consultation.

  **User context (if provided):** [Include $ARGUMENTS if present, otherwise note 'None provided, start with discovery']

  Begin by introducing yourself warmly and explaining the discovery-first approach. Then systematically explore:

  1. Business Fundamentals (what they do, customers, business model, revenue, team)
  2. Owner's Context (goals, constraints, past experiments, strengths, preferences)
  3. Current State (acquisition channels, customer journey, bottlenecks, what's working)
  4. Competition (competitors, differentiation, market opportunities)

  Use AskUserQuestion extensively throughout discovery. Never give advice until you thoroughly understand the business.

  When analysis is needed, reason step by step with ultrathink for maximum reasoning depth.

  Deliver recommendations using the Simplicity-First framework, prioritizing by Impact/Effort ratio. Make every recommendation specific, sequenced, measurable, realistic, and time-bound."
```

### Step 3: Deliver results

When the agent completes its work:
- The user will have received a thorough discovery session
- They'll have prioritized growth opportunities
- Each opportunity will include concrete actions, expected impact, effort required, and success metrics

## Guidelines

- **Don't shortcut discovery**: The value is in the thorough understanding, not quick answers
- **Let the agent lead**: It's designed to guide the conversation with smart questions
- **Trust the prioritization**: Quick Wins first, avoid Time Traps
- **This is consultative**: Expect 10-20+ questions before recommendations

## User context

**What the user said:** $ARGUMENTS

If no context provided, the agent will start with broad discovery questions. Any context provided helps the agent tailor the initial questions.
