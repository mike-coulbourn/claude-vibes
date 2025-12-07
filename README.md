# Claude Vibes

A production-grade plugin for **vibe coding** with Claude Code.

Vibe coding is describing WHAT you want while Claude handles HOW to build it. This plugin provides structured workflows, specialized agents, and intelligent tools that transform ideas into production-ready code.

---

## Installation

Open **Terminal** (press `Cmd + Space`, type "Terminal", hit Enter).

### 1. Install Homebrew

```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

### 2. Install Node.js

Node.js 18+ is required for MCP servers.

```
brew install node
```

### 3. Install Claude Code

```
brew install --cask claude-code
```

### 4. Start Claude Code

Navigate to your project folder and start a session:
```
claude
```

### 5. Install Claude Vibes

Add the marketplace:
```
/plugin marketplace add mike-coulbourn/claude-vibes
```

Then install the plugin:
```
/plugin
```

Select **Browse and install plugins** → choose **claude-vibes**.

### Verify

After restarting, run `/help` to see your new commands.

### Local Install (Alternative)

```
git clone https://github.com/mike-coulbourn/claude-vibes.git
```

Add as a local marketplace:
```
/plugin marketplace add ./claude-vibes
```

### Team Installation

Add to your repository's `.claude/settings.json` for automatic team setup:

```json
{
  "plugins": {
    "marketplaces": ["mike-coulbourn/claude-vibes"],
    "installed": ["claude-vibes@claude-vibes"]
  }
}
```

When team members trust the repository folder, the plugin installs automatically.

---

## The Workflow

```
START → BUILD → SHIP → FIX → REFACTOR
  ↓       ↓       ↓      ↓        ↓
 Plan   Code   Deploy  Debug   Evolve
```

Each phase has dedicated commands and agents designed for that stage of development.

---

## Commands & Agents

### 01-START (Discovery & Planning)

Plan before you build. Discover the problem space, scope your MVP, and create an implementation roadmap.

**Commands:**
| Command | Description |
|---------|-------------|
| `/claude-vibes:01-START/01-discover` | Understand the problem space and user needs |
| `/claude-vibes:01-START/02-scope` | Define MVP boundaries and prioritize features |
| `/claude-vibes:01-START/03-architect` | Plan technical approach and system design |
| `/claude-vibes:01-START/04-plan` | Create implementation roadmap with phases |

**Agents:**
- `market-validator` - Research market viability and competition
- `feature-brainstormer` - Generate and prioritize feature ideas
- `tech-advisor` - Recommend technology choices
- `plan-reviewer` - Review and improve implementation plans
- `data-modeler` - Design data structures and schemas

---

### 02-BUILD (Implementation)

Build features methodically. Plan each feature, implement with best practices, and review before shipping.

**Commands:**
| Command | Description |
|---------|-------------|
| `/claude-vibes:02-BUILD/01-plan` | Break down feature into implementation steps |
| `/claude-vibes:02-BUILD/02-build` | Implement the feature with production quality |
| `/claude-vibes:02-BUILD/03-review` | Review code for production readiness |

**Agents:**
- `code-architect` - Design feature architecture and patterns
- `code-guru` - Implement features with best practices
- `code-reviewer` - Thorough code review and quality checks

---

### 03-SHIP (Deployment)

Ship with confidence. Run checks, commit cleanly, and create PRs.

**Commands:**
| Command | Description |
|---------|-------------|
| `/claude-vibes:03-SHIP/01-check` | Run linting, tests, and pre-commit checks |
| `/claude-vibes:03-SHIP/02-commit` | Create a clean commit with descriptive message |
| `/claude-vibes:03-SHIP/03-push` | Push to remote branch |
| `/claude-vibes:03-SHIP/04-pr` | Create pull request with summary |

---

### 04-FIX (Debugging)

Fix bugs systematically. Diagnose root causes, apply fixes, and verify they work.

**Commands:**
| Command | Description |
|---------|-------------|
| `/claude-vibes:04-FIX/01-diagnose` | Investigate and identify root cause |
| `/claude-vibes:04-FIX/02-fix` | Apply the fix with minimal changes |
| `/claude-vibes:04-FIX/03-verify` | Verify fix works and document in LOGS.json |

**Agents:**
- `diagnostician` - Deep investigation and root cause analysis
- `fixer` - Minimal, targeted bug fixes
- `verifier` - Verification and regression testing

---

### 05-REFACTOR (Code Evolution)

Improve code without changing behavior. Assess opportunities, refactor safely, and validate preservation.

**Commands:**
| Command | Description |
|---------|-------------|
| `/claude-vibes:05-REFACTOR/01-assess` | Identify refactoring opportunities |
| `/claude-vibes:05-REFACTOR/02-refactor` | Apply refactoring with behavior preservation |
| `/claude-vibes:05-REFACTOR/03-validate` | Verify behavior unchanged, document in LOGS.json |

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

## Structure

```
claude-vibes/
├── .claude-plugin/
│   └── marketplace.json         # Plugin marketplace manifest
├── README.md                    # This file
└── plugins/
    └── claude-vibes/            # Bundled plugin
        ├── .claude-plugin/
        │   └── plugin.json      # Plugin manifest with MCP servers
        ├── commands/
        │   ├── 01-START/        # Discovery & Planning
        │   ├── 02-BUILD/        # Implementation
        │   ├── 03-SHIP/         # Deployment
        │   ├── 04-FIX/          # Debugging
        │   └── 05-REFACTOR/     # Code Evolution
        └── agents/              # All 14 agents
```

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

