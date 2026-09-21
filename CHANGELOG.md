# Changelog

Notable changes to the claude-vibes plugin. Versions follow the `version` field in `plugins/vibes/.claude-plugin/plugin.json`.

## 2.0.1

- `midjourney-prompting`: `--cref` is V6 only. V7 uses Omni Reference (`--oref`, `--ow` 1 to 1000), and V8.1/V8.2, the default since July 2026, use the Edit Model with up to four attached images. Thanks to @sbley for the report (#5).

## 2.0.0

A slimmer plugin that leans on what Claude Code now does natively and focuses on what it does not.

**Removed (breaking)**

- The five builder skills (`skill-builder`, `agent-builder`, `slash-command-builder`, `hooks-builder`, `marketplace-builder`) and `docs/claude-code-extensibility-guide.md`. Anthropic maintains better versions alongside the product: install `plugin-dev` and `skill-creator` from `anthropics/claude-plugins-official`.
- The bundled `sequential-thinking` MCP server. Commands and agents now ask Claude to reason step by step natively, and keep the `ultrathink` keyword.
- The bundled `memory` MCP server. Coding agents use Claude Code's native agent memory (`memory: project`, stored in `.claude/agent-memory/`). Knowledge saved in the old memory server's graph is not migrated.
- The `ai-writing-detection` skill and the `ai-writing-detector` agent, replaced by `natural-writing`.

**Added**

- `natural-writing`, preloaded into the 21 agents that write prose, so the pasted "Human-Sounding Writing Protocol" is gone from the commands.
- `interview-me` and `graph-engineering` skills.
- `/02-BUILD/03-review-code` also runs Claude Code's built-in `code-review` and `security-review`.

**Changed**

- README leads with the brand, planning, and creator workflows.

## 1.5.5

Builder skills checked against the official docs (September 2026):

- `slash-command-builder`: positional arguments are 0-based (`$0` is the first), so every example shifted down by one. Added named arguments, the commands-and-skills merge, and the full frontmatter table.
- `skill-builder` and `slash-command-builder`: `allowed-tools` pre-approves tools and does not restrict them; `disallowed-tools` restricts. Both skills taught the opposite.
- `agent-builder`: full frontmatter table (adds `disallowedTools`, `effort`, `maxTurns`, `memory`, `isolation`, `mcpServers`, `hooks`, `background`, `omitClaudeMd`, `color`), `fable` in the model guide, the plugin subfolder addressing rule, and the correct default when `model` is omitted.
- `hooks-builder`: about 25 additional events and the `http`, `mcp_tool`, and `agent` handler types.
- `marketplace-builder`: a git URL plugin source is `"url"`, not `"git"`, and there is no `"directory"` plugin source. Added `git-subdir`, `npm`, and `archive`, and the plugin-source versus marketplace-source distinction.
- The Task tool is now the Agent tool in all prompts and `allowed-tools` lists.
- `marketplace-builder` and `hooks-builder` SKILL.md files are back under 500 lines.

## 1.5.4

- Added `scripts/validate_plugin.py` and a CI workflow that check frontmatter, agent and skill references, relative links, MCP version pinning, and the counts claimed in `marketplace.json`.
- Fixed frontmatter in six agents and one command whose unquoted descriptions were not valid YAML.
- Added CONTRIBUTING, SECURITY, and this changelog. Documented the bundled skills in the README.

## 1.5.3

- Rewrote all 19 knowledge-skill descriptions to state when to use the skill, and removed trigger overlap between sibling skills.
- Reference pointers now say when to load the file. Every supporting file over 300 lines has a table of contents.
- Platform, Midjourney, and model-fingerprint content carries a last-verified date.
- CODING agents have "Use when" descriptions.

## 1.5.2

- Fixed agent launches in BUILD, DEBUG, REFACTOR, and TOOLKIT commands. Agents in subfolders register as `claude-vibes:<FOLDER>:<name>`, and these commands used shorter forms.
- Reasoning, review, and brand strategy agents now run on `fable`. Implementation agents stay on `opus`.
- `slash-command-builder` now explains that `[execute: ...]` is a placeholder for the real injection syntax.
- Corrected marketplace counts, completed `plugin.json` metadata, and pinned the whois MCP server.

## 1.5.1 and earlier

See the [commit history](https://github.com/mike-coulbourn/claude-vibes/commits/main).
