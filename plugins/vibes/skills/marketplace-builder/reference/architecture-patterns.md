# Marketplace Architecture Patterns

Read this when choosing how to lay out a marketplace across one or several repositories.

## Monorepo Pattern

**Structure**:
```
company-plugins/
├── .claude-plugin/
│   └── marketplace.json
├── plugins/
│   ├── plugin-a/
│   ├── plugin-b/
│   └── plugin-c/
└── README.md
```

**Pros**:
- Single repo to manage
- Unified versioning
- Easy cross-plugin changes
- Simpler CI/CD

**Cons**:
- All plugins share access control
- Larger repo size
- All-or-nothing updates

**Best for**: Team tools, related plugins, unified ownership

---

## Multi-Repo Pattern

**Structure**:
```
# Marketplace repo
tools-marketplace/
└── .claude-plugin/marketplace.json

# Separate plugin repos
plugin-a/   # github.com/org/plugin-a
plugin-b/   # github.com/org/plugin-b
plugin-c/   # github.com/org/plugin-c
```

**Pros**:
- Independent versioning
- Separate access control
- Distributed ownership
- Smaller repos

**Cons**:
- More repos to manage
- Version coordination needed
- More complex CI/CD

**Best for**: Community collections, mixed ownership, independent plugins

---

## Hybrid Pattern

**Structure**:
```json
{
  "plugins": [
    {"name": "core", "source": "./plugins/core"},
    {"name": "community", "source": {"source": "github", "repo": "community/tool"}},
    {"name": "internal", "source": {"source": "url", "url": "https://git.corp/..."}}
  ]
}
```

**Pros**:
- Flexibility to mix sources
- Can include community plugins
- Supports private + public

**Cons**:
- More complex to maintain
- Mixed trust levels
- Varied update cycles

**Best for**: Enterprise, mature ecosystems, gradual migration

---
