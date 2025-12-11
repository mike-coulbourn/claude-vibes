# Production Hooks Template

Build complete, production-ready hook systems with multi-event orchestration, security hardening, and team deployment.

## When to Use

- Deploying hooks for team/organization use
- Building comprehensive automation systems
- Requiring audit trails and compliance
- Needing robust error handling
- Coordinating multiple hook events

---

## Production Hook Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    Hook System Architecture                  │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  SessionStart ──► Environment Setup                          │
│       │                                                      │
│       ▼                                                      │
│  UserPromptSubmit ──► Context Injection + Validation         │
│       │                                                      │
│       ▼                                                      │
│  PreToolUse ──► Security Gate + Input Validation             │
│       │                                                      │
│       ▼                                                      │
│  [Tool Executes]                                             │
│       │                                                      │
│       ▼                                                      │
│  PostToolUse ──► Quality Checks + Audit Logging              │
│       │                                                      │
│       ▼                                                      │
│  Stop ──► Completion Verification                            │
│       │                                                      │
│       ▼                                                      │
│  SessionEnd ──► Cleanup + Summary                            │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

---

## Complete Example: Code Quality Guardian

A production-ready hook system for enforcing code quality.

### Directory Structure

```
project/
├── .claude/
│   ├── settings.json           # Hook configuration
│   └── hooks/                  # Hook scripts
│       ├── lib/
│       │   ├── common.sh       # Shared utilities
│       │   └── config.py       # Shared Python config
│       ├── setup-env.sh        # SessionStart
│       ├── inject-context.py   # UserPromptSubmit
│       ├── security-gate.py    # PreToolUse
│       ├── quality-check.sh    # PostToolUse
│       ├── audit-logger.py     # PostToolUse (all tools)
│       └── verify-complete.py  # Stop (prompt-based)
```

### Configuration

**`.claude/settings.json`:**
```json
{
  "hooks": {
    "SessionStart": [
      {
        "matcher": "startup|resume",
        "hooks": [
          {
            "type": "command",
            "command": "bash \"$CLAUDE_PROJECT_DIR\"/.claude/hooks/setup-env.sh",
            "timeout": 30
          }
        ]
      }
    ],
    "UserPromptSubmit": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "python3 \"$CLAUDE_PROJECT_DIR\"/.claude/hooks/inject-context.py",
            "timeout": 10
          }
        ]
      }
    ],
    "PreToolUse": [
      {
        "matcher": "Write|Edit",
        "hooks": [
          {
            "type": "command",
            "command": "python3 \"$CLAUDE_PROJECT_DIR\"/.claude/hooks/security-gate.py",
            "timeout": 10
          }
        ]
      },
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "python3 \"$CLAUDE_PROJECT_DIR\"/.claude/hooks/command-gate.py",
            "timeout": 5
          }
        ]
      }
    ],
    "PostToolUse": [
      {
        "matcher": "Write|Edit",
        "hooks": [
          {
            "type": "command",
            "command": "bash \"$CLAUDE_PROJECT_DIR\"/.claude/hooks/quality-check.sh",
            "timeout": 60
          }
        ]
      },
      {
        "matcher": "*",
        "hooks": [
          {
            "type": "command",
            "command": "python3 \"$CLAUDE_PROJECT_DIR\"/.claude/hooks/audit-logger.py",
            "timeout": 5
          }
        ]
      }
    ],
    "Stop": [
      {
        "hooks": [
          {
            "type": "prompt",
            "prompt": "Verify task completion. Check: 1) All requested work done, 2) Tests pass, 3) No TODOs left, 4) Code is clean. If incomplete, explain what's missing. Context: $ARGUMENTS",
            "timeout": 45
          }
        ]
      }
    ]
  }
}
```

### Shared Utilities

**`.claude/hooks/lib/common.sh`:**
```bash
#!/bin/bash
# Shared utilities for bash hooks

# Logging with timestamps
log() {
    local level="$1"
    local message="$2"
    local timestamp=$(date '+%Y-%m-%d %H:%M:%S')
    echo "[$timestamp] [$level] $message" >> "$CLAUDE_PROJECT_DIR/.claude/hooks.log"
}

log_info() { log "INFO" "$1"; }
log_warn() { log "WARN" "$1"; }
log_error() { log "ERROR" "$1"; }

# Safe JSON parsing
parse_json() {
    local json="$1"
    local field="$2"
    echo "$json" | jq -r "$field // empty" 2>/dev/null || echo ""
}

# Check if file is in project
is_in_project() {
    local path="$1"
    local project="$CLAUDE_PROJECT_DIR"
    [[ "$path" == "$project"* ]]
}
```

**`.claude/hooks/lib/config.py`:**
```python
#!/usr/bin/env python3
"""Shared configuration and utilities for Python hooks."""

import os
import json
import sys
from datetime import datetime
from pathlib import Path

# Project paths
PROJECT_DIR = os.environ.get('CLAUDE_PROJECT_DIR', os.getcwd())
HOOKS_DIR = Path(PROJECT_DIR) / '.claude' / 'hooks'
LOG_FILE = HOOKS_DIR / 'hooks.log'

# Protected patterns
PROTECTED_FILES = [
    '.env', '.env.local', '.env.production',
    'secrets', 'credentials', 'api_key', 'token',
    'id_rsa', 'id_ed25519', '.ssh',
]

PROTECTED_COMMANDS = [
    r'rm\s+-rf\s+/',
    r'rm\s+-rf\s+~',
    r'sudo\s+rm',
    r'chmod\s+777',
    r'curl.*\|\s*sh',
]

# Logging
def log(level: str, message: str):
    """Log message to hooks log file."""
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    LOG_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(LOG_FILE, 'a') as f:
        f.write(f"[{timestamp}] [{level}] {message}\n")

def log_info(msg): log("INFO", msg)
def log_warn(msg): log("WARN", msg)
def log_error(msg): log("ERROR", msg)

# JSON helpers
def read_input():
    """Read and parse JSON from stdin."""
    try:
        return json.load(sys.stdin)
    except json.JSONDecodeError as e:
        log_error(f"JSON parse error: {e}")
        return {}

def output_decision(decision: str, reason: str = "", updated_input: dict = None):
    """Output a hook decision."""
    result = {
        "hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "permissionDecision": decision,
            "permissionDecisionReason": reason
        }
    }
    if updated_input:
        result["hookSpecificOutput"]["updatedInput"] = updated_input
    print(json.dumps(result))

def block(message: str):
    """Block operation with error."""
    print(message, file=sys.stderr)
    sys.exit(2)
```

### Hook Scripts

**`.claude/hooks/setup-env.sh`:**
```bash
#!/bin/bash
set -euo pipefail
source "$CLAUDE_PROJECT_DIR/.claude/hooks/lib/common.sh"

log_info "Session started"

# Set up environment variables
if [ -n "${CLAUDE_ENV_FILE:-}" ]; then
    # Add project-specific environment
    echo "export NODE_ENV=development" >> "$CLAUDE_ENV_FILE"
    echo "export CLAUDE_HOOKS_ENABLED=true" >> "$CLAUDE_ENV_FILE"
    log_info "Environment configured"
fi

# Check for required tools
for tool in jq node npm; do
    if ! command -v "$tool" &> /dev/null; then
        log_warn "Missing tool: $tool"
    fi
done

# Log git status
if git rev-parse --git-dir > /dev/null 2>&1; then
    branch=$(git branch --show-current)
    log_info "Git branch: $branch"
fi

exit 0
```

**`.claude/hooks/inject-context.py`:**
```python
#!/usr/bin/env python3
"""Inject project context into user prompts."""

import sys
import json
import os
sys.path.insert(0, os.path.join(os.environ.get('CLAUDE_PROJECT_DIR', '.'), '.claude/hooks/lib'))
from config import read_input, log_info, PROJECT_DIR

def get_context():
    """Build project context."""
    context_parts = []

    # Project type
    if os.path.exists(os.path.join(PROJECT_DIR, 'package.json')):
        context_parts.append("Node.js project")
    if os.path.exists(os.path.join(PROJECT_DIR, 'requirements.txt')):
        context_parts.append("Python project")

    # Project rules
    claude_md = os.path.join(PROJECT_DIR, 'CLAUDE.md')
    if os.path.exists(claude_md):
        context_parts.append("See CLAUDE.md for project conventions")

    # Testing framework
    if os.path.exists(os.path.join(PROJECT_DIR, 'jest.config.js')):
        context_parts.append("Uses Jest for testing")
    if os.path.exists(os.path.join(PROJECT_DIR, 'pytest.ini')):
        context_parts.append("Uses pytest for testing")

    return " | ".join(context_parts) if context_parts else ""

def main():
    data = read_input()
    context = get_context()

    if context:
        log_info(f"Injecting context: {context}")
        output = {
            "hookSpecificOutput": {
                "hookEventName": "UserPromptSubmit",
                "additionalContext": f"[Project: {context}]"
            }
        }
        print(json.dumps(output))

    sys.exit(0)

if __name__ == '__main__':
    main()
```

**`.claude/hooks/security-gate.py`:**
```python
#!/usr/bin/env python3
"""Security gate for file operations."""

import sys
import os
import re
sys.path.insert(0, os.path.join(os.environ.get('CLAUDE_PROJECT_DIR', '.'), '.claude/hooks/lib'))
from config import read_input, output_decision, block, log_info, log_warn, PROTECTED_FILES, PROJECT_DIR

def check_file(file_path: str) -> tuple:
    """Check if file operation should be allowed."""
    path_lower = file_path.lower()

    # Check protected patterns
    for pattern in PROTECTED_FILES:
        if pattern in path_lower:
            return 'deny', f"Protected file pattern: {pattern}"

    # Check path traversal
    normalized = os.path.normpath(file_path)
    if '..' in file_path and not normalized.startswith(PROJECT_DIR):
        return 'deny', "Path traversal attempt blocked"

    # Check if outside project
    if os.path.isabs(file_path) and not file_path.startswith(PROJECT_DIR):
        return 'ask', f"File outside project: {file_path}"

    return 'allow', ""

def main():
    data = read_input()
    tool_input = data.get('tool_input', {})
    file_path = tool_input.get('file_path', '')

    if not file_path:
        sys.exit(0)

    decision, reason = check_file(file_path)

    if decision == 'deny':
        log_warn(f"Blocked: {file_path} - {reason}")
        block(f"BLOCKED: {reason}")
    elif decision == 'ask':
        log_info(f"Asking confirmation: {file_path}")
        output_decision('ask', reason)
    else:
        log_info(f"Allowed: {file_path}")

    sys.exit(0)

if __name__ == '__main__':
    main()
```

**`.claude/hooks/command-gate.py`:**
```python
#!/usr/bin/env python3
"""Security gate for bash commands."""

import sys
import os
import re
sys.path.insert(0, os.path.join(os.environ.get('CLAUDE_PROJECT_DIR', '.'), '.claude/hooks/lib'))
from config import read_input, output_decision, block, log_info, log_warn, PROTECTED_COMMANDS

def check_command(cmd: str) -> tuple:
    """Check if command should be allowed."""
    for pattern in PROTECTED_COMMANDS:
        if re.search(pattern, cmd, re.IGNORECASE):
            return 'deny', f"Dangerous command pattern: {pattern}"

    # Warn about sudo
    if 'sudo' in cmd.lower():
        return 'ask', "Command uses sudo - confirm?"

    return 'allow', ""

def main():
    data = read_input()
    tool_input = data.get('tool_input', {})
    command = tool_input.get('command', '')

    if not command:
        sys.exit(0)

    decision, reason = check_command(command)

    if decision == 'deny':
        log_warn(f"Blocked command: {command[:50]}...")
        block(f"BLOCKED: {reason}")
    elif decision == 'ask':
        log_info(f"Asking confirmation: {command[:50]}...")
        output_decision('ask', reason)

    sys.exit(0)

if __name__ == '__main__':
    main()
```

**`.claude/hooks/quality-check.sh`:**
```bash
#!/bin/bash
set -euo pipefail
source "$CLAUDE_PROJECT_DIR/.claude/hooks/lib/common.sh"

input=$(cat)
file_path=$(parse_json "$input" '.tool_input.file_path')

if [[ -z "$file_path" ]] || [[ ! -f "$file_path" ]]; then
    exit 0
fi

log_info "Quality check: $file_path"

# Get file extension
ext="${file_path##*.}"

# Run appropriate linter/formatter
case "$ext" in
    js|jsx|ts|tsx)
        if command -v prettier &> /dev/null; then
            prettier --write "$file_path" 2>/dev/null || true
            log_info "Formatted with prettier"
        fi
        if command -v eslint &> /dev/null; then
            eslint --fix "$file_path" 2>/dev/null || true
            log_info "Linted with eslint"
        fi
        ;;
    py)
        if command -v black &> /dev/null; then
            black --quiet "$file_path" 2>/dev/null || true
            log_info "Formatted with black"
        fi
        if command -v ruff &> /dev/null; then
            ruff check --fix "$file_path" 2>/dev/null || true
            log_info "Linted with ruff"
        fi
        ;;
    go)
        if command -v gofmt &> /dev/null; then
            gofmt -w "$file_path" 2>/dev/null || true
            log_info "Formatted with gofmt"
        fi
        ;;
esac

exit 0
```

**`.claude/hooks/audit-logger.py`:**
```python
#!/usr/bin/env python3
"""Audit log all tool usage."""

import sys
import os
import json
from datetime import datetime
sys.path.insert(0, os.path.join(os.environ.get('CLAUDE_PROJECT_DIR', '.'), '.claude/hooks/lib'))
from config import read_input, PROJECT_DIR

AUDIT_LOG = os.path.join(PROJECT_DIR, '.claude', 'audit.jsonl')

def main():
    data = read_input()

    # Build audit entry
    entry = {
        "timestamp": datetime.now().isoformat(),
        "session_id": data.get('session_id', 'unknown'),
        "tool": data.get('tool_name', 'unknown'),
        "event": data.get('hook_event_name', 'unknown'),
    }

    # Add tool-specific fields
    tool_input = data.get('tool_input', {})
    if 'file_path' in tool_input:
        entry['file'] = tool_input['file_path']
    if 'command' in tool_input:
        entry['command'] = tool_input['command'][:100]  # Truncate

    # Append to audit log
    os.makedirs(os.path.dirname(AUDIT_LOG), exist_ok=True)
    with open(AUDIT_LOG, 'a') as f:
        f.write(json.dumps(entry) + '\n')

    sys.exit(0)

if __name__ == '__main__':
    main()
```

---

## Team Deployment

### Project-Level (Recommended)

Commit hooks to git for team sharing:

```bash
# Add to git
git add .claude/settings.json .claude/hooks/
git commit -m "feat: add code quality hooks"
git push
```

**Advantages:**
- All team members get same hooks
- Version controlled
- Consistent enforcement

### Personal Overrides

Team members can add personal overrides:

**`.claude/settings.local.json`** (gitignored):
```json
{
  "hooks": {
    "PostToolUse": []
  }
}
```

This disables PostToolUse hooks locally while keeping other hooks.

### Gradual Rollout

1. **Phase 1**: Logging only (observe without blocking)
2. **Phase 2**: Warning mode (ask instead of deny)
3. **Phase 3**: Enforcement (deny violations)

```python
# Phase 1: Logging
log_warn(f"Would block: {file_path}")
sys.exit(0)

# Phase 2: Warning
output_decision('ask', f"Policy violation: {reason}")

# Phase 3: Enforcement
block(f"BLOCKED: {reason}")
```

---

## Error Handling

### Graceful Degradation

Hooks should never break Claude:

```python
def main():
    try:
        # Hook logic
        ...
    except Exception as e:
        # Log error but don't block
        log_error(f"Hook failed: {e}")
        sys.exit(0)  # Allow operation to proceed
```

### Timeout Protection

Set appropriate timeouts:

```json
{
  "type": "command",
  "command": "...",
  "timeout": 30
}
```

| Hook Type | Recommended Timeout |
|-----------|-------------------|
| Fast validation | 5-10s |
| File operations | 30s |
| External API calls | 45-60s |
| Code formatting | 60s |
| LLM evaluation | 30-45s |

### Fallback Behavior

Design for failures:

```bash
#!/bin/bash
# Try primary tool, fall back gracefully
if command -v prettier &> /dev/null; then
    prettier --write "$file" || true
elif command -v npx &> /dev/null; then
    npx prettier --write "$file" || true
else
    # No formatter available - skip silently
    exit 0
fi
```

---

## Monitoring & Maintenance

### Log Analysis

```bash
# View recent hook activity
tail -f .claude/hooks.log

# Count operations by tool
cat .claude/audit.jsonl | jq -r '.tool' | sort | uniq -c | sort -rn

# Find blocked operations
grep "BLOCKED" .claude/hooks.log

# Session summary
cat .claude/audit.jsonl | jq -s 'group_by(.session_id) | map({session: .[0].session_id, count: length})'
```

### Health Checks

```bash
#!/bin/bash
# Hook health check script

echo "Checking hook scripts..."

for script in .claude/hooks/*.{sh,py}; do
    if [[ -f "$script" ]]; then
        if [[ ! -x "$script" ]]; then
            echo "WARNING: Not executable: $script"
        fi
        if [[ "$script" == *.sh ]]; then
            bash -n "$script" 2>/dev/null || echo "SYNTAX ERROR: $script"
        fi
        if [[ "$script" == *.py ]]; then
            python3 -m py_compile "$script" 2>/dev/null || echo "SYNTAX ERROR: $script"
        fi
    fi
done

echo "Checking settings.json..."
jq . .claude/settings.json > /dev/null 2>&1 || echo "INVALID JSON: settings.json"

echo "Health check complete"
```

### Updating Hooks

When updating hooks:

1. Test changes in `.claude/settings.local.json` first
2. Run manual tests with mock inputs
3. Deploy to project settings.json
4. Monitor logs for issues

---

## Security Checklist

Before deploying production hooks:

- [ ] All variables properly quoted
- [ ] JSON parsed with jq/json library (not grep/sed)
- [ ] No sensitive data in logs
- [ ] Paths validated and normalized
- [ ] No sudo or privilege escalation
- [ ] Timeouts set appropriately
- [ ] Error handling prevents crashes
- [ ] Scripts are executable
- [ ] Graceful fallbacks for missing tools
- [ ] Audit logging enabled
- [ ] Team has reviewed hook logic
