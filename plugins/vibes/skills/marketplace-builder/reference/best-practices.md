# Marketplace Best Practices

Design principles and guidelines for creating effective marketplaces and plugins.

---

## Marketplace Design Principles

### 1. Clear Purpose

**Define the marketplace's scope**:
- What type of tools does it contain?
- Who is the target audience?
- What problems does it solve?

**Good examples**:
- `team-workflows` - Team collaboration tools
- `security-tools` - Security scanning and hardening
- `frontend-essentials` - Frontend development utilities

**Avoid**:
- `my-stuff` - Too vague
- `tools` - Not descriptive

### 2. Logical Grouping

**Group related plugins**:
```json
{
  "name": "development-toolkit",
  "plugins": [
    {"name": "formatter", "description": "Code formatting"},
    {"name": "linter", "description": "Code linting"},
    {"name": "tester", "description": "Test running"}
  ]
}
```

**Don't mix unrelated tools**:
```json
// Avoid this
{
  "plugins": [
    {"name": "code-formatter"},
    {"name": "recipe-finder"},
    {"name": "weather-checker"}
  ]
}
```

### 3. Consistent Naming

**Use consistent patterns**:
- All plugins: `verb-noun` or `domain-tool`
- All commands: `action-target`
- All agents: `role-name`

**Example convention**:
```
Plugins:    code-formatter, code-linter, code-tester
Commands:   format-file, lint-code, run-tests
Agents:     code-reviewer, test-analyzer
```

### 4. Version Management

**Marketplace version**: Increment when plugins are added/removed

**Plugin versions**: Follow semantic versioning

```json
{
  "metadata": {"version": "5.0.0"},
  "plugins": [
    {"name": "formatter", "version": "2.3.1"},
    {"name": "linter", "version": "1.8.0"}
  ]
}
```

**Version policy options**:
| Approach | Description | Best For |
|----------|-------------|----------|
| Synchronized | All plugins share version | Tightly coupled tools |
| Independent | Each plugin versioned separately | Loosely coupled tools |
| Hybrid | Marketplace + plugin versions | Most cases |

---

## Plugin Design Principles

### 1. Single Responsibility

**Each plugin should do one thing well**:

**Good**:
- `code-formatter` - Just formatting
- `test-runner` - Just tests
- `security-scanner` - Just security

**Avoid**:
- `super-tool` - Does formatting, testing, deployment, and coffee

### 2. Self-Contained

**Plugins should work independently**:
- No hard dependencies on other plugins
- Clear documentation
- Sensible defaults

**If plugins relate**:
- Document optional integrations
- Don't require installation order

### 3. Clear Descriptions

**Write descriptions for discovery**:

**Good**:
```json
{
  "description": "Run and analyze tests with coverage reporting. Supports Jest, pytest, and Go testing frameworks."
}
```

**Poor**:
```json
{
  "description": "Test stuff"
}
```

### 4. Minimal Permissions

**Request only needed tools**:

```markdown
---
allowed-tools: Read, Grep, Glob
---
```

Not:
```markdown
---
allowed-tools: Bash, Read, Write, Edit, Glob, Grep
---
```

---

## Architecture Patterns

### When to Use Monorepo

**Pros**:
- Single repo to manage
- Easier cross-plugin changes
- Unified CI/CD
- Consistent tooling

**Best for**:
- Team-owned plugin collections
- Plugins that share code
- Coordinated releases

**Structure**:
```
marketplace/
├── .claude-plugin/marketplace.json
├── plugins/
│   ├── plugin-a/
│   ├── plugin-b/
│   └── shared/
└── scripts/
```

### When to Use Multi-Repo

**Pros**:
- Independent versioning
- Separate ownership
- Flexible contribution
- Smaller repos

**Best for**:
- Community collections
- Mixed ownership
- Independent release cycles

**Structure**:
```
marketplace-catalog/    # Just the catalog
plugin-a/               # Separate repo
plugin-b/               # Separate repo
```

### When to Use Hybrid

**Pros**:
- Mix local and remote
- Support development workflow
- Include approved external tools

**Best for**:
- Enterprise environments
- Active development
- Mixed internal/external

**Structure**:
```json
{
  "plugins": [
    {"name": "internal", "source": "./plugins/internal"},
    {"name": "approved", "source": {"source": "github", "repo": "external/tool"}}
  ]
}
```

---

## Distribution Strategies

### Personal Distribution

**Use case**: Individual tools for yourself

```bash
# Create personal marketplace
mkdir -p ~/.claude/marketplaces/personal-tools/.claude-plugin
# Add marketplace.json
# Use with: /plugin marketplace add ~/.claude/marketplaces/personal-tools
```

### Team Distribution

**Use case**: Team-shared tools via git

**.claude/settings.json**:
```json
{
  "extraKnownMarketplaces": {
    "team-tools": {
      "source": {"source": "github", "repo": "team/plugins"}
    }
  },
  "enabledPlugins": {
    "formatter@team-tools": true
  }
}
```

**Team member experience**:
1. Clone project
2. Open in Claude Code
3. Trust folder
4. Accept marketplace trust
5. Install enabled plugins

### Public Distribution

**Use case**: Community tools

**README template**:
```markdown
# My Plugin Collection

## Installation

1. Add the marketplace:
   ```bash
   /plugin marketplace add username/marketplace
   ```

2. Install plugins:
   ```bash
   /plugin install plugin-name@username-marketplace
   ```

## Available Plugins

| Plugin | Description |
|--------|-------------|
| formatter | Code formatting |
```

### Enterprise Distribution

**Use case**: Company-wide tools with governance

**Components**:
1. Private marketplace repo
2. Plugin approval process
3. Team settings in project templates
4. Documentation and training

---

## Security Best Practices

### Trust Model

**Understand the trust chain**:
```
User trusts → Marketplace → Plugin → Components
```

Each level requires explicit approval.

### Plugin Security

**1. Minimal tool access**:
```markdown
---
allowed-tools: Read, Grep
---
```

**2. No secrets in code**:
```markdown
# Bad
API_KEY = "abc123"

# Good
Use environment variable: ${API_KEY}
```

**3. Validate inputs**:
```markdown
Validate all user-provided arguments before using in commands.
```

**4. Audit commands**:
- Review what bash commands do
- Avoid destructive operations
- Add confirmation for risky actions

### Marketplace Security

**1. Verify plugin sources**:
- Check repository ownership
- Review commit history
- Confirm maintainer identity

**2. Pin versions**:
```json
{
  "plugins": [
    {"name": "tool", "version": "2.3.1"}
  ]
}
```

**3. Document approvals**:
```json
{
  "name": "approved-formatter",
  "description": "Code formatter (Security reviewed: 2024-01-15, approved by: security-team)"
}
```

**4. Regular audits**:
- Review plugin changes
- Update versions deliberately
- Remove deprecated plugins

---

## Documentation Best Practices

### Marketplace Documentation

**README.md should include**:
1. Purpose and scope
2. Installation instructions
3. Plugin list with descriptions
4. Contributing guidelines
5. Contact information

### Plugin Documentation

**plugin.json fields**:
```json
{
  "homepage": "https://docs.example.com/plugin",
  "repository": "https://github.com/org/plugin"
}
```

**README.md for each plugin**:
1. What it does
2. Installation
3. Usage examples
4. Configuration
5. Troubleshooting

### Command Documentation

**In frontmatter**:
```markdown
---
description: Clear one-line description
argument-hint: [required-arg] [optional-arg]
---
```

**In body**:
- Purpose
- Steps performed
- Output format
- Examples

---

## Testing Best Practices

### Before Publishing

**1. Validate structure**:
```bash
claude plugin validate .
```

**2. Test locally**:
```bash
/plugin marketplace add ./path-to-marketplace
/plugin install my-plugin@my-marketplace
```

**3. Test each component**:
- Run each command
- Trigger each agent
- Verify hooks fire
- Check MCP servers connect

### Continuous Testing

**CI validation** (GitHub Actions):
```yaml
name: Validate

on: [push, pull_request]

jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Validate JSON
        run: |
          python3 -c "import json; json.load(open('.claude-plugin/marketplace.json'))"
      - name: Validate plugins
        run: |
          for dir in plugins/*/; do
            python3 -c "import json; json.load(open('${dir}.claude-plugin/plugin.json'))"
          done
```

### User Acceptance Testing

Before team rollout:
1. Test with 2-3 users
2. Gather feedback
3. Fix issues
4. Document edge cases
5. Create training materials

---

## Maintenance Best Practices

### Version Updates

**Regular schedule**:
- Weekly: Check for dependency updates
- Monthly: Review and update plugin versions
- Quarterly: Audit and prune

**Update process**:
1. Test new version locally
2. Update version in plugin.json
3. Update version in marketplace.json
4. Document changes
5. Notify users

### Deprecation

**When removing a plugin**:
1. Mark as deprecated in description
2. Provide migration path
3. Keep available for transition period
4. Remove in next major version

```json
{
  "name": "old-formatter",
  "description": "[DEPRECATED - Use new-formatter] Original formatter"
}
```

### Change Communication

**Changelog format**:
```markdown
## [2.0.0] - 2024-01-15

### Breaking Changes
- Removed `old-command` (use `new-command` instead)

### Added
- New `feature-command`

### Fixed
- Bug in `existing-command`
```

**Notification channels**:
- Changelog in repo
- Release notes
- Team announcements
- Migration guides for breaking changes

---

## Common Anti-Patterns

### 1. Kitchen Sink Plugin

**Problem**: Plugin that does everything
**Solution**: Split into focused plugins

### 2. Unclear Descriptions

**Problem**: "Does stuff with code"
**Solution**: Specific, actionable descriptions

### 3. No Versioning

**Problem**: No versions, breaking changes surprise users
**Solution**: Semantic versioning from day one

### 4. Missing Validation

**Problem**: Invalid JSON breaks installation
**Solution**: Validate before every commit

### 5. Over-Permissive Tools

**Problem**: All tools allowed when not needed
**Solution**: Minimal required tools only

### 6. No Documentation

**Problem**: Users don't know how to use plugins
**Solution**: README, examples, inline docs

### 7. Abandoned Plugins

**Problem**: Plugins stop working, no updates
**Solution**: Regular maintenance, clear ownership

### 8. Duplicate Functionality

**Problem**: Multiple plugins doing the same thing
**Solution**: Consolidate or clearly differentiate
