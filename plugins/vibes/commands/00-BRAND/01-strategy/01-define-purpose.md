---
description: Define your brand's purpose, mission, and vision
argument-hint: Optional context about your purpose or motivation
allowed-tools: Read, Glob, Grep, Task, Write, Edit, WebSearch, WebFetch, AskUserQuestion
---

# Define Purpose, Mission & Vision

You are helping a startup founder articulate WHY their brand exists. Using Simon Sinek's Golden Circle methodology, you'll help them discover their purpose (the WHY), mission (the HOW), and vision (the WHAT we're building toward).

## Context Loading

**Founder Brief** (required):
@docs/00-BRAND/00-DISCOVERY/01-founder-brief.md

**Audience Research** (optional):
@docs/00-BRAND/00-DISCOVERY/02-audience-research.md

**Competitive Audit** (optional):
@docs/00-BRAND/00-DISCOVERY/03-competitive-audit.md

**Brand Name** (optional):
@docs/00-BRAND/00-DISCOVERY/04-brand-name.md

**Check above:** If no founder brief content loaded, **STOP** and tell the user to run `/00-BRAND:00-discover/01-discover-founder` first.

Optional additional context: $ARGUMENTS

## Your Role

**CRITICAL: ALWAYS use the AskUserQuestion tool for ANY question to the user. Never ask questions as plain text output.** The AskUserQuestion tool ensures a guided, interactive experience with structured options. Every single user question must go through this tool.

**CRITICAL: You MUST use the Task tool to launch the brand-purpose-architect agent.** Do not create purpose statements yourself — that's what the specialized agent is for.

Your job is to:
1. Verify prerequisites exist
2. Extract key context from loaded documents
3. Prepare a comprehensive, structured prompt for the agent
4. Launch the agent
5. Save and review the results

## Interactive Experience (CRITICAL)

**ALWAYS use the AskUserQuestion tool when interacting with the user.** This ensures a guided, interactive experience where the founder feels engaged and consulted throughout the branding process.

Use AskUserQuestion to:
- Gather preferences before launching agents
- Present options with clear tradeoffs
- Validate agent outputs before saving
- Get feedback and iterate on results

Never save final outputs without user approval.

## Human-Sounding Writing Protocol

**BEFORE launching the brand-purpose-architect agent, you MUST:**

1. **Use the Skill tool** to invoke `claude-vibes:ai-writing-detection`
   - This loads expert-level knowledge of AI writing patterns to avoid

2. **Use the Sequential Thinking MCP tool (ultrathink)** to prepare AI-aware instructions:
   - Review vocabulary patterns to avoid: "delve", "tapestry", "multifaceted", "leverage", "crucial", "comprehensive", "foster", "harness", "navigate", "landscape", "realm", "beacon", "pivotal"
   - Review phrases to avoid: "It's important to note", "In today's fast-paced world", "At its core", "Let me explain"
   - Review structural patterns to avoid: uniform sentence lengths, excessive tricolons, em dash overuse

3. **Include AI-aware instructions** in the agent prompt so output is human-sounding from the start

## Launch the Agent

**Use Task tool** with `subagent_type: "claude-vibes:BRANDING:brand-purpose-architect"` and this prompt:

```
Define the brand purpose, mission, and vision for this startup. ultrathink

## FOUNDER CONTEXT

**Business**: [Extract from founder brief — what they do]
**Founder Story**: [Extract — why they started, personal connection]
**The Change They Want**: [Extract — what frustration or vision drove them]
**What Would Be Lost**: [If this company didn't exist, what would the world miss?]

## AUDIENCE INSIGHTS

**Who They Serve**: [From audience research — primary customer]
**What Customers Value**: [From audience research — key values, aspirations]
**Emotional Jobs**: [From audience research — how customers want to feel]

## COMPETITIVE LANDSCAPE

**Positioning Opportunities**: [From competitive audit — differentiation angles]
**What Others Miss**: [From competitive audit — gaps in competitor messaging]

## BRAND NAME

**Name**: [From brand name document]
**Name Rationale**: [Why this name was chosen — may inform purpose expression]

## CRITICAL: INTERACTIVE DISCOVERY

**ALWAYS use the AskUserQuestion tool to ensure an interactive, guided experience:**
- Gather preferences and opinions before making recommendations
- Present options with clear tradeoffs for the user to choose from
- Validate findings and get feedback before proceeding
- Confirm final outputs resonate before saving

Never make significant decisions without user input. The brand identity belongs to them.

## DISCOVERY APPROACH

### Phase 1: Deep Discovery (WHY Excavation)
Use the WHY Discovery principles to excavate the founder's true purpose:
- Why did they really start this? (Personal connection, formative experiences)
- What change do they want to see in the world?
- What would be lost if this company didn't exist?
- What frustration or injustice drove them to act?
- What are their "Peaks and Valleys" — the defining experiences?

Use AskUserQuestion to dig deeper into founder motivation:
- "What moment made you decide you HAD to do this?"
- "When have you felt most proud of what you're building?"
- "What would you keep doing even if you weren't paid?"

### Phase 2: Core Belief Identification
Find the underlying belief or cause:
- What do they believe about how things SHOULD be?
- What status quo are they challenging?
- What themes appear across multiple stories?
- What are the "golden threads" connecting disparate experiences?

### Phase 3: Hedgehog Validation
Test purpose against Jim Collins' three circles:
- **Passion**: Does this genuinely ignite the team?
- **Excellence**: Can they be the best in the world at this?
- **Economic Engine**: Does this drive sustainable economics?

### Phase 4: Purpose Statement Crafting
Transform insights using the "To _____ so that _____" format:
- First blank = contribution (action taken)
- Second blank = impact (difference made)
- Test against Focus Lab framework (Insight, Impact, Fit, Proofs)

### Phase 5: Mission and Vision Development
Build the supporting statements:
- **Mission**: What they do day-to-day to fulfill purpose (action-oriented, present tense)
- **Vision**: The future state they're working to create (aspirational, future tense)

### Phase 6: Validation and Stress-Testing
Apply rigorous validation:
- Purpose stress test questions
- Anti-pattern check (generic, corporate-speak, purpose washing risk)
- Authenticity verification
- Proof identification

## TOOLS TO USE

- **Sequential Thinking MCP**: Use to excavate the founder's true WHY through multiple lenses and systematically apply each framework
- **AskUserQuestion**: Dig deeper into founder motivation, validate purpose resonates, confirm final statements
- **WebSearch**: Research inspiring purpose-driven brands (Patagonia, Airbnb, Nike) and find their About/Purpose pages
- **WebFetch**: Read the full About/Purpose pages of inspiring brands — study how they articulate their WHY, mission language, and vision statements

## OUTPUT REQUIREMENTS

Deliver the complete purpose, mission, and vision using the Purpose/Mission/Vision Documentation Template from the `golden-circle-purpose` skill. Must include:

1. **Executive Summary**
2. **Full Golden Circle** (WHY/HOW/WHAT with detailed analysis)
3. **Mission Statement** with breakdown
4. **Vision Statement** with future state description
5. **Hedgehog Validation**
6. **Focus Lab Validation** (Insight/Impact/Fit/Proofs)
7. **Purpose Stress Test** results
8. **Anti-Pattern Check** results
9. **Alternative Formulations** (2-3 purpose statement options)
10. **Quick Reference** table
11. **How to Use These Statements** guidance
```

## Guidelines

- Purpose should feel emotional and personally meaningful
- Mission should be actionable and specific
- Vision should be aspirational but believable
- Avoid generic corporate language — make it uniquely theirs
- Purpose is discovered, not invented — excavate authentic stories
- Test rigorously against frameworks before finalizing
- A purpose that doesn't guide decisions isn't a real purpose

## Output

After the agent returns:

1. Ensure `docs/00-BRAND/01-STRATEGY/` directory exists
2. Save to `docs/00-BRAND/01-STRATEGY/01-purpose-mission-vision.md`

3. **Next step:** "Run `/00-BRAND:01-strategy/02-define-values` to define your brand's core values."
