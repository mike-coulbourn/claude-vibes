---
description: Define brand personality and voice guidelines
argument-hint: Optional voice direction (e.g., "friendly but authoritative")
allowed-tools: Read, Glob, Grep, Task, Write, Edit, WebSearch, WebFetch, AskUserQuestion
---

# Define Brand Voice

You are helping a startup founder define their brand personality and voice. This creates the guidelines for how the brand "speaks" — ensuring consistency across all communications.

## Context Loading

**Founder Brief** (optional):
@docs/00-BRAND/00-DISCOVERY/01-founder-brief.md

**Audience Research** (required):
@docs/00-BRAND/00-DISCOVERY/02-audience-research.md

**Competitive Audit** (optional):
@docs/00-BRAND/00-DISCOVERY/03-competitive-audit.md

**Brand Name** (optional):
@docs/00-BRAND/00-DISCOVERY/04-brand-name.md

**Purpose/Mission/Vision** (optional):
@docs/00-BRAND/01-STRATEGY/01-purpose-mission-vision.md

**Core Values** (optional):
@docs/00-BRAND/01-STRATEGY/02-core-values.md

**Positioning** (optional):
@docs/00-BRAND/01-STRATEGY/03-positioning.md

**Archetype** (required):
@docs/00-BRAND/01-STRATEGY/04-archetype.md

**Check above:** If audience research or archetype content is missing, **STOP** and tell the user to complete prerequisites first.

Optional voice direction: $ARGUMENTS

## Your Role

**CRITICAL: You MUST use the Task tool to launch the brand-voice-architect agent.** Do not create voice guidelines yourself — that's what the specialized agent is for.

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

**BEFORE launching the brand-voice-architect agent, you MUST:**

1. **Use the Skill tool** to invoke `claude-vibes:ai-writing-detection`
   - This loads expert-level knowledge of AI writing patterns to avoid

2. **Use the Sequential Thinking MCP tool (ultrathink)** to prepare AI-aware instructions:
   - Review vocabulary patterns to avoid: "delve", "tapestry", "multifaceted", "leverage", "crucial", "comprehensive", "foster", "harness", "navigate", "landscape", "realm", "beacon", "pivotal"
   - Review phrases to avoid: "It's important to note", "In today's fast-paced world", "At its core", "Let me explain"
   - Review structural patterns to avoid: uniform sentence lengths, excessive tricolons, em dash overuse

3. **Include AI-aware instructions** in the agent prompt so output is human-sounding from the start

## Launch the Agent

**Use Task tool** with `subagent_type: "claude-vibes:BRANDING:brand-voice-architect"` and this prompt:

```
Define the brand personality and voice. ultrathink

## BRAND CONTEXT

**Brand Name**: [From brand name document]
**Purpose (WHY)**: [From purpose-mission-vision.md]
**Core Values**: [From core-values.md]
**Positioning**: [From positioning.md — the territory we claim]
**Primary Archetype**: [From archetype.md — include motto]
**Secondary Archetype**: [From archetype.md — include motto]

## AUDIENCE INSIGHTS

**Who They Serve**: [From audience research — primary customer segment]
**Audience Language**: [From audience research — how they talk]
**Audience Expectations**: [What they expect from brands in this space]
**Emotional Jobs**: [From audience research — how they want to feel]

## FOUNDER CONTEXT

**Founder Communication Style**: [From founder brief — how they naturally communicate]
**Brands They Admire**: [From founder brief — voice references]

## CRITICAL: INTERACTIVE DISCOVERY

**ALWAYS use the AskUserQuestion tool to ensure an interactive, guided experience:**
- Gather preferences and opinions before making recommendations
- Present options with clear tradeoffs for the user to choose from
- Validate findings and get feedback before proceeding
- Confirm final outputs resonate before saving

Never make significant decisions without user input. The brand identity belongs to them.

## COMPETITIVE VOICE LANDSCAPE

**Competitor Voice Patterns**: [From competitive audit — how competitors sound]
**Voice Differentiation Opportunity**: [Where we can stand out through voice]

## DISCOVERY APPROACH

### Phase 1: Synthesize Brand Inputs
Analyze how purpose, values, archetype, and positioning should influence voice:
- What does the archetype suggest about voice?
- How do values translate to voice qualities?
- What positioning territory should voice claim?
- How should audience expectations shape voice?

### Phase 2: Apply Voice Discovery Methods
Use established frameworks:
- **BrandSort methodology**: Which attributes define this voice?
- **NNGroup Four Dimensions**: Plot position on each spectrum
- **Aaker Personality Dimensions**: Which dimensions apply?
- **"This But Not That" technique**: Add constraints to each trait

### Phase 3: Define Personality Traits
Select 3-5 specific personality traits:
- Clear definition for this brand
- "This but not that" constraint
- Concrete do/don't examples
- Sample phrases that demonstrate each trait

### Phase 4: Create Tone Adaptation Framework
Document how voice flexes:
- By channel (social, support, marketing, product UI, formal)
- By emotional state (happy, confused, frustrated, anxious)
- Boundaries: how far can tone flex before breaking voice?

### Phase 5: Build Comprehensive Guidelines
Create actionable documentation:
- Complete verbal identity components
- Vocabulary guidelines (words to use/avoid)
- Verbal distinctive assets (ownable phrases, signature words)
- Before/after examples
- AI-ready voice guidelines

## TOOLS TO USE

- **Sequential Thinking MCP**: Systematically translate archetype and positioning into specific voice qualities, evaluate each personality trait against brand context
- **AskUserQuestion**: Validate voice traits resonate with founder's natural style, get input on tone preferences, confirm "this but not that" constraints feel right
- **WebSearch**: Research exemplar brand voice guides (Mailchimp, Slack, Monzo), find voice examples in this industry, study how leading brands document voice
- **WebFetch**: Read actual style guides and voice documentation — study Mailchimp's Content Style Guide, Slack's voice principles, 18F Content Guide for structure and approach

## OUTPUT REQUIREMENTS

Deliver the complete voice documentation using the Voice Guidelines Document Template from the `brand-voice-development` skill. Must include:

1. **Executive Summary**
2. **Voice Foundation** (brand context, one-sentence voice description, NNGroup four dimensions)
3. **Brand Personality Traits** (3-5 traits with "this but not that" constraints)
4. **Voice Characteristics** (we sound like / we don't sound like)
5. **Tone Variations** (by channel and emotional state with examples)
6. **Vocabulary Guidelines** (words to use, words to avoid, jargon policy)
7. **Verbal Distinctive Assets** (ownable phrases, signature words)
8. **Writing Style** (sentence structure, punctuation personality)
9. **Voice in Action** (before/after examples, sample content pieces)
10. **AI Voice Guidelines** (prompts, human review checklist)
11. **Voice Summary Card** (quick reference for daily use)
```

## Guidelines

- **Voice should feel natural, not performed** — if it feels forced, it's wrong
- **Include concrete examples** — "We say X, not Y" is more useful than abstract descriptions
- **Tone varies by context, but voice stays consistent** — same personality, different volume
- **The "airport test"** — would someone recognize this brand's writing if they found it on the floor?
- **Voice must connect to archetype** — the archetype provides the emotional foundation
- **Prepare for AI** — create guidelines that work for both human and AI writers
- **Test the usability** — can someone unfamiliar with the brand write in this voice using these guidelines?

## Output

After the agent returns:

1. Ensure `docs/00-BRAND/01-STRATEGY/` directory exists
2. Save to `docs/00-BRAND/01-STRATEGY/05-brand-personality-voice.md`

3. **Next step:** "Strategy phase complete! Run `/00-BRAND:02-messaging/01-create-framework` to begin building your brand messaging."
