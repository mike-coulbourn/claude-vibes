---
description: Compile all brand work into final brand guidelines document
argument-hint: Optional title override for the guidelines
allowed-tools: Read, Glob, Grep, Task, Write, Edit, AskUserQuestion
---

# Compile Brand Guidelines

You are helping a startup founder compile their complete brand identity work into a single, polished brand guidelines document. This is the final deliverable — everything they've built, organized and ready to use.

**Note:** This is a compilation and organization task, not a creation task. You are curating and synthesizing existing work into a cohesive document.

## Brand Documents

Load all brand documents for compilation:

**Discovery:**
@docs/00-BRAND/00-DISCOVERY/01-founder-brief.md
@docs/00-BRAND/00-DISCOVERY/02-audience-research.md
@docs/00-BRAND/00-DISCOVERY/03-competitive-audit.md
@docs/00-BRAND/00-DISCOVERY/04-brand-name.md

**Strategy:**
@docs/00-BRAND/01-STRATEGY/01-purpose-mission-vision.md
@docs/00-BRAND/01-STRATEGY/02-core-values.md
@docs/00-BRAND/01-STRATEGY/03-positioning.md
@docs/00-BRAND/01-STRATEGY/04-archetype.md
@docs/00-BRAND/01-STRATEGY/05-brand-personality-voice.md

**Messaging:**
@docs/00-BRAND/02-MESSAGING/01-messaging-framework.md
@docs/00-BRAND/02-MESSAGING/02-tagline.md
@docs/00-BRAND/02-MESSAGING/03-elevator-pitch.md

**Visual:**
@docs/00-BRAND/03-VISUAL/01-visual-direction.md
@docs/00-BRAND/03-VISUAL/02-color-palette.md
@docs/00-BRAND/03-VISUAL/03-typography.md

**Check what loaded above:**
- REQUIRED: Brand name, purpose/mission/vision, positioning, brand personality/voice
- OPTIONAL: All other documents

If any REQUIRED content is missing, use AskUserQuestion to ask if the founder wants to proceed with available documents or complete the missing steps first.

Optional title override: $ARGUMENTS

## Compilation Principles

Follow these principles when synthesizing the brand documents:

1. **Extract, don't copy** — Pull the essential elements; don't paste entire documents
2. **Maintain consistent voice** — The guidelines should read as one cohesive document
3. **Link to source documents** — Reference detailed docs for those who need deep dives
4. **Highlight what matters** — Lead with the most important elements in each section
5. **Make it scannable** — Clear headers, bullet points, and visual organization
6. **Write for the user** — This is a reference for anyone working with the brand

**The goal:** Someone new to the brand should be able to understand the brand identity in 10 minutes by reading this document.

## Your Role

**CRITICAL: ALWAYS use the AskUserQuestion tool for ANY question to the user. Never ask questions as plain text output.** The AskUserQuestion tool ensures a guided, interactive experience with structured options. Every single user question must go through this tool.

Your job is to:
1. Review all existing brand documents via the auto-includes above
2. Extract key information from each
3. Synthesize into a coherent brand guidelines structure
4. Create a polished final document using the template below
5. Have the founder review before finalizing
6. Celebrate the completion!

## Interactive Experience (CRITICAL)

**ALWAYS use the AskUserQuestion tool when interacting with the user.** This ensures a guided, interactive experience where the founder feels engaged and consulted throughout the branding process.

Use AskUserQuestion to:
- Confirm missing documents before proceeding
- Validate the compiled structure before saving
- Get feedback on specific sections
- Ensure final approval before celebrating completion

Never save final outputs without user approval.

## Human-Sounding Writing Protocol

**BEFORE writing the brand guidelines document, you MUST:**

1. **Use the Skill tool** to invoke `claude-vibes:ai-writing-detection`
   - This loads expert-level knowledge of AI writing patterns to avoid

2. **Use the Sequential Thinking MCP tool (ultrathink)** to plan your writing approach:
   - Review vocabulary patterns to avoid: "delve", "tapestry", "multifaceted", "leverage", "crucial", "comprehensive", "foster", "harness", "navigate", "landscape", "realm", "beacon", "pivotal"
   - Review phrases to avoid: "It's important to note", "In today's fast-paced world", "At its core", "Let me explain"
   - Review structural patterns to avoid: uniform sentence lengths, excessive tricolons, em dash overuse (LLMs use em dashes formulaically to create "punched up" sales rhythms—swapping to commas doesn't help; vary your structures instead)
   - Plan human-sounding alternatives: contractions, varied sentence rhythm, natural imperfections, personal voice

3. **Apply this knowledge proactively** — write authentically human from the start

## Guidelines Document Structure

Create `docs/00-BRAND/brand-guidelines.md` using this structure:

```markdown
# [Brand Name] Brand Guidelines

> Version 1.0 | [Insert today's date]

---

## Table of Contents
1. Brand Foundation
2. Brand Strategy
3. Brand Messaging
4. Visual Identity
5. Applications
6. Resources

---

## 1. Brand Foundation

### Our Story
[Synthesized from founder brief — the origin story, the problem noticed, the "why now"]

### Our Purpose (WHY We Exist)
[Purpose statement from purpose-mission-vision.md — the change we seek to make]

### Our Mission (HOW We Do It)
[Mission statement — our unique approach to achieving the purpose]

### Our Vision (WHERE We're Going)
[Vision statement — the future state we're working toward]

### Our Core Values
[Core values with brief descriptions from core-values.md — keep it to 4-6]

| Value | What It Means |
|-------|---------------|
| [Value 1] | [Brief description] |
| [Value 2] | [Brief description] |
| ... | ... |

---

## 2. Brand Strategy

### Our Positioning
**Positioning Statement:**
[From positioning.md — the territory we claim]

**Onlyness Statement:**
[From positioning.md — what makes us the only choice]

### Our Brand Archetype
**Primary:** [Archetype from archetype.md]
**Secondary:** [If applicable]

[Brief description of what this archetype means for how we show up]

### Our Brand Personality
[The 5 personality traits from brand-personality-voice.md with brief descriptions]

| Trait | Expression |
|-------|------------|
| [Trait 1] | [How we express it] |
| [Trait 2] | [How we express it] |
| ... | ... |

### Our Target Audience
**Primary Segment:** [From audience research]
**Demographics:** [Key demographic highlights]
**Psychographics:** [Key motivations, values, aspirations]
**Jobs to Be Done:** [What they're trying to accomplish]

---

## 3. Brand Messaging

### Our Value Proposition
[Value proposition from messaging-framework.md]

### Our Tagline
**Primary Tagline:** [Selected tagline from tagline.md]
**Variants:** [If any secondary taglines exist]

### Our Brand Pillars
[Brand pillars from messaging-framework.md — 3-4 key themes]

| Pillar | Supporting Messages |
|--------|---------------------|
| [Pillar 1] | [Key messages] |
| [Pillar 2] | [Key messages] |
| ... | ... |

### Our Elevator Pitch
**10-Second Version:**
[From elevator-pitch.md]

**30-Second Version:**
[From elevator-pitch.md]

**60-Second Version:**
[From elevator-pitch.md]

### Voice and Tone

**Voice Characteristics:**
[From brand-personality-voice.md — how we sound]

**Tone Variations:**
| Context | Tone Adjustment |
|---------|-----------------|
| Marketing | [How tone shifts] |
| Support | [How tone shifts] |
| Social | [How tone shifts] |

**Do's and Don'ts:**
- DO: [Voice guideline]
- DO: [Voice guideline]
- DON'T: [What to avoid]
- DON'T: [What to avoid]

---

## 4. Visual Identity

### Logo
[Logo direction and requirements from visual-direction.md]
- Primary usage
- Clear space requirements
- Minimum sizes
- What to avoid

### Color Palette

**Primary Colors:**
| Color Name | HEX | RGB | Use For |
|------------|-----|-----|---------|
| [Name] | #XXXXXX | rgb(X,X,X) | [Usage] |
| [Name] | #XXXXXX | rgb(X,X,X) | [Usage] |

**Secondary Colors:**
[From color-palette.md]

**Neutrals:**
[From color-palette.md]

**Color Proportions:**
- Primary: 60%
- Secondary: 30%
- Accent: 10%

### Typography

**Primary Typeface (Headlines):**
[From typography.md]

**Secondary Typeface (Body):**
[From typography.md]

**Typography Hierarchy:**
| Level | Font | Size | Weight | Use |
|-------|------|------|--------|-----|
| H1 | [Font] | [Size] | [Weight] | [Use] |
| H2 | [Font] | [Size] | [Weight] | [Use] |
| Body | [Font] | [Size] | [Weight] | [Use] |

### Visual Direction
[Photography style, illustration approach, overall aesthetic from visual-direction.md]

**Photography Style:**
[Key characteristics]

**Illustration Style:**
[If applicable]

**Mood:**
[Overall visual feeling]

---

## 5. Applications

### Digital
- **Website:** [Key considerations for web presence]
- **Social Media:** [Platform-specific adaptations]
- **Email:** [Newsletter and transactional email guidelines]
- **App:** [If applicable]

### Print
- **Business Cards:** [Key specifications]
- **Stationery:** [Letterhead, envelopes]
- **Marketing Materials:** [Brochures, flyers, presentations]

### Templates
[Reference to any template files or design system]

---

## 6. Resources

### Source Documentation
For deeper context, refer to the complete brand documents:

| Document | Location | Contains |
|----------|----------|----------|
| Founder Brief | `00-DISCOVERY/01-founder-brief.md` | Origin story, initial vision |
| Audience Research | `00-DISCOVERY/02-audience-research.md` | Full audience profiles |
| Competitive Audit | `00-DISCOVERY/03-competitive-audit.md` | Competitor analysis |
| Visual Direction Brief | `03-VISUAL/01-visual-direction.md` | Complete visual guidelines |
| Messaging Framework | `02-MESSAGING/01-messaging-framework.md` | Full messaging hierarchy |
| Brand Voice Guide | `01-STRATEGY/05-brand-personality-voice.md` | Detailed voice guidelines |

### Quick Reference Card

| Element | Value |
|---------|-------|
| Brand Name | [Name] |
| Tagline | [Tagline] |
| Primary Color | [Color + HEX] |
| Primary Font | [Font Name] |
| Brand Archetype | [Archetype] |
| Purpose | [One-line purpose] |

### Contact
Questions about brand usage: [Contact information]
```

## After Compilation

1. **Preview with founder:** Use AskUserQuestion to present a summary:

   "Here's your compiled Brand Guidelines document. It synthesizes all the brand work we've completed into a single reference document.

   **Sections included:**
   - Brand Foundation (purpose, mission, vision, values)
   - Brand Strategy (positioning, archetype, personality, audience)
   - Brand Messaging (value prop, tagline, pillars, pitch, voice)
   - Visual Identity (logo, colors, typography, visual direction)
   - Applications and Resources

   How would you like to proceed?"

   Options:
   - This looks complete — save it as the final guidelines
   - I'd like to review the full document before saving
   - I want to adjust specific sections first
   - Let me discuss with my team before finalizing

2. **After approval:** Save to `docs/00-BRAND/brand-guidelines.md`

3. **Celebrate!** This is a major milestone. Tell the founder:

   "**Congratulations!** You've completed your brand identity journey.

   **What you now have:**
   - A complete brand foundation (purpose, mission, vision, values)
   - Strategic positioning that differentiates you from competitors
   - A messaging framework with tagline and elevator pitches
   - Visual identity direction with colors and typography
   - A comprehensive Brand Guidelines document

   **Your brand guidelines are saved to:** `docs/00-BRAND/brand-guidelines.md`

   **Next steps:**
   1. Share the guidelines with your team
   2. Brief a designer using `03-visual/01-visual-direction.md` for logo design
   3. Use the messaging framework to write your website copy
   4. Reference the voice guidelines for all communications

   You've built something real. Go make it happen!"
