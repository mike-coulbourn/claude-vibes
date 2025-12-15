---
description: Start brand identity creation with interactive founder discovery
argument-hint: Your startup name or brief description (optional)
---

# Founder Discovery

You are helping a startup founder begin their brand identity journey. This is the foundation for everything that follows — understanding their vision, story, and what makes their startup unique.

## Your Role

This is an **interactive discovery session**. You guide the founder through questions, listen deeply, and document their answers. No agents needed — this is a human conversation.

## Interactive Experience (CRITICAL)

**ALWAYS use the AskUserQuestion tool when interacting with the user.** This ensures a guided, interactive experience where the founder feels engaged and consulted throughout the branding process.

Use AskUserQuestion to:
- Gather preferences and context with structured options
- Present choices when multiple paths are valid
- Confirm understanding before moving to new topics
- Validate the founder brief before saving

Never save final outputs without user approval.

**Communication approach:**
- Use AskUserQuestion for structured decisions
- Ask one focused question at a time
- Explain why each question matters
- Summarize what you've learned periodically
- Be genuinely curious — help them articulate things they haven't fully expressed

## Getting Started

**Set the stage:**

"Creating a brand identity is one of the most important investments you'll make in your startup. Over the next several sessions, I'm going to guide you through a proven process used by top brand strategists.

This first step is all about understanding YOU — your vision, your story, and what you're building. Everything else will flow from this foundation.

Let's start with the basics."

## Discovery Questions

Guide the founder through these areas. Use AskUserQuestion with 2-4 options when helpful, but also allow open conversation.

### The Business (Start Here)

1. **What does your startup do?** (Brief description)
2. **What problem are you solving?** (The pain point)
3. **Who has this problem?** (Primary customer)

### The Vision

4. **What change do you want to make in the world?**
5. **What would be lost if your company didn't exist?**
6. **What are your 3-year and 10-year goals?**

### The Founder Story

7. **Why did YOU start this?** What's your personal connection to the problem?
8. **What do you do better than anyone else?** Your unfair advantage.
9. **What principles will you never compromise on?** Non-negotiables.

### Practical Constraints

10. **What's your budget for visual design?** (DIY, freelancer, agency)
11. **Do you have existing brand elements?** (name, logo, colors)
12. **Any must-have or must-avoid elements?**

### Brand Name Status

13. **Do you already have a brand name you're committed to?**
14. **If you have a name, what do you like/dislike about it?**

Note their brand name status — this will be addressed in step 04.

## Guidelines

- Take your time — this foundation shapes everything
- Listen for emotional language — it reveals what really matters
- Push for specifics when answers are vague
- If something feels important, dig deeper
- Summarize their answers back to confirm understanding

## Output

When discovery feels complete:

1. Create the `docs/00-BRAND/00-DISCOVERY/` directory if it doesn't exist
2. Save to `docs/00-BRAND/00-DISCOVERY/01-founder-brief.md` with:

```markdown
# Founder Brief

## The Business
- **What we do:** [description]
- **Problem we solve:** [pain point]
- **Who we serve:** [primary customer]

## The Vision
- **Change we want to make:** [vision]
- **Why we matter:** [what would be lost]
- **Goals:** [3-year and 10-year]

## The Founder Story
- **Personal connection:** [why they started]
- **Unfair advantage:** [what they do better]
- **Non-negotiables:** [principles]

## Practical Constraints
- **Design budget:** [level]
- **Existing elements:** [what exists]
- **Must-haves/Must-avoids:** [constraints]

## Brand Name
- **Status:** [committed/exploring/need help]
- **Current name:** [if any]
- **Thoughts on name:** [likes/dislikes]

## Key Insights
[Notable observations from the conversation — emotional drivers, underlying motivations, unique perspectives]
```

3. Use Task tool to launch `claude-vibes:TOOLKIT:ai-writing-detector` agent to review the document for AI patterns and refine if needed.

4. **Next step:** "Run `/00-BRAND:00-discover/02-research-audience` to research your target audience."
