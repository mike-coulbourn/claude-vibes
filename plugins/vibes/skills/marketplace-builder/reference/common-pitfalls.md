# Common Marketplace Pitfalls

Read this before finalizing a marketplace, or when an install fails.

## 1. Confusing Marketplace with Plugin

**Wrong**: Thinking marketplace.json IS the plugin
**Right**: marketplace.json POINTS TO plugins

marketplace.json is a catalog. The actual plugin code lives in separate directories or repos.

## 2. Wrong Source Type

**Wrong**: Using GitHub shorthand for private repos
```json
{"source": "github", "repo": "private-org/private-repo"}  // May fail
```

**Right**: Use git URL for private repos
```json
{"source": "url", "url": "git@github.com:private-org/private-repo.git"}
```

## 3. Missing Required Fields

**marketplace.json required**:
- `name`
- `owner.name`
- `plugins` array

**plugin.json required**:
- `name`
- `description`
- `version`

## 4. Path Errors

**Wrong**: Relative paths from wrong directory
```json
{"source": "../plugins/tool"}  // Relative to what?
```

**Right**: Paths relative to marketplace.json location
```json
{"source": "./plugins/tool"}  // Relative to .claude-plugin/
```

## 5. Version Mismatch

Keep versions in sync:
- `plugin.json` version
- `marketplace.json` plugin entry version

When you update a plugin, update both files.

## 6. Forgetting Validation

Always run before publishing:
```bash
claude plugin validate .
```

## 7. Trust Model Misunderstanding

Users MUST explicitly trust marketplaces. You cannot force-install plugins on team members. The settings.json only PRE-CONFIGURES - users still approve.

---
