# Complex Slash Command Template

Combine all features: arguments, bash execution, file references, and tool restrictions.

## When to Use This Template

- Command needs multiple dynamic features
- Requires system context AND file analysis
- Needs structured inputs AND bash execution
- Security-sensitive operations requiring tool restrictions
- Production-ready commands with full functionality

## Complete Template Structure

```markdown
---
description: [Clear, descriptive summary for /help]
allowed-tools: [Minimal necessary tools for security]
argument-hint: [expected] [arguments] [here]
model: [optional-specific-model]
---

## Context Section

[Bash commands to gather current state]
[execute: bash commands here]

## Reference Materials

[File references to project conventions and examples]
@path/to/files

## Task Section

[Clear instructions using $ARGUMENTS or $1/$2/$3]

## Constraints

[Specific requirements, format, style]
```

## Complete Real-World Examples

### Example 1: Production-Ready PR Command

**File**: `.claude/commands/create-pr.md`

```markdown
---
description: Create pull request with full context and conventions
allowed-tools: Bash(git:*), Bash(gh:*), Read, Grep
argument-hint: [base-branch] [pr-title]
---

## Current Branch Context

**Branch**: [execute: git branch --show-current]
**Base**: $1
**Commits**: [execute: git log $1..HEAD --oneline]

## Changes Summary

**Files Changed**: [execute: git diff --name-status $1...HEAD]

**Diffstat**: [execute: git diff --stat $1...HEAD]

**Full Diff**:
[execute: git diff $1...HEAD]

## Project Conventions

@CLAUDE.md
@docs/pr-template.md

## Related Issues

Check for related issues: [execute: gh issue list --search "is:open" | head -10]

## Your Task

Create a pull request for merging current branch into $1:

**PR Title**: $2 (or suggest one if not provided)

**PR Description** should include:
1. **Summary**: What changed and why
2. **Changes**: Bullet list of key changes
3. **Testing**: How you verified it works
4. **Screenshots**: If UI changes (mention need for them)
5. **Breaking Changes**: Any API/interface changes
6. **Related Issues**: Link relevant issues

Follow our PR conventions in @docs/pr-template.md

**GitHub Command**:
Provide the complete `gh pr create` command to run.
```

**Usage**:
```
/create-pr main "feat: add user authentication"
```

### Example 2: Comprehensive Code Review

**File**: `.claude/commands/deep-review.md`

```markdown
---
description: Deep code review with context and conventions
allowed-tools: Bash(git:*), Read, Grep, Glob
argument-hint: [file-or-directory]
---

## Code to Review

@$1

## Git Context

**Recent Changes**:
[execute: git log --oneline -5 -- $1]

**Current Diff** (if modified):
[execute: git diff HEAD -- $1]

**File History Stats**:
[execute: git log --oneline --all -- $1 | wc -l] commits

## Project Standards

@CLAUDE.md
@docs/coding-standards.md
@.eslintrc.json

## Similar Well-Written Code

@src/examples/reference-implementation.js

## Related Tests

[execute: find . -name "*test*" -path "*$1*" 2>/dev/null | head -5]

## Deep Review Task

Perform comprehensive review of @$1:

### 1. Security Analysis
- Input validation and sanitization
- Authentication and authorization
- SQL injection / XSS risks
- Data exposure and privacy
- Dependency vulnerabilities

### 2. Performance Review
- Algorithm efficiency
- Database query optimization
- Memory management
- Caching opportunities
- Unnecessary computations

### 3. Code Quality
- Readability and clarity
- Naming conventions
- Function size and complexity
- Code duplication
- Comment quality

### 4. Architecture
- Separation of concerns
- Dependency management
- Coupling and cohesion
- Design patterns used
- Testability

### 5. Testing
- Test coverage
- Edge cases handled
- Error scenarios tested
- Integration test needs

### 6. Maintainability
- Documentation completeness
- Error messages clarity
- Logging appropriateness
- Future extensibility

### 7. Standards Compliance
- Follows project conventions
- Matches style guide
- Consistent with codebase patterns

For each issue found:
- Severity: Critical/High/Medium/Low
- Location: File and line number
- Problem: What's wrong and why
- Solution: Specific code fix with example
- Rationale: Why this improvement matters
```

**Usage**:
```
/deep-review src/api/payments.js
```

### Example 3: Full-Stack Feature Generator

**File**: `.claude/commands/gen-feature.md`

```markdown
---
description: Generate complete feature with all layers
allowed-tools: Bash(git:*), Read, Grep, Glob, Write
argument-hint: [feature-name] [description]
---

## Feature Requirements

**Name**: $1
**Description**: $2

## Current Codebase Structure

**API Endpoints**:
[execute: find src/api -name "*.js" | head -10]

**Database Models**:
[execute: find src/models -name "*.js" | head -10]

**Frontend Components**:
[execute: find src/components -name "*.jsx" | head -10]

## Project Patterns

**API Example**: @src/api/users.js
**Model Example**: @src/models/user.js
**Component Example**: @src/components/UserCard.jsx
**Test Example**: @tests/api/users.test.js

## Conventions

@CLAUDE.md
@docs/architecture.md

## Feature Generation Task

Create complete feature: $1 ($2)

Generate the following layers following our patterns:

### 1. Database Layer
- Model definition
- Migrations needed
- Indexes required
- Relationships

### 2. API Layer
- Endpoint definitions
- Request validation
- Response formatting
- Error handling

### 3. Business Logic
- Core feature logic
- Data transformations
- External integrations
- Validation rules

### 4. Frontend Layer (if applicable)
- Component structure
- State management
- API integration
- User interactions

### 5. Tests
- Unit tests for logic
- Integration tests for API
- Frontend component tests
- E2E scenarios

### 6. Documentation
- API documentation
- Component usage
- Configuration needs
- Deployment notes

For each file:
- Show complete code
- Explain key decisions
- Note any assumptions
- List TODOs if incomplete
```

**Usage**:
```
/gen-feature notifications "real-time user notifications via websockets"
```

### Example 4: Deployment Checklist Runner

**File**: `.claude/commands/pre-deploy.md`

```markdown
---
description: Run pre-deployment checklist and validation
allowed-tools: Bash(git:*), Bash(npm:*), Bash(pytest:*), Read, Grep, Glob
---

## Pre-Deployment Checklist

Running comprehensive checks...

### 1. Git Status

**Branch**: [execute: git branch --show-current]
**Uncommitted Changes**: [execute: git status --short]
**Unpushed Commits**: [execute: git log origin/main..HEAD --oneline]

### 2. Tests

**Test Results**:
[execute: npm test 2>&1 | tail -50] or [execute: pytest -v 2>&1 | tail -50]

### 3. Linting

**Lint Results**:
[execute: npm run lint 2>&1 | tail -30]

### 4. Type Checking

**Type Check**:
[execute: npm run type-check 2>&1 | tail -30]

### 5. Build

**Build Status**:
[execute: npm run build 2>&1 | tail -30]

### 6. Security Audit

**Security Issues**:
[execute: npm audit --production 2>&1 | head -50]

### 7. Dependencies

**Outdated Packages**:
[execute: npm outdated 2>&1 | head -20]

### 8. Environment Config

**Environment Variables** (@.env.example):
@.env.example

### 9. Migration Status

**Pending Migrations**:
[execute: npm run migrate:status 2>&1] or [execute: python manage.py showmigrations 2>&1]

### 10. Deployment Configuration

@deploy/config.yml
@Dockerfile

## Analysis Task

Based on all checks above:

### ✅ Ready to Deploy

List what's passing:
- All tests green
- No lint errors
- Build succeeds
- No critical security issues
- Migrations ready

### ⚠️ Warnings

List concerns that won't block deploy:
- Non-critical security updates
- Outdated non-critical dependencies
- Minor lint warnings

### ❌ Blockers

List issues that MUST be fixed:
- Failing tests
- Build failures
- Critical security vulnerabilities
- Uncommitted changes
- Missing environment variables

### 📋 Pre-Deploy Actions

Provide step-by-step commands to run before deploying:
1. [Command and explanation]
2. [Command and explanation]

### 🚀 Deployment Command

If ready, provide the deployment command:
```bash
[deployment command here]
```

### 🔄 Rollback Plan

Provide rollback commands if deployment fails:
```bash
[rollback commands]
```
```

**Usage**:
```
/pre-deploy
```

### Example 5: Debug Investigator

**File**: `.claude/commands/debug.md`

```markdown
---
description: Investigate bug with full context gathering
allowed-tools: Bash(git:*), Bash(npm:*), Bash(grep:*), Read, Grep, Glob
argument-hint: [error-description-or-file]
---

## Bug Description

$1

## System Context

**Git Branch**: [execute: git branch --show-current]
**Recent Changes**: [execute: git log --oneline -10]
**Modified Files**: [execute: git status --short]

## Search for Related Code

**Files mentioning the error**:
[execute: grep -r "$1" src/ 2>/dev/null | head -20]

## Recent Test Failures

[execute: npm test 2>&1 | grep -A 5 "FAIL|Error" | head -50]

## Application Logs

(If log file exists):
@logs/error.log
@logs/app.log

## Related Code Files

Based on error, check these files:
@src/[relevant-file].js

## Git History of Relevant Files

[execute: git log --oneline -10 -- src/[relevant-file].js]

## Recent Changes to Related Code

[execute: git diff HEAD~5 HEAD -- src/[relevant-file].js]

## Project Debugging Guide

@CLAUDE.md
@docs/debugging.md

## Investigation Task

Based on all context above:

### 1. Root Cause Analysis
- What is the actual error?
- Where does it occur?
- What triggers it?
- Why does it happen?

### 2. Impact Assessment
- What functionality is broken?
- How many users affected?
- Severity level?
- Workarounds available?

### 3. Recent Changes Analysis
- What changed recently in related code?
- Could any recent commit have caused this?
- Are there related issues?

### 4. Reproduction Steps
- How to consistently reproduce?
- Minimal reproduction case?
- Environment requirements?

### 5. Fix Approach
- What needs to change?
- Multiple possible solutions?
- Pros/cons of each approach?
- Recommended fix with code

### 6. Testing Strategy
- How to verify fix works?
- Test cases to add?
- Regression testing needed?

### 7. Prevention
- How to prevent this in the future?
- What tests were missing?
- What guards should be added?
```

**Usage**:
```
/debug "TypeError: Cannot read property 'id' of undefined in user login"
```

## Template Best Practices

### 1. Structure with Clear Sections

```markdown
## Context
[Gather state]

## Reference
[Include files/examples]

## Task
[Clear instructions]

## Constraints
[Requirements]
```

### 2. Security via allowed-tools

```yaml
# Minimal permissions
allowed-tools: Read, Grep, Glob

# Specific operations
allowed-tools: Bash(git:*), Bash(npm test:*)

# Avoid overly broad
allowed-tools: Bash  # Too much access
```

### 3. Combine Features Logically

```markdown
# Bash for context
Branch: [execute: git branch --show-current]

# Files for analysis
Code: @$1

# Arguments for flexibility
Review $1 focusing on $2
```

### 4. Progressive Information

Start with summary, drill into details:

```markdown
## Quick Context
[Essential info]

## Detailed Context
[Full details]

## Task
[What to do with all this context]
```

### 5. Error Handling

```markdown
Check if file exists first:
[execute: [ -f "$1" ] && echo "exists" || echo "missing"]

Then reference:
@$1
```

## Testing Complex Commands

1. **Test each feature separately**
   - Arguments work?
   - Bash executes?
   - Files load?

2. **Test feature combinations**
   - Arguments + bash
   - Bash + files
   - All together

3. **Test error cases**
   - Missing arguments
   - File not found
   - Bash command fails

4. **Test with real scenarios**
   - Use actual project data
   - Verify output quality
   - Check performance

## When You Have Too Much Complexity

If your command is becoming unwieldy:

1. **Split into multiple commands**
   - `/prep-pr` gathers context
   - `/create-pr` generates PR

2. **Consider a Skill instead**
   - Multiple files with scripts
   - Complex workflows
   - See `skill-builder` Skill

3. **Use supporting scripts**
   - Bash script for complex logic
   - Call script from command: [execute: ./scripts/analyze.sh $1]

## Common Patterns

### Pattern: Analyze → Suggest → Implement

```markdown
## Analysis
[Bash + Files to understand current state]

## Suggestions
Based on analysis, suggest improvements

## Implementation
Provide code/commands to implement
```

### Pattern: Gather → Compare → Recommend

```markdown
## Current State
[Bash commands for current state]

## Desired State
[Files showing target patterns]

## Gap Analysis
What's different? What needs to change?
```

### Pattern: Check → Validate → Fix

```markdown
## Checks
[Run validation commands]

## Issues Found
Analyze failures

## Fixes
Provide specific fixes for each issue
```

---

**Remember**: Complex commands are powerful but harder to maintain. Start simple, add complexity only when needed, and consider creating a Skill if you need even more features.
