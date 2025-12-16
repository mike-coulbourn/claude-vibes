# Slash Command Syntax Guide

Complete reference for all slash command features and syntax.

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

| Field | Type | Description | Default |
|-------|------|-------------|---------|
| `description` | string | Shown in `/help`, required for SlashCommand tool | First line of content |
| `allowed-tools` | list | Restricts which tools can be used | All tools |
| `argument-hint` | string | Shows expected arguments to user | None |
| `model` | string | Specific model for this command | Inherits from conversation |
| `disable-model-invocation` | boolean | Prevents SlashCommand tool from calling this | `false` |

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

### Positional Arguments: `$1`, `$2`, `$3`...

Captures specific argument positions (space-separated).

```markdown
Review PR #$1 with priority $2 assigned to $3.
```

```bash
/review-pr 456 high alice
# $1 = "456"
# $2 = "high"
# $3 = "alice"
```

### Quoting Arguments

Use quotes for arguments with spaces:

```bash
/command "argument with spaces" second-arg
# $1 = "argument with spaces"
# $2 = "second-arg"
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

2. Must use `[execute: command]` syntax

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
Analyze @$1 for security issues

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
@$1

## Recent Changes
[execute: git log --oneline -5 -- $1]

## Analysis
Analyze @$1 considering its history above.
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
Only $ARGUMENTS, $1, [execute: cmd], @file have special meaning.
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

**File to analyze**: $1
**Focus**: $2

**Git context**:
Branch: [execute: git branch --show-current]
Recent changes: [execute: git log --oneline -5 -- $1]

## Source Code

@$1

## Related Files

@tests/$1.test.js

## Project Conventions

@CLAUDE.md

## Task

Analyze @$1 focusing on $2:
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
