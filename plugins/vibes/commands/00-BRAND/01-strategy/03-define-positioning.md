---
description: Develop brand positioning strategy
argument-hint: Optional positioning direction or differentiation angle
allowed-tools: Read, Glob, Grep, Task, Write, Edit, WebSearch, WebFetch, AskUserQuestion
---

# Define Positioning

You are helping a startup founder claim distinct territory in the customer's mind. Using methodologies from Al Ries, Jack Trout, and Marty Neumeier's ZAG, you'll develop positioning that makes the brand the obvious choice for its audience.

## Context Loading

**Founder Brief** (required):
@docs/00-BRAND/00-DISCOVERY/01-founder-brief.md

**Audience Research** (required):
@docs/00-BRAND/00-DISCOVERY/02-audience-research.md

**Competitive Audit** (required):
@docs/00-BRAND/00-DISCOVERY/03-competitive-audit.md

**Brand Name** (optional):
@docs/00-BRAND/00-DISCOVERY/04-brand-name.md

**Purpose/Mission/Vision** (optional):
@docs/00-BRAND/01-STRATEGY/01-purpose-mission-vision.md

**Core Values** (optional):
@docs/00-BRAND/01-STRATEGY/02-core-values.md

**Check above:** If founder brief, audience research, or competitive audit content is missing, **STOP** and tell the user to complete prerequisites first.

Optional positioning direction: $ARGUMENTS

## Your Role

**CRITICAL: ALWAYS use the AskUserQuestion tool for ANY question to the user. Never ask questions as plain text output.** The AskUserQuestion tool ensures a guided, interactive experience with structured options. Every single user question must go through this tool.

**CRITICAL: You MUST use the Task tool to launch the brand-positioning-strategist agent.** Do not create positioning yourself — that's what the specialized agent is for.

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

**BEFORE launching the brand-positioning-strategist agent, you MUST:**

1. **Use the Skill tool** to invoke `claude-vibes:ai-writing-detection`
   - This loads expert-level knowledge of AI writing patterns to avoid

2. **Use the Sequential Thinking MCP tool (ultrathink)** to prepare AI-aware instructions:
   - Review vocabulary patterns to avoid: "delve", "tapestry", "multifaceted", "leverage", "crucial", "comprehensive", "foster", "harness", "navigate", "landscape", "realm", "beacon", "pivotal"
   - Review phrases to avoid: "It's important to note", "In today's fast-paced world", "At its core", "Let me explain"
   - Review structural patterns to avoid: uniform sentence lengths, excessive tricolons, em dash overuse (LLMs use em dashes formulaically to create "punched up" sales rhythms—swapping to commas doesn't help; vary your structures instead)

3. **Include AI-aware instructions** in the agent prompt so output is human-sounding from the start

## Launch the Agent

**Use Task tool** with `subagent_type: "claude-vibes:BRANDING:brand-positioning-strategist"` and this prompt:

```
Develop the brand positioning strategy for this startup. ultrathink

## FOUNDER CONTEXT

**Business**: [Extract from founder brief — what they do]
**Unfair Advantage**: [From founder brief — unique strengths, assets, expertise]
**Founder Motivation**: [Why they started — what drives them]

## AUDIENCE INSIGHTS

**Who They Serve**: [From audience research — primary customer segment]
**What Customers Value**: [From audience research — key values, priorities]
**Emotional Jobs**: [From audience research — how customers want to feel]
**Functional Jobs**: [From audience research — what they need to accomplish]

## COMPETITIVE LANDSCAPE

**Market Leader**: [From competitive audit — who dominates, what they own]
**Key Competitors**: [From competitive audit — other players and their positions]
**What's Already Taken**: [Positions competitors have claimed]
**White Space**: [From competitive audit — gaps and opportunities]

## STRATEGIC FOUNDATION

**Purpose (WHY)**: [From purpose-mission-vision.md if exists]
**Core Values**: [From core-values.md if exists]

## BRAND NAME

**Name**: [From brand name document]
**Name Rationale**: [Why this name — may inform positioning expression]

## CRITICAL: INTERACTIVE DISCOVERY

**ALWAYS use the AskUserQuestion tool to ensure an interactive, guided experience:**
- Gather preferences and opinions before making recommendations
- Present options with clear tradeoffs for the user to choose from
- Validate findings and get feedback before proceeding
- Confirm final outputs resonate before saving

Never make significant decisions without user input. The brand identity belongs to them.

## DISCOVERY APPROACH

### Phase 1: Assess Current Position
- What word (if any) does this brand currently own?
- Where does it stand relative to competitors?
- What perceptions already exist in prospects' minds?

### Phase 2: Analyze the Landscape
Map the competitive positioning battlefield:
- Who is the market leader? What position do they own?
- What positions do other competitors claim?
- What does the target audience care about most?
- What territory is unclaimed?

### Phase 3: Find the White Space
Use multiple lenses to find positioning opportunities:
- **Cherchez le Creneau**: Analyze all 7 creneau types (size, price, sex, timing, age, distribution, heavy-user)
- **Positioning Map**: Plot competitors on two meaningful axes — find empty quadrants
- **Ladder Analysis**: Which ladder to climb? Or should we create a new one?
- **ZAG Opportunity**: What do all competitors do? What's the radical opposite?

### Phase 4: Apply the 22 Laws
Reference the Immutable Laws of Marketing:
- **Law of Category**: Can we create a new category to be first in?
- **Law of Focus**: What word can we own?
- **Law of Opposite**: If we're #2, how do we position against #1?
- **Law of Sacrifice**: What must we give up to own our position?

### Phase 5: Craft Positioning Statements
Develop the core positioning artifacts:
- **Onliness Statement** (all 5 W's: WHAT, HOW, WHO, WHERE, WHY)
- **Positioning Statement** (For [target], [Brand] is the [category] that [benefit] because [reason])
- **Trueline** (the one true thing — bridge from strategy to creativity)

### Phase 6: Validate and Stress-Test
Run rigorous validation:
- **Onliness Test**: Can we honestly use the word "only"?
- **Simplicity Test**: Can we explain it in one sentence?
- **Memorability Test**: Will customers remember it?
- **Credibility Test**: Can we actually deliver on this?
- **Differentiation Test**: Is it meaningfully different from competitors?
- **22 Laws Check**: Which laws support or contradict this position?

## TOOLS TO USE

- **Sequential Thinking MCP**: Rigorously map competitive positions, analyze all 7 creneau types, and systematically apply the 22 Laws
- **AskUserQuestion**: Validate positioning dimensions feel right, confirm territory resonates, get input on trade-offs
- **WebSearch**: Research competitor homepages, positioning statements, and case studies of successful positioning
- **WebFetch**: Read competitor homepages and "About" pages in full — understand their complete positioning narrative and identify white space

## OUTPUT REQUIREMENTS

Deliver the complete positioning strategy using the Positioning Documentation Template from the `brand-positioning-theory` skill. Must include:

1. **Executive Summary**
2. **Competitive Landscape Analysis** (leader, competitors, ladder, what's taken)
3. **Creneau Analysis** (all 7 types assessed)
4. **Positioning Map** (two axes, competitor placement, white space)
5. **Onliness Statement** (5W's and shortened version with validation)
6. **Positioning Statement** (with element breakdown)
7. **Trueline Development** (candidates and recommendation)
8. **22 Laws Analysis** (application of critical laws)
9. **ZAG Opportunity** (what everyone zigs, how we zag)
10. **Ladder Strategy** (climb vs. create new)
11. **Sacrifice Analysis** (product, market, messaging trade-offs)
12. **Positioning Proof Points** (what proof is needed)
13. **Anti-Pattern Check** (validation against common mistakes)
14. **Quick Reference Card** (summary for daily use)
```

## Guidelines

- **Position against the status quo, not just competitors** — the best positioning creates a new category
- **Own one word** — if you can't fill in the blanks clearly, the positioning isn't sharp enough
- **The "ONLY" must be literally true** — if you can't say "only," you don't have a zag
- **Sacrifice is the point** — real positioning requires giving something up
- **Think like the customer** — positioning exists in their mind, not yours
- **Reference the Laws** — use the 22 Laws as a checklist

## Output

After the agent returns:

1. Ensure `docs/00-BRAND/01-STRATEGY/` directory exists
2. Save to `docs/00-BRAND/01-STRATEGY/03-positioning.md`

3. **Next step:** "Run `/00-BRAND:01-strategy/04-select-archetype` to select your brand archetype."
