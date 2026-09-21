#!/usr/bin/env python3
"""Validate the claude-vibes plugin: frontmatter, cross-references, links, and manifest claims.

Markdown prompts have no compiler, so a renamed agent or a stale count fails silently
for users. This script is the compiler. Run: python3 scripts/validate_plugin.py
"""
import json
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
PLUGIN = ROOT / "plugins" / "vibes"
PLUGIN_NAME = "claude-vibes"
AGENT_MODELS = {"fable", "opus", "sonnet", "haiku", "inherit"}
MAX_DESCRIPTION_CHARS = 1024

errors = []


def fail(path, message):
    errors.append(f"{path.relative_to(ROOT)}: {message}")


def frontmatter(path):
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        fail(path, "missing YAML frontmatter")
        return None
    end = text.find("\n---", 4)
    if end == -1:
        fail(path, "unterminated YAML frontmatter")
        return None
    try:
        data = yaml.safe_load(text[4:end])
    except yaml.YAMLError as exc:
        fail(path, f"frontmatter is not valid YAML ({str(exc).splitlines()[0]})")
        return None
    if not isinstance(data, dict):
        fail(path, "frontmatter is not a mapping")
        return None
    return data


def check_description(path, data, max_chars=None):
    description = data.get("description")
    if not isinstance(description, str) or not description.strip():
        fail(path, "missing description")
    elif max_chars and len(description) > max_chars:
        fail(path, f"description is {len(description)} chars (max {max_chars})")


def strip_code_fences(text):
    """Links inside fenced blocks are illustrative examples, not real references."""
    kept, fence = [], None
    for line in text.split("\n"):
        match = re.match(r"^\s*(`{3,}|~{3,})(.*)$", line)
        if match:
            marker, info = match.group(1), match.group(2).strip()
            if fence is None:
                fence = marker
            elif marker[0] == fence[0] and len(marker) >= len(fence) and not info:
                fence = None
            continue
        if fence is None:
            kept.append(line)
    return "\n".join(kept)


skill_files = sorted((PLUGIN / "skills").glob("*/SKILL.md"))
agent_files = sorted((PLUGIN / "agents").rglob("*.md"))
command_files = sorted((PLUGIN / "commands").rglob("*.md"))

skill_names = set()
for path in skill_files:
    data = frontmatter(path)
    if data is None:
        continue
    # The 1024-char cap is part of the skill spec; agent descriptions may carry long <example> blocks.
    check_description(path, data, max_chars=MAX_DESCRIPTION_CHARS)
    if data.get("name") != path.parent.name:
        fail(path, f"name '{data.get('name')}' does not match directory '{path.parent.name}'")
    skill_names.add(path.parent.name)

agent_ids = set()
preloaded_skills = []
for path in agent_files:
    data = frontmatter(path)
    if data is None:
        continue
    check_description(path, data)
    if data.get("name") != path.stem:
        fail(path, f"name '{data.get('name')}' does not match filename '{path.stem}'")
    model = data.get("model")
    if model is not None and model not in AGENT_MODELS and not str(model).startswith("claude-"):
        fail(path, f"unknown model '{model}'")
    skills = data.get("skills") or []
    if isinstance(skills, str):
        skills = [name.strip() for name in skills.split(",")]
    preloaded_skills.extend((path, name) for name in skills)
    folder = path.parent.relative_to(PLUGIN / "agents").as_posix().replace("/", ":")
    agent_ids.add(f"{PLUGIN_NAME}:{folder}:{path.stem}" if folder != "." else f"{PLUGIN_NAME}:{path.stem}")

# A preloaded skill that no longer exists fails silently at launch, so check it here.
for path, name in preloaded_skills:
    if name.removeprefix(f"{PLUGIN_NAME}:") not in skill_names:
        fail(path, f"preloads unknown skill '{name}'")

for path in command_files:
    data = frontmatter(path)
    if data is not None:
        check_description(path, data)

# Plugin agents in subfolders register as plugin:folder:name, so every reference must use that form.
reference = re.compile(rf"{PLUGIN_NAME}:[A-Za-z0-9_-]+(?::[A-Za-z0-9_-]+)?")
for path in command_files + agent_files:
    for number, line in enumerate(path.read_text(encoding="utf-8").split("\n"), 1):
        for ref in reference.findall(line):
            is_skill = ref.count(":") == 1 and ref.split(":")[1] in skill_names
            if ref not in agent_ids and not is_skill:
                fail(path, f"line {number}: '{ref}' is not a known agent or skill")

link = re.compile(r"\[[^\]]*\]\(([^)\s]+)\)")
inline_code = re.compile(r"`[^`\n]*`")
for path in sorted((PLUGIN / "skills").rglob("*.md")):
    # templates/ and examples/ hold sample output whose links point at files the user will create.
    if {"templates", "examples"} & set(path.relative_to(PLUGIN / "skills").parts[1:-1]):
        continue
    prose = inline_code.sub("", strip_code_fences(path.read_text(encoding="utf-8")))
    for target in link.findall(prose):
        if re.match(r"^(https?:|mailto:|#)", target) or not re.search(r"[./]", target):
            continue
        if not (path.parent / target.split("#")[0]).exists():
            fail(path, f"broken relative link '{target}'")

manifest = json.loads((PLUGIN / ".claude-plugin" / "plugin.json").read_text())
marketplace = json.loads((ROOT / ".claude-plugin" / "marketplace.json").read_text())
manifest_path = PLUGIN / ".claude-plugin" / "plugin.json"
marketplace_path = ROOT / ".claude-plugin" / "marketplace.json"

for server, config in manifest.get("mcpServers", {}).items():
    if config.get("command") == "npx":
        packages = [str(arg) for arg in config.get("args", []) if not str(arg).startswith("-")]
        for package in packages[:1]:
            # A scoped name starts with "@", so look for a version after the last "@" that is not at index 0.
            version = package.rsplit("@", 1)[1] if "@" in package[1:] else ""
            if not re.fullmatch(r"\d+\.\d+\.\d+[\w.-]*", version):
                fail(manifest_path, f"MCP server '{server}' must pin '{package}' to an exact version")

actual = {
    "commands": len(command_files),
    "agents": len(agent_files),
    "skills": len(skill_files),
    "MCP servers": len(manifest.get("mcpServers", {})),
}
listing = marketplace["plugins"][0]["description"]
for label, count in actual.items():
    claimed = re.search(rf"(\d+) {label}", listing)
    if claimed and int(claimed.group(1)) != count:
        fail(marketplace_path, f"description claims {claimed.group(1)} {label}, found {count}")

if errors:
    print(f"{len(errors)} problem(s):\n")
    print("\n".join(f"  - {error}" for error in errors))
    sys.exit(1)
print("OK: " + ", ".join(f"{count} {label}" for label, count in actual.items()))
