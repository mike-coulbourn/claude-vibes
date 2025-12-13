---
description: Research and define your target audience for brand identity
argument-hint: Optional focus area or specific audience segment
allowed-tools: Read, Glob, Grep, Task, Write, Edit, WebSearch, WebFetch, AskUserQuestion
---

# Research Target Audience

You are helping a startup founder deeply understand their target audience. This research will inform brand positioning, voice, and messaging.

## Context Loading

**Founder Brief** (required):
@docs/00-BRAND/00-DISCOVERY/01-founder-brief.md

**Check above:** If no founder brief content loaded, **STOP** and tell the user to run `/00-BRAND:00-discover/01-discover-founder` first.

Optional focus area: $ARGUMENTS

## Your Role

**CRITICAL: You MUST use the Task tool to launch the brand-audience-researcher agent.** Do not do the audience research yourself — that's what the specialized agent is for.

Your job is to:
1. Verify prerequisites exist
2. Extract key context from the founder brief
3. Prepare a comprehensive, structured prompt for the agent
4. Launch the agent
5. Save and review the results

## Launch the Agent

**Use Task tool** with `subagent_type: "claude-vibes:BRANDING:brand-audience-researcher"` and this prompt:

```
Research the target audience for this startup. ultrathink

## FOUNDER CONTEXT

**Business**: [Extract from founder brief - what they do]
**Problem Solved**: [Extract - the core problem]
**Initial Customer Description**: [Extract - who founder thinks the customer is]
**Founder's Why**: [Extract - purpose/motivation]

## RESEARCH OBJECTIVES

Deliver a comprehensive audience profile covering:

### 1. Jobs-to-be-Done (All Three Dimensions)
- **Functional Job**: What task are they trying to accomplish?
- **Emotional Job**: How do they want to FEEL?
- **Social Job**: How do they want to be SEEN by others?
- **The Struggling Moment**: What triggers their search for a solution?

### 2. Four Forces Analysis (Bob Moesta)
- **PUSH**: What frustrates them about current solutions?
- **PULL**: What attracts them to new solutions?
- **ANXIETY**: What fears hold them back from switching?
- **HABIT**: What keeps them comfortable with status quo?
- **Switching Analysis**: Is Push + Pull > Anxiety + Habit?

### 3. Psychographic Profile
- **Limbic Type**: Which of the 7 types? (Traditionalist, Harmonizer, Open Connoisseur, Hedonist, Adventurer, Performer, Disciplined)
- **VALS Segment**: Which segment? (Innovator, Thinker, Achiever, Experiencer, Believer, Striver, Maker, Survivor)
- **Core Values**: What do they believe in?
- **Motivations**: What drives their decisions?

### 4. Emotional Motivators (HBR Research)
- Which emotional motivators drive this audience?
- What emotional territory could this brand own?

### 5. Language & Community
- **Where they gather**: Reddit, forums, Discord, social platforms
- **Influencers they follow**: Who do they trust?
- **Language patterns**: Exact words and phrases they use
- **Brands they love**: What earns their loyalty?

### 6. Research-to-Strategy Bridge
Map findings to brand strategy elements:
- Primary JTBD → Brand Promise
- Push Forces → Problem Messaging
- Pull Forces → Benefit Messaging
- Anxiety Forces → Trust Signals Needed
- Emotional Jobs → Emotional Territory
- Social Jobs → Brand Personality

## TOOLS TO USE

- **Sequential Thinking MCP**: Structure your analysis through the Four Forces and Three Job Types systematically
- **WebSearch**: Search extensively for:
  - `"[audience] reddit" OR "[problem] discussion"`
  - `"[audience] frustrations" OR "[audience] pain points"`
  - `"why [audience] switched from [old solution]"`
  - `"[audience] values" OR "what motivates [audience]"`
  - `"brands [audience] trust" OR "[audience] favorite brands"`
- **WebFetch**: Read full Reddit threads, forum discussions, and reviews — extract authentic voices, exact language, and emotional undertones
- **AskUserQuestion**: Validate key findings with the founder:
  - "Does this match your ideal customer?"
  - "Any segments I should explore deeper?"
  - "Does this language resonate with people you've talked to?"

## OUTPUT REQUIREMENTS

Structure the output using the templates in the `jtbd-psychographic-research` skill:
- Forces of Progress Canvas
- Job Story Template
- Psychographic Profile Summary
- Research-to-Strategy Bridge

Include a "Key Quotes and Evidence" section with real quotes from research.

Deliver findings that are SPECIFIC to this audience — avoid generic insights that could apply to anyone.
```

## Guidelines

- The agent does the research — you orchestrate
- Trust the agent's findings but validate with the founder
- If the agent surfaces surprising insights, discuss with the founder before finalizing
- The agent has deep methodology (500+ lines) — your job is to provide clear context and objectives

## Output

After the agent returns:

1. Ensure `docs/00-BRAND/00-DISCOVERY/` directory exists
2. Save the audience research to `docs/00-BRAND/00-DISCOVERY/02-audience-research.md`

3. Use Task tool to launch `claude-vibes:TOOLKIT:ai-writing-detector` agent to review the document for AI patterns and refine if needed.

4. **Next step:** "Run `/00-BRAND:00-discover/03-audit-competitors` to analyze the competitive landscape."
