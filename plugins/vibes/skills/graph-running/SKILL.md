---
name: graph-running
description: Use when the user has approved a work graph designed with the graph-engineering skill and wants it carried out, or when a command says to run an approved graph. Covers saving the graph as a file trail, running lanes at the execution level the graph recommends (by hand, one job at a time, or as parallel subagents), keeping the skeptic separate from the worker, stopping at human approval gates, and recording results. Not for designing a graph, and not for work that has no approved graph yet.
---

# Graph running

Run an approved graph the way it was drawn. The graph-engineering skill designs the work and stops at approval. This skill picks up from there.

## Start only from an approved graph

You need three things from graph-engineering before you begin: the confirmed alignment contract, the graph with each job's owner and output, and the user's approval of that graph. If any is missing, go back to `claude-vibes:graph-engineering`. Do not improvise a graph here, because a graph nobody approved has no authority to guide the work.

Approval of the graph is not approval of every step in it. Each human gate in the graph still needs its own yes at the moment the work reaches it.

## Save the graph before running it

If the approved graph recommends manual lanes, a shared note the user keeps is enough. Otherwise write the graph to a file first, so the work survives a closed session and anyone can see what was decided and why.

- A whole-project graph lives in `docs/01-START/roadmap.md`, which the `04-plan-roadmap` command writes and the `05-track-progress` command maintains. Use that file's format and do not create a second one.
- Any other graph goes in `docs/graphs/<short-name>.md`, with these sections: the alignment contract, the diagram, a checklist with one line per job (owner, what it depends on, its output, any gate), a "State" section that collects each job's result, and a dated change log.

Run `date +%Y-%m-%d` before writing a date.

## Run the jobs

1. **Follow the arrows.** A job starts only when every job it depends on has finished and its output is in the State section.
2. **Run independent lanes the way the graph says.** Use the execution level the approved graph recommends. At manual lanes, walk the user through one job at a time and carry the state yourself. At file trails, run each job in turn and record what it produced. At an orchestrated graph, launch independent lanes as separate subagents in a single message with the Agent tool. If the graph names no level, start with file trails and ask before automating further. Lanes that share no arrow must not wait on each other, and they must not see each other's drafts, or they stop being independent.

   A subagent cannot ask the user questions. Gather whatever a lane needs from the user yourself, with AskUserQuestion, before you launch it.
3. **Give every job the contract.** Each subagent's prompt includes the alignment contract, the job's own responsibility and expected output, and the specific State entries it depends on. Tell it plainly that it may not redefine the objective or reorder the user's priorities.
4. **Record each result.** When a job finishes, write its output, or a pointer to the file it produced, into the State section and tick the job. Later jobs read from State, not from your memory of the conversation.
5. **Use the owners the graph names.** When the graph assigns a job to a command or agent from this plugin, use that one. When it says the user does the job by hand, walk them through it and wait.

## Keep the skeptic separate

The worker must not grade its own work, and neither should you grade work you directed. Run the skeptic as a different subagent with fresh context, give it the contract and the outputs under review, and have it ask the questions listed under "Engineer the checking loop" in the graph-engineering skill.

- A researchable gap goes back to the job that can fix it, and then through the skeptic again.
- A gap that needs new access or authority goes to a human gate.
- Only supported facts, properly compared choices, and the user's own stated preferences reach the merger, plus strategic hypotheses that are labeled as such, tied to the objective, backed by directional evidence or sound reasoning, assessed for downside, and paired with a way to test them. A label alone does not qualify a claim.

The loop ends when every material decision has the support its class needs, or when the user chooses to stop, narrow, or accept a tradeoff. Do not add a retry budget of your own.

## Stop at every human gate

Use AskUserQuestion at each gate, and give the user a compact decision packet: the objective, the recommendation, the strongest fallback, the tradeoffs, the confidence, what evidence would change the answer, and the exact decision or permission needed.

Never cross these on your own, whatever the graph says: creating accounts, entering credentials or payment details, spending money, accepting terms, contacting people outside the conversation, publishing, deploying, and changing or deleting production data. Prepare the step and explain it. For publishing, deploying, spending, contacting people, or production data, wait for the user's explicit yes. For credentials, payment details, and account creation, hand the step to the user to do themselves.

Do not interrupt the user for low-risk, reversible choices inside authority they already gave. Choose the option that best fits the contract and record why in State.

## If the work drifts from the graph

Evidence sometimes shows the graph was wrong. Narrowing how strong a claim is, or how deep a decision goes, is within your authority. Changing the objective, the promised outcome, or what the result optimizes for is not. When that is needed, stop, tell the user what you found, and return to graph-engineering for a revised graph and a fresh approval. Note the change in the file's change log.

## Finish

When the merger's job is done, present the terminal deliverable the contract promised, the confidence in each material decision, anything left unresolved and why, and the smallest next test for any open hypothesis. Update the file so it shows the final state.
