# Multi-Repo Marketplace Template (Distributed Pattern)

Marketplace catalog pointing to plugins in separate repositories.

---

## When to Use

- Plugins developed by different teams or individuals
- Independent versioning and release cycles
- Mixed ownership (some internal, some community)
- Plugin repos that already exist independently
- Community-curated collections

---

## Architecture Overview

```
                    ┌─────────────────────────┐
                    │   Marketplace Repo      │
                    │   (catalog only)        │
                    │                         │
                    │   marketplace.json      │
                    │   points to:            │
                    └──────────┬──────────────┘
                               │
           ┌───────────────────┼───────────────────┐
           │                   │                   │
           ▼                   ▼                   ▼
    ┌──────────────┐   ┌──────────────┐   ┌──────────────┐
    │  Plugin A    │   │  Plugin B    │   │  Plugin C    │
    │  (github)    │   │  (gitlab)    │   │  (private)   │
    │              │   │              │   │              │
    │  owner/      │   │  org/        │   │  git.corp/   │
    │  plugin-a    │   │  plugin-b    │   │  plugin-c    │
    └──────────────┘   └──────────────┘   └──────────────┘
```

---

## Directory Structure

### Marketplace Repository

```
awesome-claude-plugins/
├── .claude-plugin/
│   └── marketplace.json    # Only the catalog
└── README.md               # Installation docs
```

### Individual Plugin Repositories

```
# Plugin A (github.com/alice/formatter)
formatter/
├── .claude-plugin/
│   └── plugin.json
├── commands/
│   └── format.md
└── README.md

# Plugin B (github.com/bob/linter)
linter/
├── .claude-plugin/
│   └── plugin.json
├── commands/
│   └── lint.md
└── README.md

# Plugin C (gitlab.com/company/security-scanner)
security-scanner/
├── .claude-plugin/
│   └── plugin.json
├── agents/
│   └── scanner.md
└── README.md
```

---

## Marketplace JSON with Multiple Source Types

```json
{
  "name": "awesome-claude-plugins",
  "owner": {
    "name": "Community Maintainers",
    "email": "maintainers@example.com"
  },
  "metadata": {
    "description": "Curated collection of awesome Claude Code plugins",
    "version": "5.0.0"
  },
  "plugins": [
    {
      "name": "formatter",
      "source": {
        "source": "github",
        "repo": "alice/formatter"
      },
      "description": "Multi-language code formatter",
      "version": "2.3.0",
      "author": {"name": "Alice"}
    },
    {
      "name": "linter",
      "source": {
        "source": "github",
        "repo": "bob/linter"
      },
      "description": "Comprehensive linting toolkit",
      "version": "1.8.0",
      "author": {"name": "Bob"}
    },
    {
      "name": "security-scanner",
      "source": {
        "source": "git",
        "url": "https://gitlab.com/company/security-scanner.git"
      },
      "description": "Security vulnerability scanner",
      "version": "3.0.0",
      "author": {"name": "Security Team"}
    },
    {
      "name": "deployment",
      "source": {
        "source": "git",
        "url": "git@github.com:private-org/deployment.git"
      },
      "description": "Deployment automation tools",
      "version": "1.2.0",
      "author": {"name": "DevOps"}
    }
  ]
}
```

---

## Source Type Reference

### GitHub Public Repository

```json
{
  "source": {
    "source": "github",
    "repo": "owner/repo-name"
  }
}
```
- Simplest syntax for public GitHub repos
- No authentication needed
- Claude Code handles URL construction

### GitHub Private Repository

```json
{
  "source": {
    "source": "git",
    "url": "git@github.com:owner/private-repo.git"
  }
}
```
- Use SSH URL for private repos
- Requires SSH key with access
- Or use HTTPS with token

### GitLab / Bitbucket / Self-Hosted

```json
{
  "source": {
    "source": "git",
    "url": "https://gitlab.com/org/repo.git"
  }
}
```
- Full URL required
- Works with any git service
- May require authentication

### With Specific Branch/Tag (Future)

```json
{
  "source": {
    "source": "github",
    "repo": "owner/repo",
    "ref": "v2.0.0"
  }
}
```
- Pin to specific version
- Useful for stability

---

## Complete Working Example

### Community Collection Marketplace

A curated collection of community plugins:

**.claude-plugin/marketplace.json**:
```json
{
  "name": "community-collection",
  "owner": {
    "name": "Claude Code Community",
    "email": "community@claudecode.dev"
  },
  "metadata": {
    "description": "Community-curated collection of Claude Code plugins",
    "version": "10.0.0"
  },
  "plugins": [
    {
      "name": "git-wizard",
      "source": {"source": "github", "repo": "git-tools/git-wizard"},
      "description": "Advanced git workflows: interactive rebase helper, conflict resolver, commit analyzer",
      "version": "3.2.1",
      "author": {"name": "Git Tools Community"},
      "homepage": "https://git-wizard.dev"
    },
    {
      "name": "test-master",
      "source": {"source": "github", "repo": "testing/test-master"},
      "description": "Test generation, analysis, and coverage tools",
      "version": "2.0.0",
      "author": {"name": "Testing Guild"},
      "homepage": "https://test-master.io"
    },
    {
      "name": "doc-generator",
      "source": {"source": "github", "repo": "docs-team/doc-generator"},
      "description": "Automatic documentation generation from code",
      "version": "1.5.0",
      "author": {"name": "Docs Team"}
    },
    {
      "name": "perf-analyzer",
      "source": {"source": "github", "repo": "performance/perf-analyzer"},
      "description": "Performance profiling and optimization suggestions",
      "version": "1.0.0",
      "author": {"name": "Performance Guild"}
    },
    {
      "name": "security-suite",
      "source": {"source": "github", "repo": "security/security-suite"},
      "description": "Comprehensive security scanning and hardening",
      "version": "4.1.0",
      "author": {"name": "Security Collective"}
    },
    {
      "name": "refactor-pro",
      "source": {"source": "github", "repo": "refactoring/refactor-pro"},
      "description": "Intelligent refactoring suggestions and automation",
      "version": "2.2.0",
      "author": {"name": "Refactoring Experts"}
    }
  ]
}
```

### README.md

```markdown
# Community Collection

A curated collection of high-quality Claude Code plugins.

## Installation

Add the marketplace:
```bash
/plugin marketplace add community/community-collection
```

Browse available plugins:
```bash
/plugin
```

Install specific plugins:
```bash
/plugin install git-wizard@community-collection
/plugin install test-master@community-collection
```

## Available Plugins

| Plugin | Description | Version |
|--------|-------------|---------|
| git-wizard | Advanced git workflows | 3.2.1 |
| test-master | Test generation and analysis | 2.0.0 |
| doc-generator | Auto documentation | 1.5.0 |
| perf-analyzer | Performance profiling | 1.0.0 |
| security-suite | Security scanning | 4.1.0 |
| refactor-pro | Refactoring automation | 2.2.0 |

## Contributing

Want to add a plugin? See [CONTRIBUTING.md](CONTRIBUTING.md).

## Plugin Requirements

- Must have valid plugin.json
- Must pass `claude plugin validate .`
- Must have README with usage instructions
- Must be actively maintained
```

---

## Managing Multi-Repo Marketplaces

### Adding a New Plugin

1. Verify plugin repo structure:
   ```bash
   # Clone and validate
   git clone https://github.com/owner/new-plugin
   cd new-plugin
   claude plugin validate .
   ```

2. Add entry to marketplace.json:
   ```json
   {
     "name": "new-plugin",
     "source": {"source": "github", "repo": "owner/new-plugin"},
     "description": "Description from plugin.json",
     "version": "1.0.0",
     "author": {"name": "Author Name"}
   }
   ```

3. Update marketplace version:
   ```json
   "metadata": {
     "version": "11.0.0"  // Increment
   }
   ```

4. Test:
   ```bash
   /plugin marketplace update community-collection
   /plugin install new-plugin@community-collection
   ```

### Updating Plugin Versions

When a plugin releases a new version:

1. Update version in marketplace.json plugin entry
2. Optionally increment marketplace metadata.version
3. Users run `/plugin marketplace update` to see new version

### Removing a Plugin

1. Remove entry from plugins array
2. Increment marketplace metadata.version
3. Document deprecation in README
4. Users' installed plugins continue working

### Version Synchronization

Multi-repo means versions can drift:
- Plugin author updates plugin to 2.0.0
- Marketplace may still list 1.5.0

**Best practices**:
- Set up notifications for plugin releases
- Regular sync schedule (weekly/monthly)
- Automated PR workflow for version bumps

---

## Hybrid Pattern: Local + Remote

Mix local development with remote plugins:

```json
{
  "plugins": [
    {
      "name": "my-dev-plugin",
      "source": "./plugins/my-dev-plugin",
      "description": "Local development plugin",
      "version": "0.1.0"
    },
    {
      "name": "stable-plugin",
      "source": {"source": "github", "repo": "org/stable-plugin"},
      "description": "Production-ready plugin",
      "version": "5.0.0"
    }
  ]
}
```

**Use case**: Develop new plugins locally while using stable remote plugins.

---

## Automation for Multi-Repo

### Version Checker Script

```bash
#!/bin/bash
# check-versions.sh - Compare marketplace versions with source repos

MARKETPLACE="marketplace.json"

for plugin in $(jq -r '.plugins[] | @base64' "$MARKETPLACE"); do
  name=$(echo "$plugin" | base64 -d | jq -r '.name')
  listed_version=$(echo "$plugin" | base64 -d | jq -r '.version')
  repo=$(echo "$plugin" | base64 -d | jq -r '.source.repo // empty')

  if [ -n "$repo" ]; then
    # Fetch latest version from GitHub
    latest=$(curl -s "https://api.github.com/repos/$repo/releases/latest" | jq -r '.tag_name // "unknown"')

    if [ "$listed_version" != "$latest" ]; then
      echo "⚠️  $name: listed $listed_version, latest $latest"
    else
      echo "✅ $name: up to date ($listed_version)"
    fi
  fi
done
```

### GitHub Action for Version Checks

```yaml
name: Check Plugin Versions

on:
  schedule:
    - cron: '0 9 * * 1'  # Weekly on Monday
  workflow_dispatch:

jobs:
  check:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Check versions
        run: |
          ./scripts/check-versions.sh > version-report.txt
          cat version-report.txt

      - name: Create issue if outdated
        if: contains(steps.check.outputs.report, '⚠️')
        uses: peter-evans/create-issue-from-file@v4
        with:
          title: Plugin Version Updates Available
          content-filepath: ./version-report.txt
```
