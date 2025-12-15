# 😎 Claude Vibes

A plugin for **vibe coding** production-grade apps with Claude Code.

Vibe coding is describing WHAT you want while Claude handles HOW to build it. This plugin provides structured workflows, specialized agents, and intelligent tools that transform ideas into production-ready code.

---

## 📦 Installation

Open your project in your IDE of choice (VS Code, Cursor, etc.) and open the integrated terminal.

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

### 4. Install Claude Vibes

```bash
mkdir -p .taskmaster && printf '{\n  "models": {\n    "main": {\n      "provider": "claude-code",\n      "modelId": "opus"\n    }\n  }\n}\n' > .taskmaster/config.json && grep -qxF '.taskmaster/' .gitignore 2>/dev/null || echo '.taskmaster/' >> .gitignore && claude "/plugin marketplace add mike-coulbourn/claude-vibes"
```

### 5. Start Using Claude Vibes

Type `/exit`, then run `claude` again to load the plugin. Run `/help` to see your new commands.

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
  "extraKnownMarketplaces": {
    "claude-vibes": {
      "source": {
        "source": "github",
        "repo": "mike-coulbourn/claude-vibes"
      }
    }
  },
  "enabledPlugins": {
    "claude-vibes@claude-vibes": true
  }
}
```

When team members trust the repository folder, the plugin installs automatically.

---

## 🔄 The Workflow

```
START → BUILD → SHIP → FIX → REFACTOR
  ↓       ↓       ↓      ↓        ↓
 Plan   Code   Deploy  Debug   Evolve
```

Each phase has dedicated commands and agents designed for that stage of development.

---

## 🤖 Commands & Agents

### 🎨 00-BRAND (Brand Identity)

Create complete brand identities for startups. A structured workflow from discovery through final guidelines.

**Commands:**

#### Discovery Phase
| Command | Description |
|---------|-------------|
| `/claude-vibes:00-BRAND/00-discover/01-discover-founder` | Interactive founder discovery session |
| `/claude-vibes:00-BRAND/00-discover/02-research-audience` | Research and define target audience |
| `/claude-vibes:00-BRAND/00-discover/03-audit-competitors` | Audit competitor brands |
| `/claude-vibes:00-BRAND/00-discover/04-name-brand` | Finalize brand name with domain verification |

#### Strategy Phase
| Command | Description |
|---------|-------------|
| `/claude-vibes:00-BRAND/01-strategy/01-define-purpose` | Define purpose, mission, and vision |
| `/claude-vibes:00-BRAND/01-strategy/02-define-values` | Define differentiating core values |
| `/claude-vibes:00-BRAND/01-strategy/03-define-positioning` | Develop positioning strategy |
| `/claude-vibes:00-BRAND/01-strategy/04-select-archetype` | Select brand archetype |
| `/claude-vibes:00-BRAND/01-strategy/05-define-voice` | Define brand voice and personality |

#### Messaging Phase
| Command | Description |
|---------|-------------|
| `/claude-vibes:00-BRAND/02-messaging/01-create-framework` | Create messaging framework |
| `/claude-vibes:00-BRAND/02-messaging/02-create-tagline` | Create tagline options |
| `/claude-vibes:00-BRAND/02-messaging/03-write-pitch` | Write elevator pitch variations |

#### Visual Phase
| Command | Description |
|---------|-------------|
| `/claude-vibes:00-BRAND/03-visual/01-set-direction` | Create visual identity direction |
| `/claude-vibes:00-BRAND/03-visual/02-choose-colors` | Develop brand color palette |
| `/claude-vibes:00-BRAND/03-visual/03-select-typography` | Develop typography system |

#### Compile Phase
| Command | Description |
|---------|-------------|
| `/claude-vibes:00-BRAND/04-compile/01-compile-guidelines` | Compile final brand guidelines |

**Agents:**
- `brand-archetype-selector` - Jungian archetype selection
- `brand-audience-researcher` - Psychographic analysis and audience profiling
- `brand-color-strategist` - Strategic color palette development
- `brand-competitive-auditor` - Competitor visual identity analysis
- `brand-elevator-pitch-writer` - Elevator pitch variations
- `brand-messaging-architect` - Value proposition and brand pillars
- `brand-naming-specialist` - Strategic name development
- `brand-positioning-strategist` - Positioning and onliness statements
- `brand-purpose-architect` - Purpose, mission, vision (Golden Circle)
- `brand-tagline-creator` - Memorable tagline creation
- `brand-typography-curator` - Typography system and font selection
- `brand-values-curator` - Core values discovery and articulation
- `brand-visual-director` - Visual identity direction and briefs
- `brand-voice-architect` - Voice and verbal identity guidelines
- `startup-brand-architect` - Orchestrates complete brand identity creation

---

### 🧐 01-START (Discovery & Planning)

Plan before you build. Discover the problem space, scope your MVP, and create an implementation roadmap.

**Commands:**
| Command | Description |
|---------|-------------|
| `/claude-vibes:01-START/01-discover` | Understand the problem space and user needs |
| `/claude-vibes:01-START/02-scope` | Define MVP boundaries and prioritize features |
| `/claude-vibes:01-START/03-architect` | Plan technical approach and system design |
| `/claude-vibes:01-START/04-plan-roadmap` | Create implementation roadmap with phases |

**Agents:**
- `market-validator` - Research market viability and competition
- `feature-brainstormer` - Generate and prioritize feature ideas
- `tech-advisor` - Recommend technology choices
- `plan-reviewer` - Review and improve implementation plans
- `data-modeler` - Design data structures and schemas

---

### 🏗️ 02-BUILD (Implementation)

Build features methodically. Plan each feature, implement with best practices, and review before shipping.

**Commands:**
| Command | Description |
|---------|-------------|
| `/claude-vibes:02-BUILD/01-plan-code` | Plan the code implementation |
| `/claude-vibes:02-BUILD/02-write-code` | Write the code with production quality |
| `/claude-vibes:02-BUILD/03-review-code` | Review code for production readiness |

**Agents:**
- `code-architect` - Design feature architecture and patterns
- `code-guru` - Implement features with best practices
- `code-reviewer` - Thorough code review and quality checks
- `tester` - Write and run tests iteratively to prove code works

---

### 🚀 03-SHIP (Deployment)

Ship with confidence. Run checks, commit cleanly, and create PRs.

**Commands:**
| Command | Description |
|---------|-------------|
| `/claude-vibes:03-SHIP/01-pre-commit` | Run linting, tests, and pre-commit checks |
| `/claude-vibes:03-SHIP/02-commit` | Create a clean commit with descriptive message |
| `/claude-vibes:03-SHIP/03-push` | Push to remote branch |
| `/claude-vibes:03-SHIP/04-pr` | Create pull request with summary |

---

### 🔧 04-DEBUG (Debugging)

Fix bugs systematically. Diagnose root causes, apply fixes, and verify they work.

**Commands:**
| Command | Description |
|---------|-------------|
| `/claude-vibes:04-DEBUG/01-diagnose-issue` | Investigate and identify root cause |
| `/claude-vibes:04-DEBUG/02-fix-issue` | Apply the fix with minimal changes |
| `/claude-vibes:04-DEBUG/03-verify-fix` | Verify fix works correctly |

**Agents:**
- `diagnostician` - Deep investigation and root cause analysis
- `fixer` - Minimal, targeted bug fixes
- `verifier` - Verification and regression testing
- `tester` - Write and run tests to prove fixes work

---

### ✨ 05-REFACTOR (Code Evolution)

Improve code without changing behavior. Assess opportunities, refactor safely, and validate preservation.

**Commands:**
| Command | Description |
|---------|-------------|
| `/claude-vibes:05-REFACTOR/01-assess-improvements` | Identify improvement opportunities |
| `/claude-vibes:05-REFACTOR/02-improve-code` | Apply improvements with behavior preservation |
| `/claude-vibes:05-REFACTOR/03-validate-improvements` | Verify behavior unchanged |

**Agents:**
- `assessor` - Code archaeology and improvement analysis
- `refactorer` - Safe structural improvements
- `validator` - Behavior preservation verification
- `tester` - Write and run tests to prove behavior preserved

---

### 🧰 TOOLKIT (Specialized Tools)

Utility commands and agents for tasks outside the main development workflow.

**Commands:**
| Command | Description |
|---------|-------------|
| `/claude-vibes:TOOLKIT/create-brand` | Create complete brand identity interactively |
| `/claude-vibes:TOOLKIT/nano-banana-prompt` | Craft prompts for Nano Banana Pro image generation |
| `/claude-vibes:TOOLKIT/research` | Deep research on any topic |
| `/claude-vibes:TOOLKIT/research-brand` | Research a brand for sponsored content |
| `/claude-vibes:TOOLKIT/write` | Write emails, messages, notes naturally |
| `/claude-vibes:TOOLKIT/write-copy` | Create high-converting marketing copy |
| `/claude-vibes:TOOLKIT/write-sponsor-script` | Write scripts for sponsored/affiliate content |

**Agents:**
- `ai-writing-detector` - Analyze text for AI writing patterns
- `brand-researcher` - Deep brand research for content creators
- `deep-researcher` - Comprehensive expert knowledge research
- `elite-copywriter` - Transform text into compelling copy
- `hook-generator` - Generate scroll-stopping hook variations
- `nano-banana-pro-expert` - Guidance for Nano Banana Pro image generation
- `sponsor-script-writer` - Write high-converting sponsored content scripts

---

## 🔌 MCP Servers

MCP (Model Context Protocol) servers extend Claude Code with additional capabilities. This plugin suite auto-installs essential servers that work out of the box.

### ✅ Auto-Installed (No Setup Required)

These servers start automatically when the plugin is enabled:

| Server | Purpose | Official Source |
|--------|---------|-----------------|
| **Context7** | Up-to-date documentation in prompts | [github.com/upstash/context7](https://github.com/upstash/context7) |
| **Memory** | Persistent knowledge graph across sessions | [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers/tree/main/src/memory) |
| **Sequential Thinking** | Structured problem-solving | [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers/tree/main/src/sequentialthinking) |
| **Taskmaster** | AI-powered task management | [github.com/eyaltoledano/claude-task-master](https://github.com/eyaltoledano/claude-task-master) |

**Usage Tips:**
- Add `use context7` to prompts for current library documentation
- Memory persists entities, relations, and observations across sessions
- Sequential Thinking excels at complex multi-step problems
- Taskmaster config is created automatically during installation (step 4)

### ⚙️ Optional Servers (Require Setup)

Add these based on your workflow. Each requires authentication or additional setup.

#### 🔀 Version Control & Issues

| Server | Purpose | Install | Docs |
|--------|---------|---------|------|
| **GitHub** | PR/issue management | `claude mcp add --transport http github https://api.githubcopilot.com/mcp` | [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) |
| **Linear** | Issue tracking | Connect via `/mcp` | [linear.app/changelog/2025-05-01-mcp](https://linear.app/changelog/2025-05-01-mcp) |

#### 🐛 Debugging & Testing

| Server | Purpose | Install | Docs |
|--------|---------|---------|------|
| **Sentry** | Error tracking | `claude mcp add --transport http sentry https://mcp.sentry.dev/mcp` | [docs.sentry.io/product/sentry-mcp](https://docs.sentry.io/product/sentry-mcp/) |
| **Playwright** | Browser automation | `claude mcp add playwright -- npx @playwright/mcp@latest` | [github.com/microsoft/playwright-mcp](https://github.com/microsoft/playwright-mcp) |

#### 🗄️ Database & Backend

| Server | Purpose | Install | Docs |
|--------|---------|---------|------|
| **Supabase** | Database management | Configure via JSON | [supabase.com/docs/guides/getting-started/mcp](https://supabase.com/docs/guides/getting-started/mcp) |
| **PostgreSQL** | SQL queries | `claude mcp add-json "postgres" '{"command":"npx","args":["-y","@modelcontextprotocol/server-postgres"]}'` | [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) |

#### 🌐 Deployment

| Server | Purpose | Install | Docs |
|--------|---------|---------|------|
| **Cloudflare** | Edge deployment | `claude mcp add --transport sse cloudflare https://mcp.cloudflare.com/sse` | [github.com/cloudflare/mcp-server-cloudflare](https://github.com/cloudflare/mcp-server-cloudflare) |
| **Vercel** | Frontend hosting | `claude mcp add-json "vercel" '{"command":"npx","args":["-y","vercel-mcp"]}'` | [vercel.com/docs/mcp/vercel-mcp](https://vercel.com/docs/mcp/vercel-mcp) |

### 💡 Best Practice

> Start with the auto-installed essentials. Add specialized servers only when you need them. Too many MCP servers can slow down Claude Code startup.

---

## 📁 Structure

```
claude-vibes/
├── .claude-plugin/
│   └── marketplace.json         # Plugin marketplace manifest
├── README.md                    # This file
└── plugins/
    └── vibes/                   # Bundled plugin
        ├── .claude-plugin/
        │   └── plugin.json      # Plugin manifest with MCP servers
        ├── commands/
        │   ├── 00-BRAND/        # Brand Identity
        │   ├── 01-START/        # Discovery & Planning
        │   ├── 02-BUILD/        # Implementation
        │   ├── 03-SHIP/         # Deployment
        │   ├── 04-DEBUG/        # Debugging
        │   ├── 05-REFACTOR/     # Code Evolution
        │   └── TOOLKIT/         # Specialized Tools
        ├── agents/
        │   ├── BRANDING/        # Brand identity agents
        │   ├── CODING/          # Development agents
        │   └── TOOLKIT/         # Utility agents
        └── skills/              # Agent enhancement skills
```

---

## 📚 References

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

