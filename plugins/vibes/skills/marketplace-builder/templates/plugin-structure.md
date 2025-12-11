# Plugin Structure Template

Complete guide to creating a well-structured Claude Code plugin.

---

## Plugin Anatomy

A plugin is a packaged collection of Claude Code components:

```
plugin-name/
├── .claude-plugin/
│   └── plugin.json         # Required: Plugin manifest
├── commands/               # Optional: Slash commands
│   ├── command-a.md
│   └── subdir/
│       └── command-b.md
├── agents/                 # Optional: Subagents
│   └── agent-name.md
├── skills/                 # Optional: Skills
│   └── skill-name/
│       └── SKILL.md
├── hooks/                  # Optional: Event handlers
│   └── hooks.json
├── .mcp.json              # Optional: MCP servers
└── README.md              # Recommended: Documentation
```

---

## plugin.json Schema

### Required Fields

```json
{
  "name": "plugin-name",
  "description": "Clear description of what this plugin provides",
  "version": "1.0.0"
}
```

### Full Schema

```json
{
  "name": "plugin-name",
  "description": "Clear description of what this plugin provides",
  "version": "1.0.0",
  "author": {
    "name": "Author Name",
    "email": "author@example.com",
    "url": "https://author-website.com"
  },
  "homepage": "https://plugin-docs.example.com",
  "repository": "https://github.com/owner/plugin-repo",
  "license": "MIT",
  "keywords": ["claude-code", "productivity", "development"]
}
```

### Field Details

| Field | Required | Description |
|-------|----------|-------------|
| `name` | Yes | Unique identifier, `kebab-case` |
| `description` | Yes | What the plugin does (shown in /plugin browser) |
| `version` | Yes | Semantic version `MAJOR.MINOR.PATCH` |
| `author` | No | Author info (name required if present) |
| `homepage` | No | Documentation URL |
| `repository` | No | Source code URL |
| `license` | No | License identifier (MIT, Apache-2.0, etc.) |
| `keywords` | No | Discovery keywords |

---

## Component Types

### Commands (Slash Commands)

Location: `commands/` directory

```
commands/
├── simple-command.md       # /simple-command
├── another.md              # /another
└── git/                    # Subdirectory for organization
    ├── commit.md           # /commit (git)
    └── status.md           # /status (git)
```

**Command file structure**:
```markdown
---
description: What this command does (shown in /help)
allowed-tools: Read, Grep, Bash(git:*)
argument-hint: [arg1] [arg2]
---

Your command instructions here.

Use $ARGUMENTS for all arguments or $1, $2, $3 for positional.
```

### Agents (Subagents)

Location: `agents/` directory

```
agents/
├── code-reviewer.md
├── debugger.md
└── helper.md
```

**Agent file structure**:
```markdown
---
name: agent-name
description: What this agent does and when to invoke it. Triggers: "review code", "find bugs"
tools: Read, Grep, Glob, Bash(git diff:*)
model: inherit
---

You are [role description].

## When Invoked

1. First step
2. Second step
3. Third step

## Output Format

[Describe expected output structure]
```

### Skills

Location: `skills/` directory with subdirectory per skill

```
skills/
└── code-analysis/
    ├── SKILL.md            # Main skill file
    ├── reference.md        # Optional: detailed docs
    └── examples.md         # Optional: examples
```

**SKILL.md structure**:
```markdown
---
name: skill-name
description: What this skill does. Use when [scenario]. Triggers: "trigger1", "trigger2"
---

# Skill Name

## Instructions

[Detailed instructions for Claude]

## Examples

[Usage examples]
```

### Hooks

Location: `hooks/hooks.json`

```json
{
  "hooks": [
    {
      "matcher": {
        "event": "pre-tool-use",
        "tool": "Write"
      },
      "hooks": [
        {
          "type": "command",
          "command": "echo 'Writing file: $TOOL_INPUT'"
        }
      ]
    }
  ]
}
```

**Hook events**:
- `pre-tool-use` - Before a tool runs
- `post-tool-use` - After a tool completes
- `notification` - On notifications
- `stop` - When Claude stops

### MCP Servers

Location: `.mcp.json` in plugin root

```json
{
  "mcpServers": {
    "server-name": {
      "command": "node",
      "args": ["${CLAUDE_PLUGIN_ROOT}/server/index.js"],
      "env": {
        "API_KEY": "${API_KEY}"
      }
    }
  }
}
```

**Special variables**:
- `${CLAUDE_PLUGIN_ROOT}` - Plugin installation directory
- `${ENV_VAR}` - Environment variable

---

## Complete Plugin Example

### Directory Structure

```
code-quality-tools/
├── .claude-plugin/
│   └── plugin.json
├── commands/
│   ├── lint.md
│   ├── format.md
│   └── analyze.md
├── agents/
│   ├── code-reviewer.md
│   └── security-scanner.md
├── skills/
│   └── code-patterns/
│       └── SKILL.md
├── hooks/
│   └── hooks.json
└── README.md
```

### .claude-plugin/plugin.json

```json
{
  "name": "code-quality-tools",
  "description": "Comprehensive code quality tools: linting, formatting, analysis, review, and security scanning",
  "version": "1.2.0",
  "author": {
    "name": "Quality Team",
    "email": "quality@company.com"
  },
  "repository": "https://github.com/company/code-quality-tools",
  "license": "MIT",
  "keywords": ["code-quality", "linting", "security", "review"]
}
```

### commands/lint.md

```markdown
---
description: Run linting checks on current project
allowed-tools: Bash(npm:*, npx:*), Read, Glob
---

Run linting checks on this project.

## Steps

1. Detect the project type (package.json, pyproject.toml, etc.)
2. Run appropriate linter:
   - JavaScript/TypeScript: `npx eslint .`
   - Python: `ruff check .`
   - Go: `golint ./...`
3. Parse output and summarize issues by severity
4. Suggest fixes for common issues

## Output Format

### Lint Results

**Total Issues**: X errors, Y warnings

#### Errors (Must Fix)
| File | Line | Issue |
|------|------|-------|
| ... | ... | ... |

#### Warnings (Should Fix)
| File | Line | Issue |
|------|------|-------|
| ... | ... | ... |

### Suggested Fixes
[Auto-fixable issues and commands to run]
```

### commands/format.md

```markdown
---
description: Format code files in the project
allowed-tools: Bash(npx:*, prettier:*, black:*), Read, Write
argument-hint: [file-or-directory]
---

Format code files: $ARGUMENTS

If no path specified, format the entire project.

## Steps

1. Detect project type and formatter
2. Run formatter:
   - JS/TS: `npx prettier --write [path]`
   - Python: `black [path]`
3. Report what was changed

## Output

List files that were modified with a summary of changes.
```

### agents/code-reviewer.md

```markdown
---
name: code-reviewer
description: Expert code reviewer for pull requests and changes. Use PROACTIVELY after code changes or when reviewing PRs. Triggers: "review code", "check my changes", "PR review"
tools: Read, Grep, Glob, Bash(git diff:*, git log:*, git show:*)
model: inherit
---

You are a senior code reviewer with expertise in software engineering best practices.

## When Invoked

1. Get the changes to review:
   - If PR number provided, fetch PR diff
   - Otherwise, use `git diff HEAD` for uncommitted changes
2. Analyze each file systematically
3. Check for:
   - Code correctness and logic errors
   - Security vulnerabilities
   - Performance issues
   - Code style and readability
   - Test coverage
4. Provide actionable feedback

## Review Checklist

- [ ] Logic is correct
- [ ] No obvious bugs
- [ ] Error handling is appropriate
- [ ] No security vulnerabilities
- [ ] Code is readable and maintainable
- [ ] Tests are adequate
- [ ] No hardcoded secrets
- [ ] Performance is acceptable

## Output Format

### Review Summary

**Overall**: [APPROVE / REQUEST_CHANGES / COMMENT]

**Risk Level**: [Low / Medium / High]

### Issues Found

#### Critical (Must Fix)
- [File:Line] - [Issue description]

#### Important (Should Fix)
- [File:Line] - [Issue description]

#### Suggestions (Nice to Have)
- [File:Line] - [Suggestion]

### Positive Notes
- [What was done well]
```

### agents/security-scanner.md

```markdown
---
name: security-scanner
description: Security vulnerability scanner. Use when checking for security issues, auditing code, or before deployment. Triggers: "security scan", "find vulnerabilities", "security audit"
tools: Read, Grep, Glob, Bash(npm audit:*, pip-audit:*)
model: sonnet
---

You are a security expert specializing in application security.

## When Invoked

1. Identify the project type and technologies
2. Check for common vulnerabilities:
   - Dependency vulnerabilities (`npm audit`, `pip-audit`)
   - Hardcoded secrets and credentials
   - SQL injection patterns
   - XSS vulnerabilities
   - Insecure configurations
3. Scan for OWASP Top 10 issues
4. Report findings with severity and remediation

## Security Checks

### Secrets Detection
- API keys
- Passwords
- Private keys
- Connection strings

### Dependency Audit
- Known CVEs
- Outdated packages
- Unmaintained dependencies

### Code Patterns
- SQL injection
- Command injection
- XSS (Cross-Site Scripting)
- CSRF vulnerabilities
- Insecure deserialization

## Output Format

### Security Scan Results

**Scan Date**: [Date]
**Risk Score**: [0-100]

### Critical Vulnerabilities
| Severity | Location | Issue | Remediation |
|----------|----------|-------|-------------|
| CRITICAL | file:line | ... | ... |

### High Vulnerabilities
...

### Medium Vulnerabilities
...

### Recommendations
1. [Priority action items]
```

### skills/code-patterns/SKILL.md

```markdown
---
name: code-patterns
description: Recognizes and suggests code patterns and best practices. Use when discussing code architecture, design patterns, or refactoring. Triggers: "pattern", "best practice", "refactor", "design"
---

# Code Patterns Knowledge

## Design Patterns

### Creational
- **Singleton**: Single instance, global access
- **Factory**: Object creation abstraction
- **Builder**: Complex object construction

### Structural
- **Adapter**: Interface compatibility
- **Decorator**: Dynamic behavior extension
- **Facade**: Simplified interface

### Behavioral
- **Observer**: Event subscription
- **Strategy**: Interchangeable algorithms
- **Command**: Encapsulated operations

## Anti-Patterns to Avoid

- God Object: Too many responsibilities
- Spaghetti Code: Tangled control flow
- Copy-Paste Programming: Duplicated code
- Magic Numbers: Unexplained literals

## Refactoring Patterns

- Extract Method
- Move Field
- Replace Conditional with Polymorphism
- Introduce Parameter Object
```

### hooks/hooks.json

```json
{
  "hooks": [
    {
      "matcher": {
        "event": "pre-tool-use",
        "tool": "Write"
      },
      "hooks": [
        {
          "type": "command",
          "command": "echo '📝 Writing: '$(echo $TOOL_INPUT | jq -r '.file_path')"
        }
      ]
    },
    {
      "matcher": {
        "event": "notification",
        "pattern": ".*error.*"
      },
      "hooks": [
        {
          "type": "command",
          "command": "echo '⚠️ Error detected in output'"
        }
      ]
    }
  ]
}
```

---

## Plugin Development Best Practices

### 1. Single Responsibility
Each command/agent should do one thing well.

### 2. Clear Descriptions
Descriptions appear in `/plugin` browser and `/help`. Make them count.

### 3. Sensible Defaults
Commands should work without arguments when possible.

### 4. Tool Restrictions
Use `allowed-tools` to limit what commands can do (security).

### 5. Consistent Output
Use consistent output formats across commands.

### 6. Documentation
Include README.md with:
- What the plugin provides
- Installation instructions
- Usage examples
- Configuration options

### 7. Versioning
- Follow semantic versioning
- Document changes in CHANGELOG.md
- Tag releases in git

### 8. Testing
Before publishing:
- Test each command manually
- Verify agents invoke correctly
- Check skills activate on triggers
- Test hooks fire appropriately
