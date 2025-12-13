---
description: Audit competitor brands to find differentiation opportunities
argument-hint: Optional specific competitors to analyze
allowed-tools: Read, Glob, Grep, Task, Write, Edit, WebSearch, WebFetch, AskUserQuestion
---

# Audit Competitor Brands

You are helping a startup founder understand the competitive brand landscape. This audit focuses on BRAND positioning, not just product features — visual identity, messaging, voice, and positioning.

## Prerequisites Check

**Founder brief status:** !`test -f docs/brand/00-discovery/01-founder-brief.md && echo "✓ Found" || echo "✗ MISSING - Run /00-BRAND:00-discover/01-discover-founder first"`

If the founder brief is missing, **STOP** and tell the user to run `/00-BRAND:00-discover/01-discover-founder` first.

## Context Loading

**Founder Brief** (auto-loaded):
@docs/brand/00-discovery/01-founder-brief.md

**Audience Research** (auto-loaded if exists):
@docs/brand/00-discovery/02-audience-research.md

Optional specific competitors: $ARGUMENTS

## Your Role

**CRITICAL: You MUST use the Task tool to launch the brand-competitive-auditor agent.** Do not do the competitive audit yourself — that's what the specialized agent is for.

Your job is to:
1. Verify prerequisites exist
2. Extract key context from loaded documents
3. Prepare a comprehensive, structured prompt for the agent
4. Launch the agent
5. Save and review the results

## Launch the Agent

**Use Task tool** with `subagent_type: "claude-vibes:BRANDING:brand-competitive-auditor"` and this prompt:

```
Conduct a comprehensive brand audit of competitors in this space. ultrathink

## STARTUP CONTEXT

**Business**: [Extract from founder brief — what they do]
**Problem Solved**: [Extract — the core problem]
**Target Customer**: [From audience research — who the customers are]
**What Customers Value**: [From audience research — key values, motivations, emotional jobs]

## SPECIFIC COMPETITORS TO ANALYZE

[If user provided any, list them here. Otherwise:]
"Identify 5-10 direct and indirect competitors. Aim for at least 10 for accurate landscape mapping, prioritize top 5-10 for deep analysis."

## RESEARCH OBJECTIVES

### Phase 1: Competitor Discovery & Identification
- Direct competitors (same solution category)
- Indirect competitors (different approaches to same problem)
- Aspirational brands (successful brands in adjacent spaces to learn from)

### Phase 2: Individual Competitor Brand Profiles
For each competitor, document:
- Visual identity (logo style, colors with hex values, typography, imagery)
- Positioning (tagline, claims, differentiation angle)
- Voice and tone (sample language, personality traits)
- Only-ness Assessment (can they complete the Only-ness Statement?)
- Good/Different Chart position (1-10 scores with rationale)

### Phase 3: Visual Landscape Audit Matrices
Create structured matrices for:
- **Color Audit Matrix**: competitor, primary color + hex, secondary colors, mood
- **Typography Audit Matrix**: competitor, typeface, style (serif/sans), weights
- **Imagery Style Audit**: competitor, photo vs illustration, subjects, mood, quality

### Phase 4: Strategic Analysis
- **Perceptual Map** with two relevant axes (choose based on what matters to customers)
- **Visual white space identification**: unclaimed color territories, typography gaps, imagery opportunities
- **Voice differentiation opportunities**: what tones are overused vs. missing?
- **Archetype landscape mapping**: which archetypes dominate? which are available?
- **Good/Different Chart analysis**: plot all competitors, identify quadrant opportunities

### Phase 5: Differentiation Opportunities
Apply the **Zig vs Zag decision framework**:
- Zig factors (reasons to follow conventions)
- Zag factors (reasons to break conventions)
- Recommendation with rationale

Prioritize differentiation by impact: **Color → Typography → Imagery → Layout**

## TOOLS TO USE

- **Sequential Thinking MCP**: Structure analysis through each framework systematically
- **WebSearch**: Search extensively for:
  - `"[competitor name] brand" OR "[competitor name] logo"`
  - `"[competitor name] vs" OR "[competitor name] alternative"`
  - `"[industry] brand design" site:dribbble.com OR site:behance.net`
  - `"[competitor name] review" OR "[competitor name] experience"`
  - `"[competitor name] about" OR "[competitor name] mission"`
  - `"best [solution category]" OR "top [solution category]"`
- **WebFetch**: Read competitor About pages, Mission pages, Homepage copy deeply — extract positioning, voice, and visual identity details
- **AskUserQuestion**: Confirm competitor list with founder ("Anyone I'm missing?")

## OUTPUT REQUIREMENTS

Deliver the complete competitive brand audit using your structured output format. Must include:

1. **Executive Summary** with primary differentiation opportunity
2. **Individual Competitor Profiles** (5-10 competitors)
3. **Visual Audit Matrices** (Color, Typography, Imagery) with patterns and white space identified
4. **Perceptual Map** with axes, competitor positions, and white space
5. **Good/Different Chart** with quadrant analysis
6. **Prioritized Differentiation Recommendations** (Color first, then Typography, then Imagery)
7. **Only-ness Statement Opportunity** for this brand
8. **Zig vs Zag Recommendation** with rationale

Use the templates in the `competitive-visual-audit` skill for matrix formatting.
```

## Guidelines

- The agent does the research — you orchestrate
- Trust the agent's findings but validate with the founder
- Focus on BRAND elements, not just product features
- Look for patterns (everyone uses blue? opportunity for different color)
- Pay attention to what customers complain about — that's differentiation gold
- Note what competitors do well too — don't differentiate for differentiation's sake

## Output

After the agent returns:

1. Ensure `docs/brand/00-discovery/` directory exists
2. Save the competitive audit to `docs/brand/00-discovery/03-competitive-audit.md`

3. Use Task tool to launch `claude-vibes:TOOLKIT:ai-writing-detector` agent to review the document for AI patterns and refine if needed.

4. **Next step:** "Run `/00-BRAND:00-discover/04-name-brand` to explore and finalize your brand name."
