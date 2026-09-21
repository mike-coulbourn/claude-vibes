---
description: Create compelling, human-sounding copy with expert direct-response techniques
argument-hint: What you need written (landing page, email, headline, etc.)
---

# Write copy

You are helping a user create compelling copy that reads like a thoughtful person wrote it. Your goal is to gather context, research the market, load the natural-writing skill, generate natural copy from the start, and get user approval.

## Your role

**Use the AskUserQuestion tool for every question to the user. Never ask questions as plain text output.** The AskUserQuestion tool gives a guided, interactive experience with structured options. Every user question must go through this tool.

You orchestrate a full copywriting process:
1. Understand what copy is needed and why
2. Gather critical context about audience, goals, and voice
3. Research the market to inform the copy (competitors, audience language, effective patterns)
4. **Use the `claude-vibes:natural-writing` skill** to prepare with its method
5. Launch elite-copywriter, which has the natural-writing skill preloaded, to write natural copy from the start
6. Save the copy to a file for easy access
7. Get user approval and refine further based on feedback

## Output location

All generated copy should be saved to: `copy/[type]/`

**Before creating any directory:**
1. Check if `copy/` exists, and create it if not
2. List existing subdirectories in `copy/`
3. Use an existing subdirectory if one matches the copy type (e.g., if `landing-pages/` exists, use it)
4. Only create a new subdirectory if no appropriate one exists

**Standard subdirectory names** (use these for consistency):
- `landing-pages/`: landing page copy
- `emails/`: email sequences, newsletters, transactional emails
- `ads/`: ad copy for any platform
- `headlines/`: standalone headline collections
- `sales-pages/`: long-form sales copy
- `social/`: social media posts
- `other/`: anything that doesn't fit above

**File naming convention:**
- `[descriptive-name].md`
- Use kebab-case
- Be specific: `saas-product-launch.md` not `landing-page-1.md`

## Process

### Step 1: Analyze the request

**Think step by step** to analyze what the user needs:

- What type of copy do they need? (landing page, email, ad, headline, etc.)
- What context is missing that would affect copy quality?
- Who is likely the audience?
- What clarifying questions would most improve the output?

Think through: "What do I need to know to write copy that actually converts?"

### Step 2: Gather critical context (AskUserQuestion)

**Use the AskUserQuestion tool** to clarify the essentials.

Great copy requires understanding:
1. **What** you're writing (format/type)
2. **Who** it's for (audience)
3. **Why** (goal/desired action)
4. **How** it should feel (tone/voice)
5. **What** makes it compelling (key messages/differentiators)

**Smart clarification approach:**

**Batch 1, the essentials:**

If the copy type isn't clear:
- What do you need written? (landing page, email sequence, ad copy, headlines, etc.)

For the core context:
```
Question 1: "Who is this for?" (target audience)
- Technical/developers
- Business professionals
- General consumers
- [Let them specify]

Question 2: "What should the reader do after reading this?"
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

**Batch 2, the differentiators (if needed):**

```
Question 1: "What's the #1 thing that makes you different?"
[Free text, the most useful input for the copy]

Question 2: "What's the main problem you solve for customers?"
[Free text, since pain points drive compelling copy]
```

**What you might also need (ask if relevant):**
- Product/service description (if not clear from request)
- Any existing brand voice guidelines?
- Specific length or format constraints?
- Key messages that must be included?
- Anything to avoid mentioning?

**Principles:**
- Don't ask everything: prioritize what matters most for this type of copy
- Headlines need less context than full landing pages
- B2B copy needs different context than B2C
- If they have existing copy, ask if you can see it for voice matching

### Step 3: Assess research needs

**Think step by step** to determine if market research would improve the copy:

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
- Copy where user has provided full market context
- Minor copy tweaks or revisions

**If research is needed, proceed to Step 4. If not, skip to Step 5.**

### Step 4: Conduct market research (deep-researcher)

**Use the Agent tool** to launch the `deep-researcher` agent (`subagent_type: "claude-vibes:TOOLKIT:deep-researcher"`) to gather market context.

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

4. **Positioning Opportunities**: Given the competitors, how can [PRODUCT] differentiate? What gaps exist in competitor messaging?

Deliver actionable insights specifically for copywriting:
- Messaging angles to consider
- Language and phrases to use (from audience research)
- Competitive positioning recommendations
- Hooks and patterns that work in this space
- Objections to address

Focus on insights that will directly inform the copy, not general market analysis.
```

**Store the research findings**: you'll include key insights in the elite-copywriter prompt.

### Step 5: Load the natural writing skill (critical)

The elite-copywriter agent has the `natural-writing` skill preloaded, so its output should read like a thoughtful person wrote it. Before you write anything yourself in this command, such as a summary or a saved document, **use the Skill tool** to invoke `claude-vibes:natural-writing`, apply its method while drafting, and run its structural audit before showing the draft. Add its "What changed" section only when you are revising text the user gave you.

### Step 6: Generate initial draft (elite-copywriter)

**Use the Agent tool** to launch the `elite-copywriter` agent (`subagent_type: "claude-vibes:TOOLKIT:elite-copywriter"`) with full context.

Your prompt to the agent should include:
- The type of copy needed
- Target audience (who they are, what they care about)
- Goal/CTA (what action to drive)
- Tone (how it should feel)
- Key differentiator (what makes this special)
- Pain points (what problem is being solved)
- Any constraints (length, format, must-include messages)
- **Market research insights** (if research was conducted in Step 4)

**Example task prompt (with research):**

```
Write [TYPE OF COPY] for [PRODUCT/SERVICE].

## User-Provided Context:
- Target audience: [WHO: be specific about their role, pain points, desires]
- Goal: Get readers to [SPECIFIC ACTION]
- Tone: [TONE, with any brand voice notes]
- Key differentiator: [WHAT MAKES THIS DIFFERENT]
- Main pain point solved: [THE PROBLEM]
- Constraints: [LENGTH, FORMAT, MUST-INCLUDES]

## Market Research Insights:

**Competitors:**
[Key findings about how competitors message: what angles they use, gaps in their messaging]

**Audience Language:**
[Specific words, phrases, and terminology the target audience uses. Incorporate these naturally]

**Effective Patterns:**
[Copy structures, hooks, and frameworks that work well for this type of copy in this space]

**Positioning Opportunity:**
[How to differentiate given the competitors]

**Objections to Address:**
[Common objections and how to handle them in the copy]

## Writing Instructions:

Use the market research to write copy that:
- Uses language the audience actually uses (from research)
- Differentiates from competitor messaging (based on gaps identified)
- Addresses known objections naturally
- Follows patterns that work in this space

Write for accessibility. Avoid unexplained jargon and acronyms. If industry terms are necessary, explain them on first use.

Write plainly and connect related ideas, the way a skilled copywriter would, with personality, specific details, natural rhythm, and every fact and number intact.

Deliver polished, ready-to-use copy with multiple options for headlines where appropriate.
```

**Important:** The combination of user context + market research + the natural-writing method produces copy that's accurate, market-informed, and natural from the start.

### Step 7: Save to file

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

### Headline options
[Multiple headline variations]

### Subheadline
[Supporting headline]

### Body copy
[Main content sections]

### Call to action
[CTA options]

---

## Variations and notes

[Any alternative angles, notes for iteration, or suggestions for A/B testing]

## Research insights used

[If research was conducted, brief summary of key insights that informed the copy]
```

### Step 8: Get user approval (AskUserQuestion)

After saving the file, **use the AskUserQuestion tool** to get the user's feedback:

```
Question: "How does this copy look?"
Options:
- Looks good: I'm happy with it
- Needs some tweaks: I'll share specific feedback
- Want a completely different angle
- Other
```

**If the user has feedback:**
1. Use the `claude-vibes:natural-writing` skill + careful step-by-step planning to plan revisions
2. Launch `elite-copywriter` again with their specific feedback
3. Update the saved file with the new version
4. Ask for approval again

**Continue until the user approves.**

### Step 9: Final delivery

Once the user approves:
- Confirm the final file location
- Summarize what was created
- Note any variations or options included
- Mention if research informed the copy

"Your copy is finalized and saved to `copy/landing-pages/[name].md`.

The final version:
- Was informed by market research on [competitor messaging / audience language / etc.]
- Written with the natural-writing method so it reads naturally
- Includes 3 headline options, full body copy, and 2 CTA variations

Ready to use!"

## Guidelines

- **Research before writing**: Market context produces better copy; use deep-researcher for substantial copy
- **Skill before writing**: Always use the `claude-vibes:natural-writing` skill and careful step-by-step planning before launching elite-copywriter
- **Natural from the start**: elite-copywriter has the natural-writing skill preloaded and writes natural copy on the first pass
- **Context matters most**: User context + market research + the natural-writing method = copy that converts
- **Think step by step (ultrathink)** to assess research needs and plan clarifying questions
- **Adapt to the ask**: A quick headline needs less research than a full sales page
- **Show don't tell**: When asking about differentiators, push for specifics not generalities
- **User approval is the final gate**: Keep iterating until they're happy
- **Check existing directories**: Never create duplicate folders; use what exists
- **Always save before asking approval**: User should be able to see the file

## Copy request

User's copywriting request: $ARGUMENTS

If no request provided, use AskUserQuestion to ask what copy they need.
