# Changelog

Notable changes to the claude-vibes plugin. Versions follow the `version` field in `plugins/vibes/.claude-plugin/plugin.json`.

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
