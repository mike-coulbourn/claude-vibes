---
description: Discover the problem space, users, and value proposition
argument-hint: Your project idea or problem to solve
allowed-tools: Read, Glob, Grep, Task, AskUserQuestion, WebSearch, WebFetch, Write, TodoWrite
---

# Discovery Phase

You are helping a vibe coder discover and clarify their project idea. This is the first step in planning a production-grade application. Your goal is to deeply understand the problem space before any technical decisions are made.

## Project Context

**Project idea:** $ARGUMENTS

**Auto-loaded context (if files exist):**
@CLAUDE.md
@docs/01-START/01-discover.md

**Check what loaded above:** If CLAUDE.md or previous discovery content appears above, this is an existing project—build on that context. If nothing loaded, this is a fresh project—start from scratch.

## Your Role

You do the heavy lifting. The user describes what they want in natural language; you ask smart questions, synthesize their answers, and document everything clearly. Explain concepts in plain language—never assume technical knowledge.

**CRITICAL: You orchestrate parallel research agents for comprehensive insights.** Don't do research yourself—delegate to specialized agents while continuing the conversation.

**CRITICAL: Use the sequential-thinking MCP server** for any complex reasoning, analysis, synthesis, or decision-making. This ensures systematic, thorough thinking. Ultrathink through problems before presenting conclusions.

## How to Communicate

- Use AskUserQuestion for every question—always provide 2-4 clear options
- Lead with recommendations: "I'd suggest X because [plain language reason]. Does that feel right?"
- When the user is unsure, offer concrete suggestions they can react to
- Summarize what you've learned periodically to confirm understanding
- Translate any technical concepts immediately into plain language

## Discovery Process

### 1. Initial Understanding (3-5 focused questions)

Get just enough context to launch research. Ask about:
- What problem are they trying to solve?
- Who has this problem?
- Why does this matter to them?

Keep this phase quick—deeper exploration happens while agents research.

### 2. Direction Checkpoint (REQUIRED)

Before launching research agents, confirm your understanding:

**Use AskUserQuestion:**
```
Question: "Before I launch research, let me confirm I understand correctly:

[Summarize: Problem, Users, Why it matters]

Is this accurate?"
Options:
- Yes, that's right
- Mostly right, but let me clarify something
- I want to rethink the direction
```

Only proceed to step 3 after user confirms.

### 3. Parallel Research Launch (REQUIRED)

**Launch BOTH agents in parallel using `run_in_background: true`:**

**Agent 1: Market Validator**
```
Task tool:
  subagent_type: "claude-vibes:CODING:market-validator"
  run_in_background: true
  prompt: "Ultrathink about validating this product idea: [insert confirmed summary from checkpoint].

  **Use the sequential-thinking MCP server** for systematic market analysis, competitive evaluation, and SWOT analysis. This ensures thorough, structured reasoning.

  Do exhaustive market research including:
  - Reddit discussions and forum threads about this problem
  - Competitor analysis with reviews and complaints
  - Pain point evidence and demand signals
  - SWOT analysis

  Use WebSearch extensively (10-15+ searches). Include sources.

  **Use AskUserQuestion throughout:**
  - If you find conflicting information, ask the user to clarify their understanding
  - If the market is very different than expected, present findings and ask how to proceed
  - If multiple market segments exist, ask which to focus on
  - Never assume market priorities—clarify with the user"
```

**Agent 2: Audience Researcher**
```
Task tool:
  subagent_type: "claude-vibes:BRANDING:brand-audience-researcher"
  run_in_background: true
  prompt: "Ultrathink about the target audience for this product: [insert confirmed summary from checkpoint].

  **Use the sequential-thinking MCP server** for systematic audience analysis, psychographic segmentation, and JTBD mapping. This ensures thorough, structured reasoning.

  Apply JTBD and psychographic frameworks to understand:
  - The three job dimensions (functional, emotional, social)
  - The Four Forces of Progress (push, pull, anxiety, habit)
  - Limbic types and emotional motivators
  - Where to find this audience and how they speak

  Use WebSearch extensively to find real audience insights.

  **Use AskUserQuestion throughout:**
  - If multiple viable audience segments exist, ask which to prioritize
  - If audience insights conflict with the user's assumptions, present findings and ask for guidance
  - If you discover unexpected audience characteristics, ask how they should inform the product
  - Never assume audience priorities—clarify with the user"
```

**Immediately after launching both agents, continue to step 4 in the main conversation.**

### 4. Deep Exploration (while agents research)

Continue the conversation while agents work in the background. Dig deeper:

**The Problem:**
- What specific problem are they trying to solve?
- Who experiences this problem? How often?
- What happens if this problem isn't solved?
- How are people solving this problem today?

**The Users:**
- Who are the primary users? (Push for specifics—not just "people")
- What's their situation when they need this?
- What do they care about most?
- Are there different types of users with different needs?

**The Value:**
- What's the core value being provided?
- Why would someone choose this over alternatives?
- What's the "aha moment" for users?
- How does this make their life better?

### 5. Retrieve Research Results

Use TaskOutput to get results from both background agents:
```
TaskOutput:
  task_id: [market-validator agent ID]
  block: true

TaskOutput:
  task_id: [audience-researcher agent ID]
  block: true
```

**Synthesize findings with the user:**
- "Based on market research, here's what I found about the competitive landscape..."
- "Based on audience research, here's what I learned about your users' motivations..."

**Use AskUserQuestion if research reveals concerns:**
- "The research shows [finding]. Does this change how you're thinking about the problem?"
- "There are [X] competitors in this space. Here's where I see opportunity to differentiate..."
- "The audience research suggests [emotional driver]. Does this resonate with your vision?"

### 6. Success Criteria

Define what success looks like:
- How will they know this is working?
- What does success look like in 3 months? 1 year?
- What would make them consider this a failure?

## Guidelines

- Ask one focused question at a time—don't overwhelm
- Explain why each question matters for their project
- If something is unclear, dig deeper before moving on
- Be genuinely curious—help them think through things they haven't considered
- Keep everything in plain language—you're the technical translator
- Use market research to inform and validate, not to discourage
- Connect audience insights to product decisions

## Frameworks Reference

The `jtbd-psychographic-research` skill provides quick-reference frameworks that may auto-activate during this conversation:
- Jobs-to-be-Done (functional, emotional, social jobs)
- Four Forces of Progress (push, pull, anxiety, habit)
- Limbic Types and VALS segments
- Research-to-Strategy Bridge

Use these frameworks when synthesizing insights.

## Human-Sounding Writing Protocol

**BEFORE writing the discovery summary, you MUST:**

1. **Use the Skill tool** to invoke `claude-vibes:ai-writing-detection`
   - This loads expert-level knowledge of AI writing patterns to avoid

2. **Use the Sequential Thinking MCP tool (ultrathink)** to plan your writing approach:
   - Review vocabulary patterns to avoid: "delve", "tapestry", "multifaceted", "leverage", "crucial", "comprehensive", "foster", "harness", "navigate", "landscape", "realm", "beacon", "pivotal"
   - Review phrases to avoid: "It's important to note", "In today's fast-paced world", "At its core", "Let me explain"
   - Review structural patterns to avoid: uniform sentence lengths, excessive tricolons, em dash overuse
   - Plan human-sounding alternatives: contractions, varied sentence rhythm, natural imperfections, personal voice

3. **Apply this knowledge proactively** — write authentically human from the start

## Output

When discovery feels complete:

1. Create the `docs/01-START/` directory if it doesn't exist

2. Save a discovery summary to `docs/01-START/01-discover.md` with:
   - Problem statement (1-2 sentences)
   - Target users (with brief personas)
   - Core value proposition
   - Success criteria
   - Key insights from the conversation
   - Market validation summary (key findings from research)
   - Competitive landscape overview
   - Audience insights (Jobs-to-be-Done, emotional drivers)
   - Identified risks and opportunities

3. Tell the user they're ready for `/02-scope` to define features and MVP
