# Basic Slash Command Template

The simplest possible slash command - just a prompt.

## When to Use This Template

- Fixed prompt that doesn't need dynamic inputs
- Simple, focused operation
- No bash execution or file references needed
- Getting started with slash commands

## Template

```markdown
---
description: [Brief description of what this command does]
---

[Your prompt here - this is what Claude receives when you invoke the command]
```

## Example: Simple Code Review

**File**: `.claude/commands/review.md`

```markdown
---
description: Review code for quality and best practices
---

Review this code focusing on:

1. **Security**: Input validation, injection risks, auth issues
2. **Performance**: Inefficient operations, unnecessary computations
3. **Maintainability**: Code clarity, naming, structure
4. **Best Practices**: Following language idioms and conventions

Provide specific, actionable feedback with code examples where relevant.
```

**Usage**:
```
> /review
```

Then paste or reference the code you want reviewed.

## Example: Explain Concept

**File**: `~/.claude/commands/explain.md`

```markdown
---
description: Explain a concept or term in detail
---

Explain the concept or term I provide in detail, including:

1. **What it is**: Clear definition
2. **How it works**: Mechanism or process
3. **When to use it**: Appropriate scenarios
4. **Common pitfalls**: What to watch out for
5. **Best practices**: How to use it effectively

Use examples and analogies to make it clear. Assume I'm learning this for the first time.
```

**Usage**:
```
> /explain
```

Then specify what you want explained.

## Example: Optimize Code

**File**: `.claude/commands/optimize.md`

```markdown
---
description: Analyze code for performance improvements
---

Analyze the provided code for performance issues and suggest three specific optimizations.

For each optimization:
- Explain the current issue
- Show the improved code
- Explain why it's better
- Estimate the performance impact

Focus on practical, measurable improvements.
```

**Usage**:
```
> /optimize
```

Then provide the code to optimize.

## Customization Tips

1. **Be specific in your prompt**: Vague prompts lead to vague responses
2. **Structure with sections**: Use numbered lists or headings
3. **Include criteria**: Tell Claude what to focus on
4. **Add constraints**: Specify format, length, or style requirements
5. **Use description field**: Helps others understand the command

## Limitations of Basic Commands

- No dynamic inputs (every invocation is identical)
- Can't gather system context (git status, etc.)
- Can't reference files automatically
- User must provide all context manually

**When you need these features**, see:
- [with-arguments.md](with-arguments.md) - For dynamic inputs
- [with-bash.md](with-bash.md) - For system context
- [with-files.md](with-files.md) - For file references
- [complex-command.md](complex-command.md) - For all features

## Testing Your Basic Command

1. Create the file in the correct location
2. Run `/help` to verify it appears
3. Test with `/your-command`
4. Iterate on the prompt based on results
5. Share with team if it's valuable

Start with basic commands and add complexity only when needed!
