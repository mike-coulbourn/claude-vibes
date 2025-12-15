---
description: Select brand archetype for emotional positioning
argument-hint: Optional archetype direction (e.g., "Hero", "Sage")
allowed-tools: Read, Glob, Grep, Task, Write, Edit, WebSearch, WebFetch, AskUserQuestion
---

# Select Brand Archetype

You are helping a startup founder select their brand archetype using the 12 Jungian archetypes. This establishes the emotional personality foundation that guides all brand expression.

## Context Loading

**Founder Brief** (required):
@docs/00-BRAND/00-DISCOVERY/01-founder-brief.md

**Audience Research** (optional):
@docs/00-BRAND/00-DISCOVERY/02-audience-research.md

**Competitive Audit** (optional):
@docs/00-BRAND/00-DISCOVERY/03-competitive-audit.md

**Brand Name** (optional):
@docs/00-BRAND/00-DISCOVERY/04-brand-name.md

**Purpose/Mission/Vision** (required):
@docs/00-BRAND/01-STRATEGY/01-purpose-mission-vision.md

**Core Values** (optional):
@docs/00-BRAND/01-STRATEGY/02-core-values.md

**Positioning** (optional):
@docs/00-BRAND/01-STRATEGY/03-positioning.md

**Check above:** If founder brief or purpose/mission/vision content is missing, **STOP** and tell the user to complete prerequisites first.

Optional archetype direction: $ARGUMENTS

## Your Role

**CRITICAL: You MUST use the Task tool to launch the brand-archetype-selector agent.** Do not select archetypes yourself — that's what the specialized agent is for.

Your job is to:
1. Verify prerequisites exist
2. Extract key context from loaded documents
3. Prepare a comprehensive, structured prompt for the agent
4. Launch the agent
5. Save and review the results

## Interactive Experience (CRITICAL)

**ALWAYS use the AskUserQuestion tool when interacting with the user.** This ensures a guided, interactive experience where the founder feels engaged and consulted throughout the branding process.

Use AskUserQuestion to:
- Gather preferences before launching agents
- Present options with clear tradeoffs
- Validate agent outputs before saving
- Get feedback and iterate on results

Never save final outputs without user approval.

## Launch the Agent

**Use Task tool** with `subagent_type: "claude-vibes:BRANDING:brand-archetype-selector"` and this prompt:

```
Select the brand archetype(s) for this startup. ultrathink

## FOUNDER CONTEXT

**Business**: [Extract from founder brief — what they do]
**Founder Personality**: [From founder brief — personality traits, style]
**Founder Motivation**: [Why they started — what drives them]
**What They Admire**: [From founder brief — brands/people they respect]

## PURPOSE FOUNDATION

**Purpose (WHY)**: [From purpose-mission-vision.md]
**Mission (HOW)**: [From purpose-mission-vision.md]
**Vision (WHERE)**: [From purpose-mission-vision.md]
**Core Values**: [From core-values.md if exists]

## AUDIENCE INSIGHTS

**Who They Serve**: [From audience research — primary customer segment]
**Audience Aspirations**: [What customers aspire to]
**Audience Fears**: [What customers fear/avoid]
**Emotional Needs**: [What emotional needs you fulfill]

## COMPETITIVE LANDSCAPE

**Industry**: [What industry/category]
**Industry Default Archetype**: [The expected archetype for this industry]
**Competitor Archetypes**: [From competitive audit — what archetypes competitors use]
**Differentiation Opportunity**: [Archetype gaps in competitive set]

## POSITIONING CONTEXT

**Positioning Strategy**: [From positioning.md if exists]
**Emotional Territory to Own**: [From positioning — what feelings we want to claim]

## BRAND NAME

**Name**: [From brand name document]
**Name Rationale**: [Why this name — may inform archetype expression]

## CRITICAL: INTERACTIVE DISCOVERY

**ALWAYS use the AskUserQuestion tool to ensure an interactive, guided experience:**
- Gather preferences and opinions before making recommendations
- Present options with clear tradeoffs for the user to choose from
- Validate findings and get feedback before proceeding
- Confirm final outputs resonate before saving

Never make significant decisions without user input. The brand identity belongs to them.

## DISCOVERY APPROACH

### Phase 1: Context Analysis
Analyze all inputs to understand:
- Brand purpose and values
- Target audience characteristics
- Competitive positioning
- Founder personality
- Desired emotional territory

### Phase 2: Audience Archetype Alignment
Understand what archetypes resonate with the target audience:
- What do they aspire to? (Hero, Ruler, Magician)
- What do they fear? (determines avoidance)
- What emotional needs do we fulfill?
- What brands do they love and why?

### Phase 3: Competitive Archetype Mapping
Map the competitive landscape:
- What archetype is each competitor?
- What archetypes are overused in this space?
- What archetypes are underrepresented?
- Is there white space for differentiation?

### Phase 4: Apply the 70/30 Rule
Select archetypes using the Mark-Pearson methodology:
- **Primary archetype (70%)** — core personality, aligned with purpose
- **Secondary archetype (30%)** — for differentiation
- Validate combinations are complementary, not conflicting

### Phase 5: Validate Selection
Run validation tests:
- **Authenticity Test**: Does this feel true to the founder?
- **Audience Test**: Does this resonate with customers?
- **Differentiation Test**: Does this stand out from competitors?
- **Consistency Test**: Can we express this across all touchpoints?
- **Shadow Test**: Can we avoid the archetype's dark side?

### Phase 6: Document Expression
Define how archetype manifests:
- Voice and personality traits
- Visual identity direction
- Experience guidelines
- Marketing approach

## TOOLS TO USE

- **Sequential Thinking MCP**: Systematically evaluate each archetype against brand context, map competitive archetypes, validate combinations
- **AskUserQuestion**: Validate archetype resonates with founder's vision, get input on emotional territory
- **WebSearch**: Research archetype case studies, competitive brand analysis, successful archetype implementations
- **WebFetch**: Read competitor about pages and brand materials — understand their archetypal expression to differentiate

## OUTPUT REQUIREMENTS

Deliver the complete archetype documentation using the Archetype Documentation Template from the `brand-archetype-selection` skill. Must include:

1. **Executive Summary**
2. **Context Review** (purpose, values, audience, positioning)
3. **Audience Archetype Alignment** (what archetypes resonate)
4. **Competitive Archetype Landscape** (competitor mapping)
5. **Primary Archetype Recommendation** (full profile with rationale)
6. **Secondary Archetype Recommendation** (complement rationale)
7. **Alternative Archetypes Considered** (with fit scores)
8. **Archetype Expression Guide** (voice, visuals, experience)
9. **Shadow Side Analysis** (risks and mitigation)
10. **Quick Reference Card** (summary for daily use)
```

## Guidelines

- **Apply the 70/30 rule**: One clear primary, one complementary secondary
- **Authenticity matters**: The archetype must feel true to the founder
- **Audience alignment**: The archetype must resonate with customers
- **Competitive differentiation**: Consider what archetypes competitors use
- **Avoid the shadow**: Every archetype has a dark side to watch for
- **Consistency is key**: Once chosen, express the archetype consistently

## Output

After the agent returns:

1. Ensure `docs/00-BRAND/01-STRATEGY/` directory exists
2. Save to `docs/00-BRAND/01-STRATEGY/04-archetype.md`

3. Use Task tool to launch `claude-vibes:TOOLKIT:ai-writing-detector` agent to review the document for AI patterns and refine if needed.

4. **Next step:** "Run `/00-BRAND:01-strategy/05-define-voice` to define your brand personality and voice."
