# Changelog

Notable changes to the claude-vibes plugin. Versions follow the `version` field in `plugins/vibes/.claude-plugin/plugin.json`.

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
