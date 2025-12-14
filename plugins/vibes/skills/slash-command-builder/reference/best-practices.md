# Slash Command Best Practices

Patterns and principles for creating effective commands.

## General Principles

### 1. Start Simple, Add Complexity Incrementally

```markdown
# Phase 1: Basic prompt
Analyze this code for issues.

# Phase 2: Add arguments
Analyze @$1 for issues.

# Phase 3: Add bash context
Branch: !\`git branch --show-current\`
Analyze @$1 for issues.

# Phase 4: Add structure and constraints
[Full structured command with all features]
```

**Why**: Easier to debug, clearer what each feature adds, less overwhelming.

### 2. Always Include Description

```yaml
✅ GOOD:
---
description: Review code for security issues
---

❌ BAD:
(no frontmatter)
```

**Why**: Team members understand purpose, appears in `/help`, required for SlashCommand tool.

### 3. Use Minimal Tool Permissions

```yaml
✅ GOOD:
allowed-tools: Read, Grep, Glob  # Read-only analysis

❌ BAD:
allowed-tools: Bash  # Too broad, any command
```

**Why**: Security, safety, prevents accidental modifications.

## Naming Conventions

### Use Descriptive, Action-Oriented Names

```
✅ GOOD:
review-security.md
generate-tests.md
commit-with-context.md

❌ BAD:
helper.md
do-stuff.md
cmd1.md
```

### Use Hyphens, Not Underscores or Spaces

```
✅ GOOD: code-review.md → /code-review
❌ BAD: code_review.md (underscores)
❌ BAD: code review.md (spaces don't work)
```

### Keep Names Concise But Clear

```
✅ GOOD: /commit, /review, /test, /deploy
⚠️ OK: /create-commit-message (clear but long)
❌ BAD: /c (too short, unclear)
```

## Arguments Best Practices

### Use argument-hint

```yaml
✅ GOOD:
argument-hint: [file-path] [review-focus]

❌ BAD:
(no argument-hint)
```

**Why**: Self-documenting, users know what to provide.

### Choose the Right Argument Style

**Use $ARGUMENTS when**:
- Free-form text input
- Single conceptual input
- Don't need to separate parts

```markdown
Explain $ARGUMENTS in detail.
Usage: /explain "async/await in JavaScript"
```

**Use $1, $2, $3 when**:
- Structured parameters
- Different parts used separately
- Want to validate each part

```markdown
Review PR #$1 with priority $2 assigned to $3.
Usage: /review-pr 456 high alice
```

### Document Arguments in Prompt

```markdown
✅ GOOD:
## Arguments

- $1: File path to analyze
- $2: Focus area (security, performance, quality)

## Task
Analyze @$1 focusing on $2...

❌ BAD:
Analyze @$1 focusing on $2...
(no explanation of what $1 and $2 are)
```

## Bash Execution Best Practices

### Always Restrict Tools

```yaml
✅ GOOD:
allowed-tools: Bash(git:*)

❌ BAD:
allowed-tools: Bash  # Too permissive
```

### Test Commands in Terminal First

```bash
# Test first
git branch --show-current

# Then add to command
!\`git branch --show-current\`
```

**Why**: Verify output format, ensure it works, check speed.

### Use Fast Commands

```markdown
✅ GOOD:
!\`git status --short\`        # Fast
!\`git log --oneline -10\`     # Limited output

❌ BAD:
!\`npm install\`                # Takes minutes
!\`git log --all\`              # Huge output
```

### Capture stderr When Needed

```markdown
Test results: !\`npm test 2>&1\`
```

**Why**: Errors/failures are useful context.

### Structure Output Clearly

```markdown
✅ GOOD:
## Git Status
!\`git status\`

## Recent Commits
!\`git log --oneline -5\`

❌ BAD:
!\`git status\` !\`git log --oneline -5\`
(runs together, hard to read)
```

## File Reference Best Practices

### Combine with Arguments for Flexibility

```markdown
✅ GOOD:
argument-hint: [file-to-review]
Review @$1 for quality issues.

Usage: /review src/any-file.js
```

### Reference Project Conventions

```markdown
✅ GOOD:
## Project Standards
@CLAUDE.md
@docs/coding-standards.md

## Task
Follow the standards above when reviewing...
```

**Why**: Ensures consistency with project conventions.

### Reference Examples

```markdown
## Existing Pattern
@src/examples/good-pattern.js

## Your Task
Create new code following the pattern above...
```

**Why**: Shows expected style, generates consistent code.

### Verify Paths

```markdown
# In development, verify first:
ls src/auth.js

# Then reference:
@src/auth.js
```

## Command Structure Best Practices

### Use Clear Sections

```markdown
✅ GOOD:
## Context
[Gather information]

## Reference Materials
[Include files/conventions]

## Task
[Clear instructions]

## Constraints
[Specific requirements]

❌ BAD:
Do this thing considering that other thing...
(unstructured, hard to follow)
```

### Put Context Before Task

```markdown
✅ GOOD:
## Current State
!\`git status\`

## Task
Based on status above, suggest next action.

❌ BAD:
## Task
Suggest next action.

## Current State
!\`git status\`
(context comes after task)
```

**Why**: Claude sees context before instructions.

### Be Specific in Instructions

```markdown
✅ GOOD:
Review for:
1. SQL injection vulnerabilities
2. XSS attack vectors
3. Authentication bypass risks

For each issue:
- Severity (Critical/High/Medium/Low)
- Location (file:line)
- Fix with code example

❌ BAD:
Review the code for security issues.
(vague, unclear what to look for)
```

## Security and Safety

### Principle of Least Privilege

```yaml
# Analysis only
allowed-tools: Read, Grep, Glob

# Git read-only
allowed-tools: Bash(git log:*), Bash(git diff:*), Bash(git status:*)

# Git read and commit
allowed-tools: Bash(git:*)
```

**Why**: Prevents accidental damage, limits blast radius.

### Avoid Destructive Commands

```markdown
❌ DANGEROUS:
!\`rm -rf node_modules\`
!\`git reset --hard\`
!\`npm run deploy\`

✅ SAFE:
!\`ls node_modules\`
!\`git status\`
!\`npm test\`
```

### Validate Before Executing

```markdown
Check file exists:
!\`[ -f "$1" ] && echo "exists" || echo "missing"\`

If exists, then process...
```

## Command Organization

### Group Related Commands

```
.claude/commands/
├── git/
│   ├── commit.md
│   ├── pr.md
│   └── branch.md
├── code/
│   ├── review.md
│   ├── test.md
│   └── refactor.md
```

**Why**: Easier to find, logical structure, scalable.

### Use Consistent Naming Patterns

```
# Code operations
review-code.md
analyze-code.md
refactor-code.md

# Git operations
commit-changes.md
create-pr.md
merge-branch.md
```

### Document Commands

Create `.claude/commands/README.md`:

```markdown
# Project Commands

## Code Quality
- `/review` - Code review
- `/security` - Security audit

## Git Workflow
- `/commit` - Generate commit message
- `/pr` - Create pull request
```

## Testing and Iteration

### Test with Real Data

```bash
# Don't test with:
/commit
(empty repo)

# Test with:
git add src/file.js
/commit
(actual changes)
```

### Test Edge Cases

```bash
# Missing arguments
/review-pr

# File doesn't exist
/review non-existent.js

# No git changes
/commit
(clean working directory)
```

### Iterate Based on Usage

```markdown
# Version 1: Basic
Review this code.

# Version 2: After feedback
Review @$1 for security issues.

# Version 3: After more usage
[Full structured command with learnings]
```

## Team Collaboration

### For Project Commands

1. **Discuss before creating**: Ensure team agrees it's useful
2. **Test with teammates**: Verify it works for others
3. **Document in README**: Help discovery
4. **Maintain**: Update as patterns evolve

### For Personal Commands

1. **Experiment freely**: Try ideas quickly
2. **Promote if useful**: Move to project if team could benefit
3. **Share patterns**: Document successful approaches

## Performance Considerations

### Keep Commands Fast

```markdown
✅ FAST:
!\`git status\`              # <1 second
!\`grep "pattern" file.js\`  # <1 second

❌ SLOW:
!\`npm install\`             # Minutes
!\`npm run build\`           # Could be slow
```

### Limit Output Size

```markdown
✅ GOOD:
!\`git log --oneline -10\`   # Limited

❌ BAD:
!\`git log --all\`           # Could be huge
```

### Progressive Detail

```markdown
## Quick Summary
[Essential info]

## Detailed Context
[More info if needed]
```

**Why**: User can stop reading if summary is enough.

## Common Patterns

### Pattern: Gather → Analyze → Recommend

```markdown
## Context
[Bash commands to gather state]

## Analysis
[File references to understand code]

## Recommendations
Based on above, suggest...
```

### Pattern: Show Examples → Generate

```markdown
## Existing Examples
@examples/good-pattern.js

## Your Task
Generate new code following pattern above...
```

### Pattern: Check → Report → Fix

```markdown
## Checks
[Run validation]

## Issues
[Analyze failures]

## Fixes
[Provide solutions]
```

## When to Use vs. Skills

**Use Slash Commands**:
- Manual invocation (you decide when)
- Simple, focused operations
- Quick templates
- Single-file definition

**Use Skills**:
- Automatic discovery (Claude decides when)
- Complex multi-step workflows
- Multiple supporting files
- Team capabilities

**Example**:
- Command: `/commit` - You invoke when ready
- Skill: `skill-builder` - Claude discovers when you mention Skills

## Maintenance

### Review and Prune

Periodically review commands:
- Which are actually used?
- Which are outdated?
- Which can be improved?

### Update for Evolving Patterns

When project patterns change:
- Update command templates
- Revise generated code format
- Adjust conventions references

### Version Control

```gitignore
# Commit project commands
.claude/commands/

# Don't commit personal commands
# (these are in ~/.claude/commands/)
```

---

Follow these practices to create commands that are safe, useful, and maintainable!
