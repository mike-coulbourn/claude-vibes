# Brand Color Psychology Templates

Reusable templates for brand color strategy documentation.

---

## Color Palette Documentation Template

```markdown
# Brand Color Palette: [Brand Name]

## Executive Summary

[2-3 sentences: What colors define this brand and why? Reference the strategic rationale.]

---

## Strategic Foundation for Color

### Brand Inputs

| Element | Summary | Color Implication |
|---------|---------|-------------------|
| Archetype | [Primary/Secondary] | [Colors associated with archetype] |
| Personality | [Traits] | [How traits translate to color] |
| Positioning | [Territory] | [Color territory to claim] |
| Audience | [Who] | [Color preferences of audience] |
| Industry | [Category] | [Industry color conventions] |

### Color Psychology Alignment

| Brand Quality | Color Association | Rationale |
|--------------|-------------------|-----------|
| [Quality 1] | [Colors] | [Why these colors express this] |
| [Quality 2] | [Colors] | [Why these colors express this] |
| [Quality 3] | [Colors] | [Why these colors express this] |

### Appropriateness Analysis

[Does the palette fit the brand context? Consider industry expectations, audience psychology, and perceived fit.]

---

## Competitive Color Landscape

### Competitor Audit

| Competitor | Primary Color | Secondary | Notes |
|-----------|---------------|-----------|-------|
| [A] | [Color] | [Color] | [What they own] |
| [B] | [Color] | [Color] | [What they own] |
| [C] | [Color] | [Color] | [What they own] |
| [D] | [Color] | [Color] | [What they own] |
| [E] | [Color] | [Color] | [What they own] |

### Blue Ocean Analysis

**Dominant category colors:** [What most competitors use]

**Color white space:** [Colors not used or underutilized by competitors]

**Colors to avoid:** [Colors too strongly associated with specific competitors]

**Differentiation opportunity:** [Strategic color territory to claim]

---

## Primary Colors

### Primary Color 1: [Color Name]

**The Color:**
[Visual description — e.g., "A confident, deep navy blue that commands attention without aggression"]

**Color Values:**
| System | Value |
|--------|-------|
| HEX | #[XXXXXX] |
| RGB | R: [X] G: [X] B: [X] |
| CMYK | C: [X]% M: [X]% Y: [X]% K: [X]% |
| Pantone | [PMS Number] (if applicable) |
| HSL | H: [X]° S: [X]% L: [X]% |

**Strategic Rationale:**
[Why this specific color for this brand — connect to archetype, positioning, and differentiation strategy]

**Color Psychology:**
- **Communicates:** [What this color conveys]
- **Evokes:** [Emotional response]
- **Associated with:** [Concepts/industries]
- **Context-specific meaning:** [What it means for THIS brand in THIS context]

**Usage Guidelines:**
- **Use for:** [Applications]
- **Proportion:** [~X% of brand color usage]
- **Best on:** [Background colors]
- **Avoid:** [Combinations to avoid]

### Primary Color 2: [Color Name] (if applicable)

[Same structure as Primary Color 1]

---

## Secondary Colors

### Secondary Color 1: [Color Name]

**The Color:**
[Visual description]

**Color Values:**
| System | Value |
|--------|-------|
| HEX | #[XXXXXX] |
| RGB | R: [X] G: [X] B: [X] |
| CMYK | C: [X]% M: [X]% Y: [X]% K: [X]% |
| Pantone | [PMS Number] (if applicable) |

**Color Harmony Relationship:**
[How this relates to the primary — complementary, analogous, split-complementary, etc.]

**Role in the Palette:**
[How this supports the primary colors]

**Usage Guidelines:**
- **Use for:** [Applications]
- **Proportion:** [~X% of brand color usage]
- **Best paired with:** [Colors]

---

## Neutral Colors

### Dark Neutral (Text/Headers)

| System | Value |
|--------|-------|
| HEX | #[XXXXXX] |
| RGB | R: [X] G: [X] B: [X] |

**Usage:** Primary text, headers, key UI elements
**Why not pure black:** [Rationale — usually softer on eyes, warmer feel]

### Medium Neutral (Secondary Text)

| System | Value |
|--------|-------|
| HEX | #[XXXXXX] |
| RGB | R: [X] G: [X] B: [X] |

**Usage:** Secondary text, borders, dividers

### Light Neutral (Backgrounds)

| System | Value |
|--------|-------|
| HEX | #[XXXXXX] |
| RGB | R: [X] G: [X] B: [X] |

**Usage:** Page backgrounds, cards, containers
**Why not pure white:** [Rationale — usually softer]

---

## Accent Colors

### Action/CTA Color: [Color Name]

| System | Value |
|--------|-------|
| HEX | #[XXXXXX] |
| RGB | R: [X] G: [X] B: [X] |

**Usage:** Primary buttons, CTAs, links
**Contrast ratio with white text:** [X:1] (WCAG [AA/AAA])
**Why this color:** [Stands out, creates action, psychological trigger]

### Semantic Colors

| Purpose | HEX | Usage |
|---------|-----|-------|
| Success | #[XXXXXX] | Success messages, confirmations |
| Warning | #[XXXXXX] | Warnings, caution states |
| Error | #[XXXXXX] | Errors, destructive actions |

---

## Color Combinations

### Approved Combinations

| Primary | Secondary | Background | Text | Usage |
|---------|-----------|------------|------|-------|
| [Color] | [Color] | [Color] | [Color] | [Context] |
| [Color] | [Color] | [Color] | [Color] | [Context] |

### Combinations to Avoid

| Combination | Why to Avoid |
|------------|--------------|
| [Color + Color] | [Reason — clash, accessibility, cultural] |

### Color Proportions (60-30-10 Rule)

- **60%** — [Neutral/background color] — Creates canvas and breathing room
- **30%** — [Primary color] — Establishes brand presence
- **10%** — [Accent/CTA color] — Drives action and attention

---

## Accessibility

### Contrast Ratios

| Text/Background Combination | Ratio | WCAG Level |
|----------------------------|-------|------------|
| [Dark text] on [Light bg] | [X:1] | [AAA/AA/Fail] |
| [Light text] on [Primary] | [X:1] | [AAA/AA/Fail] |
| [CTA text] on [CTA bg] | [X:1] | [AAA/AA/Fail] |

### Color Blindness Tested

- [ ] Protanopia (red-blind)
- [ ] Deuteranopia (green-blind)
- [ ] Tritanopia (blue-blind)

---

## Quick Reference

### Core Palette

| Color | HEX | Role |
|-------|-----|------|
| [Primary 1] | #[XXXXXX] | Primary brand color |
| [Secondary 1] | #[XXXXXX] | Supporting color |
| [Neutral Dark] | #[XXXXXX] | Text |
| [Neutral Light] | #[XXXXXX] | Backgrounds |
| [CTA] | #[XXXXXX] | Actions |

### CSS Custom Properties

```css
:root {
  --color-primary: #[XXXXXX];
  --color-secondary: #[XXXXXX];
  --color-accent: #[XXXXXX];
  --color-text: #[XXXXXX];
  --color-text-light: #[XXXXXX];
  --color-background: #[XXXXXX];
  --color-success: #[XXXXXX];
  --color-warning: #[XXXXXX];
  --color-error: #[XXXXXX];
}
```
```

---

## Competitor Color Audit Template

```markdown
# Competitive Color Audit: [Category/Industry]

## Category Overview

**Industry:** [Category name]
**Audit Date:** [Date]
**Competitors Analyzed:** [Number]

---

## Competitor Analysis

### [Competitor 1]

**Brand Name:** [Name]
**Website:** [URL]

| Color Role | Color | HEX | Notes |
|------------|-------|-----|-------|
| Primary | [Description] | #[XXXXXX] | [How they use it] |
| Secondary | [Description] | #[XXXXXX] | [How they use it] |
| Accent | [Description] | #[XXXXXX] | [How they use it] |

**Visual Territory Owned:** [What this brand is known for visually]

### [Competitor 2-5...]

[Same structure for each competitor]

---

## Color Landscape Summary

### Dominant Colors

| Color | Competitors Using | % of Category |
|-------|-------------------|---------------|
| [Blue] | [A, B, C] | [60%] |
| [Green] | [D, E] | [40%] |

### Underutilized Colors

| Color | Competitors Using | Opportunity Level |
|-------|-------------------|-------------------|
| [Purple] | [None] | High |
| [Orange] | [One] | Medium |

### Colors to Avoid

| Color | Why | Risk Level |
|-------|-----|------------|
| [Specific Blue] | Owned by [Competitor] | High |

---

## Blue Ocean Opportunities

**Primary Opportunity:** [Color territory that could differentiate]

**Rationale:** [Why this works for the brand]

**Risk Assessment:** [What could go wrong, how to mitigate]
```

---

## Accessibility Testing Checklist

```markdown
# Color Accessibility Validation

## Contrast Testing

### Text Combinations

| Foreground | Background | Ratio | AA Normal | AA Large | AAA Normal |
|------------|------------|-------|-----------|----------|------------|
| [Text color] | [BG color] | [X:1] | [Pass/Fail] | [Pass/Fail] | [Pass/Fail] |
| [Text color] | [BG color] | [X:1] | [Pass/Fail] | [Pass/Fail] | [Pass/Fail] |

**Tool Used:** [WebAIM / Adobe Color / Coolors]

---

## Colorblindness Simulation

### Protanopia (Red-Blind)

- [ ] All UI elements distinguishable
- [ ] Color is not the only indicator
- [ ] Key actions visible

### Deuteranopia (Green-Blind)

- [ ] All UI elements distinguishable
- [ ] Color is not the only indicator
- [ ] Key actions visible

### Tritanopia (Blue-Blind)

- [ ] All UI elements distinguishable
- [ ] Color is not the only indicator
- [ ] Key actions visible

**Tool Used:** [Coblis / Adobe Color / Chrome DevTools]

---

## Non-Color Indicators

| Use Case | Color Indicator | Non-Color Alternative |
|----------|-----------------|----------------------|
| Success | Green | Checkmark icon + "Success" text |
| Error | Red | X icon + error message |
| Warning | Yellow | Triangle icon + warning text |
| Link | Blue underline | Underline only |

---

## Validation Summary

- [ ] All text meets WCAG AA (4.5:1 normal, 3:1 large)
- [ ] Primary CTAs meet WCAG AA
- [ ] Palette works for all colorblindness types
- [ ] Color is never the only indicator
- [ ] Icons/patterns used alongside color
```

---

## Color Psychology Rationale Template

```markdown
# Color Psychology Rationale: [Color Name]

## The Color

**Visual Description:** [Rich description of the color]

**Color Values:**
- HEX: #[XXXXXX]
- RGB: rgb([X], [X], [X])
- HSL: hsl([X]°, [X]%, [X]%)

---

## Universal Associations

**Commonly Associated With:**
- [Association 1]
- [Association 2]
- [Association 3]

**Psychological Effects:**
- **Emotional:** [How it makes people feel]
- **Physical:** [Any physical responses — e.g., appetite, energy]
- **Cognitive:** [How it affects thinking — trust, urgency, calm]

---

## Context-Specific Meaning

**For This Brand:**
[What this color specifically means in this brand's context]

**For This Audience:**
[How the target audience will perceive this color]

**In This Industry:**
[How this color works within industry conventions or against them]

---

## Cultural Considerations

| Region | Meaning | Implication |
|--------|---------|-------------|
| Western | [Meaning] | [How to use] |
| Eastern | [Meaning] | [Adaptation needed?] |
| [Target Market] | [Meaning] | [Adaptation needed?] |

---

## Strategic Alignment

### Archetype Connection
[How this color aligns with the brand archetype]

### Personality Expression
[Which personality traits this color expresses]

### Positioning Support
[How this color supports competitive positioning]

### Differentiation Value
[How this color differentiates from competitors]

---

## Application Guidelines

**Use this color when:**
- [Scenario 1]
- [Scenario 2]

**Avoid this color when:**
- [Scenario 1]
- [Scenario 2]

**Best paired with:**
- [Color 1] — [Why]
- [Color 2] — [Why]
```

---

## Output Validation Checklist

Before finalizing any color palette documentation, verify:

### Strategic Foundation
- [ ] Archetype → color connection is explicit
- [ ] Personality traits → color translation is documented
- [ ] Positioning → differentiation rationale is clear
- [ ] Audience preferences are considered
- [ ] Industry conventions are acknowledged (followed or intentionally broken)

### Competitive Analysis
- [ ] 5+ competitors audited
- [ ] Dominant colors identified
- [ ] White space opportunities documented
- [ ] Colors to avoid listed
- [ ] Differentiation strategy is explicit

### Technical Specifications
- [ ] All colors specified in HEX
- [ ] All colors specified in RGB
- [ ] Primary colors specified in CMYK (for print)
- [ ] Pantone equivalents identified (for premium applications)
- [ ] CSS custom properties provided

### Palette Structure
- [ ] 1-2 primary colors
- [ ] 2-3 secondary colors
- [ ] Neutral palette (dark, medium, light)
- [ ] Accent/CTA color
- [ ] Semantic colors (success, warning, error)

### Accessibility
- [ ] All text combinations meet WCAG AA (4.5:1)
- [ ] CTAs meet WCAG AA
- [ ] Colorblindness simulation tested
- [ ] Non-color indicators documented

### Cultural Considerations
- [ ] Target market color meanings researched
- [ ] Adaptations documented if needed
- [ ] No problematic associations

### Usage Guidelines
- [ ] 60-30-10 proportions defined
- [ ] Approved combinations documented
- [ ] Combinations to avoid listed
- [ ] Application contexts described

### Quick Reference
- [ ] Core palette table
- [ ] CSS custom properties
- [ ] Copy-paste values ready
