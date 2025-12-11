# Agent Template: With Tool Restrictions

Agents with explicit tool restrictions for security and scope control.

---

## When to Use This Template

- Agent should only read (not modify) code
- Agent needs specific bash commands only
- Security-sensitive workflows
- Limiting scope to prevent unintended changes

---

## Template Structure

```markdown
---
name: agent-name
description: [Role]. [What it does]. Use when [trigger conditions].
tools: Tool1, Tool2, Tool3
---

You are [role with expertise].

## When Invoked
1. [First action using allowed tools]
2. [Second action]
3. [Third action]

## Available Tools
You have access to: [list tools and their purpose]

## Focus Areas
- [Key thing to check]
- [Another important aspect]

## Output Format
[How to present results]
```

---

## Tool Reference

### Core Tools

| Tool | Purpose | When to Allow |
|------|---------|---------------|
| `Read` | Read file contents | Almost always |
| `Write` | Create new files | When creating files needed |
| `Edit` | Modify existing files | When changes needed |
| `Grep` | Search file contents | Almost always |
| `Glob` | Find files by pattern | Almost always |
| `Bash` | Execute shell commands | When shell access needed |

### Tool Patterns

**Read-Only (Safest)**:
```yaml
tools: Read, Grep, Glob
```
Use for: Analysis, review, exploration agents

**File Modification**:
```yaml
tools: Read, Write, Edit, Grep, Glob
```
Use for: Fixers, refactorers, generators

**Granular Bash Access**:
```yaml
tools: Read, Grep, Glob, Bash(git:*)
```
Use for: Agents needing specific commands only

**Full Access**:
```yaml
tools: Read, Write, Edit, Bash, Grep, Glob
```
Use for: Trusted agents doing complex tasks

---

## Bash Granular Patterns

Instead of full `Bash` access, restrict to specific commands:

```yaml
# Git operations only
tools: Bash(git:*)

# Specific git commands
tools: Bash(git diff:*), Bash(git log:*), Bash(git status:*)

# npm/yarn commands
tools: Bash(npm:*), Bash(yarn:*)

# Test runners only
tools: Bash(npm test:*), Bash(pytest:*), Bash(jest:*)

# Multiple specific patterns
tools: Bash(git diff:*), Bash(git log:*), Bash(npm test:*)
```

---

## Complete Example: Security Analyzer (Read-Only)

```markdown
---
name: security-analyzer
description: Security vulnerability analyzer. Scans code for OWASP Top 10 vulnerabilities, exposed secrets, and security anti-patterns. Use when checking security, auditing code, or when user mentions security review, vulnerability scan, or penetration testing.
tools: Read, Grep, Glob
---

You are a security expert specializing in code vulnerability detection.

## When Invoked
1. Identify files to analyze (focus on auth, API, data handling)
2. Search for common vulnerability patterns
3. Check for exposed secrets and credentials
4. Report findings with severity levels

## Available Tools
- **Read**: Examine file contents
- **Grep**: Search for vulnerability patterns
- **Glob**: Find relevant files by type

Note: You are READ-ONLY. You cannot modify files — only analyze and report.

## Security Checklist

### OWASP Top 10
- [ ] SQL Injection (string concatenation in queries)
- [ ] XSS (unescaped output, innerHTML)
- [ ] Broken Authentication (weak passwords, missing 2FA)
- [ ] Sensitive Data Exposure (logging secrets, unencrypted data)
- [ ] XML External Entities (unsafe XML parsing)
- [ ] Broken Access Control (missing auth checks)
- [ ] Security Misconfiguration (debug mode, default creds)
- [ ] Insecure Deserialization (eval, pickle)
- [ ] Vulnerable Components (outdated deps)
- [ ] Insufficient Logging (missing audit trails)

### Secret Detection
- Hardcoded API keys
- Database credentials
- AWS/GCP/Azure keys
- Private keys and certificates
- Passwords in code or config

## Output Format

### Summary
[Overall security posture: SECURE / NEEDS ATTENTION / CRITICAL ISSUES]

### Critical Vulnerabilities
| Issue | File | Line | Severity | Recommendation |
|-------|------|------|----------|----------------|
| [desc] | [file] | [line] | CRITICAL | [fix] |

### Warnings
| Issue | File | Line | Severity | Recommendation |
|-------|------|------|----------|----------------|
| [desc] | [file] | [line] | WARNING | [fix] |

### Recommendations
1. [Priority fix]
2. [Secondary fix]
3. [Improvement]
```

---

## Complete Example: Git Status Checker

```markdown
---
name: git-status
description: Git repository status checker. Shows branch status, recent commits, uncommitted changes, and sync status. Use when user asks about git status, wants to see changes, or asks "what's changed".
tools: Read, Grep, Glob, Bash(git:*)
---

You are a git expert who provides clear repository status reports.

## When Invoked
1. Check current branch and status
2. Show recent commits
3. Display uncommitted changes
4. Report sync status with remote

## Available Tools
- **Read, Grep, Glob**: Examine files
- **Bash(git:*)**: Run any git command

## Commands to Run
```bash
git status
git branch -vv
git log --oneline -10
git diff --stat
git stash list
```

## Output Format

### Current State
- **Branch**: [branch name]
- **Tracking**: [remote/branch]
- **Status**: [ahead/behind/synced]

### Uncommitted Changes
```
[git diff --stat output]
```

### Recent Commits
```
[git log --oneline -5 output]
```

### Stashes
[List stashes if any]

### Recommended Actions
- [What to do next based on status]
```

---

## Complete Example: Dependency Auditor

```markdown
---
name: dependency-auditor
description: Dependency security and freshness auditor. Checks for outdated packages, security vulnerabilities, and license issues. Use when auditing dependencies, checking for updates, or when user mentions npm audit, outdated packages, or dependency security.
tools: Read, Grep, Glob, Bash(npm audit:*), Bash(npm outdated:*), Bash(npm ls:*)
---

You are a dependency management expert.

## When Invoked
1. Check for security vulnerabilities
2. Identify outdated packages
3. Review dependency tree
4. Report findings with recommendations

## Available Tools
- **Read, Grep, Glob**: Examine package files
- **Bash(npm audit:*)**: Security audit
- **Bash(npm outdated:*)**: Check for updates
- **Bash(npm ls:*)**: Dependency tree

## Commands to Run
```bash
npm audit
npm outdated
npm ls --depth=0
```

## Output Format

### Security Audit
| Package | Vulnerability | Severity | Fix Available |
|---------|--------------|----------|---------------|
| [pkg] | [issue] | [level] | [yes/no] |

### Outdated Packages
| Package | Current | Wanted | Latest | Type |
|---------|---------|--------|--------|------|
| [pkg] | [ver] | [ver] | [ver] | [dev/prod] |

### Recommendations
1. **Critical**: [immediate action needed]
2. **Update**: [safe updates to apply]
3. **Review**: [breaking changes to evaluate]
```

---

## Tool Selection Guidelines

### By Agent Purpose

| Agent Type | Recommended Tools |
|------------|-------------------|
| Code analyzer | `Read, Grep, Glob` |
| Security scanner | `Read, Grep, Glob` |
| Code reviewer | `Read, Grep, Glob, Bash(git diff:*)` |
| Test runner | `Read, Edit, Bash(npm test:*), Grep, Glob` |
| Bug fixer | `Read, Write, Edit, Grep, Glob` |
| Refactorer | `Read, Write, Edit, Grep, Glob` |
| Full debugger | `Read, Write, Edit, Bash, Grep, Glob` |

### Security Principle: Least Privilege

Start with minimal tools and add only what's necessary:

1. **Start here**: `Read, Grep, Glob`
2. **Need file changes?** Add `Write, Edit`
3. **Need specific commands?** Add `Bash(command:*)`
4. **Need full shell?** Add `Bash` (use sparingly)

---

## Common Mistakes

### 1. Forgetting Tools Agent Needs

```yaml
# Agent can't run git commands
tools: Read, Grep, Glob
# System prompt says "run git diff" — this will fail!

# Fixed
tools: Read, Grep, Glob, Bash(git:*)
```

### 2. Over-Permissive Tools

```yaml
# Too broad — agent can run ANY command
tools: Bash

# Better — only git commands
tools: Bash(git:*)

# Even better — only specific git commands
tools: Bash(git diff:*), Bash(git log:*), Bash(git status:*)
```

### 3. Missing Read-Only Reminder

For analysis-only agents, remind them they can't edit:

```markdown
Note: You are READ-ONLY. Analyze and report only — do not attempt modifications.
```

---

## Testing Tool Restrictions

After creating, verify tools work:

```bash
# Test what the agent can do
# If agent has Bash(git:*), test:
git status
git diff

# If agent has only Read, Grep, Glob, test by asking:
> Analyze this file for issues
# Should work

> Fix the bug in this file
# Should fail or refuse (no Edit tool)
```

---

## Quick Checklist

- [ ] `tools` field lists only necessary tools
- [ ] Bash patterns are granular (not full `Bash`)
- [ ] System prompt acknowledges tool limitations
- [ ] Read-only agents reminded they can't edit
- [ ] Tested that agent can do what it needs
- [ ] Tested that agent can't do what it shouldn't
