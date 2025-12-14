# Slash Command Troubleshooting Guide

Solutions to common issues when creating and using slash commands.

## Command Not Appearing in /help

### Symptom
Your command doesn't appear when you run `/help`.

### Possible Causes and Solutions

#### 1. File Not in Correct Location

**Check**:
```bash
# For project commands
ls .claude/commands/your-command.md

# For personal commands
ls ~/.claude/commands/your-command.md
```

**Fix**: Move file to correct location.

#### 2. Missing .md Extension

**Check**:
```bash
ls -la .claude/commands/ | grep your-command
```

**Fix**: Rename file to include `.md`:
```bash
mv .claude/commands/your-command .claude/commands/your-command.md
```

#### 3. Invalid Filename Characters

**Check**: Filename should be lowercase-with-hyphens

**Fix**:
```bash
# Bad:
My Command.md
my_command.md

# Good:
my-command.md
```

#### 4. Directory Doesn't Exist

**Check**:
```bash
ls -la .claude/
```

**Fix**: Create directory:
```bash
mkdir -p .claude/commands
```

#### 5. Need to Restart Claude Code

Commands are loaded at startup. After creating new commands, restart your Claude Code session.

---

## Arguments Not Replacing

### Symptom
Placeholders like `$ARGUMENTS` or `$1` appear literally in Claude's response instead of being replaced with values.

### Possible Causes and Solutions

#### 1. Typo in Placeholder

**Check your command file**:
```markdown
❌ $ARGUMENT (missing S)
❌ $ARG1 (not recognized)
❌ ${1} (bash syntax, wrong)

✅ $ARGUMENTS
✅ $1, $2, $3
```

**Fix**: Use exact syntax: `$ARGUMENTS` or `$1`, `$2`, etc.

#### 2. Not Passing Arguments When Invoking

**Check**:
```bash
❌ /your-command
   (no arguments provided)

✅ /your-command arg1 arg2
   (arguments provided)
```

**Fix**: Provide arguments when calling command.

#### 3. Arguments Not Defined in Command

**Check command file**:
```markdown
# If you reference $1, make sure you added argument-hint
---
argument-hint: [expected-arg]
---
```

**Test**: Create simple test command:
```markdown
---
description: Test arguments
---

You provided: $ARGUMENTS
First: $1
Second: $2
```

Invoke: `/test-args hello world`

Should show:
```
You provided: hello world
First: hello
Second: world
```

---

## Bash Commands Not Executing

### Symptom
Bash commands appear literally instead of their output, or command doesn't run.

### Possible Causes and Solutions

#### 1. Missing allowed-tools in Frontmatter

**Check command file**:
```markdown
❌ No frontmatter

✅
---
allowed-tools: Bash(git:*)
---
```

**Fix**: Add frontmatter with `allowed-tools: Bash(...)`.

#### 2. Wrong Syntax

**Check command file**:
```markdown
❌ !git status (missing backticks)
❌ `git status` (missing !)
❌ !\`git status (unclosed backtick)

✅ !\`git status\` (correct)
```

**Fix**: Use exact syntax: !\`command\`

#### 3. Command Fails When Run

**Test command in terminal**:
```bash
# Try running it yourself
git status

# If it fails in terminal, it fails in command
```

**Fix**: Ensure command works in terminal first.

#### 4. Tool Restriction Too Narrow

**Check**:
```yaml
allowed-tools: Bash(git status:*)
```

But trying to run:
```markdown
!\`git log\`  # Won't work, not in allowed-tools
```

**Fix**: Broaden tool restriction:
```yaml
allowed-tools: Bash(git:*)
```

#### 5. Command Requires Interactive Input

**Commands that won't work**:
```markdown
❌ !\`git rebase -i\` (interactive)
❌ !\`npm install\` (prompts sometimes)
```

**Fix**: Use non-interactive commands only.

---

## File References Not Working

### Symptom
File contents don't appear, or error about file not found.

### Possible Causes and Solutions

#### 1. Missing @ Prefix

**Check command file**:
```markdown
❌ Review src/auth.js
✅ Review @src/auth.js
```

**Fix**: Add `@` prefix before path.

#### 2. File Doesn't Exist

**Check**:
```bash
# Verify file exists
ls src/auth.js
cat src/auth.js
```

**Fix**: Correct the path or create the file.

#### 3. Wrong Path

**Check**: Paths are relative to current working directory

```markdown
# If working directory is /Users/you/project:
@src/auth.js                     # Correct
@./src/auth.js                   # Also correct
@/Users/you/project/src/auth.js  # Absolute, correct

@/src/auth.js                    # Wrong (absolute from root)
```

**Fix**: Use correct relative or absolute path.

#### 4. Trying to Read Directory Contents

**Check**:
```markdown
@src/  # Shows directory listing, not file contents
```

**Fix**: Reference specific files, not directories.

---

## YAML Frontmatter Errors

### Symptom
Command doesn't load, or weird behavior with frontmatter.

### Possible Causes and Solutions

#### 1. Missing Opening or Closing Delimiter

**Check**:
```markdown
❌
description: Test command
---

❌
---
description: Test command

✅
---
description: Test command
---
```

**Fix**: Both `---` delimiters required (opening and closing).

#### 2. Using Tabs Instead of Spaces

YAML requires spaces for indentation.

**Check** (in editor that shows tabs):
```yaml
❌
---
description:	Test  # Tab character
---

✅
---
description: Test  # Spaces
---
```

**Fix**: Use spaces, not tabs.

#### 3. Unquoted Strings with Special Characters

**Check**:
```yaml
❌
description: Review code: security & performance

✅
description: "Review code: security & performance"
```

**Fix**: Quote strings with special characters.

#### 4. Incorrect Field Names

**Check**:
```yaml
❌
desc: Test command  # Wrong field name

✅
description: Test command
```

**Fix**: Use correct field names (see syntax-guide.md).

---

## Command Conflicts

### Symptom
Wrong command runs, or command doesn't run at all.

### Possible Causes and Solutions

#### 1. Project Command Overrides User Command

**Precedence**:
1. Project (`.claude/commands/`)
2. User (`~/.claude/commands/`)
3. Plugin

**Check**:
```bash
# Both exist?
ls .claude/commands/review.md
ls ~/.claude/commands/review.md
```

**Fix**: Project command takes precedence. Rename one if you want both.

#### 2. Namespace Collision with Plugin

**Check**:
```
/review  # Could be your command or plugin command
```

**Fix**: Use explicit namespace:
```
/your-plugin:review  # Plugin version
/review              # Your version
```

Or rename your command to avoid collision.

---

## Extended Thinking Not Triggering

### Symptom
Command doesn't trigger extended thinking when expected.

### Solution

Include thinking keywords:

```markdown
Think deeply about $ARGUMENTS...
Think hard about the implications...

# Or:
think, think hard, think deeply, think long
```

---

## Command Too Slow

### Symptom
Command takes a long time to run.

### Possible Causes and Solutions

#### 1. Slow Bash Commands

**Check**:
```markdown
!\`npm install\`  # Takes minutes
!\`git log --all\`  # Huge output
```

**Fix**: Use faster commands or limit output:
```markdown
!\`git log --oneline -10\`  # Limited
!\`npm list --depth=0\`     # Shallow
```

#### 2. Too Many File References

**Check**:
```markdown
@src/*.js  # Might be 100+ files
```

**Fix**: Reference specific files:
```markdown
@src/file1.js
@src/file2.js
```

#### 3. Large Command Output

**Check**: Is command output huge?

**Fix**: Limit output size:
```markdown
!\`command | head -50\`
!\`command --limit 20\`
```

---

## Command Not Being Auto-Invoked by Claude

### Symptom
SlashCommand tool not calling your command.

### Possible Causes and Solutions

#### 1. Missing description Field

**Check command file**:
```yaml
❌
---
# No description
---

✅
---
description: Review code for quality
---
```

**Fix**: Add `description` field.

#### 2. Command Disabled for Auto-Invocation

**Check**:
```yaml
disable-model-invocation: true  # Prevents auto-calling
```

**Fix**: Remove this field or set to `false`.

#### 3. Over Character Budget

Commands over 15,000 characters won't be auto-invoked.

**Fix**: Shorten command or increase budget via env var:
```bash
export SLASH_COMMAND_TOOL_CHAR_BUDGET=30000
```

#### 4. Claude Doesn't Know to Use It

**Fix**: Reference in prompt or CLAUDE.md:
```markdown
When reviewing code, run /security-audit on sensitive files.
```

---

## Debugging Workflow

### Step 1: Simplify

Create minimal test command:

```markdown
---
description: Test command
---

This is a test. Hello!
```

Test: `/test-command`

If this works, add features one at a time.

### Step 2: Test Each Feature

```markdown
# Test 1: Arguments
You said: $ARGUMENTS

# Test 2: Bash
Branch: !\`git branch --show-current\`

# Test 3: Files
File: @README.md
```

Identify which feature fails.

### Step 3: Check Syntax

- YAML delimiters: `---` at start and end?
- Argument syntax: `$ARGUMENTS` or `$1` (not `$ARG`)?
- Bash syntax: !\`command\` (with backticks)?
- File syntax: `@path` (with @ prefix)?

### Step 4: Verify Paths and Permissions

```bash
# File exists?
ls path/to/file

# Directory exists?
ls -la .claude/commands/

# Permissions OK?
ls -la .claude/commands/your-command.md
```

### Step 5: Test with Simple Inputs

```bash
/command "simple test"
```

Don't use complex inputs until basic functionality works.

---

## Getting Help

If stuck:

1. **Check syntax-guide.md**: Verify you're using correct syntax
2. **Check best-practices.md**: See recommended patterns
3. **Look at examples**: Copy working examples and modify
4. **Test incrementally**: Start simple, add one feature at a time
5. **Verify files**: Ensure correct location, syntax, permissions

---

Most issues come from:
- Missing `allowed-tools` for bash
- Typos in syntax ($ARGUMENTS vs $ARGUMENT)
- Wrong file location or missing .md extension
- YAML syntax errors

Check these first!
