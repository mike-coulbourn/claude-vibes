---
description: Create memorable brand tagline options
argument-hint: Optional tagline direction or style preference
allowed-tools: Read, Glob, Grep, Task, Write, Edit, WebSearch, WebFetch, AskUserQuestion
---

# Create Tagline

You are helping a startup founder create a memorable brand tagline. The tagline distills the brand's essence into a few powerful words that stick in customers' minds.

## Context Loading

**Brand Name** (required):
@docs/00-BRAND/00-DISCOVERY/04-brand-name.md

**Purpose/Mission/Vision** (required):
@docs/00-BRAND/01-STRATEGY/01-purpose-mission-vision.md

**Core Values** (optional):
@docs/00-BRAND/01-STRATEGY/02-core-values.md

**Positioning** (required):
@docs/00-BRAND/01-STRATEGY/03-positioning.md

**Archetype** (optional):
@docs/00-BRAND/01-STRATEGY/04-archetype.md

**Brand Voice** (required):
@docs/00-BRAND/01-STRATEGY/05-brand-personality-voice.md

**Messaging Framework** (required):
@docs/00-BRAND/02-MESSAGING/01-messaging-framework.md

**Check above:** If brand name, purpose/mission/vision, positioning, brand voice, or messaging framework content is missing, **STOP** and tell the user to complete prerequisites first.

Optional tagline direction: $ARGUMENTS

## Your Role

**CRITICAL: You MUST use the Task tool to launch the brand-tagline-creator agent.** Do not create taglines yourself — that's what the specialized agent is for.

Your job is to:
1. Verify prerequisites exist
2. Extract key context from loaded documents
3. Prepare a comprehensive, structured prompt for the agent
4. Launch the agent
5. Help founder select from options
6. Save and review the results

## Launch the Agent

**Use Task tool** with `subagent_type: "claude-vibes:BRANDING:brand-tagline-creator"` and this prompt:

```
Create brand tagline options. ultrathink

## BRAND CONTEXT

**Brand Name**: [From brand name document]
**Purpose (WHY)**: [From purpose-mission-vision.md]
**Mission (HOW)**: [From purpose-mission-vision.md]
**Vision (WHERE)**: [From purpose-mission-vision.md]
**Core Values**: [From core-values.md]
**Positioning**: [From positioning.md — the territory we claim]
**Onlyness Statement**: [From positioning.md]
**Voice Traits**: [From brand-personality-voice.md]
**Archetype**: [From archetype.md — primary and secondary]

## VALUE PROPOSITION

**Core Value Proposition**: [From messaging-framework.md]
**Key Benefits**: [From messaging-framework.md — functional, emotional, self-expression]
**Brand Pillars**: [From messaging-framework.md — the key themes]

## FOUNDER CONTEXT

**Founder's Vision**: [From founder brief — what they want to achieve]
**Brands They Admire**: [From founder brief — tagline references]

## COMPETITIVE LANDSCAPE

**Competitor Taglines**: [From competitive audit if exists]
**Tagline Differentiation Opportunity**: [What angles competitors don't own]

## DISCOVERY APPROACH

### Phase 1: Strategic Foundation
Build the positioning foundation before writing:
- Complete the Brand Mantra (3 words: Emotional + Descriptive + Function)
- Write the Trueline (internal positioning truth)
- Identify audience Awareness Level (Schwartz's 5 levels)
- Define what the tagline must communicate, feel, and avoid

### Phase 2: Competitive Analysis
Research the tagline landscape:
- Analyze competitors' taglines (type, approach, gaps)
- Identify white space and differentiation opportunities
- Note overused patterns in this category

### Phase 3: Extensive Brainstorming
Generate options systematically:
- Apply the Distillation Method (USP → cut by half 3x → add device)
- Explore each Tagline Type (Descriptive, Emotional, Aspirational, Imperative, Superlative, Interrogative, Provocative)
- Apply Linguistic Devices (rhyme, alliteration, parallelism, sensory, rhythm)
- Generate 50+ candidates before filtering

### Phase 4: Shortlist and Evaluate
Filter to 5-7 finalists:
- Apply the Onlyness Test to each
- Run Anti-Pattern Check (11 common mistakes)
- Score on Evaluation Matrix (Memorability, Strategic Fit, Emotional Impact, Distinctiveness, Longevity)
- Apply AIDA and ABC tests to top candidates

### Phase 5: Finalize and Test
Prepare recommendation:
- Select top choice with detailed rationale
- Identify runner-up with "when to use instead"
- Create usage guidelines (logo treatment, context usage)
- Document testing protocol

## TOOLS TO USE

- **Sequential Thinking MCP**: Apply the Distillation Method step-by-step, systematically evaluate each option against criteria
- **AskUserQuestion**: Get tagline preferences (type, tone, length), understand emotional direction, validate finalist options
- **WebSearch**: Research competitor taglines and positioning, find famous tagline case studies, discover tagline databases
- **WebFetch**: Read competitor websites to understand their tagline positioning, study famous tagline creation stories for inspiration

## OUTPUT REQUIREMENTS

Deliver the complete tagline documentation using the Tagline Document Template from the `tagline-creation-strategies` skill. Must include:

1. **Strategic Foundation** (onlyness, brand mantra, trueline, awareness level)
2. **Tagline Options** (5-7 options with type, device, rationale, strengths)
3. **Evaluation Matrix** (scoring on 5 criteria)
4. **AIDA Scores** (top 3 candidates)
5. **Anti-Pattern Check** (11 common mistakes filter)
6. **Recommendation** (top choice + runner-up with rationale)
7. **Usage Guidelines** (logo treatment, context usage)
8. **Testing Protocol** (A/B test plan, pre-launch checklist)
9. **Quick Reference Card** (one-page summary)
```

## After Agent Returns

Use AskUserQuestion to help founder select:

"Here are the tagline options. Which resonates most with you?"
- Option A: [tagline] — [brief rationale]
- Option B: [tagline] — [brief rationale]
- Option C: [tagline] — [brief rationale]
- I'd like refinements on one of these
- None of these — try different angles

## Guidelines

- **Ruthlessly short**: If you can cut a word, cut it (aim for 2-4 words)
- **Strategy first**: Pretty words mean nothing without strategic foundation
- **Sound it out**: Taglines must sound good spoken aloud
- **Test for memory**: Can someone remember it after hearing once?
- **Check for ownership**: Could a competitor use this? Then it's not specific enough
- **Consider longevity**: Will this date? Will it work in 10 years?
- Great taglines are simple but not simplistic
- They should work with AND without the brand name
- Avoid clichés and industry jargon
- The "tattoo test": Would a customer feel proud to say it?

## Output

After the founder selects their tagline:

1. Ensure `docs/00-BRAND/02-MESSAGING/` directory exists
2. Save to `docs/00-BRAND/02-MESSAGING/02-tagline.md` with:
   - Selected tagline
   - Strategic rationale
   - Usage guidelines
   - Other finalists (for reference)

3. Use Task tool to launch `claude-vibes:TOOLKIT:ai-writing-detector` agent to review the document for AI patterns and refine if needed.

4. **Next step:** "Run `/00-BRAND:02-messaging/03-write-pitch` to create your elevator pitches."
