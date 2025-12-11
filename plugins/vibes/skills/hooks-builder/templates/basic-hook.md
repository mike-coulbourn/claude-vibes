# Basic Hook Template

The simplest hook pattern: single event, inline command, no external scripts.

## When to Use

- Quick logging or auditing
- Simple notifications
- One-line validations
- Getting started with hooks

## Template Structure

```json
{
  "hooks": {
    "EVENT_NAME": [
      {
        "matcher": "TOOL_PATTERN",
        "hooks": [
          {
            "type": "command",
            "command": "YOUR_INLINE_COMMAND",
            "timeout": 60
          }
        ]
      }
    ]
  }
}
```

## Field Reference

| Field | Required | Description |
|-------|----------|-------------|
| `EVENT_NAME` | Yes | One of 10 hook events |
| `matcher` | No* | Regex pattern for tool filtering |
| `type` | Yes | Always `"command"` for basic hooks |
| `command` | Yes | Shell command to execute |
| `timeout` | No | Seconds before kill (default: 60) |

*Matcher is only used for tool-related events (PreToolUse, PostToolUse, PermissionRequest)

---

## Example 1: Audit Logger

Log all tool usage to a file.

**Configuration** (add to `~/.claude/settings.json`):
```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "*",
        "hooks": [
          {
            "type": "command",
            "command": "echo \"$(date '+%Y-%m-%d %H:%M:%S') | Tool: $tool_name\" >> ~/.claude/audit.log"
          }
        ]
      }
    ]
  }
}
```

**What it does:**
- Triggers after ANY tool completes successfully
- Appends timestamp and tool name to audit log
- Non-blocking (PostToolUse can't block)

**Output** (`~/.claude/audit.log`):
```
2025-01-15 10:23:45 | Tool: Read
2025-01-15 10:23:47 | Tool: Edit
2025-01-15 10:23:52 | Tool: Bash
```

---

## Example 2: Write Notification

Show desktop notification when files are written.

**Configuration:**
```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Write",
        "hooks": [
          {
            "type": "command",
            "command": "osascript -e 'display notification \"File written by Claude\" with title \"Claude Code\"' 2>/dev/null || true"
          }
        ]
      }
    ]
  }
}
```

**What it does:**
- Triggers only when Write tool completes
- Shows macOS notification (fails silently on other OS)
- Non-blocking

**Note:** For Linux, use `notify-send` instead:
```json
"command": "notify-send 'Claude Code' 'File written' 2>/dev/null || true"
```

---

## Example 3: Session Start Message

Print welcome message when session starts.

**Configuration:**
```json
{
  "hooks": {
    "SessionStart": [
      {
        "matcher": "startup",
        "hooks": [
          {
            "type": "command",
            "command": "echo 'Session started at $(date)' >> ~/.claude/sessions.log"
          }
        ]
      }
    ]
  }
}
```

**What it does:**
- Triggers only on fresh session start (not resume)
- Logs session start time
- Matcher options: `startup`, `resume`, `clear`, `compact`

---

## Example 4: Git Branch Logger

Log which git branch Claude is working on.

**Configuration:**
```json
{
  "hooks": {
    "SessionStart": [
      {
        "matcher": "startup|resume",
        "hooks": [
          {
            "type": "command",
            "command": "branch=$(git branch --show-current 2>/dev/null || echo 'not a repo'); echo \"$(date): Working on branch: $branch\" >> ~/.claude/git.log"
          }
        ]
      }
    ]
  }
}
```

**What it does:**
- Triggers on session start OR resume
- Records current git branch
- Handles non-repo directories gracefully

---

## Example 5: Tool Counter

Count how many times each tool is used.

**Configuration:**
```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "*",
        "hooks": [
          {
            "type": "command",
            "command": "echo \"$tool_name\" >> ~/.claude/tool-counts.txt"
          }
        ]
      }
    ]
  }
}
```

**Analysis script:**
```bash
# Count tool usage
sort ~/.claude/tool-counts.txt | uniq -c | sort -rn
```

**Sample output:**
```
    142 Read
     87 Edit
     45 Bash
     23 Write
     12 Grep
```

---

## Matcher Patterns

### For Tool Events (PreToolUse, PostToolUse, PermissionRequest)

| Pattern | Matches |
|---------|---------|
| `"Write"` | Exact match (case-sensitive) |
| `"Write\|Edit"` | Write OR Edit |
| `"Notebook.*"` | NotebookEdit, NotebookRead, etc. |
| `".*"` or `"*"` | All tools |
| `"Bash"` | All Bash commands |
| `"Bash(git:*)"` | Only git commands |
| `"mcp__memory__.*"` | All memory MCP tools |

### For SessionStart

| Pattern | Triggers On |
|---------|-------------|
| `"startup"` | Fresh session start |
| `"resume"` | Resuming previous session |
| `"clear"` | After /clear command |
| `"compact"` | After context compaction |
| `"startup\|resume"` | Either startup or resume |

### For PreCompact

| Pattern | Triggers On |
|---------|-------------|
| `"manual"` | User-initiated compaction |
| `"auto"` | Automatic compaction |

---

## Environment Variables

Available in all hook commands:

| Variable | Value |
|----------|-------|
| `$tool_name` | Name of the tool (tool events only) |
| `$CLAUDE_PROJECT_DIR` | Project root directory |
| `$CLAUDE_CODE_REMOTE` | "true" if remote, else empty |

---

## Inline Command Tips

### Chaining Commands
```json
"command": "cmd1 && cmd2 && cmd3"
```

### Conditional Execution
```json
"command": "[ -f ~/.claude/hooks/enabled ] && echo 'Hook ran'"
```

### Redirecting Errors
```json
"command": "some-command 2>/dev/null || true"
```

### Using Subshells
```json
"command": "echo \"Time: $(date '+%H:%M:%S')\""
```

### Multi-line (Avoid)
```json
// DON'T do this - use external script instead
"command": "cmd1;\ncmd2;\ncmd3"
```

---

## Limitations of Basic Hooks

Basic inline hooks are limited:

1. **No stdin access** — Can't read full JSON input
2. **No complex logic** — Hard to do conditionals
3. **No JSON output** — Can't return structured decisions
4. **No input parsing** — Only `$tool_name` available

**When to upgrade to scripts:**
- Need to read `tool_input` fields (file paths, content)
- Need conditional blocking logic
- Need to return JSON decisions
- Logic exceeds one line

See `templates/with-scripts.md` for external script patterns.

---

## Complete Working Example

**Goal:** Log all file operations with paths.

**Configuration** (`~/.claude/settings.json`):
```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Write|Edit|Read",
        "hooks": [
          {
            "type": "command",
            "command": "echo \"$(date '+%H:%M:%S') | $tool_name\" >> ~/.claude/file-ops.log",
            "timeout": 5
          }
        ]
      }
    ]
  }
}
```

**Verification:**
```bash
# Check hooks are registered
/hooks

# Watch the log
tail -f ~/.claude/file-ops.log

# In another terminal, use Claude to edit files
# Log entries appear in real-time
```

**Expected behavior:**
- Every Read, Write, or Edit triggers the hook
- Timestamp and tool name logged
- 5-second timeout (quick operation)
- Non-blocking (PostToolUse)

---

## Troubleshooting

### Hook not triggering
1. Check `/hooks` command — is it registered?
2. Verify matcher case — `"Write"` not `"write"`
3. Check event name — `"PostToolUse"` not `"postToolUse"`

### Command failing
1. Test command manually in terminal first
2. Add `|| true` to prevent failures from showing
3. Check file permissions on log files

### No output visible
1. PostToolUse output only shows in `--debug` mode
2. Use `>> file.log` to capture output
3. Check stderr with `2>&1`

---

## Next Steps

Once comfortable with basic hooks:
1. **Add scripts** → `templates/with-scripts.md`
2. **Add blocking** → `templates/with-decisions.md`
3. **Add LLM evaluation** → `templates/with-prompts.md`
4. **Build complete systems** → `templates/production-hooks.md`
