---
name: interview-me
description: Conduct exhaustive, structured interviews with the user about any topic, business, product, plan, decision, design, process, strategy, personal context, or knowledge area. Use when the user wants to be interviewed, questioned, interrogated, grilled broadly, walked through a topic, or have their thinking/context extracted into a shared understanding. Always use the AskUserQuestion tool for each interview question.
---

# Interview Me

## Core Behavior

Interview the user relentlessly, one question at a time, until the topic is understood well enough to summarize, document, decide, plan, or create the requested follow-on artifact.

Use `AskUserQuestion` for every interview question. Do not ask interview questions as plain chat when `AskUserQuestion` is available.

If `AskUserQuestion` is unavailable, stop and say the skill requires that tool for the interview experience. Do not continue the interview with plain-text questions unless the user explicitly asks to proceed without the tool.

## Question Format

For each interview step:

- Ask exactly one question through `AskUserQuestion`.
- Use a short header, 12 characters or fewer.
- Provide 2-3 mutually exclusive answer options.
- Put the recommended option first and suffix its label with `(Recommended)`.
- Make the recommended option a real proposed answer, not a vague placeholder.
- Let the tool's free-form `Other` path handle nuance when the options do not fit.
- Keep the visible question concise, but include enough context for the user to answer quickly.

## Interview Method

Before asking, decide whether the answer can be discovered from available artifacts, repos, docs, previous messages, diagnostics, or uploaded files. If it can, inspect the source instead of asking the user.

Walk the decision tree branch by branch:

1. Establish the root definition of the topic.
2. Identify the purpose of the interview and the desired end artifact or decision.
3. Capture the audience, stakeholders, users, or affected parties.
4. Surface the user's goals, constraints, preferences, and non-negotiables.
5. Map the current state, history, and why prior choices were made.
6. Identify edge cases, exceptions, risks, objections, and failure modes.
7. Resolve dependencies between answers before moving to downstream branches.
8. Test the emerging model by proposing concise summaries and asking the user to correct them.
9. Continue until new questions are producing little new information or the user stops the interview.

For each question, include a recommended answer via the first option. The recommendation should reflect the best current understanding, not a generic default.

## Topic Coverage

Adapt the interview tree to the topic:

- Business: positioning, customers, offer, pricing, distribution, operations, risks, proof, roadmap.
- Product: users, jobs-to-be-done, workflows, feature boundaries, success metrics, edge cases.
- Design: audience, desired feeling, hierarchy, visual constraints, interaction states, references.
- Engineering: system purpose, architecture, invariants, data flow, failure modes, deployment, tests.
- Strategy: objective, options, tradeoffs, constraints, timing, dependencies, decision criteria.
- Personal knowledge capture: vocabulary, values, history, preferences, recurring decisions, examples.
- Process documentation: triggers, inputs, handoffs, tools, checklists, exceptions, escalation paths.

## Exhaustiveness Standard

Do not stop at the first plausible answer. Keep interviewing until these are clear:

- What the topic is and is not.
- Why it matters.
- Who it matters to.
- What success looks like.
- What constraints shape the answer.
- What exceptions or edge cases change the default.
- What language, labels, or framing the user prefers.
- What should be preserved, avoided, or escalated in future work.

When the user says the understanding is complete, provide a compact synthesis with:

- The root definition.
- Key principles.
- Important branches and decisions.
- Open questions, if any.
- Recommended next action.
