# Skill Description Examples

Great descriptions determine whether your Skill gets used. This guide shows proven patterns with real before/after examples.

## The Description Formula

```
[Specific operations] + [When to use it] + [Trigger terms users say]
```

Each component is critical for discovery.

---

## Component 1: Specific Operations

**What it does**: List concrete actions and capabilities.

### ❌ Vague Operations
- "Helps with files"
- "Works with data"
- "Manages documents"
- "Handles code"

### ✅ Specific Operations
- "Extract text and tables from PDF files, fill forms, merge documents"
- "Analyze CSV data, generate statistics, create pivot tables, export reports"
- "Review code for security issues, performance problems, and best practices"
- "Generate commit messages, validate branch names, create PR descriptions"

**Why it works**: Specific operations give Claude clear matching criteria. "Extract text from PDF" matches when users mention extraction or PDFs.

---

## Component 2: When to Use It

**Context**: Scenarios, file types, and situations where the Skill applies.

### ❌ Missing Context
- "Extract text from PDF files"
- "Analyze data and generate reports"
- "Review code quality"

### ✅ Clear Context
- "Extract text from PDF files. Use when working with PDF documents or forms"
- "Analyze CSV data and generate reports. Use during data analysis or when examining spreadsheets"
- "Review code quality. Use when reviewing pull requests, checking code before commits, or auditing codebases"

**Why it works**: Context helps Claude understand situations. "When working with PDF documents" matches document-related requests.

---

## Component 3: Trigger Terms

**Discovery**: Exact words and phrases users would naturally say.

### ❌ Missing Trigger Terms
- "Process documents. Use for document work"
- "Analyze information. Use for analysis tasks"

### ✅ Rich Trigger Terms
- "Process PDF documents. Use when working with PDFs, forms, document extraction, or file merging"
- "Analyze CSV data. Use when working with spreadsheets, Excel files, data analysis, statistics, or tabular data"

**Why it works**: Users don't know your Skill exists. They ask naturally: "Can you help me with this Excel file?" Trigger terms bridge their language to your Skill.

---

## Real-World Examples: Before and After

### Example 1: PDF Processing

#### ❌ Bad Description
```yaml
description: Helps with documents
```

**Problems**:
- "Helps" is vague (helps how?)
- "Documents" is too broad (what kind?)
- No trigger terms
- No operations listed
- No context provided

**Result**: Never activates because Claude can't tell when to use it.

#### ✅ Good Description
```yaml
description: Extract text and tables from PDF files, fill forms, merge documents. Use when working with PDF files, forms, or document extraction. Requires pdfplumber and pypdf packages.
```

**What improved**:
- ✅ Specific operations: extract, fill, merge
- ✅ Clear context: PDF files, forms
- ✅ Trigger terms: PDF, forms, document extraction
- ✅ Bonus: Dependencies mentioned upfront

**Result**: Activates for "help me extract text from this PDF" or "I need to merge these PDFs".

---

### Example 2: Data Analysis

#### ❌ Bad Description
```yaml
description: Works with data files
```

**Problems**:
- "Works with" is vague
- "Data files" could be anything
- No specific operations
- No file types mentioned
- No trigger terms

#### ✅ Good Description
```yaml
description: Analyze CSV and Excel files, generate statistics, create pivot tables, visualize trends. Use when working with spreadsheets, tabular data, or performing data analysis. Mentions of CSV, Excel, .xlsx, or data analysis tasks.
```

**What improved**:
- ✅ Specific operations: analyze, generate statistics, create pivot tables, visualize
- ✅ File types: CSV, Excel
- ✅ Clear context: spreadsheets, tabular data
- ✅ Trigger terms: CSV, Excel, .xlsx, data analysis

**Result**: Activates for "can you analyze this Excel file" or "I need statistics from this CSV".

---

### Example 3: Code Review

#### ❌ Bad Description
```yaml
description: Reviews code
```

**Problems**:
- Too minimal
- No review criteria mentioned
- No context (when to use)
- No trigger terms

#### ✅ Good Description
```yaml
description: Review code for security vulnerabilities, performance issues, maintainability problems, and test coverage. Use when reviewing pull requests, checking code quality, or conducting code audits before merging or deploying.
```

**What improved**:
- ✅ Specific operations: review for security, performance, maintainability, tests
- ✅ Clear context: PR reviews, before merging/deploying
- ✅ Trigger terms: pull requests, code quality, code audits, merging, deploying

**Result**: Activates for "can you review this PR" or "check this code before I merge".

---

### Example 4: Git Commits

#### ❌ Bad Description
```yaml
description: Helps with git
```

**Problems**:
- "Git" is too broad (which git operations?)
- No specific operations
- No context
- No trigger terms

#### ✅ Good Description
```yaml
description: Generate conventional commit messages from git diffs following best practices. Use when writing commits, reviewing staged changes, or needing commit message suggestions. Mentions of commits, git messages, or conventional commits.
```

**What improved**:
- ✅ Specific operation: generate commit messages
- ✅ Format mentioned: conventional commits
- ✅ Clear context: writing commits, staged changes
- ✅ Trigger terms: commits, git messages, conventional commits

**Result**: Activates for "help me write a commit message" or "I need a commit for these changes".

---

### Example 5: API Testing

#### ❌ Bad Description
```yaml
description: Tests APIs
```

**Problems**:
- Too minimal
- No testing approach mentioned
- No context
- Missing trigger terms

#### ✅ Good Description
```yaml
description: Test REST APIs including endpoints, authentication, request/response validation, error handling, and performance. Use when testing API endpoints, debugging API issues, or validating API behavior. Mentions of REST, API testing, endpoints, or HTTP requests.
```

**What improved**:
- ✅ API type: REST
- ✅ Specific tests: auth, validation, error handling, performance
- ✅ Context: testing endpoints, debugging
- ✅ Trigger terms: REST, API testing, endpoints, HTTP requests

**Result**: Activates for "test this REST API" or "help me validate these endpoints".

---

## Industry-Specific Examples

### DevOps/Infrastructure

```yaml
description: Manage Kubernetes deployments, troubleshoot pods, review manifests, scale resources. Use when working with K8s, kubectl, deployments, or container orchestration. Mentions of Kubernetes, K8s, pods, deployments, or containers.
```

### Web Development

```yaml
description: Build React components, optimize rendering, manage state with hooks, debug React applications. Use when developing React apps, debugging components, or optimizing React performance. Mentions of React, JSX, components, hooks, or useState/useEffect.
```

### Data Science

```yaml
description: Build machine learning models with scikit-learn, preprocess data, evaluate models, tune hyperparameters. Use for ML tasks, model training, or data preprocessing. Mentions of machine learning, ML, sklearn, scikit-learn, models, or training.
```

### Database Operations

```yaml
description: Write and optimize SQL queries, design schemas, debug query performance, explain query plans. Use when working with databases, writing SQL, or optimizing queries. Mentions of SQL, PostgreSQL, MySQL, queries, database, or schema.
```

---

## Pattern Library

### Pattern: File Processing

```yaml
description: [Process/Parse/Convert] [FileType] files, [operation1], [operation2]. Use when working with [FileType] files or [related context]. Mentions of [FileType], [synonym1], [synonym2].
```

**Example**:
```yaml
description: Parse and validate JSON files, format JSON, convert between JSON and YAML. Use when working with JSON configuration files or API responses. Mentions of JSON, .json files, API responses, or config files.
```

### Pattern: Code Operations

```yaml
description: [Operation] [Language] code for [criteria1], [criteria2], [criteria3]. Use when [context]. Mentions of [keywords].
```

**Example**:
```yaml
description: Review Python code for PEP 8 compliance, type hints, docstrings, and best practices. Use when reviewing Python code or preparing for code review. Mentions of Python, .py files, code review, or PEP 8.
```

### Pattern: Analysis/Report Generation

```yaml
description: Analyze [DataType], generate [output1], create [output2]. Use when [context]. Mentions of [DataType], [relatedTerms].
```

**Example**:
```yaml
description: Analyze log files, identify errors, generate incident reports, track patterns over time. Use when troubleshooting issues, investigating incidents, or analyzing system logs. Mentions of logs, errors, incidents, or troubleshooting.
```

---

## Testing Your Description

Use this checklist to validate your description:

### ✅ Checklist

- [ ] **Under 1024 characters** (hard limit)
- [ ] **Lists 3+ specific operations** (what it does)
- [ ] **Includes clear context** (when to use)
- [ ] **Has 5+ trigger terms** (words users say)
- [ ] **Mentions file types if relevant** (.pdf, .csv, .json)
- [ ] **Includes synonyms** (PDF/document, CSV/spreadsheet)
- [ ] **No vague words** (helps, manages, handles, works with)
- [ ] **No jargon without context** (define or explain)
- [ ] **Dependencies mentioned** (if requires packages)
- [ ] **Test with real questions** (would this activate?)

### Test Questions

Ask yourself: Would this description match these user requests?

**For PDF Skill**:
- "Extract text from this PDF" ✅
- "Help me with this document" ✅
- "Process these forms" ✅
- "I need to work with files" ❌ (too vague, other Skills might match better)

**For Data Skill**:
- "Analyze this Excel file" ✅
- "Generate statistics from CSV" ✅
- "I have a spreadsheet to process" ✅
- "Help me with data" ❌ (too vague, need more context)

---

## Common Mistakes and Fixes

### Mistake 1: Too Generic

❌ **Bad**: "Helps with documents and files"

✅ **Fix**: "Extract text from PDF documents, convert DOCX to plain text, merge document files. Use when working with PDF or Word documents. Mentions of PDF, DOCX, documents, or file conversion."

**Why**: Specific operations and file types enable matching.

### Mistake 2: Missing Trigger Terms

❌ **Bad**: "Process spreadsheets and create reports"

✅ **Fix**: "Process Excel and CSV spreadsheets, generate statistical reports, create visualizations. Use when working with spreadsheets, tabular data, or data analysis. Mentions of Excel, CSV, .xlsx, spreadsheets, or data analysis."

**Why**: Users say "Excel" not "spreadsheets" - include both terms.

### Mistake 3: No Context

❌ **Bad**: "Review code quality and suggest improvements"

✅ **Fix**: "Review code quality and suggest improvements for security, performance, maintainability. Use when reviewing pull requests, auditing code before releases, or checking code quality. Mentions of code review, PR review, code quality, or audit."

**Why**: Context tells Claude when this applies in the workflow.

### Mistake 4: Vague Operations

❌ **Bad**: "Manages API operations"

✅ **Fix**: "Test REST API endpoints, validate request/response formats, check authentication, measure response times. Use when testing APIs, debugging endpoints, or validating API behavior. Mentions of REST API, endpoints, HTTP requests, or API testing."

**Why**: "Test", "validate", "check", "measure" are concrete actions.

### Mistake 5: Too Broad Scope

❌ **Bad**: "Helps with development tasks, testing, deployment, monitoring, and troubleshooting across all languages and frameworks"

✅ **Fix**: Split into focused Skills:
- Skill 1: "Test Python code with pytest..."
- Skill 2: "Deploy to Kubernetes..."
- Skill 3: "Monitor application logs..."

**Why**: One broad Skill = confusion. Multiple focused Skills = clear discovery.

---

## Length Management

If your description exceeds 1024 characters:

### Strategy 1: Remove Redundancy

❌ **Too long**: "Extract text from PDF files, extract tables from PDF documents, extract images from PDFs, fill PDF forms, merge PDF documents, split PDF files..."

✅ **Concise**: "Extract text, tables, and images from PDF files. Fill forms, merge, and split documents. Use when working with PDFs or forms. Requires pypdf."

### Strategy 2: Prioritize Core Operations

❌ **Too long**: Lists 15 operations

✅ **Focused**: List 3-5 most important operations, mention "and more" if needed

### Strategy 3: Abbreviate Common Terms

- "and" → "&"
- "Use when working with" → "Use for"
- "Mentions of" → Can be implicit in trigger terms list

---

## Master Template

Use this as your starting point:

```yaml
description: [Action1], [action2], [action3] for [FileType/Domain]. [Additional capabilities]. Use when [scenario1], [scenario2], or [scenario3]. [Trigger terms]: [term1], [term2], [term3], [term4], [term5]. [Dependencies if needed].
```

**Example filled in**:
```yaml
description: Extract, validate, and transform JSON data. Convert between JSON/YAML/XML formats. Use when working with API responses, config files, or data transformation. JSON, .json, YAML, XML, API responses, configuration. Requires pyyaml.
```

---

**Remember**: The description is the single most important field in your Skill. Spend time crafting it. Test it with real requests. Iterate based on whether it activates when expected.
