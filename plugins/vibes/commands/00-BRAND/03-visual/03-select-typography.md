---
description: Develop brand typography system with font recommendations
argument-hint: Optional typography preferences or constraints (e.g., "free fonts only")
allowed-tools: Read, Glob, Grep, Task, Write, Edit, WebSearch, WebFetch, AskUserQuestion
---

# Select Brand Typography

You are helping a startup founder develop their brand typography system. This includes selecting typefaces, creating a typography hierarchy, and establishing usage guidelines that express brand personality through type.

**Note:** Typography is voice made visible. The right typefaces, used consistently, make a brand feel cohesive and intentional.

## Context Loading

**Founder Brief** (optional):
@docs/brand/00-discovery/01-founder-brief.md

**Audience Research** (optional):
@docs/brand/00-discovery/02-audience-research.md

**Brand Name** (required):
@docs/brand/00-discovery/04-brand-name.md

**Purpose/Mission/Vision** (optional):
@docs/brand/01-strategy/01-purpose-mission-vision.md

**Core Values** (optional):
@docs/brand/01-strategy/02-core-values.md

**Positioning** (optional):
@docs/brand/01-strategy/03-positioning.md

**Archetype** (optional):
@docs/brand/01-strategy/04-archetype.md

**Brand Personality/Voice** (required):
@docs/brand/01-strategy/05-brand-personality-voice.md

**Visual Direction** (required):
@docs/brand/03-visual/01-visual-direction.md

**Color Palette** (optional):
@docs/brand/03-visual/02-color-palette.md

**Check above:** If brand name, brand personality, or visual direction content is missing, **STOP** and tell the user to complete prerequisites first.

Optional typography preferences: $ARGUMENTS

## Your Role

**CRITICAL: You MUST use the Task tool to launch the brand-typography-curator agent.** Do not select typography yourself — that's what the specialized agent is for.

Your job is to:
1. Verify prerequisites exist
2. Extract key context from loaded documents
3. Prepare a comprehensive, structured prompt for the agent
4. Launch the agent
5. Help founder review and validate
6. Save and review the results

## Launch the Agent

**Use Task tool** with `subagent_type: "claude-vibes:BRANDING:brand-typography-curator"` and this prompt:

```
Develop the brand typography system. ultrathink

## BRAND CONTEXT

**Brand Name**: [From brand name document]
**Purpose (WHY)**: [From purpose-mission-vision.md]
**Mission (HOW)**: [From purpose-mission-vision.md]
**Vision (WHERE)**: [From purpose-mission-vision.md]
**Core Values**: [From core-values.md]
**Positioning**: [From positioning.md — the territory we claim]
**Onlyness Statement**: [From positioning.md]

## BRAND PERSONALITY

**Archetype**: [From archetype.md — primary and secondary]
**Personality Traits**: [From brand-personality-voice.md — the 5 traits]
**Voice Characteristics**: [From brand-personality-voice.md]
**Brand Essence**: [From brand-personality-voice.md — 2-3 words]

## VISUAL DIRECTION

**Visual Adjectives**: [From visual-direction.md — the 3-5 visual words]
**Mood Board Direction**: [From visual-direction.md — overall aesthetic]
**Visual SMP**: [From visual-direction.md — single-minded proposition]

## AUDIENCE INSIGHTS

**Who They Serve**: [From audience research — primary customer segment]
**Audience Demographics**: [From audience research — age, location, etc.]
**Typography Expectations**: [From audience research — what they expect visually]
**Aspirational Brands**: [From audience research — brands they admire]

## COLOR PALETTE (if available)

**Primary Colors**: [From color-palette.md — for text color alignment]
**Text Colors**: [From color-palette.md — existing dark/light neutrals]

## PRACTICAL CONSTRAINTS

**Design Budget**: [From founder brief — budget for design]
**Existing Elements**: [From founder brief — any existing fonts]
**Typography Preferences/Avoids**: [From founder brief or $ARGUMENTS — constraints]
**Primary Touchpoints**: [From founder brief — web, print, app]
**Free Fonts Required?**: [From $ARGUMENTS or inferred from budget]

## DISCOVERY APPROACH

### Phase 1: Analyze Brand Strategy
Extract from inputs:
- Personality → Traits that translate to type qualities
- Voice → How type should "sound"
- Archetype → Type mood and emotional foundation
- Positioning → Type style that claims this territory
- Visual Direction → Aesthetic alignment

### Phase 2: Establish Classification Direction
Apply Serif vs. Sans-Serif Decision Framework:
- Assess industry expectations
- Evaluate touchpoint distribution (digital vs. print)
- Consider brand positioning (traditional vs. modern)
- Make primary classification decision with rationale

### Phase 3: Build Modular Scale
Using modular scale principles:
- Define base size (16px for web)
- Select ratio based on personality and content type
- Calculate 6-8 distinct sizes
- Map to hierarchy levels (H1-H6, body, captions)
- Consider responsive adjustments

### Phase 4: Research and Select Typefaces
Apply Typeface Evaluation Criteria:
- Assess comprehensiveness, legibility, versatility
- Evaluate complementarity with brand elements
- Check distinctiveness vs. competitors
- Verify technical readiness (web fonts, licensing, variable font)

### Phase 5: Define Pairing Strategy
Apply Font Pairing Principles:
- Seek contrast through classification
- Ensure meaningful hierarchy distinction
- Look for shared characteristics (x-height, era)
- Test in real content contexts

### Phase 6: Build Typography System
Document complete hierarchy:
- All hierarchy levels with specifications
- Line height, tracking, line length guidelines
- Design tokens for implementation
- Usage guidelines (do's and don'ts)
- Cross-channel adaptations (web, print, email)
- Accessibility requirements

## TOOLS TO USE

- **Sequential Thinking MCP**: Match brand personality to type qualities, build modular scale systematically, evaluate typeface candidates against criteria
- **AskUserQuestion**: Understand typography constraints (free fonts needed? existing fonts?), validate classification direction, get feedback on typeface options
- **WebSearch**: Discover font pairing guides, typography resources (Google Fonts, Adobe Fonts), competitor typography, brand typography examples
- **WebFetch**: Read typography guides, font pairing articles, foundry pages — understand pairing rationale and access font specimen details

## OUTPUT REQUIREMENTS

Deliver the complete typography system using the Typography System Documentation Template from the `brand-typography-systems` skill. Must include:

1. **Executive Summary** (2-3 sentences on typefaces and personality expression)
2. **Strategic Foundation** (brand inputs, personality match, classification decision)
3. **Modular Scale** (base, ratio, calculated sizes, hierarchy mapping)
4. **Primary Typeface** (headlines — with source, rationale, evaluation, weights)
5. **Secondary Typeface** (body — with pairing rationale, readability notes)
6. **Tertiary Typeface** (optional — accent use only)
7. **Typography Hierarchy** (complete H1-H6, body, captions with specs)
8. **Typography Design Tokens** (CSS custom properties)
9. **Font Pairing Rationale** (how fonts work together)
10. **Web-Safe Fallbacks** (font stacks)
11. **Usage Guidelines** (do's and don'ts)
12. **Accessibility Verification** (sizes, contrast, dyslexia-friendly)
13. **Font Licensing Summary** (license types, sources, restrictions)
14. **Quick Reference Card** (essential specs)
```

## After Agent Returns

Use AskUserQuestion to help founder review and validate:

"Here's your brand typography system. How would you like to proceed?"
- This typography feels right — let's proceed
- I'd like to explore different typeface options
- I want to refine specific elements (primary font, body font, hierarchy)
- I have questions about the recommendations
- Let's test the fonts in real mockups first
- I need to discuss with my team before finalizing

## Guidelines

- **Typography must express brand personality** — start with personality, select to match
- **Be specific** — exact sizes, weights, spacing, not vague descriptions
- **Consider budget constraints** — free fonts (Google Fonts) vs. paid
- **Ensure fonts work well together** — contrast through classification
- **Include web-safe fallbacks** — for when fonts don't load
- **Think in systems** — typography that scales across all applications
- **Prioritize readability** — beautiful but illegible type fails
- **Test accessibility** — WCAG contrast, minimum sizes, dyslexia-friendly
- **Document licensing** — verify all use cases are covered

## Output

After the founder approves the typography:

1. Ensure `docs/brand/03-visual/` directory exists
2. Save to `docs/brand/03-visual/03-typography.md` with:
   - Executive summary
   - Strategic foundation
   - Modular scale
   - Primary and secondary typefaces
   - Complete hierarchy
   - Design tokens
   - Usage guidelines
   - Accessibility verification
   - Quick reference

3. Use Task tool to launch `claude-vibes:TOOLKIT:ai-writing-detector` agent to review the document for AI patterns and refine if needed.

4. **Next step:** "Visual phase complete! Run `/00-BRAND:04-compile/01-compile-guidelines` to create your final brand guidelines document."
