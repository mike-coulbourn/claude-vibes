# Hooks with Decision Control

Take full control of Claude's actions: allow, deny, ask for permission, or modify inputs before execution.

## When to Use

- Block dangerous operations conditionally
- Require user confirmation for risky actions
- Modify tool inputs before execution
- Override the permission system
- Implement custom security policies

## The Decision Flow

```
PreToolUse Hook Triggered
         │
         ▼
    Parse Input
         │
         ▼
    Evaluate Logic
         │
         ├─► Exit 0 + {"decision": "allow"}  → Tool executes (bypasses permissions)
         │
         ├─► Exit 0 + {"decision": "deny"}   → Tool blocked (shows reason)
         │
         ├─► Exit 0 + {"decision": "ask"}    → User prompted for confirmation
         │
         ├─► Exit 0 + no output              → Normal permission flow
         │
         └─► Exit 2 + stderr message         → Tool blocked (shows stderr)
```

---

## hookSpecificOutput Structure

### For PreToolUse

```json
{
  "hookSpecificOutput": {
    "hookEventName": "PreToolUse",
    "permissionDecision": "allow|deny|ask",
    "permissionDecisionReason": "Explanation shown to user",
    "updatedInput": {
      "file_path": "/modified/path.txt",
      "content": "Modified content"
    },
    "additionalContext": "Info added for Claude"
  }
}
```

| Field | Purpose |
|-------|---------|
| `permissionDecision` | Control action: allow, deny, or ask |
| `permissionDecisionReason` | Explanation shown when blocking/asking |
| `updatedInput` | Modify tool parameters before execution |
| `additionalContext` | Add info for Claude to see |

### For UserPromptSubmit

```json
{
  "hookSpecificOutput": {
    "hookEventName": "UserPromptSubmit",
    "additionalContext": "Context injected into the prompt"
  }
}
```

### For Stop/SubagentStop

```json
{
  "continue": true,
  "stopReason": "Task not yet complete - missing X, Y, Z"
}
```

---

## Decision Options

### allow — Bypass Permissions
Tool executes immediately, no permission prompt shown.

```python
output = {
    "hookSpecificOutput": {
        "hookEventName": "PreToolUse",
        "permissionDecision": "allow",
        "permissionDecisionReason": "Auto-approved: safe operation"
    }
}
print(json.dumps(output))
sys.exit(0)
```

### deny — Block Execution
Tool is blocked, reason shown to Claude.

```python
output = {
    "hookSpecificOutput": {
        "hookEventName": "PreToolUse",
        "permissionDecision": "deny",
        "permissionDecisionReason": "Blocked: file is protected"
    }
}
print(json.dumps(output))
sys.exit(0)
```

### ask — Prompt User
User is asked for confirmation with custom message.

```python
output = {
    "hookSpecificOutput": {
        "hookEventName": "PreToolUse",
        "permissionDecision": "ask",
        "permissionDecisionReason": "This will modify a config file. Continue?"
    }
}
print(json.dumps(output))
sys.exit(0)
```

### Exit 2 — Hard Block
Alternative to deny — shows stderr message directly.

```python
print("BLOCKED: Cannot delete production files", file=sys.stderr)
sys.exit(2)
```

---

## Example 1: Smart File Protector

Block, warn, or allow based on file sensitivity.

**Configuration:**
```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Write|Edit",
        "hooks": [
          {
            "type": "command",
            "command": "python3 ~/.claude/hooks/smart-protector.py"
          }
        ]
      }
    ]
  }
}
```

**Script** (`~/.claude/hooks/smart-protector.py`):
```python
#!/usr/bin/env python3
"""Smart file protector with tiered permissions."""

import sys
import json
import os

# Tiered protection levels
BLOCKED = ['.env', 'secrets', 'credentials', 'id_rsa', 'id_ed25519']
WARN = ['config', 'settings', '.json', '.yml', '.yaml', 'package.json']
ALLOW = ['.md', '.txt', '.log']

def get_decision(file_path):
    """Determine protection level for file."""
    path_lower = file_path.lower()
    basename = os.path.basename(path_lower)

    # Check blocked patterns
    for pattern in BLOCKED:
        if pattern in path_lower:
            return 'deny', f"Protected file: {basename} matches '{pattern}'"

    # Check warning patterns
    for pattern in WARN:
        if pattern in path_lower:
            return 'ask', f"Config file: {basename}. Modify?"

    # Check auto-allow patterns
    for pattern in ALLOW:
        if path_lower.endswith(pattern):
            return 'allow', f"Safe file type: {pattern}"

    # Default: normal permission flow
    return None, None

def main():
    data = json.load(sys.stdin)
    tool_input = data.get('tool_input', {})
    file_path = tool_input.get('file_path', '')

    decision, reason = get_decision(file_path)

    if decision:
        output = {
            "hookSpecificOutput": {
                "hookEventName": "PreToolUse",
                "permissionDecision": decision,
                "permissionDecisionReason": reason
            }
        }
        print(json.dumps(output))

    sys.exit(0)

if __name__ == '__main__':
    main()
```

**Behavior:**
- `.env` files → Blocked (denied)
- `config.json` files → User asked for confirmation
- `.md` files → Auto-allowed (no prompt)
- Other files → Normal permission flow

---

## Example 2: Command Validator

Validate bash commands with tiered safety.

**Configuration:**
```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "python3 ~/.claude/hooks/command-validator.py"
          }
        ]
      }
    ]
  }
}
```

**Script** (`~/.claude/hooks/command-validator.py`):
```python
#!/usr/bin/env python3
"""Validate bash commands for safety."""

import sys
import json
import re

# Command patterns by risk level
BLOCKED_PATTERNS = [
    r'rm\s+-rf\s+/',           # rm -rf /
    r'rm\s+-rf\s+~',           # rm -rf ~
    r'>\s*/dev/sd',            # Write to disk devices
    r'mkfs\.',                 # Format filesystems
    r'dd\s+if=.*of=/dev',      # dd to devices
    r'chmod\s+777',            # World-writable
    r'curl.*\|\s*sh',          # Pipe curl to shell
    r'wget.*\|\s*sh',          # Pipe wget to shell
]

WARN_PATTERNS = [
    r'\bsudo\b',               # sudo usage
    r'\brm\b',                 # Any rm command
    r'>\s*/',                  # Redirect to root paths
    r'chmod',                  # Permission changes
    r'chown',                  # Ownership changes
]

SAFE_PATTERNS = [
    r'^git\s',                 # Git commands
    r'^npm\s',                 # NPM commands
    r'^yarn\s',                # Yarn commands
    r'^ls\b',                  # List files
    r'^cat\b',                 # Cat files
    r'^echo\b',                # Echo
]

def check_command(cmd):
    """Check command against patterns."""
    # Check blocked first
    for pattern in BLOCKED_PATTERNS:
        if re.search(pattern, cmd, re.IGNORECASE):
            return 'deny', f"Dangerous command blocked: matches '{pattern}'"

    # Check safe patterns
    for pattern in SAFE_PATTERNS:
        if re.search(pattern, cmd):
            return 'allow', "Safe command auto-approved"

    # Check warning patterns
    for pattern in WARN_PATTERNS:
        if re.search(pattern, cmd, re.IGNORECASE):
            return 'ask', f"Potentially risky command. Continue?"

    # Default: normal flow
    return None, None

def main():
    data = json.load(sys.stdin)
    tool_input = data.get('tool_input', {})
    command = tool_input.get('command', '')

    decision, reason = check_command(command)

    if decision:
        output = {
            "hookSpecificOutput": {
                "hookEventName": "PreToolUse",
                "permissionDecision": decision,
                "permissionDecisionReason": reason
            }
        }
        print(json.dumps(output))

    sys.exit(0)

if __name__ == '__main__':
    main()
```

---

## Example 3: Input Modifier

Modify tool inputs before execution.

**Use case:** Add license headers to all new files.

**Configuration:**
```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Write",
        "hooks": [
          {
            "type": "command",
            "command": "python3 ~/.claude/hooks/license-injector.py"
          }
        ]
      }
    ]
  }
}
```

**Script** (`~/.claude/hooks/license-injector.py`):
```python
#!/usr/bin/env python3
"""Add license headers to new source files."""

import sys
import json
import os

LICENSE_HEADER = """/*
 * Copyright (c) 2025 MyCompany
 * Licensed under the MIT License
 */

"""

# File extensions that should have license headers
SOURCE_EXTENSIONS = ['.js', '.ts', '.jsx', '.tsx', '.py', '.java', '.go']

def should_add_license(file_path, content):
    """Check if file needs license header."""
    ext = os.path.splitext(file_path)[1].lower()

    if ext not in SOURCE_EXTENSIONS:
        return False

    # Don't add if already has license/copyright
    if 'copyright' in content.lower() or 'license' in content.lower():
        return False

    # Only add to new files (Write creates new files)
    if os.path.exists(file_path):
        return False

    return True

def main():
    data = json.load(sys.stdin)
    tool_input = data.get('tool_input', {})
    file_path = tool_input.get('file_path', '')
    content = tool_input.get('content', '')

    if should_add_license(file_path, content):
        # Modify the content
        new_content = LICENSE_HEADER + content

        output = {
            "hookSpecificOutput": {
                "hookEventName": "PreToolUse",
                "permissionDecision": "allow",
                "permissionDecisionReason": "Added license header",
                "updatedInput": {
                    "content": new_content
                }
            }
        }
        print(json.dumps(output))

    sys.exit(0)

if __name__ == '__main__':
    main()
```

**Behavior:**
- New `.js`, `.ts`, `.py` files get license header prepended
- Existing files or files with license → unchanged
- Non-source files → unchanged

---

## Example 4: Path Normalizer

Normalize and validate file paths.

**Configuration:**
```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Write|Edit|Read",
        "hooks": [
          {
            "type": "command",
            "command": "python3 ~/.claude/hooks/path-normalizer.py"
          }
        ]
      }
    ]
  }
}
```

**Script** (`~/.claude/hooks/path-normalizer.py`):
```python
#!/usr/bin/env python3
"""Normalize paths and block traversal attacks."""

import sys
import json
import os

def normalize_path(path, cwd):
    """Normalize path and check for traversal."""
    # Expand ~ and make absolute
    if path.startswith('~'):
        path = os.path.expanduser(path)
    elif not os.path.isabs(path):
        path = os.path.join(cwd, path)

    # Normalize (resolve .., ., etc.)
    normalized = os.path.normpath(path)

    return normalized

def is_path_traversal(original, normalized, cwd):
    """Check if path attempts to escape project."""
    # Check for .. in original
    if '..' in original:
        # Allow if still within cwd
        if normalized.startswith(cwd):
            return False
        return True
    return False

def main():
    data = json.load(sys.stdin)
    tool_input = data.get('tool_input', {})
    file_path = tool_input.get('file_path', '')
    cwd = data.get('cwd', os.getcwd())

    if not file_path:
        sys.exit(0)

    normalized = normalize_path(file_path, cwd)

    # Check for path traversal attack
    if is_path_traversal(file_path, normalized, cwd):
        output = {
            "hookSpecificOutput": {
                "hookEventName": "PreToolUse",
                "permissionDecision": "deny",
                "permissionDecisionReason": f"Path traversal blocked: {file_path}"
            }
        }
        print(json.dumps(output))
        sys.exit(0)

    # If path was modified, update it
    if normalized != file_path:
        output = {
            "hookSpecificOutput": {
                "hookEventName": "PreToolUse",
                "permissionDecision": "allow",
                "updatedInput": {
                    "file_path": normalized
                },
                "additionalContext": f"Path normalized: {file_path} -> {normalized}"
            }
        }
        print(json.dumps(output))

    sys.exit(0)

if __name__ == '__main__':
    main()
```

---

## Example 5: Context Injector

Add project context to user prompts.

**Configuration:**
```json
{
  "hooks": {
    "UserPromptSubmit": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "python3 ~/.claude/hooks/context-injector.py"
          }
        ]
      }
    ]
  }
}
```

**Script** (`~/.claude/hooks/context-injector.py`):
```python
#!/usr/bin/env python3
"""Inject project context into prompts."""

import sys
import json
import os

def get_project_context(cwd):
    """Build project context string."""
    context_parts = []

    # Check for common project files
    if os.path.exists(os.path.join(cwd, 'package.json')):
        context_parts.append("This is a Node.js project.")

    if os.path.exists(os.path.join(cwd, 'requirements.txt')):
        context_parts.append("This is a Python project.")

    if os.path.exists(os.path.join(cwd, 'go.mod')):
        context_parts.append("This is a Go project.")

    # Check for .env.example (hint about environment)
    if os.path.exists(os.path.join(cwd, '.env.example')):
        context_parts.append("Project uses environment variables (see .env.example).")

    # Check for docker
    if os.path.exists(os.path.join(cwd, 'docker-compose.yml')):
        context_parts.append("Project uses Docker Compose.")

    if context_parts:
        return "Project Context: " + " ".join(context_parts)

    return ""

def main():
    data = json.load(sys.stdin)
    cwd = data.get('cwd', os.getcwd())

    context = get_project_context(cwd)

    if context:
        output = {
            "hookSpecificOutput": {
                "hookEventName": "UserPromptSubmit",
                "additionalContext": context
            }
        }
        print(json.dumps(output))

    sys.exit(0)

if __name__ == '__main__':
    main()
```

---

## Decision Matrix

| Scenario | Decision | Exit Code |
|----------|----------|-----------|
| Safe operation, skip prompts | `allow` | 0 |
| Dangerous, must block | `deny` | 0 |
| Risky, ask user | `ask` | 0 |
| Hard block with message | N/A | 2 |
| Normal permission flow | No output | 0 |
| Modify input, allow | `allow` + `updatedInput` | 0 |

---

## Testing Decision Hooks

### Test deny decision
```bash
echo '{"tool_input": {"file_path": ".env"}}' | python3 hook.py
# Should output: {"hookSpecificOutput": {"permissionDecision": "deny", ...}}
```

### Test allow decision
```bash
echo '{"tool_input": {"file_path": "readme.md"}}' | python3 hook.py
# Should output: {"hookSpecificOutput": {"permissionDecision": "allow", ...}}
# Or no output (normal flow)
```

### Test ask decision
```bash
echo '{"tool_input": {"file_path": "config.json"}}' | python3 hook.py
# Should output: {"hookSpecificOutput": {"permissionDecision": "ask", ...}}
```

### Test input modification
```bash
echo '{"tool_input": {"file_path": "./test.js", "content": "code"}, "cwd": "/project"}' | python3 hook.py
# Should output modified file_path or content
```

---

## Next Steps

Once comfortable with decisions:
1. **Add LLM evaluation** → `templates/with-prompts.md`
2. **Build complete systems** → `templates/production-hooks.md`
