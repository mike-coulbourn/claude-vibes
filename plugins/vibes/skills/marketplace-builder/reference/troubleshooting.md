# Marketplace Troubleshooting

Common issues, debugging steps, and solutions for marketplace and plugin problems.

---

## Issue 1: Marketplace Not Found

### Symptoms
- `/plugin marketplace add owner/repo` fails
- "Marketplace not found" or "Cannot fetch" error
- Marketplace doesn't appear in `/plugin marketplace list`

### Causes & Solutions

**Cause 1: Incorrect path or URL**
```bash
# Wrong
/plugin marketplace add user/repo-name  # Typo in repo name

# Right
/plugin marketplace add user/repository-name  # Exact repo name
```

**Cause 2: Missing marketplace.json**
```bash
# Check structure
ls -la .claude-plugin/marketplace.json  # Must exist

# Expected location
repo/
└── .claude-plugin/
    └── marketplace.json  # Required
```

**Cause 3: Private repository without access**
```bash
# Test git access
git clone https://github.com/owner/private-repo.git

# For private repos, use SSH
/plugin marketplace add git@github.com:owner/private-repo.git
```

**Cause 4: Network issues**
```bash
# Test connectivity
curl -I https://github.com/owner/repo
```

---

## Issue 2: Plugin Installation Fails

### Symptoms
- `/plugin install plugin@marketplace` errors
- "Plugin not found in marketplace"
- Installation hangs or times out

### Causes & Solutions

**Cause 1: Plugin not in marketplace.json**
```json
// Check marketplace.json has the plugin
{
  "plugins": [
    {"name": "my-plugin", ...}  // Must be listed
  ]
}
```

**Cause 2: Wrong plugin@marketplace format**
```bash
# Format: plugin-name@marketplace-name
/plugin install formatter@team-tools

# Not
/plugin install formatter  # Missing marketplace
/plugin install team-tools/formatter  # Wrong format
```

**Cause 3: Plugin source inaccessible**
```json
// Check source is reachable
{
  "name": "plugin",
  "source": {"source": "github", "repo": "owner/repo"}
  // Is owner/repo accessible?
}
```

**Cause 4: Invalid plugin structure**
```bash
# Plugin must have valid plugin.json
plugin/
└── .claude-plugin/
    └── plugin.json  # Required
```

---

## Issue 3: Commands Not Appearing

### Symptoms
- Plugin installed but commands don't show in `/help`
- `/command-name` says "command not found"

### Causes & Solutions

**Cause 1: Commands not in plugin structure**
```bash
# Commands must be in commands/ directory
plugin/
├── .claude-plugin/plugin.json
└── commands/
    └── my-command.md  # Must be .md file
```

**Cause 2: Plugin not enabled**
```bash
# Check plugin is enabled
/plugin

# Enable if disabled
/plugin enable plugin-name@marketplace
```

**Cause 3: Commands path not specified in marketplace**
```json
// If using explicit paths, verify they're correct
{
  "name": "plugin",
  "commands": ["./commands/"]  // Path relative to plugin root
}
```

**Cause 4: Restart required**
Some changes require restarting Claude Code.

---

## Issue 4: Agents Not Invoking

### Symptoms
- Agent exists but never gets called
- Task tool doesn't list the agent
- Agent triggers don't work

### Causes & Solutions

**Cause 1: Agent not in agents/ directory**
```bash
plugin/
├── .claude-plugin/plugin.json
└── agents/
    └── my-agent.md  # Must be here
```

**Cause 2: Missing or poor description**
```markdown
---
name: my-agent
description: [MUST be clear about when to use]
---
```

Descriptions drive discovery. Vague = not invoked.

**Cause 3: Agent file syntax error**
```bash
# Validate YAML frontmatter
head -20 agents/my-agent.md
# Check for:
# - Opening ---
# - Closing ---
# - Valid YAML between
```

---

## Issue 5: Hooks Not Firing

### Symptoms
- Hooks defined but never execute
- No output from hook commands
- Events occur without hook response

### Causes & Solutions

**Cause 1: hooks.json not found**
```bash
plugin/
└── hooks/
    └── hooks.json  # Must exist
```

**Cause 2: Invalid hooks.json structure**
```json
// Correct structure
{
  "hooks": [
    {
      "matcher": {
        "event": "pre-tool-use",
        "tool": "Write"
      },
      "hooks": [
        {
          "type": "command",
          "command": "echo 'Hook fired'"
        }
      ]
    }
  ]
}
```

**Cause 3: Matcher doesn't match**
```json
// Event types: pre-tool-use, post-tool-use, notification, stop
// Tool must match exactly
{
  "matcher": {
    "event": "pre-tool-use",
    "tool": "Bash"  // Exact tool name
  }
}
```

**Cause 4: Command fails silently**
```bash
# Test command outside Claude Code
echo $TOOL_INPUT | jq '.file_path'
```

---

## Issue 6: MCP Servers Not Connecting

### Symptoms
- MCP server defined but tools not available
- Connection timeout errors
- Server process not starting

### Causes & Solutions

**Cause 1: Invalid .mcp.json**
```json
// Check JSON syntax
{
  "mcpServers": {
    "server-name": {
      "command": "node",
      "args": ["server.js"]
    }
  }
}
```

**Cause 2: Server executable not found**
```bash
# Check path
ls ${CLAUDE_PLUGIN_ROOT}/server.js  # Does it exist?

# Use absolute path in development
"command": "/full/path/to/server.js"
```

**Cause 3: Missing dependencies**
```bash
# Server may need npm install
cd plugin/server
npm install
```

**Cause 4: Environment variables not set**
```json
{
  "env": {
    "API_KEY": "${API_KEY}"  // Must be set in environment
  }
}
```

---

## Issue 7: JSON Syntax Errors

### Symptoms
- "Invalid JSON" errors
- Marketplace or plugin won't load
- Mysterious failures with no clear message

### Causes & Solutions

**Cause 1: Trailing commas**
```json
// Wrong
{
  "name": "plugin",
  "version": "1.0.0",  // <- Trailing comma
}

// Right
{
  "name": "plugin",
  "version": "1.0.0"
}
```

**Cause 2: Unquoted strings**
```json
// Wrong
{
  name: "plugin"  // name not quoted
}

// Right
{
  "name": "plugin"
}
```

**Cause 3: Single quotes**
```json
// Wrong
{
  'name': 'plugin'
}

// Right
{
  "name": "plugin"
}
```

**Cause 4: Comments (not allowed in JSON)**
```json
// Wrong
{
  "name": "plugin"  // This is a comment - INVALID
}

// Right
{
  "name": "plugin"
}
```

**Validation**:
```bash
# Validate JSON
python3 -c "import json; json.load(open('file.json'))"

# Or with jq
jq . file.json
```

---

## Issue 8: Team Settings Not Applied

### Symptoms
- Team members don't see configured marketplaces
- enabledPlugins not taking effect
- Different team members have different setups

### Causes & Solutions

**Cause 1: settings.json not committed**
```bash
# Check file is in git
git ls-files .claude/settings.json

# Commit if not
git add .claude/settings.json
git commit -m "Add Claude settings"
```

**Cause 2: Trust not granted**
When team member opens project:
1. Trust prompt appears
2. Must click "Trust" to enable settings
3. Marketplace trust prompts follow

**Cause 3: settings.local.json overriding**
```bash
# Check for local overrides
cat .claude/settings.local.json

# Remove if causing issues
rm .claude/settings.local.json
```

**Cause 4: Git not pulled**
```bash
git pull  # Get latest settings
```

---

## Issue 9: Version Conflicts

### Symptoms
- Wrong plugin version installed
- Marketplace shows different version than installed
- Updates not taking effect

### Causes & Solutions

**Cause 1: Cached version**
```bash
# Update marketplace cache
/plugin marketplace update marketplace-name
```

**Cause 2: Version mismatch between files**
```json
// marketplace.json
{"name": "plugin", "version": "2.0.0"}

// plugin.json
{"version": "1.5.0"}  // Should match!
```

**Cause 3: Need to reinstall**
```bash
/plugin uninstall plugin@marketplace
/plugin install plugin@marketplace
```

---

## 5-Step Debug Workflow

### Step 1: Validate JSON Syntax

```bash
# Validate all JSON files
python3 -c "import json; json.load(open('.claude-plugin/marketplace.json'))"
python3 -c "import json; json.load(open('.claude-plugin/plugin.json'))"
```

### Step 2: Check File Structure

```bash
# Expected structure
find . -name "*.json" -path "*/.claude-plugin/*"
find . -name "*.md" -path "*/commands/*"
find . -name "*.md" -path "*/agents/*"
```

### Step 3: Verify Source Access

```bash
# For GitHub sources
gh repo view owner/repo

# For Git URLs
git ls-remote https://git.example.com/repo.git

# For local paths
ls -la ./path/to/plugin
```

### Step 4: Test in Isolation

```bash
# Create minimal test
mkdir test-marketplace/.claude-plugin
echo '{"name":"test","owner":{"name":"Test"},"plugins":[]}' > test-marketplace/.claude-plugin/marketplace.json

# Add marketplace
/plugin marketplace add ./test-marketplace

# If this works, problem is in your specific files
```

### Step 5: Check Permissions and Access

```bash
# File permissions
ls -la .claude-plugin/

# Git access (for remote)
ssh -T git@github.com

# Environment variables (for MCP)
echo $API_KEY
```

---

## Diagnostic Commands

### List Current State

```bash
# List marketplaces
/plugin marketplace list

# List plugins
/plugin

# Check specific plugin
# (Look for it in /plugin output)
```

### Test Components

```bash
# Test command
/command-name

# Test agent (describe task to trigger)
"Review this code" # Should trigger code-reviewer agent

# Test hooks
# Perform action that should trigger hook
```

### Validate Files

```bash
# Full validation
claude plugin validate .

# Manual JSON check
python3 -c "
import json
import sys

def validate(path):
    try:
        json.load(open(path))
        print(f'✅ {path}')
    except Exception as e:
        print(f'❌ {path}: {e}')
        sys.exit(1)

validate('.claude-plugin/marketplace.json')
"
```

---

## Quick Validation Script

```bash
#!/bin/bash
# validate-marketplace.sh

set -e

echo "=== Marketplace Validation ==="
echo ""

# Check marketplace.json exists
if [ ! -f ".claude-plugin/marketplace.json" ]; then
    echo "❌ .claude-plugin/marketplace.json not found"
    exit 1
fi
echo "✅ marketplace.json found"

# Validate JSON syntax
if ! python3 -c "import json; json.load(open('.claude-plugin/marketplace.json'))" 2>/dev/null; then
    echo "❌ marketplace.json has invalid JSON"
    exit 1
fi
echo "✅ Valid JSON syntax"

# Check required fields
python3 -c "
import json
import sys

data = json.load(open('.claude-plugin/marketplace.json'))

errors = []
if 'name' not in data:
    errors.append('Missing: name')
if 'owner' not in data:
    errors.append('Missing: owner')
elif 'name' not in data.get('owner', {}):
    errors.append('Missing: owner.name')
if 'plugins' not in data:
    errors.append('Missing: plugins')

if errors:
    for e in errors:
        print(f'❌ {e}')
    sys.exit(1)

print('✅ Required fields present')
print(f'   Name: {data[\"name\"]}')
print(f'   Owner: {data[\"owner\"][\"name\"]}')
print(f'   Plugins: {len(data[\"plugins\"])}')
"

# Check plugin sources
echo ""
echo "=== Plugin Validation ==="
python3 -c "
import json
import os

data = json.load(open('.claude-plugin/marketplace.json'))
base = os.path.dirname('.claude-plugin/marketplace.json')

for plugin in data['plugins']:
    name = plugin.get('name', 'unknown')
    source = plugin.get('source', '')

    if isinstance(source, str) and source.startswith('.'):
        # Local path
        path = os.path.normpath(os.path.join(base, '..', source))
        plugin_json = os.path.join(path, '.claude-plugin', 'plugin.json')

        if os.path.exists(plugin_json):
            print(f'✅ {name}: Local path valid')
        else:
            print(f'⚠️  {name}: plugin.json not found at {plugin_json}')
    elif isinstance(source, dict):
        src_type = source.get('source', 'unknown')
        if src_type == 'github':
            print(f'ℹ️  {name}: GitHub repo {source.get(\"repo\")}')
        elif src_type == 'git':
            print(f'ℹ️  {name}: Git URL {source.get(\"url\")}')
        else:
            print(f'⚠️  {name}: Unknown source type {src_type}')
    else:
        print(f'⚠️  {name}: Cannot validate source')
"

echo ""
echo "=== Validation Complete ==="
```

---

## Getting Help

### Information to Gather

When asking for help, include:
1. Error message (exact text)
2. Command that caused the error
3. marketplace.json contents
4. plugin.json contents (if applicable)
5. Directory structure (`find . -type f`)
6. Claude Code version

### Common Resources

- `/help` - Built-in help
- `/plugin` - Plugin management
- GitHub Issues - Report bugs
- Documentation - Official docs
