# Specialized Domains Marketplace Examples

Six complete plugin examples for domain-specific workflows.

---

## Example 1: API Design Plugin

API design and documentation tools.

### Plugin Structure

```
api-designer/
├── .claude-plugin/
│   └── plugin.json
├── commands/
│   ├── api-design.md
│   ├── openapi-generate.md
│   └── api-mock.md
└── agents/
    └── api-architect.md
```

### .claude-plugin/plugin.json

```json
{
  "name": "api-designer",
  "description": "API design tools: OpenAPI generation, endpoint design, mock servers",
  "version": "2.5.0",
  "author": {"name": "API Guild"},
  "license": "MIT"
}
```

### commands/api-design.md

```markdown
---
description: Design a new API endpoint
allowed-tools: Read, Write
argument-hint: [resource] [action] (e.g., users create)
---

Design API endpoint for: $ARGUMENTS

## API Design Process

### 1. Resource Identification
- Resource: $1
- Action: $2 (create/read/update/delete/list/search)

### 2. Endpoint Design
Following REST conventions:
- POST /resources - Create
- GET /resources/:id - Read
- PUT /resources/:id - Update
- DELETE /resources/:id - Delete
- GET /resources - List

### 3. Schema Design
- Request body schema
- Response schema
- Error responses

## Output

### API Endpoint Design: $1 $2

#### Endpoint
```
[METHOD] /api/v1/[resource]
```

#### Request
```json
{
  // Request body schema
}
```

#### Response (200)
```json
{
  // Success response schema
}
```

#### Error Responses
| Status | Description |
|--------|-------------|
| 400 | Bad Request - Invalid input |
| 401 | Unauthorized |
| 404 | Not Found |
| 500 | Internal Server Error |

#### Implementation Notes
- Authentication: [Required/Optional]
- Rate Limiting: [Limits]
- Caching: [Strategy]
```

### agents/api-architect.md

```markdown
---
name: api-architect
description: Expert API architect for design reviews and guidance. Use when designing APIs, reviewing API changes, or making architectural decisions. Triggers: "API design", "endpoint design", "REST API", "GraphQL"
tools: Read, Grep, Glob
model: sonnet
---

You are a senior API architect with expertise in REST, GraphQL, and API best practices.

## When Invoked

1. Understand the API requirements
2. Review existing API patterns in the codebase
3. Design or review API following best practices
4. Consider:
   - RESTful principles
   - Versioning strategy
   - Error handling
   - Pagination
   - Rate limiting
   - Documentation

## API Design Principles

### REST Best Practices
- Use nouns for resources, not verbs
- Consistent naming conventions
- Proper HTTP methods
- Meaningful status codes
- HATEOAS where appropriate

### Versioning
- URL versioning: /api/v1/
- Header versioning: Accept-Version
- Deprecation strategy

### Error Handling
```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Human readable message",
    "details": [...]
  }
}
```

## Output Format

### API Design Review/Recommendation

**Endpoint**: [Method] [Path]

#### Design Assessment
- RESTfulness: [Score/Notes]
- Naming: [Score/Notes]
- Error Handling: [Score/Notes]

#### Recommendations
1. [Recommendation]
2. [Recommendation]

#### OpenAPI Spec
```yaml
paths:
  /resource:
    get:
      # ...
```
```

---

## Example 2: Database Tools Plugin

Database management and optimization.

### Plugin Structure

```
database-tools/
├── .claude-plugin/
│   └── plugin.json
├── commands/
│   ├── db-analyze.md
│   ├── migration-create.md
│   └── query-optimize.md
└── agents/
    └── db-optimizer.md
```

### .claude-plugin/plugin.json

```json
{
  "name": "database-tools",
  "description": "Database tools: schema analysis, migrations, query optimization",
  "version": "3.0.0",
  "author": {"name": "Data Team"},
  "license": "MIT"
}
```

### commands/query-optimize.md

```markdown
---
description: Analyze and optimize a SQL query
allowed-tools: Read, Write
argument-hint: [query-file or inline query]
---

Optimize query: $ARGUMENTS

## Query Optimization Process

### 1. Query Analysis
- Parse query structure
- Identify tables and joins
- Analyze WHERE clauses
- Check for N+1 patterns

### 2. Optimization Techniques
- Index recommendations
- Join optimization
- Subquery refactoring
- Pagination improvements

## Output

### Query Optimization Report

#### Original Query
```sql
[Original query]
```

#### Analysis
| Aspect | Finding | Impact |
|--------|---------|--------|
| Joins | Missing index on foreign key | High |
| WHERE | Full table scan possible | High |
| SELECT | SELECT * used | Medium |

#### Recommended Indexes
```sql
CREATE INDEX idx_table_column ON table(column);
```

#### Optimized Query
```sql
[Optimized query with explanations]
```

#### Expected Improvement
- Estimated speedup: Xms → Yms
- Index size: ~Z MB
```

### agents/db-optimizer.md

```markdown
---
name: db-optimizer
description: Database performance expert. Use when optimizing queries, designing schemas, or troubleshooting database issues. Triggers: "slow query", "database performance", "optimize query", "schema design"
tools: Read, Grep, Glob
model: sonnet
---

You are a database performance expert specializing in SQL optimization.

## When Invoked

1. Analyze the database context:
   - Schema structure
   - Existing indexes
   - Query patterns
2. Identify performance issues:
   - Missing indexes
   - Inefficient queries
   - Schema problems
3. Provide actionable recommendations

## Optimization Areas

### Query Optimization
- Use EXPLAIN ANALYZE
- Index usage
- Join order
- Subquery elimination

### Schema Design
- Normalization balance
- Appropriate data types
- Index strategy
- Partitioning needs

### Common Issues
- N+1 queries
- Missing indexes on foreign keys
- Over-indexing
- Bloated tables

## Output Format

### Database Optimization Report

**Focus Area**: [Query/Schema/Index]

#### Current State
[Analysis of current performance]

#### Issues Found
| Priority | Issue | Impact |
|----------|-------|--------|
| High | Missing index | 100x slower |

#### Recommendations
1. [Recommendation with SQL]
2. [Recommendation with SQL]

#### Implementation Plan
1. [Step 1]
2. [Step 2]
```

---

## Example 3: Frontend Tools Plugin

Frontend development utilities.

### Plugin Structure

```
frontend-tools/
├── .claude-plugin/
│   └── plugin.json
├── commands/
│   ├── component-create.md
│   ├── accessibility-check.md
│   └── bundle-analyze.md
└── agents/
    └── ui-reviewer.md
```

### .claude-plugin/plugin.json

```json
{
  "name": "frontend-tools",
  "description": "Frontend development: component generation, accessibility, bundle analysis",
  "version": "2.0.0",
  "author": {"name": "Frontend Guild"},
  "license": "MIT"
}
```

### commands/component-create.md

```markdown
---
description: Create a new React component with tests and stories
allowed-tools: Read, Write, Glob
argument-hint: [ComponentName] [type] (page|feature|ui)
---

Create component: $1 (type: $2)

## Component Generation

### Component Types
- **page**: Page-level component with routing
- **feature**: Feature component with state
- **ui**: Presentational UI component

### Generated Files
```
components/$1/
├── $1.tsx           # Component
├── $1.test.tsx      # Tests
├── $1.stories.tsx   # Storybook
├── $1.module.css    # Styles
└── index.ts         # Export
```

## Output

### Component Created: $1

#### Files Generated

**$1.tsx**
```tsx
import styles from './$1.module.css';

interface $1Props {
  // Define props
}

export function $1({ }: $1Props) {
  return (
    <div className={styles.container}>
      {/* Component content */}
    </div>
  );
}
```

**$1.test.tsx**
```tsx
import { render, screen } from '@testing-library/react';
import { $1 } from './$1';

describe('$1', () => {
  it('renders correctly', () => {
    render(<$1 />);
    // Add assertions
  });
});
```

**$1.stories.tsx**
```tsx
import type { Meta, StoryObj } from '@storybook/react';
import { $1 } from './$1';

const meta: Meta<typeof $1> = {
  component: $1,
};

export default meta;
type Story = StoryObj<typeof $1>;

export const Default: Story = {
  args: {},
};
```

#### Next Steps
1. Implement component logic
2. Add prop types
3. Write tests
4. Document in Storybook
```

### commands/accessibility-check.md

```markdown
---
description: Check components for accessibility issues
allowed-tools: Read, Glob, Grep, Bash(npx:*)
argument-hint: [path] (file or directory)
---

Check accessibility in: $ARGUMENTS

## Accessibility Audit

### WCAG Checks
- Semantic HTML
- ARIA attributes
- Color contrast
- Keyboard navigation
- Screen reader support

### Common Issues
- Missing alt text
- Invalid ARIA roles
- Poor color contrast
- Missing focus indicators
- Non-semantic elements

## Output

### Accessibility Report

**Path**: $ARGUMENTS
**Files Checked**: X

#### Critical Issues
| File | Line | Issue | WCAG |
|------|------|-------|------|
| Button.tsx | 15 | Missing aria-label | 4.1.2 |

#### Warnings
| File | Line | Issue | WCAG |
|------|------|-------|------|

#### Recommendations
1. Add aria-label to icon buttons
2. Ensure color contrast ratio > 4.5:1
3. Add focus styles to interactive elements

#### Passed Checks
- [x] Semantic HTML structure
- [x] Proper heading hierarchy
- [x] Form labels present
```

### agents/ui-reviewer.md

```markdown
---
name: ui-reviewer
description: Frontend and UI expert for code reviews. Use when reviewing React/Vue/frontend code, checking accessibility, or improving UI patterns. Triggers: "review component", "UI review", "frontend review", "accessibility"
tools: Read, Grep, Glob
model: inherit
---

You are a senior frontend engineer reviewing UI code.

## When Invoked

1. Analyze component structure
2. Check for:
   - React best practices
   - Accessibility compliance
   - Performance patterns
   - State management
   - Styling approach
3. Provide specific feedback

## Review Checklist

### React Patterns
- [ ] Proper component composition
- [ ] Hooks used correctly
- [ ] Memoization where needed
- [ ] Error boundaries present

### Accessibility
- [ ] Semantic HTML
- [ ] ARIA attributes
- [ ] Keyboard navigation
- [ ] Focus management

### Performance
- [ ] Unnecessary re-renders
- [ ] Large bundle impacts
- [ ] Lazy loading used

### Styling
- [ ] Consistent approach
- [ ] Responsive design
- [ ] Dark mode support

## Output Format

### UI Code Review

**Component**: [Name]

#### Strengths
- [What's done well]

#### Issues
| Priority | Issue | Location |
|----------|-------|----------|
| High | Missing error boundary | App.tsx |

#### Suggestions
1. [Specific improvement]
2. [Specific improvement]
```

---

## Example 4: DevOps Tools Plugin

Infrastructure and DevOps automation.

### Plugin Structure

```
devops-tools/
├── .claude-plugin/
│   └── plugin.json
├── commands/
│   ├── infra-check.md
│   ├── docker-optimize.md
│   └── k8s-debug.md
└── agents/
    └── infra-advisor.md
```

### .claude-plugin/plugin.json

```json
{
  "name": "devops-tools",
  "description": "DevOps utilities: infrastructure checks, Docker optimization, K8s debugging",
  "version": "2.8.0",
  "author": {"name": "DevOps Guild"},
  "license": "MIT"
}
```

### commands/docker-optimize.md

```markdown
---
description: Optimize Dockerfile for smaller images and faster builds
allowed-tools: Read, Write
argument-hint: [dockerfile-path] (defaults to ./Dockerfile)
---

Optimize Dockerfile: $ARGUMENTS

## Optimization Techniques

### Image Size
- Multi-stage builds
- Minimal base images
- Remove unnecessary files
- Combine RUN commands

### Build Speed
- Layer caching optimization
- .dockerignore usage
- Parallel builds

### Security
- Non-root user
- Minimal permissions
- No secrets in image

## Output

### Dockerfile Optimization Report

**Original Size**: ~X MB
**Optimized Size**: ~Y MB (Z% reduction)

#### Issues Found
| Issue | Impact | Fix |
|-------|--------|-----|
| No multi-stage | Size | Add build stage |
| Root user | Security | Add USER directive |

#### Optimized Dockerfile
```dockerfile
# Build stage
FROM node:20-alpine AS builder
WORKDIR /app
COPY package*.json ./
RUN npm ci --only=production

# Runtime stage
FROM node:20-alpine
RUN addgroup -g 1001 app && adduser -u 1001 -G app -s /bin/sh -D app
WORKDIR /app
COPY --from=builder /app/node_modules ./node_modules
COPY --chown=app:app . .
USER app
EXPOSE 3000
CMD ["node", "server.js"]
```

#### Improvements
- Multi-stage build: -50% size
- Alpine base: -30% size
- Non-root user: Security improvement
```

### agents/infra-advisor.md

```markdown
---
name: infra-advisor
description: Infrastructure and DevOps expert. Use for infrastructure decisions, Docker/K8s issues, CI/CD optimization. Triggers: "infrastructure", "DevOps", "Docker", "Kubernetes", "CI/CD"
tools: Read, Grep, Glob, Bash(docker:*, kubectl:*)
model: sonnet
---

You are a senior DevOps engineer advising on infrastructure.

## When Invoked

1. Understand the infrastructure context
2. Analyze current setup:
   - Container configuration
   - Kubernetes resources
   - CI/CD pipelines
3. Identify improvements
4. Provide actionable recommendations

## Areas of Expertise

### Containers
- Dockerfile best practices
- Image optimization
- Security hardening
- Registry management

### Kubernetes
- Resource sizing
- Scaling strategies
- Networking
- Security policies

### CI/CD
- Pipeline optimization
- Caching strategies
- Parallel execution
- Deployment strategies

## Output Format

### Infrastructure Assessment

**Focus**: [Area]

#### Current State
[Analysis]

#### Recommendations
| Priority | Recommendation | Effort |
|----------|----------------|--------|
| High | Add resource limits | Low |

#### Implementation
```yaml
# Example configuration
```
```

---

## Example 5: Security Tools Plugin

Security scanning and hardening.

### Plugin Structure

```
security-tools/
├── .claude-plugin/
│   └── plugin.json
├── commands/
│   ├── security-scan.md
│   ├── secrets-check.md
│   └── deps-audit.md
└── agents/
    └── security-analyst.md
```

### .claude-plugin/plugin.json

```json
{
  "name": "security-tools",
  "description": "Security tools: vulnerability scanning, secrets detection, dependency audits",
  "version": "3.5.0",
  "author": {"name": "Security Team"},
  "license": "MIT"
}
```

### commands/security-scan.md

```markdown
---
description: Comprehensive security scan of the codebase
allowed-tools: Read, Grep, Glob, Bash(npm:*, npx:*)
---

Run comprehensive security scan.

## Security Scan Areas

### 1. Secrets Detection
- API keys
- Passwords
- Private keys
- Connection strings

### 2. Dependency Vulnerabilities
- Known CVEs
- Outdated packages
- Unmaintained deps

### 3. Code Vulnerabilities
- SQL injection
- XSS vulnerabilities
- Command injection
- Path traversal

### 4. Configuration Issues
- Insecure defaults
- Debug mode enabled
- CORS misconfiguration

## Output

### Security Scan Report

**Scan Date**: [Date]
**Risk Score**: [0-100]

#### Critical Findings
| Type | Location | Description | Remediation |
|------|----------|-------------|-------------|
| Secret | .env.example | Exposed API key | Remove and rotate |

#### High Priority
| Type | Location | Description | Remediation |
|------|----------|-------------|-------------|

#### Medium Priority
[Summary]

#### Low Priority
[Summary]

#### Dependency Vulnerabilities
| Package | Version | CVE | Severity | Fix |
|---------|---------|-----|----------|-----|
| lodash | 4.17.15 | CVE-2021-23337 | High | 4.17.21 |

#### Recommendations
1. [Immediate actions]
2. [Short-term improvements]
3. [Long-term hardening]
```

### agents/security-analyst.md

```markdown
---
name: security-analyst
description: Security expert for vulnerability analysis and remediation. Use for security reviews, threat modeling, or investigating vulnerabilities. Triggers: "security review", "vulnerability", "threat model", "security analysis"
tools: Read, Grep, Glob
model: sonnet
---

You are a security analyst with expertise in application security.

## When Invoked

1. Understand the security context
2. Analyze for vulnerabilities:
   - OWASP Top 10
   - Business logic flaws
   - Authentication/Authorization
   - Data exposure
3. Assess risk and impact
4. Provide remediation guidance

## Security Analysis Areas

### OWASP Top 10 (2021)
1. Broken Access Control
2. Cryptographic Failures
3. Injection
4. Insecure Design
5. Security Misconfiguration
6. Vulnerable Components
7. Auth Failures
8. Data Integrity Failures
9. Logging Failures
10. SSRF

### Code Patterns to Check
- User input handling
- Authentication flows
- Session management
- Data encryption
- Error handling

## Output Format

### Security Analysis

**Scope**: [What was analyzed]

#### Threat Model
| Threat | Likelihood | Impact | Risk |
|--------|------------|--------|------|
| [Threat] | Medium | High | High |

#### Vulnerabilities Found
| ID | Type | Severity | Location | Status |
|----|------|----------|----------|--------|
| V1 | XSS | High | input.ts:45 | Open |

#### Remediation Plan
1. [Priority 1 fix]
2. [Priority 2 fix]

#### Security Recommendations
- [Best practice 1]
- [Best practice 2]
```

---

## Example 6: Analytics Tools Plugin

Data analysis and visualization.

### Plugin Structure

```
analytics-tools/
├── .claude-plugin/
│   └── plugin.json
├── commands/
│   ├── data-explore.md
│   ├── query-build.md
│   └── report-generate.md
└── agents/
    └── data-analyst.md
```

### .claude-plugin/plugin.json

```json
{
  "name": "analytics-tools",
  "description": "Analytics tools: data exploration, query building, report generation",
  "version": "1.5.0",
  "author": {"name": "Data Team"},
  "license": "MIT"
}
```

### commands/data-explore.md

```markdown
---
description: Explore a dataset and generate insights
allowed-tools: Read, Bash(python3:*)
argument-hint: [file-path] (CSV, JSON, or Parquet)
---

Explore dataset: $ARGUMENTS

## Exploration Steps

1. Load and inspect data
2. Generate statistics
3. Identify patterns
4. Flag data quality issues

## Output

### Data Exploration Report

**File**: $ARGUMENTS
**Rows**: X | **Columns**: Y

#### Schema
| Column | Type | Non-Null | Unique |
|--------|------|----------|--------|
| id | int64 | 100% | 100% |
| name | string | 98% | 95% |

#### Statistics
| Column | Min | Max | Mean | Std |
|--------|-----|-----|------|-----|
| amount | 0 | 1000 | 250 | 150 |

#### Data Quality
- Missing values: 2% in `name` column
- Duplicates: 5 rows
- Outliers: 3 values > 3 std in `amount`

#### Key Insights
1. [Insight 1]
2. [Insight 2]

#### Recommended Visualizations
- Distribution of `amount`
- Time series of `created_at`
- Correlation matrix
```

### agents/data-analyst.md

```markdown
---
name: data-analyst
description: Data analysis expert. Use for data exploration, query building, statistical analysis, or generating insights. Triggers: "analyze data", "data insights", "statistics", "data exploration"
tools: Read, Bash(python3:*)
model: sonnet
---

You are a data analyst with expertise in statistical analysis.

## When Invoked

1. Understand the analysis goal
2. Explore the data:
   - Structure and types
   - Distributions
   - Relationships
3. Apply appropriate analysis:
   - Descriptive statistics
   - Correlations
   - Trends
4. Generate actionable insights

## Analysis Techniques

### Descriptive
- Summary statistics
- Distributions
- Percentiles

### Diagnostic
- Correlations
- Groupby analysis
- Time series decomposition

### Predictive
- Trend identification
- Anomaly detection
- Forecasting basics

## Output Format

### Data Analysis Report

**Objective**: [What we're analyzing]

#### Data Overview
[Summary of dataset]

#### Analysis
[Detailed findings with statistics]

#### Visualizations
[Description of recommended charts]

#### Insights
1. [Key insight with evidence]
2. [Key insight with evidence]

#### Recommendations
- [Action item based on data]
```

---

## Complete Marketplace Configuration

### marketplace.json

```json
{
  "name": "specialized-domains",
  "owner": {
    "name": "Domain Experts Community",
    "email": "domains@example.com"
  },
  "metadata": {
    "description": "Specialized tools for specific technical domains",
    "version": "3.0.0"
  },
  "plugins": [
    {
      "name": "api-designer",
      "source": {"source": "github", "repo": "domains/api-designer"},
      "description": "API design tools: OpenAPI generation, endpoint design, mocking",
      "version": "2.5.0"
    },
    {
      "name": "database-tools",
      "source": {"source": "github", "repo": "domains/database-tools"},
      "description": "Database tools: schema analysis, migrations, query optimization",
      "version": "3.0.0"
    },
    {
      "name": "frontend-tools",
      "source": {"source": "github", "repo": "domains/frontend-tools"},
      "description": "Frontend development: components, accessibility, bundle analysis",
      "version": "2.0.0"
    },
    {
      "name": "devops-tools",
      "source": {"source": "github", "repo": "domains/devops-tools"},
      "description": "DevOps utilities: infrastructure, Docker, Kubernetes",
      "version": "2.8.0"
    },
    {
      "name": "security-tools",
      "source": {"source": "github", "repo": "domains/security-tools"},
      "description": "Security tools: vulnerability scanning, secrets detection, audits",
      "version": "3.5.0"
    },
    {
      "name": "analytics-tools",
      "source": {"source": "github", "repo": "domains/analytics-tools"},
      "description": "Analytics tools: data exploration, queries, reports",
      "version": "1.5.0"
    }
  ]
}
```
