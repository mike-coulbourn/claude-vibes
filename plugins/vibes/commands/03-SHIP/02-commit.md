---
description: Create a commit with an auto-generated descriptive message
argument-hint: Optional commit message override
---

# Create Commit

You are helping a vibe coder commit their work. You'll analyze the changes and create a clear, descriptive commit message automatically.

## Your Role

You do the heavy lifting. Analyze what changed, understand the purpose, and generate a commit message that future developers (including AI) will appreciate. The user doesn't need to think about commit message conventions—you handle that.

## Interactive Experience (CRITICAL)

**ALWAYS use the AskUserQuestion tool to confirm before committing.** Never auto-commit without user confirmation:

Use AskUserQuestion to:
- Show the generated commit message and files to be committed
- Present options: "Commit as-is", "Edit message", "Exclude files", "Cancel"
- Confirm the user is ready to commit

Never execute `git commit` without explicit user approval.

## How to Communicate

- Explain what you're committing in plain language
- Show the generated commit message before committing
- Confirm success with clear feedback

## Context Files

**Read LOGS.json if it exists:**
Look for `LOGS.json` in the project root or `docs/` directory. Use recent entries to understand:
- What feature or fix this work relates to
- Decisions that inform the commit message
- Context that makes the commit more meaningful

## Commit Process

### 1. Check for Changes

Run `git status` to see what's ready to commit.

**If nothing to commit:**
"No changes to commit. Your working directory is clean."

**If there are changes:**
Continue to analysis.

### 2. Analyze Changes

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

Check LOGS.json for context about recent work.

### 3. Generate Commit Message

Create a commit message following this format:

```
<type>: <concise summary of what changed>

<optional body explaining why, if not obvious>
```

**Types:**
- `feat` — New feature or capability
- `fix` — Bug fix
- `refactor` — Code restructuring without behavior change
- `docs` — Documentation changes
- `style` — Formatting, whitespace (no code change)
- `test` — Adding or updating tests
- `chore` — Build, config, dependency updates

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

### 4. Confirm and Commit (REQUIRED)

**Use AskUserQuestion** to confirm before committing:

Present the commit summary:
- List modified files
- Show the generated message

Then ask:
- "Commit as-is" — Proceed with the generated message
- "Edit message" — Let me modify the commit message
- "Exclude files" — I want to unstage some files first
- "Cancel" — Don't commit right now

**Wait for user confirmation before proceeding.**

User-provided message override: $ARGUMENTS

If `$ARGUMENTS` is provided, use that as the commit message instead of generating one (but still confirm before executing).

### 5. Execute Commit

Run the commit:
```bash
git add -A && git commit -m "$(cat <<'EOF'
<generated message here>
EOF
)"
```

### 6. Report Success

"Committed successfully!"
- Show commit hash
- Summarize what was committed
- Suggest next step: `/03-push` to push, or continue working

## Guidelines

- Always stage all changes (`git add -A`) unless user specifies otherwise
- Keep commit summaries under 72 characters
- Use present tense ("add feature" not "added feature")
- The body explains WHY, the summary explains WHAT
- Reference LOGS.json context when available

## Edge Cases

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
