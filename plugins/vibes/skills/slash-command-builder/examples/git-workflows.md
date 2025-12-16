# Git Workflow Slash Command Examples

Real-world slash commands for common git operations.

## Example 1: Commit Message Generator

**File**: `.claude/commands/commit.md`

```markdown
---
description: Create git commit message with full context
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

Based on the staged changes above, create a git commit message that:

1. **Follows Conventional Commits format**:
   - feat: New feature
   - fix: Bug fix
   - docs: Documentation
   - refactor: Code restructuring
   - test: Testing
   - chore: Maintenance

2. **Matches our commit history style** (see recent commits above)

3. **Structure**:
   - Subject line: <type>: <description> (max 50 chars)
   - Blank line
   - Body: Explain what and why (wrap at 72 chars)
   - Blank line
   - Footer: Breaking changes, issue references

4. **Be specific**: Describe what changed and why it matters

Provide the commit message ready to use with `git commit -m "message"` or `git commit` (multiline).
```

**Usage**:
```bash
# Stage your changes
git add src/auth.js tests/auth.test.js

# Generate commit message
/commit

# Then use the generated message
git commit -m "feat: add JWT authentication

Implement JWT-based authentication to secure API endpoints.
Includes token generation, validation, and refresh logic.

Fixes #123"
```

---

## Example 2: PR Context Gatherer

**File**: `.claude/commands/pr-context.md`

```markdown
---
description: Gather context for creating a pull request
allowed-tools: Bash(git:*), Bash(gh:*)
argument-hint: [base-branch]
---

## Branch Information

**Current Branch**: [execute: git branch --show-current]
**Base Branch**: $1

## Commits in This PR

[execute: git log $1..HEAD --format="%h %s" --reverse]

## Files Changed

[execute: git diff --name-status $1...HEAD]

## Diff Statistics

[execute: git diff --stat $1...HEAD]

## Full Diff

[execute: git diff $1...HEAD]

## Related Open Issues

[execute: gh issue list --search "is:open" --limit 10 2>/dev/null || echo "gh CLI not available"]

## Project PR Template

@.github/pull_request_template.md

## Conventions

@CLAUDE.md

## Your Task

Create a pull request from current branch to $1:

### 1. PR Title
Suggest a clear, descriptive title following our convention.

### 2. PR Description

Generate a complete PR description including:

**Summary**
- What changed and why
- Key improvements or fixes

**Changes**
- Bullet list of significant changes
- Why each change was made

**Testing**
- How you verified it works
- Manual testing performed
- Automated tests added/updated

**Screenshots** (if UI changes)
- Note need for screenshots

**Breaking Changes** (if any)
- What breaks and why
- Migration guide

**Related Issues**
- Link to issues this addresses
- Use "Fixes #123", "Closes #456" format

### 3. GitHub CLI Command

Provide the complete command to create the PR:
```bash
gh pr create --base $1 --title "..." --body "..."
```

Or provide the description to paste in GitHub web UI.
```

**Usage**:
```
/pr-context main
```

---

## Example 3: Branch Status Checker

**File**: `.claude/commands/branch-status.md`

```markdown
---
description: Check branch status and suggest next actions
allowed-tools: Bash(git:*)
---

## Current Branch

**Name**: [execute: git branch --show-current]
**Upstream**: [execute: git rev-parse --abbrev-ref @{upstream} 2>/dev/null || echo "No upstream"]

## Sync Status

**Behind origin**: [execute: git rev-list --count HEAD..@{upstream} 2>/dev/null || echo "0"]
**Ahead of origin**: [execute: git rev-list --count @{upstream}..HEAD 2>/dev/null || echo "0"]

## Recent Activity

**Your recent commits**:
[execute: git log --oneline -10 --author="$(git config user.name)"]

**Others' recent commits on origin**:
[execute: git log --oneline -10 origin/$(git branch --show-current) 2>/dev/null || echo "No origin branch"]

## Local Changes

**Modified files**:
[execute: git status --short]

## Branch Age

**Created**: [execute: git log --reverse --format="%ar" | head -1]
**Last commit**: [execute: git log -1 --format="%ar"]

## Related Branches

**Other branches with similar names**:
[execute: git branch --list "*$(git branch --show-current | cut -d- -f1)*" | head -10]

## Analysis Task

Based on the status above:

### 1. Current State
- What's the branch doing?
- Is it in sync with origin?
- Any local changes?

### 2. Recommended Actions
- Should you pull from origin?
- Ready to push?
- Ready for PR?
- Conflicts to resolve?
- Should rebase on main?

### 3. Next Commands
Provide specific git commands to run:
```bash
# Example:
git pull origin main  # If behind
git push origin branch  # If ahead
git add . && git commit  # If changes
```

### 4. Warnings
- Is this a long-lived branch? (Consider merging/updating)
- Conflicts likely?
- Need to sync with main?
```

**Usage**:
```
/branch-status
```

---

## Example 4: Conflict Resolver Helper

**File**: `.claude/commands/resolve-conflicts.md`

```markdown
---
description: Help resolve merge conflicts with context
allowed-tools: Bash(git:*), Read, Grep, Glob
---

## Conflict Status

**Current operation**: [execute: git status | head -5]

**Conflicted files**:
[execute: git diff --name-only --diff-filter=U]

## Conflict Details

[execute: git diff --check]

## Incoming Changes

**Their commits** (what you're merging in):
[execute: git log --oneline HEAD..MERGE_HEAD 2>/dev/null || git log --oneline HEAD..REBASE_HEAD 2>/dev/null || echo "Not in merge/rebase"]

## Your Changes

**Your commits** (what they conflict with):
[execute: git log --oneline MERGE_HEAD..HEAD 2>/dev/null || git log --oneline REBASE_HEAD..HEAD 2>/dev/null || echo "Not in merge/rebase"]

## Project Merge Guidelines

@CLAUDE.md
@docs/merge-strategy.md

## For Each Conflicted File

[Loop through each file]:

### File: [filename]

**Current conflict markers**:
@[filename]

**Analysis**:
1. What does OURS (HEAD) do?
2. What does THEIRS (incoming) do?
3. Why do they conflict?
4. What's the correct resolution?
5. Are both changes needed?

**Recommended resolution**:
```language
[Show resolved code]
```

**Explanation**: Why this resolution is correct.

## Resolution Steps

1. **Edit conflicted files** with recommended resolutions
2. **Test after each resolution**: Ensure code works
3. **Mark as resolved**: `git add [file]`
4. **Continue operation**:
   - If merge: `git commit`
   - If rebase: `git rebase --continue`

## Conflict Prevention

How could this conflict have been avoided?
- Better communication?
- Smaller changes?
- More frequent syncing?
```

**Usage**:
```
# When you hit a conflict:
/resolve-conflicts
```

---

## Example 5: Rebase Interactive Helper

**File**: `.claude/commands/rebase-plan.md`

```markdown
---
description: Plan interactive rebase with commit analysis
allowed-tools: Bash(git:*)
argument-hint: [base-branch-or-commit]
---

## Rebase Context

**Current branch**: [execute: git branch --show-current]
**Rebase onto**: $1

## Commits to Rebase

[execute: git log $1..HEAD --oneline --reverse]

## Detailed Commit Info

[execute: git log $1..HEAD --format="%h %s%n  Author: %an <%ae>%n  Date: %ar%n" --reverse]

## File Changes Per Commit

[execute: git log $1..HEAD --format="%h %s" --name-status --reverse]

## Current Diff

**What will change overall**:
[execute: git diff $1...HEAD --stat]

## Rebase Planning Task

Based on the commits above, suggest an interactive rebase plan:

### 1. Commit Organization
- Which commits should be squashed together?
- Which should remain separate?
- Why?

### 2. Commit Message Improvements
- Which commit messages need editing?
- Suggested improved messages

### 3. Reordering
- Should any commits be reordered?
- Benefits of reordering

### 4. Potential Issues
- Conflicts likely?
- Tests might break during rebase?
- Considerations for each step

### 5. Rebase Commands

Provide the rebase command to start:
```bash
git rebase -i $1
```

Then show the suggested rebase plan in this format:
```
pick abc1234 commit message
squash def5678 related commit
reword ghi9012 commit with bad message
drop jkl3456 commit to remove
```

### 6. Testing Strategy
- When to run tests during rebase
- How to verify each step
- Rollback plan if needed
```

**Usage**:
```
/rebase-plan main
```

---

## Example 6: Stash Manager

**File**: `.claude/commands/stash-review.md`

```markdown
---
description: Review and manage git stash entries
allowed-tools: Bash(git:*)
---

## Stash List

[execute: git stash list]

## Stash Details

### Latest Stash (stash@{0}):
[execute: git stash show -p stash@{0} 2>/dev/null || echo "No stashes"]

### Second Latest (stash@{1}):
[execute: git stash show -p stash@{1} 2>/dev/null || echo "Only one stash"]

## Current Branch

**Branch**: [execute: git branch --show-current]
**Status**: [execute: git status --short]

## Analysis Task

Based on stash contents:

### 1. Stash Inventory
For each stash:
- What changes does it contain?
- Which branch was it created on?
- How old is it?
- Is it still relevant?

### 2. Recommendations
- Should any be applied now?
- Should any be dropped?
- Should any be turned into commits?
- Are there conflicts between stashes?

### 3. Actions

For each stash, suggest:
```bash
# Apply if needed:
git stash apply stash@{n}

# Apply and remove from stash list:
git stash pop stash@{n}

# Create a branch from stash:
git stash branch branch-name stash@{n}

# Drop if obsolete:
git stash drop stash@{n}
```

### 4. Stash Hygiene
- Clean up old stashes
- Document what remains
- Establish stashing strategy
```

**Usage**:
```
/stash-review
```

---

## Implementation Tips

1. **Test commands with real repos**
   - Use actual project data
   - Verify git commands work
   - Check output formatting

2. **Handle edge cases**
   - Empty git status
   - No commits yet
   - Detached HEAD
   - No remote configured

3. **Security with allowed-tools**
   ```yaml
   allowed-tools: Bash(git:*)  # Git only, no arbitrary bash
   ```

4. **Include project conventions**
   ```markdown
   @CLAUDE.md
   @.github/pull_request_template.md
   ```

5. **Provide ready-to-use commands**
   ```bash
   git commit -m "feat: add feature"
   gh pr create --base main --title "..."
   ```

---

These examples cover the most common git workflows. Adapt them to your team's specific conventions and processes!
