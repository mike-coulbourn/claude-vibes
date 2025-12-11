# Claude Code Extensibility Guide

Claude Code has four ways to extend its behavior: **Commands**, **Skills**, **Agents**, and **Hooks**. Each solves a different problem, and knowing when to reach for which one will save you a lot of trial and error.

---

## Table of Contents

1. [Overview](#overview)
2. [Quick Comparison](#quick-comparison)
3. [Commands](#commands)
4. [Skills](#skills)
5. [Agents](#agents)
6. [Hooks](#hooks)
7. [How They Work Together](#how-they-work-together)
8. [Single-Trigger Workflow Example](#single-trigger-workflow-example)
9. [Decision Guide](#decision-guide)

---

## Overview

Claude Code has four extensibility mechanisms, each serving a distinct purpose:

| Mechanism | One-Line Definition |
|-----------|---------------------|
| **Commands** | Shortcuts YOU trigger (`/commit`) |
| **Skills** | Knowledge CLAUDE activates automatically |
| **Agents** | Specialists CLAUDE delegates work to |
| **Hooks** | Guards that ENFORCE rules |

### Simple Analogies

- **Commands** = Remote control buttons (you press, something happens)
- **Skills** = Auto-pilot features (car turns on headlights when dark)
- **Agents** = Delegating to coworkers ("go research this, report back")
- **Hooks** = Security guards (standing at checkpoints, can actually stop things)

---

## Quick Comparison

| Aspect | Commands | Skills | Agents | Hooks |
|--------|----------|--------|--------|-------|
| **Who triggers?** | You (`/name`) | Claude (auto) | Claude (Task tool) | Events (auto) |
| **Same memory?** | Yes | Yes | No (fresh start) | External script |
| **Can block actions?** | No | No | No | **YES** |
| **Best for** | Manual shortcuts | Auto-loaded knowledge | Complex isolated tasks | Enforcement & control |

---

## Commands

Commands are the simplest mechanism - you type `/something` and it expands into a full prompt. Think of them as keyboard shortcuts for your most common requests.

The key thing: **you** control when they fire. Claude doesn't decide to run a command for you.

### Good fits for commands

- Stuff you do repeatedly: `/commit`, `/review`, `/test`
- Anything needing arguments: `/fix-issue 123`, `/deploy staging`
- Multi-step workflows you want to trigger manually
- Prompts you've refined over time and don't want to retype

### File Structure

```
.claude/commands/          # Project commands (shared via git)
~/.claude/commands/        # Personal commands (only you)
```

Each command is a single `.md` file.

### Basic Example

**`.claude/commands/optimize.md`**
```markdown
Analyze this code for performance issues and suggest three specific optimizations.
```

**Usage:** `/optimize`

### Command with Arguments

**`.claude/commands/fix-issue.md`**
```markdown
---
argument-hint: [issue-number]
description: Fix a GitHub issue by number
---

Fix issue #$1. Follow these steps:
1. Understand the issue
2. Locate relevant code
3. Implement solution
4. Add tests
```

**Usage:** `/fix-issue 123`

### Command with Dynamic Features

**`.claude/commands/commit.md`**
```markdown
---
allowed-tools: Bash(git:*)
description: Create a git commit with context
---

## Context
- Current changes: !`git diff HEAD`
- Current branch: !`git branch --show-current`
- Recent commits: !`git log --oneline -5`

## Standards
Review @CLAUDE.md for commit message format.

## Task
Create a commit with message: $ARGUMENTS
```

**Usage:** `/commit feat: add user authentication`

### Dynamic Features Reference

| Feature | Syntax | Purpose |
|---------|--------|---------|
| Arguments (free-form) | `$ARGUMENTS` | Everything after command name |
| Arguments (positional) | `$1`, `$2`, `$3` | Space-separated arguments |
| Bash execution | `!`command`` | Run shell command, inject output |
| File references | `@path/to/file` | Include file contents |
| Tool restrictions | `allowed-tools:` frontmatter | Limit available tools |

---

## Skills

Here's where it gets interesting. Skills activate automatically based on what you're talking about. You mention "PDF" and suddenly Claude knows how to extract tables from documents - without you typing any command.

The magic (and the frustration) is in the **description matching**. Claude reads skill descriptions to decide what's relevant. Vague descriptions mean skills never activate. More on this below.

### When skills make sense

- Knowledge Claude should "just have" when the topic comes up
- Team standards that should apply without anyone remembering to invoke them
- Complex capabilities with supporting files (templates, scripts, reference docs)
- Workflows that need context from multiple files in a skill directory

### File Structure

```
.claude/skills/skill-name/     # Project skills (shared via git)
~/.claude/skills/skill-name/   # Personal skills (only you)
```

Each skill is a **directory** with at least a `SKILL.md` file.

### Basic Structure

```
skill-name/
├── SKILL.md              # Required: main instructions
├── templates/            # Optional: reusable templates
├── examples/             # Optional: example code/usage
└── reference/            # Optional: detailed documentation
```

### SKILL.md Format

```markdown
---
name: security-standards
description: Apply security best practices when writing authentication,
  passwords, or API code. Use when discussing security, auth, or passwords.
---

# Security Standards

## Password Handling
- Always hash with bcrypt (cost factor 12)
- Never store plaintext passwords
- Use secure random tokens for resets

## API Security
- Validate all inputs
- Use parameterized queries
- Implement rate limiting

[... more instructions ...]
```

### How discovery actually works

This trips up everyone at first. Here's the flow:

1. You say something like "help me add password reset"
2. Claude scans all skill descriptions looking for keyword overlap
3. `security-standards` description mentions "passwords" - match
4. That skill's instructions load into context

**The gotcha:** Your description isn't for humans - it's for Claude's matching algorithm. Write it like you're stuffing keywords into a search engine. List every term someone might use when they need this skill.

### Good vs bad descriptions

| Bad (won't activate) | Good (will activate) |
|----------------------|----------------------|
| "Helps with security" | "Apply security best practices when writing authentication, passwords, or API code. Use when discussing security, auth, passwords, or tokens." |
| "PDF helper" | "Extract text and tables from PDF files, fill PDF forms, merge documents. Use when working with PDFs or when user mentions PDF, forms, or document extraction." |

---

## Agents

Agents are the weird one. They're like skills, but they run in a completely separate conversation - fresh memory, no context from what you've been discussing.

Why would you want that? Two reasons:

1. **Unbiased review**: An agent doing security review hasn't been "primed" by your earlier debugging. It sees the code with fresh eyes.
2. **Complex isolated work**: You want deep analysis without cluttering your main conversation with 50 messages about edge cases.

The tradeoff is real: agents need everything re-explained. If you've been debugging for 20 minutes and launch an agent, it knows nothing about what you've tried.

### File Structure

```
.claude/agents/            # Project agents (shared via git)
~/.claude/agents/          # Personal agents (only you)
```

Each agent is a single `.md` file.

### Basic Agent

**`.claude/agents/security-reviewer.md`**
```markdown
---
name: security-reviewer
description: Deep security analysis. Use after writing security-sensitive code.
tools: Read, Grep, Glob, Bash(git diff:*)
---

You are a senior security engineer performing a code audit.

## When Invoked
1. Run `git diff HEAD` to see recent changes
2. Identify security-sensitive code (auth, input handling, data access)
3. Check for OWASP Top 10 vulnerabilities
4. Report findings with severity and remediation

## Focus Areas
- Authentication and authorization
- Input validation and sanitization
- SQL injection and XSS
- Secrets and credential handling
- Access control

## Output Format
Return a structured report:
- Critical issues (must fix)
- Warnings (should fix)
- Suggestions (nice to have)
```

### Fresh context: the double-edged sword

I mentioned this above but it's worth a table to really drive it home:

| Scenario | Skill (shared context) | Agent (fresh context) |
|----------|------------------------|----------------------|
| Debugging for 20 minutes | Has full history | Knows nothing - you'll repeat yourself |
| Code review after implementation | Might be "anchored" to your approach | Clean slate, might catch things you're blind to |
| Quick question | Fast, uses existing context | Overkill - launches a whole new session |

### YAML Fields Reference

| Field | Required | Purpose |
|-------|----------|---------|
| `name` | Yes | Identifier for the agent |
| `description` | Yes | When to use (enables discovery) |
| `tools` | No | Restrict available tools |
| `model` | No | `haiku`, `sonnet`, `opus`, or `inherit` |
| `allowedTools` | No | Alternative to `tools` |

### Launching Agents

Claude launches agents via the **Task tool**:

```
Task tool invocation:
  subagent_type: "security-reviewer"
  prompt: "Review the authentication code in src/auth/"
```

You can also instruct Claude to launch agents in command prompts or skill instructions.

---

## Hooks

Hooks are fundamentally different from the other three. Commands, skills, and agents are all "guidance" - Claude can technically ignore them (even if it usually doesn't). Hooks are **enforcement**. They're external scripts that can actually block Claude from doing something.

When Claude tries to write a file, a hook can say "nope" and the write doesn't happen. No amount of prompt engineering can override a hook that returns exit code 2.

### When you need hooks

- Blocking dangerous operations (never write to `.env`, never push to main)
- Auto-formatting after every file save
- Audit logging everything Claude does
- Injecting context into prompts before Claude sees them
- Anything where "Claude should know not to do this" isn't good enough

### The real difference

| Commands, Skills, Agents | Hooks |
|--------------------------|-------|
| Guidance - Claude usually follows | Enforcement - Claude literally cannot bypass |
| Runs inside Claude's context | Runs as external script |
| Like company policies | Like a locked door |

### Configuration Location

```json
// ~/.claude/settings.json (personal)
// .claude/settings.json (project, committed)
// .claude/settings.local.json (project, not committed)

{
  "hooks": {
    "PreToolUse": [...],
    "PostToolUse": [...],
    "UserPromptSubmit": [...]
  }
}
```

### Hook Events

| Event | When It Fires | Can Block? | Common Use |
|-------|---------------|------------|------------|
| `PreToolUse` | Before Claude uses a tool | Yes | Block dangerous operations |
| `PostToolUse` | After tool completes | No | Format code, log actions |
| `UserPromptSubmit` | When you send a message | Yes | Add context, validate input |
| `Stop` | When Claude wants to stop | No | Force continuation |
| `SessionStart` | Conversation begins | No | Environment setup |
| `SessionEnd` | Conversation ends | No | Cleanup, final logging |

### Basic Hook Structure

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Write|Edit",
        "hooks": [
          {
            "type": "command",
            "command": "/path/to/validator.sh",
            "timeout": 60
          }
        ]
      }
    ]
  }
}
```

### Matcher Patterns

| Pattern | Matches |
|---------|---------|
| `"Write"` | Exactly the Write tool |
| `"Write\|Edit"` | Write OR Edit tools |
| `".*"` or `"*"` | All tools |
| `"Bash(git:*)"` | Only git bash commands |
| `"mcp__memory__.*"` | All MCP memory server tools |

### Exit Codes

| Exit Code | Meaning | Effect |
|-----------|---------|--------|
| `0` | Success | Proceed, parse stdout for modifications |
| `2` | VETO | **BLOCK the action**, show stderr to Claude |
| Other | Error | Non-blocking, log warning |

### Example: Block .env Writes

**`scripts/protect-env.sh`**
```bash
#!/bin/bash
# Receives JSON on stdin with tool_input.file_path

FILE_PATH=$(cat | jq -r '.tool_input.file_path // empty')

if [[ "$FILE_PATH" == *".env" ]] && [[ "$FILE_PATH" != *".env.example" ]]; then
    echo "BLOCKED: Cannot write to .env files. Add secrets manually." >&2
    exit 2
fi

exit 0
```

**`settings.json`**
```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Write|Edit",
        "hooks": [{"type": "command", "command": "./scripts/protect-env.sh"}]
      }
    ]
  }
}
```

### Example: Auto-Format on Save

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Write|Edit",
        "hooks": [
          {
            "type": "command",
            "command": "prettier --write \"$TOOL_INPUT_FILE_PATH\""
          }
        ]
      }
    ]
  }
}
```

### Common hook mistakes

A few things that'll bite you:

1. **Forgetting `chmod +x`** on your script. Claude will report a confusing error.
2. **Not handling missing input**. The `jq -r '... // empty'` pattern saves you when fields are missing.
3. **Blocking too broadly**. A matcher of `".*"` fires on EVERY tool. Start specific.
4. **Slow scripts**. Hooks have timeouts. If your script does network calls, you'll hit them.
5. **Exit code confusion**. Only `2` blocks. Other non-zero codes log warnings but don't prevent the action.

---

## How They Work Together

Here's the mental model that finally made this click for me:

```
┌─────────────────────────────────────────────┐
│           COMMAND (Orchestrator)            │
│  Entry point - user's single trigger        │
│  Contains workflow instructions             │
└─────────────────────────────────────────────┘
                      │
         ┌────────────┴────────────┐
         ▼                         ▼
┌─────────────────┐     ┌─────────────────────┐
│ SKILLS          │     │ AGENTS              │
│ (Knowledge)     │     │ (Delegation)        │
│                 │     │                     │
│ Auto-activate   │     │ Launched for        │
│ when relevant   │     │ complex tasks       │
└─────────────────┘     └─────────────────────┘
         │                         │
         └────────────┬────────────┘
                      ▼
┌─────────────────────────────────────────────┐
│            HOOKS (Enforcement)              │
│  Fire automatically on every action         │
│  Block dangerous operations                 │
│  The guardrails that can't be bypassed      │
└─────────────────────────────────────────────┘
```

### The cascade

A single command can trigger all four mechanisms. This is where it gets powerful:

1. **Command** kicks things off (your entry point)
2. **Skills** auto-activate from keywords in the expanded prompt
3. **Agents** get launched per the command's instructions
4. **Hooks** fire on every single action throughout

---

## Single-Trigger Workflow Example

Let's make this concrete. Here's a `/feature` command that orchestrates all four mechanisms:

**`.claude/commands/feature.md`**
```markdown
---
description: Implement a feature end-to-end with reviews and shipping
allowed-tools: Read, Write, Edit, Bash, Task, Glob, Grep
---

## Context
Project structure: !`find src -type f -name "*.ts" | head -20`
Current branch: !`git branch --show-current`
Coding standards: @CLAUDE.md

## Your Task
Implement this feature following security best practices: $ARGUMENTS

## Workflow
1. Plan the implementation
2. Write the code
3. Launch security-reviewer agent to audit the code
4. Launch code-reviewer agent to check quality
5. Fix any issues found
6. Run tests: npm test
7. If all passes, commit and create PR
```

You type one thing:

```
/feature add user profile photo upload
```

And here's what happens behind the scenes:

#### 1. COMMAND Expands

The `/feature` command expands into a full prompt with:
- Project structure (via `!`find...``)
- Current branch (via `!`git branch``)
- Coding standards (via `@CLAUDE.md`)
- Feature description ("add user profile photo upload")

#### 2. SKILLS Activate

Claude sees "security best practices" + "photo upload" in the prompt:

| Skill | Trigger Words | Knowledge Loaded |
|-------|---------------|------------------|
| `security-standards` | "security best practices" | Auth rules, validation |
| `file-upload-patterns` | "photo upload" | File handling patterns |

#### 3. Claude Implements → HOOKS Fire

As Claude writes each file:

| Action | Hook Event | Result |
|--------|------------|--------|
| Write `upload.ts` | PostToolUse | Prettier formats |
| Write `storage.ts` | PostToolUse | ESLint checks |
| Edit `.env` | PreToolUse | **BLOCKED** |

#### 4. AGENTS Launch

Per command instructions, Claude launches reviewers:

```
┌─────────────────────┐    ┌─────────────────────┐
│ security-reviewer   │    │ code-reviewer       │
│ (parallel)          │    │ (parallel)          │
│                     │    │                     │
│ Checks for vulns    │    │ Checks quality      │
│ Returns: 0 issues   │    │ Returns: 1 issue    │
└─────────────────────┘    └─────────────────────┘
```

#### 5. Test & Ship → HOOKS Validate

| Action | Hook Check | Result |
|--------|------------|--------|
| `git commit -m "feat: ..."` | Commit format? | Valid |
| `git push` | To main? | No (feature branch) |
| `gh pr create` | - | Logged to audit |

### Complete Flow Diagram

```
┌──────────────────────────────────────────────────────────────┐
│  /feature add user profile photo upload                      │
└──────────────────────────────────────────────────────────────┘
                              │
                    ┌─────────▼─────────┐
                    │    COMMAND        │
                    │    expands        │
                    └─────────┬─────────┘
                              │
                    ┌─────────▼─────────┐
                    │    SKILLS         │
                    │    activate       │
                    │    (automatic)    │
                    └─────────┬─────────┘
                              │
        ┌─────────────────────┴─────────────────────┐
        │                                           │
        ▼                                           ▼
┌───────────────┐                         ┌─────────────────┐
│ Claude writes │ ──── HOOKS fire ────▶  │ • Auto-format   │
│ code          │      on every          │ • Block .env    │
│               │      file action       │ • Lint check    │
└───────┬───────┘                         └─────────────────┘
        │
        ▼
┌───────────────────────────────────────────────────┐
│              AGENTS launch (parallel)             │
│  ┌──────────────────┐    ┌──────────────────┐    │
│  │ security-reviewer│    │ code-reviewer    │    │
│  └────────┬─────────┘    └────────┬─────────┘    │
│           └──────────┬───────────┘               │
└──────────────────────┼───────────────────────────┘
                       │
                       ▼
              Claude fixes issues
                       │
        ┌──────────────┴──────────────┐
        │                             │
        ▼                             ▼
┌───────────────┐           ┌─────────────────┐
│ npm test      │           │ HOOKS validate  │
│ git commit    │ ────────▶ │ • commit format │
│ git push      │           │ • branch check  │
│ gh pr create  │           │ • audit log     │
└───────────────┘           └─────────────────┘
                       │
                       ▼
        ┌──────────────────────────────┐
        │  PR #143 ready for review    │
        └──────────────────────────────┘
```

---

## Decision Guide

When you're staring at a new automation idea, run through this:

```
Need to BLOCK or ENFORCE something?
    └── YES → HOOK

Complex task needing fresh, unbiased perspective?
    └── YES → AGENT

Should happen automatically when topic is relevant?
    └── YES → SKILL

Something you trigger manually on demand?
    └── YES → COMMAND
```

### Quick Reference

| I want to... | Use |
|--------------|-----|
| Create a shortcut I type manually | Command |
| Have Claude auto-apply team standards | Skill |
| Get an expert review of complex work | Agent |
| Block writes to sensitive files | Hook |
| Auto-format all saved code | Hook |
| Load security knowledge when discussing auth | Skill |
| Run lint/test/commit in one action | Command |
| Audit log every Claude action | Hook |
| Delegate deep analysis work | Agent |

---

## Where to start

If you're new to all this, here's my suggested order:

1. **Start with a command or two.** Make a `/commit` that writes good commit messages. Make a `/review` that audits your code. Get comfortable with the basics.

2. **Add a skill when you're repeating yourself.** If you keep telling Claude the same context ("we use Tailwind, our API is at /api/v2, always use TypeScript"), put it in a skill.

3. **Try an agent for code review.** Fresh-eyes review is the killer use case. Set up a security reviewer and run it before PRs.

4. **Add hooks last, when you need hard guarantees.** Hooks are powerful but they're also more complex to debug. Only add them when "Claude should know better" isn't cutting it.

The mechanisms work well together, but you don't need all four on day one. Build up as your workflows get more sophisticated.
