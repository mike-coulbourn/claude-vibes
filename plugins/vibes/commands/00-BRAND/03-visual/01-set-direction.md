---
description: Create visual identity direction and logo brief
argument-hint: Optional visual style preferences
allowed-tools: Read, Glob, Grep, Task, Write, Edit, WebSearch, WebFetch, AskUserQuestion
---

# Set Visual Direction

You are helping a startup founder establish the visual direction for their brand. This creates the creative brief for designers — mood board direction, logo brief, and overall visual system guidelines.

**Note:** Claude provides detailed creative direction for visual identity, but not actual designs. The outputs are briefs for a designer or specifications for DIY implementation.

## Context Loading

**Founder Brief** (optional):
@docs/brand/00-discovery/01-founder-brief.md

**Audience Research** (optional):
@docs/brand/00-discovery/02-audience-research.md

**Competitive Audit** (required):
@docs/brand/00-discovery/03-competitive-audit.md

**Brand Name** (required):
@docs/brand/00-discovery/04-brand-name.md

**Purpose/Mission/Vision** (optional):
@docs/brand/01-strategy/01-purpose-mission-vision.md

**Core Values** (optional):
@docs/brand/01-strategy/02-core-values.md

**Positioning** (optional):
@docs/brand/01-strategy/03-positioning.md

**Archetype** (required):
@docs/brand/01-strategy/04-archetype.md

**Brand Personality/Voice** (required):
@docs/brand/01-strategy/05-brand-personality-voice.md

**Check above:** If brand name, competitive audit, archetype, or brand personality content is missing, **STOP** and tell the user to complete prerequisites first.

**Messaging Framework** (auto-loaded if exists):
@docs/brand/02-messaging/01-messaging-framework.md

**Tagline** (auto-loaded if exists):
@docs/brand/02-messaging/02-tagline.md

Optional visual preferences: $ARGUMENTS

## Your Role

**CRITICAL: You MUST use the Task tool to launch the brand-visual-director agent.** Do not create visual direction yourself — that's what the specialized agent is for.

Your job is to:
1. Verify prerequisites exist
2. Extract key context from loaded documents
3. Prepare a comprehensive, structured prompt for the agent
4. Launch the agent
5. Help founder review and refine
6. Save and review the results

## Launch the Agent

**Use Task tool** with `subagent_type: "claude-vibes:BRANDING:brand-visual-director"` and this prompt:

```
Create the visual identity direction for this brand. ultrathink

## BRAND CONTEXT

**Brand Name**: [From brand name document]
**Purpose (WHY)**: [From purpose-mission-vision.md]
**Mission (HOW)**: [From purpose-mission-vision.md]
**Vision (WHERE)**: [From purpose-mission-vision.md]
**Core Values**: [From core-values.md]
**Positioning**: [From positioning.md — the territory we claim]
**Onlyness Statement**: [From positioning.md]
**Tagline**: [From tagline.md — if available]

## BRAND PERSONALITY

**Archetype**: [From archetype.md — primary and secondary]
**Personality Traits**: [From brand-personality-voice.md — the 5 traits]
**Voice Characteristics**: [From brand-personality-voice.md]
**Brand Essence**: [From brand-personality-voice.md — 2-3 words]

## AUDIENCE INSIGHTS

**Who They Serve**: [From audience research — primary customer segment]
**Audience Demographics**: [From audience research — age, location, etc.]
**Visual Expectations**: [From audience research — what they expect visually]
**Aspirational Brands**: [From audience research — brands they admire]

## COMPETITIVE LANDSCAPE

**Competitor Visual Styles**: [From competitive audit — how competitors look]
**Visual Patterns to Avoid**: [From competitive audit — overused approaches]
**Visual White Space**: [From competitive audit — opportunities to differentiate]

## PRACTICAL CONSTRAINTS

**Design Budget**: [From founder brief — budget for design]
**Existing Elements**: [From founder brief — any existing visuals]
**Must-Haves/Must-Avoids**: [From founder brief — visual constraints]
**Timeline**: [From founder brief — urgency]

## DISCOVERY APPROACH

### Phase 1: Synthesize Brand Strategy
Extract from inputs:
- Purpose → What the brand stands for (visual soul)
- Values → Principles that guide visual choices
- Positioning → Territory that visuals must claim
- Archetype → Emotional foundation of visual expression
- Personality → Traits that translate to visual qualities
- Competitive landscape → What to differentiate from

### Phase 2: Commit to Words
Before any visual exploration:
- Define 3-5 brand adjectives
- Create Visual Word Translation for each adjective
- Create Single-Minded Proposition for visual identity
- Identify the "3 words" that capture the overall aesthetic

### Phase 3: Translate Strategy to Visual Language
For each personality trait and archetype quality:
- Define visual expression using archetype visual language
- Apply Visual Word Translation table
- Create mood board direction with strategic rationale

### Phase 4: Create Comprehensive Direction
Build detailed briefs for each visual component:
- Mood board direction (overall aesthetic, textures, emotional qualities)
- Logo design brief (style, conceptual directions, technical requirements)
- Photography style (lighting, composition, color treatment, people)
- Typography direction (personality, category, selection criteria)
- Color strategy (palette structure, psychological rationale)
- Supporting elements (icons, patterns, graphic devices)

### Phase 5: Establish System Governance
- Define what stays constant vs. what can vary
- Create hierarchy of visual elements
- List application priorities
- Document design principles checklist

## TOOLS TO USE

- **Sequential Thinking MCP**: Apply Strategy to Visual Translation Method step-by-step, systematically translate brand adjectives to visual expressions
- **AskUserQuestion**: Understand visual preferences, validate aesthetic directions, get feedback on mood board concepts
- **WebSearch**: Research competitor websites visually, find brand case studies, discover design agency portfolios, find photography style references
- **WebFetch**: Read brand case study pages, study design portfolio writeups, analyze famous brand identity projects for strategic rationale

## OUTPUT REQUIREMENTS

Deliver the complete visual identity direction using the Visual Identity Direction Document Template from the `visual-identity-direction` skill. Must include:

1. **Executive Summary** (3 words + overview)
2. **Single-Minded Proposition** (visual SMP + translation)
3. **Strategic Foundation** (brand inputs, visual word translation, archetype visual language, positioning map, competitive landscape)
4. **Mood Board Direction** (overall aesthetic, references, textures, emotional qualities)
5. **Logo Design Brief** (strategy, style, conceptual directions, technical requirements, what to avoid)
6. **Photography/Imagery Style** (direction, composition, lighting, color, people, do's/don'ts)
7. **Illustration Style** (if applicable)
8. **Supporting Visual Elements** (graphic devices, iconography)
9. **Visual System Overview** (hierarchy, flexibility, application priorities, design principles)
10. **Designer Briefing Summary** (assignment, success criteria, questions)
```

## After Agent Returns

Use AskUserQuestion to help founder review and select:

"Here's your visual identity direction. How would you like to proceed?"
- This direction feels right — let's proceed
- I'd like to explore a different aesthetic direction
- I want to refine specific sections (logo, photography, etc.)
- I have questions about the recommendations
- Let's discuss with my team before finalizing

## Guidelines

- **Visual direction must connect back to brand strategy** — every choice has rationale
- **Be specific enough that a designer could work from this** — not vague descriptions
- **Consider the founder's budget and constraints** — practical recommendations
- **Balance aspiration with practicality** — aspirational but achievable
- **Strategy drives design** — commit to words first, then visuals
- **Mood boards before detail** — align on direction before detailed design
- **Think in systems** — coherent visual language, not one-off designs
- **Differentiate visually** — use competitive audit to find white space

## Output

After the founder approves the direction:

1. Ensure `docs/brand/03-visual/` directory exists
2. Save to `docs/brand/03-visual/01-visual-direction.md` with:
   - Executive summary
   - Strategic foundation
   - Mood board direction
   - Logo design brief
   - Photography style
   - Visual system overview

3. Use Task tool to launch `claude-vibes:TOOLKIT:ai-writing-detector` agent to review the document for AI patterns and refine if needed.

4. **Next step:** "Run `/00-BRAND:03-visual/02-choose-colors` to develop your brand color palette."
