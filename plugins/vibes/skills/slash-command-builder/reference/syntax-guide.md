# Slash Command Syntax Guide

Complete reference for all slash command features and syntax.

## Contents

- [File Structure](#file-structure)
- [YAML Frontmatter Reference](#yaml-frontmatter-reference)
- [Arguments](#arguments)
- [Bash Execution](#bash-execution)
- [File References](#file-references)
- [Path Resolution](#path-resolution)
- [Combining Features](#combining-features)
- [Command Invocation](#command-invocation)
- [Command Precedence](#command-precedence)
- [Special Characters and Escaping](#special-characters-and-escaping)
- [Extended Thinking](#extended-thinking)
- [File Naming](#file-naming)
- [Subdirectory Organization](#subdirectory-organization)
- [Command Scope](#command-scope)
- [SlashCommand Tool Integration](#slashcommand-tool-integration)
- [Complete Syntax Example](#complete-syntax-example)

## File Structure

```markdown
---
[YAML frontmatter - optional]
---

[Markdown content - your prompt]
```

## YAML Frontmatter Reference

All fields are optional unless noted:

```yaml
---
description: Brief description for /help and SlashCommand tool
allowed-tools: Tool, OtherTool, Bash(command:*)
argument-hint: [expected] [arguments]
model: claude-3-5-haiku-20241022
disable-model-invocation: false
---
```

### Field Descriptions

| Field | Description | Default |
|-------|-------------|---------|
| `description` | What the command does and when to use it. Shown in the `/` menu and used by Claude to decide when to invoke it | First non-empty line of content |
| `argument-hint` | Autocomplete hint for expected arguments, such as `[issue-number]` | None |
| `arguments` | Named positional arguments for `$name` substitution. Space-separated string or YAML list; names map to positions in order | None |
| `allowed-tools` | Tools Claude may use **without asking permission** during the turn that invokes the command. This pre-approves tools; it does not restrict the others. The grant clears on the user's next message | No pre-approval |
| `disallowed-tools` | Tools removed from Claude's pool while the command is active. This is the field that restricts | None |
| `model` | Model for the rest of the current turn: `fable`, `opus`, `sonnet`, `haiku`, or a full model ID | Session model |
| `effort` | Effort level while active: `low`, `medium`, `high`, `xhigh`, `max` | Session effort |
| `disable-model-invocation` | `true` means only the user can run it with `/name`; Claude never loads it on its own. Use for anything with side effects, such as deploy or commit | `false` |
| `user-invocable` | `false` hides it from the `/` menu so only Claude invokes it | `true` |
| `context` | `fork` runs the command in a forked subagent; pair with `agent` to choose the subagent type | Runs inline |
| `shell` | Shell for bash injection: `bash` or `powershell` | `bash` |

Command files accept every skill frontmatter field except `name` and `paths`. Source: https://code.claude.com/docs/en/skills#frontmatter-reference (last verified September 2026).

## Arguments

### All Arguments: `$ARGUMENTS`

Captures everything after the command name as a single string.

```markdown
Explain $ARGUMENTS in detail.
```

```bash
/explain async/await in JavaScript
# $ARGUMENTS = "async/await in JavaScript"
```

### Positional Arguments: `$0`, `$1`, `$2`...

Captures specific argument positions (space-separated).

```markdown
Review PR #$0 with priority $1 assigned to $2.
```

```bash
/review-pr 456 high alice
# $0 = "456"
# $1 = "high"
# $2 = "alice"
```

### Quoting Arguments

Use quotes for arguments with spaces:

```bash
/command "argument with spaces" second-arg
# $0 = "argument with spaces"
# $1 = "second-arg"
```

## Bash Execution

Execute bash commands BEFORE the prompt runs.

### Syntax

```markdown
[execute: command here]
```

### Requirements

1. Must include `allowed-tools` with Bash:
```yaml
allowed-tools: Bash(git:*)
```

2. Must use the real injection syntax: an exclamation mark immediately followed by the command in single backticks. `[execute: command]` in this guide is a placeholder for it, because the real form would execute when this file loads

3. Command output replaces the `[execute: command]` in the prompt

### Examples

```markdown
---
allowed-tools: Bash(git:*)
---

Branch: [execute: git branch --show-current]
Status: [execute: git status --short]
```

Becomes:

```markdown
Branch: main
Status:
 M src/file.js
```

### Tool Restrictions

Limit bash access to specific commands:

```yaml
# Git operations only
allowed-tools: Bash(git:*)

# Multiple specific tools
allowed-tools: Bash(git:*), Bash(npm:*)

# Specific commands
allowed-tools: Bash(git status:*), Bash(git log:*)

# All bash (use carefully!)
allowed-tools: Bash
```

### Capturing stderr

Include stderr in output:

```markdown
[execute: command 2>&1]
```

## File References

Include file contents with the `@` prefix.

### Syntax

```markdown
@path/to/file
```

### Features

1. File contents are included in prompt
2. CLAUDE.md files from directory hierarchy auto-included
3. Relative or absolute paths supported
4. Multiple file references allowed

### Examples

```markdown
# Single file
Review @src/auth.js

# Multiple files
Compare @src/old.js with @src/new.js

# With arguments
Analyze @$0 for security issues

# Directory (shows listing, not contents)
Structure: @src/components/
```

### Automatic CLAUDE.md Inclusion

When you reference `@src/auth/login.js`, Claude also receives:
- `src/auth/CLAUDE.md` (if exists)
- `src/CLAUDE.md` (if exists)
- Root `CLAUDE.md` (if exists)

This ensures project conventions are always available.

## Path Resolution

Paths are relative to current working directory:

```markdown
@src/file.js              # Relative
@./src/file.js            # Relative (explicit)
@/absolute/path/file.js   # Absolute
```

## Combining Features

You can combine arguments, bash, and file references:

```markdown
---
description: Analyze file with git context
allowed-tools: Bash(git:*), Read
argument-hint: [file-path]
---

## File
@$0

## Recent Changes
[execute: git log --oneline -5 -- $0]

## Analysis
Analyze @$0 considering its history above.
```

## Command Invocation

### Basic Syntax

```
/command-name
/command-name arg1 arg2
/command-name "arg with spaces" arg2
```

### Namespaced Commands

Plugin and MCP commands use namespaces:

```
/plugin:category:command-name
/mcp__server__prompt-name
```

### Help

List all commands:

```
/help
```

## Command Precedence

When same command name exists in multiple places:

1. **Project commands** (`.claude/commands/`) - highest
2. **User commands** (`~/.claude/commands/`) - ignored if project exists
3. **Plugin commands** - can namespace to avoid conflicts

## Special Characters and Escaping

### In Prompts

No escaping needed in markdown content:

```markdown
Use $, @, and ! symbols freely here.
Only $ARGUMENTS, $0, [execute: cmd], @file have special meaning.
```

### In YAML Frontmatter

Quote strings with special characters:

```yaml
description: "Analyze code for @mentions and $variables"
argument-hint: "[file] [options]"
```

## Extended Thinking

Trigger extended thinking with keywords:

```markdown
Think deeply about $ARGUMENTS and analyze thoroughly.
```

Keywords that trigger thinking:
- "think"
- "think hard"
- "think deeply"
- "think long"

## File Naming

```
command-name.md → /command-name
optimize-code.md → /optimize-code
my-workflow.md → /my-workflow
```

Rules:
- Lowercase with hyphens recommended
- No spaces in filename
- `.md` extension required
- Filename becomes command name

## Subdirectory Organization

```
.claude/commands/
├── frontend/
│   └── component.md  → /component (project:frontend)
└── backend/
    └── api.md        → /api (project:backend)
```

Subdirectory appears in `/help` for context but doesn't change command name.

## Command Scope

### Project Commands

Location: `.claude/commands/`
- Shared with team via git
- Team-wide standardization
- Higher precedence than user commands

### Personal Commands

Location: `~/.claude/commands/`
- Individual use only
- Not in version control
- Personal productivity shortcuts

## SlashCommand Tool Integration

The `SlashCommand` tool allows Claude to execute your commands programmatically.

### Requirements

1. Command must have `description` in frontmatter
2. Command must not have `disable-model-invocation: true`
3. Must be under character budget (default 15,000)

### Enabling Auto-Invocation

Reference commands in prompts or CLAUDE.md:

```markdown
When reviewing code, run /security-audit on sensitive files.
```

### Disabling Auto-Invocation

```yaml
---
disable-model-invocation: true
---
```

## Complete Syntax Example

```markdown
---
description: Comprehensive example command
allowed-tools: Bash(git:*), Read, Grep, Glob
argument-hint: [file] [focus-area]
model: claude-3-5-haiku-20241022
---

## Context

**File to analyze**: $0
**Focus**: $1

**Git context**:
Branch: [execute: git branch --show-current]
Recent changes: [execute: git log --oneline -5 -- $0]

## Source Code

@$0

## Related Files

@tests/$0.test.js

## Project Conventions

@CLAUDE.md

## Task

Analyze @$0 focusing on $1:
1. Current implementation
2. Issues found
3. Recommended improvements
4. Example fixes

Consider the git history and project conventions above.
```

Usage:
```
/comprehensive src/auth.js security
```

---

This syntax guide covers all features. See best-practices.md for when and how to use them effectively.
