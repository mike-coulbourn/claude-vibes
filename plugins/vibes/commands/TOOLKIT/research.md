---
description: Deep research on any topic using expert knowledge extraction
argument-hint: Topic or question to research
---

# Deep Research

You are helping a user conduct deep research on a topic. Your goal is to gather comprehensive expert knowledge that enables informed decision-making.

## Your Role

You orchestrate the research process:
1. Understand what the user really needs
2. Clarify context to ensure the research is targeted
3. Launch the deep-researcher agent with rich context
4. Save the research to a file for reference
5. Deliver actionable findings

## Output Location

All research reports should be saved to: `research/[topic-area]/`

**Before creating any directory:**
1. Check if `research/` exists — if not, create it
2. List existing subdirectories in `research/`
3. Use an existing subdirectory if one matches the topic area
4. Only create a new subdirectory if no appropriate one exists

**Subdirectory examples** (create as needed, check first):
- `branding/` — brand identity, positioning, strategy
- `marketing/` — marketing strategies, channels, tactics
- `tech/` — technologies, frameworks, architectures
- `business/` — business models, pricing, operations
- `design/` — design principles, UX, visual design
- `industry/` — industry-specific research

**File naming convention:**
- `[descriptive-topic].md`
- Use kebab-case
- Be specific: `brand-positioning-strategies.md` not `research-1.md`

## Process

### Step 1: Analyze the Request (Sequential Thinking)

**Use the `sequentialthinking` MCP tool** to analyze the user's research request:

- What topic/question are they researching?
- What context is missing that would affect research quality?
- What's likely the PURPOSE behind this research?
- What clarifying questions would most improve the output?

Think through: "What do I need to know to make this research maximally useful?"

### Step 2: Gather Critical Context (AskUserQuestion)

**Use the AskUserQuestion tool** to clarify the most important unknowns.

**Essential questions to consider:**

**Purpose** — Why do they need this research?
- Learning/understanding a new topic
- Making a specific decision
- Implementing something (need actionable guidance)
- Validating an existing approach

**Depth** — How comprehensive should it be?
- Quick overview (key concepts, major experts)
- Moderate depth (methodologies, best practices)
- Exhaustive (everything top experts know and do)

**Application** — What will they DO with this research?
- Understanding this helps the agent tailor the output format and focus

**Specific angles** — Any particular aspects to focus on?
- Certain methodologies, specific experts, particular use cases

**Smart clarification principles:**
- Don't overwhelm with questions — ask the 2-3 most critical ones
- If the request is clear and specific, fewer questions needed
- If vague or broad, more clarification helps
- Always explain WHY you're asking (helps user give better answers)

**Example AskUserQuestion usage:**

"To make sure I research the right things, I have a couple questions:"

```
Question 1: "What will you use this research for?"
- Learning about the topic
- Making a decision (tell me which one)
- Building/implementing something
- Other

Question 2: "How deep should I go?"
- Quick overview — key concepts and top experts
- Moderate — methodologies and best practices included
- Exhaustive — comprehensive expert knowledge extraction
```

### Step 3: Launch the Deep Researcher Agent

**Use the Task tool** to launch the `deep-researcher` agent with an enriched prompt.

Your prompt to the agent should include:
- The original research topic/question
- The PURPOSE (from clarification)
- The desired DEPTH
- How the research will be USED
- Any SPECIFIC ANGLES or focus areas
- Any CONSTRAINTS (time-sensitivity, specific sources to include/exclude)

**Example Task prompt:**

```
Research [TOPIC].

Context:
- Purpose: The user is [implementing/deciding/learning] [specific context]
- Depth needed: [Exhaustive/Moderate/Overview]
- Application: This research will be used to [specific use]
- Focus areas: [Any specific aspects to emphasize]

Deliver comprehensive findings following your standard research report format. Focus especially on [key areas based on user's purpose].
```

**Important:** The more context you provide in the prompt, the better the research output will be. Don't launch with just the topic — include everything you learned from clarification.

### Step 4: Save to File

**Before saving, check existing directories:**
```bash
ls research/
```

Use an existing matching directory. Only create new if needed.

**Write the research report to a markdown file** in the appropriate subdirectory.

The file should contain the full research report as returned by the agent, with a header:

```markdown
# Research: [Topic]

> Generated: [date]
> Purpose: [why this research was conducted]
> Depth: [overview/moderate/exhaustive]

---

[Full research report from the agent]
```

### Step 5: Deliver Results

Once the research is saved:
- Tell the user where the file was saved
- Highlight the most actionable insights based on their stated purpose
- Offer to dig deeper on any section if needed

"Saved research to `research/[area]/[topic].md`.

Based on your goal of [purpose], I'd highlight [key findings]. Want me to go deeper on any area?"

## Guidelines

- **Front-load context gathering** — Better to ask questions upfront than get unfocused research
- **Use Sequential Thinking** to plan your clarifying questions strategically
- **Tailor questions to the topic** — Technical topics may need different clarification than creative topics
- **Respect user's time** — If they give short answers, don't over-ask; make reasonable assumptions
- **Always launch the agent** — Don't try to do the research yourself; use the deep-researcher agent
- **Check existing directories** — Never create duplicate folders; use what exists
- **Always save to file** — Research should persist in the appropriate `research/` subdirectory

## Research Topic

User's research request: $ARGUMENTS

If no topic provided, use AskUserQuestion to ask what they'd like to research.
