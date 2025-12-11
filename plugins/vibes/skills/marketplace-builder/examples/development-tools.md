# Development Tools Marketplace Examples

Six complete plugin examples for common development workflows.

---

## Example 1: Git Workflow Plugin

A comprehensive git workflow automation plugin.

### Plugin Structure

```
git-workflow/
├── .claude-plugin/
│   └── plugin.json
├── commands/
│   ├── smart-commit.md
│   ├── branch-create.md
│   └── pr-prepare.md
└── agents/
    └── commit-analyzer.md
```

### .claude-plugin/plugin.json

```json
{
  "name": "git-workflow",
  "description": "Git workflow automation: smart commits, branch management, PR preparation",
  "version": "2.0.0",
  "author": {
    "name": "DevTools Team",
    "email": "devtools@example.com"
  },
  "repository": "https://github.com/devtools/git-workflow",
  "license": "MIT",
  "keywords": ["git", "workflow", "commits", "branches", "pull-requests"]
}
```

### commands/smart-commit.md

```markdown
---
description: Create a smart commit with conventional commit message
allowed-tools: Bash(git:*), Read
argument-hint: [type] (feat|fix|docs|style|refactor|test|chore)
---

Create a commit with type: $ARGUMENTS

## Steps

1. Run `git status` to see changes
2. Run `git diff --staged` to see staged changes (or `git diff` if nothing staged)
3. Analyze the changes to understand what was modified
4. Generate a conventional commit message:
   - Format: `type(scope): description`
   - Types: feat, fix, docs, style, refactor, test, chore
   - Scope: affected component or area
   - Description: concise summary (50 chars max)
5. Show the proposed commit message
6. If user approves, create the commit

## Example Output

```
Proposed commit:
feat(auth): add password reset functionality

Changes included:
- src/auth/reset.ts (new file)
- src/auth/routes.ts (modified)
- tests/auth/reset.test.ts (new file)

Proceed with commit? [Y/n]
```
```

### commands/branch-create.md

```markdown
---
description: Create a new branch with naming convention
allowed-tools: Bash(git:*)
argument-hint: [type/description] (e.g., feature/user-auth)
---

Create and checkout new branch: $ARGUMENTS

## Naming Convention

- `feature/` - New features
- `fix/` - Bug fixes
- `hotfix/` - Urgent production fixes
- `refactor/` - Code refactoring
- `docs/` - Documentation updates
- `test/` - Test additions/changes

## Steps

1. Validate branch name format
2. Fetch latest from origin
3. Create branch from main/master
4. Push branch with upstream tracking
5. Confirm branch creation

## Output

```
✅ Created branch: feature/user-authentication
   Based on: main (up to date)
   Tracking: origin/feature/user-authentication

Ready to start development!
```
```

### agents/commit-analyzer.md

```markdown
---
name: commit-analyzer
description: Analyzes git history and commit patterns. Use when reviewing commit history, understanding changes, or preparing release notes. Triggers: "analyze commits", "commit history", "what changed"
tools: Bash(git log:*, git diff:*, git show:*)
model: inherit
---

You are a git historian analyzing commit patterns and changes.

## When Invoked

1. Determine the scope of analysis:
   - Recent commits (default: last 10)
   - Date range
   - Specific files/directories
   - Between tags/releases
2. Analyze commit patterns
3. Identify themes and contributors
4. Generate summary

## Output Format

### Commit Analysis

**Period**: [date range or commit range]
**Total Commits**: X

#### By Type
| Type | Count | Percentage |
|------|-------|------------|
| feat | X | X% |
| fix | X | X% |

#### By Author
| Author | Commits | Lines Changed |
|--------|---------|---------------|

#### Key Changes
- [Major change 1]
- [Major change 2]

#### Release Notes Draft
[Auto-generated release notes from commits]
```

### Marketplace Entry

```json
{
  "name": "git-workflow",
  "source": {"source": "github", "repo": "devtools/git-workflow"},
  "description": "Git workflow automation: smart commits, branch management, PR preparation",
  "version": "2.0.0",
  "author": {"name": "DevTools Team"},
  "commands": ["./commands/"],
  "agents": ["./agents/commit-analyzer.md"]
}
```

---

## Example 2: Code Formatter Plugin

Universal code formatting across multiple languages.

### Plugin Structure

```
code-formatter/
├── .claude-plugin/
│   └── plugin.json
├── commands/
│   ├── format.md
│   ├── format-check.md
│   └── format-config.md
└── hooks/
    └── hooks.json
```

### .claude-plugin/plugin.json

```json
{
  "name": "code-formatter",
  "description": "Universal code formatting: auto-detect language, consistent styling",
  "version": "1.5.0",
  "author": {"name": "Format Team"},
  "license": "MIT"
}
```

### commands/format.md

```markdown
---
description: Format code files (auto-detects language and formatter)
allowed-tools: Bash(npx:*, prettier:*, black:*, gofmt:*, rustfmt:*), Read, Write, Glob
argument-hint: [path] (file or directory, defaults to .)
---

Format code in: $ARGUMENTS

## Supported Languages & Formatters

| Language | Formatter | Config File |
|----------|-----------|-------------|
| JS/TS | Prettier | .prettierrc |
| Python | Black | pyproject.toml |
| Go | gofmt | - |
| Rust | rustfmt | rustfmt.toml |
| CSS/SCSS | Prettier | .prettierrc |
| JSON/YAML | Prettier | .prettierrc |
| Markdown | Prettier | .prettierrc |

## Steps

1. Detect files to format (by extension)
2. Identify appropriate formatter for each
3. Run formatter with project config (or defaults)
4. Report results

## Output

### Formatting Complete

| Language | Files | Modified |
|----------|-------|----------|
| TypeScript | 15 | 3 |
| Python | 8 | 2 |
| JSON | 5 | 0 |

**Total**: 28 files checked, 5 modified
```

### hooks/hooks.json

```json
{
  "hooks": [
    {
      "matcher": {
        "event": "post-tool-use",
        "tool": "Write"
      },
      "hooks": [
        {
          "type": "command",
          "command": "FILE=$(echo $TOOL_INPUT | jq -r '.file_path'); EXT=\"${FILE##*.}\"; if [[ \"$EXT\" =~ ^(ts|js|tsx|jsx|css|json)$ ]]; then npx prettier --write \"$FILE\" 2>/dev/null && echo '✨ Auto-formatted'; fi"
        }
      ]
    }
  ]
}
```

### Marketplace Entry

```json
{
  "name": "code-formatter",
  "source": {"source": "github", "repo": "devtools/code-formatter"},
  "description": "Universal code formatting: auto-detect language, consistent styling",
  "version": "1.5.0",
  "commands": ["./commands/"],
  "hooks": "./hooks/hooks.json"
}
```

---

## Example 3: Test Runner Plugin

Comprehensive testing toolkit.

### Plugin Structure

```
test-runner/
├── .claude-plugin/
│   └── plugin.json
├── commands/
│   ├── test.md
│   ├── test-watch.md
│   └── coverage.md
└── agents/
    └── test-helper.md
```

### .claude-plugin/plugin.json

```json
{
  "name": "test-runner",
  "description": "Testing toolkit: run tests, watch mode, coverage reports, test generation",
  "version": "3.0.0",
  "author": {"name": "Testing Guild"},
  "license": "MIT"
}
```

### commands/test.md

```markdown
---
description: Run tests with smart detection of test framework
allowed-tools: Bash(npm:*, npx:*, pytest:*, go:*, cargo:*), Read
argument-hint: [pattern] (optional file/test pattern)
---

Run tests matching: $ARGUMENTS

## Framework Detection

Checks for:
- `jest.config.*` or `package.json` jest key → Jest
- `vitest.config.*` → Vitest
- `pytest.ini`, `pyproject.toml [tool.pytest]` → pytest
- `*_test.go` → go test
- `Cargo.toml` → cargo test

## Steps

1. Detect test framework
2. Run tests with specified pattern (or all)
3. Parse results
4. Provide summary with actionable insights

## Output

### Test Results

**Framework**: Jest
**Status**: ✅ PASSED

| Suite | Tests | Passed | Failed | Skipped |
|-------|-------|--------|--------|---------|
| auth | 12 | 12 | 0 | 0 |
| api | 25 | 24 | 1 | 0 |

**Coverage**: 85.2%

### Failed Tests
```
FAIL api/users.test.ts
  ✕ should return 404 for unknown user (15ms)
    Expected: 404
    Received: 500
```

### Recommendations
- Fix the 500 error in user lookup
- Consider adding error boundary tests
```

### agents/test-helper.md

```markdown
---
name: test-helper
description: Helps write and debug tests. Use when creating new tests, fixing failing tests, or improving coverage. Triggers: "write test", "test for", "fix test", "improve coverage"
tools: Read, Write, Grep, Glob
model: inherit
---

You are a testing expert who writes thorough, maintainable tests.

## When Invoked

1. Understand what needs testing
2. Read the implementation code
3. Identify test scenarios:
   - Happy path
   - Edge cases
   - Error conditions
   - Boundary values
4. Write tests following project patterns
5. Ensure proper assertions

## Testing Principles

- **Arrange-Act-Assert** pattern
- **One assertion focus** per test (mostly)
- **Descriptive names**: `should [expected] when [condition]`
- **Isolated tests**: no dependencies between tests
- **Fast tests**: mock external services

## Output

Generate test file with:
1. Import statements
2. Test suite structure
3. Setup/teardown if needed
4. Individual test cases
5. Comprehensive assertions
```

### Marketplace Entry

```json
{
  "name": "test-runner",
  "source": {"source": "github", "repo": "devtools/test-runner"},
  "description": "Testing toolkit: run tests, watch mode, coverage reports, test generation",
  "version": "3.0.0",
  "commands": ["./commands/"],
  "agents": ["./agents/test-helper.md"]
}
```

---

## Example 4: Dependency Manager Plugin

Manage project dependencies safely.

### Plugin Structure

```
dependency-manager/
├── .claude-plugin/
│   └── plugin.json
├── commands/
│   ├── deps-audit.md
│   ├── deps-update.md
│   └── deps-why.md
└── agents/
    └── deps-advisor.md
```

### .claude-plugin/plugin.json

```json
{
  "name": "dependency-manager",
  "description": "Dependency management: security audits, updates, impact analysis",
  "version": "2.1.0",
  "author": {"name": "Security Team"},
  "license": "MIT"
}
```

### commands/deps-audit.md

```markdown
---
description: Audit dependencies for security vulnerabilities
allowed-tools: Bash(npm:*, npx:*, pip-audit:*, cargo:*), Read
---

Audit project dependencies for known vulnerabilities.

## Supported Package Managers

- npm/yarn/pnpm → `npm audit`
- pip → `pip-audit`
- cargo → `cargo audit`
- go → `govulncheck`

## Steps

1. Detect package manager
2. Run security audit
3. Parse and categorize findings
4. Provide remediation guidance

## Output

### Security Audit Report

**Total Vulnerabilities**: X

#### Critical (Immediate Action Required)
| Package | Version | Vulnerability | Fix |
|---------|---------|---------------|-----|
| lodash | 4.17.15 | CVE-2021-23337 | 4.17.21 |

#### High Priority
| Package | Version | Vulnerability | Fix |
|---------|---------|---------------|-----|

#### Medium/Low
[Summary count]

### Remediation Commands
```bash
npm update lodash
npm audit fix
```

### Breaking Changes Warning
- lodash 4.17.21: No breaking changes
```

### commands/deps-update.md

```markdown
---
description: Update dependencies with safety checks
allowed-tools: Bash(npm:*, yarn:*, pip:*), Read, Write
argument-hint: [package] (optional, updates all if not specified)
---

Update dependencies: $ARGUMENTS

## Update Strategy

1. **Patch updates**: Apply automatically (bug fixes)
2. **Minor updates**: Apply with test verification
3. **Major updates**: Show changelog, require confirmation

## Steps

1. Check current versions
2. Find available updates
3. Categorize by semver change
4. Show impact analysis
5. Apply updates (with user confirmation for major)
6. Run tests to verify

## Output

### Update Plan

| Package | Current | Latest | Change | Risk |
|---------|---------|--------|--------|------|
| react | 18.2.0 | 18.3.0 | Minor | Low |
| typescript | 4.9.5 | 5.3.0 | Major | Medium |

### Major Update Details

**typescript 4.9.5 → 5.3.0**
- Breaking: `--moduleResolution bundler` behavior changed
- New: `satisfies` operator improvements
- [Changelog link]

Proceed with updates? [y/N]
```

### Marketplace Entry

```json
{
  "name": "dependency-manager",
  "source": {"source": "github", "repo": "devtools/dependency-manager"},
  "description": "Dependency management: security audits, updates, impact analysis",
  "version": "2.1.0",
  "commands": ["./commands/"],
  "agents": ["./agents/deps-advisor.md"]
}
```

---

## Example 5: Documentation Generator Plugin

Auto-generate and maintain documentation.

### Plugin Structure

```
doc-generator/
├── .claude-plugin/
│   └── plugin.json
├── commands/
│   ├── docs-generate.md
│   ├── docs-api.md
│   └── readme-update.md
└── skills/
    └── documentation/
        └── SKILL.md
```

### .claude-plugin/plugin.json

```json
{
  "name": "doc-generator",
  "description": "Documentation generation: API docs, README updates, code documentation",
  "version": "1.8.0",
  "author": {"name": "Docs Team"},
  "license": "MIT"
}
```

### commands/docs-generate.md

```markdown
---
description: Generate documentation for code
allowed-tools: Read, Write, Glob, Grep
argument-hint: [path] (file or directory)
---

Generate documentation for: $ARGUMENTS

## Documentation Types

- **JSDoc/TSDoc**: For JavaScript/TypeScript
- **Docstrings**: For Python
- **GoDoc**: For Go
- **Rustdoc**: For Rust

## Steps

1. Analyze code structure
2. Identify undocumented items:
   - Functions/methods
   - Classes/types
   - Exports/public API
3. Generate appropriate documentation
4. Add to files

## Output

### Documentation Added

| File | Items Documented |
|------|------------------|
| src/auth.ts | 5 functions |
| src/types.ts | 3 interfaces |

### Example Generated Doc

```typescript
/**
 * Authenticates a user with the provided credentials.
 *
 * @param username - The user's username or email
 * @param password - The user's password
 * @returns A promise resolving to the authenticated user object
 * @throws {AuthenticationError} If credentials are invalid
 *
 * @example
 * const user = await authenticate('john@example.com', 'secret123');
 * console.log(user.id);
 */
```
```

### skills/documentation/SKILL.md

```markdown
---
name: documentation
description: Documentation best practices and standards. Use when writing or reviewing documentation. Triggers: "document", "documentation", "README", "API docs"
---

# Documentation Standards

## README Structure

1. **Title and Description**
2. **Installation**
3. **Quick Start**
4. **Usage Examples**
5. **API Reference** (or link)
6. **Configuration**
7. **Contributing**
8. **License**

## Code Documentation

### Functions
- Purpose (what, not how)
- Parameters with types
- Return value
- Exceptions/errors
- Usage example

### Classes
- Purpose
- Constructor params
- Public methods
- Usage example

## Best Practices

- Write for your future self
- Include examples
- Keep in sync with code
- Link to related docs
```

### Marketplace Entry

```json
{
  "name": "doc-generator",
  "source": {"source": "github", "repo": "devtools/doc-generator"},
  "description": "Documentation generation: API docs, README updates, code documentation",
  "version": "1.8.0",
  "commands": ["./commands/"],
  "skills": {"documentation": "./skills/documentation"}
}
```

---

## Example 6: Code Quality Plugin

Comprehensive code quality analysis.

### Plugin Structure

```
code-quality/
├── .claude-plugin/
│   └── plugin.json
├── commands/
│   ├── quality-check.md
│   ├── complexity.md
│   └── duplication.md
└── agents/
    └── quality-advisor.md
```

### .claude-plugin/plugin.json

```json
{
  "name": "code-quality",
  "description": "Code quality analysis: complexity metrics, duplication detection, maintainability scores",
  "version": "2.5.0",
  "author": {"name": "Quality Guild"},
  "license": "MIT"
}
```

### commands/quality-check.md

```markdown
---
description: Comprehensive code quality analysis
allowed-tools: Read, Grep, Glob, Bash(npx:*)
argument-hint: [path] (defaults to src/)
---

Analyze code quality in: $ARGUMENTS

## Metrics Checked

### Complexity
- Cyclomatic complexity
- Cognitive complexity
- Nesting depth

### Maintainability
- Function length
- File length
- Parameter count

### Code Smells
- Duplicate code
- Long methods
- Large classes
- Too many parameters

## Output

### Code Quality Report

**Overall Score**: B (78/100)

#### Complexity Analysis
| File | Cyclomatic | Cognitive | Rating |
|------|------------|-----------|--------|
| auth.ts | 12 | 8 | ⚠️ Medium |
| utils.ts | 5 | 3 | ✅ Good |

#### Code Smells
- **Long Method**: `processOrder()` (150 lines) → Consider splitting
- **Duplicate Code**: 3 instances in api/ → Extract to shared utility

#### Recommendations
1. Refactor `auth.ts:processLogin` (complexity 15)
2. Extract duplicate validation logic
3. Break down `OrderService` class
```

### agents/quality-advisor.md

```markdown
---
name: quality-advisor
description: Code quality expert providing refactoring advice. Use when improving code quality, reducing complexity, or addressing tech debt. Triggers: "improve quality", "refactor", "reduce complexity", "tech debt"
tools: Read, Grep, Glob
model: sonnet
---

You are a code quality expert specializing in clean code principles.

## When Invoked

1. Analyze the code structure
2. Identify quality issues:
   - High complexity
   - Code duplication
   - Poor naming
   - Missing abstractions
   - SOLID violations
3. Prioritize improvements
4. Provide specific refactoring suggestions

## Quality Principles

### SOLID
- **S**ingle Responsibility
- **O**pen/Closed
- **L**iskov Substitution
- **I**nterface Segregation
- **D**ependency Inversion

### Clean Code
- Meaningful names
- Small functions
- One level of abstraction
- DRY (Don't Repeat Yourself)
- Minimal comments (self-documenting code)

## Output Format

### Quality Analysis

**Current State**: [Assessment]

#### High Priority Refactoring
1. [Issue]: [Specific location]
   - Problem: [Description]
   - Suggestion: [How to fix]
   - Effort: [Low/Medium/High]

#### Code Improvement Plan
1. [Step 1]
2. [Step 2]
3. [Step 3]
```

### Marketplace Entry

```json
{
  "name": "code-quality",
  "source": {"source": "github", "repo": "devtools/code-quality"},
  "description": "Code quality analysis: complexity metrics, duplication detection, maintainability scores",
  "version": "2.5.0",
  "commands": ["./commands/"],
  "agents": ["./agents/quality-advisor.md"]
}
```

---

## Complete Marketplace Configuration

### marketplace.json

```json
{
  "name": "development-tools",
  "owner": {
    "name": "DevTools Community",
    "email": "devtools@example.com"
  },
  "metadata": {
    "description": "Essential development tools for productive coding",
    "version": "6.0.0"
  },
  "plugins": [
    {
      "name": "git-workflow",
      "source": {"source": "github", "repo": "devtools/git-workflow"},
      "description": "Git workflow automation: smart commits, branch management, PR preparation",
      "version": "2.0.0"
    },
    {
      "name": "code-formatter",
      "source": {"source": "github", "repo": "devtools/code-formatter"},
      "description": "Universal code formatting: auto-detect language, consistent styling",
      "version": "1.5.0"
    },
    {
      "name": "test-runner",
      "source": {"source": "github", "repo": "devtools/test-runner"},
      "description": "Testing toolkit: run tests, watch mode, coverage reports",
      "version": "3.0.0"
    },
    {
      "name": "dependency-manager",
      "source": {"source": "github", "repo": "devtools/dependency-manager"},
      "description": "Dependency management: security audits, updates, impact analysis",
      "version": "2.1.0"
    },
    {
      "name": "doc-generator",
      "source": {"source": "github", "repo": "devtools/doc-generator"},
      "description": "Documentation generation: API docs, README updates",
      "version": "1.8.0"
    },
    {
      "name": "code-quality",
      "source": {"source": "github", "repo": "devtools/code-quality"},
      "description": "Code quality analysis: complexity, duplication, maintainability",
      "version": "2.5.0"
    }
  ]
}
```
