# Common Hook Pitfalls

Read this before finalizing a hook, or when a hook does not fire, blocks unexpectedly, or hangs.

## 1. Forgetting Exit Code 2 for Blocking
```bash
# WRONG - exit 1 doesn't block
echo "Error" >&2
exit 1

# RIGHT - exit 2 blocks Claude
echo "BLOCKED: reason" >&2
exit 2
```

## 2. Case Sensitivity in Matchers
```json
// WRONG - won't match "Write" tool
"matcher": "write"

// RIGHT - case-sensitive match
"matcher": "Write"
```

## 3. Unquoted Variables (Injection Risk)
```bash
# WRONG - command injection vulnerability
rm $file_path

# RIGHT - properly quoted
rm -- "$file_path"
```

## 4. Missing Shebang in Scripts
```bash
# WRONG - no shebang, may fail
set -euo pipefail

# RIGHT - explicit interpreter
#!/bin/bash
set -euo pipefail
```

## 5. Not Making Scripts Executable
```bash
# Don't forget!
chmod +x ~/.claude/hooks/my-hook.sh
```

## 6. Forgetting to Quote Paths in JSON
```json
// WRONG - spaces in path will break
"command": "$CLAUDE_PROJECT_DIR/.claude/hooks/script.sh"

// RIGHT - quoted path
"command": "\"$CLAUDE_PROJECT_DIR\"/.claude/hooks/script.sh"
```

## 7. No Error Handling
```bash
# WRONG - silent failures
input=$(cat)
tool=$(echo "$input" | jq -r '.tool_name')

# RIGHT - handle errors
input=$(cat) || { echo "Failed to read input" >&2; exit 1; }
tool=$(echo "$input" | jq -r '.tool_name') || { echo "Failed to parse JSON" >&2; exit 1; }
```

## 8. Logging Sensitive Data
```bash
# WRONG - may log secrets
echo "Processing: $input" >> /tmp/debug.log

# RIGHT - sanitize before logging
echo "Processing tool: $tool_name" >> /tmp/debug.log
```

---
