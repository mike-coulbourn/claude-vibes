# Skill Validation Checklist

Use this comprehensive checklist before finalizing any Skill to ensure it's production-ready and will be discovered properly.

---

## Pre-Creation Validation

### Requirements Clarity

- [ ] **Purpose is clear**: Can explain what the Skill does in one sentence
- [ ] **Scope is focused**: One Skill = one capability (not multiple unrelated features)
- [ ] **Target users identified**: Know who will use this (personal vs project)
- [ ] **Trigger scenarios mapped**: Can list 3+ situations when this Skill should activate

### Planning Complete

- [ ] **Structure decided**: Single-file vs multi-file determined
- [ ] **Dependencies identified**: Know what packages/tools are required
- [ ] **Tool restrictions considered**: Decided if allowed-tools is needed
- [ ] **Examples planned**: Have 2-3 concrete examples in mind

---

## YAML Frontmatter Validation

### Syntax

- [ ] **Opening delimiter**: First line is exactly `---`
- [ ] **Closing delimiter**: Line after last field is exactly `---`
- [ ] **Spacing**: Uses spaces (not tabs) for indentation
- [ ] **No trailing spaces**: No whitespace after values

### Name Field

- [ ] **Present**: Name field exists
- [ ] **Lowercase**: All letters are lowercase
- [ ] **Valid characters**: Only contains: a-z, 0-9, hyphens (-)
- [ ] **No spaces**: Uses hyphens instead of spaces
- [ ] **Length**: Under 64 characters
- [ ] **Descriptive**: Name hints at what the Skill does
- [ ] **Matches directory**: Name matches the directory name

**Test**:
```bash
# Valid names
commit-helper ✅
pdf-tools ✅
data-analyzer ✅

# Invalid names
Commit Helper ❌ (has space, uppercase)
commit_helper ❌ (underscore not allowed)
pdf-tools! ❌ (special character)
```

### Description Field

- [ ] **Present**: Description field exists
- [ ] **Under limit**: 1024 characters or less
- [ ] **Has operations**: Lists 3+ specific operations (extract, analyze, generate, etc.)
- [ ] **Has context**: Explains when to use (when working with X, during Y)
- [ ] **Has trigger terms**: Includes 5+ words/phrases users would say
- [ ] **Includes file types**: Mentions relevant extensions (.pdf, .csv, .json) if applicable
- [ ] **Includes synonyms**: Has alternative terms (PDF/document, CSV/spreadsheet)
- [ ] **No vague words**: Avoids "helps", "manages", "handles", "works with"
- [ ] **Mentions dependencies**: Notes required packages if any
- [ ] **Not generic**: Specific enough to distinguish from other Skills

**Formula check**: [Operations] + [When to use] + [Trigger terms]

### Optional Fields

- [ ] **allowed-tools** (if used):
  - Only includes valid tool names
  - Appropriate for the Skill's purpose
  - Not overly restrictive
  - Serves a security or clarity purpose

---

## Content Validation

### Instructions Section

- [ ] **Present**: Has an Instructions or How to Use section
- [ ] **Actionable**: Steps are concrete and specific (not vague guidance)
- [ ] **Ordered**: Steps are in logical sequence
- [ ] **Complete**: Covers the full workflow from start to finish
- [ ] **Clear outcomes**: States what should happen at each step

### Examples Section

- [ ] **Present**: Has at least one example
- [ ] **Concrete**: Shows actual code/commands (not pseudocode)
- [ ] **Tested**: All examples have been verified to work
- [ ] **Commented**: Complex examples have explanatory comments
- [ ] **Diverse**: Shows different use cases if applicable
- [ ] **Complete**: Examples are runnable as-is (not fragments)

### Dependencies Section

- [ ] **Listed if needed**: All required packages/tools are documented
- [ ] **Install commands**: Shows how to install dependencies
- [ ] **Prerequisites**: Lists any system requirements
- [ ] **Versions noted**: Specifies version requirements if critical

---

## Multi-File Validation (if applicable)

### File Structure

- [ ] **Logical organization**: Files are organized into appropriate directories
- [ ] **Referenced in SKILL.md**: All supporting files are mentioned in main SKILL.md
- [ ] **Relative paths**: Uses relative paths for links (e.g., `[ref](reference.md)`)
- [ ] **Consistent naming**: Files follow consistent naming conventions

### Scripts

- [ ] **Shebang lines**: Python scripts have `#!/usr/bin/env python3`
- [ ] **Executable permissions**: Scripts have execute bit set (`chmod +x`)
- [ ] **Usage docs**: Each script has usage instructions or --help
- [ ] **Error handling**: Scripts handle common errors gracefully
- [ ] **Tested**: All scripts have been run and verified

### Templates

- [ ] **Valid syntax**: Templates are syntactically correct
- [ ] **Placeholders marked**: Clear indication of what to replace ({{VARIABLE}})
- [ ] **Documentation**: Explains what each placeholder is for
- [ ] **Examples provided**: Shows completed template examples

---

## Discovery Testing

### Trigger Term Testing

Test with actual user requests that should activate the Skill:

- [ ] **Test 1**: [Exact trigger term from description]
- [ ] **Test 2**: [Synonym or alternative phrasing]
- [ ] **Test 3**: [Scenario-based request]
- [ ] **Test 4**: [File type mention if applicable]
- [ ] **Test 5**: [Operation verb from description]

**Example for PDF Skill**:
```
Test 1: "Extract text from this PDF" ✅
Test 2: "Help me with this PDF document" ✅
Test 3: "I need to merge these PDFs" ✅
Test 4: "Process this .pdf file" ✅
Test 5: "Can you extract data from PDFs" ✅
```

### False Positive Testing

Test with requests that should NOT activate this Skill:

- [ ] **Test 1**: [Similar but different domain]
- [ ] **Test 2**: [Generic request without specifics]
- [ ] **Test 3**: [Different file type/operation]

**Example for PDF Skill**:
```
Test 1: "Extract text from this Word document" ❌
Test 2: "Help me with files" ❌
Test 3: "Analyze this image" ❌
```

---

## Technical Validation

### YAML Syntax Validation

```bash
# Method 1: View first 10 lines to check YAML
head -n 10 ~/.claude/skills/your-skill/SKILL.md

# Method 2: Check for common issues
cat ~/.claude/skills/your-skill/SKILL.md | grep -E "^---|^name:|^description:"

# Method 3: Python YAML validation
python3 -c "
import yaml
with open('~/.claude/skills/your-skill/SKILL.md'.replace('~', '/Users/$(whoami)')) as f:
    content = f.read()
    parts = content.split('---')
    if len(parts) >= 2:
        yaml.safe_load(parts[1])
        print('✅ YAML is valid')
"
```

### File Permissions

```bash
# Check if scripts are executable
ls -la ~/.claude/skills/your-skill/scripts/

# Make scripts executable if needed
chmod +x ~/.claude/skills/your-skill/scripts/*.py
chmod +x ~/.claude/skills/your-skill/scripts/*.sh
```

### Character Limits

```bash
# Check description length
python3 -c "
import yaml
with open('~/.claude/skills/your-skill/SKILL.md'.replace('~', '/Users/$(whoami)')) as f:
    content = f.read()
    parts = content.split('---')
    if len(parts) >= 2:
        meta = yaml.safe_load(parts[1])
        desc_len = len(meta.get('description', ''))
        print(f'Description: {desc_len}/1024 characters')
        if desc_len > 1024:
            print('❌ Too long!')
        else:
            print('✅ Within limit')
"
```

---

## Activation Testing

### Setup

```bash
# 1. Verify Skill file exists
cat ~/.claude/skills/your-skill/SKILL.md

# 2. Restart Claude Code (REQUIRED for new Skills)
# Exit and restart your Claude Code session

# 3. Check Skills are loaded
# Ask Claude: "What Skills are available?"
```

### Testing Process

1. **Use trigger term from description**
   ```
   Ask: "[exact phrase from your description]"
   Expected: Skill activates
   ```

2. **Use natural phrasing**
   ```
   Ask: "[how a user would naturally ask]"
   Expected: Skill activates
   ```

3. **Test edge cases**
   ```
   Ask: "[similar but not exact match]"
   Expected: Decide if it should activate or not
   ```

4. **Verify instructions are followed**
   ```
   Observe: Does Claude follow the instructions correctly?
   Expected: Yes, steps are executed in order
   ```

### Debug if Skill Doesn't Activate

1. **Check loading**:
   ```bash
   claude --debug
   # Look for: "Loaded skill: your-skill-name"
   ```

2. **Review description**:
   - Is it specific enough?
   - Does it include the exact words you're using?
   - Are there trigger terms present?

3. **Check YAML syntax**:
   - Missing `---` delimiters?
   - Tabs instead of spaces?
   - Unquoted strings with special characters?

4. **Verify file location**:
   ```bash
   ls ~/.claude/skills/your-skill/SKILL.md
   # or
   ls .claude/skills/your-skill/SKILL.md
   ```

---

## Quality Validation

### Clarity

- [ ] **Beginner-friendly**: Someone new could follow the instructions
- [ ] **No jargon**: Technical terms are defined when first used
- [ ] **Consistent terminology**: Same concepts use same terms throughout
- [ ] **No ambiguity**: Instructions have one clear interpretation

### Completeness

- [ ] **Covers common cases**: Addresses typical usage scenarios
- [ ] **Handles errors**: Mentions what to do when things go wrong
- [ ] **Shows alternatives**: Provides options when multiple approaches exist
- [ ] **Edge cases noted**: Calls out limitations or special cases

### Maintainability

- [ ] **Versioned**: Has a version number or date if likely to change
- [ ] **Ownership clear**: Team knows who maintains this (for project Skills)
- [ ] **Dependencies pinned**: Specifies versions if compatibility matters
- [ ] **Update process**: Clear how to update the Skill

---

## Documentation Validation

### README or Comments

- [ ] **Purpose stated**: First few lines explain what this does
- [ ] **Quick start present**: Shows simplest usage immediately
- [ ] **Examples working**: All code examples have been tested
- [ ] **Links valid**: All references and links work

### Code Quality (for scripts)

- [ ] **Readable**: Code is clean and understandable
- [ ] **Commented**: Complex logic has explanatory comments
- [ ] **Error handling**: Catches and handles common errors
- [ ] **Exit codes**: Scripts return appropriate exit codes

---

## Team Readiness (for project Skills)

### Collaboration

- [ ] **Team reviewed**: At least one other person has reviewed the Skill
- [ ] **Naming discussed**: Team agrees on name and purpose
- [ ] **No conflicts**: Doesn't overlap with existing Skills
- [ ] **Git ready**: Ready to commit (no secrets, credentials, or local paths)

### Documentation

- [ ] **Mentioned in project docs**: Added to project CLAUDE.md or Skills README
- [ ] **Usage examples**: Team knows how to trigger it
- [ ] **Contact info**: Team knows who to ask about this Skill

---

## Final Checklist

Before marking a Skill as complete:

- [ ] All YAML validation checks pass
- [ ] All content validation checks pass
- [ ] Description follows the formula
- [ ] At least 3 trigger term tests pass
- [ ] Skill activates when expected
- [ ] Instructions are followed correctly by Claude
- [ ] All examples work
- [ ] All scripts are executable and tested
- [ ] Dependencies are documented
- [ ] No secrets or credentials in files
- [ ] Ready to share (if project Skill)

---

## Quick Validation Command

Create this script for rapid validation:

```bash
#!/bin/bash
# validate-skill.sh

SKILL_PATH="$1"

echo "🔍 Validating Skill: $SKILL_PATH"
echo ""

# Check file exists
if [ ! -f "$SKILL_PATH/SKILL.md" ]; then
  echo "❌ SKILL.md not found"
  exit 1
fi

echo "✅ SKILL.md exists"

# Check YAML delimiters
if ! head -n 1 "$SKILL_PATH/SKILL.md" | grep -q "^---$"; then
  echo "❌ Missing opening ---"
  exit 1
fi
echo "✅ Has opening ---"

# Check required fields
if ! grep -q "^name:" "$SKILL_PATH/SKILL.md"; then
  echo "❌ Missing name field"
  exit 1
fi
echo "✅ Has name field"

if ! grep -q "^description:" "$SKILL_PATH/SKILL.md"; then
  echo "❌ Missing description field"
  exit 1
fi
echo "✅ Has description field"

# Check description length
DESC_LEN=$(python3 -c "
import yaml
with open('$SKILL_PATH/SKILL.md') as f:
    parts = f.read().split('---')
    if len(parts) >= 2:
        meta = yaml.safe_load(parts[1])
        print(len(meta.get('description', '')))
")

if [ "$DESC_LEN" -gt 1024 ]; then
  echo "❌ Description too long: $DESC_LEN/1024"
  exit 1
fi
echo "✅ Description length OK: $DESC_LEN/1024"

echo ""
echo "✅ Basic validation passed!"
echo "📝 Manual checks still needed:"
echo "   - Test trigger terms"
echo "   - Verify examples work"
echo "   - Check scripts are executable"
```

Usage:
```bash
chmod +x validate-skill.sh
./validate-skill.sh ~/.claude/skills/your-skill
```

---

## Remember

- **YAML syntax** is the #1 cause of Skill loading failures
- **Description specificity** is the #1 cause of activation failures
- **Testing** is the only way to know if your Skill works
- **Iteration** is normal - refine based on actual usage

Use this checklist every time. It catches issues before they become problems.
