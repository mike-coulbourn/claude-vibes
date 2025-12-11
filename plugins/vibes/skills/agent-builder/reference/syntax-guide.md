# Agent Syntax Guide

Complete reference for agent configuration syntax.

---

## File Structure

Agents are Markdown files with YAML frontmatter:

```markdown
---
name: agent-name
description: What it does and when to use it
tools: Tool1, Tool2
model: sonnet
permissionMode: default
skills: skill1, skill2
---

System prompt content here.
This can be multiple paragraphs with Markdown formatting.

## Sections
Organized content for the agent.
```

---

## File Locations

### Project Scope (Team)
```
.claude/agents/agent-name.md
```
- Committed to git
- Shared with team
- Project-specific

### Personal Scope (Individual)
```
~/.claude/agents/agent-name.md
```
- Your private agents
- Available in all projects
- Not version controlled

### Precedence
If same name exists in both:
- Project agents take precedence over personal

---

## YAML Frontmatter Fields

### Required Fields

#### `name`
Unique identifier for the agent.

**Rules**:
- Lowercase letters only
- Hyphens allowed (no underscores)
- No spaces
- Maximum 64 characters
- Must be unique

**Valid**:
```yaml
name: code-reviewer
name: security-auditor
name: pr-helper
name: my-custom-agent
```

**Invalid**:
```yaml
name: Code_Reviewer    # No uppercase, no underscores
name: code reviewer    # No spaces
name: code.reviewer    # No dots
```

#### `description`
Natural language description determining when Claude invokes this agent.

**Formula**: `[Role/Expertise] + [What it does] + [When to invoke] + [Trigger terms]`

**Characteristics**:
- Critical for auto-discovery
- Should be specific, not vague
- Include action verbs
- Include trigger terms users would say
- 50-200 words recommended

**Good Example**:
```yaml
description: Senior code reviewer specializing in security and quality. Reviews code changes for vulnerabilities, best practices, and maintainability. Use PROACTIVELY after code changes, when reviewing PRs, or when user mentions code review, pull request review, security audit, or check my code.
```

**Bad Example**:
```yaml
description: Helps with code
```

### Optional Fields

#### `tools`
Comma-separated list of allowed tools.

**If omitted**: Agent inherits all tools from parent.

**Available Tools**:
| Tool | Purpose |
|------|---------|
| `Read` | Read file contents |
| `Write` | Create new files |
| `Edit` | Modify existing files |
| `Grep` | Search file contents |
| `Glob` | Find files by pattern |
| `Bash` | Execute shell commands |
| `WebSearch` | Search the web |
| `WebFetch` | Fetch web page content |

**Syntax**:
```yaml
# Multiple tools
tools: Read, Grep, Glob

# With file modification
tools: Read, Write, Edit, Grep, Glob

# With bash
tools: Read, Bash, Grep, Glob
```

**Granular Bash Patterns**:
```yaml
# Any git command
tools: Bash(git:*)

# Specific git commands
tools: Bash(git diff:*), Bash(git log:*), Bash(git status:*)

# npm commands
tools: Bash(npm:*)

# Specific npm commands
tools: Bash(npm test:*), Bash(npm run:*)

# Multiple patterns
tools: Read, Grep, Glob, Bash(git:*), Bash(npm test:*)
```

#### `model`
Which Claude model to use.

**Options**:
| Value | Description |
|-------|-------------|
| `haiku` | Fastest, cheapest, good for simple tasks |
| `sonnet` | Balanced (default if omitted) |
| `opus` | Most capable, best for complex tasks |
| `inherit` | Use main conversation's model |

**Syntax**:
```yaml
model: haiku    # Fast, simple tasks
model: sonnet   # Balanced (default)
model: opus     # Complex analysis
model: inherit  # Match user's model
```

#### `permissionMode`
How the agent handles permission requests.

**Options**:
| Value | Behavior |
|-------|----------|
| `default` | Standard permission prompts |
| `acceptEdits` | Auto-accept file edits |
| `bypassPermissions` | No permission checks |
| `plan` | Read-only, no execution |

**Syntax**:
```yaml
permissionMode: default          # Safe default
permissionMode: acceptEdits      # Trust file edits
permissionMode: bypassPermissions # CI/CD automation
permissionMode: plan             # Analysis only
```

**Security Notes**:
- `default`: Safest, recommended for most
- `acceptEdits`: Only for trusted automation (formatters, linters)
- `bypassPermissions`: Only for controlled environments (CI/CD)
- `plan`: Safest for research/analysis

#### `skills`
Skills to auto-load when agent starts.

**Syntax**:
```yaml
skills: skill-name
skills: skill1, skill2, skill3
```

---

## System Prompt (Body)

Everything after the YAML closing `---` is the system prompt.

### Markdown Support
Full Markdown is supported:
- Headers (`#`, `##`, `###`)
- Lists (bullet, numbered)
- Code blocks
- Bold, italic
- Tables

### Recommended Structure

```markdown
---
[YAML frontmatter]
---

You are [role description].

## When Invoked
1. [First step]
2. [Second step]
3. [Third step]

## Focus Areas
- [Key area 1]
- [Key area 2]

## Output Format
[How to present results]

## Constraints
- [What NOT to do]
- [Boundaries]
```

### System Prompt Patterns

#### Role Definition
```markdown
You are a senior code reviewer specializing in security.
Your primary focus is identifying vulnerabilities and best practices.
```

#### Workflow Steps
```markdown
## When Invoked
1. Gather context by running `git diff HEAD`
2. Identify changed files and their purpose
3. Review each change against checklist
4. Present findings with severity levels
```

#### Checklist
```markdown
## Review Checklist
- [ ] No SQL injection vulnerabilities
- [ ] Input validation on all boundaries
- [ ] No exposed secrets
- [ ] Proper error handling
```

#### Output Format
```markdown
## Output Format

### Summary
[One-line verdict]

### Issues Found
| Severity | Location | Description |
|----------|----------|-------------|
| [level] | [file:line] | [issue] |

### Recommendations
1. [Priority fix]
2. [Secondary fix]
```

#### Constraints
```markdown
## Constraints
- Do NOT modify code unless explicitly asked
- Do NOT change API contracts
- ALWAYS explain WHY something is an issue
- ALWAYS provide specific line references
```

#### Decision Trees
```markdown
## Decision Flow
If no changes detected:
  → Report "No changes to review"

If only test files changed:
  → Focus on test quality and coverage

If security-sensitive files:
  → Prioritize security review
```

---

## Complete Examples

### Minimal Agent
```markdown
---
name: code-explainer
description: Explains code in plain English. Use when user asks "what does this do" or wants code explained.
---

You are a patient code teacher who explains complex code simply.

## When Invoked
1. Identify the code to explain
2. Break down the logic step by step
3. Explain in plain English with analogies

## Output Format
### Overview
[What this code does]

### Step-by-Step
1. [First part explained]
2. [Second part explained]
```

### Full-Featured Agent
```markdown
---
name: security-auditor
description: Security vulnerability specialist. Scans code for OWASP Top 10 vulnerabilities, exposed secrets, and security anti-patterns. Use when auditing security, checking vulnerabilities, or when user mentions security review, vulnerability scan, or penetration testing.
tools: Read, Grep, Glob
model: opus
permissionMode: plan
---

You are an elite security researcher performing vulnerability assessment.

## When Invoked
1. Identify security-sensitive files
2. Scan for OWASP Top 10 vulnerabilities
3. Check for exposed secrets
4. Report findings with severity and remediation

## OWASP Top 10 Checklist
- [ ] A01: Broken Access Control
- [ ] A02: Cryptographic Failures
- [ ] A03: Injection
...

## Output Format
### Security Audit Report
**Risk Level**: CRITICAL / HIGH / MEDIUM / LOW

### Vulnerabilities
| ID | Type | Location | Severity | Fix |
|----|------|----------|----------|-----|

### Recommendations
1. [Immediate action]
2. [Short-term fix]

## Constraints
- Read-only analysis
- Never expose actual secret values
- Prioritize by exploitability
```

---

## YAML Syntax Rules

### Correct YAML
```yaml
---
name: my-agent
description: Does something useful
tools: Read, Grep, Glob
---
```

### Common YAML Errors

**Missing opening/closing `---`**:
```yaml
# Wrong - missing delimiters
name: my-agent
description: Does something

# Correct
---
name: my-agent
description: Does something
---
```

**Incorrect indentation**:
```yaml
# Wrong - YAML uses spaces, not tabs
name:	my-agent    # Tab character

# Correct
name: my-agent      # Spaces
```

**Missing quotes for special characters**:
```yaml
# Wrong - colon in value
description: Security: Audits code

# Correct
description: "Security: Audits code"
```

**Incorrect list syntax**:
```yaml
# Wrong
tools: [Read Grep Glob]

# Correct (comma-separated string)
tools: Read, Grep, Glob
```

---

## Validation

### Check YAML Syntax
```bash
# Using Python
python3 -c "
import yaml
with open('.claude/agents/my-agent.md') as f:
    content = f.read()
    parts = content.split('---')
    if len(parts) >= 3:
        yaml.safe_load(parts[1])
        print('YAML valid')
"
```

### Check Name Format
```bash
# Name should match pattern: ^[a-z][a-z0-9-]*$
grep -E '^name: [a-z][a-z0-9-]*$' .claude/agents/*.md
```

### Check Description Length
```python
# Description should be 50-500 characters
import yaml
# ... parse and check len(description)
```

---

## Quick Reference Table

| Field | Required | Type | Default |
|-------|----------|------|---------|
| `name` | Yes | String | - |
| `description` | Yes | String | - |
| `tools` | No | Comma-separated | Inherit all |
| `model` | No | Enum | `sonnet` |
| `permissionMode` | No | Enum | `default` |
| `skills` | No | Comma-separated | None |
