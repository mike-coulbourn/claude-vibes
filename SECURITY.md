# Security

claude-vibes is Markdown prompts plus a `plugin.json` that starts three MCP servers. Two of them (Taskmaster and Whois) run on your machine through `npx`, and one (Context7) is a hosted service that receives the library-documentation lookups you send it. The main risks are a compromised MCP package and a prompt that tells Claude to do something unsafe.

## Supported versions

Fixes go into the latest release only. Update with `claude plugin update claude-vibes@claude-vibes`.

## Reporting a vulnerability

Please report privately through [GitHub security advisories](https://github.com/mike-coulbourn/claude-vibes/security/advisories/new) rather than a public issue. Include the file involved and what it could cause.

## What the plugin does and does not do

- It ships no hooks and no executable scripts. `scripts/validate_plugin.py` is a repo check that is not part of the installed plugin.
- CI rejects any MCP package pinned to `@latest`. The Whois package is pinned to an exact version.
- The ship commands run `git commit`, `git push`, and `gh pr create` for you. The commit command shows you the message and waits for approval. The push and pull request commands act when you run them, and they never force-push without your approval.
- Coding agents keep notes in `.claude/agent-memory/` inside your project. Review that folder before committing it, as you would any other file.
