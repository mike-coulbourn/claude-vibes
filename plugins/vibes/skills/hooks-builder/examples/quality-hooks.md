# Code Quality Hooks Examples

Six complete hooks for automated code formatting, linting, testing, and quality enforcement.

---

## 1. Auto Formatter

Automatically format code after Write/Edit operations.

### Configuration

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Write|Edit",
        "hooks": [
          {
            "type": "command",
            "command": "bash ~/.claude/hooks/auto-formatter.sh",
            "timeout": 30
          }
        ]
      }
    ]
  }
}
```

### Script (`~/.claude/hooks/auto-formatter.sh`)

```bash
#!/bin/bash
set -euo pipefail

# Read input
input=$(cat)
file_path=$(echo "$input" | jq -r '.tool_input.file_path // empty')

# Exit if no file path
[[ -z "$file_path" ]] && exit 0
[[ ! -f "$file_path" ]] && exit 0

# Get file extension
ext="${file_path##*.}"

# Format based on file type
case "$ext" in
    # JavaScript/TypeScript
    js|jsx|ts|tsx|mjs|cjs)
        if command -v prettier &> /dev/null; then
            prettier --write "$file_path" 2>/dev/null || true
        elif command -v npx &> /dev/null; then
            npx prettier --write "$file_path" 2>/dev/null || true
        fi
        ;;

    # Python
    py)
        if command -v black &> /dev/null; then
            black --quiet "$file_path" 2>/dev/null || true
        elif command -v autopep8 &> /dev/null; then
            autopep8 --in-place "$file_path" 2>/dev/null || true
        fi
        # Sort imports
        if command -v isort &> /dev/null; then
            isort --quiet "$file_path" 2>/dev/null || true
        fi
        ;;

    # Go
    go)
        if command -v gofmt &> /dev/null; then
            gofmt -w "$file_path" 2>/dev/null || true
        fi
        if command -v goimports &> /dev/null; then
            goimports -w "$file_path" 2>/dev/null || true
        fi
        ;;

    # Rust
    rs)
        if command -v rustfmt &> /dev/null; then
            rustfmt "$file_path" 2>/dev/null || true
        fi
        ;;

    # Ruby
    rb)
        if command -v rubocop &> /dev/null; then
            rubocop -a "$file_path" 2>/dev/null || true
        fi
        ;;

    # JSON
    json)
        if command -v jq &> /dev/null; then
            tmp=$(mktemp)
            jq '.' "$file_path" > "$tmp" 2>/dev/null && mv "$tmp" "$file_path" || rm -f "$tmp"
        elif command -v prettier &> /dev/null; then
            prettier --write "$file_path" 2>/dev/null || true
        fi
        ;;

    # YAML
    yml|yaml)
        if command -v prettier &> /dev/null; then
            prettier --write "$file_path" 2>/dev/null || true
        fi
        ;;

    # Markdown
    md)
        if command -v prettier &> /dev/null; then
            prettier --write "$file_path" 2>/dev/null || true
        fi
        ;;

    # CSS/SCSS/Less
    css|scss|less)
        if command -v prettier &> /dev/null; then
            prettier --write "$file_path" 2>/dev/null || true
        fi
        ;;

    # HTML
    html|htm)
        if command -v prettier &> /dev/null; then
            prettier --write "$file_path" 2>/dev/null || true
        fi
        ;;

    # Shell
    sh|bash)
        if command -v shfmt &> /dev/null; then
            shfmt -w "$file_path" 2>/dev/null || true
        fi
        ;;
esac

exit 0
```

---

## 2. Linter Runner

Run linters after code changes.

### Configuration

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Write|Edit",
        "hooks": [
          {
            "type": "command",
            "command": "python3 ~/.claude/hooks/linter-runner.py",
            "timeout": 60
          }
        ]
      }
    ]
  }
}
```

### Script (`~/.claude/hooks/linter-runner.py`)

```python
#!/usr/bin/env python3
"""
Hook: Linter Runner
Event: PostToolUse (Write, Edit)
Purpose: Run linters and report issues
"""

import sys
import json
import os
import subprocess
from pathlib import Path

# Linter configurations by extension
LINTERS = {
    '.js': [
        ('eslint', ['eslint', '--fix', '{file}']),
        ('jshint', ['jshint', '{file}']),
    ],
    '.jsx': [
        ('eslint', ['eslint', '--fix', '{file}']),
    ],
    '.ts': [
        ('eslint', ['eslint', '--fix', '{file}']),
        ('tsc', ['npx', 'tsc', '--noEmit', '{file}']),
    ],
    '.tsx': [
        ('eslint', ['eslint', '--fix', '{file}']),
    ],
    '.py': [
        ('ruff', ['ruff', 'check', '--fix', '{file}']),
        ('flake8', ['flake8', '{file}']),
        ('pylint', ['pylint', '--errors-only', '{file}']),
        ('mypy', ['mypy', '{file}']),
    ],
    '.go': [
        ('golint', ['golint', '{file}']),
        ('go vet', ['go', 'vet', '{file}']),
    ],
    '.rb': [
        ('rubocop', ['rubocop', '-a', '{file}']),
    ],
    '.sh': [
        ('shellcheck', ['shellcheck', '{file}']),
    ],
    '.bash': [
        ('shellcheck', ['shellcheck', '{file}']),
    ],
}

def command_exists(cmd: str) -> bool:
    """Check if command is available."""
    try:
        subprocess.run(
            ['which', cmd],
            capture_output=True,
            timeout=5
        )
        return True
    except:
        return False

def run_linter(name: str, cmd: list, file_path: str) -> dict:
    """Run a linter and return results."""
    # Replace {file} placeholder
    cmd = [arg.replace('{file}', file_path) for arg in cmd]

    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=30,
            cwd=os.path.dirname(file_path) or '.'
        )
        return {
            'linter': name,
            'success': result.returncode == 0,
            'output': result.stdout[:500] if result.stdout else '',
            'errors': result.stderr[:500] if result.stderr else '',
        }
    except subprocess.TimeoutExpired:
        return {'linter': name, 'success': False, 'errors': 'Timeout'}
    except FileNotFoundError:
        return {'linter': name, 'success': False, 'errors': 'Not installed'}
    except Exception as e:
        return {'linter': name, 'success': False, 'errors': str(e)}

def main():
    try:
        data = json.load(sys.stdin)
    except json.JSONDecodeError:
        sys.exit(0)

    tool_input = data.get('tool_input', {})
    file_path = tool_input.get('file_path', '')

    if not file_path or not os.path.isfile(file_path):
        sys.exit(0)

    ext = Path(file_path).suffix.lower()
    linters = LINTERS.get(ext, [])

    if not linters:
        sys.exit(0)

    results = []
    for name, cmd in linters:
        # Check if linter is available
        if command_exists(cmd[0]):
            result = run_linter(name, cmd, file_path)
            results.append(result)
            # Stop on first successful linter for each type
            if result['success']:
                break

    # Log results
    log_file = Path.home() / '.claude' / 'lint.log'
    log_file.parent.mkdir(parents=True, exist_ok=True)
    with open(log_file, 'a') as f:
        for r in results:
            status = "OK" if r['success'] else "FAIL"
            f.write(f"{file_path} | {r['linter']} | {status}\n")
            if r.get('errors'):
                f.write(f"  {r['errors'][:200]}\n")

    sys.exit(0)

if __name__ == '__main__':
    main()
```

---

## 3. Type Checker

Run type checking after TypeScript/Python changes.

### Configuration

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Write|Edit",
        "hooks": [
          {
            "type": "command",
            "command": "bash ~/.claude/hooks/type-checker.sh",
            "timeout": 60
          }
        ]
      }
    ]
  }
}
```

### Script (`~/.claude/hooks/type-checker.sh`)

```bash
#!/bin/bash
set -euo pipefail

input=$(cat)
file_path=$(echo "$input" | jq -r '.tool_input.file_path // empty')
cwd=$(echo "$input" | jq -r '.cwd // empty')

[[ -z "$file_path" ]] && exit 0
[[ ! -f "$file_path" ]] && exit 0

ext="${file_path##*.}"
log_file="$HOME/.claude/typecheck.log"
mkdir -p "$(dirname "$log_file")"

case "$ext" in
    ts|tsx)
        # TypeScript - check if tsconfig exists
        if [[ -f "${cwd}/tsconfig.json" ]] || [[ -f "$(dirname "$file_path")/tsconfig.json" ]]; then
            if command -v npx &> /dev/null; then
                echo "=== Type check: $file_path ===" >> "$log_file"
                npx tsc --noEmit 2>&1 | head -20 >> "$log_file" || true
            fi
        fi
        ;;

    py)
        # Python - run mypy if available
        if command -v mypy &> /dev/null; then
            echo "=== Type check: $file_path ===" >> "$log_file"
            mypy "$file_path" 2>&1 | head -20 >> "$log_file" || true
        elif command -v pyright &> /dev/null; then
            echo "=== Type check: $file_path ===" >> "$log_file"
            pyright "$file_path" 2>&1 | head -20 >> "$log_file" || true
        fi
        ;;

    go)
        # Go - type checking is part of compilation
        if command -v go &> /dev/null; then
            echo "=== Type check: $file_path ===" >> "$log_file"
            go build -o /dev/null "$file_path" 2>&1 | head -20 >> "$log_file" || true
        fi
        ;;
esac

exit 0
```

---

## 4. Test Runner

Automatically run related tests after code changes.

### Configuration

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Write|Edit",
        "hooks": [
          {
            "type": "command",
            "command": "python3 ~/.claude/hooks/test-runner.py",
            "timeout": 120
          }
        ]
      }
    ]
  }
}
```

### Script (`~/.claude/hooks/test-runner.py`)

```python
#!/usr/bin/env python3
"""
Hook: Test Runner
Event: PostToolUse (Write, Edit)
Purpose: Run related tests after code changes
"""

import sys
import json
import os
import subprocess
from pathlib import Path

def find_related_tests(file_path: str) -> list:
    """Find test files related to the changed file."""
    path = Path(file_path)
    name = path.stem
    parent = path.parent

    # Common test patterns
    test_patterns = [
        # Same directory
        parent / f"test_{name}.py",
        parent / f"{name}_test.py",
        parent / f"{name}.test.js",
        parent / f"{name}.test.ts",
        parent / f"{name}.test.jsx",
        parent / f"{name}.test.tsx",
        parent / f"{name}.spec.js",
        parent / f"{name}.spec.ts",

        # __tests__ directory
        parent / "__tests__" / f"{name}.test.js",
        parent / "__tests__" / f"{name}.test.ts",
        parent / "__tests__" / f"{name}.test.jsx",
        parent / "__tests__" / f"{name}.test.tsx",

        # tests directory (sibling)
        parent.parent / "tests" / f"test_{name}.py",
        parent.parent / "tests" / f"{name}_test.py",

        # test directory (sibling)
        parent.parent / "test" / f"{name}.test.js",
        parent.parent / "test" / f"{name}.test.ts",
    ]

    # Find existing test files
    return [str(p) for p in test_patterns if p.exists()]

def detect_test_framework(cwd: str) -> tuple:
    """Detect test framework based on project files."""
    cwd = Path(cwd)

    # Node.js projects
    if (cwd / "package.json").exists():
        with open(cwd / "package.json") as f:
            try:
                pkg = json.load(f)
                deps = {**pkg.get('dependencies', {}), **pkg.get('devDependencies', {})}

                if 'vitest' in deps:
                    return 'vitest', ['npx', 'vitest', 'run']
                elif 'jest' in deps:
                    return 'jest', ['npx', 'jest', '--passWithNoTests']
                elif 'mocha' in deps:
                    return 'mocha', ['npx', 'mocha']
            except:
                pass

    # Python projects
    if (cwd / "pytest.ini").exists() or (cwd / "pyproject.toml").exists():
        return 'pytest', ['pytest', '-x', '--tb=short']
    if (cwd / "setup.py").exists():
        return 'pytest', ['pytest', '-x', '--tb=short']

    # Go projects
    if (cwd / "go.mod").exists():
        return 'go test', ['go', 'test', '-v']

    # Rust projects
    if (cwd / "Cargo.toml").exists():
        return 'cargo test', ['cargo', 'test']

    return None, None

def run_tests(test_files: list, framework: str, cmd: list, cwd: str) -> dict:
    """Run tests and return results."""
    if not test_files:
        return {'ran': False, 'reason': 'No related tests found'}

    try:
        # Add test files to command
        if framework in ['jest', 'vitest']:
            cmd.extend(test_files)
        elif framework == 'pytest':
            cmd.extend(test_files)

        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=90,
            cwd=cwd
        )

        return {
            'ran': True,
            'framework': framework,
            'tests': test_files,
            'passed': result.returncode == 0,
            'output': result.stdout[-500:] if result.stdout else '',
            'errors': result.stderr[-500:] if result.stderr else '',
        }

    except subprocess.TimeoutExpired:
        return {'ran': True, 'passed': False, 'errors': 'Test timeout'}
    except Exception as e:
        return {'ran': True, 'passed': False, 'errors': str(e)}

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

    # Skip if this is a test file itself
    if 'test' in file_path.lower() or 'spec' in file_path.lower():
        sys.exit(0)

    # Find related tests
    test_files = find_related_tests(file_path)

    # Detect framework
    framework, cmd = detect_test_framework(cwd)

    if not framework:
        sys.exit(0)

    # Run tests
    result = run_tests(test_files, framework, cmd, cwd)

    # Log results
    log_file = Path.home() / '.claude' / 'test.log'
    log_file.parent.mkdir(parents=True, exist_ok=True)
    with open(log_file, 'a') as f:
        status = "PASS" if result.get('passed') else "FAIL" if result.get('ran') else "SKIP"
        f.write(f"{file_path} | {framework or 'none'} | {status}\n")
        if result.get('errors'):
            f.write(f"  {result['errors'][:200]}\n")

    sys.exit(0)

if __name__ == '__main__':
    main()
```

---

## 5. Import Organizer

Sort and organize imports after file changes.

### Configuration

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Write|Edit",
        "hooks": [
          {
            "type": "command",
            "command": "bash ~/.claude/hooks/import-organizer.sh",
            "timeout": 15
          }
        ]
      }
    ]
  }
}
```

### Script (`~/.claude/hooks/import-organizer.sh`)

```bash
#!/bin/bash
set -euo pipefail

input=$(cat)
file_path=$(echo "$input" | jq -r '.tool_input.file_path // empty')

[[ -z "$file_path" ]] && exit 0
[[ ! -f "$file_path" ]] && exit 0

ext="${file_path##*.}"

case "$ext" in
    py)
        # Python - isort
        if command -v isort &> /dev/null; then
            isort --quiet "$file_path" 2>/dev/null || true
        fi
        # Remove unused imports with autoflake
        if command -v autoflake &> /dev/null; then
            autoflake --in-place --remove-all-unused-imports "$file_path" 2>/dev/null || true
        fi
        ;;

    js|jsx|ts|tsx)
        # JavaScript/TypeScript - organize with eslint or prettier
        if command -v npx &> /dev/null; then
            # Try eslint with import sorting rules
            npx eslint --fix --rule 'sort-imports: off' "$file_path" 2>/dev/null || true
        fi
        ;;

    go)
        # Go - goimports handles this
        if command -v goimports &> /dev/null; then
            goimports -w "$file_path" 2>/dev/null || true
        fi
        ;;

    java)
        # Java - use google-java-format or organize imports
        if command -v google-java-format &> /dev/null; then
            google-java-format --replace "$file_path" 2>/dev/null || true
        fi
        ;;

    rs)
        # Rust - rustfmt handles imports
        if command -v rustfmt &> /dev/null; then
            rustfmt "$file_path" 2>/dev/null || true
        fi
        ;;
esac

exit 0
```

---

## 6. Commit Validator

Enforce commit message format before git commits.

### Configuration

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash(git commit:*)",
        "hooks": [
          {
            "type": "command",
            "command": "python3 ~/.claude/hooks/commit-validator.py",
            "timeout": 5
          }
        ]
      }
    ]
  }
}
```

### Script (`~/.claude/hooks/commit-validator.py`)

```python
#!/usr/bin/env python3
"""
Hook: Commit Validator
Event: PreToolUse (Bash git commit)
Purpose: Enforce commit message conventions
"""

import sys
import json
import re

# Conventional commits pattern
# Format: type(scope): description
# Types: feat, fix, docs, style, refactor, test, chore, perf, ci, build
COMMIT_PATTERN = r'^(feat|fix|docs|style|refactor|test|chore|perf|ci|build)(\([a-z0-9-]+\))?!?: .{3,}'

# Alternative patterns
PATTERNS = {
    'conventional': r'^(feat|fix|docs|style|refactor|test|chore|perf|ci|build)(\([a-z0-9-]+\))?!?: .{3,}',
    'angular': r'^(build|ci|docs|feat|fix|perf|refactor|style|test)(\([a-z0-9-]+\))?: .{3,}',
    'simple': r'^.{10,}',  # At least 10 characters
}

# Use conventional by default
ACTIVE_PATTERN = PATTERNS['conventional']

def extract_commit_message(command: str) -> str:
    """Extract commit message from git commit command."""
    # Pattern: git commit -m "message" or git commit -m 'message'
    patterns = [
        r'-m\s+"([^"]+)"',
        r"-m\s+'([^']+)'",
        r'-m\s+(\S+)',
    ]

    for pattern in patterns:
        match = re.search(pattern, command)
        if match:
            return match.group(1)

    return ""

def validate_message(message: str) -> tuple:
    """Validate commit message format."""
    if not message:
        return False, "Could not extract commit message"

    if len(message) < 10:
        return False, "Commit message too short (min 10 chars)"

    if len(message) > 100:
        return False, "Commit message first line too long (max 100 chars)"

    if not re.match(ACTIVE_PATTERN, message, re.IGNORECASE):
        return False, (
            "Invalid commit format. Use conventional commits:\n"
            "  feat: add new feature\n"
            "  fix: bug fix\n"
            "  docs: documentation\n"
            "  refactor: code refactoring\n"
            "  test: add tests\n"
            "  chore: maintenance"
        )

    return True, ""

def main():
    try:
        data = json.load(sys.stdin)
    except json.JSONDecodeError:
        sys.exit(0)

    tool_input = data.get('tool_input', {})
    command = tool_input.get('command', '')

    # Only check git commit commands with -m flag
    if 'git commit' not in command or '-m' not in command:
        sys.exit(0)

    message = extract_commit_message(command)
    valid, reason = validate_message(message)

    if not valid:
        output = {
            "hookSpecificOutput": {
                "hookEventName": "PreToolUse",
                "permissionDecision": "ask",
                "permissionDecisionReason": f"Commit message issue: {reason}"
            }
        }
        print(json.dumps(output))

    sys.exit(0)

if __name__ == '__main__':
    main()
```

---

## Combined Quality Configuration

Use all quality hooks together:

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash(git commit:*)",
        "hooks": [
          {"type": "command", "command": "python3 ~/.claude/hooks/commit-validator.py", "timeout": 5}
        ]
      }
    ],
    "PostToolUse": [
      {
        "matcher": "Write|Edit",
        "hooks": [
          {"type": "command", "command": "bash ~/.claude/hooks/auto-formatter.sh", "timeout": 30},
          {"type": "command", "command": "bash ~/.claude/hooks/import-organizer.sh", "timeout": 15},
          {"type": "command", "command": "python3 ~/.claude/hooks/linter-runner.py", "timeout": 60},
          {"type": "command", "command": "bash ~/.claude/hooks/type-checker.sh", "timeout": 60},
          {"type": "command", "command": "python3 ~/.claude/hooks/test-runner.py", "timeout": 120}
        ]
      }
    ]
  }
}
```

**Note:** PostToolUse hooks run in parallel by default, but these are ordered by likely execution time (fast first).

---

## Viewing Quality Results

```bash
# View formatting log
tail -f ~/.claude/format.log

# View lint results
cat ~/.claude/lint.log | grep FAIL

# View type check results
cat ~/.claude/typecheck.log | tail -50

# View test results
cat ~/.claude/test.log | grep -E "(PASS|FAIL)"

# Summary of recent activity
for log in ~/.claude/*.log; do
    echo "=== $(basename $log) ==="
    tail -5 "$log"
done
```
