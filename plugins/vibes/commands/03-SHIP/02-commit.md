---
description: Create a commit with an auto-generated descriptive message
argument-hint: Optional commit message override
---

# Create commit

You are helping a vibe coder commit their work. You'll analyze the changes and create a clear, descriptive commit message automatically.

## Your role

**Use the AskUserQuestion tool for every question to the user. Never ask questions as plain text output.** The AskUserQuestion tool gives a guided, interactive experience with structured options. Every user question must go through this tool.

You do the heavy lifting. Analyze what changed, understand the purpose, and generate a commit message that future developers (including AI) will appreciate. The user doesn't need to think about commit message conventions, so you handle that.

## Interactive experience (critical)

**Use the AskUserQuestion tool to confirm before committing.** Never auto-commit without user confirmation:

Use AskUserQuestion to:
- Show the generated commit message and files to be committed
- Present options: "Commit as-is", "Edit message", "Exclude files", "Cancel"
- Confirm the user is ready to commit

Never execute `git commit` without explicit user approval.

## How to communicate

- Explain what you're committing in plain language
- Show the generated commit message before committing
- Confirm success with clear feedback

## Context files (conditional)

**Only check LOGS.json if it has uncommitted changes.**

First, run:
```bash
git status --porcelain -- LOGS.json docs/LOGS.json 2>/dev/null
```

**If output is non-empty** (LOGS.json has uncommitted changes), read it and use recent entries to understand:
- What feature or fix this work relates to
- Decisions that inform the commit message
- Context that makes the commit more meaningful

**If output is empty**, skip reading LOGS.json, because any context it contains is from a previous session and isn't relevant to the current changes.

## Commit process

### 1. Check for changes

Run `git status` to see what's ready to commit.

**If nothing to commit:**
"No changes to commit. Your working directory is clean."

**If there are changes:**
Continue to analysis.

### 2. Analyze changes

Run `git diff --staged` to see staged changes, or `git diff` for unstaged.

**Safety check for sensitive files:**
Before staging, check for files that shouldn't be committed:
- `.env`, `.env.local`, `.env.production`
- `credentials.json`, `secrets.json`
- Private keys (`*.pem`, `*.key`)
- `node_modules/`, `__pycache__/`

If found, warn the user and exclude them (or verify .gitignore handles them).

Understand:
- What files were modified?
- What's the nature of the change? (new feature, bug fix, refactor, config, docs)
- What's the user-facing impact?

Check LOGS.json for context (only if it has uncommitted changes per the check above).

### 3. Generate commit message

Create a commit message following this format:

```
<type>: <concise summary of what changed>

<optional body explaining why, if not obvious>
```

**Types:**
- `feat`: New feature or capability
- `fix`: Bug fix
- `refactor`: Code restructuring without behavior change
- `docs`: Documentation changes
- `style`: Formatting, whitespace (no code change)
- `test`: Adding or updating tests
- `chore`: Build, config, dependency updates

**Examples:**
```
feat: add user authentication with email/password

Implements NextAuth with credentials provider. Users can now
sign up and log in with their email address.
```

```
fix: prevent duplicate form submissions

Added loading state to submit button to prevent users from
accidentally submitting the form multiple times.
```

### 4. Confirm and commit (required)

**Use AskUserQuestion** to confirm before committing:

Present the commit summary:
- List modified files
- Show the generated message

Then ask:
- "Commit as-is": proceed with the generated message
- "Edit message": let me modify the commit message
- "Exclude files": I want to unstage some files first
- "Cancel": don't commit right now

**Wait for user confirmation before proceeding.**

User-provided message override: $ARGUMENTS

If `$ARGUMENTS` is provided, use that as the commit message instead of generating one (but still confirm before executing).

### 5. Execute commit

Run the commit:
```bash
git add -A && git commit -m "$(cat <<'EOF'
<generated message here>
EOF
)"
```

### 6. Report success

"Committed successfully!"
- Show commit hash
- Summarize what was committed
- Suggest next step: `/03-push` to push, or continue working

## Guidelines

- Always stage all changes (`git add -A`) unless user specifies otherwise
- Keep commit summaries under 72 characters
- Use present tense ("add feature" not "added feature")
- The body explains why, the summary explains what
- Reference LOGS.json context when it has uncommitted changes

## Edge cases

**Large number of changes:**
If many files changed, group them logically in the body:
```
refactor: reorganize authentication module

- Moved auth utilities to src/lib/auth/
- Split session handling into separate module
- Updated imports across 12 files
```

**Mixed changes (not recommended but happens):**
If changes span multiple purposes, note it:
```
feat: add user profiles, fix login redirect

Primary: Added user profile pages with avatar upload.
Also fixed: Login now redirects to intended destination.
```
