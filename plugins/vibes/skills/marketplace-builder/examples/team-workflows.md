# Team Workflows Marketplace Examples

Six complete plugin examples for team collaboration and workflows.

---

## Example 1: PR Reviewer Plugin

Automated pull request review assistance.

### Plugin Structure

```
pr-reviewer/
├── .claude-plugin/
│   └── plugin.json
├── commands/
│   ├── review-pr.md
│   ├── pr-summary.md
│   └── approve-pr.md
└── agents/
    └── pr-analyst.md
```

### .claude-plugin/plugin.json

```json
{
  "name": "pr-reviewer",
  "description": "Pull request review automation: code analysis, summary generation, review comments",
  "version": "2.0.0",
  "author": {"name": "Review Team"},
  "license": "MIT"
}
```

### commands/review-pr.md

```markdown
---
description: Review a pull request with detailed analysis
allowed-tools: Bash(gh:*, git:*), Read, Grep
argument-hint: [pr-number]
---

Review PR #$1

## Steps

1. Fetch PR details: `gh pr view $1 --json title,body,files,additions,deletions`
2. Get the diff: `gh pr diff $1`
3. Analyze changes for:
   - Code quality
   - Security concerns
   - Performance implications
   - Test coverage
   - Documentation updates
4. Generate review summary

## Output

### PR Review: #$1

**Title**: [PR title]
**Author**: [author]
**Changes**: +X/-Y lines across Z files

#### Summary
[What this PR does in 2-3 sentences]

#### Code Quality
| Aspect | Rating | Notes |
|--------|--------|-------|
| Readability | ⭐⭐⭐⭐ | Clear variable names |
| Complexity | ⭐⭐⭐ | Consider extracting helper |
| Testing | ⭐⭐⭐⭐⭐ | Good coverage |

#### Security Review
- [ ] No hardcoded secrets
- [ ] Input validation present
- [ ] Auth checks in place

#### Suggestions
1. [Suggestion with file:line reference]
2. [Suggestion with file:line reference]

#### Verdict
**[APPROVE / REQUEST_CHANGES / COMMENT]**
```

### agents/pr-analyst.md

```markdown
---
name: pr-analyst
description: Deep analysis of pull requests. Use when reviewing PRs, understanding changes, or preparing review feedback. Triggers: "analyze PR", "PR analysis", "review pull request"
tools: Bash(gh:*, git:*), Read, Grep, Glob
model: sonnet
---

You are a senior engineer conducting thorough PR reviews.

## When Invoked

1. Gather PR context:
   - PR description and linked issues
   - Full diff
   - Related files not in diff
2. Analyze systematically:
   - Architecture impact
   - Code correctness
   - Edge cases
   - Error handling
3. Provide constructive feedback

## Review Checklist

### Functionality
- [ ] Solves the stated problem
- [ ] Handles edge cases
- [ ] Error scenarios covered

### Code Quality
- [ ] Follows project conventions
- [ ] No code duplication
- [ ] Appropriate abstractions

### Testing
- [ ] Unit tests for new code
- [ ] Edge cases tested
- [ ] Integration tests if needed

### Documentation
- [ ] Code comments where needed
- [ ] README updated if applicable
- [ ] API docs for public interfaces

## Output Format

### Detailed PR Analysis

**Summary**: [What and why]

**Impact Assessment**:
- Scope: [Low/Medium/High]
- Risk: [Low/Medium/High]
- Breaking Changes: [Yes/No]

**Line-by-Line Comments**:
- `file.ts:25` - [Comment]
- `file.ts:42` - [Comment]

**Overall Recommendation**: [Approve/Changes Requested]
```

---

## Example 2: Deployment Plugin

Safe deployment automation with checks and rollback.

### Plugin Structure

```
deployment/
├── .claude-plugin/
│   └── plugin.json
├── commands/
│   ├── deploy-staging.md
│   ├── deploy-prod.md
│   ├── rollback.md
│   └── deploy-status.md
└── hooks/
    └── hooks.json
```

### .claude-plugin/plugin.json

```json
{
  "name": "deployment",
  "description": "Deployment automation: staging/production deploys, rollback support, health checks",
  "version": "3.0.0",
  "author": {"name": "DevOps Team"},
  "license": "MIT"
}
```

### commands/deploy-staging.md

```markdown
---
description: Deploy to staging with pre-flight checks
allowed-tools: Bash(git:*, docker:*, kubectl:*, curl:*), Read
---

Deploy current branch to staging environment.

## Pre-Flight Checks

1. ✓ Branch is up to date with main
2. ✓ All tests passing (CI green)
3. ✓ No critical security vulnerabilities
4. ✓ Environment secrets configured

## Deployment Steps

1. Build container image
2. Push to registry
3. Update staging deployment
4. Wait for rollout
5. Run smoke tests
6. Report status

## Output

### Deployment to Staging

**Branch**: feature/new-auth
**Commit**: abc1234
**Image**: registry.io/app:abc1234

#### Pre-Flight
- [x] Branch synced
- [x] Tests passing
- [x] Security clean

#### Progress
- [x] Image built (2m 15s)
- [x] Image pushed
- [x] Deployment updated
- [x] Pods healthy (3/3)
- [x] Smoke tests passed

**Status**: ✅ SUCCESS
**URL**: https://staging.app.com
**Time**: 4m 32s
```

### commands/deploy-prod.md

```markdown
---
description: Deploy to production (requires confirmation)
allowed-tools: Bash(git:*, docker:*, kubectl:*, curl:*), Read
---

Deploy to production environment.

## ⚠️ PRODUCTION DEPLOYMENT ⚠️

This will deploy to PRODUCTION. Please confirm:
- Staging has been tested
- Stakeholders are notified
- Rollback plan is ready

## Requirements

1. Must be on main branch
2. All tests passing
3. Staging verified within last 24h
4. No active incidents

## Deployment Steps

1. Create deployment record
2. Build production image
3. Blue-green deployment
4. Gradual traffic shift (10% → 50% → 100%)
5. Monitor error rates
6. Complete or rollback

## Output

### Production Deployment

**Version**: v2.5.0
**Previous**: v2.4.3

#### Traffic Shift
- [ ] 10% → Monitoring...
- [ ] 50% → Monitoring...
- [ ] 100% → Complete

**Rollback Command**: `/rollback v2.4.3`
```

### hooks/hooks.json

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
          "command": "if echo \"$TOOL_INPUT\" | grep -qE 'kubectl.*(delete|scale.*0|rollout.*restart).*prod'; then echo '⚠️ DESTRUCTIVE PRODUCTION COMMAND - Requires explicit confirmation'; exit 1; fi"
        }
      ]
    }
  ]
}
```

---

## Example 3: Standup Plugin

Daily standup automation and reporting.

### Plugin Structure

```
standup/
├── .claude-plugin/
│   └── plugin.json
├── commands/
│   ├── standup.md
│   ├── standup-summary.md
│   └── blockers.md
└── agents/
    └── standup-reporter.md
```

### .claude-plugin/plugin.json

```json
{
  "name": "standup",
  "description": "Daily standup automation: activity summaries, blocker tracking, team updates",
  "version": "1.5.0",
  "author": {"name": "Team Tools"},
  "license": "MIT"
}
```

### commands/standup.md

```markdown
---
description: Generate your daily standup update
allowed-tools: Bash(git:*, gh:*), Read
---

Generate standup update based on recent activity.

## Data Sources

1. Git commits since yesterday
2. PRs opened/reviewed/merged
3. Issues worked on
4. Calendar (if accessible)

## Steps

1. Get commits: `git log --author="$(git config user.email)" --since="yesterday" --oneline`
2. Get PRs: `gh pr list --author=@me --state=all --json number,title,state`
3. Get issues: `gh issue list --assignee=@me --json number,title,state`
4. Format standup

## Output

### Daily Standup - [Date]

#### Yesterday
- Completed PR #123: Add user authentication
- Reviewed PR #125: Fix payment bug
- Worked on issue #100: Performance optimization

#### Today
- Continue issue #100
- Review pending PRs
- Start issue #105: API rate limiting

#### Blockers
- None currently

---
*Auto-generated from git and GitHub activity*
```

### agents/standup-reporter.md

```markdown
---
name: standup-reporter
description: Generates team standup summaries and tracks blockers. Use for team standups, progress reports, or blocker identification. Triggers: "standup", "team update", "what's everyone working on"
tools: Bash(git:*, gh:*), Read
model: haiku
---

You are a team coordinator generating standup reports.

## When Invoked

1. Gather activity for each team member (if accessible)
2. Or summarize individual activity
3. Identify patterns and blockers
4. Generate concise report

## Report Format

### Team Standup Summary

**Date**: [Today]
**Team**: [Team name]

#### Activity Highlights
- [Member]: [Key accomplishment]
- [Member]: [Key accomplishment]

#### In Progress
| Member | Task | Status |
|--------|------|--------|

#### Blockers
| Member | Blocker | Since | Action Needed |
|--------|---------|-------|---------------|

#### PRs Awaiting Review
- PR #X by [author] - [title] (waiting Xh)
```

---

## Example 4: Onboarding Plugin

New team member onboarding automation.

### Plugin Structure

```
onboarding/
├── .claude-plugin/
│   └── plugin.json
├── commands/
│   ├── setup-dev.md
│   ├── codebase-tour.md
│   └── team-intro.md
└── skills/
    └── project-context/
        └── SKILL.md
```

### .claude-plugin/plugin.json

```json
{
  "name": "onboarding",
  "description": "Developer onboarding: environment setup, codebase tours, team introductions",
  "version": "2.0.0",
  "author": {"name": "Platform Team"},
  "license": "MIT"
}
```

### commands/setup-dev.md

```markdown
---
description: Set up development environment for new team members
allowed-tools: Bash(brew:*, npm:*, pip:*, git:*), Read, Write
---

Set up development environment for this project.

## Environment Setup

### Step 1: Check Prerequisites
- [ ] Git configured
- [ ] Node.js installed (if JS project)
- [ ] Python installed (if Python project)
- [ ] Docker installed (if containerized)

### Step 2: Clone and Install
```bash
# Clone repository
git clone <repo-url>
cd <project>

# Install dependencies
npm install  # or pip install -r requirements.txt
```

### Step 3: Configure Environment
- Copy `.env.example` to `.env`
- Fill in required values
- Set up local database (if needed)

### Step 4: Verify Setup
```bash
# Run tests
npm test

# Start development server
npm run dev
```

## Output

### Setup Progress

- [x] Prerequisites checked
- [x] Repository cloned
- [x] Dependencies installed
- [x] Environment configured
- [x] Tests passing

**Setup Complete!** 🎉

### Next Steps
1. Read `/codebase-tour` for architecture overview
2. Check `/team-intro` for team contacts
3. Look at good-first-issues for starter tasks
```

### commands/codebase-tour.md

```markdown
---
description: Interactive tour of the codebase structure
allowed-tools: Read, Glob, Grep
---

Take a guided tour of this codebase.

## Codebase Tour

### Project Overview
[Read README and describe project purpose]

### Directory Structure
```
project/
├── src/           # Source code
├── tests/         # Test files
├── docs/          # Documentation
└── config/        # Configuration
```

### Key Files
| File | Purpose |
|------|---------|
| src/index.ts | Application entry point |
| src/routes/ | API route handlers |
| src/services/ | Business logic |
| src/models/ | Data models |

### Architecture Patterns
- [Pattern 1]: Where and why
- [Pattern 2]: Where and why

### Common Tasks

**Add a new API endpoint:**
1. Create handler in `src/routes/`
2. Add service in `src/services/`
3. Register route in `src/routes/index.ts`
4. Add tests in `tests/routes/`

**Add a new model:**
1. Define in `src/models/`
2. Add migration in `migrations/`
3. Update services that use it

### Code Conventions
- [List key conventions from CLAUDE.md or similar]
```

### skills/project-context/SKILL.md

```markdown
---
name: project-context
description: Project-specific knowledge and conventions. Use when questions arise about project patterns, architecture decisions, or conventions. Triggers: "how do we", "project convention", "architecture"
---

# Project Context

## Architecture Decisions

[Document key architectural decisions]

## Coding Conventions

[Document coding standards]

## Common Patterns

[Document recurring patterns in the codebase]

## Troubleshooting

[Common issues and solutions]
```

---

## Example 5: Incident Response Plugin

Production incident management.

### Plugin Structure

```
incident-response/
├── .claude-plugin/
│   └── plugin.json
├── commands/
│   ├── incident-start.md
│   ├── incident-status.md
│   └── postmortem.md
└── agents/
    └── incident-analyzer.md
```

### .claude-plugin/plugin.json

```json
{
  "name": "incident-response",
  "description": "Incident management: response tracking, log analysis, postmortem generation",
  "version": "1.8.0",
  "author": {"name": "SRE Team"},
  "license": "MIT"
}
```

### commands/incident-start.md

```markdown
---
description: Start incident response tracking
allowed-tools: Bash(date:*), Read, Write
argument-hint: [severity] [description]
---

Start incident: $ARGUMENTS

## Incident Initialization

### Severity Levels
- **P1**: Complete outage, all users affected
- **P2**: Major feature broken, many users affected
- **P3**: Minor issue, some users affected
- **P4**: Cosmetic or low-impact issue

## Output

### 🚨 Incident Started

**ID**: INC-[timestamp]
**Severity**: [P1/P2/P3/P4]
**Started**: [timestamp]
**Description**: $2

#### Immediate Actions
1. [ ] Page on-call engineer (if P1/P2)
2. [ ] Create incident channel
3. [ ] Notify stakeholders
4. [ ] Begin investigation

#### Investigation Checklist
- [ ] Check error logs
- [ ] Check metrics dashboards
- [ ] Identify affected services
- [ ] Determine timeline

#### Communication Template
```
[INCIDENT] [Severity]: [Description]
Status: Investigating
Impact: [Describe impact]
ETA: Unknown
Updates: [Channel/link]
```

**Run `/incident-status` to update progress**
```

### agents/incident-analyzer.md

```markdown
---
name: incident-analyzer
description: Analyzes logs and metrics during incidents. Use during active incidents or when investigating past issues. Triggers: "analyze logs", "incident investigation", "what caused"
tools: Read, Grep, Glob, Bash(curl:*, grep:*)
model: sonnet
---

You are an SRE investigating production incidents.

## When Invoked

1. Gather context about the incident
2. Analyze available logs and metrics
3. Identify patterns and anomalies
4. Trace root cause
5. Suggest remediation

## Investigation Approach

### Timeline Construction
- When did it start?
- What changed before it started?
- What was the pattern of failures?

### Log Analysis
- Error messages
- Stack traces
- Request patterns
- Resource utilization

### Impact Assessment
- Users affected
- Requests failed
- Data integrity

## Output Format

### Incident Analysis

**Time Range**: [start] - [end]

#### Timeline
| Time | Event |
|------|-------|
| HH:MM | First error observed |
| HH:MM | Spike in errors |

#### Root Cause Analysis
**Primary Cause**: [Description]
**Contributing Factors**:
- [Factor 1]
- [Factor 2]

#### Evidence
```
[Relevant log snippets]
```

#### Remediation
- Immediate: [Steps]
- Long-term: [Improvements]
```

---

## Example 6: Release Management Plugin

Release coordination and changelog generation.

### Plugin Structure

```
release-manager/
├── .claude-plugin/
│   └── plugin.json
├── commands/
│   ├── release-prepare.md
│   ├── changelog.md
│   └── release-notes.md
└── agents/
    └── release-coordinator.md
```

### .claude-plugin/plugin.json

```json
{
  "name": "release-manager",
  "description": "Release management: version bumping, changelog generation, release coordination",
  "version": "2.2.0",
  "author": {"name": "Release Team"},
  "license": "MIT"
}
```

### commands/release-prepare.md

```markdown
---
description: Prepare a new release
allowed-tools: Bash(git:*, npm:*), Read, Write
argument-hint: [version] (major|minor|patch or specific version)
---

Prepare release: $1

## Release Preparation

### Step 1: Version Bump
- Determine new version from $1
- Update package.json
- Update version in other files

### Step 2: Changelog
- Generate from commits since last release
- Categorize changes (Features, Fixes, etc.)
- Add to CHANGELOG.md

### Step 3: Release Checklist
- [ ] All tests passing
- [ ] Documentation updated
- [ ] Breaking changes documented
- [ ] Migration guide (if needed)

## Output

### Release Preparation: v[X.Y.Z]

**Previous**: v[old]
**New**: v[new]
**Type**: [Major/Minor/Patch]

#### Changes Since Last Release
- X new features
- Y bug fixes
- Z other changes

#### Files Updated
- package.json
- CHANGELOG.md
- [other version files]

#### Next Steps
1. Review CHANGELOG.md
2. Create release PR
3. Merge and tag
4. `/release-notes` for announcement
```

### commands/changelog.md

```markdown
---
description: Generate changelog from commit history
allowed-tools: Bash(git:*), Read, Write
argument-hint: [since] (tag or commit, defaults to last release)
---

Generate changelog since: $ARGUMENTS

## Steps

1. Get commits since last release
2. Parse conventional commit messages
3. Categorize changes
4. Format as markdown

## Output

### Changelog

## [Unreleased]

### Features
- feat(auth): Add OAuth2 support (#123)
- feat(api): New rate limiting endpoints (#125)

### Bug Fixes
- fix(ui): Correct button alignment (#130)
- fix(api): Handle null responses (#132)

### Performance
- perf(db): Optimize user queries (#140)

### Documentation
- docs: Update API reference (#145)

### Breaking Changes
- **auth**: OAuth1 support removed

---

*Generated from X commits*
```

---

## Complete Marketplace Configuration

### marketplace.json

```json
{
  "name": "team-workflows",
  "owner": {
    "name": "Team Tools Community",
    "email": "teamtools@example.com"
  },
  "metadata": {
    "description": "Team collaboration and workflow automation tools",
    "version": "4.0.0"
  },
  "plugins": [
    {
      "name": "pr-reviewer",
      "source": {"source": "github", "repo": "teamtools/pr-reviewer"},
      "description": "Pull request review automation: analysis, summaries, comments",
      "version": "2.0.0"
    },
    {
      "name": "deployment",
      "source": {"source": "github", "repo": "teamtools/deployment"},
      "description": "Deployment automation: staging/prod deploys, rollback, health checks",
      "version": "3.0.0"
    },
    {
      "name": "standup",
      "source": {"source": "github", "repo": "teamtools/standup"},
      "description": "Daily standup automation: activity summaries, blocker tracking",
      "version": "1.5.0"
    },
    {
      "name": "onboarding",
      "source": {"source": "github", "repo": "teamtools/onboarding"},
      "description": "Developer onboarding: environment setup, codebase tours",
      "version": "2.0.0"
    },
    {
      "name": "incident-response",
      "source": {"source": "github", "repo": "teamtools/incident-response"},
      "description": "Incident management: response tracking, log analysis, postmortems",
      "version": "1.8.0"
    },
    {
      "name": "release-manager",
      "source": {"source": "github", "repo": "teamtools/release-manager"},
      "description": "Release management: versioning, changelogs, coordination",
      "version": "2.2.0"
    }
  ]
}
```
