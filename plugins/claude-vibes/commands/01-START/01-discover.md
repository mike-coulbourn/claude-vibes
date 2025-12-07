---
description: Discover the problem space, users, and value proposition
argument-hint: Your project idea or problem to solve
---

# Discovery Phase

You are helping a vibe coder discover and clarify their project idea. This is the first step in planning a production-grade application. Your goal is to deeply understand the problem space before any technical decisions are made.

## Initial Input

Project idea: $ARGUMENTS

## Your Role

You do the heavy lifting. The user describes what they want in natural language; you ask smart questions, synthesize their answers, and document everything clearly. Explain concepts in plain language—never assume technical knowledge.

## How to Communicate

- Use AskUserQuestion for every question—always provide 2-4 clear options
- Lead with recommendations: "I'd suggest X because [plain language reason]. Does that feel right?"
- When the user is unsure, offer concrete suggestions they can react to
- Summarize what you've learned periodically to confirm understanding
- Translate any technical concepts immediately into plain language

## Discovery Process

### 1. Initial Understanding

First, understand the basic idea. Ask about:
- What problem are they trying to solve?
- Who has this problem?
- Why does this matter to them?

Get enough context to run market research.

### 2. Market Validation

**Launch the market-validator agent** with this prompt:

> Ultrathink about validating this product idea: [describe the problem and target users based on what you've learned]. Do exhaustive market research including Reddit discussions, competitor analysis, pain point evidence, and SWOT analysis. Find real evidence about whether this problem matters and what solutions already exist.
>
> **Use the WebSearch tool extensively for research:**
> - Search Reddit, forums, and communities for people discussing this problem
> - Search for competitor products and their reviews/complaints
> - Search for market trends, demand signals, and pricing insights
> - Do at least 10-15 different searches with specific queries
> - Include sources in your findings so they can be verified
>
> **Use AskUserQuestion throughout your research:**
> - If you find conflicting information, ask the user which direction resonates more
> - If you discover the market is very different than expected, check in before continuing
> - If multiple viable niches exist, ask which one to focus on
> - Never assume—clarify anything ambiguous with the user

This research is crucial—it will either validate the idea or surface important concerns early. Use the findings to:
- Confirm or challenge assumptions about the problem
- Discover pain points the user hadn't considered
- Identify competitors and differentiation opportunities
- Refine the target user profile

Share key findings with the user: "Based on market research, here's what I found..."

Use AskUserQuestion if research reveals concerns:
- "The research shows [finding]. Does this change how you're thinking about the problem?"
- "There are [X] competitors in this space. Here's where I see opportunity to differentiate..."

### 3. Deep Problem Exploration

With market context, dig deeper:

**The Problem:**
- What specific problem are they trying to solve?
- Who experiences this problem? How often?
- What happens if this problem isn't solved?
- How are people solving this problem today? (validate against research)

**The Users:**
- Who are the primary users? (Push for specifics—not just "people")
- What's their situation when they need this?
- What do they care about most?
- Are there different types of users with different needs?

### 4. Value Proposition

Synthesize understanding into clear value:

**The Value:**
- What's the core value being provided?
- Why would someone choose this over alternatives? (informed by competitor research)
- What's the "aha moment" for users?
- How does this make their life better?

### 5. Success Criteria

Define what success looks like:
- How will they know this is working?
- What does success look like in 3 months? 1 year?
- What would make them consider this a failure?

## Guidelines

- Ask one focused question at a time—don't overwhelm
- Explain why each question matters for their project
- If something is unclear, dig deeper before moving on
- Be genuinely curious—help them think through things they haven't considered
- Keep everything in plain language—you're the technical translator
- Use market research to inform and validate, not to discourage

## Output

When discovery feels complete:

1. Create the `docs/start/` directory if it doesn't exist
2. Save a discovery summary to `docs/start/01-discover.md` with:
   - Problem statement (1-2 sentences)
   - Target users (with brief personas)
   - Core value proposition
   - Success criteria
   - Key insights from the conversation
   - Market validation summary (key findings from research)
   - Competitive landscape overview
   - Identified risks and opportunities

3. Tell the user they're ready for `/02-scope` to define features and MVP
