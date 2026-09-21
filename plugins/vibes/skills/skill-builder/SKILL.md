---
name: skill-builder
description: Create new Skills for Claude Code including YAML frontmatter, descriptions, instructions, and structure. Use when creating, building, or designing skills, or when asked about skill creation, structure, best practices, or debugging skills that don't activate properly.
---

# Skill Builder

Build production-quality Skills for Claude Code with proper structure, discoverable descriptions, and best practices.

## Quick Reference

**Description Formula**: `[What it does] + [When to use it] + [Trigger terms users say]`

**Name Rules**: Lowercase letters, numbers, hyphens only; max 64 characters; no spaces

**Description Rules**: Keep it under 1024 characters (the Agent Skills spec limit, which keeps the skill portable). Claude Code truncates the combined `description` and `when_to_use` at 1,536 characters in its listing, so put the key use case first. Say when to use the skill and include the words users actually type. Do not summarize the skill's workflow, because Claude may follow the summary and skip the body.

**Frontmatter fields** (all optional in Claude Code; `name` defaults to the directory name):

| Field | Purpose |
|-------|---------|
| `description`, `when_to_use` | Discovery text. `when_to_use` is appended to `description` |
| `argument-hint`, `arguments` | Autocomplete hint, and named arguments for `$name` substitution |
| `disable-model-invocation` | `true` means only the user can run it as `/name`. Use for anything with side effects, such as deploy or commit |
| `user-invocable` | `false` hides it from the `/` menu so only Claude invokes it. Use for background knowledge |
| `allowed-tools` | Tools Claude may use **without a permission prompt** while the skill runs. It pre-approves; it does not restrict |
| `disallowed-tools` | Tools removed from Claude's pool while the skill is active. This is the field that restricts |
| `model`, `effort` | Model and effort override for the current turn |
| `context`, `agent`, `background` | `context: fork` runs the skill in a subagent, and `agent` picks the subagent type |
| `paths` | Glob patterns; the skill auto-loads only when Claude works with matching files |
| `hooks`, `shell` | Hooks registered on invocation, and the shell used for bash injection |
| `license`, `compatibility`, `metadata` | Agent Skills spec fields. Claude Code accepts them and does not act on them |

**Substitutions in the body**: `$ARGUMENTS`, `$0` and `$1` (0-based, so `$0` is the first argument), `$name` for declared arguments, `${CLAUDE_SKILL_DIR}` for bundled scripts, `${CLAUDE_PROJECT_DIR}`, `${CLAUDE_SESSION_ID}`, and in plugin skills `${CLAUDE_PLUGIN_ROOT}` and `${CLAUDE_PLUGIN_DATA}`.

**Skills are also commands.** Every skill can be run as `/skill-name`, or `/plugin-name:skill-name` from a plugin, and `.claude/commands/*.md` files are the older form of the same thing.

Source: https://code.claude.com/docs/en/skills#frontmatter-reference (last verified September 2026).

## The Skill Creation Workflow

### Phase 1: Requirements Gathering

Use AskUserQuestion to understand what they need:

1. **What should the Skill do?**
   - What capability or expertise should it provide?
   - What tasks should it help with?

2. **When should it activate?**
   - What scenarios or contexts?
   - What words/phrases would users say?
   - What file types or operations?

3. **Scope decision**
   - Personal Skill (~/.claude/skills/) - just for this user
   - Project Skill (.claude/skills/) - shared with team via git

4. **Structure complexity**
   - Single file (simple instructions/examples)
   - Multi-file (scripts, templates, extensive docs)

5. **Tool permissions**
   - Default (Claude asks permission as usual)
   - Pre-approve the tools the skill needs with `allowed-tools`, so it runs without prompts
   - Remove tools the skill must never use with `disallowed-tools`

6. **Who invokes it**
   - Claude and the user (default)
   - User only (`disable-model-invocation: true`), for workflows with side effects
   - Claude only (`user-invocable: false`), for background knowledge

### Phase 2: Description Crafting

The description determines discoverability. Use this proven formula:

```
[Specific operations] + [When to use] + [Trigger terms]
```

**Example walkthrough**:
- ❌ "Helps with documents" (too vague)
- ✅ "Extract text and tables from PDF files, fill forms, merge documents. Use when working with PDF files or when user mentions PDFs, forms, or document extraction."

**Key elements**:
1. **Specific operations**: List concrete actions (extract, analyze, generate, validate)
2. **When to use**: Scenarios and contexts (when working with X, during Y, for Z tasks)
3. **Trigger terms**: Exact words users would say (PDF, forms, commit message, data analysis)

See [examples/descriptions.md](examples/descriptions.md) for more patterns.

### Phase 3: Name Validation

Validate and format the name:

- Convert to lowercase
- Replace spaces with hyphens
- Remove invalid characters (only allow: a-z, 0-9, -)
- Ensure max 64 characters
- Make it descriptive but concise

**Examples**:
- "My PDF Tool" → "my-pdf-tool"
- "Code Reviewer!!!" → "code-reviewer"
- "data_analysis" → "data-analysis"

### Phase 4: Structure Planning

**Single file** when:
- Instructions and examples fit comfortably in one file
- No scripts or utilities needed
- Straightforward workflow

**Multi-file** when:
- Extensive documentation (split into reference.md)
- Scripts or utilities needed (scripts/ directory)
- Templates or boilerplate (templates/ directory)
- Many examples (examples.md)

Recommended structure for complex Skills:
```
skill-name/
├── SKILL.md           # Core instructions (loaded first)
├── reference.md       # Detailed API/reference (loaded if needed)
├── examples.md        # Additional examples (loaded if needed)
├── scripts/           # Utility scripts
│   ├── helper.py
│   └── process.sh
└── templates/         # Template files
    └── template.txt
```

### Phase 5: Implementation

#### Create the directory

```bash
# Personal Skill
mkdir -p ~/.claude/skills/skill-name

# Project Skill
mkdir -p .claude/skills/skill-name

# Multi-file structure
mkdir -p ~/.claude/skills/skill-name/{templates,scripts,examples}
```

#### Write SKILL.md

Template structure:

```yaml
---
name: skill-name
description: [Use the formula from Phase 2]
allowed-tools: Read, Grep, Glob  # Optional: pre-approves these tools, no permission prompt
---

# Skill Name

Brief introduction explaining what this Skill does.

## Quick Start

Provide the most common use case with a concrete example.

## Instructions

Step-by-step guidance for Claude:

1. [First step with specific actions]
2. [Second step with expected behavior]
3. [Continue pattern]

## Examples

Show concrete code examples:

```language
# Example code that demonstrates usage
```

## Best Practices

- Key principle or pattern
- Important consideration
- Common pitfall to avoid

## Requirements

List any dependencies:
```bash
pip install required-package
```
```

#### Add supporting files if multi-file

Reference from SKILL.md:
```markdown
For detailed API reference, see [reference.md](reference.md).

Use the helper script:
```bash
python scripts/helper.py input.txt
```
```

### Phase 6: Validation

Before finalizing, check:

- [ ] Description follows formula (what + when + triggers)
- [ ] Description under 1024 characters
- [ ] Name is lowercase-with-hyphens, under 64 chars
- [ ] YAML has opening and closing `---`
- [ ] YAML uses spaces not tabs
- [ ] Instructions are clear and actionable
- [ ] Examples are concrete and tested
- [ ] Dependencies are documented
- [ ] `allowed-tools` pre-approves only what the skill needs, and `disallowed-tools` covers anything it must never use

See [reference/validation-checklist.md](reference/validation-checklist.md) for complete checklist.

### Phase 7: Testing

1. **Restart Claude Code** (required for Skills to load)

2. **Test discovery**:
   - Ask using trigger terms from your description
   - Verify Skill activates automatically
   - Try variations of trigger phrases

3. **Test workflow**:
   - Follow instructions as Claude
   - Verify all examples work
   - Check edge cases

4. **Debug if needed**:
   ```bash
   # Check Skill was loaded
   # Ask: "What Skills are available?"

   # View Skill file
   cat ~/.claude/skills/skill-name/SKILL.md

   # Check for YAML syntax errors
   claude --debug
   ```

## Common Issues and Solutions

### Issue: Skill doesn't activate

**Causes**:
1. Description too vague
2. Trigger terms don't match user's words
3. YAML syntax error
4. Didn't restart Claude Code

**Solutions**:
1. Make description more specific with exact trigger terms
2. Add more synonyms and related terms
3. Validate YAML (check --- delimiters, spaces not tabs)
4. Restart Claude Code

### Issue: Skill activates when it shouldn't

**Causes**:
1. Description too broad
2. Overlapping with other Skills

**Solutions**:
1. Narrow description scope
2. Add specific context (file types, operations)
3. Consider splitting into focused Skills

### Issue: YAML syntax errors

**Common mistakes**:
- Missing opening `---` (line 1)
- Missing closing `---` (before Markdown content)
- Using tabs instead of spaces
- Unquoted strings with special characters

**Fix**:
```yaml
---
name: skill-name
description: Description text here
---

# Markdown starts here
```

## Iteration and Improvement

After using a Skill, improve it:

1. **Track activation patterns**: Does it activate when expected?
2. **Gather feedback**: What's confusing or missing?
3. **Refine description**: Add trigger terms from actual usage
4. **Expand examples**: Add real scenarios encountered
5. **Update instructions**: Clarify ambiguous steps

## Educational Principles

When creating Skills, remember:

**Why descriptions matter**: Claude uses them for discovery. Vague descriptions = never activated.

**Why multi-file structure works**: Progressive loading. Claude reads SKILL.md first, supporting files only when needed. Keeps context focused.

**Why tool fields need care**: `allowed-tools` grants permission, it does not take any away. A skill listing `Read, Grep, Glob` can still edit files; Claude just has to ask first. To guarantee a read-only skill, list the write tools in `disallowed-tools`.

**Why trigger terms are crucial**: Users don't know your Skill exists. They ask questions naturally. Trigger terms bridge their words to your Skill.

## Quick Templates

Basic Skill template: [templates/basic-skill.md](templates/basic-skill.md)

Advanced multi-file template: [templates/advanced-skill.md](templates/advanced-skill.md)

Description examples: [examples/descriptions.md](examples/descriptions.md)

## Tips for Great Skills

1. **Be specific in descriptions** - exact operations, file types, scenarios
2. **Include trigger synonyms** - users say things differently
3. **Start simple, expand later** - single file first, add complexity when needed
4. **Test with real requests** - use actual words users would say
5. **Document dependencies clearly** - don't assume packages are installed
6. **Provide concrete examples** - show don't tell
7. **Make instructions actionable** - specific steps, not vague guidance
8. **Consider scope carefully** - personal for experimentation, project for team
9. **Use tool fields deliberately** - `allowed-tools` to cut permission prompts, `disallowed-tools` to make analysis and review skills truly read-only
10. **Iterate based on usage** - refine trigger terms from real activation patterns

## Next Steps

After creating a Skill:

1. Share with team (if project Skill, commit to git)
2. Document in project CLAUDE.md if it's a pattern others should know
3. Create related Skills for connected workflows
4. Consider packaging multiple Skills as a plugin for wider distribution

---

**Remember**: Great Skills have specific descriptions with trigger terms. That's the difference between a Skill that gets used and one that never activates.
