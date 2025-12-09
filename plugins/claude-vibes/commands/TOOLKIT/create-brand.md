---
description: Interactively create a complete brand identity for your startup
argument-hint: Your startup name or brief description (optional)
---

# Create Brand Identity

You are helping a startup founder create a comprehensive brand identity from scratch. This is an interactive, multi-phase process that guides them through discovery, strategy, messaging, and visual direction.

## Your Role

You orchestrate the entire brand identity creation process:
1. Guide the founder through each phase with AskUserQuestion
2. Launch specialized agents for expert-level work at each step
3. Save all outputs to organized files in `docs/brand/`
4. Build on previous phases — each step informs the next
5. Deliver a complete brand identity package

**CRITICAL: Use specialized agents for each area.** Do not try to create brand elements yourself — launch the appropriate agent for each step.

## Output Location

All brand identity work should be saved to: `docs/brand/`

**Directory structure:**
```
docs/brand/
├── 00-discovery/
│   ├── founder-brief.md
│   ├── audience-research.md
│   └── competitive-audit.md
├── 01-strategy/
│   ├── purpose-mission-vision.md
│   ├── core-values.md
│   ├── positioning.md
│   ├── archetype.md
│   └── brand-personality-voice.md
├── 02-messaging/
│   ├── messaging-framework.md
│   ├── tagline.md
│   └── elevator-pitch.md
├── 03-visual/
│   ├── visual-direction.md
│   ├── color-palette.md
│   └── typography.md
└── brand-guidelines.md (final compilation)
```

**Before creating any directory**, check if `docs/brand/` exists. Create subdirectories as you progress through each phase.

## The Brand Identity Creation Process

This process follows expert methodologies from Marty Neumeier, Simon Sinek, David Aaker, Al Ries & Jack Trout, and Emily Heyward.

---

## PHASE 1: Discovery

### Step 1.1: Founder Discovery (Interactive)

Start by understanding the founder's vision. **Use AskUserQuestion** to gather the essentials:

**First, acknowledge the journey:**
"Creating a brand identity is one of the most important investments you'll make in your startup. I'm going to guide you through a proven process used by top brand strategists. It will take some time, but the result will be a complete brand identity you can use everywhere."

**Core Discovery Questions (use AskUserQuestion in batches of 2-3):**

Batch 1 - The Business:
- What does your startup do? (Brief description)
- What problem do you solve?
- Who is your primary customer?

Batch 2 - The Vision:
- What change do you want to make in the world?
- What would be lost if your company didn't exist?
- What are your 3-year and 10-year goals?

Batch 3 - The Founder Story:
- Why did YOU start this? What's your personal connection?
- What do you do better than anyone else?
- What principles will you never compromise on?

Batch 4 - Practical Constraints:
- What's your budget for visual design? (DIY, freelancer, agency)
- Do you have existing brand elements (name, logo, colors)?
- Any must-have or must-avoid elements?

**Save the responses to:** `docs/brand/00-discovery/founder-brief.md`

### Step 1.2: Audience Research (Agent)

**Use Task tool** to launch `brand-audience-researcher`:

```
Research the target audience for this startup.

FOUNDER CONTEXT:
[Include key details from founder brief]

RESEARCH FOCUS:
- Psychographic profile of ideal customers
- Emotional triggers and aspirations
- Jobs-to-be-Done (functional, emotional, social)
- Where this audience spends time online
- Language and terminology they use
- What brands do they currently trust and why?

Deliver a detailed audience profile that will inform brand positioning and voice.
```

**Save to:** `docs/brand/00-discovery/audience-research.md`

### Step 1.3: Competitive Brand Audit (Agent)

**Use Task tool** to launch `brand-competitive-auditor`:

```
Conduct a brand audit of competitors in this space.

STARTUP CONTEXT:
[From founder brief]

TARGET AUDIENCE:
[From audience research]

AUDIT FOCUS:
- Direct competitors (3-4) — their brand positioning, visual identity, voice
- Indirect competitors — how else do people solve this problem?
- Visual landscape — common colors, typography, design patterns in the space
- Messaging patterns — how competitors talk about this problem
- Positioning white space — opportunities to differentiate
- Competitor weaknesses — what are customers complaining about?

Deliver a competitive brand map with clear differentiation opportunities.
```

**Save to:** `docs/brand/00-discovery/competitive-audit.md`

---

## PHASE 2: Brand Strategy

### Step 2.1: Purpose, Mission, Vision (Agent)

**Use Task tool** to launch `brand-purpose-architect`:

```
Define the brand purpose, mission, and vision for this startup.

DISCOVERY CONTEXT:
[Key insights from founder brief]

AUDIENCE INSIGHTS:
[Key insights from audience research]

COMPETITIVE LANDSCAPE:
[Key differentiation opportunities from competitive audit]

Use Simon Sinek's Golden Circle methodology:
- WHY: The brand's purpose — why it exists beyond making money
- HOW: The unique approach or values that enable the purpose
- WHAT: The products/services that prove the purpose

Deliver:
1. Purpose statement (the WHY — one powerful sentence)
2. Mission statement (what you do to fulfill the purpose)
3. Vision statement (the future state you're working toward)

Make these specific and ownable, not generic corporate-speak.
```

**Save to:** `docs/brand/01-strategy/purpose-mission-vision.md`

### Step 2.2: Core Values (Agent)

**Use Task tool** to launch `brand-values-curator`:

```
Define 3-4 core values for this brand.

CONTEXT:
- Purpose: [From previous step]
- Founder principles: [From founder brief]
- Audience values: [From audience research]

REQUIREMENTS:
- Values must be SPECIFIC and DIFFERENTIATING, not generic (avoid: integrity, quality, excellence, innovation)
- Values must be ACTIONABLE — guide real decisions
- Values must be AUTHENTIC to the founder's beliefs
- Values must RESONATE with the target audience

For each value, provide:
1. The value name (2-3 words max)
2. What it means in plain language
3. How it shows up in decisions ("When faced with X, we choose Y")
4. How it connects to the brand purpose

Deliver 3-4 core values that form the ethical backbone of this brand.
```

**Save to:** `docs/brand/01-strategy/core-values.md`

### Step 2.3: Positioning (Agent)

**Use Task tool** to launch `brand-positioning-strategist`:

```
Develop the brand positioning strategy.

CONTEXT:
- Purpose: [From purpose step]
- Values: [From values step]
- Competitive landscape: [From audit]
- Target audience: [From research]

Using Ries & Trout positioning methodology, develop:

1. POSITIONING STATEMENT:
   "For [target audience], [Brand] is the [category] that [key benefit] because [reason to believe]."

2. ONLINESS STATEMENT (Neumeier's ZAG):
   "Our brand is the ONLY [category] that [unique differentiator]."

3. POSITIONING MAP:
   - Two key axes that matter to customers
   - Where competitors sit
   - Where this brand should position

4. COMPETITIVE POSITIONING:
   - Position AGAINST the status quo, not just competitors
   - Clear differentiation angle

Deliver a positioning strategy that claims defensible territory in the customer's mind.
```

**Save to:** `docs/brand/01-strategy/positioning.md`

### Step 2.4: Brand Archetype (Agent)

**Use Task tool** to launch `brand-archetype-selector`:

```
Select the brand archetype(s) for this startup.

CONTEXT:
- Purpose: [From purpose]
- Values: [From values]
- Positioning: [From positioning]
- Target audience: [From research]
- Founder personality: [From brief]

Using the 12 Jungian brand archetypes, determine:

1. PRIMARY ARCHETYPE (choose one):
   - The Innocent, The Everyman, The Hero, The Outlaw/Rebel
   - The Explorer, The Creator, The Ruler, The Magician
   - The Lover, The Caregiver, The Jester, The Sage

2. SECONDARY ARCHETYPE (optional, for depth)

For the selected archetype(s), provide:
- Why this archetype fits the brand purpose and audience
- How this archetype expresses through brand communication
- Example brands that embody this archetype
- Key personality traits and emotional territory
- What to avoid (the shadow side of the archetype)

Deliver an archetype profile that grounds the brand's emotional expression.
```

**Save to:** `docs/brand/01-strategy/archetype.md`

### Step 2.5: Brand Personality and Voice (Agent)

**Use Task tool** to launch `brand-voice-architect`:

```
Define the brand personality and voice.

CONTEXT:
- Purpose: [From purpose]
- Values: [From values]
- Positioning: [From positioning]
- Archetype: [From archetype selection]
- Audience: [From research]

Develop:

1. BRAND PERSONALITY TRAITS (3-5 adjectives):
   - Specific traits that describe how the brand "acts"
   - Examples of brands with similar personalities

2. BRAND VOICE GUIDELINES:
   For each personality trait, provide:
   - Description: What this trait means
   - Do's: How to express this trait in writing
   - Don'ts: What to avoid
   - Example phrases: How this sounds in practice

3. TONE VARIATIONS:
   - Professional contexts (investor decks, contracts)
   - Marketing contexts (website, ads)
   - Support contexts (customer service, help docs)
   - Social contexts (social media, casual communication)

4. VOCABULARY GUIDELINES:
   - Words we use (aligned with audience language)
   - Words we avoid
   - Industry jargon: use or explain?

Deliver a complete voice guide that anyone can use to write "in the brand."
```

**Save to:** `docs/brand/01-strategy/brand-personality-voice.md`

---

## PHASE 3: Brand Messaging

### Step 3.1: Messaging Framework (Agent)

**Use Task tool** to launch `brand-messaging-architect`:

```
Create the brand messaging framework.

CONTEXT:
- Purpose: [Purpose statement]
- Positioning: [Positioning statement]
- Values: [Core values]
- Voice: [Brand voice traits]
- Audience: [From research — what they care about]

Develop:

1. VALUE PROPOSITION:
   - Functional benefit: What the product/service does
   - Emotional benefit: How it makes customers feel
   - Self-expression benefit: What using it says about them
   - Combined value statement (1-2 sentences)

2. BRAND PILLARS (3-5):
   - Key themes that support the value proposition
   - Each pillar with:
     - Pillar name
     - What it means
     - Key message under this pillar
     - Proof points

3. KEY MESSAGES:
   - Primary message (the one thing to remember)
   - Secondary messages (supporting points)
   - Messages by audience segment (if relevant)

4. MESSAGING HIERARCHY:
   - How messages flow from pillar to headline to body

Deliver a messaging framework that ensures consistency across all communication.
```

**Save to:** `docs/brand/02-messaging/messaging-framework.md`

### Step 3.2: Tagline (Agent)

**Use Task tool** to launch `brand-tagline-creator`:

```
Create brand tagline options.

CONTEXT:
- Purpose: [Purpose statement]
- Positioning: [Positioning and onliness]
- Value proposition: [From messaging framework]
- Brand voice: [Voice traits]
- Archetype: [Brand archetype]

TAGLINE REQUIREMENTS:
- Short (ideally 3-5 words)
- Memorable and distinctive
- Emotionally resonant
- Aligned with brand strategy
- Not generic or category-focused

EXPLORE DIFFERENT ANGLES:
- Benefit-focused taglines
- Promise-focused taglines
- Challenge/provocative taglines
- Emotional/aspirational taglines
- Action-oriented taglines

Deliver:
1. 5-7 tagline options
2. For each: strategic rationale, how it connects to brand strategy
3. Top recommendation with explanation
4. Usage guidance (when to use tagline vs. when to use full name)
```

**Save to:** `docs/brand/02-messaging/tagline.md`

**After agent returns, use AskUserQuestion:**
"Here are the tagline options. Which resonates most with you?"
[Present the options]
- Option A: [tagline]
- Option B: [tagline]
- Option C: [tagline]
- I'd like refinements on one of these
- None of these — try different angles

Update the tagline file with the selected option.

### Step 3.3: Elevator Pitch (Agent)

**Use Task tool** to launch `brand-elevator-pitch-writer`:

```
Create the brand elevator pitch.

CONTEXT:
- Purpose: [Purpose statement]
- Positioning: [Positioning statement]
- Value proposition: [From messaging]
- Tagline: [Selected tagline]
- Brand voice: [Voice traits]

Create elevator pitches for different durations:

1. ONE-LINER (10 seconds):
   - The briefest way to explain what you do

2. ELEVATOR PITCH (30 seconds):
   - Problem you solve
   - Who you solve it for
   - How you're different
   - Call to interest

3. EXTENDED PITCH (60 seconds):
   - Adds: proof points, traction, vision

4. FOUNDER STORY PITCH (when founder background is relevant):
   - Weaves personal story with business

For each, provide:
- The pitch itself (written as spoken word)
- Key emphasis points
- Natural pause moments
- Common follow-up questions to prepare for

Deliver pitches that feel natural when spoken, not like marketing copy read aloud.
```

**Save to:** `docs/brand/02-messaging/elevator-pitch.md`

---

## PHASE 4: Visual Identity Direction

**Note to user:** "Claude can provide detailed creative direction for visual identity, but not actual designs. The outputs from this phase are briefs for a designer or specifications you can implement yourself."

### Step 4.1: Overall Visual Direction (Agent)

**Use Task tool** to launch `brand-visual-director`:

```
Create the visual identity direction for this brand.

BRAND CONTEXT:
- Purpose: [Purpose statement]
- Positioning: [Positioning]
- Archetype: [Brand archetype]
- Personality: [Personality traits]
- Values: [Core values]
- Audience: [Target audience]
- Competitive landscape: [Visual patterns to avoid/differentiate from]

Develop:

1. MOOD BOARD DIRECTION:
   - Overall aesthetic feel (describe in detail)
   - Reference imagery descriptions (what kinds of images convey the brand)
   - Textures and patterns
   - Photography style guidelines
   - Illustration style (if applicable)

2. VISUAL PERSONALITY:
   - How each brand personality trait translates visually
   - Visual do's and don'ts for each trait

3. LOGO DESIGN BRIEF:
   - Logo style direction (wordmark, lettermark, symbol, combination)
   - Conceptual approaches to explore
   - Required variations (primary, secondary, icon, horizontal, stacked)
   - Technical requirements (scalability, single-color version)
   - What to avoid (based on competitive audit)
   - Emotional qualities the logo should convey

4. OVERALL VISUAL SYSTEM:
   - How visual elements should work together
   - Flexibility guidelines (what can vary vs. what stays constant)
   - Application priorities (website, social, print)

Deliver a comprehensive creative direction brief for a designer.
```

**Save to:** `docs/brand/03-visual/visual-direction.md`

### Step 4.2: Color Palette (Agent)

**Use Task tool** to launch `brand-color-strategist`:

```
Develop the brand color palette.

BRAND CONTEXT:
- Purpose: [Purpose]
- Archetype: [Archetype]
- Personality: [Personality traits]
- Visual direction: [Key visual direction points]
- Competitive landscape: [Colors used by competitors to avoid]
- Industry context: [Standard colors in this space]

Develop:

1. PRIMARY COLORS (1-2):
   - Color name and description
   - HEX, RGB, CMYK values
   - Pantone equivalent (if applicable)
   - Psychological rationale (why this color for this brand)
   - Usage guidelines (when to use)

2. SECONDARY COLORS (2-3):
   - Color name and description
   - HEX, RGB, CMYK values
   - How they complement the primary
   - Usage guidelines

3. NEUTRAL COLORS:
   - Background colors
   - Text colors
   - Grayscale palette
   - HEX, RGB values

4. ACCENT/ACTION COLORS:
   - For CTAs, highlights, alerts
   - When and how to use

5. COLOR COMBINATIONS:
   - Approved color pairings
   - Combinations to avoid
   - Contrast ratios for accessibility (WCAG compliance)

6. COLOR IN CONTEXT:
   - Digital applications (web, app)
   - Print applications
   - Environmental applications

Deliver a complete color system with exact specifications.
```

**Save to:** `docs/brand/03-visual/color-palette.md`

### Step 4.3: Typography (Agent)

**Use Task tool** to launch `brand-typography-curator`:

```
Develop the brand typography system.

BRAND CONTEXT:
- Personality: [Personality traits]
- Voice: [Brand voice]
- Visual direction: [Key visual direction]
- Use cases: [Primary applications — web, print, app]

Develop:

1. PRIMARY TYPEFACE (Headlines):
   - Font family name
   - Where to obtain (Google Fonts, Adobe Fonts, or purchase)
   - Why this typeface fits the brand personality
   - Weights to use
   - Tracking/letter-spacing recommendations

2. SECONDARY TYPEFACE (Body):
   - Font family name
   - Where to obtain
   - Why it pairs well with primary
   - Weights for different purposes (regular, bold, etc.)
   - Optimal size ranges for readability

3. TYPOGRAPHY HIERARCHY:
   - H1: Font, weight, size range
   - H2: Font, weight, size range
   - H3: Font, weight, size range
   - Body: Font, weight, size, line-height
   - Captions/Small: Font, weight, size
   - CTAs/Buttons: Font, weight, size

4. WEB-SAFE ALTERNATIVES:
   - Fallback fonts for each typeface
   - System font stack recommendations

5. TYPOGRAPHY DO'S AND DON'TS:
   - Minimum sizes
   - Maximum line lengths
   - What to avoid (condensed on body, too many weights, etc.)

6. ACCESSIBILITY:
   - Minimum contrast ratios
   - Scalability considerations

Deliver a complete typography system with specific font recommendations.
```

**Save to:** `docs/brand/03-visual/typography.md`

---

## PHASE 5: Final Compilation

### Step 5.1: Compile Brand Guidelines

After all phases are complete, compile everything into a single brand guidelines document.

Read all files from `docs/brand/` subdirectories and create a comprehensive brand guidelines document:

**Structure for `docs/brand/brand-guidelines.md`:**

```markdown
# [Brand Name] Brand Guidelines

> Version 1.0 | [Date]

---

## Table of Contents
1. Brand Foundation
2. Brand Strategy
3. Brand Messaging
4. Visual Identity
5. Applications

---

## 1. Brand Foundation

### Our Story
[From founder brief]

### Our Purpose (WHY)
[Purpose statement]

### Our Mission
[Mission statement]

### Our Vision
[Vision statement]

### Our Values
[Core values with descriptions]

---

## 2. Brand Strategy

### Our Positioning
[Positioning statement, onliness statement]

### Our Brand Archetype
[Archetype and what it means]

### Our Brand Personality
[Personality traits]

### Our Target Audience
[Audience profile summary]

---

## 3. Brand Messaging

### Our Value Proposition
[Value proposition]

### Our Tagline
[Selected tagline with usage]

### Our Brand Pillars
[Brand pillars]

### Our Elevator Pitch
[All pitch versions]

### Voice and Tone
[Voice guidelines summary]

---

## 4. Visual Identity

### Logo
[Logo direction and requirements — reference full brief]

### Color Palette
[All colors with values]

### Typography
[Typography system]

### Visual Direction
[Photography, illustration, overall aesthetic]

---

## 5. Applications

### Digital
- Website guidelines
- Social media guidelines
- Email guidelines

### Print
- Business cards
- Stationery
- Marketing materials

---

## Resources

- Full visual direction brief: `03-visual/visual-direction.md`
- Complete messaging framework: `02-messaging/messaging-framework.md`
- Audience research: `00-discovery/audience-research.md`
- Competitive audit: `00-discovery/competitive-audit.md`
```

---

## Process Flow

### How to Guide the User

1. **Start with welcome and overview** — Explain what they'll get and the time investment

2. **Go phase by phase** — Complete each phase before moving to the next

3. **Checkpoint after each phase** — Use AskUserQuestion:
   - "We've completed [Phase]. Here's what we have so far: [summary]"
   - "Ready to move to [Next Phase], or would you like to review/adjust anything?"

4. **Build on previous outputs** — Each agent prompt includes context from previous steps

5. **Save as you go** — Don't wait until the end; save each output to its file

6. **End with the complete package** — Compile everything and celebrate

### If User Wants to Skip or Pause

Use AskUserQuestion to confirm:
- "You can pause anytime and continue later — all work is saved to `docs/brand/`"
- "Would you like to skip [Phase] for now? Note: later phases build on earlier ones, so you may get less tailored results."

---

## Guidelines

- **This is interactive** — Use AskUserQuestion frequently to gather input and confirm direction
- **Always use specialized agents** — Don't generate brand elements yourself
- **Build context cumulatively** — Each agent prompt includes relevant context from previous phases
- **Save everything** — Create the file structure as you go
- **Celebrate progress** — Brand building is a journey; acknowledge milestones
- **Be educational** — Explain WHY each element matters as you go
- **Respect founder intuition** — They know their business; guide, don't dictate

## Startup Context

User's startup: $ARGUMENTS

If no context provided, begin with:
"I'm excited to help you create a complete brand identity for your startup! This process will guide you through discovery, strategy, messaging, and visual direction. Let's start with the basics — tell me about your startup."
