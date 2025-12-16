# Code Analysis Slash Command Examples

Real-world commands for analyzing, reviewing, and improving code.

## Example 1: Security Audit Command

**File**: `.claude/commands/security-audit.md`

```markdown
---
description: Comprehensive security audit of code
allowed-tools: Read, Grep, Glob
argument-hint: [file-or-directory]
---

## Code to Audit

@$1

## Project Security Guidelines

@CLAUDE.md
@docs/security-guidelines.md

## Security Audit Task

Perform comprehensive security analysis of @$1:

### 1. Authentication & Authorization
- [ ] Authentication checks present?
- [ ] Authorization properly enforced?
- [ ] Session management secure?
- [ ] Password handling correct?
- [ ] Token validation proper?

### 2. Input Validation
- [ ] All user input validated?
- [ ] Input sanitized before use?
- [ ] Type checking implemented?
- [ ] Length limits enforced?
- [ ] Allowlists used (not blocklists)?

### 3. Injection Vulnerabilities
- [ ] SQL injection prevention?
- [ ] NoSQL injection prevention?
- [ ] Command injection prevention?
- [ ] XSS prevention?
- [ ] LDAP injection prevention?

### 4. Data Protection
- [ ] Sensitive data encrypted?
- [ ] Secrets not in code?
- [ ] PII handled correctly?
- [ ] Data exposure prevented?
- [ ] Secure communication (HTTPS)?

### 5. API Security
- [ ] Rate limiting implemented?
- [ ] CORS configured correctly?
- [ ] CSRF protection present?
- [ ] API authentication required?
- [ ] Input validation on endpoints?

### 6. Error Handling
- [ ] Errors don't expose sensitive info?
- [ ] Stack traces not in production?
- [ ] Error messages user-friendly?
- [ ] Logging doesn't include secrets?

### 7. Dependencies
- [ ] Third-party libraries vetted?
- [ ] Dependency versions pinned?
- [ ] Known vulnerabilities checked?
- [ ] Minimal dependencies used?

For each issue found:
- **Severity**: Critical/High/Medium/Low
- **Location**: File and line number
- **Vulnerability**: Specific security issue
- **Exploit**: How it could be exploited
- **Fix**: Exact code changes needed
- **Prevention**: How to avoid in future
```

**Usage**:
```
/security-audit src/api/auth.js
```

---

## Example 2: Performance Analyzer

**File**: `.claude/commands/perf-analysis.md`

```markdown
---
description: Analyze code for performance issues
allowed-tools: Read, Grep, Glob, Bash(npm:*)
argument-hint: [file-to-analyze]
---

## Code to Analyze

@$1

## Performance Baseline (if available)

!\\\`npm run benchmark -- $1 2>/dev/null || echo "No benchmarks"\\`

## Analysis Task

Analyze @$1 for performance issues:

### 1. Algorithm Efficiency
- Time complexity of key operations
- Space complexity considerations
- Better algorithms available?
- Unnecessary computations?

### 2. Database Operations
- N+1 query problems?
- Missing indexes?
- Inefficient queries?
- Connection pooling used?
- Batch operations possible?

### 3. Memory Management
- Memory leaks?
- Unnecessary object creation?
- Caching opportunities?
- Resource cleanup proper?

### 4. I/O Operations
- Synchronous operations blocking?
- File operations optimized?
- Network calls efficient?
- Parallelization possible?

### 5. Loop Optimizations
- Loop invariants moved out?
- Early exits used?
- Unnecessary iterations?
- Better data structures?

### 6. Code-Level Optimizations
- Repeated calculations cached?
- String concatenation optimized?
- Regular expressions compiled?
- Closures creating overhead?

For each issue:
- **Current code**: Show problematic code
- **Performance impact**: Quantify if possible
- **Optimized code**: Show improved version
- **Benchmarks**: Expected improvement
- **Tradeoffs**: Readability vs performance
```

**Usage**:
```
/perf-analysis src/utils/data-processor.js
```

---

## Example 3: Code Quality Reviewer

**File**: `.claude/commands/quality-review.md`

```markdown
---
description: Review code quality and maintainability
allowed-tools: Read, Grep, Glob
argument-hint: [file-path]
---

## Code to Review

@$1

## Project Conventions

@CLAUDE.md
@.eslintrc.json
@.prettierrc

## Quality Review Task

Comprehensive quality review of @$1:

### 1. Readability
- Clear variable/function names?
- Consistent naming conventions?
- Appropriate abstraction level?
- Self-documenting code?
- Comments where needed (not obvious)?

### 2. Complexity
- Functions doing one thing?
- Cyclomatic complexity acceptable?
- Nesting depth reasonable?
- Long functions needing split?

### 3. DRY Principle
- Code duplication?
- Repeated patterns?
- Abstraction opportunities?
- Shared utilities available?

### 4. SOLID Principles
- Single Responsibility?
- Open/Closed?
- Liskov Substitution?
- Interface Segregation?
- Dependency Inversion?

### 5. Error Handling
- Errors caught appropriately?
- Error messages helpful?
- Resources cleaned up?
- Graceful degradation?

### 6. Testing
- Testable design?
- Dependencies injectable?
- Side effects minimized?
- Pure functions where possible?

### 7. Documentation
- Public APIs documented?
- Complex logic explained?
- Edge cases noted?
- Examples provided?

### 8. Code Smells
- Long parameter lists?
- Large classes/modules?
- Dead code?
- Speculative generality?
- Feature envy?

For each issue:
- **Problem**: What's wrong
- **Impact**: Why it matters
- **Refactored code**: How to fix it
- **Rationale**: Why the fix is better
```

**Usage**:
```
/quality-review src/services/payment.js
```

---

## Example 4: Dependency Analyzer

**File**: `.claude/commands/analyze-deps.md`

```markdown
---
description: Analyze dependencies and imports in code
allowed-tools: Read, Grep, Glob, Bash(npm:*)
argument-hint: [file-or-directory]
---

## Code to Analyze

@$1

## Dependency Graph

**Direct dependencies used**:
!\\\`grep -h "import\|require" $1 | sort | uniq\\`

**Package.json**:
@package.json

## Unused Dependencies Check

!\\\`npx depcheck $1 2>/dev/null || echo "Run: npm install -g depcheck"\\`

## Analysis Task

### 1. Import Analysis
- Which dependencies are imported?
- Are all imports used?
- Circular dependencies?
- Import organization logical?

### 2. Dependency Health
- Dependencies up to date?
- Security vulnerabilities?
- Maintenance status of packages?
- Bundle size impact?

### 3. Optimization Opportunities
- Tree-shaking possible?
- Code-splitting opportunities?
- Lazy loading applicable?
- Lighter alternatives available?

### 4. Best Practices
- Imports at top of file?
- Named imports used appropriately?
- Default exports used correctly?
- Barrel exports creating issues?

### 5. Recommendations
- Dependencies to remove
- Dependencies to update
- Import structure improvements
- Bundle optimization suggestions
```

**Usage**:
```
/analyze-deps src/components/
```

---

## Example 5: Architecture Reviewer

**File**: `.claude/commands/arch-review.md`

```markdown
---
description: Review architectural decisions and patterns
allowed-tools: Read, Grep, Glob
argument-hint: [directory-or-module]
---

## Code Structure

!\\\`find $1 -type f -name "*.js" -o -name "*.ts" | head -50\\`

## Key Files

@$1

## Project Architecture Guide

@CLAUDE.md
@docs/architecture.md

## Architecture Review Task

### 1. Structure Analysis
- Logical organization?
- Clear separation of concerns?
- Appropriate layering?
- Module boundaries clear?

### 2. Design Patterns
- Which patterns are used?
- Patterns applied correctly?
- Patterns appropriate for context?
- Missing beneficial patterns?

### 3. Coupling & Cohesion
- High cohesion within modules?
- Low coupling between modules?
- Dependencies unidirectional?
- Circular dependencies?

### 4. Scalability
- Can it handle growth?
- Performance at scale?
- Easy to add features?
- Technical debt accumulating?

### 5. Testability
- Easy to unit test?
- Dependencies mockable?
- Integration points clear?
- Test coverage achievable?

### 6. Maintainability
- Easy to understand?
- Easy to modify?
- Consistent patterns?
- Documentation adequate?

Provide:
- Current architecture diagram (text/ASCII)
- Issues identified
- Recommended improvements
- Migration path if needed
```

**Usage**:
```
/arch-review src/api/
```

---

## Example 6: Test Coverage Analyzer

**File**: `.claude/commands/coverage-analysis.md`

```markdown
---
description: Analyze test coverage and suggest tests
allowed-tools: Bash(npm:*), Bash(pytest:*), Read, Grep, Glob
argument-hint: [file-path]
---

## Source Code

@$1

## Existing Tests

!\\\`find tests -name "*$(basename $1 .js)*" 2>/dev/null | head -10\\`

## Current Coverage

!\\\`npm run coverage -- $1 2>/dev/null || pytest --cov=$1 --cov-report=term 2>/dev/null || echo "Coverage not available"\\`

## Test Analysis Task

### 1. Coverage Assessment
- Overall coverage percentage?
- Uncovered lines/branches?
- Critical paths covered?
- Edge cases tested?

### 2. Missing Tests
- Untested functions?
- Untested branches?
- Error paths tested?
- Integration scenarios?

### 3. Test Quality
- Assertions meaningful?
- Tests independent?
- Setup/teardown proper?
- Mocks appropriate?

### 4. Test Suggestions

For each uncovered section, provide:

```javascript
describe('[function name]', () => {
  it('should [behavior]', () => {
    // Arrange
    // Act
    // Assert
  });
});
```

### 5. Priority
- Which tests are most important?
- Order to implement tests
- Risk assessment if not tested
```

**Usage**:
```
/coverage-analysis src/utils/validator.js
```

---

## Implementation Tips

1. **Use specific analysis criteria**
   - Checklists make reviews systematic
   - Easy to verify coverage

2. **Provide actionable feedback**
   - Show exact code changes
   - Explain why improvements matter

3. **Include examples**
   - Before/after code
   - Common patterns to follow

4. **Reference standards**
   - Link to project conventions
   - Industry best practices

5. **Prioritize findings**
   - Critical/High/Medium/Low
   - Order by impact

---

These commands help maintain code quality systematically!
