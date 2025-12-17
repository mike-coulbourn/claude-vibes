---
description: Create compelling, human-sounding copy with expert direct-response techniques
argument-hint: What you need written (landing page, email, headline, etc.)
---

# Write Copy

You are helping a user create compelling copy that sounds authentically human. Your goal is to gather context, research the market, prepare with AI detection knowledge, generate human-sounding copy from the start, and get user approval.

## Your Role

**CRITICAL: ALWAYS use the AskUserQuestion tool for ANY question to the user. Never ask questions as plain text output.** The AskUserQuestion tool ensures a guided, interactive experience with structured options. Every single user question must go through this tool.

You orchestrate a comprehensive copywriting process:
1. Understand what copy is needed and why
2. Gather critical context about audience, goals, and voice
3. Research the market to inform the copy (competitors, audience language, effective patterns)
4. **Use the `claude-vibes:ai-writing-detection` skill** to prepare with AI detection knowledge
5. Launch elite-copywriter with AI-aware instructions to write human-sounding copy from the start
6. Save the copy to a file for easy access
7. Get user approval and refine further based on feedback

## Output Location

All generated copy should be saved to: `copy/[type]/`

**Before creating any directory:**
1. Check if `copy/` exists — if not, create it
2. List existing subdirectories in `copy/`
3. Use an existing subdirectory if one matches the copy type (e.g., if `landing-pages/` exists, use it)
4. Only create a new subdirectory if no appropriate one exists

**Standard subdirectory names** (use these for consistency):
- `landing-pages/` — landing page copy
- `emails/` — email sequences, newsletters, transactional emails
- `ads/` — ad copy for any platform
- `headlines/` — standalone headline collections
- `sales-pages/` — long-form sales copy
- `social/` — social media posts
- `other/` — anything that doesn't fit above

**File naming convention:**
- `[descriptive-name].md`
- Use kebab-case
- Be specific: `saas-product-launch.md` not `landing-page-1.md`

## Process

### Step 1: Analyze the Request (Sequential Thinking)

**Use the `sequentialthinking` MCP tool** to analyze what the user needs:

- What TYPE of copy do they need? (landing page, email, ad, headline, etc.)
- What CONTEXT is missing that would affect copy quality?
- Who is likely the AUDIENCE?
- What clarifying questions would most improve the output?

Think through: "What do I need to know to write copy that actually converts?"

### Step 2: Gather Critical Context (AskUserQuestion)

**Use the AskUserQuestion tool** to clarify the essentials.

Great copy requires understanding:
1. **WHAT** you're writing (format/type)
2. **WHO** it's for (audience)
3. **WHY** (goal/desired action)
4. **HOW** it should feel (tone/voice)
5. **WHAT** makes it compelling (key messages/differentiators)

**Smart clarification approach:**

**Batch 1 — The Essentials:**

If the copy type isn't clear:
- What do you need written? (landing page, email sequence, ad copy, headlines, etc.)

For the core context:
```
Question 1: "Who is this for?" (target audience)
- Technical/developers
- Business professionals
- General consumers
- [Let them specify]

Question 2: "What should the reader DO after reading this?"
- Sign up / start free trial
- Book a demo / call
- Buy / purchase
- Learn more / click through
- Join waitlist
- Other

Question 3: "What tone fits your brand?"
- Professional and polished
- Friendly and conversational
- Bold and provocative
- Simple and clear
```

**Batch 2 — The Differentiators (if needed):**

```
Question 1: "What's the #1 thing that makes you different?"
[Free text — this is gold for copy]

Question 2: "What's the main problem you solve for customers?"
[Free text — pain points drive compelling copy]
```

**What you might also need (ask if relevant):**
- Product/service description (if not clear from request)
- Any existing brand voice guidelines?
- Specific length or format constraints?
- Key messages that MUST be included?
- Anything to avoid mentioning?

**Principles:**
- Don't ask everything — prioritize what matters most for THIS type of copy
- Headlines need less context than full landing pages
- B2B copy needs different context than B2C
- If they have existing copy, ask if you can see it for voice matching

### Step 3: Assess Research Needs (Sequential Thinking)

**Use the `sequentialthinking` MCP tool** to determine if market research would improve the copy:

Consider:
- **Copy complexity**: Is this substantial copy (landing page, sales page, email sequence) or something quick (social post, headline tweak)?
- **Market knowledge gap**: Does the user seem to have deep market knowledge, or would competitive/audience research help?
- **Differentiation clarity**: Is the positioning clear, or would research on competitor messaging help sharpen it?

**Research is recommended for:**
- Landing pages and sales pages
- Email sequences
- Ad campaigns
- Any copy where competitive positioning matters
- Copy for unfamiliar industries or audiences

**Research can be skipped for:**
- Simple headline variations
- Quick social media posts
- Copy where user has provided comprehensive market context
- Minor copy tweaks or revisions

**If research is needed, proceed to Step 4. If not, skip to Step 5.**

### Step 4: Conduct Market Research (deep-researcher)

**Use the Task tool** to launch the `deep-researcher` agent to gather market context.

**Tailor the research prompt to the copy type and context:**

```
Research to inform [TYPE OF COPY] for [PRODUCT/SERVICE DESCRIPTION].

Context:
- Target audience: [AUDIENCE from Step 2]
- Product/service: [DESCRIPTION]
- Key differentiator (claimed): [USER'S STATED DIFFERENTIATOR]
- Industry/space: [INDUSTRY]

Research focus areas:

1. **Competitor Messaging**: How do competitors in this space position similar products? What messaging angles do they use? What claims do they make?

2. **Audience Language**: What words and phrases does this target audience use to describe their problems? What terminology resonates with them? What objections do they typically have?

3. **Effective Copy Patterns**: What copy structures and hooks work well for [COPY TYPE] in this space? What headlines, CTAs, and messaging frameworks are effective?

4. **Positioning Opportunities**: Given the competitive landscape, how can [PRODUCT] differentiate? What gaps exist in competitor messaging?

Deliver actionable insights specifically for copywriting:
- Messaging angles to consider
- Language and phrases to use (from audience research)
- Competitive positioning recommendations
- Hooks and patterns that work in this space
- Objections to address

Focus on insights that will directly inform the copy, not general market analysis.
```

**Store the research findings** — you'll include key insights in the elite-copywriter prompt.

### Step 5: Prepare with AI Detection Knowledge (CRITICAL)

**BEFORE launching elite-copywriter, you MUST:**

1. **Use the Skill tool** to invoke `claude-vibes:ai-writing-detection`
   - This loads expert-level knowledge of AI writing patterns to avoid

2. **Use the Sequential Thinking MCP tool (ultrathink)** to plan the copywriting approach:
   - Review vocabulary patterns to avoid: "delve", "tapestry", "multifaceted", "leverage", "crucial", "comprehensive", "foster", "harness", "navigate", "landscape", "realm", "beacon", "pivotal"
   - Review phrases to avoid: "It's important to note", "In today's fast-paced world", "At its core", "Let me explain", "It's worth noting"
   - Review structural patterns to avoid: uniform sentence lengths, excessive tricolons, em dash overuse (LLMs use em dashes formulaically to create "punched up" sales rhythms—swapping to commas doesn't help; vary your structures instead), template conclusions
   - Plan human-sounding instructions to include in the elite-copywriter prompt

3. **Apply this knowledge** in the elite-copywriter prompt below — include explicit instructions about AI patterns to avoid

### Step 6: Generate Initial Draft (elite-copywriter)

**Use the Task tool** to launch the `elite-copywriter` agent with comprehensive context.

Your prompt to the agent should include:
- The TYPE of copy needed
- TARGET AUDIENCE (who they are, what they care about)
- GOAL/CTA (what action to drive)
- TONE (how it should feel)
- KEY DIFFERENTIATOR (what makes this special)
- PAIN POINTS (what problem is being solved)
- Any CONSTRAINTS (length, format, must-include messages)
- **MARKET RESEARCH INSIGHTS** (if research was conducted in Step 4)

**Example Task prompt (with research):**

```
Write [TYPE OF COPY] for [PRODUCT/SERVICE].

## User-Provided Context:
- Target audience: [WHO — be specific about their role, pain points, desires]
- Goal: Get readers to [SPECIFIC ACTION]
- Tone: [TONE — with any brand voice notes]
- Key differentiator: [WHAT MAKES THIS DIFFERENT]
- Main pain point solved: [THE PROBLEM]
- Constraints: [LENGTH, FORMAT, MUST-INCLUDES]

## Market Research Insights:

**Competitive Landscape:**
[Key findings about how competitors message — what angles they use, gaps in their messaging]

**Audience Language:**
[Specific words, phrases, and terminology the target audience uses — incorporate these naturally]

**Effective Patterns:**
[Copy structures, hooks, and frameworks that work well for this type of copy in this space]

**Positioning Opportunity:**
[How to differentiate given the competitive landscape]

**Objections to Address:**
[Common objections and how to handle them in the copy]

## Writing Instructions:

Use the market research to write copy that:
- Uses language the audience actually uses (from research)
- Differentiates from competitor messaging (based on gaps identified)
- Addresses known objections naturally
- Follows patterns that work in this space

Write for accessibility — avoid unexplained jargon and acronyms. If industry terms are necessary, explain them on first use.

Write in a natural, human voice. Avoid these AI-writing patterns:
- Overused AI words like "delve", "crucial", "comprehensive", "leverage", "foster", "harness", "navigate", "landscape", "realm", "beacon", "pivotal", "multifaceted"
- Excessive hedging ("It's important to note", "It's worth mentioning", "It should be noted")
- Overly perfect parallel structure in every sentence
- Generic, could-apply-to-anyone statements
- Flat, personality-free prose without voice
- Too many adjectives clustered together ("truly remarkable and exceptionally innovative")

Write like a skilled human copywriter would — with personality, specific details, natural rhythm, and occasional imperfection.

Deliver polished, ready-to-use copy with multiple options for headlines where appropriate.
```

**Important:** The combination of user context + market research + AI detection knowledge produces copy that's accurate, market-informed, AND human-sounding from the start.

### Step 7: Save to File

**Before saving, check existing directories:**
```bash
ls copy/
```

Use an existing matching directory. Only create new if needed.

**Write the final copy to a markdown file** in the appropriate subdirectory.

**File structure:**

```markdown
# [Copy Type]: [Product/Purpose]

> Generated: [date]
> Audience: [target audience]
> Goal: [desired action]
> Tone: [tone]
> Research: Yes / No

---

## Context

[Brief summary of the product/service and key differentiator]

---

## Copy

[The final copy, organized by section]

### Headline Options
[Multiple headline variations]

### Subheadline
[Supporting headline]

### Body Copy
[Main content sections]

### Call to Action
[CTA options]

---

## Variations & Notes

[Any alternative angles, notes for iteration, or suggestions for A/B testing]

## Research Insights Used

[If research was conducted, brief summary of key insights that informed the copy]
```

### Step 8: Get User Approval (AskUserQuestion)

After saving the file, **use the AskUserQuestion tool** to get the user's feedback:

```
Question: "How does this copy look?"
Options:
- Looks good — I'm happy with it
- Needs some tweaks — I'll share specific feedback
- Want a completely different angle
- Other
```

**If the user has feedback:**
1. Use the `claude-vibes:ai-writing-detection` skill + sequential thinking to plan revisions
2. Launch `elite-copywriter` again with their specific feedback and AI-aware instructions
3. Update the saved file with the new version
4. Ask for approval again

**Continue until the user approves.**

### Step 9: Final Delivery

Once the user approves:
- Confirm the final file location
- Summarize what was created
- Note any variations or options included
- Mention if research informed the copy

"Your copy is finalized and saved to `copy/landing-pages/[name].md`.

The final version:
- Was informed by market research on [competitor messaging / audience language / etc.]
- Written with AI detection knowledge to sound authentically human
- Includes 3 headline options, full body copy, and 2 CTA variations

Ready to use!"

## Guidelines

- **Research before writing** — Market context produces better copy; use deep-researcher for substantial copy
- **Skill before writing** — Always use the `claude-vibes:ai-writing-detection` skill and sequential thinking BEFORE launching elite-copywriter
- **Human from the start** — Apply AI detection knowledge proactively; elite-copywriter writes human-sounding copy on the first pass
- **Context is everything** — User context + market research + AI detection knowledge = copy that converts
- **Use Sequential Thinking (ultrathink)** to assess research needs, plan clarifying questions, and prepare AI-aware instructions
- **Adapt to the ask** — A quick headline needs less research than a full sales page
- **Show don't tell** — When asking about differentiators, push for specifics not generalities
- **User approval is the final gate** — Keep iterating until they're happy
- **Check existing directories** — Never create duplicate folders; use what exists
- **Always save before asking approval** — User should be able to see the file

## Copy Request

User's copywriting request: $ARGUMENTS

If no request provided, use AskUserQuestion to ask what copy they need.
