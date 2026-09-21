# Security

claude-vibes ships prompts plus a `plugin.json` that launches MCP servers through `npx` on the user's machine, so the main risks are a compromised or unpinned MCP package and a prompt that instructs Claude to do something unsafe.

## Reporting a vulnerability

Please report privately through [GitHub security advisories](https://github.com/mike-coulbourn/claude-vibes/security/advisories/new) rather than a public issue. Include the file involved and what it could cause.

## What we do

- MCP server packages are pinned where the publisher is not a well-known vendor, and CI rejects `@latest`.
- The plugin ships no hooks and no executable scripts.
