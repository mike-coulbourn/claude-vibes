# Slash Command with File References Template

Include file contents in your commands using the `@` prefix.

## When to Use This Template

- Analyzing specific files
- Comparing files
- Generating code based on existing files
- Following project patterns from example files
- Ensuring project conventions are included

## Basic Syntax

```markdown
---
description: [Brief description]
---

Analyze the file @path/to/file.js

[Your prompt about the file]
```

**Key features**:
- File contents are automatically included
- CLAUDE.md files from directory hierarchy auto-included
- Works with relative or absolute paths
- Supports multiple file references

## How File References Work

When you write `@src/auth/login.js`, Claude receives:
1. Contents of `src/auth/login.js`
2. Contents of `src/auth/CLAUDE.md` (if exists)
3. Contents of `src/CLAUDE.md` (if exists)
4. Contents of root `CLAUDE.md` (if exists)

This ensures project conventions are always available.

## Complete Examples

### Example 1: Code Review

**File**: `.claude/commands/review.md`

```markdown
---
description: Review a specific file for code quality
argument-hint: [file-path]
---

Review @$1 for:

1. **Security**
   - Input validation
   - SQL injection / XSS risks
   - Authentication / authorization
   - Data exposure

2. **Performance**
   - Inefficient operations
   - Memory leaks
   - Unnecessary computations
   - Database query optimization

3. **Maintainability**
   - Code clarity and readability
   - Naming conventions
   - Function size and complexity
   - Comments and documentation

4. **Best Practices**
   - Error handling
   - Testing approach
   - Logging
   - Following language idioms

Provide specific, actionable feedback with code examples.
```

**Usage**:
```
/review src/auth/login.js
```

### Example 2: File Comparison

**File**: `.claude/commands/compare-files.md`

```markdown
---
description: Compare two files and explain differences
argument-hint: [file1] [file2]
---

## File 1

@$1

## File 2

@$2

## Analysis Task

Compare these two files and explain:

1. **What Changed**
   - New features added
   - Bugs fixed
   - Code refactored
   - Deleted functionality

2. **Why**
   - Purpose of changes
   - Benefits gained
   - Risks introduced

3. **Impact**
   - Breaking changes?
   - Performance implications?
   - Migration needed?

4. **Recommendations**
   - Further improvements?
   - Testing needed?
   - Documentation to update?
```

**Usage**:
```
/compare-files src/v1/api.js src/v2/api.js
```

### Example 3: Generate Tests

**File**: `.claude/commands/gen-tests.md`

```markdown
---
description: Generate tests for a file following project patterns
argument-hint: [file-to-test]
allowed-tools: Read, Grep, Glob, Write
---

## Source Code to Test

@$1

## Existing Test Patterns

Look at how we structure tests:
@tests/example.test.js

## Project Testing Conventions

@CLAUDE.md

## Your Task

Generate comprehensive tests for @$1 that:

1. **Follow Our Patterns**
   - Same structure as existing tests
   - Same naming conventions
   - Same assertion style

2. **Cover All Cases**
   - Happy path scenarios
   - Edge cases
   - Error conditions
   - Integration points

3. **Include**
   - Setup and teardown
   - Mock external dependencies
   - Clear test descriptions
   - Helpful comments

Write the test file following our naming convention: [filename].test.js
```

**Usage**:
```
/gen-tests src/utils/validator.js
```

### Example 4: Documentation Generator

**File**: `.claude/commands/document.md`

```markdown
---
description: Generate documentation for a file
argument-hint: [file-path]
---

## Source Code

@$1

## Existing Documentation Examples

See how we document similar code:
@docs/api-reference.md

## Task

Generate comprehensive documentation for @$1 including:

1. **Overview**
   - Purpose of this module
   - When to use it
   - Key concepts

2. **API Reference**
   - Each exported function/class
   - Parameters and types
   - Return values
   - Exceptions thrown

3. **Examples**
   - Common use cases
   - Code examples
   - Expected output

4. **Notes**
   - Performance considerations
   - Thread safety
   - Known limitations

Follow our documentation style and format.
```

**Usage**:
```
/document src/api/users.js
```

### Example 5: Refactor Suggester

**File**: `.claude/commands/suggest-refactor.md`

```markdown
---
description: Suggest refactoring for a file
argument-hint: [file-path]
---

## Current Implementation

@$1

## Project Patterns

Check our architectural patterns:
@CLAUDE.md
@docs/architecture.md

## Similar Well-Refactored Code

@src/examples/good-structure.js

## Analysis Task

Analyze @$1 and suggest refactoring:

1. **Current Issues**
   - Code smells
   - Duplication
   - Complexity
   - Coupling

2. **Proposed Improvements**
   - Specific refactoring steps
   - Why each improvement helps
   - Show before/after code

3. **Refactoring Plan**
   - Order of operations
   - Testing strategy
   - Risk mitigation

4. **Expected Benefits**
   - Maintainability
   - Testability
   - Performance
   - Readability

Ensure suggestions align with our project patterns.
```

**Usage**:
```
/suggest-refactor src/legacy/payment.js
```

## Directory References

Reference a directory to see its structure:

```markdown
---
description: Analyze directory structure
argument-hint: [directory-path]
---

Structure of @$1:

[Directory listing is included]

Based on this structure, suggest:
1. Organizational improvements
2. Missing components
3. Better grouping
```

**Note**: Directories show listing, not file contents. To analyze contents, reference specific files.

## Multiple File References

Include multiple files in one command:

```markdown
---
description: Analyze authentication flow
---

## Login Handler

@src/auth/login.js

## Authentication Middleware

@src/middleware/auth.js

## User Model

@src/models/user.js

## Analysis

Based on these three files, analyze our authentication flow:
1. Security assessment
2. Flow diagram
3. Potential issues
4. Improvement suggestions
```

## Combining with Arguments

```markdown
---
description: Compare file with another
argument-hint: [file1] [file2]
---

## First File
@$1

## Second File
@$2

[Comparison task...]
```

## Combining with Bash

```markdown
---
description: Analyze file with git history
allowed-tools: Bash(git:*)
argument-hint: [file-path]
---

## Current File

@$1

## Recent Changes

!`git log --oneline -5 -- $1`

## Diff from Last Week

!`git diff HEAD~7 HEAD -- $1`

## Analysis

How has @$1 evolved? What patterns emerge?
```

## Automatic CLAUDE.md Inclusion

When you reference a file, related CLAUDE.md files are automatically included:

```markdown
# You write:
@src/components/Button.jsx

# Claude receives:
- src/components/Button.jsx (the file you requested)
- src/components/CLAUDE.md (component patterns)
- src/CLAUDE.md (source conventions)
- CLAUDE.md (project conventions)
```

This ensures conventions are always available without explicit references.

## Pattern: Following Existing Examples

```markdown
---
description: Create new API endpoint
argument-hint: [endpoint-name]
---

## Existing Endpoint Examples

@src/api/users.js
@src/api/posts.js

## Your Task

Create a new API endpoint named $1 that:
- Follows the patterns above
- Includes same error handling
- Uses same validation approach
- Matches our API conventions

Show the complete implementation.
```

## Pattern: Project Consistency

```markdown
---
description: Ensure file follows project patterns
argument-hint: [file-path]
---

## File to Check

@$1

## Project Conventions

@CLAUDE.md
@docs/style-guide.md

## Example of Good Pattern

@src/examples/reference-implementation.js

## Task

Compare @$1 against our conventions and examples.

List:
1. What it does well
2. What doesn't match patterns
3. Specific changes needed
4. Updated code following patterns
```

## Best Practices

1. **Use with arguments for flexibility**
   ```markdown
   argument-hint: [file-path]
   Review @$1 for code quality
   ```

2. **Reference examples**
   ```markdown
   Follow patterns in @tests/example.test.js
   ```

3. **Include conventions**
   ```markdown
   Ensure alignment with @CLAUDE.md
   ```

4. **Be specific in prompts**
   ```markdown
   Review @src/auth.js focusing on security
   ```

5. **Combine with bash for context**
   ```markdown
   File: @$1
   Recent changes: !`git log -5 --oneline -- $1`
   ```

## Common Pitfalls

### Missing @ prefix
```markdown
❌ Review src/auth.js
✅ Review @src/auth.js
```

### Wrong path
```markdown
❌ @/src/auth.js (leading slash might fail)
✅ @src/auth.js (relative path)
✅ @/Users/you/project/src/auth.js (absolute)
```

### File doesn't exist
```bash
# Verify first:
ls src/auth.js

# Then reference:
@src/auth.js
```

### Too many large files
```markdown
❌ @src/*.js (glob might include 100+ files)
✅ @src/auth.js @src/api.js (specific files)
```

## Path Resolution

File references are relative to current working directory:

```markdown
# If you're in /Users/you/project:
@src/auth.js           # Resolves to /Users/you/project/src/auth.js
@./src/auth.js         # Same
@/Users/you/project/src/auth.js  # Absolute path
```

## Testing File References

1. **Verify file exists**
   ```bash
   ls src/auth.js
   cat src/auth.js
   ```

2. **Add to command**
   ```markdown
   Review @src/auth.js
   ```

3. **Test command**
   ```
   /review
   ```

4. **Verify Claude received file**
   - Check response mentions file contents
   - Verify specific code is referenced

## When to Move to Complex Template

If you also need:
- Arguments (dynamic inputs)
- Bash execution (system context)
- All features combined

See [complex-command.md](complex-command.md) for template with all features.

---

**Remember**: File references automatically include CLAUDE.md files from the directory hierarchy, ensuring project conventions are always available to Claude.
