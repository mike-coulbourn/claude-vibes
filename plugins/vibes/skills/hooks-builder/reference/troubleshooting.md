# Hooks Troubleshooting Guide

Diagnose and fix common hook issues with systematic debugging.

---

## Quick Diagnosis Commands

```bash
# Check if hooks are registered
/hooks

# Enable debug mode
claude --debug

# Validate settings.json
jq . .claude/settings.json

# Check script permissions
ls -la ~/.claude/hooks/

# Test script manually
cat /tmp/mock.json | ~/.claude/hooks/my-hook.sh; echo "Exit: $?"
```

---

## Common Issues

### Issue 1: Hook Not Triggering

**Symptoms:**
- Hook doesn't run when expected
- No debug output for hook
- `/hooks` doesn't list the hook

**Causes & Solutions:**

| Cause | Solution |
|-------|----------|
| Settings file not loaded | Restart Claude Code |
| Invalid JSON | Run `jq . .claude/settings.json` |
| Wrong event name | Check spelling: `PreToolUse` not `preToolUse` |
| Matcher not matching | Check case sensitivity: `"Write"` not `"write"` |
| Wrong settings file | Check location: project vs personal |

**Debugging:**
```bash
# Check settings are valid
jq '.hooks' .claude/settings.json

# Verify hook structure
jq '.hooks.PreToolUse' .claude/settings.json

# Check matcher pattern
echo "Write" | grep -E "Write|Edit"  # Should match
```

---

### Issue 2: Exit Code Errors

**Symptoms:**
- Hook runs but doesn't block/allow as expected
- Unexpected behavior after hook execution
- stderr messages appearing unexpectedly

**Causes & Solutions:**

| Exit Code | Expected Behavior | Common Mistake |
|-----------|------------------|----------------|
| 0 | Success, parse stdout | Hook returns 1 instead |
| 2 | Block operation | Using exit 1 (non-blocking) |
| 1 | Non-blocking error | Meant to block, used wrong code |

**Fix:**
```bash
# WRONG - won't block
if [[ dangerous ]]; then
    echo "Error" >&2
    exit 1  # Non-blocking!
fi

# RIGHT - will block
if [[ dangerous ]]; then
    echo "BLOCKED: reason" >&2
    exit 2  # Blocking error
fi
```

---

### Issue 3: JSON Parse Failures

**Symptoms:**
- Hook crashes with JSON error
- "JSONDecodeError" in debug output
- Hook works sometimes but not always

**Causes & Solutions:**

| Cause | Solution |
|-------|----------|
| Invalid JSON from stdin | Check `cat` or read command |
| Empty stdin | Handle empty input gracefully |
| Non-JSON output | Ensure stdout is valid JSON or empty |

**Fix:**
```python
# Robust JSON reading
import sys
import json

try:
    data = json.load(sys.stdin)
except json.JSONDecodeError:
    sys.exit(0)  # Allow if can't parse
except Exception:
    sys.exit(0)
```

```bash
# Robust bash parsing
input=$(cat) || exit 0
if [[ -z "$input" ]]; then
    exit 0
fi
tool_name=$(echo "$input" | jq -r '.tool_name // empty') || exit 0
```

---

### Issue 4: Permission Denied

**Symptoms:**
- "Permission denied" error
- Hook listed but doesn't execute
- Works when run manually, fails in Claude

**Causes & Solutions:**

| Cause | Solution |
|-------|----------|
| Script not executable | `chmod +x script.sh` |
| Wrong shebang | Add `#!/bin/bash` or `#!/usr/bin/env python3` |
| Path issues | Use absolute paths |

**Fix:**
```bash
# Make executable
chmod +x ~/.claude/hooks/my-hook.sh
chmod +x ~/.claude/hooks/my-hook.py

# Verify
ls -la ~/.claude/hooks/
# Should show: -rwxr-xr-x

# Check shebang
head -1 ~/.claude/hooks/my-hook.sh
# Should be: #!/bin/bash
```

---

### Issue 5: Timeout Exceeded

**Symptoms:**
- Hook starts but gets killed
- "Timeout" in debug output
- Works locally but fails in Claude

**Causes & Solutions:**

| Cause | Solution |
|-------|----------|
| Slow network call | Increase timeout or make async |
| Heavy computation | Optimize or increase timeout |
| Infinite loop | Fix loop condition |
| Blocking on input | Check stdin reading |

**Fix:**
```json
// Increase timeout for slow operations
{
  "type": "command",
  "command": "~/.claude/hooks/slow-check.sh",
  "timeout": 120  // 2 minutes instead of default 60
}
```

```python
# Add timeout to subprocess calls
import subprocess
try:
    result = subprocess.run(
        ['slow-command'],
        timeout=30,  # Internal timeout
        capture_output=True
    )
except subprocess.TimeoutExpired:
    sys.exit(0)  # Allow if timeout
```

---

### Issue 6: Matcher Not Matching

**Symptoms:**
- Hook registered but doesn't trigger for expected tool
- Works for some tools but not others

**Causes & Solutions:**

| Cause | Solution |
|-------|----------|
| Case sensitivity | `"Write"` not `"write"` |
| Regex escape | `"Write\|Edit"` for OR |
| MCP tool naming | `"mcp__server__tool"` pattern |
| Bash subpattern | `"Bash(git:*)"` format |

**Debugging:**
```bash
# Check exact tool names
/tools  # List available tools

# Test regex pattern
echo "Write" | grep -E "Write|Edit"  # Should match
echo "Bash" | grep -E "Bash"  # Should match
echo "mcp__memory__store" | grep -E "mcp__memory__.*"  # Should match
```

**Common patterns:**
```json
"matcher": "Write"           // Exact match
"matcher": "Write|Edit"      // OR (escape pipe in JSON)
"matcher": "Write\\|Edit"    // OR (double escape sometimes needed)
"matcher": "Bash"            // All Bash commands
"matcher": "Bash(git:*)"     // Only git commands
"matcher": "*"               // All tools
```

---

### Issue 7: Script Not Found

**Symptoms:**
- "No such file or directory"
- "command not found"
- Hook registered but fails immediately

**Causes & Solutions:**

| Cause | Solution |
|-------|----------|
| Wrong path | Use absolute path |
| Spaces in path | Quote path with `\"` |
| Missing interpreter | Check `python3`, `bash` available |

**Fix:**
```json
// WRONG - relative path
{
  "command": ".claude/hooks/my-hook.sh"
}

// WRONG - unquoted path with potential spaces
{
  "command": "$CLAUDE_PROJECT_DIR/.claude/hooks/my-hook.sh"
}

// RIGHT - quoted absolute path
{
  "command": "\"$CLAUDE_PROJECT_DIR\"/.claude/hooks/my-hook.sh"
}

// RIGHT - home directory
{
  "command": "python3 ~/.claude/hooks/my-hook.py"
}
```

---

### Issue 8: Environment Variables Missing

**Symptoms:**
- `$CLAUDE_PROJECT_DIR` is empty
- Script can't find project files
- Different behavior in Claude vs terminal

**Causes & Solutions:**

| Cause | Solution |
|-------|----------|
| Wrong variable name | Use exact name: `CLAUDE_PROJECT_DIR` |
| Not available for event | Check event supports variable |
| Shell escaping | Use `"$VAR"` not `$VAR` |

**Available variables by event:**
```
All events:
- CLAUDE_PROJECT_DIR
- CLAUDE_CODE_REMOTE

SessionStart only:
- CLAUDE_ENV_FILE

Plugin hooks only:
- CLAUDE_PLUGIN_ROOT
```

**Debugging:**
```bash
# Check variable is set
echo "Project: $CLAUDE_PROJECT_DIR" >> /tmp/debug.log
```

---

### Issue 9: Output Not Parsed

**Symptoms:**
- Hook returns JSON but decision ignored
- `permissionDecision` not taking effect
- `updatedInput` not applied

**Causes & Solutions:**

| Cause | Solution |
|-------|----------|
| Non-zero exit code | Ensure `exit 0` |
| Invalid JSON | Validate with `jq` |
| Wrong structure | Check `hookSpecificOutput` nesting |
| Missing `hookEventName` | Include in output |

**Correct output structure:**
```json
{
  "hookSpecificOutput": {
    "hookEventName": "PreToolUse",
    "permissionDecision": "allow",
    "permissionDecisionReason": "reason",
    "updatedInput": {
      "field": "value"
    }
  }
}
```

**Debugging:**
```bash
# Test output is valid JSON
echo '{"hookSpecificOutput": {"permissionDecision": "allow"}}' | jq .

# Run hook and validate output
cat /tmp/mock.json | ~/.claude/hooks/my-hook.py | jq .
```

---

### Issue 10: Security Blocking

**Symptoms:**
- Hook blocked by security policy
- Works locally but fails in Claude
- "Operation not permitted"

**Causes & Solutions:**

| Cause | Solution |
|-------|----------|
| Sandbox restrictions | Check allowed operations |
| Network access blocked | Use local operations |
| File access restricted | Check permissions |

**Debugging:**
```bash
# Check what's allowed
claude --debug  # Look for security messages

# Test simpler operation first
echo '{}' | bash -c 'echo "test"'
```

---

## 5-Step Debug Workflow

### Step 1: Verify Registration

```bash
# In Claude Code
/hooks
```

Look for your hook in the output. If not listed:
- Check settings.json location
- Validate JSON syntax
- Restart Claude Code

### Step 2: Validate JSON

```bash
# Check settings.json is valid
jq . .claude/settings.json

# Check specific hook
jq '.hooks.PreToolUse' .claude/settings.json
```

### Step 3: Test Script Manually

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
  },
  "cwd": "/tmp"
}
EOF

# Run script
cat /tmp/mock.json | ~/.claude/hooks/my-hook.py
echo "Exit code: $?"

# Check output is valid JSON
cat /tmp/mock.json | ~/.claude/hooks/my-hook.py | jq .
```

### Step 4: Check Permissions

```bash
# Script must be executable
ls -la ~/.claude/hooks/my-hook.py
# Should show: -rwxr-xr-x

# Fix if needed
chmod +x ~/.claude/hooks/my-hook.py
```

### Step 5: Enable Debug Mode

```bash
# Start Claude with debug
claude --debug

# Trigger the tool your hook targets
# Watch for hook-related messages:
# [DEBUG] Executing hooks for PreToolUse:Write
# [DEBUG] Hook command completed with status 0
```

---

## Diagnostic Script

Save this script to test hooks systematically:

```bash
#!/bin/bash
# ~/.claude/hooks/diagnose.sh
# Run: bash ~/.claude/hooks/diagnose.sh

echo "=== Hook Diagnostics ==="
echo ""

# Check settings files
echo "1. Settings files:"
for f in ~/.claude/settings.json .claude/settings.json .claude/settings.local.json; do
    if [[ -f "$f" ]]; then
        echo "   ✓ Found: $f"
        if jq . "$f" > /dev/null 2>&1; then
            echo "     Valid JSON"
            hooks=$(jq '.hooks | keys | length' "$f" 2>/dev/null || echo "0")
            echo "     Hooks defined: $hooks events"
        else
            echo "     ✗ INVALID JSON!"
        fi
    else
        echo "   - Not found: $f"
    fi
done
echo ""

# Check hook scripts
echo "2. Hook scripts:"
for dir in ~/.claude/hooks .claude/hooks; do
    if [[ -d "$dir" ]]; then
        echo "   Directory: $dir"
        for script in "$dir"/*.{sh,py,js} 2>/dev/null; do
            if [[ -f "$script" ]]; then
                name=$(basename "$script")
                if [[ -x "$script" ]]; then
                    echo "     ✓ $name (executable)"
                else
                    echo "     ✗ $name (NOT executable)"
                fi
            fi
        done
    fi
done
echo ""

# Check required tools
echo "3. Required tools:"
for tool in jq python3 bash; do
    if command -v "$tool" &> /dev/null; then
        echo "   ✓ $tool: $(which $tool)"
    else
        echo "   ✗ $tool: NOT FOUND"
    fi
done
echo ""

# Test a hook
echo "4. Hook test:"
if [[ -f ~/.claude/hooks/test-hook.py ]]; then
    echo '{"tool_name": "Write", "tool_input": {"file_path": "/tmp/test"}}' | \
        python3 ~/.claude/hooks/test-hook.py
    echo "   Exit code: $?"
else
    echo "   Create ~/.claude/hooks/test-hook.py to test"
fi
echo ""

echo "=== Done ==="
```

---

## Mock Input Templates

### PreToolUse - Write

```json
{
  "session_id": "test-123",
  "hook_event_name": "PreToolUse",
  "cwd": "/home/user/project",
  "permission_mode": "default",
  "tool_name": "Write",
  "tool_input": {
    "file_path": "/home/user/project/src/index.ts",
    "content": "console.log('hello');"
  },
  "tool_use_id": "toolu_test"
}
```

### PreToolUse - Bash

```json
{
  "session_id": "test-123",
  "hook_event_name": "PreToolUse",
  "cwd": "/home/user/project",
  "tool_name": "Bash",
  "tool_input": {
    "command": "npm test"
  }
}
```

### PostToolUse

```json
{
  "session_id": "test-123",
  "hook_event_name": "PostToolUse",
  "tool_name": "Write",
  "tool_input": {
    "file_path": "/home/user/project/src/index.ts",
    "content": "console.log('hello');"
  },
  "tool_response": "File written successfully"
}
```

### UserPromptSubmit

```json
{
  "session_id": "test-123",
  "hook_event_name": "UserPromptSubmit",
  "prompt": "Help me refactor this code",
  "cwd": "/home/user/project"
}
```

### SessionStart

```json
{
  "session_id": "test-123",
  "hook_event_name": "SessionStart",
  "source": "startup",
  "cwd": "/home/user/project"
}
```

### Stop

```json
{
  "session_id": "test-123",
  "hook_event_name": "Stop",
  "stop_hook_active": false,
  "cwd": "/home/user/project"
}
```

---

## Getting Help

1. **Check debug output**: `claude --debug`
2. **Validate JSON**: `jq . settings.json`
3. **Test manually**: `cat mock.json | ./hook.sh`
4. **Check permissions**: `ls -la hooks/`
5. **Review docs**: `/hooks` command in Claude Code
