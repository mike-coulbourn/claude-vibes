# Multi-Plugin Marketplace Template (Monorepo Pattern)

Multiple plugins in a single repository, managed together.

---

## When to Use

- Multiple related plugins under unified ownership
- Team tools that should be versioned together
- Easier management with single repo
- Shared development infrastructure

---

## Directory Structure

```
company-plugins/
├── .claude-plugin/
│   └── marketplace.json        # Marketplace catalog
├── plugins/
│   ├── formatter/
│   │   ├── .claude-plugin/
│   │   │   └── plugin.json
│   │   └── commands/
│   │       └── format.md
│   ├── linter/
│   │   ├── .claude-plugin/
│   │   │   └── plugin.json
│   │   └── commands/
│   │       └── lint.md
│   └── tester/
│       ├── .claude-plugin/
│       │   └── plugin.json
│       ├── commands/
│       │   └── test.md
│       └── agents/
│           └── test-analyzer.md
└── README.md
```

---

## Step-by-Step Setup

### Step 1: Create Directory Structure

```bash
mkdir -p company-plugins/.claude-plugin
mkdir -p company-plugins/plugins/formatter/.claude-plugin
mkdir -p company-plugins/plugins/formatter/commands
mkdir -p company-plugins/plugins/linter/.claude-plugin
mkdir -p company-plugins/plugins/linter/commands
mkdir -p company-plugins/plugins/tester/.claude-plugin
mkdir -p company-plugins/plugins/tester/{commands,agents}
```

### Step 2: Create Marketplace JSON

Create `company-plugins/.claude-plugin/marketplace.json`:

```json
{
  "name": "company-tools",
  "owner": {
    "name": "Company Dev Team",
    "email": "devtools@company.com"
  },
  "metadata": {
    "description": "Company development tools collection",
    "version": "2.0.0",
    "pluginRoot": "./plugins"
  },
  "plugins": [
    {
      "name": "formatter",
      "source": "./plugins/formatter",
      "description": "Code formatting tools for multiple languages",
      "version": "1.2.0",
      "author": {"name": "Dev Team"}
    },
    {
      "name": "linter",
      "source": "./plugins/linter",
      "description": "Linting and static analysis tools",
      "version": "1.1.0",
      "author": {"name": "Dev Team"}
    },
    {
      "name": "tester",
      "source": "./plugins/tester",
      "description": "Testing utilities and test analysis",
      "version": "1.0.0",
      "author": {"name": "Dev Team"}
    }
  ]
}
```

### Step 3: Create Plugin Manifests

**plugins/formatter/.claude-plugin/plugin.json**:
```json
{
  "name": "formatter",
  "description": "Code formatting tools for multiple languages",
  "version": "1.2.0",
  "author": {
    "name": "Company Dev Team",
    "email": "devtools@company.com"
  },
  "repository": "https://github.com/company/company-plugins",
  "license": "MIT"
}
```

**plugins/linter/.claude-plugin/plugin.json**:
```json
{
  "name": "linter",
  "description": "Linting and static analysis tools",
  "version": "1.1.0",
  "author": {
    "name": "Company Dev Team",
    "email": "devtools@company.com"
  },
  "repository": "https://github.com/company/company-plugins",
  "license": "MIT"
}
```

**plugins/tester/.claude-plugin/plugin.json**:
```json
{
  "name": "tester",
  "description": "Testing utilities and test analysis",
  "version": "1.0.0",
  "author": {
    "name": "Company Dev Team",
    "email": "devtools@company.com"
  },
  "repository": "https://github.com/company/company-plugins",
  "license": "MIT"
}
```

### Step 4: Create Plugin Components

**plugins/formatter/commands/format.md**:
```markdown
---
description: Format code files using project-configured formatter
allowed-tools: Bash(npx:*, prettier:*, black:*, gofmt:*), Read, Write
argument-hint: [file-or-directory]
---

Format code in: $ARGUMENTS (defaults to current directory if not specified)

## Steps

1. Detect project type from config files:
   - `.prettierrc` / `package.json` → Prettier
   - `pyproject.toml` / `setup.py` → Black
   - `go.mod` → gofmt
2. Run the appropriate formatter
3. Report files modified

## Output

### Formatting Complete

**Formatter**: [detected formatter]
**Files Modified**: X

| File | Status |
|------|--------|
| path/file.ts | Formatted |
| path/other.ts | No changes |
```

**plugins/linter/commands/lint.md**:
```markdown
---
description: Run linting checks and report issues
allowed-tools: Bash(npx:*, eslint:*, ruff:*, golint:*), Read, Glob
argument-hint: [file-or-directory]
---

Lint code in: $ARGUMENTS (defaults to current directory if not specified)

## Steps

1. Detect project type and linter configuration
2. Run appropriate linter with JSON output if available
3. Parse and categorize issues by severity
4. Provide summary and actionable recommendations

## Output Format

### Lint Results

**Total**: X errors, Y warnings, Z info

#### Errors (Must Fix)
- `file.ts:10` - [error message]

#### Warnings (Should Fix)
- `file.ts:20` - [warning message]

### Auto-Fix Available
Run `/lint-fix` to automatically fix X issues.
```

**plugins/tester/commands/test.md**:
```markdown
---
description: Run tests and analyze results
allowed-tools: Bash(npm test:*, npx:*, pytest:*, go test:*), Read
argument-hint: [test-pattern]
---

Run tests matching: $ARGUMENTS (runs all tests if not specified)

## Steps

1. Detect test framework:
   - `jest.config.*` → Jest
   - `pytest.ini` / `conftest.py` → pytest
   - `*_test.go` → go test
2. Run tests with coverage if available
3. Analyze failures and provide insights

## Output

### Test Results

**Status**: PASSED / FAILED
**Passed**: X | **Failed**: Y | **Skipped**: Z
**Coverage**: XX%

### Failed Tests
| Test | Error |
|------|-------|
| test_name | AssertionError: ... |

### Analysis
[Insights about failures and potential fixes]
```

**plugins/tester/agents/test-analyzer.md**:
```markdown
---
name: test-analyzer
description: Analyzes test failures and suggests fixes. Use when tests fail or when debugging test issues. Triggers: "test failed", "fix test", "test analysis"
tools: Read, Grep, Glob
model: inherit
---

You are an expert at debugging test failures.

## When Invoked

1. Identify the failing tests and error messages
2. Read the test file and implementation being tested
3. Analyze the failure:
   - Is the test wrong?
   - Is the implementation wrong?
   - Is there a configuration issue?
4. Suggest specific fixes

## Output Format

### Test Failure Analysis

**Test**: [test name]
**Error Type**: [assertion / exception / timeout / etc.]

### Root Cause
[Explanation of why the test is failing]

### Diagnosis
- [ ] Test expectation is incorrect
- [ ] Implementation has a bug
- [ ] Test setup is wrong
- [ ] Configuration issue

### Recommended Fix

```[language]
// Suggested code change
```

### Verification
Steps to verify the fix works.
```

---

## Complete Working Example

### Marketplace: Development Toolbox

A complete monorepo marketplace with three plugins:

```
dev-toolbox/
├── .claude-plugin/
│   └── marketplace.json
├── plugins/
│   ├── git-tools/
│   │   ├── .claude-plugin/plugin.json
│   │   ├── commands/
│   │   │   ├── commit.md
│   │   │   ├── pr-create.md
│   │   │   └── branch-cleanup.md
│   │   └── agents/
│   │       └── commit-reviewer.md
│   ├── doc-tools/
│   │   ├── .claude-plugin/plugin.json
│   │   ├── commands/
│   │   │   ├── generate-docs.md
│   │   │   └── update-readme.md
│   │   └── skills/
│   │       └── documentation/SKILL.md
│   └── deploy-tools/
│       ├── .claude-plugin/plugin.json
│       ├── commands/
│       │   ├── deploy-staging.md
│       │   └── deploy-prod.md
│       └── hooks/
│           └── hooks.json
└── README.md
```

### .claude-plugin/marketplace.json

```json
{
  "name": "dev-toolbox",
  "owner": {
    "name": "DevOps Team",
    "email": "devops@company.com"
  },
  "metadata": {
    "description": "Complete development toolbox: git workflows, documentation, deployment",
    "version": "3.0.0",
    "pluginRoot": "./plugins"
  },
  "plugins": [
    {
      "name": "git-tools",
      "source": "./plugins/git-tools",
      "description": "Git workflow automation: smart commits, PR creation, branch management",
      "version": "2.1.0",
      "author": {"name": "DevOps Team"},
      "commands": ["./commands/"],
      "agents": ["./agents/commit-reviewer.md"]
    },
    {
      "name": "doc-tools",
      "source": "./plugins/doc-tools",
      "description": "Documentation generation and maintenance tools",
      "version": "1.5.0",
      "author": {"name": "DevOps Team"},
      "commands": ["./commands/"],
      "skills": {"documentation": "./skills/documentation"}
    },
    {
      "name": "deploy-tools",
      "source": "./plugins/deploy-tools",
      "description": "Deployment commands with safety checks and rollback support",
      "version": "1.0.0",
      "author": {"name": "DevOps Team"},
      "commands": ["./commands/"],
      "hooks": "./hooks/hooks.json"
    }
  ]
}
```

---

## Managing Monorepo Plugins

### Version Strategy

**Option A: Synchronized Versions**
All plugins share the same version. Update all together.
- Simpler to manage
- Clear release cadence
- May force unnecessary updates

**Option B: Independent Versions**
Each plugin has its own version. Update individually.
- More precise tracking
- Avoid unnecessary updates
- More version numbers to track

### Recommended: Independent with Marketplace Version

- Each plugin: own semantic version
- Marketplace metadata.version: increment when adding/removing plugins

### Adding a New Plugin

1. Create plugin directory with structure
2. Add plugin.json
3. Add components
4. Add entry to marketplace.json plugins array
5. Increment marketplace metadata.version
6. Test with `claude plugin validate .`

### Removing a Plugin

1. Remove plugin entry from marketplace.json
2. Keep or delete plugin directory
3. Increment marketplace metadata.version
4. Notify users of deprecation

### Updating a Plugin

1. Make changes to plugin
2. Increment plugin version in both:
   - plugins/NAME/.claude-plugin/plugin.json
   - .claude-plugin/marketplace.json plugins entry
3. Users run `/plugin marketplace update` to see new version

---

## Team Configuration

Add to project's `.claude/settings.json`:

```json
{
  "extraKnownMarketplaces": {
    "dev-toolbox": {
      "source": {
        "source": "github",
        "repo": "company/dev-toolbox"
      }
    }
  },
  "enabledPlugins": {
    "git-tools@dev-toolbox": true,
    "doc-tools@dev-toolbox": true,
    "deploy-tools@dev-toolbox": false
  }
}
```

This pre-configures:
- The dev-toolbox marketplace
- git-tools and doc-tools enabled by default
- deploy-tools available but not auto-enabled

---

## CI/CD for Monorepo Marketplace

### GitHub Actions Example

```yaml
name: Validate Marketplace

on:
  push:
    paths:
      - 'plugins/**'
      - '.claude-plugin/**'
  pull_request:
    paths:
      - 'plugins/**'
      - '.claude-plugin/**'

jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Install Claude Code
        run: npm install -g @anthropic-ai/claude-code

      - name: Validate marketplace
        run: claude plugin validate .

      - name: Check JSON syntax
        run: |
          python3 -c "import json; json.load(open('.claude-plugin/marketplace.json'))"
          for plugin in plugins/*/; do
            python3 -c "import json; json.load(open('${plugin}.claude-plugin/plugin.json'))"
          done
```
