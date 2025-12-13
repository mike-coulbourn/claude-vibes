---
description: Create brand messaging framework with value proposition and pillars
argument-hint: Optional messaging focus or priority
allowed-tools: Read, Glob, Grep, Task, Write, Edit, WebSearch, WebFetch, AskUserQuestion
---

# Create Messaging Framework

You are helping a startup founder create a comprehensive messaging framework. This establishes the value proposition, brand pillars, and key messages that ensure consistency across all communications.

## Context Loading

**Founder Brief** (optional):
@docs/brand/00-discovery/01-founder-brief.md

**Audience Research** (required):
@docs/brand/00-discovery/02-audience-research.md

**Brand Name** (optional):
@docs/brand/00-discovery/04-brand-name.md

**Purpose/Mission/Vision** (required):
@docs/brand/01-strategy/01-purpose-mission-vision.md

**Core Values** (optional):
@docs/brand/01-strategy/02-core-values.md

**Positioning** (required):
@docs/brand/01-strategy/03-positioning.md

**Brand Voice** (required):
@docs/brand/01-strategy/05-brand-personality-voice.md

**Check above:** If audience research, purpose/mission/vision, positioning, or brand voice content is missing, **STOP** and tell the user to complete prerequisites first.

Optional messaging focus: $ARGUMENTS

## Your Role

**CRITICAL: You MUST use the Task tool to launch the brand-messaging-architect agent.** Do not create the messaging framework yourself — that's what the specialized agent is for.

Your job is to:
1. Verify prerequisites exist
2. Extract key context from loaded documents
3. Prepare a comprehensive, structured prompt for the agent
4. Launch the agent
5. Save and review the results

## Launch the Agent

**Use Task tool** with `subagent_type: "claude-vibes:BRANDING:brand-messaging-architect"` and this prompt:

```
Create the brand messaging framework. ultrathink

## BRAND CONTEXT

**Brand Name**: [From brand name document]
**Purpose (WHY)**: [From purpose-mission-vision.md]
**Mission (HOW)**: [From purpose-mission-vision.md]
**Vision (WHERE)**: [From purpose-mission-vision.md]
**Core Values**: [From core-values.md]
**Positioning**: [From positioning.md — the territory we claim]
**Voice Traits**: [From brand-personality-voice.md]

## AUDIENCE INSIGHTS

**Who They Serve**: [From audience research — primary customer segment]
**Customer Jobs**: [From audience research — functional, social, emotional jobs]
**Customer Pains**: [From audience research — frustrations and obstacles]
**Customer Gains**: [From audience research — desired outcomes]
**Audience Language**: [From audience research — how they talk]

## FOUNDER CONTEXT

**Founder's Vision**: [From founder brief — what they want to achieve]
**Key Differentiators**: [From founder brief — what makes them unique]

## COMPETITIVE LANDSCAPE

**Competitor Messaging**: [From competitive audit if exists — how competitors message]
**Messaging Gaps**: [From competitive audit — opportunities for differentiation]

## DISCOVERY APPROACH

### Phase 1: Synthesize Brand Inputs
Analyze all inputs to understand:
- How purpose, values, and positioning should inform messaging
- What voice traits mean for how we communicate
- What the audience cares about most (jobs, pains, gains)
- Where competitive white space exists

### Phase 2: Develop Value Proposition
Apply value proposition frameworks:
- **Value Proposition Canvas**: Map customer jobs/pains/gains to our offering
- **Jobs-to-be-Done**: Identify the functional, social, emotional jobs
- **Three Benefits**: Define functional, emotional, self-expression benefits
- **Geoffrey Moore Template**: Write the positioning statement
- **The "Only" Test**: Complete the Onlyness statement

### Phase 3: Define Brand Pillars
Create 3-5 messaging pillars:
- Each pillar with theme, core message, supporting messages
- Each pillar with proof points (rational, emotional, visual)
- Map how pillars support the value proposition
- Define usage guidance for each pillar

### Phase 4: Build Messaging Architecture
Construct the complete messaging system:
- **Messaging House**: Roof (value prop), Pillars, Foundation
- **Messaging Hierarchy**: Primary → Secondary → Tertiary
- **Message Layers Assessment**: Clarity → Relevance → Value → Differentiation
- **Messages by Audience**: Adapt for different segments
- **Messages by Touchpoint**: Website, sales, social, email, etc.

### Phase 5: Validate and Test
Run quality checks:
- **MECLABS Criteria**: Appeal, Exclusivity, Clarity, Credibility
- **The "Only" Test**: Can only we claim this?
- **The Clarity Test**: Understood in 5 seconds?
- **The "So What?" Test**: Why should customers care?
- Document testing recommendations

## TOOLS TO USE

- **Sequential Thinking MCP**: Systematically build from value proposition through pillars to messaging hierarchy
- **AskUserQuestion**: Validate value proposition resonates, get input on pillar priorities, confirm messaging tone
- **WebSearch**: Research competitor landing pages and messaging patterns, find industry messaging examples
- **WebFetch**: Read competitor websites — analyze their value propositions, messaging pillars, and proof points for differentiation opportunities

## OUTPUT REQUIREMENTS

Deliver the complete messaging framework using the Messaging Framework Document Template from the `brand-messaging-architecture` skill. Must include:

1. **Executive Summary**
2. **Strategic Foundation** (brand inputs, messaging challenge)
3. **Value Proposition** (core statement, Onlyness, Geoffrey Moore, three benefits)
4. **Message Layers Assessment** (Peep Laja's 4 layers)
5. **Brand Pillars** (3-5 pillars with proof points)
6. **Messaging House** (visual architecture)
7. **Messaging Hierarchy** (primary, secondary, tertiary)
8. **Messages by Audience** (segment adaptations)
9. **Messages by Touchpoint** (channel adaptations)
10. **Quality Tests Completed** (MECLABS assessment)
11. **Quick Reference Card** (one-page summary)
```

## Guidelines

- **Start with value proposition**: Everything flows from here
- **Apply Peep Laja's layers in order**: Clarity first, then relevance, then value, then differentiation
- **Limit pillars to 3-5**: More creates confusion
- **Be specific**: Vague messages are forgettable
- **Prove claims**: Every claim needs supporting evidence
- **Customer is the hero**: Position brand as guide, not protagonist
- **Test with real language**: Use words customers actually say

## Output

After the agent returns:

1. Ensure `docs/brand/02-messaging/` directory exists
2. Save to `docs/brand/02-messaging/01-messaging-framework.md`

3. Use Task tool to launch `claude-vibes:TOOLKIT:ai-writing-detector` agent to review the document for AI patterns and refine if needed.

4. **Next step:** "Run `/00-BRAND:02-messaging/02-create-tagline` to develop your brand tagline."
