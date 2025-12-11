# Enterprise Marketplace Template

Complete enterprise marketplace setup with team configuration, private repos, and governance.

---

## When to Use

- Company-wide plugin distribution
- Mix of internal and approved external plugins
- Strict access control requirements
- Team onboarding automation
- Compliance and security governance

---

## Enterprise Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                    ENTERPRISE PLUGIN ECOSYSTEM                   │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  ┌──────────────────┐    ┌──────────────────┐                   │
│  │ Internal         │    │ Approved         │                   │
│  │ Marketplace      │    │ External         │                   │
│  │ (private git)    │    │ (public GitHub)  │                   │
│  │                  │    │                  │                   │
│  │ - company-tools  │    │ - community-lint │                   │
│  │ - deploy-tools   │    │ - doc-generator  │                   │
│  │ - security-scan  │    │                  │                   │
│  └────────┬─────────┘    └────────┬─────────┘                   │
│           │                       │                              │
│           └───────────┬───────────┘                              │
│                       │                                          │
│           ┌───────────▼───────────┐                              │
│           │ Team Settings         │                              │
│           │ .claude/settings.json │                              │
│           │                       │                              │
│           │ - Pre-configured      │                              │
│           │ - Default plugins     │                              │
│           │ - Trust boundaries    │                              │
│           └───────────────────────┘                              │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## Complete Enterprise Setup

### Step 1: Internal Marketplace Repository

Create private marketplace at `git.company.com/devtools/claude-marketplace`:

**.claude-plugin/marketplace.json**:
```json
{
  "name": "company-internal",
  "owner": {
    "name": "Platform Engineering",
    "email": "platform@company.com"
  },
  "metadata": {
    "description": "Company-approved Claude Code plugins",
    "version": "4.0.0",
    "pluginRoot": "./plugins"
  },
  "plugins": [
    {
      "name": "company-tools",
      "source": "./plugins/company-tools",
      "description": "Company-specific development tools and standards",
      "version": "2.5.0",
      "author": {"name": "Platform Team"}
    },
    {
      "name": "deploy-tools",
      "source": "./plugins/deploy-tools",
      "description": "Deployment automation with company infrastructure",
      "version": "3.1.0",
      "author": {"name": "DevOps Team"}
    },
    {
      "name": "security-scanner",
      "source": "./plugins/security-scanner",
      "description": "Security scanning aligned with company policies",
      "version": "1.8.0",
      "author": {"name": "Security Team"}
    },
    {
      "name": "compliance-checker",
      "source": "./plugins/compliance-checker",
      "description": "Compliance validation for regulated industries",
      "version": "1.2.0",
      "author": {"name": "Compliance Team"}
    }
  ]
}
```

### Step 2: Approved External Marketplace

Create curation marketplace at `github.com/company/approved-plugins`:

**.claude-plugin/marketplace.json**:
```json
{
  "name": "company-approved",
  "owner": {
    "name": "Platform Engineering",
    "email": "platform@company.com"
  },
  "metadata": {
    "description": "Company-approved external plugins (vetted for security)",
    "version": "2.0.0"
  },
  "plugins": [
    {
      "name": "community-formatter",
      "source": {"source": "github", "repo": "formatting/code-formatter"},
      "description": "Multi-language code formatter (approved v2.5.0)",
      "version": "2.5.0",
      "author": {"name": "Formatting Community"}
    },
    {
      "name": "community-linter",
      "source": {"source": "github", "repo": "linting/universal-linter"},
      "description": "Universal linting toolkit (approved v3.0.0)",
      "version": "3.0.0",
      "author": {"name": "Linting Community"}
    },
    {
      "name": "doc-generator",
      "source": {"source": "github", "repo": "docs/auto-docs"},
      "description": "Automatic documentation generator (approved v1.5.0)",
      "version": "1.5.0",
      "author": {"name": "Docs Community"}
    }
  ]
}
```

### Step 3: Team Settings Configuration

Add to project template's `.claude/settings.json`:

```json
{
  "extraKnownMarketplaces": {
    "company-internal": {
      "source": {
        "source": "git",
        "url": "git@git.company.com:devtools/claude-marketplace.git"
      }
    },
    "company-approved": {
      "source": {
        "source": "github",
        "repo": "company/approved-plugins"
      }
    }
  },
  "enabledPlugins": {
    "company-tools@company-internal": true,
    "security-scanner@company-internal": true,
    "compliance-checker@company-internal": true,
    "community-formatter@company-approved": true,
    "community-linter@company-approved": true
  }
}
```

**What this does**:
1. Pre-configures both marketplaces for the project
2. Auto-enables required company plugins
3. Auto-enables approved external plugins
4. deploy-tools and doc-generator available but not auto-enabled

---

## Internal Plugin Examples

### plugins/company-tools/.claude-plugin/plugin.json

```json
{
  "name": "company-tools",
  "description": "Company-specific development tools: coding standards, project templates, internal API access",
  "version": "2.5.0",
  "author": {
    "name": "Platform Engineering",
    "email": "platform@company.com"
  },
  "repository": "https://git.company.com/devtools/claude-marketplace",
  "license": "PROPRIETARY"
}
```

### plugins/company-tools/commands/init-project.md

```markdown
---
description: Initialize a new project with company standards
allowed-tools: Bash(git:*, mkdir:*, cp:*), Read, Write
argument-hint: [project-name] [template-type]
---

Initialize a new project: $1 using template: $2

## Available Templates

- `service` - Microservice with company boilerplate
- `library` - Shared library package
- `frontend` - React frontend with design system
- `data` - Data pipeline project

## Steps

1. Create project directory
2. Copy template files from company-templates/
3. Initialize git with company hooks
4. Configure CI/CD based on template
5. Add standard dependencies
6. Create initial documentation

## Output

- Project created at ./$1
- Git initialized with company remote
- README with next steps
```

### plugins/company-tools/commands/standards-check.md

```markdown
---
description: Check code against company coding standards
allowed-tools: Read, Grep, Glob, Bash(npx:*)
---

Check the current project against company coding standards.

## Standards Checked

### Code Style
- [ ] Uses company ESLint config
- [ ] Follows naming conventions
- [ ] Proper file organization

### Security
- [ ] No hardcoded secrets
- [ ] Uses company auth library
- [ ] Input validation present

### Documentation
- [ ] README exists and complete
- [ ] API documentation present
- [ ] Changelog maintained

### Testing
- [ ] Unit test coverage > 80%
- [ ] Integration tests present
- [ ] E2E tests for critical paths

## Output

### Standards Compliance Report

**Overall Score**: X/100

#### Passing
- [Standard]: [Details]

#### Failing
- [Standard]: [Issue] → [How to fix]

#### Recommendations
- [Improvement suggestions]
```

### plugins/security-scanner/agents/security-reviewer.md

```markdown
---
name: security-reviewer
description: Company security reviewer for code changes. Use PROACTIVELY on PRs and before deployments. Triggers: "security review", "check security", "audit code"
tools: Read, Grep, Glob, Bash(git diff:*)
model: sonnet
---

You are a security engineer reviewing code against company security standards.

## When Invoked

1. Get the code changes (PR diff or uncommitted changes)
2. Check against company security checklist
3. Flag any violations with severity
4. Suggest remediations

## Company Security Checklist

### Authentication
- [ ] Uses company auth library (not custom auth)
- [ ] Proper session management
- [ ] MFA enforced where required

### Authorization
- [ ] RBAC implemented correctly
- [ ] No privilege escalation paths
- [ ] Audit logging present

### Data Protection
- [ ] PII properly encrypted
- [ ] No sensitive data in logs
- [ ] Data retention policies followed

### Input Validation
- [ ] All inputs validated
- [ ] SQL injection prevention
- [ ] XSS prevention

### Dependencies
- [ ] No known CVEs
- [ ] Approved dependency list followed
- [ ] Locked versions

### Secrets
- [ ] No hardcoded secrets
- [ ] Uses company secrets manager
- [ ] Proper key rotation

## Output Format

### Security Review: [PASS/FAIL/NEEDS_ATTENTION]

**Risk Level**: [Low/Medium/High/Critical]

#### Critical Issues (Block Deployment)
| Issue | Location | Remediation |
|-------|----------|-------------|

#### High Priority (Fix Before Merge)
| Issue | Location | Remediation |
|-------|----------|-------------|

#### Medium Priority (Track in Backlog)
| Issue | Location | Remediation |
|-------|----------|-------------|

#### Recommendations
- [Best practice suggestions]

#### Compliance Notes
- [Regulatory considerations if applicable]
```

### plugins/deploy-tools/commands/deploy-staging.md

```markdown
---
description: Deploy to staging environment with safety checks
allowed-tools: Bash(git:*, kubectl:*, helm:*, curl:*), Read
---

Deploy current branch to staging environment.

## Pre-Deploy Checks

1. **Branch Status**
   - Must be up to date with main
   - All tests passing in CI
   - No merge conflicts

2. **Security Scan**
   - Run security-scanner
   - No critical/high vulnerabilities

3. **Configuration**
   - Staging secrets configured
   - Feature flags set

## Deploy Process

1. Build container image
2. Push to company registry
3. Update Helm values for staging
4. Apply via kubectl
5. Wait for rollout
6. Run smoke tests

## Post-Deploy

1. Verify health endpoints
2. Check logs for errors
3. Notify #deployments Slack channel

## Rollback

If issues detected:
```bash
kubectl rollout undo deployment/[service] -n staging
```

## Output

### Deployment Report

**Environment**: Staging
**Version**: [git SHA]
**Status**: [SUCCESS/FAILED]

#### Pre-Deploy Checks
- [ ] Branch up to date
- [ ] Tests passing
- [ ] Security scan clean

#### Deploy Steps
- [ ] Image built
- [ ] Image pushed
- [ ] Helm applied
- [ ] Rollout complete

#### Health Check
- [ ] /health returning 200
- [ ] No errors in logs

**Staging URL**: https://staging.service.company.com
```

### plugins/deploy-tools/hooks/hooks.json

```json
{
  "hooks": [
    {
      "matcher": {
        "event": "pre-tool-use",
        "tool": "Bash"
      },
      "hooks": [
        {
          "type": "command",
          "command": "if echo \"$TOOL_INPUT\" | grep -q 'kubectl.*production'; then echo '⚠️  PRODUCTION DEPLOYMENT DETECTED - Requires approval'; fi"
        }
      ]
    }
  ]
}
```

---

## Governance Workflow

### Plugin Approval Process

```
1. Developer creates plugin
         │
         ▼
2. Security review
   - Code audit
   - Dependency check
   - Permission analysis
         │
         ▼
3. Platform review
   - Architecture review
   - Integration check
   - Documentation review
         │
         ▼
4. Add to appropriate marketplace
   - Internal: company-internal
   - External (approved): company-approved
         │
         ▼
5. Notify teams of availability
```

### Version Control

**For internal plugins**:
- All changes require PR review
- Security team approval for security-related plugins
- Changelog required

**For approved external plugins**:
- Pin to specific versions
- Re-review required for version bumps
- Document approval in marketplace.json

---

## Access Control

### Private Repository Access

**SSH Key Setup**:
```bash
# Generate deploy key
ssh-keygen -t ed25519 -f ~/.ssh/claude-plugins -C "claude-plugins-deploy"

# Add public key to git server
# Add private key to team keychain or secrets manager
```

**For CI/CD**:
```yaml
# Store SSH key as secret
# Configure git to use key
- name: Setup SSH
  run: |
    mkdir -p ~/.ssh
    echo "${{ secrets.PLUGIN_DEPLOY_KEY }}" > ~/.ssh/id_ed25519
    chmod 600 ~/.ssh/id_ed25519
    ssh-keyscan git.company.com >> ~/.ssh/known_hosts
```

### Personal Access Tokens

For HTTPS access to private repos:
```bash
# Configure git credential
git config --global credential.helper store
echo "https://oauth2:${PAT}@git.company.com" >> ~/.git-credentials
```

---

## Onboarding Automation

### New Developer Setup

1. Clone project with settings.json
2. Run Claude Code in project
3. Trust prompt appears for marketplaces
4. Accept trust for company-internal and company-approved
5. Plugin installation prompts appear
6. Install required plugins

### Setup Script

```bash
#!/bin/bash
# setup-claude-plugins.sh

echo "Setting up Claude Code plugins for company projects..."

# Ensure SSH access to private git
if ! ssh -T git@git.company.com 2>&1 | grep -q "successfully"; then
  echo "❌ Cannot access git.company.com - configure SSH key first"
  exit 1
fi

echo "✅ Git access verified"
echo ""
echo "Next steps:"
echo "1. Open any company project in Claude Code"
echo "2. Trust the folder when prompted"
echo "3. Accept marketplace trust prompts"
echo "4. Install recommended plugins"
```

---

## Monitoring and Compliance

### Plugin Usage Tracking

Create audit log for plugin installations:

```json
// .claude/audit-log.json (git-ignored)
{
  "installations": [
    {
      "timestamp": "2024-01-15T10:30:00Z",
      "user": "developer@company.com",
      "plugin": "deploy-tools",
      "marketplace": "company-internal",
      "version": "3.1.0"
    }
  ]
}
```

### Compliance Reporting

```markdown
## Quarterly Plugin Compliance Report

### Approved Plugins in Use
| Plugin | Version | Last Updated | Security Review |
|--------|---------|--------------|-----------------|
| company-tools | 2.5.0 | 2024-01-10 | Passed |
| security-scanner | 1.8.0 | 2024-01-05 | Passed |

### Pending Reviews
| Plugin | Requested | Status |
|--------|-----------|--------|
| new-tool | 2024-01-14 | In Review |

### Deprecated Plugins
| Plugin | Deprecated | Replacement |
|--------|------------|-------------|
| old-formatter | 2023-12-01 | community-formatter |
```
