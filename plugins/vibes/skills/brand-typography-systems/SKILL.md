---
name: brand-typography-systems
description: Use when choosing brand typefaces, pairing fonts, building a type hierarchy or modular scale, or writing typography guidelines and design tokens. Keywords - brand typography, font selection, font pairing, serif vs sans-serif, type scale, typeface licensing, web font performance, WCAG typography and readability.
---

# Brand typography systems & strategic type selection

Quick reference for developing strategic brand typography systems grounded in personality, hierarchy, and practical application.

> "Typography exists to honor content." — Robert Bringhurst, *The Elements of Typographic Style*

> "Typography and design should enhance communication, not just look attractive." — Erik Spiekermann

> "I can teach anyone good typography in two or three days. The craft is very simple, the rest is just practice." — Erik Spiekermann

---

## Key principles

1. **Start with personality**: Typography selection flows from brand personality to typeface choices. Never the reverse.
2. **Honor content**: Beautiful type that doesn't serve content fails its purpose.
3. **Contrast through classification**: Serif + sans-serif pairing creates natural hierarchy without conflict.
4. **Form follows function**: Body text prioritizes legibility; display text can prioritize personality.
5. **Consistency builds recognition**: Every touchpoint reinforces (or undermines) brand perception.
6. **Accessibility is non-negotiable**: Design for the widest possible audience.
7. **Systems scale**: Create hierarchies that work across all applications and contexts.

---

## Core frameworks

### 1. Brand-first typography selection process

Typography selection must flow from brand strategy, not aesthetic preference.

**The process:**

| Step | Action | Purpose |
|------|--------|---------|
| 1 | **Define Brand Personality** | Identify 3-5 traits that define brand voice and image |
| 2 | **Understand Target Audience** | Demographics, preferences, industry expectations |
| 3 | **Gather Inspiration** | Analyze competitors, identify differentiation opportunities |
| 4 | **Select and Pair Fonts** | Create mockups across touchpoints (print, web, mobile) |
| 5 | **Establish Hierarchy** | Define primary, secondary, tertiary with clear purposes |
| 6 | **Create Guidelines** | Document everything with examples and specifications |

**Key insight**: "If the brand can define itself using descriptions to capture the tone, personality, and principles—we can translate that into typographic forms."

---

### 2. Modular scale typography system

A mathematical approach to creating harmonious type hierarchies using consistent ratios.

**Common ratios:**

| Ratio | Value | Character | Best For |
|-------|-------|-----------|----------|
| Minor Second | 1.067 | Subtle increments | Dense layouts, data-heavy UIs |
| Major Second | 1.125 | Slightly noticeable | Functional interfaces |
| Minor Third | 1.200 | Moderate differentiation | Balanced content hierarchy |
| Major Third | 1.250 | Clear hierarchy | General UI design |
| Perfect Fourth | 1.333 | Distinct visual hierarchy | Editorial, marketing |
| Golden Ratio | 1.618 | Dramatic, high-end | Premium brands, display-heavy |

**The process:**
1. **Define Base Size**: Start with 16px for web (browser default, accessibility baseline)
2. **Choose a Ratio**: Match to brand personality and content type
3. **Calculate Sizes**: Multiply base by ratio for each step up, divide for steps down
4. **Apply to Hierarchy**: Map calculated sizes to H1–H6, body, captions
5. **Test Responsively**: Adjust ratio or base for different screen sizes

**Key principle**: Limit to 6-8 distinct sizes. Larger screens can use more dramatic ratios; smaller screens benefit from conservative ratios.

**Tools**: [Typescale.io](https://typescale.io/) | [Type Scale Tool](https://precise-type.com/)

---

### 3. Ellen Lupton's "Thinking with Type" framework

An approach covering three connected systems:

| System | Focus | Key Elements |
|--------|-------|--------------|
| **Letter** | Individual characters | Typeface anatomy, classification, personality |
| **Text** | Words and paragraphs | Alignment, spacing, kerning, tracking, leading |
| **Grid** | Page structure | Columns, margins, spatial relationships |

**Key principles:**
- "Learn the rules and how to break them"
- Historical context informs modern practice
- Visual balance and Gestalt grouping guide effective layouts
- Accessibility and legibility are non-negotiable

---

## Font classification & personality matrix

| Classification | Personality Traits | Best For | Example Industries |
|---------------|-------------------|----------|-------------------|
| **Serif** | Traditional, classical, reliable, authoritative, sophisticated | Long-form reading, heritage positioning, trust | Law firms, finance, luxury, editorial |
| **Sans-Serif** | Modern, clean, minimal, approachable, contemporary | Digital interfaces, startups, accessibility | Tech, SaaS, healthcare, contemporary retail |
| **Script** | Elegant, distinctive, personal, feminine | Special occasions, luxury accents | Fashion, wedding, high-end beauty |
| **Handwritten** | Artsy, informal, fun, playful, authentic | Personal connection, casual brands | Creative agencies, children's products, artisan food |
| **Display/Decorative** | Bold, attention-grabbing, distinctive | Headlines only, limited accent use | Entertainment, events, creative campaigns |
| **Slab Serif** | Strong, sturdy, mechanical, modern-classic | Technology with heritage, contemporary editorial | Construction, automotive, journalism |
| **Monospace** | Technical, precise, developer-oriented | Code, data, technical documentation | Developer tools, fintech, data platforms |

---

## Serif vs. sans-serif decision framework

### Choose serif when:
- Brand leans artisanal, authoritative, or editorial
- **Industries**: Boutique hotels, legal firms, investment advisory, craft producers, heritage brands
- Long-form print content leads touchpoints
- You want to convey tradition, trust, premium positioning
- Target audience expects established credibility

### Choose sans-serif when:
- 70%+ of touchpoints are digital UI (apps, dashboards, small screens)
- **Industries**: Tech, startups, digital products, contemporary retail, healthcare
- Quick legibility matters most
- You want to convey modernity, accessibility, innovation
- Audiences expect contemporary, forward-thinking brands

**Note**: High-resolution displays have reduced the screen legibility gap between serif and sans-serif. Context and specific typeface matter more than classification alone.

---

## Typeface evaluation criteria

Seven dimensions for evaluating any typeface:

| Criterion | Question to Ask | Why It Matters |
|-----------|-----------------|----------------|
| **Completeness** | Does it have all characters, weights, and styles needed? | Brand needs evolve; typeface must grow with you |
| **Legibility** | Is it readable at small sizes? Are characters distinctive? | Content must be consumable |
| **Versatility** | Works across headlines, body, captions, different media? | One system must serve many contexts |
| **Complementarity** | Works well with logo, colors, imagery? | Typography exists within visual system |
| **Distinctiveness** | Helps differentiate from competitors? | Typography is branding opportunity |
| **Technical Readiness** | Available as web font? Proper licensing? Variable font? | Implementation constraints matter |
| **X-Height Appropriateness** | Optimal for intended sizes? | Higher x-height improves screen legibility, but extremely high reduces word-shape recognition |

---

## Font pairing principles

### The classic approach: contrast through classification

The oldest reliable rule: pair serif with sans-serif. This creates clear contrast through form while allowing both typefaces to serve distinct purposes.

### Five key principles

1. **Seek Contrast, Not Conflict**
   > "When two styles are paired that are almost the same—but not quite—they begin to clash, like wearing two slightly different plaid patterns at once." — Ellen Lupton

2. **Avoid "Typographic Mud"**: Typefaces from the same classification but different families can blur together without creating meaningful distinction.

3. **Create Meaningful Hierarchy**: Use contrast in weight, size, and style to guide readers.

4. **Limit Strong Personalities**: Mixing two bold typographic personalities rarely works. They compete for attention.

5. **Consider Weight Contrast**: Bolder weights for titles, lighter for body (or vice versa for specific effects).

### Practical tips
- Keep one font simple when using a distinctive display font
- Serif headlines + sans-serif body (or reverse) is reliable
- Look for shared characteristics: similar x-heights, proportions, or historical era
- Test extensively in real content contexts before committing

---

## Typography spacing guidelines

### Line height (leading)

| Text Type | Line Height | Rationale |
|-----------|-------------|-----------|
| Headlines | 1.1 - 1.25 | Tight for impact |
| Subheads | 1.25 - 1.35 | Moderate |
| Body copy | 1.5 - 1.7 | Optimal readability |
| Long-form content | 1.6 - 1.8 | Extra breathing room |

### Letter spacing (tracking)

| Context | Tracking | Rationale |
|---------|----------|-----------|
| Large headlines (>36px) | -0.02em to -0.01em | Tighten for impact |
| Medium headings | 0 | Default |
| Body text | 0 | Designed for optimal spacing |
| Small text (<14px) | 0.01em to 0.02em | Open up for legibility |
| All caps | 0.05em to 0.1em | Always add spacing |
| Buttons/Labels | 0.05em | Improve readability |

### Line length (measure)

- **Optimal**: 50-75 characters per line (66 often cited as ideal)
- **Minimum**: 45 characters (below = choppy reading)
- **Maximum**: 80 characters (above = eye strain)

---

## Digital typography specifics

### Variable fonts

**What they are**: Single font file containing all weights, widths, and styles through continuous interpolation.

**Benefits**:
- **Performance**: One file vs. multiple static files (e.g., 405KB vs 1,170KB for full Source Sans Pro family)
- **Design Flexibility**: Access any weight (e.g., 450, not just 400 or 500)
- **Responsive Typography**: Adjust weight/width based on viewport
- **Animation**: Smooth transitions between styles

**Key axes**:

| Axis | Code | Range | Effect |
|------|------|-------|--------|
| Weight | `wght` | Thin to Black | Stroke thickness |
| Width | `wdth` | Condensed to Extended | Character width |
| Italic | `ital` | Upright to Italic | Roman/italic switch |
| Slant | `slnt` | Angle of lean | Oblique angle |
| Optical Size | `opsz` | Size-specific adjustments | Auto-adjusts details for size |

### Web font performance

**The problem**: Custom fonts require downloads that delay text rendering.

**FOIT vs FOUT**:
- **FOIT (Flash of Invisible Text)**: Browser hides text until font loads, which is poor UX
- **FOUT (Flash of Unstyled Text)**: Shows fallback font first, then swaps when ready, which is preferred

**Recommended strategies**:
1. Use `font-display: swap`
2. Preload critical fonts
3. Use `font-display: optional` for maximum performance
4. Match fallback metrics to reduce layout shift

### Responsive typography

**Fluid typography with `clamp()`**:
```css
h1 {
  font-size: clamp(2rem, 5vw, 4rem);
}
```
- **Minimum**: 2rem (won't shrink below)
- **Preferred**: 5vw (scales with viewport)
- **Maximum**: 4rem (won't grow above)

### System font stacks

**When to use**: Applications, dashboards, content-heavy tools where neutrality and performance matter.

**Modern system font stack**:
```css
font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto,
             Oxygen-Sans, Ubuntu, Cantarell, "Helvetica Neue", sans-serif;
```

**Resource**: [Modern Font Stacks](https://modernfontstacks.com/)

---

## WCAG typography requirements

### Contrast ratios

| Standard | Ratio | Use Case |
|----------|-------|----------|
| **Level AA (minimum)** | 4.5:1 | Normal text |
| **Level AA (minimum)** | 3:1 | Large text (24px+ or 18.5px bold) |
| **Level AAA (enhanced)** | 7:1 | Normal text |
| **Level AAA (enhanced)** | 4.5:1 | Large text |

### Text resizing (WCAG 1.4.4)
- Text must be resizable to 200% without loss of content or functionality
- Use relative units (rem, em, %) not fixed pixels

### Text spacing (WCAG 1.4.12)
Must accommodate user overrides for:
- Line height: 1.5x font size
- Paragraph spacing: 2x font size
- Letter spacing: 0.12x font size
- Word spacing: 0.16x font size

---

## Dyslexia-friendly typography

**Key characteristics**:
- Simple letter shapes (sans-serif generally preferred)
- Wider letter and word spacing
- Distinct letterforms (clear b/d, p/q differentiation)
- Upright (avoid italics for body text)
- Adequate size (16px+ for body)

**Recommended fonts**:

| Font | Why It Works |
|------|--------------|
| **Lexend** | Specifically designed for readability and dyslexia |
| **Open Sans** | Clear shapes, generous spacing |
| **Verdana** | Clear letter shapes, uniformity |
| **Atkinson Hyperlegible** | Designed for low-vision readers, benefits all |
| **Inter** | Clear shapes, excellent for digital |

**Key finding**: Sans-serif, monospaced, and roman fonts are most readable for dyslexic readers. Italics significantly reduce readability.

---

## Print vs. digital considerations

| Factor | Print | Digital |
|--------|-------|---------|
| **Resolution** | 300 dpi | 72-100 ppi (varies by screen) |
| **Body Font Size** | 10-12pt typical | 15-25px typical |
| **Font Freedom** | Any font works if printed | Limited by availability/licensing |
| **Rendering** | Consistent across prints | Varies by device/browser |
| **Serif Readability** | Excellent for long text | Depends on screen quality |

### Cross-channel best practices
- Choose typefaces designed for both environments
- Test selected fonts in both print and digital mockups
- Consider typeface superfamilies (versions optimized for each medium)
- Ensure licensing covers all intended uses
- Document specific size/weight adjustments needed per medium

---

## Font licensing

### License types

| Type | Use Case | Typical Limits |
|------|----------|----------------|
| **Desktop** | Design software, print materials | Number of users/devices |
| **Web** | Websites via CSS | Page views, domains |
| **App** | Mobile/desktop applications | App downloads, platforms |
| **ePub** | Digital publications | Title count |
| **Server/API** | Dynamic image generation | Impressions |

### Key considerations
1. **Read the EULA**: Every foundry's terms differ
2. **Logo Use**: Some licenses explicitly prohibit logo use
3. **Client Work**: Clients need their own license; you cannot transfer yours
4. **Modifications**: Most licenses prohibit altering font files
5. **Embedding**: PDF embedding, video embedding have specific rules

### Open source options
- **SIL Open Font License (OFL)**: Free for personal and commercial use, can modify
- **Google Fonts**: All fonts licensed for commercial use
- **The League of Moveable Type**: Quality open-source fonts

---

## Recommended free fonts (Google Fonts)

### Sans-serif
- **Inter**: Excellent for digital interfaces, 9 weights
- **DM Sans**: Clean, geometric, 9 weights
- **Source Sans Pro**: Adobe's first open-source font
- **Work Sans**: Versatile, 9 weights
- **Fira Sans**: Space-efficient, originally for Mozilla

### Serif
- **Lora**: Modern and classic elements, excellent readability
- **Cormorant**: Elegant display serif
- **Playfair Display**: High contrast, editorial feel
- **Merriweather**: Designed for screen, highly readable

### Display
- **Montserrat**: Geometric, contemporary
- **Raleway**: Thin, sophisticated
- **Oswald**: Bold, structured

---

## Common mistakes

| Mistake | Problem | Solution |
|---------|---------|----------|
| Inconsistent font usage across platforms | Harms brand recognition | Document and enforce typography system |
| Too many fonts | Creates visual chaos | Stick to 2-3 maximum |
| Sacrificing readability for style | Audience can't consume content | Test legibility at actual use sizes |
| Ignoring licensing | Legal liability | Audit all fonts, ensure proper licenses |
| Mismatched personality | Typography undermines brand message | Start with personality, select to match |
| Low contrast text | Fails accessibility, hard to read | Use contrast checkers, meet WCAG AA |
| Over-styling | Shadows, gradients look unprofessional | Keep typography clean and purposeful |
| Ignoring mobile | Fails on primary device category | Test across all device sizes |
| Using trendy fonts | Dates quickly, requires rebrand | Choose timeless options |
| Skipping hierarchy | Users can't navigate content | Define clear size/weight distinctions |
| Not testing across media | Print and digital render differently | Test in both contexts |
| Default fonts for logos | Lacks distinctiveness | Custom or carefully selected typefaces only |

---

## Key mental models

**Contrast Through Classification**: Serif + sans-serif pairing creates natural hierarchy and visual interest without conflict.

**Form Follows Function**: Body text prioritizes legibility; display text can prioritize personality.

**Consistency Builds Recognition**: Every touchpoint reinforces (or undermines) brand perception.

**Accessibility is Non-Negotiable**: Design for the widest possible audience. Good accessibility is good design.

**Start With Personality**: Typography selection flows from brand personality to typeface choices. Never the reverse.

**If You Have Fewer Choices**: "It doesn't necessarily make your life more difficult. It often makes it easier." — Erik Spiekermann

---

## Templates

Read [reference/templates.md](reference/templates.md) when producing a deliverable the user will keep, such as a filled worksheet, a documented decision, or a final write-up. Skip it for conceptual questions and quick recommendations, which this file covers. It opens with a table of contents, so load only the template needed:
- Typography system documentation template (complete output structure)
- Modular scale calculator reference
- Accessibility testing checklist
- Font licensing checklist

---

## When to apply this knowledge

### During strategy phase
- Apply the brand-first typography selection process
- Use the font classification & personality matrix
- Consider the serif vs. sans-serif decision framework

### During font selection
- Apply the typeface evaluation criteria (7 dimensions)
- Use the font pairing principles
- Research font options (Google Fonts, premium foundries)

### During hierarchy development
- Apply Modular Scale System
- Set spacing guidelines (line height, tracking, measure)
- Define typography tokens

### During validation
- Test WCAG accessibility requirements
- Verify dyslexia-friendly considerations
- Test across print and digital
- Check font licensing
