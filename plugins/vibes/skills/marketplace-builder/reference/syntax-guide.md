# Marketplace Syntax Guide

Complete reference for marketplace.json, plugin.json, and settings.json schemas.

---

## marketplace.json Schema

### Complete Schema

```json
{
  "name": "string (required)",
  "owner": {
    "name": "string (required)",
    "email": "string (optional)"
  },
  "metadata": {
    "description": "string (optional)",
    "version": "string (optional)",
    "pluginRoot": "string (optional)"
  },
  "plugins": [
    {
      "name": "string (required)",
      "source": "string | SourceObject (required)",
      "description": "string (optional)",
      "version": "string (optional)",
      "author": {
        "name": "string (optional)",
        "email": "string (optional)"
      },
      "homepage": "string (optional)",
      "commands": ["string (paths)"],
      "agents": ["string (paths)"],
      "skills": {"name": "path"},
      "hooks": "string (path)",
      "mcpServers": {}
    }
  ]
}
```

### Field Reference

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `name` | string | Yes | Unique identifier (kebab-case) |
| `owner` | object | Yes | Marketplace owner info |
| `owner.name` | string | Yes | Owner name |
| `owner.email` | string | No | Contact email |
| `metadata` | object | No | Marketplace metadata |
| `metadata.description` | string | No | Marketplace description |
| `metadata.version` | string | No | Marketplace catalog version |
| `metadata.pluginRoot` | string | No | Base path for relative plugin sources |
| `plugins` | array | Yes | List of plugins |

### Plugin Entry Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `name` | string | Yes | Plugin identifier |
| `source` | string/object | Yes | Plugin source location |
| `description` | string | No | Plugin description (shown in browser) |
| `version` | string | No | Plugin version (semver) |
| `author` | object | No | Plugin author info |
| `homepage` | string | No | Documentation URL |
| `commands` | array | No | Paths to command files |
| `agents` | array | No | Paths to agent files |
| `skills` | object | No | Map of skill names to paths |
| `hooks` | string | No | Path to hooks.json |
| `mcpServers` | object | No | MCP server configurations |

---

## Source Types

### Relative Path (Shorthand)

```json
{
  "name": "my-plugin",
  "source": "./plugins/my-plugin"
}
```

Path relative to marketplace.json location.

### Directory Source

```json
{
  "name": "my-plugin",
  "source": {
    "source": "directory",
    "path": "./plugins/my-plugin"
  }
}
```

Explicit form of relative path.

### GitHub Source

```json
{
  "name": "my-plugin",
  "source": {
    "source": "github",
    "repo": "owner/repository-name"
  }
}
```

For public GitHub repositories. Format: `owner/repo-name`.

### Git URL Source

```json
{
  "name": "my-plugin",
  "source": {
    "source": "git",
    "url": "https://gitlab.com/org/repo.git"
  }
}
```

For any git repository. Use for:
- GitLab
- Bitbucket
- Self-hosted git
- Private GitHub (SSH URL)

### Source Type Summary

| Type | Syntax | Use Case |
|------|--------|----------|
| Relative | `"./path"` | Same repo plugins |
| Directory | `{"source": "directory", "path": "..."}` | Explicit local |
| GitHub | `{"source": "github", "repo": "owner/repo"}` | Public GitHub |
| Git URL | `{"source": "git", "url": "..."}` | Any git service |

---

## plugin.json Schema

### Complete Schema

```json
{
  "name": "string (required)",
  "description": "string (required)",
  "version": "string (required)",
  "author": {
    "name": "string (optional)",
    "email": "string (optional)",
    "url": "string (optional)"
  },
  "homepage": "string (optional)",
  "repository": "string (optional)",
  "license": "string (optional)",
  "keywords": ["string (optional)"]
}
```

### Field Reference

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `name` | string | Yes | Plugin identifier (kebab-case) |
| `description` | string | Yes | What the plugin does |
| `version` | string | Yes | Semantic version (X.Y.Z) |
| `author` | object | No | Author information |
| `author.name` | string | No* | Author name (*required if author present) |
| `author.email` | string | No | Author email |
| `author.url` | string | No | Author website |
| `homepage` | string | No | Plugin documentation URL |
| `repository` | string | No | Source code URL |
| `license` | string | No | License identifier (MIT, Apache-2.0, etc.) |
| `keywords` | array | No | Discovery keywords |

### Example

```json
{
  "name": "code-formatter",
  "description": "Multi-language code formatter with automatic detection",
  "version": "2.1.0",
  "author": {
    "name": "Format Team",
    "email": "format@example.com",
    "url": "https://formatters.dev"
  },
  "homepage": "https://docs.formatters.dev",
  "repository": "https://github.com/formatters/code-formatter",
  "license": "MIT",
  "keywords": ["formatting", "prettier", "code-style"]
}
```

---

## settings.json Schema

### Team Configuration

Location: `.claude/settings.json` (project root)

```json
{
  "extraKnownMarketplaces": {
    "marketplace-name": {
      "source": {
        "source": "github | git | directory",
        "repo": "owner/repo",
        "url": "https://...",
        "path": "./..."
      }
    }
  },
  "enabledPlugins": {
    "plugin-name@marketplace-name": true | false
  }
}
```

### Field Reference

| Field | Type | Description |
|-------|------|-------------|
| `extraKnownMarketplaces` | object | Marketplaces to pre-configure |
| `enabledPlugins` | object | Plugins to enable/disable |

### Marketplace Source in Settings

```json
{
  "extraKnownMarketplaces": {
    "team-tools": {
      "source": {
        "source": "github",
        "repo": "company/claude-plugins"
      }
    },
    "private-tools": {
      "source": {
        "source": "git",
        "url": "git@git.company.com:tools/plugins.git"
      }
    },
    "local-dev": {
      "source": {
        "source": "directory",
        "path": "../my-marketplace"
      }
    }
  }
}
```

### Plugin Enabling

```json
{
  "enabledPlugins": {
    "formatter@team-tools": true,
    "linter@team-tools": true,
    "experimental@team-tools": false
  }
}
```

Format: `"plugin-name@marketplace-name": boolean`
- `true`: Auto-enable when user trusts folder
- `false`: Available but not auto-enabled

### Personal Overrides

Location: `.claude/settings.local.json` (git-ignored)

```json
{
  "enabledPlugins": {
    "experimental@team-tools": true
  }
}
```

Overrides team settings for local machine.

---

## Component Paths

### Commands

```json
{
  "commands": [
    "./commands/",
    "./commands/subdir/",
    "./commands/specific.md"
  ]
}
```

- Directories: Include all `.md` files
- Files: Include specific command

### Agents

```json
{
  "agents": [
    "./agents/",
    "./agents/specific-agent.md"
  ]
}
```

### Skills

```json
{
  "skills": {
    "skill-name": "./skills/skill-name",
    "another-skill": "./skills/another"
  }
}
```

Object mapping skill names to directory paths. Each directory must contain `SKILL.md`.

### Hooks

```json
{
  "hooks": "./hooks/hooks.json"
}
```

Single path to hooks.json file.

### MCP Servers

```json
{
  "mcpServers": {
    "server-name": {
      "command": "node",
      "args": ["${CLAUDE_PLUGIN_ROOT}/server/index.js"],
      "env": {
        "API_KEY": "${API_KEY}"
      }
    }
  }
}
```

Special variables:
- `${CLAUDE_PLUGIN_ROOT}`: Plugin installation directory
- `${ENV_VAR}`: Environment variable

---

## Version Format

### Semantic Versioning

Format: `MAJOR.MINOR.PATCH`

| Component | Meaning | When to Increment |
|-----------|---------|-------------------|
| MAJOR | Breaking changes | Incompatible API changes |
| MINOR | New features | Backward-compatible additions |
| PATCH | Bug fixes | Backward-compatible fixes |

Examples:
- `1.0.0`: Initial release
- `1.0.1`: Bug fix
- `1.1.0`: New feature
- `2.0.0`: Breaking change

### Pre-release Versions

```
1.0.0-alpha
1.0.0-beta.1
1.0.0-rc.1
```

---

## Naming Conventions

### Marketplace Names

- Use `kebab-case`
- Descriptive of contents
- Examples: `team-tools`, `company-plugins`, `dev-essentials`

### Plugin Names

- Use `kebab-case`
- Action or domain focused
- Examples: `code-formatter`, `git-workflow`, `security-scanner`

### Command Names

- File: `verb-noun.md` (e.g., `format-code.md`)
- Shows as: `/format-code`

### Agent Names

- File: `role-name.md` (e.g., `code-reviewer.md`)
- YAML name field: `code-reviewer`

---

## Validation

### JSON Syntax Validation

```bash
# Python
python3 -c "import json; json.load(open('marketplace.json'))"

# Node.js
node -e "JSON.parse(require('fs').readFileSync('marketplace.json'))"

# jq
jq . marketplace.json > /dev/null && echo "Valid"
```

### Claude Plugin Validation

```bash
claude plugin validate .
```

Checks:
- JSON syntax
- Required fields
- File paths exist
- Schema compliance

### Quick Validation Script

```bash
#!/bin/bash
# validate-marketplace.sh

MARKETPLACE=".claude-plugin/marketplace.json"

# Check file exists
if [ ! -f "$MARKETPLACE" ]; then
  echo "❌ marketplace.json not found"
  exit 1
fi

# Validate JSON
if ! python3 -c "import json; json.load(open('$MARKETPLACE'))" 2>/dev/null; then
  echo "❌ Invalid JSON syntax"
  exit 1
fi

# Check required fields
if ! python3 -c "
import json
data = json.load(open('$MARKETPLACE'))
assert 'name' in data, 'Missing name'
assert 'owner' in data, 'Missing owner'
assert 'name' in data['owner'], 'Missing owner.name'
assert 'plugins' in data, 'Missing plugins'
print('✅ Required fields present')
" 2>&1; then
  exit 1
fi

# Check plugin sources
python3 -c "
import json
import os
data = json.load(open('$MARKETPLACE'))
for plugin in data['plugins']:
  source = plugin.get('source', '')
  if isinstance(source, str) and source.startswith('./'):
    path = os.path.join(os.path.dirname('$MARKETPLACE'), '..', source)
    if not os.path.exists(path):
      print(f'⚠️  Plugin path not found: {source}')
    else:
      print(f'✅ Plugin found: {plugin[\"name\"]}')
  else:
    print(f'ℹ️  Remote plugin: {plugin[\"name\"]}')
"

echo ""
echo "Validation complete"
```

---

## Complete Examples

### Minimal Marketplace

```json
{
  "name": "my-tools",
  "owner": {"name": "Developer"},
  "plugins": [
    {
      "name": "tool",
      "source": ".",
      "version": "1.0.0"
    }
  ]
}
```

### Full-Featured Marketplace

```json
{
  "name": "enterprise-tools",
  "owner": {
    "name": "Platform Team",
    "email": "platform@company.com"
  },
  "metadata": {
    "description": "Enterprise development tools and workflows",
    "version": "5.0.0",
    "pluginRoot": "./plugins"
  },
  "plugins": [
    {
      "name": "code-tools",
      "source": "./plugins/code-tools",
      "description": "Code formatting, linting, and analysis",
      "version": "2.3.0",
      "author": {"name": "Code Team"},
      "commands": ["./commands/"],
      "agents": ["./agents/analyzer.md"],
      "hooks": "./hooks/hooks.json"
    },
    {
      "name": "deploy-tools",
      "source": {"source": "github", "repo": "company/deploy-tools"},
      "description": "Deployment automation and monitoring",
      "version": "3.1.0",
      "author": {"name": "DevOps Team"},
      "homepage": "https://docs.company.com/deploy"
    },
    {
      "name": "security-scanner",
      "source": {"source": "git", "url": "git@git.company.com:security/scanner.git"},
      "description": "Security vulnerability scanning",
      "version": "1.5.0",
      "author": {"name": "Security Team"},
      "mcpServers": {
        "scanner": {
          "command": "${CLAUDE_PLUGIN_ROOT}/bin/scanner",
          "env": {"SCAN_TOKEN": "${SCAN_TOKEN}"}
        }
      }
    }
  ]
}
```

### Full-Featured Settings

```json
{
  "extraKnownMarketplaces": {
    "enterprise-tools": {
      "source": {
        "source": "git",
        "url": "git@git.company.com:platform/claude-plugins.git"
      }
    },
    "community-approved": {
      "source": {
        "source": "github",
        "repo": "company/approved-plugins"
      }
    }
  },
  "enabledPlugins": {
    "code-tools@enterprise-tools": true,
    "security-scanner@enterprise-tools": true,
    "deploy-tools@enterprise-tools": false,
    "formatter@community-approved": true
  }
}
```
