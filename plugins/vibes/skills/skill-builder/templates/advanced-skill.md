# Advanced Multi-File Skill Template

Use this template for complex Skills that need scripts, extensive documentation, templates, or utility files.

## When to use this template

- Instructions too extensive for one file
- Scripts or utilities required
- Templates or boilerplate needed
- Detailed API/reference documentation
- Multiple related workflows

---

## Directory Structure

```
skill-name/
├── SKILL.md           # Core instructions (always loaded first)
├── reference.md       # Detailed API/reference (loaded when needed)
├── examples.md        # Additional examples (loaded when needed)
├── scripts/           # Utility scripts
│   ├── helper.py
│   ├── process.sh
│   └── validate.py
└── templates/         # Template files
    ├── config.json
    └── boilerplate.txt
```

---

## File 1: SKILL.md (Main entry point)

```yaml
---
name: skill-name
description: [What it does] + [When to use it] + [Trigger terms]. Include any required packages here too.
allowed-tools: Read, Grep, Glob  # Optional: only if restricting tools
---

# Skill Name

Brief overview of what this Skill provides.

## Quick Start

Show the simplest, most common operation:

```language
# Minimal working example
```

## Core Operations

### Operation 1: [Name]

```language
# Example for operation 1
```

### Operation 2: [Name]

```language
# Example for operation 2
```

## Advanced Usage

For detailed API reference, see [reference.md](reference.md).

For more examples, see [examples.md](examples.md).

## Utility Scripts

Helper script for batch processing:
```bash
python scripts/helper.py input.txt --option value
```

Validation script:
```bash
python scripts/validate.py config.json
```

## Templates

Use the provided templates for common scenarios:
- `templates/config.json` - Configuration template
- `templates/boilerplate.txt` - Boilerplate code

## Requirements

Install required packages:
```bash
pip install package1 package2
```

Prerequisites:
- Prerequisite 1
- Prerequisite 2
```

---

## File 2: reference.md (Detailed documentation)

```markdown
# [Skill Name] Reference

Complete API reference and detailed documentation.

## Table of Contents

1. [Core Concepts](#core-concepts)
2. [API Reference](#api-reference)
3. [Configuration](#configuration)
4. [Troubleshooting](#troubleshooting)

## Core Concepts

Explain fundamental concepts users need to understand.

### Concept 1

Detailed explanation of concept 1.

### Concept 2

Detailed explanation of concept 2.

## API Reference

### Function 1

```language
function_name(param1, param2, option=default)
```

**Parameters**:
- `param1` (type): Description
- `param2` (type): Description
- `option` (type, optional): Description. Default: `default`

**Returns**: Description of return value

**Example**:
```language
# Usage example
result = function_name("value1", "value2")
```

### Function 2

[Similar structure]

## Configuration

### Configuration Options

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| option1 | string | "default" | What it does |
| option2 | number | 100 | What it does |

### Configuration File Format

```json
{
  "option1": "value",
  "option2": 100
}
```

## Troubleshooting

### Issue: [Common problem]

**Symptoms**: Description of symptoms

**Cause**: Why it happens

**Solution**: How to fix it

### Issue: [Another problem]

[Similar structure]
```

---

## File 3: examples.md (Additional examples)

```markdown
# [Skill Name] Examples

Real-world examples and use cases.

## Example 1: [Scenario Name]

**Context**: When you need to [scenario description]

**Code**:
```language
# Complete working example
# with multiple steps
# showing real usage
```

**Output**:
```
Expected output here
```

**Explanation**: Why this approach works and when to use it.

## Example 2: [Another Scenario]

[Similar structure]

## Example 3: [Complex Scenario]

**Context**: Advanced usage showing [what it demonstrates]

**Setup**:
```bash
# Any setup commands needed
```

**Code**:
```language
# Complex example
# demonstrating advanced features
```

**Best Practices**:
- Key principle from this example
- Important consideration
- Pitfall to avoid

## Common Patterns

### Pattern 1: [Pattern name]

Used when [context for this pattern]

```language
# Pattern implementation
```

### Pattern 2: [Another pattern]

[Similar structure]
```

---

## File 4: scripts/helper.py (Utility script)

```python
#!/usr/bin/env python3
"""
Helper script for [what it does]

Usage:
    python helper.py <input> [options]

Options:
    --option1    Description of option1
    --option2    Description of option2
"""

import sys
import argparse

def main():
    """Main function"""
    parser = argparse.ArgumentParser(description="Helper script for [purpose]")
    parser.add_argument("input", help="Input file or value")
    parser.add_argument("--option1", default="default", help="Option 1 description")
    parser.add_argument("--option2", type=int, default=100, help="Option 2 description")

    args = parser.parse_args()

    # Implementation
    result = process_input(args.input, args.option1, args.option2)
    print(result)

def process_input(input_val, option1, option2):
    """Process the input with given options"""
    # Implementation here
    return f"Processed: {input_val}"

if __name__ == "__main__":
    main()
```

---

## File 5: scripts/validate.py (Validation script)

```python
#!/usr/bin/env python3
"""
Validation script for [what it validates]

Usage:
    python validate.py <config_file>
"""

import sys
import json

def validate_config(config_path):
    """Validate configuration file"""
    try:
        with open(config_path, 'r') as f:
            config = json.load(f)

        # Validation checks
        required_keys = ['option1', 'option2']
        for key in required_keys:
            if key not in config:
                print(f"❌ Missing required key: {key}")
                return False

        # Type checking
        if not isinstance(config['option1'], str):
            print(f"❌ option1 must be a string")
            return False

        print("✅ Configuration is valid")
        return True

    except json.JSONDecodeError as e:
        print(f"❌ Invalid JSON: {e}")
        return False
    except FileNotFoundError:
        print(f"❌ File not found: {config_path}")
        return False

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python validate.py <config_file>")
        sys.exit(1)

    valid = validate_config(sys.argv[1])
    sys.exit(0 if valid else 1)
```

---

## File 6: templates/config.json (Configuration template)

```json
{
  "option1": "default_value",
  "option2": 100,
  "option3": {
    "nested": "value"
  },
  "list_option": [
    "item1",
    "item2"
  ]
}
```

---

## File 7: templates/boilerplate.txt (Code template)

```
# Boilerplate template for [what it's used for]

[Template content with placeholders]

{{PLACEHOLDER_1}} - Description of what goes here
{{PLACEHOLDER_2}} - Description of what goes here

[More template content]
```

---

## Real Example: PDF Processing Skill

Here's a complete working example of a multi-file Skill:

### Structure
```
pdf-tools/
├── SKILL.md
├── reference.md
├── examples.md
└── scripts/
    ├── extract_text.py
    └── merge_pdfs.py
```

### SKILL.md
````yaml
---
name: pdf-tools
description: Extract text, tables, and metadata from PDF files. Merge, split, and manipulate PDFs. Use when working with PDF files, forms, or document extraction. Requires pypdf and pdfplumber packages.
---

# PDF Tools

Process PDF files: extract text/tables, merge documents, manipulate pages.

## Quick Start

Extract text from a PDF:

```python
import pdfplumber
with pdfplumber.open("document.pdf") as pdf:
    text = pdf.pages[0].extract_text()
    print(text)
```

## Core Operations

### Extract Text

```python
import pdfplumber
with pdfplumber.open("doc.pdf") as pdf:
    for page in pdf.pages:
        text = page.extract_text()
```

### Extract Tables

```python
with pdfplumber.open("report.pdf") as pdf:
    table = pdf.pages[0].extract_table()
```

### Merge PDFs

```python
from pypdf import PdfWriter
merger = PdfWriter()
for pdf in ["file1.pdf", "file2.pdf"]:
    merger.append(pdf)
merger.write("merged.pdf")
merger.close()
```

## Advanced Usage

For complete API reference, see [reference.md](reference.md).

For real-world examples, see [examples.md](examples.md).

## Utility Scripts

Batch text extraction:
```bash
python scripts/extract_text.py document.pdf
```

Merge multiple PDFs:
```bash
python scripts/merge_pdfs.py output.pdf file1.pdf file2.pdf file3.pdf
```

## Requirements

```bash
pip install pypdf pdfplumber
```
````

---

## Tips for Multi-File Skills

1. **Keep SKILL.md focused** - quick start and common operations only
2. **Progressive detail** - reference.md for deep dives
3. **Make scripts standalone** - they should work independently
4. **Document script usage** - show exact commands in SKILL.md
5. **Reference supporting files** - use relative links `[text](reference.md)`
6. **Make scripts executable** - `chmod +x scripts/*.py`
7. **Add shebang lines** - `#!/usr/bin/env python3` at top of scripts
8. **Validate templates** - ensure templates are syntactically correct
9. **Test all files** - verify every example and script works
10. **Keep structure consistent** - same patterns across similar Skills
