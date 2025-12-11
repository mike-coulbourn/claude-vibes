# Hooks Best Practices

Design, security, and deployment guidance for production-quality hooks.

---

## Design Principles

### 1. Single Responsibility

Each hook should do ONE thing well.

```json
// GOOD - separate hooks for separate concerns
{
  "PostToolUse": [
    {
      "matcher": "Write|Edit",
      "hooks": [
        {"type": "command", "command": "~/.claude/hooks/format.sh"},
        {"type": "command", "command": "~/.claude/hooks/lint.sh"},
        {"type": "command", "command": "~/.claude/hooks/audit.sh"}
      ]
    }
  ]
}

// BAD - one hook doing everything
{
  "PostToolUse": [
    {
      "matcher": "Write|Edit",
      "hooks": [
        {"type": "command", "command": "~/.claude/hooks/do-everything.sh"}
      ]
    }
  ]
}
```

### 2. Fail-Safe Defaults

When uncertain, default to safety.

```python
# GOOD - block on error
try:
    result = validate(data)
except Exception:
    print("Validation failed - blocking", file=sys.stderr)
    sys.exit(2)  # Block

# BAD - allow on error
try:
    result = validate(data)
except Exception:
    sys.exit(0)  # Allow anyway
```

### 3. Fast and Non-Blocking

Hooks should be fast. Slow hooks degrade user experience.

| Operation | Target Time |
|-----------|-------------|
| Simple validation | < 1 second |
| File formatting | < 5 seconds |
| Linting | < 10 seconds |
| Test running | < 30 seconds |

```json
// Set appropriate timeouts
{
  "type": "command",
  "command": "~/.claude/hooks/fast-check.sh",
  "timeout": 5  // Fast operations
}

{
  "type": "command",
  "command": "~/.claude/hooks/run-tests.sh",
  "timeout": 120  // Slow operations
}
```

### 4. Graceful Degradation

Hooks should never break Claude's core functionality.

```bash
#!/bin/bash
# GOOD - continue if formatter not installed
if command -v prettier &> /dev/null; then
    prettier --write "$file" || true
fi
exit 0

# BAD - fail if formatter not installed
prettier --write "$file"  # Crashes if not installed
```

### 5. Idempotent Operations

Running a hook multiple times should produce the same result.

```python
# GOOD - idempotent
def add_license_header(content):
    if content.startswith("/* License */"):
        return content  # Already has header
    return "/* License */\n" + content

# BAD - not idempotent
def add_license_header(content):
    return "/* License */\n" + content  # Adds multiple headers
```

---

## Security Best Practices

### 1. Quote All Variables

**CRITICAL**: Unquoted variables enable command injection.

```bash
# DANGEROUS - command injection
file_path=$(echo "$input" | jq -r '.tool_input.file_path')
rm $file_path  # If file_path is "; rm -rf /", disaster

# SAFE - properly quoted
file_path=$(echo "$input" | jq -r '.tool_input.file_path')
rm -- "$file_path"  # -- prevents flag injection
```

### 2. Parse JSON Properly

Never use grep/sed/awk to parse JSON.

```bash
# DANGEROUS - regex parsing
file_path=$(echo "$input" | grep -o '"file_path":"[^"]*"' | cut -d'"' -f4)

# SAFE - proper JSON parsing
file_path=$(echo "$input" | jq -r '.tool_input.file_path')
```

```python
# DANGEROUS - string manipulation
import re
match = re.search(r'"file_path":"([^"]*)"', input_str)

# SAFE - proper JSON parsing
import json
data = json.load(sys.stdin)
file_path = data.get('tool_input', {}).get('file_path', '')
```

### 3. Validate and Sanitize Paths

```python
import os

def safe_path(path: str, allowed_root: str) -> str:
    """Validate and normalize path."""
    # Expand user home
    if path.startswith('~'):
        path = os.path.expanduser(path)

    # Make absolute
    path = os.path.abspath(path)

    # Normalize (resolve .., .)
    path = os.path.normpath(path)

    # Check for traversal
    if not path.startswith(allowed_root):
        raise ValueError(f"Path outside allowed directory: {path}")

    return path
```

### 4. Never Log Sensitive Data

```python
# DANGEROUS - logs secrets
def process(data):
    print(f"Processing: {data}")  # May contain secrets

# SAFE - sanitize before logging
def process(data):
    safe_data = {k: v for k, v in data.items() if k not in ['content', 'token']}
    print(f"Processing tool: {safe_data.get('tool_name')}")
```

### 5. No Privilege Escalation

```bash
# DANGEROUS - never use sudo in hooks
sudo rm -rf "$path"
sudo chmod 777 "$file"

# SAFE - operate with user permissions only
rm -- "$path"
chmod 644 "$file"
```

### 6. Audit Project Hooks

Before running code from a repository:

```bash
# Review project hooks before trusting
cat .claude/settings.json | jq '.hooks'

# Check hook scripts
find .claude/hooks -type f -name "*.sh" -exec cat {} \;
```

### 7. Use Separate Processes

Don't execute untrusted input in the same process.

```python
# DANGEROUS - eval of untrusted input
eval(data.get('code'))

# SAFE - subprocess with restrictions
import subprocess
subprocess.run(
    ['python3', '-c', validated_code],
    timeout=10,
    capture_output=True
)
```

---

## Security Checklist

Before deploying hooks:

- [ ] All shell variables are quoted (`"$var"`)
- [ ] JSON is parsed with jq/json library (not grep/sed)
- [ ] Paths are validated and normalized
- [ ] No sensitive data in logs or output
- [ ] No sudo or privilege escalation
- [ ] Scripts tested manually first
- [ ] Project hooks reviewed before running
- [ ] Timeouts set appropriately
- [ ] Error handling prevents crashes
- [ ] Exit codes are correct (2 for blocking)

---

## Performance Optimization

### 1. Use Appropriate Timeouts

```json
{
  "hooks": {
    "PreToolUse": [{
      "matcher": "Write",
      "hooks": [{
        "type": "command",
        "command": "~/.claude/hooks/validate.sh",
        "timeout": 5  // Short - validation should be fast
      }]
    }],
    "PostToolUse": [{
      "matcher": "Write",
      "hooks": [{
        "type": "command",
        "command": "~/.claude/hooks/format.sh",
        "timeout": 30  // Longer - formatting takes time
      }]
    }]
  }
}
```

### 2. Check Tool Availability Once

```bash
#!/bin/bash
# Check at script start, not per-file
if ! command -v prettier &> /dev/null; then
    exit 0  # Skip if not installed
fi

# Now use prettier without checking each time
prettier --write "$file"
```

### 3. Batch Operations When Possible

```python
# Instead of running linter per-file in hook,
# collect files and run once at session end
# or use PostToolUse with debouncing
```

### 4. Use Early Returns

```python
def main():
    data = json.load(sys.stdin)
    file_path = data.get('tool_input', {}).get('file_path', '')

    # Early returns for common skip cases
    if not file_path:
        sys.exit(0)

    if '/node_modules/' in file_path:
        sys.exit(0)

    if not file_path.endswith(('.js', '.ts')):
        sys.exit(0)

    # Expensive operations only if needed
    run_expensive_validation(file_path)
```

---

## Team Deployment

### Project Hooks (Recommended)

Commit hooks to version control for team sharing:

```
project/
├── .claude/
│   ├── settings.json     # Hook configuration
│   └── hooks/            # Hook scripts
│       ├── format.sh
│       └── validate.py
├── .gitignore
└── ...
```

**.gitignore:**
```gitignore
# Don't ignore hooks
!.claude/
!.claude/hooks/
!.claude/settings.json

# But ignore local overrides
.claude/settings.local.json
```

### Personal Overrides

Allow team members to customize:

**.claude/settings.local.json** (gitignored):
```json
{
  "hooks": {
    "PostToolUse": []
  }
}
```

### Gradual Rollout Strategy

1. **Phase 1: Logging Only**
   ```python
   # Just log, don't block
   log_warn(f"Would block: {file_path}")
   sys.exit(0)
   ```

2. **Phase 2: Warning Mode**
   ```python
   # Ask instead of block
   output = {"hookSpecificOutput": {"permissionDecision": "ask", ...}}
   ```

3. **Phase 3: Enforcement**
   ```python
   # Block violations
   print("BLOCKED", file=sys.stderr)
   sys.exit(2)
   ```

### Documentation for Team

Include a README in hooks directory:

```markdown
# Project Hooks

## What These Do
- format.sh: Auto-formats code after writes
- validate.py: Blocks writes to sensitive files

## How to Disable Locally
Create `.claude/settings.local.json`:
```json
{"hooks": {"PostToolUse": []}}
```

## Requirements
- Python 3.8+
- jq
- prettier (optional)
```

---

## Error Handling

### Always Handle stdin Errors

```python
try:
    data = json.load(sys.stdin)
except json.JSONDecodeError:
    # Can't parse - allow operation
    sys.exit(0)
except Exception as e:
    # Log but don't block
    print(f"Hook error: {e}", file=sys.stderr)
    sys.exit(0)
```

### Use Try/Except Around External Commands

```python
try:
    result = subprocess.run(
        ['prettier', '--write', file_path],
        capture_output=True,
        timeout=30
    )
except subprocess.TimeoutExpired:
    print("Formatter timed out", file=sys.stderr)
except FileNotFoundError:
    pass  # Formatter not installed, skip
```

### Log Errors for Debugging

```python
import logging
from pathlib import Path

log_file = Path.home() / '.claude' / 'hooks.log'
logging.basicConfig(filename=log_file, level=logging.DEBUG)

try:
    # Hook logic
    pass
except Exception as e:
    logging.exception("Hook failed")
    sys.exit(0)  # Don't block on errors
```

---

## Anti-Patterns to Avoid

### 1. Blocking on Non-Critical Errors

```python
# BAD - blocks if formatter fails
result = subprocess.run(['prettier', file])
if result.returncode != 0:
    sys.exit(2)  # Blocks Claude

# GOOD - log and continue
result = subprocess.run(['prettier', file])
if result.returncode != 0:
    log_warning(f"Formatter failed: {result.stderr}")
    sys.exit(0)  # Don't block
```

### 2. Infinite Loops

```python
# BAD - hook modifies file, triggers itself
def on_post_write(file_path):
    content = read_file(file_path)
    modified = add_header(content)
    write_file(file_path, modified)  # Triggers PostToolUse again!

# GOOD - check if already processed
def on_post_write(file_path):
    content = read_file(file_path)
    if has_header(content):
        return  # Already processed
    modified = add_header(content)
    write_file(file_path, modified)
```

### 3. Hardcoded Paths

```python
# BAD - hardcoded path
config = json.load(open('/home/user/project/.claude/config.json'))

# GOOD - use environment variables
project_dir = os.environ.get('CLAUDE_PROJECT_DIR', os.getcwd())
config_path = os.path.join(project_dir, '.claude/config.json')
```

### 4. Silent Failures

```python
# BAD - fails silently
try:
    validate(data)
except:
    pass

# GOOD - log failures
try:
    validate(data)
except Exception as e:
    logging.error(f"Validation failed: {e}")
```

### 5. Complex Shell One-Liners

```json
// BAD - hard to debug
{
  "command": "cat | jq -r '.tool_input.file_path' | xargs -I {} sh -c 'test -f {} && prettier --write {} || true'"
}

// GOOD - use external script
{
  "command": "~/.claude/hooks/format.sh"
}
```

### 6. Modifying Input Without Allowing

```python
# BAD - modifies but doesn't set decision
output = {
    "hookSpecificOutput": {
        "updatedInput": {"content": new_content}
        # Missing permissionDecision!
    }
}

# GOOD - always include decision with modifications
output = {
    "hookSpecificOutput": {
        "hookEventName": "PreToolUse",
        "permissionDecision": "allow",
        "updatedInput": {"content": new_content}
    }
}
```

### 7. Trusting tool_input Blindly

```python
# BAD - uses path without validation
file_path = data['tool_input']['file_path']
os.remove(file_path)

# GOOD - validate before using
file_path = data.get('tool_input', {}).get('file_path', '')
if not file_path:
    sys.exit(0)
if '..' in file_path or not file_path.startswith(allowed_dir):
    print("Invalid path", file=sys.stderr)
    sys.exit(2)
```

### 8. Running Heavy Operations on Every Tool

```python
# BAD - runs full test suite after every write
def on_post_write():
    subprocess.run(['npm', 'test'])  # Takes 2 minutes!

# GOOD - run only related tests
def on_post_write(file_path):
    test_file = find_related_test(file_path)
    if test_file:
        subprocess.run(['npm', 'test', test_file])
```

---

## Testing Hooks

### Manual Testing

```bash
# Create mock input
cat > /tmp/mock.json << 'EOF'
{
  "session_id": "test",
  "hook_event_name": "PreToolUse",
  "tool_name": "Write",
  "tool_input": {
    "file_path": "/tmp/test.txt",
    "content": "test"
  }
}
EOF

# Test hook
cat /tmp/mock.json | ~/.claude/hooks/my-hook.py
echo "Exit code: $?"
```

### Edge Case Testing

```bash
# Empty input
echo '{}' | ~/.claude/hooks/my-hook.py

# Missing fields
echo '{"tool_name": "Write"}' | ~/.claude/hooks/my-hook.py

# Malicious input
echo '{"tool_input": {"file_path": "; rm -rf /"}}' | ~/.claude/hooks/my-hook.py
```

### Integration Testing

```bash
# Start Claude with debug
claude --debug

# Watch hook execution
# Trigger relevant tools
```

---

## Maintenance

### Version Control Hook Scripts

```bash
# Track changes
git add .claude/hooks/
git commit -m "feat: add code formatting hook"
```

### Monitor Hook Performance

```bash
# Time hook execution
time (echo '{}' | ~/.claude/hooks/my-hook.py)
```

### Regular Audits

- Review hook scripts monthly
- Update dependencies
- Check for security advisories
- Prune unused hooks
