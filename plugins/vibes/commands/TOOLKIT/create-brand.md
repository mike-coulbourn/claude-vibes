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
│   ├── 01-founder-brief.md
│   ├── 02-audience-research.md
│   ├── 03-competitive-audit.md
│   └── 04-brand-name.md (if naming was needed)
├── 01-strategy/
│   ├── 01-purpose-mission-vision.md
│   ├── 02-core-values.md
│   ├── 03-positioning.md
│   ├── 04-archetype.md
│   └── 05-brand-personality-voice.md
├── 02-messaging/
│   ├── 01-messaging-framework.md
│   ├── 02-tagline.md
│   └── 03-elevator-pitch.md
├── 03-visual/
│   ├── 01-visual-direction.md
│   ├── 02-color-palette.md
│   └── 03-typography.md
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

Batch 5 - Brand Name:
- Do you already have a brand name you're committed to?
- If not, would you like help developing one?
- If you have a name, what do you like/dislike about it?

**Note:** If the founder does NOT have a brand name, flag this for Step 1.4 (Brand Naming). The name should be developed before moving to Phase 2 (Strategy), as the name influences all subsequent brand decisions.

**Save to:** `docs/brand/00-discovery/01-founder-brief.md` → **Review with ai-writing-detector**

### Step 1.2: Audience Research (Agent)

**Use Task tool** to launch `brand-audience-researcher`:

```
Research the target audience for this startup. ultrathink

FOUNDER CONTEXT:
[Include key details from founder brief]

RESEARCH FOCUS:
- Psychographic profile of ideal customers
- Emotional triggers and aspirations
- Jobs-to-be-Done (functional, emotional, social)
- Where this audience spends time online
- Language and terminology they use
- What brands do they currently trust and why?

TOOLS TO USE:
- Use sequential thinking MCP for structured audience analysis
- Use WebSearch extensively to discover community discussions, forums, Reddit threads, and social platforms
- Use WebFetch to read the full content of promising discussions found — extract pain points, language patterns, and authentic customer voices
- Use AskUserQuestion to validate findings with the founder ("Does this match your ideal customer?")

Deliver a detailed audience profile that will inform brand positioning and voice.
```

**Save to:** `docs/brand/00-discovery/02-audience-research.md` → **Review with ai-writing-detector**

### Step 1.3: Competitive Brand Audit (Agent)

**Use Task tool** to launch `brand-competitive-auditor`:

```
Conduct a brand audit of competitors in this space. ultrathink

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

TOOLS TO USE:
- Use sequential thinking MCP to systematically analyze each competitor
- Use WebSearch extensively to discover competitor brands, review sites, and visual identity examples
- Use WebFetch to read competitor About pages, Mission pages, and review content — deeply analyze their positioning, values, and messaging
- Use AskUserQuestion to confirm competitor list with founder ("Anyone I'm missing?")

Deliver a competitive brand map with clear differentiation opportunities.
```

**Save to:** `docs/brand/00-discovery/03-competitive-audit.md` → **Review with ai-writing-detector**

### Step 1.4: Brand Naming (If Needed)

**Only if the founder does NOT have a name yet.** If they have a name they're committed to, skip this step.

Use AskUserQuestion to confirm:
"You mentioned you don't have a brand name yet. Would you like to develop one now before we build the rest of your brand identity? The name will influence your positioning, messaging, and visual identity — so it's best to settle it first."

- Yes, let's develop a name now (Recommended)
- I want to continue without a name for now and come back to it
- I have a working name I'd like to use: [input]

**If developing a name:**

**Use Task tool** to launch `brand-naming-specialist`:

```
Develop brand name options for this startup. ultrathink

FOUNDER CONTEXT:
[Include key details from founder brief — what they do, who they serve, their vision]

AUDIENCE INSIGHTS:
[Key insights from audience research — who needs to resonate with this name]

COMPETITIVE LANDSCAPE:
[Key insights from competitive audit — names to differentiate from]

NAMING APPROACH:
Guide the founder through an interactive naming process:
1. Understand naming preferences and constraints
2. Develop names across multiple approaches (descriptive, suggestive, abstract, etc.)
3. Check availability (domain, trademark conflicts)
4. Present 5-7 vetted options with strategic rationale
5. Refine based on founder feedback
6. Select final name

TOOLS TO USE:
- Use sequential thinking MCP to systematically develop and evaluate name options
- Use WebSearch to discover domain availability tools, trademark databases, and existing brands using similar names
- Use WebFetch to read domain/trademark search results and existing brand pages — verify true availability and understand usage context
- Use AskUserQuestion throughout: preferences, presenting options, refinement, final selection
```

**After name selection, use AskUserQuestion:**
"You've chosen **[Name]** for your brand. Before we continue, please confirm:"
- Yes, I'm committed to this name — let's build the brand identity around it
- I'd like to explore more options first
- I want to proceed but keep the name tentative for now

**Save to:** `docs/brand/00-discovery/04-brand-name.md` → **Review with ai-writing-detector**

**Important:** Update the `[Brand Name]` placeholder in all subsequent files with the selected name.

---

## PHASE 2: Brand Strategy

### Step 2.1: Purpose, Mission, Vision (Agent)

**Use Task tool** to launch `brand-purpose-architect`:

```
Define the brand purpose, mission, and vision for this startup. ultrathink

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

TOOLS TO USE:
- Use sequential thinking MCP to excavate the founder's true WHY through multiple lenses
- Use AskUserQuestion to dig deeper into founder motivation and validate purpose resonates
- Use WebSearch to discover inspiring purpose-driven brands and find their About/Purpose pages
- Use WebFetch to read the full About/Purpose pages of inspiring brands — study how they articulate their WHY, mission language, and vision statements
```

**Save to:** `docs/brand/01-strategy/01-purpose-mission-vision.md` → **Review with ai-writing-detector**

### Step 2.2: Core Values (Agent)

**Use Task tool** to launch `brand-values-curator`:

```
Define 3-4 core values for this brand. ultrathink

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

TOOLS TO USE:
- Use sequential thinking MCP to filter generic values and test each for specificity/authenticity
- Use AskUserQuestion to uncover non-negotiables and validate values feel true to founder
- Use WebSearch to discover competitor values pages and values-forward brand examples
- Use WebFetch to read competitor values pages in full — analyze their exact language, framing, and identify opportunities for differentiation
```

**Save to:** `docs/brand/01-strategy/02-core-values.md` → **Review with ai-writing-detector**

### Step 2.3: Positioning (Agent)

**Use Task tool** to launch `brand-positioning-strategist`:

```
Develop the brand positioning strategy. ultrathink

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

TOOLS TO USE:
- Use sequential thinking MCP to rigorously map competitive positions and find white space
- Use AskUserQuestion to validate positioning dimensions and confirm territory feels right
- Use WebSearch to discover competitor homepages, case studies, and positioning articles
- Use WebFetch to read competitor homepages and positioning content in full — understand their complete positioning narrative and identify white space
```

**Save to:** `docs/brand/01-strategy/03-positioning.md` → **Review with ai-writing-detector**

### Step 2.4: Brand Archetype (Agent)

**Use Task tool** to launch `brand-archetype-selector`:

```
Select the brand archetype(s) for this startup. ultrathink

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

TOOLS TO USE:
- Use sequential thinking MCP to systematically map brand inputs to archetype qualities
- Use AskUserQuestion to validate archetype resonates with founder's vision
- Use WebSearch to discover archetype case studies, brand analysis articles, and competitive archetype examples
- Use WebFetch to read archetype case studies and brand analysis articles — understand how successful brands embody specific archetypes
```

**Save to:** `docs/brand/01-strategy/04-archetype.md` → **Review with ai-writing-detector**

### Step 2.5: Brand Personality and Voice (Agent)

**Use Task tool** to launch `brand-voice-architect`:

```
Define the brand personality and voice. ultrathink

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

TOOLS TO USE:
- Use sequential thinking MCP to translate archetype and personality into specific voice qualities
- Use AskUserQuestion to understand founder's communication style preferences
- Use WebSearch to discover public style guides and voice-forward brand examples (Mailchimp, Slack, 18F, etc.)
- Use WebFetch to read actual style guides and voice documentation — study how leading brands document their voice, structure guidelines, and provide examples
```

**Save to:** `docs/brand/01-strategy/05-brand-personality-voice.md` → **Review with ai-writing-detector**

---

## PHASE 3: Brand Messaging

### Step 3.1: Messaging Framework (Agent)

**Use Task tool** to launch `brand-messaging-architect`:

```
Create the brand messaging framework. ultrathink

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

TOOLS TO USE:
- Use sequential thinking MCP to build messaging hierarchy from value prop through pillars to key messages
- Use AskUserQuestion to validate key messages resonate and identify priority pillars
- Use WebSearch to discover competitor landing pages, product pages, and messaging examples
- Use WebFetch to read competitor landing pages and product copy — analyze their full messaging hierarchy, value propositions, and proof points
```

**Save to:** `docs/brand/02-messaging/01-messaging-framework.md` → **Review with ai-writing-detector**

### Step 3.2: Tagline (Agent)

**Use Task tool** to launch `brand-tagline-creator`:

```
Create brand tagline options. ultrathink

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

TOOLS TO USE:
- Use sequential thinking MCP to systematically explore each tagline angle and filter for best options
- Use AskUserQuestion to understand tagline preferences before generating and to refine after
- Use WebSearch to discover tagline databases, famous tagline case studies, and competitive taglines
- Use WebFetch to read tagline articles and case studies — understand the context, history, and effectiveness of inspiring taglines
```

**Save to:** `docs/brand/02-messaging/02-tagline.md` → **Review with ai-writing-detector**

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
Create the brand elevator pitch. ultrathink

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

TOOLS TO USE:
- Use sequential thinking MCP to structure pitch flow and ensure natural speech rhythm
- Use AskUserQuestion to understand pitch contexts and validate pitches feel natural to say
```

**Save to:** `docs/brand/02-messaging/03-elevator-pitch.md` → **Review with ai-writing-detector**

---

## PHASE 4: Visual Identity Direction

**Note to user:** "Claude can provide detailed creative direction for visual identity, but not actual designs. The outputs from this phase are briefs for a designer or specifications you can implement yourself."

### Step 4.1: Overall Visual Direction (Agent)

**Use Task tool** to launch `brand-visual-director`:

```
Create the visual identity direction for this brand. ultrathink

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

TOOLS TO USE:
- Use sequential thinking MCP to translate brand strategy into visual language systematically
- Use AskUserQuestion to understand visual preferences, logo style preferences, and validate direction
- Use WebSearch to discover competitor websites, design agency portfolios, and brand case studies
- Use WebFetch to read brand case study pages and design portfolio writeups — understand the strategic rationale behind visual identity decisions
```

**Save to:** `docs/brand/03-visual/01-visual-direction.md` → **Review with ai-writing-detector**

### Step 4.2: Color Palette (Agent)

**Use Task tool** to launch `brand-color-strategist`:

```
Develop the brand color palette. ultrathink

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

TOOLS TO USE:
- Use sequential thinking MCP to build color palette from brand psychology through to specific values
- Use AskUserQuestion to understand color preferences/constraints and validate primary color direction
- Use WebSearch to discover competitor brand colors, color psychology resources, and brand color case studies
- Use WebFetch to read color psychology articles and brand color case studies — understand the research behind color associations and how brands justify their palettes
```

**Save to:** `docs/brand/03-visual/02-color-palette.md` → **Review with ai-writing-detector**

### Step 4.3: Typography (Agent)

**Use Task tool** to launch `brand-typography-curator`:

```
Develop the brand typography system. ultrathink

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

TOOLS TO USE:
- Use sequential thinking MCP to match brand personality to typeface qualities and build hierarchy
- Use AskUserQuestion to understand typography constraints (free fonts needed? existing fonts?)
- Use WebSearch to discover font pairing guides, typography resources (Google Fonts, Adobe Fonts), and brand typography examples
- Use WebFetch to read typography guides, font pairing articles, and foundry pages — understand pairing rationale and access font specimen details
```

**Save to:** `docs/brand/03-visual/03-typography.md` → **Review with ai-writing-detector**

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

- Full visual direction brief: `03-visual/01-visual-direction.md`
- Complete messaging framework: `02-messaging/01-messaging-framework.md`
- Audience research: `00-discovery/02-audience-research.md`
- Competitive audit: `00-discovery/03-competitive-audit.md`
```

---

## Process Flow

### How to Guide the User

1. **Start with welcome and overview** — Explain what they'll get and the time investment

2. **Go phase by phase** — Complete each phase before moving to the next

3. **Handle naming early** — If user doesn't have a brand name, address this in Step 1.4 BEFORE moving to Phase 2. The name influences everything else.

4. **Checkpoint after each phase** — Use AskUserQuestion:
   - "We've completed [Phase]. Here's what we have so far: [summary]"
   - "Ready to move to [Next Phase], or would you like to review/adjust anything?"

5. **Build on previous outputs** — Each agent prompt includes context from previous steps

6. **Save as you go** — Don't wait until the end; save each output to its file

7. **End with the complete package** — Compile everything and celebrate

### Using MCP Tools Throughout

**Each agent prompt MUST include these tool instructions:**

1. **ultrathink** — Trigger deep reasoning for complex decisions
2. **Sequential thinking MCP** (`mcp__plugin_claude-vibes_sequential-thinking__sequentialthinking`) — For structured, multi-step analysis
3. **AskUserQuestion tool** — For interactive, guided experience with the founder
4. **WebSearch** — For discovering sources (competitors, examples, availability tools, resources)
5. **WebFetch** — For reading discovered pages in full (competitor About pages, style guides, case studies, research articles)
6. **ai-writing-detector agent** — After saving each document, review for AI writing patterns and refine

**The WebSearch → WebFetch workflow:**
- WebSearch DISCOVERS relevant URLs and gives snippets
- WebFetch READS the full content of promising pages
- Example: WebSearch finds a competitor's website → WebFetch reads their About page to analyze positioning

**AI Writing Review workflow (REQUIRED after every document save):**

After saving ANY brand document to `docs/brand/`, you MUST review it for AI writing patterns and refine as needed. This ensures all brand content sounds authentic and human.

**Use Task tool** to launch `ai-writing-detector`:

```
Review this brand document for AI writing patterns and refine as needed. ultrathink

FILE TO REVIEW: [path to saved document, e.g., docs/brand/00-discovery/01-founder-brief.md]

Use sequential thinking MCP to systematically:
1. Read the document thoroughly
2. Identify specific passages that exhibit AI writing patterns:
   - Generic corporate-speak
   - Overly formal or robotic language
   - Repetitive sentence structures
   - Hedging language ("It's important to note that...")
   - Lists of obvious statements
   - Lack of specific, authentic voice
3. If AI patterns are detected:
   - Rewrite affected passages to sound more authentic and human
   - Preserve the strategic content and meaning
   - Make the voice match the brand personality being developed
   - Use more specific, concrete language
   - Save the refined version to the same file path
4. If the content passes review, confirm it's ready and move on
```

This review step ensures every brand deliverable sounds like it was written by a human brand strategist, not generated by AI.

Ensure each agent is receiving the context it needs and that users are actively engaged throughout.

### If User Wants to Skip or Pause

Use AskUserQuestion to confirm:
- "You can pause anytime and continue later — all work is saved to `docs/brand/`"
- "Would you like to skip [Phase] for now? Note: later phases build on earlier ones, so you may get less tailored results."

---

## Guidelines

- **This is interactive** — Use AskUserQuestion frequently to gather input and confirm direction
- **Always use specialized agents** — Don't generate brand elements yourself; launch the appropriate agent
- **Agents ultrathink** — Each agent prompt includes "ultrathink" and instructions to use AskUserQuestion, sequential thinking MCP, WebSearch, and WebFetch
- **WebSearch → WebFetch workflow** — WebSearch discovers sources; WebFetch reads them deeply for analysis
- **Review all outputs for AI writing** — After saving each document, ALWAYS use ai-writing-detector agent to identify and refine any passages that sound generic or robotic; brand content must sound authentically human
- **Name before strategy** — If no name exists, develop one in Step 1.4 before Phase 2; the name influences everything
- **Build context cumulatively** — Each agent prompt includes relevant context from previous phases
- **Save everything** — Create the file structure as you go
- **Celebrate progress** — Brand building is a journey; acknowledge milestones
- **Be educational** — Explain WHY each element matters as you go
- **Respect founder intuition** — They know their business; guide, don't dictate

## Startup Context

User's startup: $ARGUMENTS

If no context provided, begin with:
"I'm excited to help you create a complete brand identity for your startup! This process will guide you through discovery, strategy, messaging, and visual direction. Let's start with the basics — tell me about your startup."
