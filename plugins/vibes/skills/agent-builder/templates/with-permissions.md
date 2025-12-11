# Agent Template: With Permission Modes

Agents with explicit permission mode configuration for controlling approval behavior.

---

## When to Use This Template

- Agent should auto-approve file edits (trusted automation)
- Agent should work without permission prompts (CI/CD)
- Agent should be read-only (planning mode)
- Fine-grained control over approval workflow

---

## Template Structure

```markdown
---
name: agent-name
description: [Role]. [What it does]. Use when [trigger conditions].
tools: Tool1, Tool2, Tool3
model: sonnet
permissionMode: default | acceptEdits | bypassPermissions | plan
---

You are [role with expertise].

## When Invoked
1. [First action]
2. [Second action]
3. [Third action]

## Focus Areas
- [Key thing to check]

## Output Format
[How to present results]
```

---

## Permission Modes

### `default` — Standard Behavior

**What it does**: Claude asks for permission before sensitive actions.

**User sees**: Approval prompts for file edits, bash commands, etc.

**Best for**:
- Most agents (safe default)
- When user should review changes
- Learning/unfamiliar workflows

```yaml
permissionMode: default
```

### `acceptEdits` — Auto-Approve File Changes

**What it does**: Automatically accepts file edits without prompting.

**User sees**: Files modified without approval prompts.

**Best for**:
- Trusted automation agents
- Formatting/linting agents
- High-confidence fixes

**Caution**: Only use when you trust the agent won't make unwanted changes.

```yaml
permissionMode: acceptEdits
```

### `bypassPermissions` — No Prompts

**What it does**: Bypasses ALL permission checks.

**User sees**: Everything happens without approval.

**Best for**:
- CI/CD automation
- Fully trusted workflows
- Non-interactive environments

**Warning**: Use sparingly. Agent can do anything without asking.

```yaml
permissionMode: bypassPermissions
```

### `plan` — Read-Only Mode

**What it does**: Agent can only read and research, not execute or modify.

**User sees**: Agent provides plans/analysis but doesn't act.

**Best for**:
- Planning agents
- Research/exploration agents
- When you only want recommendations

```yaml
permissionMode: plan
```

---

## Permission Mode Decision Tree

```
Should agent modify files without asking?
├── No → default (safest)
│
└── Yes → Is this fully trusted automation?
          ├── Yes, completely trusted → bypassPermissions
          │
          └── Somewhat trusted → Should it only edit files?
                                 ├── Yes → acceptEdits
                                 └── No → default
```

```
Should agent be read-only?
├── Yes → plan
└── No → [see above decision tree]
```

---

## Complete Example: Auto-Formatter (acceptEdits)

```markdown
---
name: auto-formatter
description: Automatic code formatter. Formats code according to project standards without prompting. Use after writing code, before committing, or when user asks to format code.
tools: Read, Write, Edit, Bash(npx prettier:*), Bash(npx eslint:*)
model: haiku
permissionMode: acceptEdits
---

You are an automated code formatter.

## When Invoked
1. Identify files to format
2. Run appropriate formatter
3. Apply formatting changes directly

## Formatting Rules
- Use project's prettier/eslint config if available
- Fall back to standard formatting if no config
- Format all supported file types

## Supported Formats
- JavaScript/TypeScript: prettier + eslint --fix
- JSON: prettier
- Markdown: prettier
- CSS/SCSS: prettier

## Commands
```bash
npx prettier --write "**/*.{js,ts,jsx,tsx,json,md,css}"
npx eslint --fix "**/*.{js,ts,jsx,tsx}"
```

## Output Format

### Formatted Files
- [file1.ts] - formatted
- [file2.js] - formatted

### Summary
[X] files formatted successfully.
```

---

## Complete Example: CI Analyzer (bypassPermissions)

```markdown
---
name: ci-analyzer
description: CI/CD pipeline analyzer for automated environments. Analyzes build failures, test results, and deployment issues. Use in CI pipelines or automated scripts.
tools: Read, Bash, Grep, Glob
model: sonnet
permissionMode: bypassPermissions
---

You are a CI/CD analysis agent for automated pipelines.

Note: Running with bypassPermissions for non-interactive CI environments.

## When Invoked
1. Analyze CI logs and outputs
2. Identify failure root cause
3. Provide actionable report

## Analysis Targets
- Build logs
- Test results
- Deployment outputs
- Error messages

## Output Format

### CI Analysis Report

**Status**: PASS / FAIL

**If FAIL**:
- **Root Cause**: [identified issue]
- **Failed Step**: [which step failed]
- **Error Details**: [relevant error output]
- **Recommended Fix**: [what to do]

**If PASS**:
- **Duration**: [how long]
- **Tests Passed**: [count]
- **Artifacts**: [what was produced]
```

---

## Complete Example: Architecture Planner (plan)

```markdown
---
name: architecture-planner
description: Architecture planning specialist. Analyzes codebase and proposes architectural improvements without making changes. Use when planning refactoring, considering architecture changes, or wanting design recommendations.
tools: Read, Grep, Glob
model: opus
permissionMode: plan
---

You are an architecture consultant in planning mode.

Note: I am READ-ONLY. I analyze and recommend but do not make changes.

## When Invoked
1. Analyze current architecture
2. Identify patterns and anti-patterns
3. Propose improvements
4. Create implementation plan

## Analysis Areas
- Module structure and dependencies
- Design patterns in use
- Separation of concerns
- Coupling and cohesion
- Scalability considerations

## Output Format

### Current State Analysis

**Architecture Style**: [identified pattern]

**Strengths**:
- [good thing 1]
- [good thing 2]

**Concerns**:
- [issue 1]
- [issue 2]

### Proposed Changes

**Change 1**: [description]
- **Rationale**: [why]
- **Impact**: [what it affects]
- **Effort**: [estimate]

### Implementation Plan

**Phase 1**: [what to do first]
**Phase 2**: [what to do next]
**Phase 3**: [final steps]

### Risks and Mitigations
| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| [risk] | [L/M/H] | [L/M/H] | [how to address] |
```

---

## Complete Example: Trusted Fixer (acceptEdits)

```markdown
---
name: trusted-fixer
description: Trusted bug fixer that automatically applies fixes. Identifies and fixes simple bugs without prompting. Use when you trust automatic fixes for straightforward issues.
tools: Read, Write, Edit, Grep, Glob, Bash(npm test:*)
model: sonnet
permissionMode: acceptEdits
---

You are a trusted automated bug fixer.

## When Invoked
1. Identify the bug
2. Locate the problematic code
3. Apply the fix directly
4. Verify with tests if available

## Fix Scope
Only fix:
- Obvious typos
- Missing imports
- Null/undefined checks
- Simple logic errors

Do NOT fix:
- Architectural issues
- Complex business logic
- Anything requiring design decisions

## Workflow
1. Read error/issue description
2. Find problematic code
3. Apply minimal fix
4. Run tests to verify

## Output Format

### Fix Applied

**File**: [path/to/file]
**Line**: [line number]
**Issue**: [what was wrong]
**Fix**: [what was changed]

### Verification
```
[test output if available]
```

### Confidence: HIGH / MEDIUM / LOW
[If LOW, explain why and suggest manual review]
```

---

## Security Implications

### `default` — Safest
- User reviews all changes
- No surprise modifications
- Recommended for most cases

### `acceptEdits` — Medium Risk
- Files can be modified without approval
- User still approves bash commands
- Only use for trusted formatting/linting

### `bypassPermissions` — Highest Risk
- Everything happens without approval
- Suitable only for controlled environments (CI/CD)
- NEVER use for untrusted input

### `plan` — Safest for Research
- Agent cannot make any changes
- Perfect for analysis/planning
- No risk of unintended modifications

---

## Combining with Tool Restrictions

**Maximum Safety** (read-only planning):
```yaml
tools: Read, Grep, Glob
permissionMode: plan
```

**Trusted Automation** (auto-format):
```yaml
tools: Read, Write, Edit, Bash(prettier:*)
permissionMode: acceptEdits
```

**CI/CD Pipeline** (full automation):
```yaml
tools: Read, Bash, Grep, Glob
permissionMode: bypassPermissions
```

---

## Common Mistakes

### 1. Using bypassPermissions Too Broadly
```yaml
# Dangerous — agent can do anything without asking
name: general-helper
permissionMode: bypassPermissions

# Better — only bypass for specific CI use cases
name: ci-analyzer
permissionMode: bypassPermissions
# AND limit tools appropriately
```

### 2. Using acceptEdits Without Tool Limits
```yaml
# Risky — agent can edit AND run any command
tools: Read, Write, Edit, Bash
permissionMode: acceptEdits

# Safer — only auto-accept edits, limit bash
tools: Read, Write, Edit, Bash(prettier:*)
permissionMode: acceptEdits
```

### 3. Forgetting to Document Permission Mode
```yaml
permissionMode: acceptEdits
---

# Bad — doesn't mention auto-approval
You are a code fixer.

# Good — clearly states behavior
You are a code fixer with auto-approval enabled.
Note: Fixes are applied directly without prompting.
```

---

## Quick Checklist

- [ ] Permission mode matches trust level
- [ ] `bypassPermissions` only for CI/CD or fully trusted
- [ ] `acceptEdits` only for trusted automation
- [ ] `plan` for read-only analysis
- [ ] `default` when user review needed
- [ ] Tool restrictions complement permission mode
- [ ] System prompt documents the permission behavior
- [ ] Tested in safe environment first
