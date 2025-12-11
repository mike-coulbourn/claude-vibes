# Agent Troubleshooting Guide

Diagnosing and fixing common agent issues.

---

## Quick Diagnosis

### Symptom → Likely Cause → Solution

| Symptom | Likely Cause | Quick Fix |
|---------|--------------|-----------|
| Agent not discovered | Vague description | Add specific triggers |
| Wrong agent invoked | Similar descriptions | Make descriptions distinct |
| Agent can't do task | Missing tool | Add required tool |
| Agent errors out | YAML syntax error | Validate YAML |
| Inconsistent output | No output format | Define output structure |
| Agent too slow | Wrong model | Use `haiku` for simple tasks |
| Permission denied | Missing permission | Adjust permissionMode |

---

## Issue 1: Agent Not Discovered

**Symptom**: You ask Claude to do something your agent should handle, but it doesn't use the agent.

### Cause 1: Vague Description

**Problem**:
```yaml
description: Helps with code
```

**Solution**: Make description specific with triggers:
```yaml
description: Senior code reviewer. Reviews code for quality, security, and maintainability. Use when reviewing code, checking PRs, or when user mentions code review, pull request review, or check my code.
```

### Cause 2: Missing Trigger Terms

**Problem**:
```yaml
description: Performs security analysis on code
```

**Solution**: Add natural language triggers:
```yaml
description: Security vulnerability scanner. Scans code for OWASP Top 10 vulnerabilities. Use when user mentions security audit, vulnerability scan, security check, or penetration testing.
```

### Cause 3: File Location Wrong

**Problem**: File not in correct directory.

**Solution**: Verify location:
```bash
# Project agents
ls .claude/agents/

# Personal agents
ls ~/.claude/agents/
```

### Cause 4: YAML Syntax Error

**Problem**: Invalid YAML prevents loading.

**Solution**: Validate YAML:
```bash
python3 -c "
import yaml
with open('.claude/agents/my-agent.md') as f:
    content = f.read()
    parts = content.split('---')
    yaml.safe_load(parts[1])
    print('YAML valid')
"
```

### Testing Discovery
After fixing, test with natural language:
```
> Review my recent code changes
> Check this for security issues
> Help me debug this error
```

---

## Issue 2: Wrong Agent Invoked

**Symptom**: Claude uses a different agent than intended.

### Cause 1: Overlapping Descriptions

**Problem**: Two agents have similar descriptions.

**Agent 1**:
```yaml
name: code-reviewer
description: Reviews code for issues
```

**Agent 2**:
```yaml
name: security-reviewer
description: Reviews code for security issues
```

**Solution**: Make descriptions distinct:

**Agent 1**:
```yaml
description: Code quality reviewer. Focuses on readability, maintainability, and best practices. Use for general code review, PR review, or quality checks.
```

**Agent 2**:
```yaml
description: Security vulnerability scanner. Focuses on OWASP Top 10, injection attacks, and exposed secrets. Use specifically for security audits, vulnerability scans, or penetration testing prep.
```

### Cause 2: Generic Triggers

**Problem**: Description uses generic terms that match many contexts.

**Solution**: Use specific, unique triggers for each agent.

### Testing Selection
Be explicit to test:
```
> Use the code-reviewer agent to check this
> Use the security-reviewer agent to scan for vulnerabilities
```

---

## Issue 3: Agent Can't Perform Task

**Symptom**: Agent tries to do something but fails due to missing capability.

### Cause 1: Missing Tool

**Problem**:
```yaml
tools: Read, Grep, Glob
```
Agent tries to run `git diff` but can't.

**Solution**: Add required tool:
```yaml
tools: Read, Grep, Glob, Bash(git:*)
```

### Cause 2: Tool Too Restricted

**Problem**:
```yaml
tools: Bash(git diff:*)
```
Agent needs `git log` but can only run `git diff`.

**Solution**: Broaden tool access:
```yaml
tools: Bash(git:*)
# or specifically
tools: Bash(git diff:*), Bash(git log:*), Bash(git status:*)
```

### Cause 3: Permission Mode Blocking

**Problem**:
```yaml
permissionMode: plan
```
Agent can't edit files in plan mode.

**Solution**: Change permission mode:
```yaml
permissionMode: default
```

### Diagnosis Command
Ask Claude:
```
> What tools does the [agent-name] agent have access to?
```

---

## Issue 4: Agent Errors During Execution

**Symptom**: Agent starts but encounters errors.

### Cause 1: YAML Syntax Error

**Symptoms**:
- Agent not loaded at all
- Unexpected behavior

**Diagnosis**:
```bash
claude --debug
```

**Common YAML Errors**:

```yaml
# Missing quotes for special characters
description: Security: scans code    # Error: colon in value
description: "Security: scans code"  # Fixed

# Tab instead of spaces
name:	my-agent    # Error: tab character
name: my-agent      # Fixed: spaces

# Missing closing ---
---
name: agent
description: desc
# Missing closing ---
```

### Cause 2: Invalid Tool Specification

**Problem**:
```yaml
tools: [Read, Grep]    # Wrong: array syntax
tools: Read Grep       # Wrong: missing commas
```

**Solution**:
```yaml
tools: Read, Grep, Glob    # Correct: comma-separated
```

### Cause 3: Invalid Model Value

**Problem**:
```yaml
model: gpt-4    # Wrong: not a valid option
```

**Solution**:
```yaml
model: sonnet   # Correct: haiku, sonnet, opus, or inherit
```

---

## Issue 5: Inconsistent Output

**Symptom**: Agent produces different output formats each time.

### Cause: Missing Output Format

**Problem**: No output format specified in system prompt.

**Solution**: Define explicit format:
```markdown
## Output Format

### Summary
[One-line verdict: PASS/FAIL/NEEDS REVIEW]

### Issues Found
| Severity | Location | Description | Recommendation |
|----------|----------|-------------|----------------|

### Next Steps
1. [First action]
2. [Second action]
```

### Cause 2: Ambiguous Instructions

**Problem**: System prompt is vague about expected output.

**Bad**:
```markdown
Report what you find.
```

**Good**:
```markdown
Report findings as a severity-sorted table with file locations and recommendations.
```

---

## Issue 6: Agent Too Slow

**Symptom**: Agent takes too long to respond.

### Cause 1: Using Opus for Simple Tasks

**Problem**:
```yaml
model: opus    # Overkill for simple checks
```

**Solution**: Use appropriate model:
```yaml
model: haiku   # Fast for simple tasks
model: sonnet  # Balanced for most tasks
model: opus    # Only for complex analysis
```

### Cause 2: Too Many Tools

**Problem**: Agent has access to many tools it doesn't need.

**Solution**: Limit to required tools:
```yaml
# Before: all tools
tools: Read, Write, Edit, Bash, Grep, Glob, WebSearch, WebFetch

# After: only needed
tools: Read, Grep, Glob
```

### Cause 3: Overly Complex Workflow

**Problem**: System prompt has too many steps.

**Solution**: Simplify workflow to essential steps.

---

## Issue 7: Permission Denied Errors

**Symptom**: Agent is blocked from performing actions.

### Cause 1: Permission Mode Too Restrictive

**Problem**:
```yaml
permissionMode: plan    # Can't edit files
```

**Solution**: Adjust mode:
```yaml
permissionMode: default    # Prompts for permission
permissionMode: acceptEdits # Auto-accepts edits
```

### Cause 2: Missing Tool for Action

**Problem**: Agent needs to edit files but only has Read.

**Solution**: Add Edit tool:
```yaml
tools: Read, Write, Edit, Grep, Glob
```

### Cause 3: Bash Pattern Doesn't Match

**Problem**:
```yaml
tools: Bash(git diff:*)
```
Agent tries to run `git status` but pattern only allows `git diff`.

**Solution**: Broaden pattern:
```yaml
tools: Bash(git:*)
```

---

## Issue 8: Agent Does Too Much/Too Little

### Too Much

**Symptom**: Agent modifies files or performs actions beyond scope.

**Cause**: Tools or permissions too broad.

**Solution**:
1. Restrict tools:
```yaml
tools: Read, Grep, Glob  # Read-only
```

2. Add constraints:
```markdown
## Constraints
- Do NOT modify any files
- Do NOT execute commands
- Analysis and reporting only
```

3. Use plan mode:
```yaml
permissionMode: plan
```

### Too Little

**Symptom**: Agent stops short of completing task.

**Cause**: Missing tools or unclear workflow.

**Solution**:
1. Add required tools:
```yaml
tools: Read, Write, Edit, Grep, Glob
```

2. Clarify workflow:
```markdown
## When Invoked
1. Identify issue
2. Locate code
3. Implement fix  # Be explicit
4. Verify fix works
```

---

## Issue 9: YAML Parsing Errors

### Common Errors and Fixes

**Error: Tabs instead of spaces**
```yaml
# Wrong
name:	my-agent    # Tab character

# Fixed
name: my-agent      # Space
```

**Error: Missing closing `---`**
```yaml
# Wrong
---
name: agent
description: does stuff

Content here...

# Fixed
---
name: agent
description: does stuff
---

Content here...
```

**Error: Colon in value without quotes**
```yaml
# Wrong
description: Focus: Security analysis

# Fixed
description: "Focus: Security analysis"
```

**Error: Invalid characters in name**
```yaml
# Wrong
name: Code_Reviewer    # Underscore
name: code reviewer    # Space
name: Code-Reviewer    # Uppercase

# Fixed
name: code-reviewer    # Lowercase with hyphens
```

### YAML Validation Script
```bash
#!/bin/bash
# validate-agent.sh

FILE=$1

python3 << EOF
import yaml
import re

with open("$FILE") as f:
    content = f.read()

# Check for --- delimiters
if not content.startswith('---'):
    print("ERROR: Missing opening ---")
    exit(1)

parts = content.split('---')
if len(parts) < 3:
    print("ERROR: Missing closing ---")
    exit(1)

# Parse YAML
try:
    meta = yaml.safe_load(parts[1])
except yaml.YAMLError as e:
    print(f"YAML ERROR: {e}")
    exit(1)

# Check required fields
if 'name' not in meta:
    print("ERROR: Missing 'name' field")
    exit(1)

if 'description' not in meta:
    print("ERROR: Missing 'description' field")
    exit(1)

# Validate name format
name = meta['name']
if not re.match(r'^[a-z][a-z0-9-]*$', name):
    print(f"ERROR: Invalid name format: {name}")
    print("  Name must be lowercase letters, numbers, and hyphens")
    exit(1)

# Check description length
desc = meta.get('description', '')
if len(desc) < 20:
    print(f"WARNING: Description too short ({len(desc)} chars)")
elif len(desc) > 500:
    print(f"WARNING: Description very long ({len(desc)} chars)")

print("✓ Agent file is valid")
EOF
```

---

## 5-Step Debugging Workflow

When an agent isn't working:

### Step 1: Verify File
```bash
# Check file exists
ls -la .claude/agents/my-agent.md
# or
ls -la ~/.claude/agents/my-agent.md

# Check file content
cat .claude/agents/my-agent.md
```

### Step 2: Validate YAML
```bash
# Use debug mode
claude --debug

# Or validate manually
python3 -c "import yaml; yaml.safe_load(open('.claude/agents/my-agent.md').read().split('---')[1])"
```

### Step 3: Check Description
- Is it specific?
- Does it include trigger terms?
- Is it different from other agents?

### Step 4: Test Discovery
```
> Use the my-agent agent to [do something]
```
If explicit invocation works but natural language doesn't, the description needs improvement.

### Step 5: Check Tools
If agent can't do something:
```
> What tools does my-agent have?
```
Add missing tools to the `tools` field.

---

## Diagnostic Commands

### List All Agents
```bash
/agents
```

### Check Debug Output
```bash
claude --debug
```

### Validate YAML Syntax
```bash
python3 -c "
import yaml
with open('FILE') as f:
    parts = f.read().split('---')
    yaml.safe_load(parts[1])
    print('Valid')
"
```

### Check Agent Description
```bash
grep -A1 "description:" .claude/agents/*.md
```

### Compare Descriptions
```bash
# Find similar descriptions
for f in .claude/agents/*.md; do
  echo "=== $f ==="
  grep "description:" "$f"
done
```

---

## Getting Help

If still stuck:

1. **Check official docs**: `/help` for Claude Code documentation
2. **Debug mode**: `claude --debug` shows loading errors
3. **Simplify**: Start with minimal agent, add complexity
4. **Test explicitly**: `Use the X agent to...` bypasses discovery
5. **Compare to examples**: Use working examples as templates
