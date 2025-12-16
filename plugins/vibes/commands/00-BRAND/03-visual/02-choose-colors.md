---
description: Develop brand color palette with exact specifications
argument-hint: Optional color preferences or constraints
allowed-tools: Read, Glob, Grep, Task, Write, Edit, WebSearch, WebFetch, AskUserQuestion
---

# Choose Brand Colors

You are helping a startup founder develop their brand color palette. This includes primary colors, secondary colors, neutrals, and accent colors — all with exact specifications and usage guidelines.

**Note:** Color is one of the most powerful brand tools — research shows 62-90% of snap judgments about products are based on color alone.

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

**Visual Direction** (required):
@docs/00-BRAND/03-VISUAL/01-visual-direction.md

**Check above:** If brand name, competitive audit, archetype, brand personality, or visual direction content is missing, **STOP** and tell the user to complete prerequisites first.

Optional color preferences: $ARGUMENTS

## Your Role

**CRITICAL: You MUST use the Task tool to launch the brand-color-strategist agent.** Do not create color palettes yourself — that's what the specialized agent is for.

Your job is to:
1. Verify prerequisites exist
2. Extract key context from loaded documents
3. Prepare a comprehensive, structured prompt for the agent
4. Launch the agent
5. Help founder review and validate
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

**BEFORE launching the brand-color-strategist agent, you MUST:**

1. **Use the Skill tool** to invoke `claude-vibes:ai-writing-detection`
   - This loads expert-level knowledge of AI writing patterns to avoid

2. **Use the Sequential Thinking MCP tool (ultrathink)** to prepare AI-aware instructions:
   - Review vocabulary patterns to avoid: "delve", "tapestry", "multifaceted", "leverage", "crucial", "comprehensive", "foster", "harness", "navigate", "landscape", "realm", "beacon", "pivotal"
   - Review phrases to avoid: "It's important to note", "In today's fast-paced world", "At its core", "Let me explain"
   - Review structural patterns to avoid: uniform sentence lengths, excessive tricolons, em dash overuse

3. **Include AI-aware instructions** in the agent prompt so output is human-sounding from the start

## Launch the Agent

**Use Task tool** with `subagent_type: "claude-vibes:BRANDING:brand-color-strategist"` and this prompt:

```
Develop the brand color palette. ultrathink

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
**Brand Essence**: [From brand-personality-voice.md — 2-3 words]

## VISUAL DIRECTION

**Visual Adjectives**: [From visual-direction.md — the 3-5 visual words]
**Mood Board Direction**: [From visual-direction.md — overall aesthetic]
**Visual SMP**: [From visual-direction.md — single-minded proposition]

## AUDIENCE INSIGHTS

**Who They Serve**: [From audience research — primary customer segment]
**Audience Demographics**: [From audience research — age, location, etc.]
**Color Expectations**: [From audience research — what they expect visually]
**Aspirational Brands**: [From audience research — brands they admire]

## COMPETITIVE LANDSCAPE

**Competitor Colors**: [From competitive audit — what colors competitors use]
**Dominant Category Colors**: [From competitive audit — industry patterns]
**Color White Space**: [From competitive audit — opportunities to differentiate]

## PRACTICAL CONSTRAINTS

**Design Budget**: [From founder brief — budget for design]
**Existing Elements**: [From founder brief — any existing colors/visuals]
**Color Preferences/Avoids**: [From founder brief or $ARGUMENTS — constraints]
**Target Markets**: [From founder brief — cultural considerations needed]

## CRITICAL: INTERACTIVE DISCOVERY

**ALWAYS use the AskUserQuestion tool to ensure an interactive, guided experience:**
- Gather preferences and opinions before making recommendations
- Present options with clear tradeoffs for the user to choose from
- Validate findings and get feedback before proceeding
- Confirm final outputs resonate before saving

Never make significant decisions without user input. The brand identity belongs to them.

## DISCOVERY APPROACH

### Phase 1: Analyze Brand Strategy
Extract from inputs:
- Archetype → What colors align with this emotional territory
- Personality → How traits translate to color qualities
- Positioning → Color territory to claim or avoid
- Audience → Color preferences of target segment
- Industry → Conventions to follow or intentionally break

### Phase 2: Audit Competitive Color Landscape
Apply Blue Ocean Color Strategy:
1. Identify dominant colors in category
2. Find underutilized colors (white space)
3. Identify colors to avoid (owned by competitors)
4. Assess: Can we own alternative territory credibly?

### Phase 3: Apply Color Psychology
For each potential color:
- Check Appropriateness Principle (fit over preference)
- Apply Color-in-Context Theory (context determines meaning)
- Verify cultural implications for target markets
- Connect to archetype color framework

### Phase 4: Build the Palette
Using color harmony systems:
- Select primary color based on strategy
- Add secondaries using harmony schemes (complementary, analogous, etc.)
- Add neutrals for balance
- Add accent/CTA color for action
- Apply 60-30-10 Rule for proportions
- Keep total to 3-5 core colors

### Phase 5: Validate Accessibility
- Test WCAG contrast ratios (4.5:1 normal text, 3:1 large)
- Simulate colorblindness (protanopia, deuteranopia, tritanopia)
- Ensure color is never the only indicator
- Document accessible alternatives

### Phase 6: Document Completely
Specify every color in:
- HEX (web)
- RGB (digital)
- CMYK (print)
- Pantone (brand consistency)

## TOOLS TO USE

- **Sequential Thinking MCP**: Build palette from brand psychology through to specific values systematically
- **AskUserQuestion**: Understand color preferences/constraints, validate primary color direction, get feedback on palette options
- **WebSearch**: Discover competitor brand colors, research color psychology, find brand color case studies, check industry color patterns
- **WebFetch**: Read color psychology articles, study brand color case studies, understand research behind color associations

## OUTPUT REQUIREMENTS

Deliver the complete color palette using the Color Palette Documentation Template from the `brand-color-psychology` skill. Must include:

1. **Executive Summary** (2-3 sentences on palette and rationale)
2. **Strategic Foundation** (brand inputs, psychology alignment, appropriateness analysis)
3. **Competitive Color Landscape** (audit, Blue Ocean analysis, differentiation strategy)
4. **Primary Colors** (1-2 with all values, rationale, usage guidelines)
5. **Secondary Colors** (2-3 with harmony relationship, role in palette)
6. **Neutral Colors** (dark, medium, light with usage)
7. **Accent Colors** (CTA, success, warning, error)
8. **Color Combinations** (approved, avoided, 60-30-10 proportions)
9. **Accessibility** (contrast ratios, colorblindness testing, non-color indicators)
10. **Quick Reference** (core palette table, CSS custom properties)
```

## After Agent Returns

Use AskUserQuestion to help founder review and validate:

"Here's your brand color palette. How would you like to proceed?"
- This palette feels right — let's proceed
- I'd like to explore different primary color options
- I want to refine specific colors (primary, secondary, accent)
- I have questions about the color choices
- Let's test the accessibility more thoroughly
- I need to discuss with my team before finalizing

## Guidelines

- **Colors must differentiate from competitors** — Blue Ocean thinking
- **Include accessibility considerations** — WCAG compliance is non-negotiable
- **Provide exact values** — no "blue-ish" vagueness; HEX, RGB, CMYK, Pantone
- **Consider how colors work across digital and print** — test CMYK conversion
- **Account for culture** — research color meanings in target markets
- **Appropriateness over preference** — color must "fit" the brand context
- **Keep it simple** — 3-5 core colors maximum; simplicity scales
- **Connect every choice to strategy** — rationale for each color

## Output

After the founder approves the palette:

1. Ensure `docs/00-BRAND/03-VISUAL/` directory exists
2. Save to `docs/00-BRAND/03-VISUAL/02-color-palette.md` with:
   - Executive summary
   - Strategic foundation
   - Competitive landscape
   - Complete color specifications
   - Accessibility validation
   - Quick reference

3. **Next step:** "Run `/00-BRAND:03-visual/03-select-typography` to develop your brand typography."
