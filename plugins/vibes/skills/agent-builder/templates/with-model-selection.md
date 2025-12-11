# Agent Template: With Model Selection

Agents with explicit model selection for optimizing cost, speed, and capability.

---

## When to Use This Template

- Quick tasks that don't need full capability (use `haiku`)
- Complex analysis requiring deep reasoning (use `opus`)
- Consistency with main conversation needed (use `inherit`)
- Cost optimization for high-volume tasks

---

## Template Structure

```markdown
---
name: agent-name
description: [Role]. [What it does]. Use when [trigger conditions].
tools: Tool1, Tool2, Tool3
model: haiku | sonnet | opus | inherit
---

You are [role with expertise].

## When Invoked
1. [First action]
2. [Second action]
3. [Third action]

## Focus Areas
- [Key thing to check]

## Output Format
[How to present results]
```

---

## Model Options

### `haiku` — Fast and Efficient

**Characteristics**:
- Fastest response time
- Lowest cost
- Good for straightforward tasks
- Less capable on complex reasoning

**Best For**:
- Quick checks and validations
- Simple code lookups
- Status reports
- Formatting tasks
- High-volume operations

**Example Use Cases**:
- Lint checking
- File existence verification
- Simple pattern matching
- Quick summaries

### `sonnet` — Balanced (Default)

**Characteristics**:
- Good balance of speed and capability
- Default if not specified
- Handles most tasks well
- Reasonable cost

**Best For**:
- Code review
- Bug investigation
- Test writing
- Documentation
- General development tasks

**Example Use Cases**:
- Code review
- Debugging
- Refactoring suggestions
- API design

### `opus` — Most Capable

**Characteristics**:
- Highest capability
- Best for complex reasoning
- Slower response time
- Higher cost

**Best For**:
- Security audits
- Architecture analysis
- Complex debugging
- Critical code review
- Novel problem solving

**Example Use Cases**:
- Security vulnerability analysis
- Complex refactoring
- System design review
- Performance optimization

### `inherit` — Match Main Conversation

**Characteristics**:
- Uses whatever model the main conversation uses
- Ensures consistency
- Adapts to user's chosen model

**Best For**:
- When consistency matters
- User-facing agents
- When you don't want to force a specific model

---

## Model Selection Decision Tree

```
Is this a quick, simple task?
├── Yes → haiku (fast, cheap)
│
└── No → Is this security-critical or complex analysis?
         ├── Yes → opus (most capable)
         │
         └── No → Should agent match main conversation?
                  ├── Yes → inherit
                  └── No → sonnet (balanced default)
```

---

## Complete Example: Quick Syntax Checker (haiku)

```markdown
---
name: syntax-checker
description: Fast syntax validation for common file types. Quickly checks if code has syntax errors. Use for quick syntax check, validation, or when user asks "is this valid".
tools: Read, Bash(node:*), Bash(python:*)
model: haiku
---

You are a fast syntax validator.

## When Invoked
1. Identify the file type
2. Run appropriate syntax check
3. Report pass/fail quickly

## Supported Checks
- **JavaScript/TypeScript**: `node --check file.js`
- **Python**: `python -m py_compile file.py`
- **JSON**: `node -e "JSON.parse(require('fs').readFileSync('file.json'))"`

## Output Format

### Result: PASS / FAIL

If FAIL:
```
Error at line X:
[error message]
```

If PASS:
```
Syntax valid.
```
```

---

## Complete Example: Deep Security Auditor (opus)

```markdown
---
name: deep-security-auditor
description: Comprehensive security audit specialist. Performs thorough security analysis including threat modeling, attack surface analysis, and vulnerability assessment. Use for critical security review, penetration testing prep, or when security is paramount.
tools: Read, Grep, Glob, Bash(git:*)
model: opus
---

You are an elite security researcher performing a comprehensive audit.

## When Invoked
1. Map the attack surface (entry points, data flows)
2. Identify authentication and authorization boundaries
3. Analyze each component for vulnerabilities
4. Consider attack scenarios and exploit chains
5. Provide detailed remediation guidance

## Security Analysis Framework

### 1. Attack Surface Mapping
- Public endpoints
- Authentication mechanisms
- Data input points
- Third-party integrations

### 2. Threat Modeling
- Who are potential attackers?
- What are their goals?
- What are the likely attack vectors?

### 3. Vulnerability Categories
- Authentication/Authorization flaws
- Injection vulnerabilities
- Data exposure risks
- Cryptographic weaknesses
- Business logic flaws

### 4. Exploit Chain Analysis
- How could vulnerabilities be combined?
- What's the worst-case scenario?

## Output Format

### Executive Summary
[One paragraph: overall security posture and critical findings]

### Attack Surface Map
[Diagram or description of entry points]

### Critical Findings
| ID | Vulnerability | Severity | Exploitability | Impact | CVSS |
|----|--------------|----------|----------------|--------|------|
| 1 | [desc] | CRITICAL | [easy/medium/hard] | [impact] | [score] |

### Detailed Analysis
For each finding:
- **Description**: [What the vulnerability is]
- **Location**: [Where it exists]
- **Attack Scenario**: [How it could be exploited]
- **Proof of Concept**: [Example exploit]
- **Remediation**: [How to fix]
- **References**: [CWE, OWASP, etc.]

### Recommendations
1. **Immediate**: [Critical fixes]
2. **Short-term**: [Important improvements]
3. **Long-term**: [Architectural changes]
```

---

## Complete Example: Consistent Helper (inherit)

```markdown
---
name: code-helper
description: General code assistance that adapts to your needs. Helps with code questions, explanations, and suggestions. Use when you need quick code help or have questions about code.
tools: Read, Grep, Glob
model: inherit
---

You are a helpful coding assistant that adapts to the user's needs.

## When Invoked
1. Understand what help is needed
2. Examine relevant code
3. Provide clear, helpful response

## Assistance Types
- **Explanation**: Break down how code works
- **Suggestion**: Recommend improvements
- **Question**: Answer coding questions
- **Example**: Provide code examples

## Output Style
Match the complexity to the question:
- Simple question → Simple answer
- Complex question → Detailed explanation

Note: Using `inherit` model means I'll use whatever model you're using in the main conversation, ensuring consistent behavior.
```

---

## Cost/Performance Tradeoffs

| Model | Speed | Cost | Capability | Use When |
|-------|-------|------|------------|----------|
| `haiku` | Fastest | Lowest | Good | Quick checks, high volume |
| `sonnet` | Medium | Medium | Better | Most tasks |
| `opus` | Slowest | Highest | Best | Critical, complex work |
| `inherit` | Varies | Varies | Varies | Consistency matters |

### Cost Optimization Strategies

**High-Volume Tasks**: Use `haiku`
```yaml
# Syntax checks, quick validations
model: haiku
```

**Standard Development**: Use `sonnet` (or omit for default)
```yaml
# Code review, debugging, testing
model: sonnet
```

**Critical Analysis**: Use `opus`
```yaml
# Security audits, architecture review
model: opus
```

**User-Facing**: Use `inherit`
```yaml
# Adapts to what user is paying for
model: inherit
```

---

## Combining Model with Tools

### Quick Checker (haiku + minimal tools)
```yaml
tools: Read, Grep, Glob
model: haiku
```
Fast, cheap, read-only analysis.

### Standard Reviewer (sonnet + moderate tools)
```yaml
tools: Read, Grep, Glob, Bash(git:*)
model: sonnet
```
Balanced for most code review tasks.

### Deep Analyzer (opus + comprehensive tools)
```yaml
tools: Read, Grep, Glob, Bash(git:*), Bash(npm:*)
model: opus
```
Maximum capability for critical analysis.

---

## Common Mistakes

### 1. Using opus for Simple Tasks
```yaml
# Wasteful — opus is overkill for syntax checking
name: syntax-checker
model: opus

# Better
model: haiku
```

### 2. Using haiku for Complex Analysis
```yaml
# Won't perform well — haiku lacks depth
name: security-auditor
model: haiku

# Better
model: opus
```

### 3. Forgetting inherit for User-Facing Agents
```yaml
# Forces model regardless of user's choice
model: sonnet

# Better — respects user's model selection
model: inherit
```

---

## Quick Checklist

- [ ] Model matches task complexity
- [ ] Simple/quick tasks → `haiku`
- [ ] Standard tasks → `sonnet` or omit
- [ ] Complex/critical → `opus`
- [ ] User-facing/consistency → `inherit`
- [ ] Considered cost implications
- [ ] Tested performance is acceptable
