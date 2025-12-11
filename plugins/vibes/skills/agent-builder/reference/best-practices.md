# Agent Best Practices

Principles and patterns for creating effective agents.

---

## Core Principles

### 1. Single Responsibility
Each agent should do one thing well.

**Good**:
- `code-reviewer` - reviews code quality
- `security-auditor` - scans for vulnerabilities
- `test-runner` - runs and fixes tests

**Bad**:
- `code-helper` - reviews, fixes, tests, documents (too broad)

**Why**: Focused agents are easier to discover, more reliable, and produce better results.

### 2. Self-Contained Prompts
Agents run in **separate context** — they don't see conversation history.

**Good**:
```markdown
## When Invoked
1. Run `git diff HEAD` to see changes
2. Review each file against checklist
3. Report findings
```

**Bad**:
```markdown
Review the code I just showed you.
```

**Why**: Agents start fresh. Include all context they need in the system prompt.

### 3. Minimal Tool Access
Follow the principle of least privilege.

**Good**:
```yaml
# Read-only analyzer
tools: Read, Grep, Glob

# Specific bash commands only
tools: Bash(git diff:*), Bash(git log:*)
```

**Bad**:
```yaml
# Full access for simple analysis
tools: Read, Write, Edit, Bash, Grep, Glob
```

**Why**: Limits potential damage, makes agent behavior predictable.

### 4. Clear Workflows
Agents work autonomously — give them clear steps.

**Good**:
```markdown
## When Invoked
1. Get context: `git diff HEAD~1`
2. Identify changed files
3. Review against checklist
4. Format findings
```

**Bad**:
```markdown
Review the code and report issues.
```

**Why**: Clear workflows produce consistent, high-quality results.

### 5. Explicit Output Format
Define exactly how results should look.

**Good**:
```markdown
## Output Format
### Summary
[One-line verdict]

### Issues
| Severity | Location | Description |
|----------|----------|-------------|
```

**Bad**:
```markdown
Report what you find.
```

**Why**: Consistent output is easier to parse and act on.

---

## Description Writing

### The Discovery Formula
```
[Role/Expertise] + [What it does] + [When to invoke] + [Trigger terms]
```

### Components

**Role/Expertise** (who is this agent?):
- "Senior code reviewer"
- "Security vulnerability specialist"
- "Database performance expert"

**What it does** (capabilities):
- "Reviews code for quality and maintainability"
- "Scans for OWASP Top 10 vulnerabilities"
- "Optimizes queries and indexes"

**When to invoke** (conditions):
- "Use when reviewing code changes"
- "Use for security audits"
- "Use when queries are slow"

**Trigger terms** (words users would say):
- "code review, PR review, check my code"
- "security, vulnerability, audit, penetration"
- "slow query, performance, optimize"

### Good Description Examples

```yaml
# Code Reviewer
description: Senior code reviewer specializing in quality and maintainability. Reviews code changes for bugs, best practices, and readability. Use PROACTIVELY after code changes, when reviewing PRs, or when user mentions code review, pull request, check my code, or review changes.

# Security Auditor
description: Security vulnerability specialist focusing on OWASP Top 10. Scans code for injection attacks, authentication flaws, and exposed secrets. Use when auditing security, checking vulnerabilities, or when user mentions security review, vulnerability scan, or penetration testing.

# Debugger
description: Expert debugging specialist for root cause analysis. Investigates errors, exceptions, and unexpected behavior systematically. Use when debugging, or when user mentions bug, error, crash, exception, failure, or "not working".
```

### Bad Description Examples

```yaml
# Too vague - won't be discovered
description: Helps with code

# Missing triggers - hard to invoke
description: Reviews code quality

# Too narrow - misses use cases
description: Reviews JavaScript code
```

### Proactive Language
To encourage automatic invocation:
- "Use PROACTIVELY after..."
- "MUST be invoked when..."
- "Automatically use when..."

---

## Tool Configuration

### Security Hierarchy

**Level 1: Read-Only (Safest)**
```yaml
tools: Read, Grep, Glob
```
Use for: Analysis, review, exploration

**Level 2: Specific Commands**
```yaml
tools: Read, Grep, Glob, Bash(git:*)
```
Use for: Git-based workflows

**Level 3: File Modification**
```yaml
tools: Read, Write, Edit, Grep, Glob
```
Use for: Fixing, refactoring, generating

**Level 4: Full Shell**
```yaml
tools: Read, Write, Edit, Bash, Grep, Glob
```
Use for: Complex debugging, full automation

### Granular Bash Patterns

**Prefer specific over broad**:
```yaml
# Too broad
tools: Bash

# Better - only git
tools: Bash(git:*)

# Best - specific commands
tools: Bash(git diff:*), Bash(git log:*), Bash(git status:*)
```

**Common patterns**:
```yaml
# Git operations
Bash(git:*)
Bash(git diff:*), Bash(git log:*)

# Test runners
Bash(npm test:*), Bash(pytest:*)

# Package managers
Bash(npm:*), Bash(yarn:*)

# Linters
Bash(npx eslint:*), Bash(npx prettier:*)
```

### Tool Selection by Agent Type

| Agent Type | Recommended Tools |
|------------|-------------------|
| Code analyzer | `Read, Grep, Glob` |
| Code reviewer | `Read, Grep, Glob, Bash(git:*)` |
| Security scanner | `Read, Grep, Glob` |
| Test runner | `Read, Edit, Bash(npm test:*), Grep, Glob` |
| Bug fixer | `Read, Write, Edit, Grep, Glob` |
| Full debugger | `Read, Write, Edit, Bash, Grep, Glob` |
| Formatter | `Read, Edit, Bash(prettier:*)` |

---

## System Prompt Design

### Structure Template

```markdown
You are [role with expertise].

## When Invoked
1. [First action - gather context]
2. [Second action - analyze/process]
3. [Third action - produce output]
4. [Fourth action - verify if applicable]

## Focus Areas
- [Key thing to check/do]
- [Another important aspect]
- [Critical consideration]

## Output Format
[Define exactly how results should look]

## Constraints
- Do NOT [forbidden action]
- ALWAYS [required behavior]
```

### Effective Role Definitions

```markdown
# Clear and specific
You are a senior code reviewer specializing in security vulnerabilities.

# With primary focus
You are a debugging expert. Your primary focus is finding root causes, not just symptoms.

# With personality
You are a patient code teacher who explains complex concepts simply.
```

### Workflow Patterns

**Gather → Analyze → Report**:
```markdown
## When Invoked
1. Gather context (git diff, read files)
2. Analyze against criteria
3. Report findings with evidence
```

**Investigate → Hypothesize → Verify**:
```markdown
## When Invoked
1. Capture error/symptom
2. Form hypotheses
3. Test each hypothesis
4. Implement fix
5. Verify fix works
```

**Check → Fix → Verify**:
```markdown
## When Invoked
1. Run checks (lint, test)
2. Fix any issues
3. Re-run to verify
```

### Output Format Patterns

**Checklist Format**:
```markdown
## Output Format
### Checklist
- [x] Check passed
- [ ] Check failed: [reason]
```

**Table Format**:
```markdown
## Output Format
| Severity | Location | Issue | Recommendation |
|----------|----------|-------|----------------|
```

**Structured Report**:
```markdown
## Output Format
### Summary
[One-line verdict]

### Details
[Structured findings]

### Recommendations
[Actionable next steps]
```

### Effective Constraints

```markdown
## Constraints
# What NOT to do
- Do NOT modify code unless explicitly asked
- Do NOT change API contracts
- Do NOT skip security checks

# What to ALWAYS do
- ALWAYS explain WHY something is an issue
- ALWAYS provide specific file:line references
- ALWAYS verify fixes work before reporting
```

---

## Model Selection

### Quick Reference

| Model | Use When |
|-------|----------|
| `haiku` | Quick checks, simple tasks, high volume |
| `sonnet` | Most tasks, balanced needs |
| `opus` | Complex analysis, security, architecture |
| `inherit` | User-facing, consistency matters |

### Selection Criteria

**Use `haiku` when**:
- Task is straightforward
- Speed matters more than depth
- High-volume operations
- Simple validation checks

**Use `sonnet` when**:
- Standard development tasks
- Code review and debugging
- Test writing
- Default choice

**Use `opus` when**:
- Security-critical analysis
- Architecture review
- Complex problem solving
- Deep investigation needed

**Use `inherit` when**:
- Agent should match user's choice
- Consistency with main conversation
- User-facing interactions

---

## Permission Modes

### When to Use Each

| Mode | Use Case | Risk Level |
|------|----------|------------|
| `default` | Most agents | Low |
| `acceptEdits` | Trusted formatters/linters | Medium |
| `bypassPermissions` | CI/CD automation only | High |
| `plan` | Analysis/planning agents | Lowest |

### Safe Combinations

**Analysis Agent (Safest)**:
```yaml
tools: Read, Grep, Glob
permissionMode: plan
```

**Trusted Automation**:
```yaml
tools: Read, Edit, Bash(prettier:*)
permissionMode: acceptEdits
```

**CI/CD Only**:
```yaml
tools: Read, Bash, Grep
permissionMode: bypassPermissions
```

---

## Team Collaboration

### Version Control
- Commit project agents to git: `.claude/agents/`
- Review agent changes like code
- Document agent purpose in description

### Naming Conventions
- Use descriptive names: `security-auditor` not `sa`
- Prefix by domain: `frontend-reviewer`, `backend-debugger`
- Avoid generic names: `helper`, `tool`

### Documentation
- Clear description (for discovery)
- Workflow steps (for understanding)
- Output format (for consistency)
- Constraints (for safety)

### Testing Protocol
1. Create agent
2. Test discovery with natural language
3. Verify tool access works
4. Check output format
5. Review with team
6. Commit to git

---

## Common Mistakes

### 1. Vague Descriptions
```yaml
# Bad
description: Helps with code

# Good
description: Reviews code for quality, security, and maintainability. Use when...
```

### 2. Over-Permissive Tools
```yaml
# Bad - too broad
tools: Bash

# Good - scoped
tools: Bash(git:*), Bash(npm test:*)
```

### 3. Non-Self-Contained Prompts
```markdown
# Bad - assumes context
Review the code from our earlier discussion.

# Good - self-contained
## When Invoked
1. Run `git diff HEAD` to see changes
```

### 4. Missing Output Format
```markdown
# Bad - no structure
Report what you find.

# Good - explicit format
## Output Format
| Severity | Location | Issue |
```

### 5. Missing Constraints
```markdown
# Bad - no boundaries
You are a code fixer.

# Good - clear limits
## Constraints
- Make MINIMAL changes
- Do NOT refactor unrelated code
```

---

## Maintenance

### Regular Review
- Are agents still being discovered correctly?
- Are outputs still meeting needs?
- Have tools/permissions scope creeped?

### Deprecation
- Remove unused agents
- Consolidate overlapping agents
- Update outdated workflows

### Evolution
- Start simple, add complexity as needed
- Refine based on usage patterns
- Update for new project patterns
