---
name: hooks-builder
description: "Create event-driven hooks for Claude Code automation. Use when the user wants to create hooks, automate tool validation, add pre/post processing, enforce security policies, or configure settings.json hooks. Triggers: create hook, build hook, PreToolUse, PostToolUse, event automation, tool validation, security hook"
---

# Hooks Builder

A comprehensive guide for creating Claude Code hooks — event-driven automation that monitors and controls Claude's actions.

## Quick Reference

### The 10 Hook Events

| Event | When It Fires | Can Block? | Supports Matchers? |
|-------|--------------|------------|-------------------|
| **PreToolUse** | Before tool executes | YES | YES (tool names) |
| **PermissionRequest** | Permission dialog shown | YES | YES (tool names) |
| **PostToolUse** | After tool succeeds | No | YES (tool names) |
| **Notification** | Claude sends notification | No | YES |
| **UserPromptSubmit** | User submits prompt | YES | No |
| **Stop** | Claude finishes responding | Can force continue | No |
| **SubagentStop** | Subagent finishes | Can force continue | No |
| **PreCompact** | Before context compaction | No | YES (manual/auto) |
| **SessionStart** | Session begins | No | YES (startup/resume/clear/compact) |
| **SessionEnd** | Session ends | No | No |

These ten cover most needs. Claude Code has about 25 more events, including `SubagentStart`, `PostToolUseFailure`, `PostToolBatch`, `StopFailure`, `PermissionDenied`, `PostCompact`, `FileChanged`, `CwdChanged`, `ConfigChange`, `InstructionsLoaded`, `TaskCreated`, `TaskCompleted`, and `WorktreeCreate`. Handlers can also be `http`, `mcp_tool`, or `agent` as well as `command` and `prompt`. Read the "Additional Events" section of [reference/syntax-guide.md](reference/syntax-guide.md) when the user's trigger does not fit the table above, and check https://code.claude.com/docs/en/hooks for the input schema of any event before writing a handler for it.

### Exit Code Semantics

| Exit Code | Meaning | Effect |
|-----------|---------|--------|
| **0** | Success | stdout parsed as JSON for control |
| **2** | Blocking error | **VETO** — stderr shown to Claude |
| **Other** | Non-blocking error | stderr logged in debug mode |

### Configuration Locations

```
~/.claude/settings.json          → Personal hooks (all projects)
.claude/settings.json            → Project hooks (team, committed)
.claude/settings.local.json      → Local overrides (not committed)
```

### Essential Environment Variables

| Variable | Description |
|----------|-------------|
| `$CLAUDE_PROJECT_DIR` | Project root directory |
| `$CLAUDE_CODE_REMOTE` | Remote/local indicator |
| `$CLAUDE_ENV_FILE` | Environment persistence path (SessionStart) |
| `$CLAUDE_PLUGIN_ROOT` | Plugin directory (plugin hooks) |

### Key Commands

```bash
/hooks              # View active hooks
claude --debug      # Enable debug logging
chmod +x script.sh  # Make script executable
```

---

## 6-Phase Workflow

### Phase 1: Requirements Gathering

**Use AskUserQuestion to clarify:**

1. **What event should trigger this hook?**
   - Tool execution (Pre/Post/Permission) → PreToolUse, PostToolUse, PermissionRequest
   - User input → UserPromptSubmit
   - Response completion → Stop, SubagentStop
   - Session lifecycle → SessionStart, SessionEnd
   - Context management → PreCompact
   - Notifications → Notification

2. **What should happen when triggered?**
   - Observe only (logging, metrics)
   - Block/allow based on conditions
   - Modify inputs before execution
   - Add context to prompts
   - Force continuation

3. **Should it block, modify, or just observe?**
   - Observer: PostToolUse, Notification, SessionEnd (can't block)
   - Gatekeeper: PreToolUse, PermissionRequest, UserPromptSubmit (can block)
   - Transformer: PreToolUse with updatedInput (can modify)
   - Controller: Stop, SubagentStop (can force continue)

4. **What are the security implications?**
   - Will it handle untrusted input?
   - Could it expose sensitive data?
   - Does it need to access external systems?

### Phase 2: Event Selection

**Match event to use case:**

| Use Case | Best Event |
|----------|-----------|
| Block dangerous operations | PreToolUse |
| Auto-format code after writes | PostToolUse |
| Validate user prompts | UserPromptSubmit |
| Setup environment | SessionStart |
| Ensure task completion | Stop |
| Log all tool usage | PostToolUse with `"*"` matcher |
| Protect sensitive files | PreToolUse for Write/Edit |
| Add project context | UserPromptSubmit |

**Determine if matchers are needed:**
- Specific tools? → Use matcher: `"Write|Edit"`
- All tools? → Use `"*"` or omit matcher
- MCP tools? → Use `mcp__server__tool` pattern
- Bash commands? → Use `Bash(git:*)` pattern

### Phase 3: Matcher Design

**Matcher Pattern Syntax:**

```json
// Exact match (case-sensitive!)
"matcher": "Write"

// OR pattern
"matcher": "Write|Edit"

// Prefix match
"matcher": "Notebook.*"

// Contains match
"matcher": ".*Read.*"

// All tools
"matcher": "*"

// MCP tools
"matcher": "mcp__memory__.*"

// Bash sub-patterns
"matcher": "Bash(git:*)"
```

**Common Matcher Patterns:**

| Pattern | Matches |
|---------|---------|
| `"Write"` | Only Write tool |
| `"Write\|Edit"` | Write OR Edit |
| `"Bash"` | All Bash commands |
| `"Bash(git:*)"` | Only git commands |
| `"Bash(npm:*)"` | Only npm commands |
| `"mcp__.*__.*"` | All MCP tools |
| `".*"` or `"*"` | Everything |

### Phase 4: Implementation

**Choose implementation approach:**

1. **Inline command** (simple, no external file):
   ```json
   {
     "type": "command",
     "command": "echo \"$(date) | $tool_name\" >> ~/.claude/audit.log"
   }
   ```

2. **External script** (complex logic, reusable):
   ```json
   {
     "type": "command",
     "command": "\"$CLAUDE_PROJECT_DIR\"/.claude/hooks/validate.sh"
   }
   ```

3. **Prompt-based** (LLM evaluation, intelligent decisions):
   ```json
   {
     "type": "prompt",
     "prompt": "Analyze if all tasks are complete: $ARGUMENTS",
     "timeout": 30
   }
   ```

**Script Template (Bash):**
```bash
#!/bin/bash
set -euo pipefail

# Read JSON input from stdin
input=$(cat)

# Parse fields with jq
tool_name=$(echo "$input" | jq -r '.tool_name // empty')
file_path=$(echo "$input" | jq -r '.tool_input.file_path // empty')

# Your logic here
if [[ "$file_path" == *".env"* ]]; then
    echo "BLOCKED: Cannot modify .env files" >&2
    exit 2
fi

# Success - output decision
echo '{"decision": "approve"}'
exit 0
```

**Script Template (Python):**
```python
#!/usr/bin/env python3
import sys
import json

# Read JSON input from stdin
data = json.load(sys.stdin)

# Extract fields
tool_name = data.get('tool_name', '')
tool_input = data.get('tool_input', {})
file_path = tool_input.get('file_path', '')

# Your logic here
if '.env' in file_path:
    print("BLOCKED: Cannot modify .env files", file=sys.stderr)
    sys.exit(2)

# Success - output decision
output = {"decision": "approve"}
print(json.dumps(output))
sys.exit(0)
```

### Phase 5: Security Hardening

**CRITICAL: Hooks execute shell commands with YOUR permissions.**

**Security Checklist:**
- [ ] All variables quoted: `"$VAR"` not `$VAR`
- [ ] JSON parsed with jq or json.load (not grep/sed)
- [ ] Paths validated (no `..`, normalized)
- [ ] No sensitive data in logs/output
- [ ] No sudo or privilege escalation
- [ ] Script tested manually first
- [ ] Project hooks audited before running
- [ ] Timeout set appropriately
- [ ] Error handling for all failure modes

**Secure Patterns:**
```bash
# UNSAFE - injection risk
rm $file_path

# SAFE - quoted, prevents flag injection
rm -- "$file_path"

# UNSAFE - parsing risk
cat "$input" | grep "field"

# SAFE - proper JSON parsing
echo "$input" | jq -r '.field'
```

**Defense in Depth:**
1. Input validation (parse JSON properly)
2. Path sanitization (normalize, check boundaries)
3. Output sanitization (no sensitive data)
4. Fail-safe defaults (block on error, not allow)
5. Timeout protection (prevent infinite loops)

### Phase 6: Testing

**Step 1: Manual Script Testing**
```bash
# Create mock input
cat > /tmp/mock-input.json << 'EOF'
{
  "session_id": "test-123",
  "hook_event_name": "PreToolUse",
  "tool_name": "Write",
  "tool_input": {
    "file_path": "/path/to/file.txt",
    "content": "test content"
  }
}
EOF

# Test script
cat /tmp/mock-input.json | ./my-hook.sh
echo "Exit code: $?"
```

**Step 2: Edge Case Testing**
- Empty inputs: `{}`
- Missing fields: `{"tool_name": "Write"}`
- Malicious inputs: `{"tool_input": {"file_path": "; rm -rf /"}}`
- Large inputs: 10KB+ content
- Unicode: paths with special characters

**Step 3: Integration Testing**
```bash
# Start Claude with debug mode
claude --debug

# Trigger the tool your hook targets
# Watch debug output for hook execution
```

**Step 4: Verification**
```bash
# Check hooks are registered
/hooks

# Watch hook execution
claude --debug 2>&1 | grep -i hook
```

---

## Hook Patterns

### Observer Pattern
Log without blocking — use PostToolUse or Notification.

```json
{
  "hooks": {
    "PostToolUse": [{
      "matcher": "*",
      "hooks": [{
        "type": "command",
        "command": "echo \"$(date) | $tool_name\" >> ~/.claude/audit.log"
      }]
    }]
  }
}
```

### Gatekeeper Pattern
Block dangerous actions — use PreToolUse or PermissionRequest.

```json
{
  "hooks": {
    "PreToolUse": [{
      "matcher": "Write|Edit",
      "hooks": [{
        "type": "command",
        "command": "python3 ~/.claude/hooks/file-protector.py"
      }]
    }]
  }
}
```

### Transformer Pattern
Modify inputs before execution — use PreToolUse with updatedInput.

```python
# In script, output:
output = {
    "hookSpecificOutput": {
        "hookEventName": "PreToolUse",
        "permissionDecision": "allow",
        "updatedInput": {
            "content": add_license_header(original_content)
        }
    }
}
print(json.dumps(output))
```

### Orchestrator Pattern
Coordinate multiple events — combine SessionStart + PreToolUse + PostToolUse.

```json
{
  "hooks": {
    "SessionStart": [{
      "matcher": "startup",
      "hooks": [{"type": "command", "command": "~/.claude/hooks/setup-env.sh"}]
    }],
    "PreToolUse": [{
      "matcher": "Write|Edit",
      "hooks": [{"type": "command", "command": "~/.claude/hooks/validate.sh"}]
    }],
    "PostToolUse": [{
      "matcher": "Write|Edit",
      "hooks": [{"type": "command", "command": "~/.claude/hooks/format.sh"}]
    }]
  }
}
```

---

## Common Pitfalls

Read [reference/common-pitfalls.md](reference/common-pitfalls.md) before finalizing any hook, and first when a hook does not fire, blocks unexpectedly, or hangs.

## When to Use Hooks

**USE hooks for:**
- Security enforcement (block dangerous operations)
- Code quality automation (format, lint on save)
- Compliance and auditing (log all actions)
- Environment setup (consistent configuration)
- Workflow automation (notifications, integrations)
- Input validation (prompt checking)
- Task completion verification

**DON'T use hooks for:**
- Adding new capabilities (use Skills)
- Delegating complex work (use Agents)
- User-invoked prompts (use Commands)
- Simple one-off tasks (just ask Claude)

---

## Files in This Skill

### Templates (Progressive Complexity)
- `templates/basic-hook.md` — Single event, inline command
- `templates/with-scripts.md` — External shell scripts
- `templates/with-decisions.md` — Permission control, input modification
- `templates/with-prompts.md` — LLM-based evaluation
- `templates/production-hooks.md` — Complete multi-event system

### Examples (18 Complete Hooks)
- `examples/security-hooks.md` — Protection, validation, auditing
- `examples/quality-hooks.md` — Formatting, linting, testing
- `examples/workflow-hooks.md` — Setup, context, notifications

### Reference
- `reference/syntax-guide.md` — Complete JSON schemas, all events
- `reference/best-practices.md` — Security, design, team deployment
- `reference/troubleshooting.md` — 10 common issues, testing methodology
