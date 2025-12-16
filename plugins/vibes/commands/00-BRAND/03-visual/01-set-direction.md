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
@docs/00-BRAND/00-DISCOVERY/01-founder-brief.md

**Audience Research** (optional):
@docs/00-BRAND/00-DISCOVERY/02-audience-research.md

**Competitive Audit** (required):
@docs/00-BRAND/00-DISCOVERY/03-competitive-audit.md

**Brand Name** (required):
@docs/00-BRAND/00-DISCOVERY/04-brand-name.md

**Purpose/Mission/Vision** (optional):
@docs/00-BRAND/01-STRATEGY/01-purpose-mission-vision.md

**Core Values** (optional):
@docs/00-BRAND/01-STRATEGY/02-core-values.md

**Positioning** (optional):
@docs/00-BRAND/01-STRATEGY/03-positioning.md

**Archetype** (required):
@docs/00-BRAND/01-STRATEGY/04-archetype.md

**Brand Personality/Voice** (required):
@docs/00-BRAND/01-STRATEGY/05-brand-personality-voice.md

**Check above:** If brand name, competitive audit, archetype, or brand personality content is missing, **STOP** and tell the user to complete prerequisites first.

**Messaging Framework** (auto-loaded if exists):
@docs/00-BRAND/02-MESSAGING/01-messaging-framework.md

**Tagline** (auto-loaded if exists):
@docs/00-BRAND/02-MESSAGING/02-tagline.md

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

## Interactive Experience (CRITICAL)

**ALWAYS use the AskUserQuestion tool when interacting with the user.** This ensures a guided, interactive experience where the founder feels engaged and consulted throughout the branding process.

Use AskUserQuestion to:
- Gather preferences before launching agents
- Present options with clear tradeoffs
- Validate agent outputs before saving
- Get feedback and iterate on results

Never save final outputs without user approval.

## Human-Sounding Writing Protocol

**BEFORE launching the brand-visual-director agent, you MUST:**

1. **Use the Skill tool** to invoke `claude-vibes:ai-writing-detection`
   - This loads expert-level knowledge of AI writing patterns to avoid

2. **Use the Sequential Thinking MCP tool (ultrathink)** to prepare AI-aware instructions:
   - Review vocabulary patterns to avoid: "delve", "tapestry", "multifaceted", "leverage", "crucial", "comprehensive", "foster", "harness", "navigate", "landscape", "realm", "beacon", "pivotal"
   - Review phrases to avoid: "It's important to note", "In today's fast-paced world", "At its core", "Let me explain"
   - Review structural patterns to avoid: uniform sentence lengths, excessive tricolons, em dash overuse

3. **Include AI-aware instructions** in the agent prompt so output is human-sounding from the start

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

## CRITICAL: INTERACTIVE DISCOVERY

**ALWAYS use the AskUserQuestion tool to ensure an interactive, guided experience:**
- Gather preferences and opinions before making recommendations
- Present options with clear tradeoffs for the user to choose from
- Validate findings and get feedback before proceeding
- Confirm final outputs resonate before saving

Never make significant decisions without user input. The brand identity belongs to them.

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

1. Ensure `docs/00-BRAND/03-VISUAL/` directory exists
2. Save to `docs/00-BRAND/03-VISUAL/01-visual-direction.md` with:
   - Executive summary
   - Strategic foundation
   - Mood board direction
   - Logo design brief
   - Photography style
   - Visual system overview

3. **Next step:** "Run `/00-BRAND:03-visual/02-choose-colors` to develop your brand color palette."
