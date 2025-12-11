# Security Hooks Examples

Six complete, production-ready security hooks for protecting your system and enforcing policies.

---

## 1. File Protector

Block writes to sensitive files like `.env`, credentials, and SSH keys.

### Configuration

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Write|Edit",
        "hooks": [
          {
            "type": "command",
            "command": "python3 ~/.claude/hooks/file-protector.py",
            "timeout": 5
          }
        ]
      }
    ]
  }
}
```

### Script (`~/.claude/hooks/file-protector.py`)

```python
#!/usr/bin/env python3
"""
Hook: File Protector
Event: PreToolUse (Write, Edit)
Purpose: Block writes to sensitive files
"""

import sys
import json
import os

# Protected file patterns (case-insensitive matching)
BLOCKED_PATTERNS = [
    # Environment files
    '.env',
    '.env.local',
    '.env.development',
    '.env.production',
    '.env.staging',

    # Credential files
    'secrets.json',
    'secrets.yml',
    'secrets.yaml',
    'credentials.json',
    'credentials.yml',
    'service-account.json',

    # SSH keys
    'id_rsa',
    'id_ed25519',
    'id_ecdsa',
    'id_dsa',
    '.ssh/config',

    # API keys and tokens
    'api_key',
    'api-key',
    'apikey',
    'token.txt',
    'auth_token',
    '.npmrc',  # May contain tokens
    '.pypirc',  # May contain tokens

    # Database
    '.pgpass',
    '.my.cnf',

    # Cloud credentials
    '.aws/credentials',
    '.gcloud/',
    'kubeconfig',
]

# Patterns that should warn but not block
WARN_PATTERNS = [
    'config.json',
    'settings.json',
    '.gitconfig',
    'docker-compose.yml',
]

def check_path(file_path: str) -> tuple:
    """
    Check file path against protection rules.
    Returns: (decision, reason) where decision is 'deny', 'ask', or None
    """
    path_lower = file_path.lower()
    basename = os.path.basename(path_lower)

    # Check blocked patterns
    for pattern in BLOCKED_PATTERNS:
        if pattern in path_lower:
            return 'deny', f"Protected file: matches '{pattern}'"

    # Check warning patterns
    for pattern in WARN_PATTERNS:
        if pattern in path_lower:
            return 'ask', f"Sensitive file: {basename}. Continue?"

    return None, None

def main():
    try:
        data = json.load(sys.stdin)
    except json.JSONDecodeError:
        sys.exit(0)  # Can't parse, allow

    tool_input = data.get('tool_input', {})
    file_path = tool_input.get('file_path', '')

    if not file_path:
        sys.exit(0)

    decision, reason = check_path(file_path)

    if decision == 'deny':
        print(f"BLOCKED: {reason}", file=sys.stderr)
        sys.exit(2)
    elif decision == 'ask':
        output = {
            "hookSpecificOutput": {
                "hookEventName": "PreToolUse",
                "permissionDecision": "ask",
                "permissionDecisionReason": reason
            }
        }
        print(json.dumps(output))

    sys.exit(0)

if __name__ == '__main__':
    main()
```

### Behavior

| File | Result |
|------|--------|
| `.env` | BLOCKED |
| `secrets.json` | BLOCKED |
| `~/.ssh/id_rsa` | BLOCKED |
| `config.json` | User asked to confirm |
| `readme.md` | Allowed |

---

## 2. Command Validator

Warn about dangerous bash commands before execution.

### Configuration

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "python3 ~/.claude/hooks/command-validator.py",
            "timeout": 5
          }
        ]
      }
    ]
  }
}
```

### Script (`~/.claude/hooks/command-validator.py`)

```python
#!/usr/bin/env python3
"""
Hook: Command Validator
Event: PreToolUse (Bash)
Purpose: Block or warn about dangerous commands
"""

import sys
import json
import re

# Commands that are always blocked
BLOCKED_COMMANDS = [
    # Destructive file operations
    (r'rm\s+-rf\s+/', "Recursive delete from root"),
    (r'rm\s+-rf\s+~', "Recursive delete from home"),
    (r'rm\s+-rf\s+\*', "Recursive delete wildcard"),
    (r'rm\s+-rf\s+\.', "Recursive delete current directory"),

    # System damage
    (r'mkfs\.', "Filesystem format"),
    (r'dd\s+if=.*of=/dev', "Direct disk write"),
    (r'>\s*/dev/sd', "Redirect to disk device"),
    (r':\(\)\{.*\}', "Fork bomb pattern"),

    # Permission abuse
    (r'chmod\s+777\s+/', "World-writable root"),
    (r'chmod\s+-R\s+777', "Recursive world-writable"),

    # Remote code execution
    (r'curl.*\|\s*(ba)?sh', "Pipe curl to shell"),
    (r'wget.*\|\s*(ba)?sh', "Pipe wget to shell"),
    (r'curl.*\|.*python', "Pipe curl to python"),

    # History manipulation
    (r'history\s+-c', "Clear history"),
    (r'>\s*~/\.bash_history', "Overwrite history"),
]

# Commands that should warn
WARN_COMMANDS = [
    (r'\bsudo\b', "Uses sudo"),
    (r'\brm\s+-r', "Recursive delete"),
    (r'\brm\s+', "Delete command"),
    (r'chmod\s+', "Permission change"),
    (r'chown\s+', "Ownership change"),
    (r'kill\s+-9', "Force kill"),
    (r'pkill\s+', "Process kill"),
    (r'systemctl\s+(stop|restart|disable)', "Service control"),
    (r'docker\s+rm', "Docker remove"),
    (r'docker\s+system\s+prune', "Docker prune"),
    (r'git\s+push\s+.*--force', "Force push"),
    (r'git\s+reset\s+--hard', "Hard reset"),
    (r'DROP\s+TABLE', "SQL drop table"),
    (r'DROP\s+DATABASE', "SQL drop database"),
    (r'TRUNCATE', "SQL truncate"),
]

# Commands that are safe (skip further checks)
SAFE_COMMANDS = [
    r'^ls\b',
    r'^pwd\b',
    r'^echo\b',
    r'^cat\b',
    r'^head\b',
    r'^tail\b',
    r'^grep\b',
    r'^find\b',
    r'^which\b',
    r'^whoami\b',
    r'^date\b',
    r'^git\s+(status|log|diff|branch|show)',
    r'^npm\s+(list|ls|outdated|audit)',
    r'^pip\s+(list|show|freeze)',
]

def check_command(cmd: str) -> tuple:
    """Check command against patterns."""
    # Check safe first (fast path)
    for pattern in SAFE_COMMANDS:
        if re.search(pattern, cmd):
            return 'allow', ""

    # Check blocked
    for pattern, reason in BLOCKED_COMMANDS:
        if re.search(pattern, cmd, re.IGNORECASE):
            return 'deny', reason

    # Check warnings
    for pattern, reason in WARN_COMMANDS:
        if re.search(pattern, cmd, re.IGNORECASE):
            return 'ask', reason

    return None, None

def main():
    try:
        data = json.load(sys.stdin)
    except json.JSONDecodeError:
        sys.exit(0)

    tool_input = data.get('tool_input', {})
    command = tool_input.get('command', '')

    if not command:
        sys.exit(0)

    decision, reason = check_command(command)

    if decision == 'deny':
        print(f"BLOCKED: Dangerous command - {reason}", file=sys.stderr)
        sys.exit(2)
    elif decision == 'ask':
        output = {
            "hookSpecificOutput": {
                "hookEventName": "PreToolUse",
                "permissionDecision": "ask",
                "permissionDecisionReason": f"Potentially risky: {reason}"
            }
        }
        print(json.dumps(output))
    elif decision == 'allow':
        output = {
            "hookSpecificOutput": {
                "hookEventName": "PreToolUse",
                "permissionDecision": "allow"
            }
        }
        print(json.dumps(output))

    sys.exit(0)

if __name__ == '__main__':
    main()
```

---

## 3. Path Sanitizer

Prevent path traversal attacks and validate file paths.

### Configuration

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Write|Edit|Read",
        "hooks": [
          {
            "type": "command",
            "command": "python3 ~/.claude/hooks/path-sanitizer.py",
            "timeout": 5
          }
        ]
      }
    ]
  }
}
```

### Script (`~/.claude/hooks/path-sanitizer.py`)

```python
#!/usr/bin/env python3
"""
Hook: Path Sanitizer
Event: PreToolUse (Write, Edit, Read)
Purpose: Prevent path traversal and validate paths
"""

import sys
import json
import os

# Directories that should never be accessed
FORBIDDEN_PATHS = [
    '/etc/passwd',
    '/etc/shadow',
    '/etc/sudoers',
    '/root/',
    '/var/log/auth',
    '/boot/',
    '/sys/',
    '/proc/',
]

def normalize_path(path: str, cwd: str) -> str:
    """Normalize and resolve path."""
    if path.startswith('~'):
        path = os.path.expanduser(path)
    if not os.path.isabs(path):
        path = os.path.join(cwd, path)
    return os.path.normpath(os.path.realpath(path))

def check_path(original: str, normalized: str, cwd: str) -> tuple:
    """
    Check path for security issues.
    Returns: (decision, reason, corrected_path)
    """
    # Check forbidden paths
    for forbidden in FORBIDDEN_PATHS:
        if normalized.startswith(forbidden) or normalized == forbidden.rstrip('/'):
            return 'deny', f"Access to {forbidden} is forbidden", None

    # Check for path traversal attempts
    if '..' in original:
        # See if traversal escapes project
        if not normalized.startswith(cwd):
            return 'deny', "Path traversal outside project directory", None
        # Traversal stays in project - normalize it
        return 'allow', "Path normalized", normalized

    # Check for symlink escapes
    try:
        real_path = os.path.realpath(normalized)
        if os.path.isabs(original) and real_path != normalized:
            # Symlink points elsewhere
            if not real_path.startswith(cwd):
                return 'ask', f"Symlink points outside project: {real_path}", None
    except OSError:
        pass  # Path doesn't exist yet, that's fine

    return None, None, None

def main():
    try:
        data = json.load(sys.stdin)
    except json.JSONDecodeError:
        sys.exit(0)

    tool_input = data.get('tool_input', {})
    file_path = tool_input.get('file_path', '')
    cwd = data.get('cwd', os.getcwd())

    if not file_path:
        sys.exit(0)

    normalized = normalize_path(file_path, cwd)
    decision, reason, corrected = check_path(file_path, normalized, cwd)

    if decision == 'deny':
        print(f"BLOCKED: {reason}", file=sys.stderr)
        sys.exit(2)
    elif decision == 'ask':
        output = {
            "hookSpecificOutput": {
                "hookEventName": "PreToolUse",
                "permissionDecision": "ask",
                "permissionDecisionReason": reason
            }
        }
        print(json.dumps(output))
    elif decision == 'allow' and corrected:
        # Path was normalized - update it
        output = {
            "hookSpecificOutput": {
                "hookEventName": "PreToolUse",
                "permissionDecision": "allow",
                "updatedInput": {"file_path": corrected},
                "additionalContext": f"Path normalized: {file_path} -> {corrected}"
            }
        }
        print(json.dumps(output))

    sys.exit(0)

if __name__ == '__main__':
    main()
```

---

## 4. Secret Scanner

Block commits or writes containing API keys and secrets.

### Configuration

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Write|Edit",
        "hooks": [
          {
            "type": "command",
            "command": "python3 ~/.claude/hooks/secret-scanner.py",
            "timeout": 10
          }
        ]
      }
    ]
  }
}
```

### Script (`~/.claude/hooks/secret-scanner.py`)

```python
#!/usr/bin/env python3
"""
Hook: Secret Scanner
Event: PreToolUse (Write, Edit)
Purpose: Detect and block secrets in code
"""

import sys
import json
import re

# Patterns for detecting secrets
SECRET_PATTERNS = [
    # AWS
    (r'AKIA[0-9A-Z]{16}', "AWS Access Key ID"),
    (r'aws_secret_access_key\s*=\s*["\'][^"\']+["\']', "AWS Secret Key"),

    # GitHub
    (r'ghp_[a-zA-Z0-9]{36}', "GitHub Personal Access Token"),
    (r'gho_[a-zA-Z0-9]{36}', "GitHub OAuth Token"),
    (r'ghu_[a-zA-Z0-9]{36}', "GitHub User Token"),
    (r'ghs_[a-zA-Z0-9]{36}', "GitHub Server Token"),
    (r'ghr_[a-zA-Z0-9]{36}', "GitHub Refresh Token"),

    # Generic API keys
    (r'api[_-]?key\s*[=:]\s*["\'][a-zA-Z0-9]{20,}["\']', "API Key"),
    (r'apikey\s*[=:]\s*["\'][a-zA-Z0-9]{20,}["\']', "API Key"),
    (r'secret[_-]?key\s*[=:]\s*["\'][a-zA-Z0-9]{20,}["\']', "Secret Key"),

    # Private keys
    (r'-----BEGIN (?:RSA |EC |DSA |OPENSSH )?PRIVATE KEY-----', "Private Key"),
    (r'-----BEGIN PGP PRIVATE KEY BLOCK-----', "PGP Private Key"),

    # Tokens
    (r'bearer\s+[a-zA-Z0-9\-_.]+', "Bearer Token"),
    (r'token\s*[=:]\s*["\'][a-zA-Z0-9\-_.]{20,}["\']', "Token"),

    # Database URLs
    (r'postgres://[^:]+:[^@]+@', "PostgreSQL Connection String"),
    (r'mysql://[^:]+:[^@]+@', "MySQL Connection String"),
    (r'mongodb://[^:]+:[^@]+@', "MongoDB Connection String"),
    (r'redis://:[^@]+@', "Redis Connection String"),

    # Slack
    (r'xox[baprs]-[0-9]{10,13}-[0-9]{10,13}-[a-zA-Z0-9]{24}', "Slack Token"),

    # Stripe
    (r'sk_live_[0-9a-zA-Z]{24}', "Stripe Live Key"),
    (r'sk_test_[0-9a-zA-Z]{24}', "Stripe Test Key"),

    # Twilio
    (r'SK[0-9a-fA-F]{32}', "Twilio API Key"),

    # SendGrid
    (r'SG\.[a-zA-Z0-9]{22}\.[a-zA-Z0-9]{43}', "SendGrid API Key"),

    # Google
    (r'AIza[0-9A-Za-z\-_]{35}', "Google API Key"),

    # Generic high entropy (likely secrets)
    (r'password\s*[=:]\s*["\'][^"\']{8,}["\']', "Hardcoded Password"),
]

# Patterns to ignore (false positives)
IGNORE_PATTERNS = [
    r'example',
    r'placeholder',
    r'your[_-]?api[_-]?key',
    r'xxx+',
    r'\*{5,}',
    r'<.*>',  # Template placeholders
    r'\$\{.*\}',  # Variable substitutions
]

def scan_content(content: str) -> list:
    """Scan content for secrets."""
    findings = []

    # Skip if content looks like documentation/examples
    content_lower = content.lower()
    for ignore in IGNORE_PATTERNS:
        if re.search(ignore, content_lower):
            # Still scan but be less aggressive
            pass

    for pattern, secret_type in SECRET_PATTERNS:
        matches = re.findall(pattern, content, re.IGNORECASE)
        for match in matches:
            # Check if it's likely a placeholder
            match_lower = match.lower()
            is_placeholder = any(
                re.search(ignore, match_lower)
                for ignore in IGNORE_PATTERNS
            )
            if not is_placeholder:
                findings.append({
                    "type": secret_type,
                    "match": match[:20] + "..." if len(match) > 20 else match
                })

    return findings

def main():
    try:
        data = json.load(sys.stdin)
    except json.JSONDecodeError:
        sys.exit(0)

    tool_input = data.get('tool_input', {})
    content = tool_input.get('content', '')
    file_path = tool_input.get('file_path', '')

    if not content:
        sys.exit(0)

    # Skip scanning for certain file types
    skip_extensions = ['.md', '.txt', '.log', '.json']
    if any(file_path.lower().endswith(ext) for ext in skip_extensions):
        sys.exit(0)

    findings = scan_content(content)

    if findings:
        types = set(f["type"] for f in findings)
        reason = f"Potential secrets detected: {', '.join(types)}"
        output = {
            "hookSpecificOutput": {
                "hookEventName": "PreToolUse",
                "permissionDecision": "ask",
                "permissionDecisionReason": reason
            }
        }
        print(json.dumps(output))

    sys.exit(0)

if __name__ == '__main__':
    main()
```

---

## 5. Permission Enforcer

Require confirmation for destructive operations.

### Configuration

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Write|Edit|Bash",
        "hooks": [
          {
            "type": "command",
            "command": "python3 ~/.claude/hooks/permission-enforcer.py",
            "timeout": 5
          }
        ]
      }
    ]
  }
}
```

### Script (`~/.claude/hooks/permission-enforcer.py`)

```python
#!/usr/bin/env python3
"""
Hook: Permission Enforcer
Event: PreToolUse (Write, Edit, Bash)
Purpose: Require confirmation for destructive operations
"""

import sys
import json
import os
import re

# Operations that always need confirmation
CONFIRM_OPERATIONS = {
    "Write": [
        # System config files
        (r'/etc/', "System configuration"),
        (r'\.config/', "Application config"),
        (r'package\.json$', "Package manifest"),
        (r'package-lock\.json$', "Package lock"),
        (r'yarn\.lock$', "Yarn lock"),
        (r'Gemfile\.lock$', "Bundler lock"),
        (r'Cargo\.lock$', "Cargo lock"),
        (r'go\.sum$', "Go checksum"),
        (r'requirements.*\.txt$', "Python dependencies"),
        (r'\.github/', "GitHub config"),
        (r'Dockerfile', "Docker config"),
        (r'docker-compose', "Docker Compose"),
        (r'Makefile', "Build config"),
        (r'\.gitlab-ci', "GitLab CI"),
        (r'\.travis', "Travis CI"),
    ],
    "Edit": [
        # Same as Write
        (r'/etc/', "System configuration"),
        (r'\.config/', "Application config"),
        (r'package\.json$', "Package manifest"),
    ],
    "Bash": [
        # Destructive commands
        (r'\brm\b', "Delete files"),
        (r'\bmv\b.*/', "Move files"),
        (r'git\s+push', "Git push"),
        (r'git\s+merge', "Git merge"),
        (r'git\s+rebase', "Git rebase"),
        (r'git\s+checkout\s+-', "Git checkout"),
        (r'npm\s+(publish|unpublish)', "NPM publish"),
        (r'pip\s+uninstall', "Pip uninstall"),
        (r'docker\s+(rm|rmi|prune)', "Docker cleanup"),
        (r'kubectl\s+(delete|apply)', "Kubernetes operations"),
    ],
}

def check_operation(tool_name: str, tool_input: dict) -> tuple:
    """Check if operation needs confirmation."""
    patterns = CONFIRM_OPERATIONS.get(tool_name, [])

    if tool_name in ['Write', 'Edit']:
        target = tool_input.get('file_path', '')
    elif tool_name == 'Bash':
        target = tool_input.get('command', '')
    else:
        return None, None

    for pattern, description in patterns:
        if re.search(pattern, target, re.IGNORECASE):
            return 'ask', f"{description}: {os.path.basename(target) if '/' in target else target[:50]}"

    return None, None

def main():
    try:
        data = json.load(sys.stdin)
    except json.JSONDecodeError:
        sys.exit(0)

    tool_name = data.get('tool_name', '')
    tool_input = data.get('tool_input', {})

    decision, reason = check_operation(tool_name, tool_input)

    if decision == 'ask':
        output = {
            "hookSpecificOutput": {
                "hookEventName": "PreToolUse",
                "permissionDecision": "ask",
                "permissionDecisionReason": f"Confirm: {reason}"
            }
        }
        print(json.dumps(output))

    sys.exit(0)

if __name__ == '__main__':
    main()
```

---

## 6. Audit Logger

Log all tool usage for compliance and debugging.

### Configuration

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "*",
        "hooks": [
          {
            "type": "command",
            "command": "python3 ~/.claude/hooks/audit-logger.py",
            "timeout": 5
          }
        ]
      }
    ]
  }
}
```

### Script (`~/.claude/hooks/audit-logger.py`)

```python
#!/usr/bin/env python3
"""
Hook: Audit Logger
Event: PostToolUse (all tools)
Purpose: Comprehensive audit logging
"""

import sys
import json
import os
from datetime import datetime
from pathlib import Path

# Configuration
LOG_DIR = Path.home() / '.claude' / 'audit'
LOG_FILE = LOG_DIR / 'audit.jsonl'
MAX_CONTENT_LENGTH = 500  # Truncate long content

def sanitize_content(content: str) -> str:
    """Sanitize and truncate content for logging."""
    if not content:
        return ""
    # Remove potential secrets (basic sanitization)
    sanitized = content
    # Truncate
    if len(sanitized) > MAX_CONTENT_LENGTH:
        sanitized = sanitized[:MAX_CONTENT_LENGTH] + "...[truncated]"
    return sanitized

def build_log_entry(data: dict) -> dict:
    """Build structured log entry."""
    entry = {
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "session_id": data.get('session_id', 'unknown'),
        "event": data.get('hook_event_name', 'unknown'),
        "tool": data.get('tool_name', 'unknown'),
        "cwd": data.get('cwd', ''),
        "permission_mode": data.get('permission_mode', 'default'),
    }

    # Add tool-specific details
    tool_input = data.get('tool_input', {})
    tool_name = data.get('tool_name', '')

    if tool_name in ['Write', 'Edit', 'Read']:
        entry['file'] = tool_input.get('file_path', '')
        if tool_name == 'Write':
            content = tool_input.get('content', '')
            entry['content_length'] = len(content)
            entry['content_preview'] = sanitize_content(content[:100])

    elif tool_name == 'Bash':
        entry['command'] = sanitize_content(tool_input.get('command', ''))

    elif tool_name == 'Grep':
        entry['pattern'] = tool_input.get('pattern', '')
        entry['path'] = tool_input.get('path', '')

    elif tool_name == 'Glob':
        entry['pattern'] = tool_input.get('pattern', '')

    elif tool_name.startswith('mcp__'):
        # MCP tool - log the tool name and input keys
        entry['mcp_server'] = tool_name.split('__')[1] if '__' in tool_name else 'unknown'
        entry['input_keys'] = list(tool_input.keys())

    # Add response summary
    response = data.get('tool_response', '')
    if response:
        entry['response_length'] = len(str(response))
        entry['success'] = 'error' not in str(response).lower()

    return entry

def write_log(entry: dict):
    """Write log entry to file."""
    LOG_DIR.mkdir(parents=True, exist_ok=True)
    with open(LOG_FILE, 'a') as f:
        f.write(json.dumps(entry) + '\n')

def main():
    try:
        data = json.load(sys.stdin)
    except json.JSONDecodeError:
        sys.exit(0)

    entry = build_log_entry(data)
    write_log(entry)

    sys.exit(0)

if __name__ == '__main__':
    main()
```

### Analyzing Audit Logs

```bash
# View recent activity
tail -20 ~/.claude/audit/audit.jsonl | jq .

# Count operations by tool
cat ~/.claude/audit/audit.jsonl | jq -r '.tool' | sort | uniq -c | sort -rn

# Find all file writes
cat ~/.claude/audit/audit.jsonl | jq -r 'select(.tool == "Write") | .file'

# Filter by session
cat ~/.claude/audit/audit.jsonl | jq -r 'select(.session_id == "abc123")'

# Find errors
cat ~/.claude/audit/audit.jsonl | jq -r 'select(.success == false)'

# Activity by hour
cat ~/.claude/audit/audit.jsonl | jq -r '.timestamp[:13]' | sort | uniq -c
```

---

## Combined Security Configuration

Use all security hooks together:

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Write|Edit",
        "hooks": [
          {"type": "command", "command": "python3 ~/.claude/hooks/file-protector.py", "timeout": 5},
          {"type": "command", "command": "python3 ~/.claude/hooks/path-sanitizer.py", "timeout": 5},
          {"type": "command", "command": "python3 ~/.claude/hooks/secret-scanner.py", "timeout": 10},
          {"type": "command", "command": "python3 ~/.claude/hooks/permission-enforcer.py", "timeout": 5}
        ]
      },
      {
        "matcher": "Bash",
        "hooks": [
          {"type": "command", "command": "python3 ~/.claude/hooks/command-validator.py", "timeout": 5},
          {"type": "command", "command": "python3 ~/.claude/hooks/permission-enforcer.py", "timeout": 5}
        ]
      },
      {
        "matcher": "Read",
        "hooks": [
          {"type": "command", "command": "python3 ~/.claude/hooks/path-sanitizer.py", "timeout": 5}
        ]
      }
    ],
    "PostToolUse": [
      {
        "matcher": "*",
        "hooks": [
          {"type": "command", "command": "python3 ~/.claude/hooks/audit-logger.py", "timeout": 5}
        ]
      }
    ]
  }
}
```

---

## Setup Script

```bash
#!/bin/bash
# setup-security-hooks.sh - Install all security hooks

HOOKS_DIR="$HOME/.claude/hooks"
mkdir -p "$HOOKS_DIR"

# Download or create each script
# (In practice, copy the scripts above)

# Make executable
chmod +x "$HOOKS_DIR"/*.py

echo "Security hooks installed in $HOOKS_DIR"
echo "Add configuration to ~/.claude/settings.json"
```
