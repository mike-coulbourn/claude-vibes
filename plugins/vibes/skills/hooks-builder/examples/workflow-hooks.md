# Workflow Hooks Examples

Six complete hooks for session management, context injection, notifications, and workflow automation.

---

## 1. Session Setup

Configure environment and load context when sessions start.

### Configuration

```json
{
  "hooks": {
    "SessionStart": [
      {
        "matcher": "startup|resume",
        "hooks": [
          {
            "type": "command",
            "command": "bash ~/.claude/hooks/session-setup.sh",
            "timeout": 30
          }
        ]
      }
    ]
  }
}
```

### Script (`~/.claude/hooks/session-setup.sh`)

```bash
#!/bin/bash
set -euo pipefail

# Read input
input=$(cat)
source=$(echo "$input" | jq -r '.source // "startup"')
cwd=$(echo "$input" | jq -r '.cwd // empty')
session_id=$(echo "$input" | jq -r '.session_id // "unknown"')

# Log session start
log_file="$HOME/.claude/sessions.log"
mkdir -p "$(dirname "$log_file")"
echo "$(date '+%Y-%m-%d %H:%M:%S') | $source | $session_id | $cwd" >> "$log_file"

# Set up environment variables (if CLAUDE_ENV_FILE is available)
if [[ -n "${CLAUDE_ENV_FILE:-}" ]]; then
    # Project-specific environment
    if [[ -n "$cwd" ]] && [[ -d "$cwd" ]]; then
        # Detect project type and set appropriate vars
        if [[ -f "$cwd/package.json" ]]; then
            echo "export NODE_ENV=development" >> "$CLAUDE_ENV_FILE"
        fi
        if [[ -f "$cwd/requirements.txt" ]] || [[ -f "$cwd/pyproject.toml" ]]; then
            echo "export PYTHONDONTWRITEBYTECODE=1" >> "$CLAUDE_ENV_FILE"
        fi

        # Load .env.example as template (without values)
        if [[ -f "$cwd/.env.example" ]]; then
            echo "# Environment template loaded from .env.example" >> "$CLAUDE_ENV_FILE"
        fi
    fi

    # Global settings
    echo "export CLAUDE_SESSION_START=$(date +%s)" >> "$CLAUDE_ENV_FILE"
    echo "export CLAUDE_HOOKS_ACTIVE=true" >> "$CLAUDE_ENV_FILE"
fi

# Check for required tools
required_tools=("git" "jq")
missing_tools=()

for tool in "${required_tools[@]}"; do
    if ! command -v "$tool" &> /dev/null; then
        missing_tools+=("$tool")
    fi
done

if [[ ${#missing_tools[@]} -gt 0 ]]; then
    echo "Warning: Missing tools: ${missing_tools[*]}" >&2
fi

# Git info (if in a repo)
if [[ -n "$cwd" ]] && git -C "$cwd" rev-parse --git-dir &> /dev/null; then
    branch=$(git -C "$cwd" branch --show-current 2>/dev/null || echo "unknown")
    echo "$(date '+%Y-%m-%d %H:%M:%S') | Git branch: $branch" >> "$log_file"

    # Check for uncommitted changes
    if ! git -C "$cwd" diff --quiet 2>/dev/null; then
        echo "$(date '+%Y-%m-%d %H:%M:%S') | Warning: Uncommitted changes" >> "$log_file"
    fi
fi

exit 0
```

---

## 2. Context Injector

Add project-specific context to every prompt.

### Configuration

```json
{
  "hooks": {
    "UserPromptSubmit": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "python3 ~/.claude/hooks/context-injector.py",
            "timeout": 10
          }
        ]
      }
    ]
  }
}
```

### Script (`~/.claude/hooks/context-injector.py`)

```python
#!/usr/bin/env python3
"""
Hook: Context Injector
Event: UserPromptSubmit
Purpose: Add project-specific context to prompts
"""

import sys
import json
import os
from pathlib import Path
from datetime import datetime

def get_project_context(cwd: str) -> list:
    """Gather project context."""
    context = []
    cwd = Path(cwd)

    # Project type detection
    if (cwd / "package.json").exists():
        try:
            with open(cwd / "package.json") as f:
                pkg = json.load(f)
                name = pkg.get('name', 'unknown')
                context.append(f"Node.js project: {name}")

                # Key dependencies
                deps = list(pkg.get('dependencies', {}).keys())[:5]
                if deps:
                    context.append(f"Dependencies: {', '.join(deps)}")
        except:
            context.append("Node.js project")

    if (cwd / "requirements.txt").exists():
        context.append("Python project")

    if (cwd / "go.mod").exists():
        context.append("Go project")

    if (cwd / "Cargo.toml").exists():
        context.append("Rust project")

    # Git status
    git_dir = cwd / ".git"
    if git_dir.exists():
        try:
            import subprocess
            branch = subprocess.run(
                ["git", "branch", "--show-current"],
                capture_output=True, text=True, cwd=cwd, timeout=5
            ).stdout.strip()
            if branch:
                context.append(f"Git branch: {branch}")
        except:
            pass

    # CLAUDE.md rules
    claude_md = cwd / "CLAUDE.md"
    if claude_md.exists():
        context.append("Project has CLAUDE.md - follow its conventions")

    # Recent activity
    try:
        import subprocess
        recent = subprocess.run(
            ["git", "log", "--oneline", "-1"],
            capture_output=True, text=True, cwd=cwd, timeout=5
        ).stdout.strip()
        if recent:
            context.append(f"Last commit: {recent[:50]}")
    except:
        pass

    return context

def get_time_context() -> str:
    """Get time-based context."""
    hour = datetime.now().hour
    if 5 <= hour < 12:
        return "Good morning"
    elif 12 <= hour < 17:
        return "Good afternoon"
    elif 17 <= hour < 21:
        return "Good evening"
    else:
        return "Working late"

def main():
    try:
        data = json.load(sys.stdin)
    except json.JSONDecodeError:
        sys.exit(0)

    cwd = data.get('cwd', os.getcwd())
    prompt = data.get('prompt', '')

    # Skip for very short prompts (likely commands)
    if len(prompt) < 20:
        sys.exit(0)

    context_parts = get_project_context(cwd)

    if context_parts:
        context_str = " | ".join(context_parts)
        output = {
            "hookSpecificOutput": {
                "hookEventName": "UserPromptSubmit",
                "additionalContext": f"[Context: {context_str}]"
            }
        }
        print(json.dumps(output))

    sys.exit(0)

if __name__ == '__main__':
    main()
```

---

## 3. Completion Checker

Verify task completion before allowing Claude to stop.

### Configuration

```json
{
  "hooks": {
    "Stop": [
      {
        "hooks": [
          {
            "type": "prompt",
            "prompt": "Review the conversation and verify task completion. Check:\n1. Did Claude complete all requested tasks?\n2. Were all files that needed changes actually modified?\n3. Are there any TODOs or incomplete items mentioned?\n4. Did Claude run tests if code was changed?\n5. Were there any errors that weren't resolved?\n\nIf any task is incomplete, set continue=true and explain what's missing.\nIf all tasks are complete, allow the stop.\n\nConversation context: $ARGUMENTS",
            "timeout": 45
          }
        ]
      }
    ]
  }
}
```

### Alternative: Command-Based Checker

```json
{
  "hooks": {
    "Stop": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "python3 ~/.claude/hooks/completion-checker.py",
            "timeout": 10
          }
        ]
      }
    ]
  }
}
```

### Script (`~/.claude/hooks/completion-checker.py`)

```python
#!/usr/bin/env python3
"""
Hook: Completion Checker
Event: Stop
Purpose: Basic completion verification
"""

import sys
import json
import os
from pathlib import Path

def check_for_incomplete_markers(cwd: str) -> list:
    """Check for signs of incomplete work."""
    issues = []
    cwd = Path(cwd)

    # Check for TODO comments in recently modified files
    try:
        import subprocess
        # Get files modified in last 5 minutes
        result = subprocess.run(
            ["find", str(cwd), "-type", "f", "-mmin", "-5",
             "-name", "*.py", "-o", "-name", "*.js", "-o", "-name", "*.ts"],
            capture_output=True, text=True, timeout=10
        )
        recent_files = result.stdout.strip().split('\n')

        for file_path in recent_files:
            if file_path and os.path.isfile(file_path):
                try:
                    with open(file_path, 'r') as f:
                        content = f.read()
                        if 'TODO' in content or 'FIXME' in content:
                            issues.append(f"TODO/FIXME in {os.path.basename(file_path)}")
                except:
                    pass
    except:
        pass

    # Check for uncommitted changes
    try:
        import subprocess
        result = subprocess.run(
            ["git", "status", "--porcelain"],
            capture_output=True, text=True, cwd=cwd, timeout=5
        )
        if result.stdout.strip():
            lines = result.stdout.strip().split('\n')
            issues.append(f"{len(lines)} uncommitted changes")
    except:
        pass

    return issues

def main():
    try:
        data = json.load(sys.stdin)
    except json.JSONDecodeError:
        sys.exit(0)

    cwd = data.get('cwd', os.getcwd())
    stop_hook_active = data.get('stop_hook_active', False)

    # Don't run repeatedly
    if stop_hook_active:
        sys.exit(0)

    issues = check_for_incomplete_markers(cwd)

    if issues:
        output = {
            "continue": True,
            "stopReason": f"Potential incomplete work: {'; '.join(issues)}"
        }
        print(json.dumps(output))

    sys.exit(0)

if __name__ == '__main__':
    main()
```

---

## 4. Notification Forwarder

Send notifications to external services (Slack, Discord, etc.).

### Configuration

```json
{
  "hooks": {
    "Notification": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "python3 ~/.claude/hooks/notification-forwarder.py",
            "timeout": 15
          }
        ]
      }
    ]
  }
}
```

### Script (`~/.claude/hooks/notification-forwarder.py`)

```python
#!/usr/bin/env python3
"""
Hook: Notification Forwarder
Event: Notification
Purpose: Forward notifications to external services
"""

import sys
import json
import os
import urllib.request
import urllib.error
from datetime import datetime

# Configuration - set these environment variables or modify directly
SLACK_WEBHOOK = os.environ.get('CLAUDE_SLACK_WEBHOOK', '')
DISCORD_WEBHOOK = os.environ.get('CLAUDE_DISCORD_WEBHOOK', '')
NTFY_TOPIC = os.environ.get('CLAUDE_NTFY_TOPIC', '')

def send_slack(message: str, notification_type: str):
    """Send to Slack webhook."""
    if not SLACK_WEBHOOK:
        return

    # Color based on type
    colors = {
        'error': '#dc3545',
        'warning': '#ffc107',
        'success': '#28a745',
        'info': '#17a2b8',
    }
    color = colors.get(notification_type, '#6c757d')

    payload = {
        "attachments": [{
            "color": color,
            "title": f"Claude Code - {notification_type.title()}",
            "text": message,
            "ts": datetime.now().timestamp()
        }]
    }

    try:
        req = urllib.request.Request(
            SLACK_WEBHOOK,
            data=json.dumps(payload).encode(),
            headers={'Content-Type': 'application/json'}
        )
        urllib.request.urlopen(req, timeout=10)
    except Exception as e:
        log_error(f"Slack send failed: {e}")

def send_discord(message: str, notification_type: str):
    """Send to Discord webhook."""
    if not DISCORD_WEBHOOK:
        return

    # Color based on type (Discord uses decimal)
    colors = {
        'error': 14495300,    # Red
        'warning': 16761095,  # Yellow
        'success': 2664261,   # Green
        'info': 2201331,      # Blue
    }
    color = colors.get(notification_type, 7105644)

    payload = {
        "embeds": [{
            "title": f"Claude Code - {notification_type.title()}",
            "description": message,
            "color": color,
            "timestamp": datetime.utcnow().isoformat()
        }]
    }

    try:
        req = urllib.request.Request(
            DISCORD_WEBHOOK,
            data=json.dumps(payload).encode(),
            headers={'Content-Type': 'application/json'}
        )
        urllib.request.urlopen(req, timeout=10)
    except Exception as e:
        log_error(f"Discord send failed: {e}")

def send_ntfy(message: str, notification_type: str):
    """Send to ntfy.sh topic."""
    if not NTFY_TOPIC:
        return

    # Priority based on type
    priorities = {
        'error': '5',     # Urgent
        'warning': '4',   # High
        'success': '3',   # Default
        'info': '2',      # Low
    }
    priority = priorities.get(notification_type, '3')

    try:
        url = f"https://ntfy.sh/{NTFY_TOPIC}"
        req = urllib.request.Request(
            url,
            data=message.encode(),
            headers={
                'Title': f'Claude Code - {notification_type.title()}',
                'Priority': priority,
                'Tags': 'robot,computer'
            }
        )
        urllib.request.urlopen(req, timeout=10)
    except Exception as e:
        log_error(f"ntfy send failed: {e}")

def send_desktop(message: str, notification_type: str):
    """Send desktop notification (macOS/Linux)."""
    import subprocess
    import platform

    title = f"Claude Code - {notification_type.title()}"

    try:
        if platform.system() == 'Darwin':
            # macOS
            script = f'display notification "{message}" with title "{title}"'
            subprocess.run(['osascript', '-e', script], timeout=5)
        elif platform.system() == 'Linux':
            # Linux with notify-send
            subprocess.run(['notify-send', title, message], timeout=5)
    except Exception as e:
        log_error(f"Desktop notification failed: {e}")

def log_error(message: str):
    """Log errors to file."""
    log_file = os.path.expanduser('~/.claude/notification-errors.log')
    os.makedirs(os.path.dirname(log_file), exist_ok=True)
    with open(log_file, 'a') as f:
        f.write(f"{datetime.now().isoformat()} | {message}\n")

def main():
    try:
        data = json.load(sys.stdin)
    except json.JSONDecodeError:
        sys.exit(0)

    message = data.get('message', '')
    notification_type = data.get('notification_type', 'info')

    if not message:
        sys.exit(0)

    # Send to all configured services
    send_slack(message, notification_type)
    send_discord(message, notification_type)
    send_ntfy(message, notification_type)
    send_desktop(message, notification_type)

    sys.exit(0)

if __name__ == '__main__':
    main()
```

### Environment Setup

```bash
# Add to ~/.bashrc or ~/.zshrc
export CLAUDE_SLACK_WEBHOOK="https://hooks.slack.com/services/..."
export CLAUDE_DISCORD_WEBHOOK="https://discord.com/api/webhooks/..."
export CLAUDE_NTFY_TOPIC="my-claude-notifications"
```

---

## 5. Time Tracker

Track session duration and tool usage statistics.

### Configuration

```json
{
  "hooks": {
    "SessionStart": [
      {
        "matcher": "startup",
        "hooks": [
          {
            "type": "command",
            "command": "python3 ~/.claude/hooks/time-tracker.py start",
            "timeout": 5
          }
        ]
      }
    ],
    "SessionEnd": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "python3 ~/.claude/hooks/time-tracker.py end",
            "timeout": 10
          }
        ]
      }
    ],
    "PostToolUse": [
      {
        "matcher": "*",
        "hooks": [
          {
            "type": "command",
            "command": "python3 ~/.claude/hooks/time-tracker.py tool",
            "timeout": 5
          }
        ]
      }
    ]
  }
}
```

### Script (`~/.claude/hooks/time-tracker.py`)

```python
#!/usr/bin/env python3
"""
Hook: Time Tracker
Events: SessionStart, SessionEnd, PostToolUse
Purpose: Track session duration and tool usage
"""

import sys
import json
import os
from datetime import datetime, timedelta
from pathlib import Path

DATA_DIR = Path.home() / '.claude' / 'time-tracking'
ACTIVE_SESSION_FILE = DATA_DIR / 'active_session.json'
HISTORY_FILE = DATA_DIR / 'history.jsonl'

def ensure_data_dir():
    DATA_DIR.mkdir(parents=True, exist_ok=True)

def start_session(session_id: str, cwd: str):
    """Record session start."""
    ensure_data_dir()

    session = {
        'session_id': session_id,
        'start_time': datetime.now().isoformat(),
        'cwd': cwd,
        'tool_counts': {},
        'tool_times': [],
    }

    with open(ACTIVE_SESSION_FILE, 'w') as f:
        json.dump(session, f)

def end_session(session_id: str, reason: str):
    """Record session end and save to history."""
    ensure_data_dir()

    if not ACTIVE_SESSION_FILE.exists():
        return

    with open(ACTIVE_SESSION_FILE, 'r') as f:
        session = json.load(f)

    # Calculate duration
    start = datetime.fromisoformat(session['start_time'])
    end = datetime.now()
    duration = (end - start).total_seconds()

    # Build summary
    summary = {
        'session_id': session['session_id'],
        'start_time': session['start_time'],
        'end_time': end.isoformat(),
        'duration_seconds': duration,
        'duration_human': str(timedelta(seconds=int(duration))),
        'end_reason': reason,
        'cwd': session['cwd'],
        'tool_counts': session.get('tool_counts', {}),
        'total_tool_uses': sum(session.get('tool_counts', {}).values()),
    }

    # Append to history
    with open(HISTORY_FILE, 'a') as f:
        f.write(json.dumps(summary) + '\n')

    # Clean up active session
    ACTIVE_SESSION_FILE.unlink(missing_ok=True)

    # Print summary for logging
    print(f"Session ended: {summary['duration_human']}, {summary['total_tool_uses']} tool uses")

def record_tool(tool_name: str):
    """Record tool usage."""
    ensure_data_dir()

    if not ACTIVE_SESSION_FILE.exists():
        return

    with open(ACTIVE_SESSION_FILE, 'r') as f:
        session = json.load(f)

    # Update counts
    counts = session.get('tool_counts', {})
    counts[tool_name] = counts.get(tool_name, 0) + 1
    session['tool_counts'] = counts

    # Record timestamp
    times = session.get('tool_times', [])
    times.append({'tool': tool_name, 'time': datetime.now().isoformat()})
    session['tool_times'] = times[-100]  # Keep last 100

    with open(ACTIVE_SESSION_FILE, 'w') as f:
        json.dump(session, f)

def main():
    if len(sys.argv) < 2:
        sys.exit(0)

    action = sys.argv[1]

    try:
        data = json.load(sys.stdin)
    except json.JSONDecodeError:
        data = {}

    session_id = data.get('session_id', 'unknown')
    cwd = data.get('cwd', os.getcwd())

    if action == 'start':
        start_session(session_id, cwd)
    elif action == 'end':
        reason = data.get('reason', 'unknown')
        end_session(session_id, reason)
    elif action == 'tool':
        tool_name = data.get('tool_name', 'unknown')
        record_tool(tool_name)

    sys.exit(0)

if __name__ == '__main__':
    main()
```

### Viewing Time Stats

```bash
# View session history
cat ~/.claude/time-tracking/history.jsonl | jq .

# Total time today
cat ~/.claude/time-tracking/history.jsonl | \
  jq -r 'select(.start_time | startswith("'$(date +%Y-%m-%d)'")) | .duration_seconds' | \
  awk '{sum += $1} END {print sum/3600 " hours"}'

# Tool usage summary
cat ~/.claude/time-tracking/history.jsonl | \
  jq -r '.tool_counts | to_entries[] | "\(.key): \(.value)"' | \
  sort | uniq -c | sort -rn

# Average session length
cat ~/.claude/time-tracking/history.jsonl | \
  jq -s 'map(.duration_seconds) | add / length / 60 | floor' | \
  xargs -I {} echo "{} minutes average"
```

---

## 6. Backup Creator

Create backups of files before editing.

### Configuration

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Edit",
        "hooks": [
          {
            "type": "command",
            "command": "python3 ~/.claude/hooks/backup-creator.py",
            "timeout": 10
          }
        ]
      }
    ]
  }
}
```

### Script (`~/.claude/hooks/backup-creator.py`)

```python
#!/usr/bin/env python3
"""
Hook: Backup Creator
Event: PreToolUse (Edit)
Purpose: Backup files before editing
"""

import sys
import json
import os
import shutil
from datetime import datetime
from pathlib import Path

# Configuration
BACKUP_DIR = Path.home() / '.claude' / 'backups'
MAX_BACKUPS_PER_FILE = 5
MAX_FILE_SIZE_MB = 10

def should_backup(file_path: str) -> bool:
    """Determine if file should be backed up."""
    path = Path(file_path)

    # Skip if doesn't exist
    if not path.exists():
        return False

    # Skip large files
    size_mb = path.stat().st_size / (1024 * 1024)
    if size_mb > MAX_FILE_SIZE_MB:
        return False

    # Skip binary files (basic check)
    binary_extensions = ['.exe', '.dll', '.so', '.dylib', '.bin', '.img', '.iso']
    if path.suffix.lower() in binary_extensions:
        return False

    # Skip common non-code files
    skip_patterns = ['node_modules', '__pycache__', '.git', 'venv', 'dist', 'build']
    if any(p in str(file_path) for p in skip_patterns):
        return False

    return True

def create_backup(file_path: str, cwd: str) -> str:
    """Create backup of file."""
    path = Path(file_path)

    # Create backup directory structure
    # ~/.claude/backups/project_name/relative/path/filename/timestamp.ext
    try:
        project_name = Path(cwd).name
    except:
        project_name = 'unknown'

    try:
        relative = path.relative_to(cwd)
    except ValueError:
        relative = path.name

    backup_subdir = BACKUP_DIR / project_name / relative
    backup_subdir.mkdir(parents=True, exist_ok=True)

    # Create timestamped backup
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    backup_name = f"{timestamp}{path.suffix}"
    backup_path = backup_subdir / backup_name

    # Copy file
    shutil.copy2(file_path, backup_path)

    # Cleanup old backups
    cleanup_old_backups(backup_subdir, path.suffix)

    return str(backup_path)

def cleanup_old_backups(backup_dir: Path, extension: str):
    """Remove old backups, keeping only MAX_BACKUPS_PER_FILE."""
    backups = sorted(
        [f for f in backup_dir.glob(f'*{extension}')],
        key=lambda f: f.stat().st_mtime,
        reverse=True
    )

    for old_backup in backups[MAX_BACKUPS_PER_FILE:]:
        old_backup.unlink()

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

    if should_backup(file_path):
        try:
            backup_path = create_backup(file_path, cwd)
            # Log backup
            log_file = BACKUP_DIR / 'backup.log'
            with open(log_file, 'a') as f:
                f.write(f"{datetime.now().isoformat()} | {file_path} -> {backup_path}\n")
        except Exception as e:
            # Don't block on backup failure
            pass

    sys.exit(0)

if __name__ == '__main__':
    main()
```

### Restoring Backups

```bash
# List backups for a file
ls -la ~/.claude/backups/project-name/path/to/file/

# View backup
cat ~/.claude/backups/project-name/src/index.ts/20250115_143022.ts

# Restore backup
cp ~/.claude/backups/project-name/src/index.ts/20250115_143022.ts ./src/index.ts

# Find recent backups
find ~/.claude/backups -type f -mmin -60 -ls

# Backup disk usage
du -sh ~/.claude/backups/
```

---

## Combined Workflow Configuration

Use all workflow hooks together:

```json
{
  "hooks": {
    "SessionStart": [
      {
        "matcher": "startup|resume",
        "hooks": [
          {"type": "command", "command": "bash ~/.claude/hooks/session-setup.sh", "timeout": 30},
          {"type": "command", "command": "python3 ~/.claude/hooks/time-tracker.py start", "timeout": 5}
        ]
      }
    ],
    "UserPromptSubmit": [
      {
        "hooks": [
          {"type": "command", "command": "python3 ~/.claude/hooks/context-injector.py", "timeout": 10}
        ]
      }
    ],
    "PreToolUse": [
      {
        "matcher": "Edit",
        "hooks": [
          {"type": "command", "command": "python3 ~/.claude/hooks/backup-creator.py", "timeout": 10}
        ]
      }
    ],
    "PostToolUse": [
      {
        "matcher": "*",
        "hooks": [
          {"type": "command", "command": "python3 ~/.claude/hooks/time-tracker.py tool", "timeout": 5}
        ]
      }
    ],
    "Notification": [
      {
        "hooks": [
          {"type": "command", "command": "python3 ~/.claude/hooks/notification-forwarder.py", "timeout": 15}
        ]
      }
    ],
    "Stop": [
      {
        "hooks": [
          {"type": "prompt", "prompt": "Verify completion: $ARGUMENTS", "timeout": 45}
        ]
      }
    ],
    "SessionEnd": [
      {
        "hooks": [
          {"type": "command", "command": "python3 ~/.claude/hooks/time-tracker.py end", "timeout": 10}
        ]
      }
    ]
  }
}
```

---

## Workflow Dashboard

Create a simple dashboard to view all workflow data:

```bash
#!/bin/bash
# ~/.claude/hooks/dashboard.sh

echo "=== Claude Code Workflow Dashboard ==="
echo ""

echo "📊 Today's Sessions:"
cat ~/.claude/time-tracking/history.jsonl 2>/dev/null | \
  jq -r 'select(.start_time | startswith("'$(date +%Y-%m-%d)'")) | "  \(.duration_human) - \(.total_tool_uses) tools"' || echo "  No sessions today"
echo ""

echo "🔧 Recent Tool Usage:"
cat ~/.claude/time-tracking/history.jsonl 2>/dev/null | \
  tail -5 | jq -r '.tool_counts | to_entries | sort_by(-.value) | .[0:3][] | "  \(.key): \(.value)"' || echo "  No data"
echo ""

echo "💾 Recent Backups:"
find ~/.claude/backups -type f -mmin -60 2>/dev/null | tail -5 | while read f; do
  echo "  $(basename "$f")"
done || echo "  No recent backups"
echo ""

echo "📝 Session Log (last 5):"
tail -5 ~/.claude/sessions.log 2>/dev/null || echo "  No sessions logged"
```
