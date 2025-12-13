---
description: Write elevator pitch variations for different contexts
argument-hint: Optional pitch context or audience focus
allowed-tools: Read, Glob, Grep, Task, Write, Edit, WebSearch, WebFetch, AskUserQuestion
---

# Write Elevator Pitches

You are helping a startup founder create elevator pitches for different situations. These are verbal summaries that sound natural when spoken — not marketing copy read aloud.

## Prerequisites Check

**Brand name status:** !`test -f docs/brand/00-discovery/04-brand-name.md && echo "✓ Found" || echo "✗ MISSING - Run /00-BRAND:00-discover/04-create-name first"`

**Purpose/Mission/Vision status:** !`test -f docs/brand/01-strategy/01-purpose-mission-vision.md && echo "✓ Found" || echo "✗ MISSING - Run /00-BRAND:01-strategy/01-define-purpose first"`

**Positioning status:** !`test -f docs/brand/01-strategy/03-positioning.md && echo "✓ Found" || echo "✗ MISSING - Run /00-BRAND:01-strategy/03-define-positioning first"`

**Brand voice status:** !`test -f docs/brand/01-strategy/05-brand-personality-voice.md && echo "✓ Found" || echo "✗ MISSING - Run /00-BRAND:01-strategy/05-define-voice first"`

**Messaging framework status:** !`test -f docs/brand/02-messaging/01-messaging-framework.md && echo "✓ Found" || echo "✗ MISSING - Run /00-BRAND:02-messaging/01-create-framework first"`

If required files are missing, **STOP** and tell the user to complete prerequisites first.

## Context Loading

**Founder Brief** (auto-loaded if exists):
@docs/brand/00-discovery/01-founder-brief.md

**Audience Research** (auto-loaded if exists):
@docs/brand/00-discovery/02-audience-research.md

**Brand Name** (auto-loaded - REQUIRED):
@docs/brand/00-discovery/04-brand-name.md

**Purpose/Mission/Vision** (auto-loaded - REQUIRED):
@docs/brand/01-strategy/01-purpose-mission-vision.md

**Core Values** (auto-loaded if exists):
@docs/brand/01-strategy/02-core-values.md

**Positioning** (auto-loaded - REQUIRED):
@docs/brand/01-strategy/03-positioning.md

**Brand Voice** (auto-loaded - REQUIRED):
@docs/brand/01-strategy/05-brand-personality-voice.md

**Messaging Framework** (auto-loaded - REQUIRED):
@docs/brand/02-messaging/01-messaging-framework.md

**Tagline** (auto-loaded if exists):
@docs/brand/02-messaging/02-tagline.md

Optional pitch context: $ARGUMENTS

## Your Role

**CRITICAL: You MUST use the Task tool to launch the brand-elevator-pitch-writer agent.** Do not write pitches yourself — that's what the specialized agent is for.

Your job is to:
1. Verify prerequisites exist
2. Extract key context from loaded documents
3. Prepare a comprehensive, structured prompt for the agent
4. Launch the agent
5. Help founder practice and refine
6. Save and review the results

## Launch the Agent

**Use Task tool** with `subagent_type: "claude-vibes:BRANDING:brand-elevator-pitch-writer"` and this prompt:

```
Create the brand elevator pitch variations. ultrathink

## BRAND CONTEXT

**Brand Name**: [From brand name document]
**Purpose (WHY)**: [From purpose-mission-vision.md]
**Mission (HOW)**: [From purpose-mission-vision.md]
**Vision (WHERE)**: [From purpose-mission-vision.md]
**Core Values**: [From core-values.md]
**Positioning**: [From positioning.md — the territory we claim]
**Onlyness Statement**: [From positioning.md]
**Tagline**: [From tagline.md — if available]
**Voice Traits**: [From brand-personality-voice.md]

## VALUE PROPOSITION

**Core Value Proposition**: [From messaging-framework.md]
**Key Benefits**: [From messaging-framework.md — functional, emotional, self-expression]
**Brand Pillars**: [From messaging-framework.md — the key themes]

## AUDIENCE INSIGHTS

**Who They Serve**: [From audience research — primary customer segment]
**Customer Problem**: [From audience research — main pain point]
**Customer Language**: [From audience research — how they talk about the problem]
**Desired Outcome**: [From audience research — what they want]

## FOUNDER CONTEXT

**Founder Story**: [From founder brief — personal connection to the problem]
**Origin Moment**: [From founder brief — the catalyst for starting]
**Founder Vision**: [From founder brief — where they want to go]

## DISCOVERY APPROACH

### Phase 1: Synthesize Brand Inputs
Analyze all inputs to understand:
- How purpose, values, and positioning should inform pitch
- What makes this brand the "only" one
- What the audience cares about most
- How the brand voice should sound when spoken

### Phase 2: Select Primary Framework
Choose the primary framework based on brand needs:
- **StoryBrand (SB7)** — When customer transformation is central
- **Golden Circle** — When purpose is the differentiator
- **Onlyness** — When category position is key
- **Strategic Narrative** — When there's a big industry shift to leverage
- **Sparkline** — When contrast between current/future state is powerful
- **CLARITY** — When authenticity and audience connection are priorities

### Phase 3: Craft Time-Based Variations
Create pitches for different durations:

**ONE-LINER (10 seconds):**
- The briefest way to explain what you do
- For "What do you do?" moments
- Creates intrigue, not explanation

**ELEVATOR PITCH (30 seconds):**
- Hook → Problem → Solution → Differentiation → Interest Close
- Natural flow, conversational pace
- Include S.T.A.R. moment (Something They'll Always Remember)

**EXTENDED PITCH (60 seconds):**
- Adds: proof points, traction, deeper story
- For interested audiences who want more

**FOUNDER STORY PITCH (when founder background is relevant):**
- Weaves personal story with business
- Use when authenticity matters most

### Phase 4: Add Delivery Guidance
For each pitch, include:
- Pace and emphasis guidance
- Strategic pause moments
- Tone recommendations
- Natural pause points
- The 3 C's check (Clarity, Conciseness, Confidence)

### Phase 5: Prepare for Success
Document:
- 3+ Hook options using different hook types
- CTA options by context (meetings, demo, connection)
- Common follow-up questions to prepare for
- 7-day testing and iteration framework

## TOOLS TO USE

- **Sequential Thinking MCP**: Structure pitch flow systematically, ensure natural speech rhythm, evaluate hook options
- **AskUserQuestion**: Understand pitch contexts, validate pitches feel natural to say, get feedback on hook preferences
- **WebSearch**: Research competitor pitch examples, find industry pitch patterns, discover memorable brand intros
- **WebFetch**: Study competitor landing page language for pitch inspiration, analyze famous pitch breakdowns

## OUTPUT REQUIREMENTS

Deliver the complete pitch documentation using the Elevator Pitch Document Template from the `elevator-pitch-techniques` skill. Must include:

1. **Executive Summary** (primary pitch, one-liner, framework)
2. **Strategic Foundation** (inputs, Onlyness, framework selection, pitch challenge)
3. **One-Liner** (pitch, hook type, delivery notes, alternatives)
4. **30-Second Elevator Pitch** (pitch, What Is/Could Be, structure breakdown, S.T.A.R. moment, delivery notes, follow-up prep)
5. **60-Second Extended Pitch** (pitch, structure, what it adds, when to use)
6. **Founder Story Pitch** (if relevant — story elements, when stronger)
7. **Hook Options** (3+ from different types with contexts)
8. **CTA Options** (meetings, demo, connection)
9. **Context Variations** (networking, investor, customer, press, social)
10. **Testing Checklist** (7-day iteration plan, readiness signs)
11. **Quick Reference Card** (one-page summary)
```

## After Agent Returns

Use AskUserQuestion to help founder practice and select:

"Here are your elevator pitches. Let's make sure they feel natural. Which would you like to focus on?"
- The one-liner — practice the quickest version first
- The 30-second pitch — the core elevator pitch
- The 60-second pitch — the extended version
- The founder story — when your background matters
- I'd like to practice all of them
- I want refinements on one of these

## Guidelines

- **These must sound natural SPOKEN** — read them aloud
- **Avoid marketing jargon** that sounds awkward verbally
- **Include natural pause points** — silence is powerful
- **The founder should feel comfortable** saying these
- **Test: Can the founder deliver this without reading?**
- **Goal is "Tell me more"** — not closing a deal
- **Customer is the hero** — brand is the guide
- **Clarity over cleverness** — if they don't understand, it failed

## Output

After the founder selects their pitches:

1. Ensure `docs/brand/02-messaging/` directory exists
2. Save to `docs/brand/02-messaging/03-elevator-pitch.md` with:
   - All pitch variations
   - Strategic foundation
   - Delivery guidance
   - Hook options
   - Testing framework

3. Use Task tool to launch `claude-vibes:TOOLKIT:ai-writing-detector` agent to review the document for AI patterns and refine if needed.

4. **Next step:** "Messaging phase complete! Run `/00-BRAND:03-visual/01-set-direction` to begin visual identity direction."
