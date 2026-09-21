---
description: Finalize brand name with domain verification
argument-hint: Your brand name if you have one, or naming preferences
allowed-tools: Read, Glob, Grep, Skill, Agent, Write, Edit, WebSearch, WebFetch, AskUserQuestion
---

# Finalize brand name

You are helping a startup founder finalize their brand name. Whether they already have a name or need to develop one, this step ensures the name is verified and documented before moving to Strategy.

## Context loading

**Founder Brief** (required):
@docs/00-BRAND/00-DISCOVERY/01-founder-brief.md

**Audience Research** (optional):
@docs/00-BRAND/00-DISCOVERY/02-audience-research.md

**Competitive Audit** (optional):
@docs/00-BRAND/00-DISCOVERY/03-competitive-audit.md

**Check above:** If no founder brief content loaded, **STOP** and tell the user to run `/00-BRAND:00-discover/01-discover-founder` first.

Optional input: $ARGUMENTS

## Your role

**Use the AskUserQuestion tool for every question to the user. Never ask questions as plain text output.** The AskUserQuestion tool ensures a guided, interactive experience with structured options. Every single user question must go through this tool.

First, check the founder brief to determine if they already have a brand name:

**If they have a name they're committed to:**
1. Verify domain availability using whois MCP
2. Check for trademark conflicts
3. Document the name and its status
4. Skip the naming agent unless they want alternatives

**If they need a name:**
Use the Agent tool to launch the brand-naming-specialist agent (instructions below).

## Interactive experience (critical)

**Use the AskUserQuestion tool whenever you interact with the user.** This ensures a guided, interactive experience where the founder feels engaged and consulted throughout the branding process.

Use AskUserQuestion to:
- Gather preferences before launching agents
- Present options with clear tradeoffs
- Validate agent outputs before saving
- Get feedback and iterate on results

Never save final outputs without user approval.

## Natural writing

The brand-naming-specialist agent has the `natural-writing` skill preloaded, so its output should read like a thoughtful person wrote it. Before you write anything yourself in this command, such as a summary or a saved document, **use the Skill tool** to invoke `claude-vibes:natural-writing`, apply its method while drafting, and run its structural audit before showing the draft. Add its "What changed" section only when you are revising text the user gave you.

## When the work deserves a graph

Some requests here are bigger than one pass: naming, which combines option generation, comparison against criteria, and trademark and domain checks before the founder decides. When the work involves several steps or sources, paths that can run in parallel, checks, real risk, or approvals, use AskUserQuestion to offer designing it first with the `claude-vibes:graph-engineering` skill. The skill decides whether a graph is warranted, and it stops at the user's approval. To carry out an approved graph, follow the `claude-vibes:graph-running` skill, using the brand-naming-specialist agent for generation and comparison, the Whois tool for domain checks, and a gate for the founder's final choice. For a simple request, skip this and carry on below.

## For founders with an existing name

Use whois MCP (`mcp__plugin_claude-vibes_whois__whois_domain`) to verify their domain:
1. Check [name].com first
2. If taken, check alternatives (.io, .co, etc.)
3. Use WebSearch to check for trademark conflicts
4. Use AskUserQuestion to confirm they want to proceed with this name

## For founders who need a name

**Use Agent tool** with `subagent_type: "claude-vibes:BRANDING:brand-naming-specialist"` and this prompt:

```
Develop brand name options for this startup. ultrathink

## FOUNDER CONTEXT

**Business**: [Extract from founder brief: what they do]
**Problem Solved**: [Extract: the core problem]
**Target Customer**: [From audience research: who the customers are]
**What Customers Value**: [From audience research: key values, motivations]

## COMPETITIVE LANDSCAPE

[From competitive audit if available: names to differentiate from, naming patterns in the space]

## Critical: interactive discovery

**Use the AskUserQuestion tool throughout to keep the experience interactive and guided:**
- Gather preferences and opinions before making recommendations
- Present options with clear tradeoffs for the user to choose from
- Validate findings and get feedback before proceeding
- Confirm final outputs resonate before saving

Never make significant decisions without user input. The brand identity belongs to them.

## NAMING APPROACH

Guide the founder through an interactive naming process:

### Phase 1: Understand preferences
Use AskUserQuestion to gather:
- Style preferences (modern, classic, playful, serious)
- Length preferences (1, 2, or 3+ syllables)
- Any must-avoid sounds, letters, or associations
- Budget for premium domains if needed
- Position preference on naming matrix (descriptive → suggestive → abstract)

### Phase 2: Generate candidates
Generate 10-15 candidate names across approaches:
- Descriptive (says what you do)
- Suggestive (hints at benefits), recommended for most startups
- Abstract (invented words)
- Compound (two words combined)
- Metaphorical (symbolic representation)

Apply sound symbolism thinking:
- V sounds = vibrant, alive
- B sounds = reliable, solid
- Plosives (b, c, k, p) = memorable
- Soft sounds (l, m, n) = approachable

### Phase 3: Verify domain availability (required - do not skip)

For each candidate name, check domain availability using whois MCP:

a. Check .com first:
   Call `mcp__plugin_claude-vibes_whois__whois_domain` with "[name].com"

b. If .com is taken, check alternatives:
   - [name].io
   - [name].co
   - [name]app.com
   - get[name].com

c. Record availability for each name:
   - ✅ .com available → top priority, present first
   - 🟡 .com taken but .io/.co available → Present as alternative option
   - ❌ All common TLDs taken → do not present (unless truly exceptional)

### Phase 4: Apply evaluation frameworks

For each domain-verified candidate, evaluate using:

**SMILE Test** (score each 1-5):
- Suggestive: evokes something about the brand?
- Memorable: makes an association with the familiar?
- Imagery: aids memory through evocative visuals?
- Legs: lends itself to extended wordplay and branding?
- Emotional: moves people?

**SCRATCH Filter** (must pass all):
- Not Spelling Challenged (no typos)
- Not Copycat (distinct from competitors)
- Not Restrictive (allows growth)
- Not Annoying (feels natural)
- Not Tame (distinctive)
- No Curse of Knowledge (accessible)
- Not Hard to Pronounce (easy to say)

### Phase 5: Present 5-7 domain-verified options

Use the Name Candidate Table format:

| # | Name | Domain | Status | Category | Strategic Rationale |
|---|------|--------|--------|----------|---------------------|
| 1 | [Name] | [name].com | ✅ Available | Suggestive | [Why it fits] |

For each name include:
- The name and recommended domain
- Availability status with verification timestamp
- SMILE score (/25)
- Strategic rationale (why this name fits the brand)
- Pronunciation and spelling considerations
- Position on naming matrix

### Phase 6: Refine based on feedback

Use AskUserQuestion to get founder feedback:
- If they like a direction, generate more options in that style
- Re-verify domains for any new candidates
- Iterate until they find options they love

### Phase 7: Confirm final selection

Before finalizing:
- Verify domain is still available (can change quickly)
- Recommend founder purchase domain immediately
- Check trademark conflicts via WebSearch
- Document runner-up names

## Critical rules

1. **Never present a name without verified domain availability**: founders fall in love with names; don't let them fall for one they can't own
2. **A good-enough name with .com is better than a perfect name without**
3. **Two syllables is optimal** for memorability
4. **Push past comfort**: the best names often feel uncomfortable at first (Sonos was rejected as "not entertainment enough")

## TOOLS TO USE

- **Whois MCP** (`mcp__plugin_claude-vibes_whois__whois_domain`): required for every name before presenting
- **Structured reasoning**: systematically develop and evaluate options
- **WebSearch**: check trademark databases and existing brands
- **WebFetch**: read trademark results and brand pages
- **AskUserQuestion**: gather preferences, present options, get feedback
```

## After agent returns

Use AskUserQuestion to confirm the final choice:

"You've chosen **[Name]** for your brand. Before we continue, please confirm:"
- Yes, I'm committed to this name. Let's build the brand identity around it
- I'd like to explore more options first
- I want to proceed but keep the name tentative for now

## Guidelines

- Domain availability is non-negotiable: don't let founder fall for unavailable names
- A good-enough name with .com is better than a perfect name without
- Encourage founder to purchase domain immediately after selection
- Check for trademark conflicts before finalizing
- Reference the `brand-naming-strategies` skill templates for consistent formatting

## Output

After the founder confirms their selection:

1. Ensure `docs/00-BRAND/00-DISCOVERY/` directory exists
2. Save to `docs/00-BRAND/00-DISCOVERY/04-brand-name.md` using the Final Selection Documentation Template from the skill

3. **Next step:** "Discovery phase complete! Run `/00-BRAND:01-strategy/01-define-purpose` to begin building your brand strategy."
