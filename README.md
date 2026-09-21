# 😎 Claude Vibes

A Claude Code plugin for people who describe WHAT they want and let Claude handle HOW.

It covers three things that Claude Code does not ship on its own:

- **Build a brand from nothing.** Sixteen guided commands take you from founder interview to a compiled brand guidelines document: purpose, values, positioning, archetype, voice, messaging, tagline, pitch, colors, and typography.
- **Turn an idea into a plan, and stay on it.** Discovery, scoping, and architecture, then the `graph-engineering` skill designs the whole project as a graph of jobs with real dependencies, separate checks, and approval points, covering code, brand work, content, account setup, legal, and launch. The approved graph is saved as a checklist that every command reads before it works, and anything not on it has to be added on purpose. That is what stops a project from drifting.
- **A creator toolkit.** Sponsor scripts, hooks, marketing copy, deep research, and image prompts for Midjourney and Nano Banana Pro.

It also wraps building, shipping, debugging, and refactoring in the same plain-language, confirm-before-acting style, and leans on Claude Code's built-in review, reasoning, and memory wherever those exist.

---

## Installation

### 1. Install Claude Code

macOS, Linux, or WSL:

```bash
curl -fsSL https://claude.ai/install.sh | bash
```

Windows PowerShell:

```powershell
irm https://claude.ai/install.ps1 | iex
```

This is Anthropic's native installer, and it keeps Claude Code updated automatically. Homebrew (`brew install --cask claude-code`) and WinGet also work, but they do not auto-update by default. Already have Claude Code? Skip this step.

### 2. Install Node.js 18+ (only for brand naming)

The Whois server, which checks whether a domain is free while you name a brand, starts through `npx`. If you will use that command, install Node from [nodejs.org](https://nodejs.org), or with `brew install node` on macOS. Everything else works without Node.

### 3. Install Claude Vibes

```bash
claude plugin marketplace add mike-coulbourn/claude-vibes
```

```bash
claude plugin install claude-vibes@claude-vibes
```

### 4. Start

Open a terminal in your project folder, run `claude`, and type `/` to see the new commands. If Claude Code was already running, restart it or run `/reload-plugins`.

To update later, run `claude plugin update claude-vibes@claude-vibes`, then restart Claude Code.

### Local install (alternative)

```
git clone https://github.com/mike-coulbourn/claude-vibes.git
```

Add as a local marketplace:
```
/plugin marketplace add ./claude-vibes
```

### Team installation

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

## The workflow

```
BRAND → START → BUILD → SHIP → FIX → REFACTOR        + TOOLKIT (any time)
  ↓       ↓       ↓       ↓      ↓        ↓
Identity Plan   Code   Deploy  Debug   Evolve
```

Each phase has its own commands and agents.

---

## Commands and agents

### 00-BRAND (brand identity)

Build a startup's brand identity step by step, from the founder interview to a finished guidelines document.

**Commands:**

#### Discovery phase
| Command | Description |
|---------|-------------|
| `/claude-vibes:00-BRAND/00-discover/01-discover-founder` | Interactive founder discovery session |
| `/claude-vibes:00-BRAND/00-discover/02-research-audience` | Research and define target audience |
| `/claude-vibes:00-BRAND/00-discover/03-audit-competitors` | Audit competitor brands |
| `/claude-vibes:00-BRAND/00-discover/04-name-brand` | Finalize brand name with domain verification |

#### Strategy phase
| Command | Description |
|---------|-------------|
| `/claude-vibes:00-BRAND/01-strategy/01-define-purpose` | Define purpose, mission, and vision |
| `/claude-vibes:00-BRAND/01-strategy/02-define-values` | Define differentiating core values |
| `/claude-vibes:00-BRAND/01-strategy/03-define-positioning` | Develop positioning strategy |
| `/claude-vibes:00-BRAND/01-strategy/04-select-archetype` | Select brand archetype |
| `/claude-vibes:00-BRAND/01-strategy/05-define-voice` | Define brand voice and personality |

#### Messaging phase
| Command | Description |
|---------|-------------|
| `/claude-vibes:00-BRAND/02-messaging/01-create-framework` | Create messaging framework |
| `/claude-vibes:00-BRAND/02-messaging/02-create-tagline` | Create tagline options |
| `/claude-vibes:00-BRAND/02-messaging/03-write-pitch` | Write elevator pitch variations |

#### Visual phase
| Command | Description |
|---------|-------------|
| `/claude-vibes:00-BRAND/03-visual/01-set-direction` | Create visual identity direction |
| `/claude-vibes:00-BRAND/03-visual/02-choose-colors` | Develop brand color palette |
| `/claude-vibes:00-BRAND/03-visual/03-select-typography` | Develop typography system |

#### Compile phase
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

### 01-START (discovery and planning)

Plan before you build. Discover the problem, scope the MVP, design the foundation, and write the roadmap that the rest of the project follows. The roadmap lives in `docs/01-START/roadmap.md` in your project, so you can read it, edit it, and keep it in git.

**Commands:**
| Command | Description |
|---------|-------------|
| `/claude-vibes:01-START/01-discover` | Understand the problem space and user needs |
| `/claude-vibes:01-START/02-scope` | Define MVP boundaries and prioritize features |
| `/claude-vibes:01-START/03-architect` | Plan technical approach and system design |
| `/claude-vibes:01-START/04-plan-roadmap` | Scope the whole project with `graph-engineering` and save the approved graph as the roadmap |
| `/claude-vibes:01-START/05-track-progress` | See where the project stands, move the next task forward, and change the roadmap on purpose |

**Agents:**
- `market-validator` - Research market viability and competition
- `feature-brainstormer` - Generate and prioritize feature ideas
- `tech-advisor` - Recommend technology choices
- `plan-reviewer` - Review and improve implementation plans
- `data-modeler` - Design data structures and schemas

#### How planning and tracking work

1. **Run the first three START commands.** They produce plain-language documents on the problem, what is in and out of scope, and the technical foundation.
2. **Run `04-plan-roadmap`.** It hands all of that to the `graph-engineering` skill, which first confirms an alignment contract with you (the objective, what done means, what to optimize for, what is out of scope, and which decisions stay yours), then designs the work as jobs. Each job has one owner and one checkable output. Reviews are separate jobs, so no job grades its own work, and an approval point sits in front of anything expensive or hard to undo. The skill only designs. Nothing runs until you approve the graph.
3. **The approved graph becomes `docs/01-START/roadmap.md`**, a file in your project that you can read and keep in git. One line per task:

   ```
   - [ ] 2.1 Build checkout | type: build | how: 01-plan-code, then 02-write-code | depends on: 1.4 | done when: a test card payment succeeds
   - [ ] 2.2 Review checkout | type: check | how: 03-review-code | depends on: 2.1 | done when: review passes with no blockers
   - [ ] 2.3 Open the Stripe account | type: setup | how: you, by hand | gate: your approval before starting | done when: live keys are saved
   ```

4. **Work from the roadmap.** `05-track-progress` shows where things stand and moves the next task forward, whatever its type. For code, `01-plan-code` picks the next build task and `02-write-code` ticks it off once its done-when line is true.
5. **Change course on purpose.** Ask for something that is not on the roadmap and the command stops to ask where it belongs: a phase, the "Later" list, or "Not doing". A change to the objective itself sends you back to `04-plan-roadmap` to approve a new graph.

You can use the skill by itself for any multi-step piece of work, not only a software project. Run `/claude-vibes:graph-engineering` and describe the objective.

---

### TOOLKIT (specialized tools)

Commands and agents for work outside the development workflow: research, copy, scripts, and image prompts.

**Commands:**
| Command | Description |
|---------|-------------|
| `/claude-vibes:TOOLKIT/midjourney-prompt` | Craft Midjourney prompts through guided discovery (covers V8.2, V8.1, V7, and Niji 7) |
| `/claude-vibes:TOOLKIT/nano-banana-prompt` | Craft prompts for Nano Banana Pro image generation |
| `/claude-vibes:TOOLKIT/research` | Deep research on any topic |
| `/claude-vibes:TOOLKIT/research-brand` | Research a brand for sponsored content |
| `/claude-vibes:TOOLKIT/scale-business` | Strategic business growth consultation with prioritized opportunities |
| `/claude-vibes:TOOLKIT/write` | Write emails, messages, notes naturally |
| `/claude-vibes:TOOLKIT/write-copy` | Write marketing copy for a page, ad, or email |
| `/claude-vibes:TOOLKIT/write-sponsor-script` | Write scripts for sponsored/affiliate content |

**Agents:**
- `brand-researcher` - Deep brand research for content creators
- `business-growth-advisor` - Strategic business growth consultation
- `deep-researcher` - Research a topic in depth and report what experts actually do
- `elite-copywriter` - Write or rewrite marketing copy
- `hook-generator` - Write several opening hooks for a video
- `nano-banana-pro-expert` - Guidance for Nano Banana Pro image generation
- `sponsor-script-writer` - Write scripts for sponsored and affiliate videos

---

### 02-BUILD (implementation)

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

### 03-SHIP (deployment)

Check, commit, push, and open a pull request. The commit command confirms its message with you first, and nothing force-pushes without your approval.

**Commands:**
| Command | Description |
|---------|-------------|
| `/claude-vibes:03-SHIP/01-pre-commit` | Check uncommitted changes before shipping |
| `/claude-vibes:03-SHIP/02-commit` | Commit with a generated, descriptive message |
| `/claude-vibes:03-SHIP/03-push` | Commit and push to the remote branch |
| `/claude-vibes:03-SHIP/04-pr` | Commit, push, and open a pull request |

---

### 04-DEBUG (debugging)

Fix bugs systematically. Diagnose root causes, apply fixes, and verify they work.

**Commands:**
| Command | Description |
|---------|-------------|
| `/claude-vibes:04-DEBUG/01-diagnose-issue` | Investigate and identify root cause |
| `/claude-vibes:04-DEBUG/02-fix-issue` | Apply the fix with minimal changes |
| `/claude-vibes:04-DEBUG/03-verify-fix` | Verify the fix and record it in `LOGS.json` |

**Agents:**
- `diagnostician` - Deep investigation and root cause analysis
- `fixer` - Minimal, targeted bug fixes
- `verifier` - Verification and regression testing
- `tester` - Write and run tests to prove fixes work

---

### 05-REFACTOR (improving existing code)

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

## Skills

Skills are knowledge packs that Claude loads on its own when a conversation calls for them, in any conversation once the plugin is installed. The commands and agents above rely on them. You can also run one directly, which is how you would normally start the two thinking tools: `/claude-vibes:interview-me` and `/claude-vibes:graph-engineering`.

| Area | Skills |
|------|--------|
| **Brand strategy** | `golden-circle-purpose`, `brand-values-development`, `brand-positioning-theory`, `brand-archetype-selection`, `jtbd-psychographic-research`, `competitive-visual-audit` |
| **Brand expression** | `brand-naming-strategies`, `brand-voice-development`, `brand-messaging-architecture`, `tagline-creation-strategies`, `elevator-pitch-techniques` |
| **Visual identity** | `visual-identity-direction`, `brand-color-psychology`, `brand-typography-systems` |
| **Content & copy** | `natural-writing`, `scriptwriting-methodology`, `conversion-psychology`, `platform-optimization`, `midjourney-prompting` |
| **Thinking tools** | `interview-me` (get interviewed until a topic is fully understood), `graph-engineering` (design a multi-step AI work graph with checks and human gates before running anything) |

`platform-optimization` and `midjourney-prompting` describe fast-moving targets. Each carries a last-verified date and tells Claude to check current sources before relying on specific numbers.

**Building your own skills, agents, hooks, or plugins?** Version 1 shipped builder skills for that. Anthropic now maintains better ones alongside the product, so install those instead: `/plugin install plugin-dev@claude-plugins-official` and `/plugin install skill-creator@claude-plugins-official`. Claude Code adds that marketplace automatically. If it reports the marketplace as not found, run `/plugin marketplace add anthropics/claude-plugins-official` first.

---

## MCP servers

MCP (Model Context Protocol) servers give Claude Code extra tools. The plugin installs two that need no setup.

### Installed automatically

These servers start automatically when the plugin is enabled:

| Server | Purpose | Official Source |
|--------|---------|-----------------|
| **Context7** | Up-to-date documentation in prompts | [github.com/upstash/context7](https://github.com/upstash/context7) |
| **Whois** | Domain/IP lookup | [@mcp-server/whois-mcp](https://www.npmjs.com/package/@mcp-server/whois-mcp) |

Notes:
- Add `use context7` to a prompt to pull current library documentation. Context7 is a hosted service, so those lookups leave your machine.
- Whois runs locally through `npx`, pinned to an exact version.
- Project tracking needs no server. The roadmap is a file in your project that the commands keep up to date.
- Cross-session learning uses Claude Code's native agent memory, stored in `.claude/agent-memory/` in your project, so there is no memory server. Commit that folder to share it with your team, or add it to `.gitignore` to keep it private.

### Optional servers (setup required)

None of these are needed by the plugin. They are the ones that pair well with it, and each asks you to sign in the first time you use it (run `/mcp` inside Claude Code). All use the HTTP transport, since Claude Code has deprecated SSE.

| Server | Purpose | Install |
|--------|---------|---------|
| **GitHub** | Pull requests and issues | `claude mcp add --transport http github https://api.githubcopilot.com/mcp/ --header "Authorization: Bearer YOUR_GITHUB_PAT"` |
| **Linear** | Issue tracking | `claude mcp add --transport http linear https://mcp.linear.app/mcp` |
| **Sentry** | Error tracking | `claude mcp add --transport http sentry https://mcp.sentry.dev/mcp` |
| **Supabase** | Database and backend | `claude mcp add --transport http supabase https://mcp.supabase.com/mcp` |
| **Vercel** | Hosting and deployments | `claude mcp add --transport http vercel https://mcp.vercel.com` |
| **Cloudflare** | Edge deployment | `claude mcp add --transport http cloudflare https://mcp.cloudflare.com/mcp` |
| **Playwright** | Browser automation (local) | `claude mcp add playwright -- npx @playwright/mcp@latest` |

Vendors change these endpoints, so if one fails, check the vendor's MCP page or the [Claude Code MCP guide](https://code.claude.com/docs/en/mcp).

### Keep the list short

Every MCP server adds to Claude Code's startup time, so add one only when you need it.

---

## Structure

```
claude-vibes/
├── .claude-plugin/
│   └── marketplace.json         # Marketplace manifest
├── .github/                     # CI workflow, issue and PR templates
├── scripts/
│   └── validate_plugin.py       # Checks frontmatter, references, links, and counts
├── CHANGELOG.md
├── CONTRIBUTING.md
├── SECURITY.md
├── CLAUDE.md                    # The vibe coding framework this repo is built with
└── plugins/
    └── vibes/                   # The plugin
        ├── .claude-plugin/
        │   └── plugin.json      # Plugin manifest, including MCP servers
        ├── commands/
        │   ├── 00-BRAND/        # Brand identity
        │   ├── 01-START/        # Discovery and planning
        │   ├── 02-BUILD/        # Implementation
        │   ├── 03-SHIP/         # Commit, push, pull request
        │   ├── 04-DEBUG/        # Debugging
        │   ├── 05-REFACTOR/     # Improving existing code
        │   └── TOOLKIT/         # Research, copy, scripts, image prompts
        ├── agents/
        │   ├── BRANDING/
        │   ├── CODING/
        │   └── TOOLKIT/
        └── skills/              # 21 knowledge skills
```

---

## Contributing, security, and license

See [CONTRIBUTING.md](CONTRIBUTING.md) before opening a pull request, and [CHANGELOG.md](CHANGELOG.md) for what changed in each release. Report vulnerabilities privately as described in [SECURITY.md](SECURITY.md). If a skill teaches something that is out of date, open an issue with the "Outdated or wrong content" form. Released under the [MIT License](LICENSE).

---

## References

- [Plugins](https://code.claude.com/docs/en/plugins) and the [plugins reference](https://code.claude.com/docs/en/plugins-reference)
- [Skills and custom commands](https://code.claude.com/docs/en/skills), which are now one system
- [Subagents](https://code.claude.com/docs/en/sub-agents)
- [MCP in Claude Code](https://code.claude.com/docs/en/mcp)
- [Claude Code overview](https://code.claude.com/docs/en/overview) and [best practices](https://code.claude.com/docs/en/best-practices)
