# Hooks Syntax Guide

Complete reference for Claude Code hooks configuration syntax.

---

## Configuration File Locations

### Precedence (highest to lowest)

1. **Local overrides**: `.claude/settings.local.json` (not committed)
2. **Project hooks**: `.claude/settings.json` (committed, team-shared)
3. **Personal hooks**: `~/.claude/settings.json` (user-level)
4. **Plugin hooks**: `plugin/hooks/hooks.json` (bundled with plugins)

---

## settings.json Schema

### Top-Level Structure

```json
{
  "hooks": {
    "EVENT_NAME": [
      {
        "matcher": "PATTERN",
        "hooks": [
          {
            "type": "command",
            "command": "SHELL_COMMAND",
            "timeout": 60
          }
        ]
      }
    ]
  }
}
```

### Complete Schema

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "properties": {
    "hooks": {
      "type": "object",
      "properties": {
        "PreToolUse": { "$ref": "#/definitions/hookArray" },
        "PostToolUse": { "$ref": "#/definitions/hookArray" },
        "PermissionRequest": { "$ref": "#/definitions/hookArray" },
        "Notification": { "$ref": "#/definitions/hookArray" },
        "UserPromptSubmit": { "$ref": "#/definitions/hookArray" },
        "Stop": { "$ref": "#/definitions/hookArray" },
        "SubagentStop": { "$ref": "#/definitions/hookArray" },
        "PreCompact": { "$ref": "#/definitions/hookArray" },
        "SessionStart": { "$ref": "#/definitions/hookArray" },
        "SessionEnd": { "$ref": "#/definitions/hookArray" }
      }
    }
  },
  "definitions": {
    "hookArray": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "matcher": { "type": "string" },
          "hooks": {
            "type": "array",
            "items": {
              "oneOf": [
                {
                  "type": "object",
                  "properties": {
                    "type": { "const": "command" },
                    "command": { "type": "string" },
                    "timeout": { "type": "integer", "minimum": 1 }
                  },
                  "required": ["type", "command"]
                },
                {
                  "type": "object",
                  "properties": {
                    "type": { "const": "prompt" },
                    "prompt": { "type": "string" },
                    "timeout": { "type": "integer", "minimum": 1 }
                  },
                  "required": ["type", "prompt"]
                }
              ]
            }
          }
        },
        "required": ["hooks"]
      }
    }
  }
}
```

---

## Event Reference

### PreToolUse

**When**: Before a tool executes
**Can Block**: YES
**Supports Matchers**: YES (tool names)

**Input JSON:**
```json
{
  "session_id": "abc123",
  "transcript_path": "/path/to/transcript.jsonl",
  "cwd": "/current/working/directory",
  "permission_mode": "default",
  "hook_event_name": "PreToolUse",
  "tool_name": "Write",
  "tool_input": {
    "file_path": "/path/to/file.txt",
    "content": "file content"
  },
  "tool_use_id": "toolu_abc123"
}
```

**Output JSON (hookSpecificOutput):**
```json
{
  "hookSpecificOutput": {
    "hookEventName": "PreToolUse",
    "permissionDecision": "allow|deny|ask",
    "permissionDecisionReason": "explanation",
    "updatedInput": {
      "file_path": "/modified/path.txt",
      "content": "modified content"
    },
    "additionalContext": "info for Claude"
  }
}
```

---

### PostToolUse

**When**: After a tool completes successfully
**Can Block**: NO
**Supports Matchers**: YES (tool names)

**Input JSON:**
```json
{
  "session_id": "abc123",
  "transcript_path": "/path/to/transcript.jsonl",
  "cwd": "/current/working/directory",
  "permission_mode": "default",
  "hook_event_name": "PostToolUse",
  "tool_name": "Write",
  "tool_input": {
    "file_path": "/path/to/file.txt",
    "content": "file content"
  },
  "tool_response": "File written successfully",
  "tool_use_id": "toolu_abc123"
}
```

---

### PermissionRequest

**When**: User is shown a permission dialog
**Can Block**: YES (can override decision)
**Supports Matchers**: YES (tool names)

**Input JSON:**
```json
{
  "session_id": "abc123",
  "hook_event_name": "PermissionRequest",
  "message": "Allow Write to /path/to/file.txt?",
  "notification_type": "permission"
}
```

---

### Notification

**When**: Claude sends a notification
**Can Block**: NO
**Supports Matchers**: YES

**Input JSON:**
```json
{
  "session_id": "abc123",
  "hook_event_name": "Notification",
  "message": "Task completed",
  "notification_type": "info|warning|error|success"
}
```

---

### UserPromptSubmit

**When**: User submits a prompt
**Can Block**: YES
**Supports Matchers**: NO

**Input JSON:**
```json
{
  "session_id": "abc123",
  "hook_event_name": "UserPromptSubmit",
  "prompt": "Help me refactor this code...",
  "cwd": "/current/working/directory"
}
```

**Output JSON (hookSpecificOutput):**
```json
{
  "hookSpecificOutput": {
    "hookEventName": "UserPromptSubmit",
    "additionalContext": "Context injected into prompt"
  }
}
```

---

### Stop

**When**: Claude finishes responding
**Can Block**: Can force continuation
**Supports Matchers**: NO
**Supports Prompt Hooks**: YES

**Input JSON:**
```json
{
  "session_id": "abc123",
  "hook_event_name": "Stop",
  "stop_hook_active": false,
  "cwd": "/current/working/directory"
}
```

**Output JSON:**
```json
{
  "continue": true,
  "stopReason": "Task not complete - missing tests"
}
```

---

### SubagentStop

**When**: A subagent finishes
**Can Block**: Can force continuation
**Supports Matchers**: NO
**Supports Prompt Hooks**: YES

**Input JSON:**
```json
{
  "session_id": "abc123",
  "hook_event_name": "SubagentStop",
  "stop_hook_active": false
}
```

---

### PreCompact

**When**: Before context compaction
**Can Block**: NO
**Supports Matchers**: YES (`manual`, `auto`)

**Input JSON:**
```json
{
  "session_id": "abc123",
  "hook_event_name": "PreCompact",
  "trigger": "auto|manual",
  "custom_instructions": "preserve recent context"
}
```

---

### SessionStart

**When**: Session begins
**Can Block**: NO
**Supports Matchers**: YES (`startup`, `resume`, `clear`, `compact`)

**Input JSON:**
```json
{
  "session_id": "abc123",
  "hook_event_name": "SessionStart",
  "source": "startup|resume|clear|compact",
  "cwd": "/current/working/directory"
}
```

**Special**: Can write to `$CLAUDE_ENV_FILE` to set environment variables.

---

### SessionEnd

**When**: Session ends
**Can Block**: NO
**Supports Matchers**: NO

**Input JSON:**
```json
{
  "session_id": "abc123",
  "hook_event_name": "SessionEnd",
  "reason": "clear|logout|prompt_input_exit|other",
  "cwd": "/current/working/directory"
}
```

---

## Matcher Patterns

### Tool Name Patterns

| Pattern | Description | Example Matches |
|---------|-------------|-----------------|
| `"Write"` | Exact match | Write |
| `"Write\|Edit"` | OR pattern | Write, Edit |
| `"Notebook.*"` | Prefix match | NotebookEdit, NotebookRead |
| `".*Read.*"` | Contains | Read, FileRead, ReadLine |
| `".*"` | All tools | Everything |
| `"*"` | All tools (shorthand) | Everything |
| `""` | All tools (empty) | Everything |

### MCP Tool Patterns

MCP tools follow: `mcp__<server>__<tool>`

| Pattern | Description |
|---------|-------------|
| `"mcp__memory__.*"` | All memory server tools |
| `"mcp__github__create_issue"` | Specific GitHub tool |
| `"mcp__.*__read.*"` | All read operations |

### Bash Command Patterns

| Pattern | Description |
|---------|-------------|
| `"Bash"` | All Bash commands |
| `"Bash(git:*)"` | Only git commands |
| `"Bash(npm:*)"` | Only npm commands |
| `"Bash(docker:*)"` | Only docker commands |

### SessionStart Patterns

| Pattern | Triggers On |
|---------|-------------|
| `"startup"` | Fresh session start |
| `"resume"` | Resuming session |
| `"clear"` | After /clear |
| `"compact"` | After compaction |
| `"startup\|resume"` | Either |

### PreCompact Patterns

| Pattern | Triggers On |
|---------|-------------|
| `"manual"` | User-initiated |
| `"auto"` | Automatic |

---

## Exit Code Semantics

| Exit Code | Meaning | Behavior |
|-----------|---------|----------|
| `0` | Success | stdout parsed as JSON |
| `2` | Blocking error | stderr shown to Claude, operation blocked |
| `1` | Non-blocking error | stderr logged in debug mode |
| Other | Non-blocking error | stderr logged in debug mode |

---

## Environment Variables

### Available in All Hooks

| Variable | Description |
|----------|-------------|
| `$CLAUDE_PROJECT_DIR` | Project root directory |
| `$CLAUDE_CODE_REMOTE` | "true" if remote, otherwise empty |

### SessionStart Only

| Variable | Description |
|----------|-------------|
| `$CLAUDE_ENV_FILE` | Path to write persistent env vars |

### Plugin Hooks Only

| Variable | Description |
|----------|-------------|
| `$CLAUDE_PLUGIN_ROOT` | Plugin installation directory |

---

## Hook Types

### Command Hook

```json
{
  "type": "command",
  "command": "python3 ~/.claude/hooks/my-hook.py",
  "timeout": 60
}
```

| Field | Required | Default | Description |
|-------|----------|---------|-------------|
| `type` | Yes | - | Must be `"command"` |
| `command` | Yes | - | Shell command to execute |
| `timeout` | No | 60 | Seconds before kill |

### Prompt Hook

```json
{
  "type": "prompt",
  "prompt": "Evaluate this: $ARGUMENTS",
  "timeout": 30
}
```

| Field | Required | Default | Description |
|-------|----------|---------|-------------|
| `type` | Yes | - | Must be `"prompt"` |
| `prompt` | Yes | - | Instructions for LLM |
| `timeout` | No | 30 | Seconds to wait |

**Supported Events**: Stop, SubagentStop, UserPromptSubmit, PreToolUse, PermissionRequest

---

## Tool Input Fields

### Write Tool

```json
{
  "file_path": "/absolute/path/to/file.txt",
  "content": "file content"
}
```

### Edit Tool

```json
{
  "file_path": "/absolute/path/to/file.txt",
  "old_string": "text to replace",
  "new_string": "replacement text"
}
```

### Read Tool

```json
{
  "file_path": "/absolute/path/to/file.txt",
  "offset": 0,
  "limit": 2000
}
```

### Bash Tool

```json
{
  "command": "git status",
  "timeout": 120000
}
```

### Grep Tool

```json
{
  "pattern": "TODO",
  "path": "/search/path",
  "glob": "*.js"
}
```

### Glob Tool

```json
{
  "pattern": "**/*.ts",
  "path": "/search/path"
}
```

---

## Script Best Practices

### Shebang Lines

```bash
#!/bin/bash           # Bash script
#!/usr/bin/env bash   # Portable bash
#!/usr/bin/env python3  # Python script
#!/usr/bin/env node   # Node.js script
```

### Bash Script Template

```bash
#!/bin/bash
set -euo pipefail

input=$(cat)
tool_name=$(echo "$input" | jq -r '.tool_name // empty')
file_path=$(echo "$input" | jq -r '.tool_input.file_path // empty')

# Your logic here

exit 0
```

### Python Script Template

```python
#!/usr/bin/env python3
import sys
import json

data = json.load(sys.stdin)
tool_name = data.get('tool_name', '')
tool_input = data.get('tool_input', {})

# Your logic here

sys.exit(0)
```

### Making Scripts Executable

```bash
chmod +x ~/.claude/hooks/my-hook.sh
chmod +x ~/.claude/hooks/my-hook.py
```

---

## JSON Output Examples

### Allow Operation

```json
{
  "hookSpecificOutput": {
    "hookEventName": "PreToolUse",
    "permissionDecision": "allow"
  }
}
```

### Deny Operation

```json
{
  "hookSpecificOutput": {
    "hookEventName": "PreToolUse",
    "permissionDecision": "deny",
    "permissionDecisionReason": "File is protected"
  }
}
```

### Ask User

```json
{
  "hookSpecificOutput": {
    "hookEventName": "PreToolUse",
    "permissionDecision": "ask",
    "permissionDecisionReason": "This will modify a config file"
  }
}
```

### Modify Input

```json
{
  "hookSpecificOutput": {
    "hookEventName": "PreToolUse",
    "permissionDecision": "allow",
    "updatedInput": {
      "content": "Modified content with license header"
    }
  }
}
```

### Force Continuation

```json
{
  "continue": true,
  "stopReason": "Task incomplete - tests not run"
}
```

### Add Context to Prompt

```json
{
  "hookSpecificOutput": {
    "hookEventName": "UserPromptSubmit",
    "additionalContext": "Project uses TypeScript with strict mode"
  }
}
```

---

## Validation

### JSON Validation

```bash
# Check settings.json is valid JSON
jq . .claude/settings.json

# Check for syntax errors
python3 -m json.tool .claude/settings.json
```

### Script Validation

```bash
# Bash syntax check
bash -n ~/.claude/hooks/my-hook.sh

# Python syntax check
python3 -m py_compile ~/.claude/hooks/my-hook.py
```

### Hook Registration Check

```bash
# In Claude Code
/hooks
```
