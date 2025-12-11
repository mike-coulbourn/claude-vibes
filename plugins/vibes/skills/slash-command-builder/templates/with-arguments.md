# Slash Command with Arguments Template

Add dynamic inputs to your commands using arguments.

## When to Use This Template

- Command needs user-provided values
- Different invocations need different inputs
- Building flexible, reusable commands
- Want structured parameters

## Two Argument Styles

### Style 1: All Arguments ($ARGUMENTS)

Captures everything after the command as a single string.

```markdown
---
description: [Brief description]
argument-hint: [what-user-should-provide]
---

[Your prompt with $ARGUMENTS placeholder]
```

**Use when**:
- All input is treated as one block
- Free-form text (messages, descriptions, queries)
- Don't need to separate into parts

**Example**:
```markdown
---
description: Explain a concept in detail
argument-hint: [concept-to-explain]
---

Explain $ARGUMENTS in detail, including what it is, how it works, when to use it, and common pitfalls.
```

Usage: `/explain async/await in JavaScript`

### Style 2: Positional Arguments ($1, $2, $3...)

Captures specific argument positions separately (like shell scripts).

```markdown
---
description: [Brief description]
argument-hint: [arg1] [arg2] [arg3]
---

[Your prompt with $1, $2, $3 placeholders]
```

**Use when**:
- Need structured, specific parameters
- Different arguments used in different places
- Want to reference parts separately
- Can provide defaults for missing arguments

**Example**:
```markdown
---
description: Review pull request
argument-hint: [pr-number] [priority] [reviewer]
---

Review PR #$1 with priority level $2 and assign to $3.

Focus on:
- Code quality and style
- Security concerns
- Performance implications
- Test coverage

Provide specific, actionable feedback.
```

Usage: `/review-pr 456 high alice`

## Complete Examples

### Example 1: Issue Fixer with $ARGUMENTS

**File**: `.claude/commands/fix-issue.md`

```markdown
---
description: Fix a GitHub issue by number
argument-hint: [issue-number]
---

Fix issue #$ARGUMENTS following our team standards:

1. Understand the issue thoroughly
2. Locate all relevant code
3. Implement a robust solution
4. Add tests to prevent regression
5. Prepare clear PR description

Reference our coding standards in @CLAUDE.md
```

**Usage**:
```
/fix-issue 123
```

### Example 2: Database Query with Positional Args

**File**: `.claude/commands/query-db.md`

```markdown
---
description: Generate database query
argument-hint: [table] [operation] [conditions]
---

Generate a SQL query for:
- Table: $1
- Operation: $2 (SELECT, INSERT, UPDATE, DELETE)
- Conditions: $3

Include:
- Proper indexing considerations
- SQL injection prevention
- Error handling
- Example usage

Follow our database conventions in @docs/database-style.md
```

**Usage**:
```
/query-db users SELECT "active=true AND role='admin'"
```

### Example 3: Test Generator with Multiple Args

**File**: `.claude/commands/gen-test.md`

```markdown
---
description: Generate tests for a function
argument-hint: [file] [function-name] [test-type]
---

Generate $3 tests for function `$2` in @$1

Test categories:
- Happy path scenarios
- Edge cases
- Error conditions
- Integration points (if applicable)

Follow our testing patterns in @tests/ directory.

Test framework: Based on project setup
Coverage target: 100% of function branches
```

**Usage**:
```
/gen-test src/auth/login.js validateCredentials unit
```

### Example 4: Refactor Planner

**File**: `.claude/commands/refactor.md`

```markdown
---
description: Plan refactoring approach
argument-hint: [file-or-directory] [goal]
---

Plan a refactoring approach for @$1 with goal: $2

Analysis:
1. Current structure and issues
2. Proposed improvements
3. Step-by-step refactoring plan
4. Risks and mitigation strategies
5. Testing strategy

Ensure backward compatibility and follow our refactoring guidelines.
```

**Usage**:
```
/refactor src/legacy/payment.js "improve error handling"
```

## Combining Both Styles

You can use positional args for structure and $ARGUMENTS for free-form:

```markdown
---
description: Create feature with context
argument-hint: [feature-name] [additional-context]
---

Create a new feature: $1

Additional context: $ARGUMENTS

Plan:
1. Design approach for $1
2. Identify affected files
3. List implementation steps
4. Note testing requirements

Consider: $ARGUMENTS
```

Usage: `/create-feature user-auth need to support OAuth and JWT`
- $1 = "user-auth"
- $ARGUMENTS = "user-auth need to support OAuth and JWT"

## Handling Missing Arguments

If user doesn't provide all arguments, Claude receives empty strings:

```markdown
Review PR #$1 (priority: ${2:-medium}) assigned to ${3:-unassigned}
```

**Note**: Default syntax `${2:-medium}` is not directly supported. Instead, handle in your prompt:

```markdown
Review PR #$1 with priority $2 and assignee $3.

If priority is not specified, assume medium.
If assignee is not specified, suggest reviewer based on PR content.
```

## Best Practices for Arguments

1. **Always include argument-hint**
   - Shows users what to provide
   - Self-documenting command
   - Reduces confusion

2. **Use descriptive placeholders**
   ```
   argument-hint: [feature-name] [priority] [assignee]
   ```
   Not:
   ```
   argument-hint: [arg1] [arg2] [arg3]
   ```

3. **Document in prompt**
   ```markdown
   Generate tests for:
   - File: $1 (path to source file)
   - Type: $2 (unit, integration, or e2e)
   ```

4. **Choose the right style**
   - Structured data → Positional ($1, $2)
   - Free-form text → $ARGUMENTS

5. **Test with various inputs**
   - Missing arguments
   - Extra arguments
   - Special characters
   - Empty strings

## Common Pitfalls

### Typo in placeholder
```markdown
❌ $ARGUMENT (missing S)
❌ $ARG1 (should be $1)
✅ $ARGUMENTS
✅ $1, $2, $3
```

### Wrong syntax
```markdown
❌ ${1} (bash style, doesn't work)
❌ $arg1 (not recognized)
✅ $1 (correct)
```

### Not providing arguments
```
❌ /review-pr
   (expects /review-pr 123)
```

Always test with actual argument values!

## Testing Your Command with Arguments

1. **Create the file** with argument placeholders
2. **Run `/help`** to verify argument-hint appears
3. **Test with arguments**: `/command arg1 arg2`
4. **Test missing arguments**: `/command arg1` (omit arg2)
5. **Test special chars**: `/command "quoted string"`
6. **Verify replacements** work correctly

## When to Move to Complex Template

If you also need:
- Bash execution (get system state)
- File references (analyze files)
- Tool restrictions (security)

See [complex-command.md](complex-command.md) for template with all features.

---

**Remember**: Arguments make commands flexible and reusable. Choose the right style ($ARGUMENTS vs $1/$2) based on how you'll use the inputs.
