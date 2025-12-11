# Basic Marketplace Template

The simplest marketplace pattern: a single plugin in the same repository.

---

## When to Use

- You have one plugin to share
- Plugin and marketplace live in the same repo
- Simple personal or team distribution
- Getting started with marketplaces

---

## Directory Structure

```
my-marketplace/
├── .claude-plugin/
│   ├── plugin.json         # Plugin manifest
│   └── marketplace.json    # Marketplace catalog
├── commands/               # Your slash commands
│   └── example.md
├── agents/                 # Your agents (optional)
│   └── helper.md
└── README.md              # Documentation
```

---

## Step-by-Step Setup

### Step 1: Create Directory Structure

```bash
mkdir -p my-marketplace/.claude-plugin
mkdir -p my-marketplace/commands
mkdir -p my-marketplace/agents
```

### Step 2: Create plugin.json

Create `my-marketplace/.claude-plugin/plugin.json`:

```json
{
  "name": "my-tools",
  "description": "My personal development tools for Claude Code",
  "version": "1.0.0",
  "author": {
    "name": "Your Name",
    "email": "you@example.com"
  },
  "repository": "https://github.com/yourusername/my-marketplace",
  "license": "MIT"
}
```

### Step 3: Create marketplace.json

Create `my-marketplace/.claude-plugin/marketplace.json`:

```json
{
  "name": "my-marketplace",
  "owner": {
    "name": "Your Name",
    "email": "you@example.com"
  },
  "metadata": {
    "description": "My personal tools collection",
    "version": "1.0.0"
  },
  "plugins": [
    {
      "name": "my-tools",
      "source": ".",
      "description": "My personal development tools for Claude Code",
      "version": "1.0.0",
      "author": {
        "name": "Your Name"
      }
    }
  ]
}
```

**Note**: `"source": "."` means the plugin is in the same directory as marketplace.json's parent.

### Step 4: Add Components

Create a sample command at `my-marketplace/commands/hello.md`:

```markdown
---
description: A simple hello world command
---

Say hello to the user in a friendly way. Include the current date and time.
```

Create a sample agent at `my-marketplace/agents/helper.md`:

```markdown
---
name: helper
description: A helpful assistant for quick questions. Use when the user needs a quick answer.
---

You are a helpful assistant. Answer questions concisely and accurately.

When invoked:
1. Read the user's question carefully
2. Provide a clear, concise answer
3. Offer to elaborate if needed
```

### Step 5: Validate

```bash
cd my-marketplace
claude plugin validate .
```

### Step 6: Test Locally

```bash
# Add the marketplace
/plugin marketplace add ./my-marketplace

# Check it appears
/plugin marketplace list

# Install the plugin
/plugin install my-tools@my-marketplace

# Test the command
/hello
```

### Step 7: Publish (Optional)

```bash
cd my-marketplace
git init
git add .
git commit -m "Initial marketplace setup"
git remote add origin https://github.com/yourusername/my-marketplace.git
git push -u origin main
```

Users can now add your marketplace:
```bash
/plugin marketplace add yourusername/my-marketplace
```

---

## Complete Example: Personal Tools

A working example of a personal tools marketplace:

### Directory Structure

```
personal-tools/
├── .claude-plugin/
│   ├── plugin.json
│   └── marketplace.json
├── commands/
│   ├── quick-review.md
│   └── summarize.md
├── agents/
│   └── explainer.md
└── README.md
```

### plugin.json

```json
{
  "name": "personal-tools",
  "description": "My personal productivity tools: quick code review, summarization, and explanations",
  "version": "1.0.0",
  "author": {
    "name": "Developer"
  },
  "license": "MIT"
}
```

### marketplace.json

```json
{
  "name": "dev-personal",
  "owner": {
    "name": "Developer"
  },
  "plugins": [
    {
      "name": "personal-tools",
      "source": ".",
      "description": "Personal productivity tools: quick code review, summarization, and explanations",
      "version": "1.0.0"
    }
  ]
}
```

### commands/quick-review.md

```markdown
---
description: Quick code review of current changes
allowed-tools: Bash(git diff:*), Read, Grep
---

Review the current uncommitted changes in this repository.

## Steps

1. Run `git diff` to see all changes
2. Analyze each changed file for:
   - Code quality issues
   - Potential bugs
   - Security concerns
   - Style inconsistencies
3. Provide a brief summary with recommendations

## Output Format

### Summary
[One-line overview]

### Issues Found
- [Issue 1]
- [Issue 2]

### Recommendations
- [Recommendation 1]
- [Recommendation 2]
```

### commands/summarize.md

```markdown
---
description: Summarize a file or code block
argument-hint: [file-path]
---

Summarize the contents of the specified file: $ARGUMENTS

Provide:
1. A one-paragraph overview
2. Key components or sections
3. Main functionality
4. Any notable patterns or concerns
```

### agents/explainer.md

```markdown
---
name: explainer
description: Expert at explaining code and concepts. Use when the user asks "explain", "what does this do", or "how does this work".
tools: Read, Grep, Glob
---

You are an expert code explainer.

## When Invoked

1. Identify what needs to be explained
2. Read relevant code or documentation
3. Explain in clear, simple terms
4. Use analogies when helpful
5. Offer to go deeper on specific parts

## Output Format

### Overview
[High-level explanation]

### How It Works
[Step-by-step breakdown]

### Key Concepts
- [Concept 1]: [Explanation]
- [Concept 2]: [Explanation]

### Example
[Concrete example if applicable]
```

---

## Tips for Basic Marketplaces

### Keep It Simple
- Start with 1-3 commands or agents
- Add more as you identify needs
- Don't over-engineer initially

### Good Naming
- Marketplace name: Your username or project name
- Plugin name: Descriptive of contents
- Command names: Action-oriented (verb-noun)

### Version Management
- Start at 1.0.0
- Increment PATCH for fixes (1.0.1)
- Increment MINOR for new features (1.1.0)
- Increment MAJOR for breaking changes (2.0.0)

### Documentation
Include a README.md explaining:
- What the marketplace provides
- How to install
- List of available commands/agents
- Usage examples

---

## Upgrading to Multi-Plugin

When your marketplace grows, consider splitting into multiple plugins:

1. Create `plugins/` directory
2. Move components into separate plugin directories
3. Update marketplace.json with multiple plugin entries
4. See `templates/multi-plugin.md` for the pattern
