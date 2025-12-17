---
description: Define core values that differentiate your brand
argument-hint: Optional context about values important to you
allowed-tools: Read, Glob, Grep, Task, Write, Edit, WebSearch, WebFetch, AskUserQuestion
---

# Define Core Values

You are helping a startup founder define 3-4 core values that will guide their brand. These values must be specific, differentiating, and actionable — not generic corporate platitudes.

## Context Loading

**Founder Brief** (required):
@docs/00-BRAND/00-DISCOVERY/01-founder-brief.md

**Audience Research** (optional):
@docs/00-BRAND/00-DISCOVERY/02-audience-research.md

**Competitive Audit** (optional):
@docs/00-BRAND/00-DISCOVERY/03-competitive-audit.md

**Brand Name** (optional):
@docs/00-BRAND/00-DISCOVERY/04-brand-name.md

**Purpose/Mission/Vision** (required):
@docs/00-BRAND/01-STRATEGY/01-purpose-mission-vision.md

**Check above:** If founder brief or purpose/mission/vision content is missing, **STOP** and tell the user to complete prerequisites first.

Optional additional context: $ARGUMENTS

## Your Role

**CRITICAL: ALWAYS use the AskUserQuestion tool for ANY question to the user. Never ask questions as plain text output.** The AskUserQuestion tool ensures a guided, interactive experience with structured options. Every single user question must go through this tool.

**CRITICAL: You MUST use the Task tool to launch the brand-values-curator agent.** Do not create values yourself — that's what the specialized agent is for.

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

**BEFORE launching the brand-values-curator agent, you MUST:**

1. **Use the Skill tool** to invoke `claude-vibes:ai-writing-detection`
   - This loads expert-level knowledge of AI writing patterns to avoid

2. **Use the Sequential Thinking MCP tool (ultrathink)** to prepare AI-aware instructions:
   - Review vocabulary patterns to avoid: "delve", "tapestry", "multifaceted", "leverage", "crucial", "comprehensive", "foster", "harness", "navigate", "landscape", "realm", "beacon", "pivotal"
   - Review phrases to avoid: "It's important to note", "In today's fast-paced world", "At its core", "Let me explain"
   - Review structural patterns to avoid: uniform sentence lengths, excessive tricolons, em dash overuse

3. **Include AI-aware instructions** in the agent prompt so output is human-sounding from the start

## Launch the Agent

**Use Task tool** with `subagent_type: "claude-vibes:BRANDING:brand-values-curator"` and this prompt:

```
Define 3-4 core values for this brand. ultrathink

## FOUNDER CONTEXT

**Business**: [Extract from founder brief — what they do]
**Founder Motivation**: [Why they started — personal connection]
**Non-Negotiables**: [From founder brief — what they'd never compromise on]
**Decisions That Reveal Values**: [Past decisions that show values in action]

## PURPOSE FOUNDATION

**Purpose (WHY)**: [From purpose-mission-vision.md]
**Mission (HOW)**: [From purpose-mission-vision.md]
**Core Belief**: [The underlying belief driving the brand]

## AUDIENCE INSIGHTS

**Who They Serve**: [From audience research — primary customer]
**What Customers Value**: [From audience research — key values, motivations]
**Tribal Mores**: [From audience research — moral views of target tribe]

## COMPETITIVE LANDSCAPE

**Competitor Values**: [From competitive audit — values competitors claim]
**Differentiation Opportunities**: [Values competitors don't emphasize]

## BRAND NAME

**Name**: [From brand name document]
**Name Rationale**: [Why this name — may inform value expression]

## CRITICAL: INTERACTIVE DISCOVERY

**ALWAYS use the AskUserQuestion tool to ensure an interactive, guided experience:**
- Gather preferences and opinions before making recommendations
- Present options with clear tradeoffs for the user to choose from
- Validate findings and get feedback before proceeding
- Confirm final outputs resonate before saving

Never make significant decisions without user input. The brand identity belongs to them.

## DISCOVERY APPROACH

### Phase 1: Deep Discovery (Values Excavation)
Use discovery principles to excavate authentic values:
- What motivated the founder to start this? (Personal connection)
- What would they never compromise on, even if it cost business?
- What decisions have revealed their values?
- What do they respect in other companies? What do they despise?
- Use "Always/Never" statements to reveal actual behaviors

Use AskUserQuestion to dig deeper:
- "What would you never compromise on, even if it cost you business?"
- "Describe a decision you made that revealed what you stand for"
- "What do you respect most in other companies? What do you despise?"

### Phase 2: Connect to Purpose
Ensure values enable the purpose:
- What principles make the purpose achievable?
- What values does the target audience share?
- Do these values align with customer "mores" (tribal moral views)?

### Phase 3: Differentiate from Generic
Strip away anything a competitor could claim:
- Apply the Opposite Test (could a reasonable company claim opposite?)
- Identify the sacrifice/antivalue for each (what do we give up?)
- Test with Behavioral Specificity (can we describe exactly how it looks?)
- Check against generic values list (integrity, quality, excellence alone = fail)

### Phase 4: Categorize Values (Lencioni Framework)
Use the four categories:
- **Core Values**: Unchanging, non-negotiable (2-3 max)
- **Aspirational Values**: Where we're heading (label honestly)
- **Permission-to-Play**: Table stakes, don't feature
- **Accidental**: Emerged without intention

### Phase 5: Operationalize (Brene Brown Process)
For each value:
- Map 3-5 observable behaviors
- Define aligned vs. unaligned behaviors
- Identify "slippery behaviors" (subtle erosion)
- Create context-specific applications (decisions, culture, product, communication)

### Phase 6: Validate
Run final checks:
- Fire Someone Test: Would we fire a high performer who violated this?
- Hard Choice Test: Does this help make difficult decisions?
- Memorability: Can employees recite these?
- Evidence: Is there proof we actually live this?

## TOOLS TO USE

- **Sequential Thinking MCP**: Systematically apply each framework and test every value candidate
- **AskUserQuestion**: Dig deeper into non-negotiables, validate values feel authentic
- **WebSearch**: Research competitor values pages and values-forward brand examples
- **WebFetch**: Read competitor values pages in full — analyze their exact language to differentiate

## OUTPUT REQUIREMENTS

Deliver the complete values documentation using the Values Documentation Template from the `brand-values-development` skill. Must include:

1. **Executive Summary**
2. **Values Category Analysis** (Core/Aspirational/Permission-to-Play)
3. **Full Core Values** (3-4 with complete detail for each)
4. **Differentiation Test Results** (Opposite, Sacrifice, Fire Someone)
5. **Values in Practice** (Decision framework, Hiring filter, Product principles)
6. **What We DON'T Value** (Anti-values)
7. **Values Summary Card** (Quick reference)
```

## Guidelines

- **Quality over quantity**: 3-4 values maximum — more dilutes everything
- **Specific over generic**: If a competitor could claim it, it's not specific enough
- **Actions over aspirations**: Values should describe actual behavior, not wishes
- **Trade-offs required**: Real values require giving something up
- **Behaviors required**: Each value needs observable behaviors mapped
- **The Fire Test**: If you wouldn't fire a high performer over it, it's not core

## Output

After the agent returns:

1. Ensure `docs/00-BRAND/01-STRATEGY/` directory exists
2. Save to `docs/00-BRAND/01-STRATEGY/02-core-values.md`

3. **Next step:** "Run `/00-BRAND:01-strategy/03-define-positioning` to develop your brand positioning."
