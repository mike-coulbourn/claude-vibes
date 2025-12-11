# Hooks with External Scripts

Move beyond inline commands to external scripts for complex logic, input parsing, and reusability.

## When to Use

- Need to read tool_input fields (file paths, content)
- Complex conditional logic
- Reusable across multiple hooks
- Need proper JSON parsing
- Want version control for hook logic

## Template Structure

**Configuration** (`settings.json`):
```json
{
  "hooks": {
    "EVENT_NAME": [
      {
        "matcher": "TOOL_PATTERN",
        "hooks": [
          {
            "type": "command",
            "command": "\"$CLAUDE_PROJECT_DIR\"/.claude/hooks/script.sh",
            "timeout": 60
          }
        ]
      }
    ]
  }
}
```

**Script** (`.claude/hooks/script.sh`):
```bash
#!/bin/bash
set -euo pipefail

# Read JSON input from stdin
input=$(cat)

# Parse fields with jq
tool_name=$(echo "$input" | jq -r '.tool_name // empty')
# ... your logic ...

exit 0
```

---

## Input JSON Structure

Every hook receives JSON via stdin with common fields:

```json
{
  "session_id": "abc-123-def",
  "transcript_path": "/path/to/transcript.jsonl",
  "cwd": "/current/working/directory",
  "permission_mode": "default",
  "hook_event_name": "PreToolUse"
}
```

### Event-Specific Fields

**PreToolUse:**
```json
{
  "tool_name": "Write",
  "tool_input": {
    "file_path": "/path/to/file.txt",
    "content": "file content here"
  },
  "tool_use_id": "toolu_abc123"
}
```

**PostToolUse:**
```json
{
  "tool_name": "Write",
  "tool_input": { "file_path": "...", "content": "..." },
  "tool_response": "File written successfully",
  "tool_use_id": "toolu_abc123"
}
```

**UserPromptSubmit:**
```json
{
  "prompt": "Help me refactor this code..."
}
```

**SessionStart:**
```json
{
  "source": "startup"
}
```

**SessionEnd:**
```json
{
  "reason": "clear"
}
```

**Stop/SubagentStop:**
```json
{
  "stop_hook_active": true
}
```

**PreCompact:**
```json
{
  "trigger": "auto",
  "custom_instructions": "preserve recent context"
}
```

---

## Bash Script Template

```bash
#!/bin/bash
set -euo pipefail

# ============================================
# Hook: [NAME]
# Event: [PreToolUse|PostToolUse|etc.]
# Purpose: [What this hook does]
# ============================================

# Read JSON input from stdin
input=$(cat)

# Parse common fields
session_id=$(echo "$input" | jq -r '.session_id // empty')
hook_event=$(echo "$input" | jq -r '.hook_event_name // empty')
cwd=$(echo "$input" | jq -r '.cwd // empty')

# Parse tool-specific fields (for tool events)
tool_name=$(echo "$input" | jq -r '.tool_name // empty')
file_path=$(echo "$input" | jq -r '.tool_input.file_path // empty')
content=$(echo "$input" | jq -r '.tool_input.content // empty')

# ============================================
# YOUR LOGIC HERE
# ============================================

# Example: Log tool usage
echo "$(date '+%Y-%m-%d %H:%M:%S') | $tool_name | $file_path" >> ~/.claude/hook.log

# ============================================
# EXIT CODES
# ============================================
# exit 0  → Success (stdout parsed as JSON if present)
# exit 2  → Blocking error (stderr shown to Claude)
# exit 1+ → Non-blocking error (stderr in debug mode)

exit 0
```

---

## Python Script Template

```python
#!/usr/bin/env python3
"""
Hook: [NAME]
Event: [PreToolUse|PostToolUse|etc.]
Purpose: [What this hook does]
"""

import sys
import json
from datetime import datetime
from pathlib import Path

def main():
    # Read JSON input from stdin
    try:
        data = json.load(sys.stdin)
    except json.JSONDecodeError as e:
        print(f"Failed to parse JSON: {e}", file=sys.stderr)
        sys.exit(1)

    # Parse common fields
    session_id = data.get('session_id', '')
    hook_event = data.get('hook_event_name', '')
    cwd = data.get('cwd', '')

    # Parse tool-specific fields
    tool_name = data.get('tool_name', '')
    tool_input = data.get('tool_input', {})
    file_path = tool_input.get('file_path', '')
    content = tool_input.get('content', '')

    # ==========================================
    # YOUR LOGIC HERE
    # ==========================================

    # Example: Log tool usage
    log_path = Path.home() / '.claude' / 'hook.log'
    with open(log_path, 'a') as f:
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        f.write(f"{timestamp} | {tool_name} | {file_path}\n")

    # ==========================================
    # EXIT CODES
    # ==========================================
    # sys.exit(0)  → Success
    # sys.exit(2)  → Blocking error
    # sys.exit(1)  → Non-blocking error

    sys.exit(0)

if __name__ == '__main__':
    main()
```

---

## Example 1: File Protector

Block writes to sensitive files.

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
            "command": "python3 \"$CLAUDE_PROJECT_DIR\"/.claude/hooks/file-protector.py"
          }
        ]
      }
    ]
  }
}
```

**Script** (`.claude/hooks/file-protector.py`):
```python
#!/usr/bin/env python3
"""Block writes to sensitive files."""

import sys
import json

# Protected patterns
PROTECTED = [
    '.env',
    '.env.local',
    '.env.production',
    'secrets.json',
    'credentials.yml',
    'id_rsa',
    'id_ed25519',
    '.ssh/',
    'token.txt',
    'api_key',
]

def main():
    data = json.load(sys.stdin)
    tool_input = data.get('tool_input', {})
    file_path = tool_input.get('file_path', '')

    # Check against protected patterns
    for pattern in PROTECTED:
        if pattern in file_path.lower():
            print(f"BLOCKED: Cannot modify protected file: {file_path}", file=sys.stderr)
            sys.exit(2)  # Exit code 2 = blocking error

    # Allow the operation
    sys.exit(0)

if __name__ == '__main__':
    main()
```

**Behavior:**
- Blocks Write/Edit to files matching protected patterns
- Exit code 2 stops Claude and shows error message
- Exit code 0 allows the operation

---

## Example 2: Path Logger with Details

Log file operations with full details.

**Configuration:**
```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Write|Edit|Read",
        "hooks": [
          {
            "type": "command",
            "command": "bash \"$CLAUDE_PROJECT_DIR\"/.claude/hooks/path-logger.sh"
          }
        ]
      }
    ]
  }
}
```

**Script** (`.claude/hooks/path-logger.sh`):
```bash
#!/bin/bash
set -euo pipefail

input=$(cat)

tool_name=$(echo "$input" | jq -r '.tool_name')
file_path=$(echo "$input" | jq -r '.tool_input.file_path // "N/A"')
response=$(echo "$input" | jq -r '.tool_response // "N/A"' | head -c 100)

# Get file info if it exists
if [[ -f "$file_path" ]]; then
    file_size=$(stat -f%z "$file_path" 2>/dev/null || stat -c%s "$file_path" 2>/dev/null || echo "unknown")
    file_type=$(file -b "$file_path" 2>/dev/null | head -c 50 || echo "unknown")
else
    file_size="N/A"
    file_type="N/A"
fi

# Log to file
log_file="$HOME/.claude/file-ops.log"
mkdir -p "$(dirname "$log_file")"

cat >> "$log_file" << EOF
---
Time: $(date '+%Y-%m-%d %H:%M:%S')
Tool: $tool_name
Path: $file_path
Size: $file_size bytes
Type: $file_type
Response: $response
EOF

exit 0
```

---

## Example 3: Content Size Validator

Warn about large file writes.

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
            "command": "python3 ~/.claude/hooks/size-validator.py"
          }
        ]
      }
    ]
  }
}
```

**Script** (`~/.claude/hooks/size-validator.py`):
```python
#!/usr/bin/env python3
"""Warn about large file writes."""

import sys
import json

MAX_SIZE_KB = 100  # Warn for files > 100KB

def main():
    data = json.load(sys.stdin)
    tool_input = data.get('tool_input', {})
    content = tool_input.get('content', '')
    file_path = tool_input.get('file_path', '')

    size_kb = len(content.encode('utf-8')) / 1024

    if size_kb > MAX_SIZE_KB:
        # Return JSON to ask user for confirmation
        output = {
            "decision": "ask",
            "reason": f"Large file write: {size_kb:.1f}KB to {file_path}"
        }
        print(json.dumps(output))

    sys.exit(0)

if __name__ == '__main__':
    main()
```

---

## Script Organization

### Personal Hooks
```
~/.claude/
├── settings.json         # Hook configuration
└── hooks/                # Hook scripts
    ├── file-protector.py
    ├── path-logger.sh
    └── size-validator.py
```

### Project Hooks
```
project/
├── .claude/
│   ├── settings.json     # Project hook config
│   └── hooks/            # Project hook scripts
│       ├── format.sh
│       └── validate.py
```

### Path Patterns

**Personal scripts:**
```json
"command": "python3 ~/.claude/hooks/script.py"
```

**Project scripts (with spaces handling):**
```json
"command": "python3 \"$CLAUDE_PROJECT_DIR\"/.claude/hooks/script.py"
```

**Absolute paths:**
```json
"command": "/usr/local/bin/my-hook.sh"
```

---

## Making Scripts Executable

```bash
# Create hooks directory
mkdir -p ~/.claude/hooks

# Create script
cat > ~/.claude/hooks/my-hook.sh << 'EOF'
#!/bin/bash
# ... script content ...
EOF

# Make executable
chmod +x ~/.claude/hooks/my-hook.sh

# Verify
ls -la ~/.claude/hooks/
```

---

## Error Handling Patterns

### Graceful Failures (Bash)
```bash
#!/bin/bash
set -euo pipefail

# Trap errors
trap 'echo "Hook failed: $BASH_COMMAND" >&2; exit 1' ERR

input=$(cat) || { echo "Failed to read stdin" >&2; exit 1; }

tool_name=$(echo "$input" | jq -r '.tool_name') || {
    echo "Failed to parse tool_name" >&2
    exit 1
}
```

### Graceful Failures (Python)
```python
#!/usr/bin/env python3
import sys
import json

def main():
    try:
        data = json.load(sys.stdin)
    except json.JSONDecodeError as e:
        print(f"JSON parse error: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)
        sys.exit(1)

    # ... rest of logic ...

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(f"Hook crashed: {e}", file=sys.stderr)
        sys.exit(1)
```

---

## Testing Scripts

### Create Mock Input
```bash
cat > /tmp/mock-pretool.json << 'EOF'
{
  "session_id": "test-123",
  "hook_event_name": "PreToolUse",
  "cwd": "/home/user/project",
  "permission_mode": "default",
  "tool_name": "Write",
  "tool_input": {
    "file_path": "/home/user/project/test.txt",
    "content": "Hello, World!"
  },
  "tool_use_id": "toolu_test"
}
EOF
```

### Run Script with Mock
```bash
cat /tmp/mock-pretool.json | ~/.claude/hooks/my-hook.sh
echo "Exit code: $?"
```

### Test Edge Cases
```bash
# Empty input
echo '{}' | ~/.claude/hooks/my-hook.sh

# Missing fields
echo '{"tool_name": "Write"}' | ~/.claude/hooks/my-hook.sh

# Malicious path
echo '{"tool_input": {"file_path": "; rm -rf /"}}' | ~/.claude/hooks/my-hook.sh
```

---

## Next Steps

Once comfortable with scripts:
1. **Add decision control** → `templates/with-decisions.md`
2. **Add LLM evaluation** → `templates/with-prompts.md`
3. **Build complete systems** → `templates/production-hooks.md`
