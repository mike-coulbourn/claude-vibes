# Slash Command with Bash Execution Template

Execute bash commands to gather system context before your prompt runs.

## When to Use This Template

- Need current system state (git status, test results, file lists)
- Want to gather dynamic context
- Automate context collection
- Build commands that adapt to current state

## Basic Syntax

```markdown
---
description: [Brief description]
allowed-tools: Bash(command:*)
---

## Context

Current state: [execute: command here]

## Task

[Your prompt using the context above]
```

**Critical requirement**: Must include `allowed-tools: Bash(...)` in frontmatter.

## How Bash Execution Works

1. Bash commands execute BEFORE Claude sees the prompt
2. Command output replaces the [execute: command] in the text
3. Claude receives the prompt with actual output included

**Example**:
```markdown
Branch: [execute: git branch --show-current]
```

Becomes:
```markdown
Branch: main
```

## Security: Tool Restrictions

Limit bash access to specific commands:

```yaml
# Git operations only
allowed-tools: Bash(git:*)

# Multiple tools
allowed-tools: Bash(git:*), Bash(npm:*)

# Specific commands
allowed-tools: Bash(git status:*), Bash(git log:*), Bash(git diff:*)

# No restrictions (use carefully!)
allowed-tools: Bash
```

**Best practice**: Use narrowest permissions needed.

## Complete Examples

### Example 1: Git Commit Command

**File**: `.claude/commands/commit.md`

```markdown
---
description: Create git commit with full context
allowed-tools: Bash(git:*)
---

## Current Git State

**Branch**: [execute: git branch --show-current]

**Status**:
[execute: git status --short]

**Recent Commits** (for style reference):
[execute: git log --oneline -10]

## Changes to Commit

### Staged Changes:
[execute: git diff --staged]

### Unstaged Changes (FYI):
[execute: git diff]

## Project Conventions

@CLAUDE.md

## Your Task

Create a commit message that:
- Follows our project conventions (see above)
- Matches our commit history style (see recent commits)
- Clearly describes what changed and why
- Uses conventional commit format (feat, fix, docs, etc.)
```

**Usage**:
```
# Stage your changes
git add .

# Generate commit message
/commit
```

### Example 2: Test Runner

**File**: `.claude/commands/run-tests.md`

```markdown
---
description: Run tests and analyze failures
allowed-tools: Bash(npm:*), Bash(pytest:*)
---

## Test Execution

Running tests...

[execute: npm test 2>&1] or [execute: pytest -v 2>&1]

## Analysis Task

Based on the test output above:

1. **Summarize Results**
   - How many passed/failed?
   - What categories of tests failed?

2. **Identify Issues**
   - What are the root causes?
   - Are failures related?

3. **Suggest Fixes**
   - Specific code changes needed
   - Priority order for fixes

4. **Prevention**
   - How to prevent these failures?
   - Should we add more tests?
```

**Usage**:
```
/run-tests
```

### Example 3: Code Coverage Check

**File**: `.claude/commands/check-coverage.md`

```markdown
---
description: Check test coverage and suggest improvements
allowed-tools: Bash(npm:*), Bash(pytest:*), Read, Grep, Glob
---

## Current Coverage

[execute: npm run coverage --silent] or [execute: pytest --cov=src --cov-report=term]

## Uncovered Files

Files with low coverage:
[execute: find src -name "*.js" -o -name "*.ts" | head -20]

## Analysis Task

Based on the coverage report:

1. **Coverage Summary**
   - Overall percentage
   - Areas with good coverage
   - Areas needing improvement

2. **Priority Files**
   - Which uncovered files are most critical?
   - Which should be tested first?

3. **Test Suggestions**
   - What tests are missing?
   - What scenarios aren't covered?

4. **Generate Tests**
   - Create tests for the highest priority uncovered code
   - Follow our testing patterns in @tests/
```

**Usage**:
```
/check-coverage
```

### Example 4: Dependency Audit

**File**: `.claude/commands/audit-deps.md`

```markdown
---
description: Audit project dependencies for issues
allowed-tools: Bash(npm:*), Bash(pip:*)
---

## Dependency Status

### Outdated Packages:
[execute: npm outdated] or [execute: pip list --outdated]

### Security Vulnerabilities:
[execute: npm audit] or [execute: pip-audit]

### Dependency Tree (key packages):
[execute: npm list --depth=1] or [execute: pip show --verbose key-package]

## Analysis Task

Based on the dependency information:

1. **Security Assessment**
   - Critical vulnerabilities to address immediately
   - Medium/low priority items

2. **Update Strategy**
   - Safe updates (patch versions)
   - Potentially breaking updates (major versions)
   - Update order and approach

3. **Action Plan**
   - Commands to run
   - Testing needed after updates
   - Rollback plan if needed
```

**Usage**:
```
/audit-deps
```

### Example 5: PR Context Gatherer

**File**: `.claude/commands/pr-context.md`

```markdown
---
description: Gather context for creating a pull request
allowed-tools: Bash(git:*)
argument-hint: [base-branch]
---

## Current Branch

**Branch Name**: [execute: git branch --show-current]

**Base Branch**: $1

## Commit History

Commits to include in PR:
[execute: git log $1..HEAD --oneline]

## Full Diff

Changes in this PR:
[execute: git diff $1...HEAD --stat]

Detailed changes:
[execute: git diff $1...HEAD]

## PR Creation Task

Based on the changes above, create:

1. **PR Title**
   - Clear, descriptive
   - Follows our convention

2. **PR Description**
   - Summary of changes
   - Why these changes were made
   - Testing performed
   - Any breaking changes
   - Related issues

3. **Checklist**
   - [ ] Tests added/updated
   - [ ] Documentation updated
   - [ ] No breaking changes (or documented)
   - [ ] Ready for review
```

**Usage**:
```
/pr-context main
```

## Combining with Arguments

```markdown
---
description: Run specific test file
allowed-tools: Bash(npm:*), Bash(pytest:*)
argument-hint: [test-file]
---

## Running Test

[execute: npm test $1] or [execute: pytest $1 -v]

## Analysis

[Analyze the results...]
```

Usage: `/run-test tests/auth.test.js`

## Combining with File References

```markdown
---
description: Compare file with git history
allowed-tools: Bash(git:*)
argument-hint: [file-path]
---

## File History

Recent changes to @$1:
[execute: git log --oneline -5 -- $1]

## Current Content

@$1

## Diff from 10 commits ago

[execute: git diff HEAD~10 HEAD -- $1]

## Analysis

[Analyze how file evolved...]
```

## Common Bash Patterns

### Git Commands
```markdown
Current branch: [execute: git branch --show-current]
Status: [execute: git status --short]
Recent commits: [execute: git log --oneline -10]
Staged changes: [execute: git diff --staged]
Unstaged changes: [execute: git diff]
Changed files: [execute: git diff --name-only]
```

### File System
```markdown
List directory: [execute: ls -la src/]
Find files: [execute: find src -name "*.js"]
Count files: [execute: find src -name "*.test.js" | wc -l]
File size: [execute: du -sh src/]
```

### Testing
```markdown
Run tests: [execute: npm test]
Coverage: [execute: npm run coverage]
Specific test: [execute: npm test -- auth.test.js]
Verbose output: [execute: npm test -- --verbose]
```

### Dependencies
```markdown
List deps: [execute: npm list --depth=0]
Outdated: [execute: npm outdated]
Audit: [execute: npm audit]
Package info: [execute: npm info package-name]
```

### Build/Lint
```markdown
Build: [execute: npm run build]
Lint: [execute: npm run lint]
Type check: [execute: npm run type-check]
Format check: [execute: npm run format:check]
```

## Error Handling

If a bash command fails, its error output is included:

```markdown
Test results: [execute: npm test]
```

If tests fail, Claude sees the failure output and can analyze it.

## Best Practices

1. **Always include allowed-tools**
   ```yaml
   allowed-tools: Bash(git:*)
   ```

2. **Limit to necessary commands**
   ```yaml
   # Too broad
   allowed-tools: Bash

   # Better
   allowed-tools: Bash(git:*), Bash(npm test:*)
   ```

3. **Use 2>&1 to capture stderr**
   ```markdown
   [execute: npm test 2>&1]
   ```

4. **Test commands in terminal first**
   - Verify command works
   - Check output format
   - Ensure it's fast enough

5. **Structure output clearly**
   ```markdown
   ## Git Status
   [execute: git status]

   ## Recent Commits
   [execute: git log --oneline -5]
   ```

6. **Combine with file references**
   ```markdown
   Code: @src/file.js
   Tests: [execute: npm test src/file.test.js]
   ```

## Common Pitfalls

### Missing allowed-tools
```markdown
❌ [execute: git status]
   (without allowed-tools frontmatter)

✅
---
allowed-tools: Bash(git:*)
---
[execute: git status]
```

### Wrong syntax
```markdown
❌ !git status (missing backticks)
❌ `git status` (missing !)
✅ [execute: git status] (correct)
```

### Too broad permissions
```yaml
❌ allowed-tools: Bash
   (allows ANY command)

✅ allowed-tools: Bash(git:*), Bash(npm:*)
   (restricts to specific tools)
```

### Slow commands
```markdown
❌ [execute: npm install] (takes minutes)
❌ [execute: git log --all] (huge output)

✅ [execute: git status] (fast)
✅ [execute: git log --oneline -10] (limited)
```

## Testing Bash Commands

1. **Test command in terminal**
   ```bash
   git status --short
   ```

2. **Add to command file**
   ```markdown
   ---
   allowed-tools: Bash(git:*)
   ---
   Status: [execute: git status --short]
   ```

3. **Run the slash command**
   ```
   /your-command
   ```

4. **Verify output appears**
   - Check Claude received the output
   - Verify formatting is readable

## When to Move to Complex Template

If you also need:
- Arguments (dynamic inputs)
- File references (analyze files)
- All features combined

See [complex-command.md](complex-command.md) for template with all features.

---

**Remember**: Bash execution happens BEFORE Claude sees the prompt. Use it to gather dynamic context that makes your commands context-aware and intelligent.
