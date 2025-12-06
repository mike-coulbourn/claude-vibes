# Claude Vibes

A production-grade plugin suite for **vibe coding** with Claude Code.

Vibe coding is describing WHAT you want while Claude handles HOW to build it. These plugins provide structured workflows, specialized agents, and intelligent tools that transform ideas into production-ready code.

---

## Installation

### Option 1: Install from GitHub (Recommended)

```bash
# Add the marketplace
/plugin marketplace add your-username/claude-vibes

# Install all plugins
/plugin install 01-start@claude-vibes
/plugin install 02-build@claude-vibes
/plugin install 03-ship@claude-vibes
/plugin install 04-fix@claude-vibes
/plugin install 05-refactor@claude-vibes

# Restart Claude Code to activate
```

### Option 2: Install Locally

```bash
# Clone the repository
git clone https://github.com/your-username/claude-vibes.git

# Add as local marketplace (use your actual path)
/plugin marketplace add /path/to/claude-vibes

# Install plugins
/plugin install 01-start@claude-vibes
/plugin install 02-build@claude-vibes
/plugin install 03-ship@claude-vibes
/plugin install 04-fix@claude-vibes
/plugin install 05-refactor@claude-vibes

# Restart Claude Code to activate
```

### Verify Installation

After restarting Claude Code:

```bash
# Check plugins are installed
/plugin

# Verify MCP servers are running
/mcp

# See all available commands
/help
```

You should see commands like `/01-start/01-discover`, `/02-build/02-build`, etc.

### Team Installation

Add to your repository's `.claude/settings.json` for automatic team setup:

```json
{
  "plugins": {
    "marketplaces": ["your-org/claude-vibes"],
    "installed": [
      "01-start@claude-vibes",
      "02-build@claude-vibes",
      "03-ship@claude-vibes",
      "04-fix@claude-vibes",
      "05-refactor@claude-vibes"
    ]
  }
}
```

When team members trust the repository folder, plugins install automatically.

---

## The Workflow

```
start → build → ship → fix → refactor
  ↓       ↓       ↓      ↓        ↓
 Plan   Code   Deploy  Debug   Evolve
```

Each phase has dedicated plugins with commands and agents designed for that stage of development.

---

## Plugins

### 01-start (Discovery & Planning)

Plan before you build. Discover the problem space, scope your MVP, and create an implementation roadmap.

**Commands:**
| Command | Description |
|---------|-------------|
| `/01-start/01-discover` | Understand the problem space and user needs |
| `/01-start/02-scope` | Define MVP boundaries and prioritize features |
| `/01-start/03-architect` | Plan technical approach and system design |
| `/01-start/04-plan` | Create implementation roadmap with phases |

**Agents:**
- `market-validator` - Research market viability and competition
- `feature-brainstormer` - Generate and prioritize feature ideas
- `tech-advisor` - Recommend technology choices
- `plan-reviewer` - Review and improve implementation plans
- `data-modeler` - Design data structures and schemas

---

### 02-build (Implementation)

Build features methodically. Plan each feature, implement with best practices, and review before shipping.

**Commands:**
| Command | Description |
|---------|-------------|
| `/02-build/01-plan` | Break down feature into implementation steps |
| `/02-build/02-build` | Implement the feature with production quality |
| `/02-build/03-review` | Review code for production readiness |

**Agents:**
- `code-architect` - Design feature architecture and patterns
- `code-guru` - Implement features with best practices
- `code-reviewer` - Thorough code review and quality checks

---

### 03-ship (Deployment)

Ship with confidence. Run checks, commit cleanly, and create PRs.

**Commands:**
| Command | Description |
|---------|-------------|
| `/03-ship/01-check` | Run linting, tests, and pre-commit checks |
| `/03-ship/02-commit` | Create a clean commit with descriptive message |
| `/03-ship/03-push` | Push to remote branch |
| `/03-ship/04-pr` | Create pull request with summary |

---

### 04-fix (Debugging)

Fix bugs systematically. Diagnose root causes, apply fixes, and verify they work.

**Commands:**
| Command | Description |
|---------|-------------|
| `/04-fix/01-diagnose` | Investigate and identify root cause |
| `/04-fix/02-fix` | Apply the fix with minimal changes |
| `/04-fix/03-verify` | Verify fix works and document in LOGS.json |

**Agents:**
- `diagnostician` - Deep investigation and root cause analysis
- `fixer` - Minimal, targeted bug fixes
- `verifier` - Verification and regression testing

---

### 05-refactor (Code Evolution)

Improve code without changing behavior. Assess opportunities, refactor safely, and validate preservation.

**Commands:**
| Command | Description |
|---------|-------------|
| `/05-refactor/01-assess` | Identify refactoring opportunities |
| `/05-refactor/02-refactor` | Apply refactoring with behavior preservation |
| `/05-refactor/03-validate` | Verify behavior unchanged, document in LOGS.json |

**Agents:**
- `assessor` - Code archaeology and improvement analysis
- `refactorer` - Safe structural improvements
- `validator` - Behavior preservation verification

---

## MCP Servers

MCP (Model Context Protocol) servers extend Claude Code with additional capabilities. This plugin suite auto-installs essential servers that work out of the box.

### Auto-Installed (No Setup Required)

These servers start automatically when the plugin is enabled:

| Server | Purpose | Official Source |
|--------|---------|-----------------|
| **Context7** | Up-to-date documentation in prompts | [github.com/upstash/context7](https://github.com/upstash/context7) |
| **Memory** | Persistent knowledge graph across sessions | [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers/tree/main/src/memory) |
| **Sequential Thinking** | Structured problem-solving | [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers/tree/main/src/sequentialthinking) |

**Usage Tips:**
- Add `use context7` to prompts for current library documentation
- Memory persists entities, relations, and observations across sessions
- Sequential Thinking excels at complex multi-step problems

### Optional Servers (Require Setup)

Add these based on your workflow. Each requires authentication or additional setup.

#### Version Control & Issues

| Server | Purpose | Install | Docs |
|--------|---------|---------|------|
| **GitHub** | PR/issue management | `claude mcp add --transport http github https://api.githubcopilot.com/mcp` | [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) |
| **Linear** | Issue tracking | Connect via `/mcp` | [linear.app/changelog/2025-05-01-mcp](https://linear.app/changelog/2025-05-01-mcp) |

#### Debugging & Testing

| Server | Purpose | Install | Docs |
|--------|---------|---------|------|
| **Sentry** | Error tracking | `claude mcp add --transport http sentry https://mcp.sentry.dev/mcp` | [docs.sentry.io/product/sentry-mcp](https://docs.sentry.io/product/sentry-mcp/) |
| **Playwright** | Browser automation | `claude mcp add playwright -- npx @playwright/mcp@latest` | [github.com/microsoft/playwright-mcp](https://github.com/microsoft/playwright-mcp) |

#### Database & Backend

| Server | Purpose | Install | Docs |
|--------|---------|---------|------|
| **Supabase** | Database management | Configure via JSON | [supabase.com/docs/guides/getting-started/mcp](https://supabase.com/docs/guides/getting-started/mcp) |
| **PostgreSQL** | SQL queries | `claude mcp add-json "postgres" '{"command":"npx","args":["-y","@modelcontextprotocol/server-postgres"]}'` | [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) |

#### Deployment

| Server | Purpose | Install | Docs |
|--------|---------|---------|------|
| **Cloudflare** | Edge deployment | `claude mcp add --transport sse cloudflare https://mcp.cloudflare.com/sse` | [github.com/cloudflare/mcp-server-cloudflare](https://github.com/cloudflare/mcp-server-cloudflare) |
| **Vercel** | Frontend hosting | `claude mcp add-json "vercel" '{"command":"npx","args":["-y","vercel-mcp"]}'` | [vercel.com/docs/mcp/vercel-mcp](https://vercel.com/docs/mcp/vercel-mcp) |

### Best Practice

> Start with the auto-installed essentials. Add specialized servers only when you need them. Too many MCP servers can slow down Claude Code startup.

---

## LOGS.json

All plugins share a unified `LOGS.json` file at the project root for compounding learning. Each phase writes entries with relevant metadata:

```json
{
  "entries": [
    {
      "id": "entry-1733500800000",
      "timestamp": "2025-12-06T12:00:00Z",
      "phase": "build",
      "type": "feature",
      "area": "auth",
      "summary": "Added OAuth2 login flow",
      "patterns": ["oauth-provider-pattern"],
      "files": ["src/auth/oauth.ts"],
      "tags": ["auth", "oauth", "login"]
    }
  ],
  "patterns": {
    "oauth-provider-pattern": "Use provider abstraction for OAuth flows"
  }
}
```

The `phase` field enables filtering while the unified file enables cross-phase learning.

---

## Agent MCP Integration

Each agent is configured to use MCP servers when relevant:

| Agent | Context7 | Memory | Sequential Thinking |
|-------|:--------:|:------:|:-------------------:|
| **01-start** |
| tech-advisor | ✓ | ✓ | ✓ |
| data-modeler | ✓ | ✓ | ✓ |
| plan-reviewer | — | ✓ | ✓ |
| **02-build** |
| code-guru | ✓ | ✓ | — |
| code-architect | ✓ | ✓ | ✓ |
| code-reviewer | ✓ | ✓ | ✓ |
| **04-fix** |
| diagnostician | ✓ | ✓ | ✓ |
| fixer | ✓ | ✓ | — |
| verifier | — | ✓ | ✓ |
| **05-refactor** |
| assessor | — | ✓ | ✓ |
| refactorer | — | ✓ | — |
| validator | — | ✓ | ✓ |

**How agents use MCP servers:**
- **Context7**: Fetches current library documentation for accurate code generation and review
- **Memory**: Stores and recalls project patterns, past decisions, and lessons learned
- **Sequential Thinking**: Structures complex analysis, diagnosis, and planning tasks

---

## Structure

```
claude-vibes/
├── .claude-plugin/
│   └── marketplace.json         # Plugin marketplace manifest
├── .mcp.json                    # Auto-installed MCP servers
├── README.md                    # This file
└── plugins/
    ├── 01-start/                # Discovery & Planning
    │   ├── plugin.json
    │   ├── commands/
    │   └── agents/
    ├── 02-build/                # Implementation
    │   ├── plugin.json
    │   ├── commands/
    │   └── agents/
    ├── 03-ship/                 # Deployment
    │   ├── plugin.json
    │   └── commands/
    ├── 04-fix/                  # Debugging
    │   ├── plugin.json
    │   ├── commands/
    │   └── agents/
    └── 05-refactor/             # Code Evolution
        ├── plugin.json
        ├── commands/
        └── agents/
```

---

## Requirements

- **Claude Code** v2.0.12 or higher
- **Node.js** 18+ (for MCP servers via npx)

---

## References

### Plugins
- [Plugins Overview](https://code.claude.com/docs/en/plugins) - Install and create plugins
- [Plugins Reference](https://code.claude.com/docs/en/plugins-reference) - Technical specifications
- [Plugin Announcement](https://www.anthropic.com/news/claude-code-plugins) - Introduction to the plugin system

### Plugin Components
- [Slash Commands](https://code.claude.com/docs/en/slash-commands) - Custom command syntax
- [Subagents](https://code.claude.com/docs/en/sub-agents) - Specialized agent configuration
- [Hooks Reference](https://code.claude.com/docs/en/hooks) - Event-driven automation
- [Agent Skills](https://www.anthropic.com/news/skills) - Model-invoked capabilities

### MCP (Model Context Protocol)
- [Claude Code MCP](https://docs.anthropic.com/en/docs/claude-code/mcp) - Connect to external tools
- [Introducing MCP](https://www.anthropic.com/news/model-context-protocol) - Protocol overview

### Claude Code
- [Claude Code Overview](https://docs.anthropic.com/en/docs/claude-code/overview) - Getting started
- [Best Practices](https://www.anthropic.com/engineering/claude-code-best-practices) - Agentic coding patterns

---

## License

MIT
