# Contributing to claude-vibes

Thanks for helping. This plugin is all Markdown prompts, so nothing fails loudly when a reference breaks. The checks below are how we catch that.

## Before you open a PR

```bash
pip install pyyaml
python3 scripts/validate_plugin.py
claude plugin validate ./plugins/vibes
```

The first command checks frontmatter, agent and skill references, skills that agents preload, relative links, MCP version pinning, and the counts claimed in `marketplace.json`. CI runs it on every PR. The second is Claude Code's own manifest check.

## Conventions

**Agents** live in `plugins/vibes/agents/<FOLDER>/<name>.md`. The folder is part of the agent's identifier, so commands must launch them as `claude-vibes:<FOLDER>:<name>`, for example `claude-vibes:CODING:code-architect`. Start the description with "Use when". Use `model: fable` for agents that plan, review, diagnose, or do strategy, and `model: opus` for agents that implement.

Agents that write prose for the user preload the writing skill with `skills: natural-writing` in frontmatter, so commands do not need to paste writing rules into agent prompts. Coding agents that should learn across sessions set `memory: project`. Ask for step-by-step reasoning in plain words (the `ultrathink` keyword is fine) instead of bundling a reasoning or memory MCP server.

**Skills** live in `plugins/vibes/skills/<name>/SKILL.md`, and `name` must match the directory.

- The description says when to use the skill, not what its workflow is, and stays under 1024 characters. If it contains a colon followed by a space, wrap the whole value in single quotes so it stays valid YAML.
- Keep `SKILL.md` under 500 lines. Move templates and long reference material into `reference/`, link them from `SKILL.md` with a note on when to load them, and give any file over 300 lines a table of contents.
- Teach what Claude does not already know: decision rules, templates, and hard-won specifics. Skip textbook summaries.
- Mark facts that go stale (platform numbers, tool versions) with a last-verified date.

**Commands** live in `plugins/vibes/commands/`. Ask the user questions with the AskUserQuestion tool rather than plain text. When you add, remove, or rename a command or agent, update its row in `README.md` and the counts in `.claude-plugin/marketplace.json`.

**Writing style.** These files are prompts, and their style carries into what the plugin writes for users. Use plain words and sentence-case headings. Keep em dashes out of running text (they are fine inside a real person's quotation). State an instruction once, without capitals such as CRITICAL or ALWAYS, and give the reason when it is not obvious. Leave sample copy, "words to avoid" lists, and deliberately bad examples as they are.

**MCP servers** in `plugin.json` start for every user on every session. Pin every `npx` package to an exact version (CI enforces this), and only add a server that a command actually calls. Prefer a file in the user's project or a native Claude Code feature over a new server.

## Versioning

Bump `version` in `plugins/vibes/.claude-plugin/plugin.json` with every change under `plugins/vibes/`: patch for fixes and edits, minor for new commands, agents, or skills, major for removals or renames. Add a line to `CHANGELOG.md`. Changes that touch only repo files such as the README, CI, or templates need no version bump.

After a PR that bumps the version merges, the maintainer tags it (`v2.0.4`) and publishes a GitHub release with the changelog entry.

## Commits

Use conventional commits with a scope, for example `fix(commands): ...` or `feat(TOOLKIT): ...`.
