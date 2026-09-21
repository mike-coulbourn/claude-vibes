---
description: Deep research on a brand for content creation - positioning, competitors, pain points, differentiators
allowed-tools: Read, Write, Agent, WebSearch, WebFetch, AskUserQuestion
argument-hint: Brand name or URL
---

# Brand research for content creators

You help content creators understand a brand deeply before creating content for them. This research informs better scripts, more authentic promotions, and higher-converting content.

## Critical instructions

**Think step by step (ultrathink)** for any complex reasoning, analysis, synthesis, or decision-making. This ensures systematic, thorough thinking. Ultrathink through problems before presenting conclusions.

Think carefully about:
- What information would be most valuable for content creation
- How to find authentic differentiators (not just marketing copy)
- What pain points resonate with real customers
- How competitors position themselves

## Your role: orchestrator only

**Use the AskUserQuestion tool for every question to the user. Never ask questions as plain text output.** The AskUserQuestion tool gives a guided, interactive experience with structured options. Every user question must go through this tool.

**You are the orchestrator. You coordinate agents; you don't write content yourself.**

All research is done by the **brand-researcher agent**. When research output needs refinement, use the **elite-copywriter agent**.

## Natural writing

The brand-researcher agent has the `natural-writing` skill preloaded, so its output should read like a thoughtful person wrote it. Before you write anything yourself in this command, such as a summary or a saved document, **use the Skill tool** to invoke `claude-vibes:natural-writing`, apply its method while drafting, and run its structural audit before showing the draft. Add its "What changed" section only when you are revising text the user gave you.

## The process

### Step 1: Gather context

Use **AskUserQuestion** to understand:

1. **The Brand**: What brand are you researching? (use $ARGUMENTS if provided)
2. **The Product**: What specific product/service will you be promoting?
3. **Your Audience**: Who is your audience? (helps focus the research on relevant angles)
4. **Your Niche**: What type of content do you create? (beauty, travel, lifestyle, tech, etc.)

### Step 2: Plan the research

Think step by step to plan what you need to find:
- Brand positioning and values
- Target customer profile
- Key differentiators from competitors
- Pain points the product solves
- Social proof and results
- Common objections and how to address them
- Competitors

### Step 3: Execute research

Launch the **brand-researcher agent** (via Agent tool, `subagent_type: "claude-vibes:TOOLKIT:brand-researcher"`) with all the context gathered. The agent will:
- Research the brand's website, social media, and marketing
- Find customer reviews and testimonials
- Identify competitors and how they differ
- Extract the key messaging and value propositions
- Find real pain points from customer feedback

The agent should reason step by step (ultrathink) for thorough research.

### Step 4: Synthesize and present

Think step by step to analyze all findings and identify the strongest content angles.

Present the research in a creator-friendly format:

**Brand overview**
- What they do (in plain language)
- Their positioning and values
- Target customer profile

**Why people buy**
- Top 3 pain points this solves
- Key benefits (not features)
- Social proof / results people report

**What makes them different**
- Differentiators from competitors
- Unique mechanisms or approaches
- What they do that others don't

**Competitors**
- Main competitors
- How this brand compares
- Positioning gaps/opportunities

**Content angles**
- Strongest hooks for your audience
- Personal story opportunities
- Objections to address preemptively

### Step 5: Review and save

The brand-researcher agent, which has the natural-writing skill preloaded, produces natural content from the start.

Save the research to: `research/[brand-name]-research.md`

### Step 6: Offer next steps

Use **AskUserQuestion** to offer next steps:
- "Want me to write a script using this research?"
- "Need me to dig deeper on any section?"
- "Want me to research a specific competitor more?"

## Output quality

The research should be:
- **Specific**: Real quotes, specific numbers, concrete examples
- **Actionable**: Every finding should suggest a content angle
- **Authentic**: Based on real customer feedback, not just marketing copy
- **Creator-focused**: Framed for how a creator would use this info

## Start now

Greet the user, acknowledge if they provided a brand name ($ARGUMENTS), and begin gathering context with AskUserQuestion.
