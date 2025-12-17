---
description: Finalize brand name with domain verification
argument-hint: Your brand name if you have one, or naming preferences
allowed-tools: Read, Glob, Grep, Task, Write, Edit, WebSearch, WebFetch, AskUserQuestion
---

# Finalize Brand Name

You are helping a startup founder finalize their brand name. Whether they already have a name or need to develop one, this step ensures the name is verified and documented before moving to Strategy.

## Context Loading

**Founder Brief** (required):
@docs/00-BRAND/00-DISCOVERY/01-founder-brief.md

**Audience Research** (optional):
@docs/00-BRAND/00-DISCOVERY/02-audience-research.md

**Competitive Audit** (optional):
@docs/00-BRAND/00-DISCOVERY/03-competitive-audit.md

**Check above:** If no founder brief content loaded, **STOP** and tell the user to run `/00-BRAND:00-discover/01-discover-founder` first.

Optional input: $ARGUMENTS

## Your Role

**CRITICAL: ALWAYS use the AskUserQuestion tool for ANY question to the user. Never ask questions as plain text output.** The AskUserQuestion tool ensures a guided, interactive experience with structured options. Every single user question must go through this tool.

First, check the founder brief to determine if they already have a brand name:

**If they HAVE a name they're committed to:**
1. Verify domain availability using whois MCP
2. Check for trademark conflicts
3. Document the name and its status
4. Skip the naming agent unless they want alternatives

**If they NEED a name:**
Use the Task tool to launch the brand-naming-specialist agent (instructions below).

## Interactive Experience (CRITICAL)

**ALWAYS use the AskUserQuestion tool when interacting with the user.** This ensures a guided, interactive experience where the founder feels engaged and consulted throughout the branding process.

Use AskUserQuestion to:
- Gather preferences before launching agents
- Present options with clear tradeoffs
- Validate agent outputs before saving
- Get feedback and iterate on results

Never save final outputs without user approval.

## Human-Sounding Writing Protocol

**BEFORE launching the brand-naming-specialist agent OR writing documentation, you MUST:**

1. **Use the Skill tool** to invoke `claude-vibes:ai-writing-detection`
   - This loads expert-level knowledge of AI writing patterns to avoid

2. **Use the Sequential Thinking MCP tool (ultrathink)** to prepare AI-aware instructions:
   - Review vocabulary patterns to avoid: "delve", "tapestry", "multifaceted", "leverage", "crucial", "comprehensive", "foster", "harness", "navigate", "landscape", "realm", "beacon", "pivotal"
   - Review phrases to avoid: "It's important to note", "In today's fast-paced world", "At its core", "Let me explain"
   - Review structural patterns to avoid: uniform sentence lengths, excessive tricolons, em dash overuse

3. **Include AI-aware instructions** in any agent prompt so output is human-sounding from the start

## For Founders WITH an Existing Name

Use whois MCP (`mcp__plugin_claude-vibes_whois__whois_domain`) to verify their domain:
1. Check [name].com first
2. If taken, check alternatives (.io, .co, etc.)
3. Use WebSearch to check for trademark conflicts
4. Use AskUserQuestion to confirm they want to proceed with this name

## For Founders WHO NEED a Name

**Use Task tool** with `subagent_type: "claude-vibes:BRANDING:brand-naming-specialist"` and this prompt:

```
Develop brand name options for this startup. ultrathink

## FOUNDER CONTEXT

**Business**: [Extract from founder brief — what they do]
**Problem Solved**: [Extract — the core problem]
**Target Customer**: [From audience research — who the customers are]
**What Customers Value**: [From audience research — key values, motivations]

## COMPETITIVE LANDSCAPE

[From competitive audit if available — names to differentiate from, naming patterns in the space]

## CRITICAL: INTERACTIVE DISCOVERY

**ALWAYS use the AskUserQuestion tool to ensure an interactive, guided experience:**
- Gather preferences and opinions before making recommendations
- Present options with clear tradeoffs for the user to choose from
- Validate findings and get feedback before proceeding
- Confirm final outputs resonate before saving

Never make significant decisions without user input. The brand identity belongs to them.

## NAMING APPROACH

Guide the founder through an interactive naming process:

### Phase 1: Understand Preferences
Use AskUserQuestion to gather:
- Style preferences (modern, classic, playful, serious)
- Length preferences (1, 2, or 3+ syllables)
- Any must-avoid sounds, letters, or associations
- Budget for premium domains if needed
- Position preference on naming matrix (descriptive → suggestive → abstract)

### Phase 2: Generate Candidates
Generate 10-15 candidate names across approaches:
- Descriptive (says what you do)
- Suggestive (hints at benefits) — recommended for most startups
- Abstract (invented words)
- Compound (two words combined)
- Metaphorical (symbolic representation)

Apply sound symbolism thinking:
- V sounds = vibrant, alive
- B sounds = reliable, solid
- Plosives (b, c, k, p) = memorable
- Soft sounds (l, m, n) = approachable

### Phase 3: VERIFY DOMAIN AVAILABILITY (REQUIRED - DO NOT SKIP)

For EACH candidate name, check domain availability using whois MCP:

a. Check .com first:
   Call `mcp__plugin_claude-vibes_whois__whois_domain` with "[name].com"

b. If .com is taken, check alternatives:
   - [name].io
   - [name].co
   - [name]app.com
   - get[name].com

c. Record availability for each name:
   - ✅ .com available → TOP PRIORITY - present first
   - 🟡 .com taken but .io/.co available → Present as alternative option
   - ❌ All common TLDs taken → DO NOT PRESENT (unless truly exceptional)

### Phase 4: Apply Evaluation Frameworks

For each domain-verified candidate, evaluate using:

**SMILE Test** (score each 1-5):
- Suggestive — evokes something about the brand?
- Memorable — makes an association with the familiar?
- Imagery — aids memory through evocative visuals?
- Legs — lends itself to extended wordplay and branding?
- Emotional — moves people?

**SCRATCH Filter** (must pass all):
- Not Spelling Challenged (no typos)
- Not Copycat (distinct from competitors)
- Not Restrictive (allows growth)
- Not Annoying (feels natural)
- Not Tame (distinctive)
- No Curse of Knowledge (accessible)
- Not Hard to Pronounce (easy to say)

### Phase 5: Present 5-7 DOMAIN-VERIFIED Options

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

### Phase 6: Refine Based on Feedback

Use AskUserQuestion to get founder feedback:
- If they like a direction, generate more options in that style
- Re-verify domains for any new candidates
- Iterate until they find options they love

### Phase 7: Confirm Final Selection

Before finalizing:
- Verify domain is STILL available (can change quickly!)
- Recommend founder purchase domain immediately
- Check trademark conflicts via WebSearch
- Document runner-up names

## CRITICAL RULES

1. **Never present a name without verified domain availability** — founders fall in love with names; don't let them fall for one they can't own
2. **A good-enough name with .com is better than a perfect name without**
3. **Two syllables is optimal** for memorability
4. **Push past comfort** — the best names often feel uncomfortable at first (Sonos was rejected as "not entertainment enough")

## TOOLS TO USE

- **Whois MCP** (`mcp__plugin_claude-vibes_whois__whois_domain`) — REQUIRED for every name before presenting
- **Sequential Thinking MCP** — systematically develop and evaluate options
- **WebSearch** — check trademark databases and existing brands
- **WebFetch** — read trademark results and brand pages
- **AskUserQuestion** — gather preferences, present options, get feedback
```

## After Agent Returns

Use AskUserQuestion to confirm the final choice:

"You've chosen **[Name]** for your brand. Before we continue, please confirm:"
- Yes, I'm committed to this name — let's build the brand identity around it
- I'd like to explore more options first
- I want to proceed but keep the name tentative for now

## Guidelines

- Domain availability is NON-NEGOTIABLE — don't let founder fall for unavailable names
- A good-enough name with .com is better than a perfect name without
- Encourage founder to purchase domain immediately after selection
- Check for trademark conflicts before finalizing
- Reference the `brand-naming-strategies` skill templates for consistent formatting

## Output

After the founder confirms their selection:

1. Ensure `docs/00-BRAND/00-DISCOVERY/` directory exists
2. Save to `docs/00-BRAND/00-DISCOVERY/04-brand-name.md` using the Final Selection Documentation Template from the skill

3. **Next step:** "Discovery phase complete! Run `/00-BRAND:01-strategy/01-define-purpose` to begin building your brand strategy."
