#!/usr/bin/env python3
"""Validate the skills-first Designwright portable Agent Plugin."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Any


SCHEMA_URL = "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json"
EXPECTED_MANIFEST = {
    "$schema": SCHEMA_URL,
    "name": "designwright",
    "version": "0.1.0",
    "description": "Evidence-first, project-adaptive design workflow skills for agent clients.",
    "author": {"name": "wkimball1"},
    "repository": "https://github.com/wkimball1/designwright",
    "keywords": ["design", "design-systems", "evidence", "ux", "agent-skills"],
}
REQUIRED_SKILLS = {
    "designwright-init",
    "designwright-direction",
    "designwright-component-intelligence",
    "designwright-evidence-loop",
    "designwright-independent-critique",
}
PLUGIN_NAME_PATTERN = re.compile(r"^[a-z0-9](?:[a-z0-9.-]*[a-z0-9])?$")
FRONTMATTER_KEY_PATTERN = re.compile(r"^[A-Za-z0-9_-]+$")


class DuplicateKeyError(ValueError):
    """Raised when JSON contains a duplicate object key."""


def _unique_pairs(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise DuplicateKeyError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def _read_manifest(root: Path, errors: list[str]) -> dict[str, Any] | None:
    path = root / "plugin.json"
    if not path.is_file():
        errors.append("plugin.json is missing")
        return None
    try:
        value = json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=_unique_pairs)
    except (OSError, UnicodeError, json.JSONDecodeError, DuplicateKeyError) as exc:
        errors.append(f"plugin.json is not valid JSON: {exc}")
        return None
    if not isinstance(value, dict):
        errors.append("plugin.json must contain a JSON object")
        return None
    return value


def _check_manifest(manifest: dict[str, Any], errors: list[str]) -> None:
    expected_keys = set(EXPECTED_MANIFEST)
    actual_keys = set(manifest)
    if actual_keys != expected_keys:
        missing = sorted(expected_keys - actual_keys)
        unexpected = sorted(actual_keys - expected_keys)
        if missing:
            errors.append(f"plugin.json is missing fields: {', '.join(missing)}")
        if unexpected:
            errors.append(f"plugin.json has unexpected fields: {', '.join(unexpected)}")
    if manifest != EXPECTED_MANIFEST:
        errors.append("plugin.json fields or values do not match the Designwright 0.1.0 contract")

    name = manifest.get("name")
    if isinstance(name, str):
        if len(name) > 64 or "--" in name or ".." in name or not PLUGIN_NAME_PATTERN.fullmatch(name):
            errors.append(f"plugin name is invalid: {name!r}")


def _parse_frontmatter(content: str, expected_name: str) -> list[str]:
    errors: list[str] = []
    lines = content.splitlines()
    if not lines or lines[0] != "---":
        return ["frontmatter must start with --- at byte 0"]

    closing_index = next((index for index in range(1, len(lines)) if lines[index] == "---"), None)
    if closing_index is None:
        return ["frontmatter is missing its closing ---"]
    if not any(line.strip() for line in lines[closing_index + 1 :]):
        errors.append("skill body is empty")

    fields: dict[str, str] = {}
    for line_number, line in enumerate(lines[1:closing_index], start=2):
        if not line.strip():
            continue
        if line[0].isspace():
            # Nested YAML is valid; this validator only needs the required scalars.
            continue
        match = re.match(r"^([^:#][^:]*):(?:[ \t]*(.*))?$", line)
        if not match:
            errors.append(f"frontmatter line {line_number} is not a YAML mapping entry")
            continue
        key = match.group(1).strip()
        value = (match.group(2) or "").strip()
        if not FRONTMATTER_KEY_PATTERN.fullmatch(key):
            errors.append(f"frontmatter key {key!r} is invalid")
            continue
        if key in fields:
            errors.append(f"frontmatter repeats key {key!r}")
            continue
        fields[key] = value

    if not fields.get("name"):
        errors.append("frontmatter name is missing")
    elif fields["name"] != expected_name:
        errors.append(
            f"frontmatter name {fields['name']!r} does not match directory {expected_name!r}"
        )
    if not fields.get("description"):
        errors.append("frontmatter description is missing")
    return errors


def _check_skills(root: Path, errors: list[str]) -> None:
    skills_root = root / "skills"
    if not skills_root.is_dir():
        errors.append("skills/ is missing")
        return

    actual_skills = {entry.name for entry in skills_root.iterdir() if entry.is_dir()}
    if actual_skills != REQUIRED_SKILLS:
        missing = sorted(REQUIRED_SKILLS - actual_skills)
        unexpected = sorted(actual_skills - REQUIRED_SKILLS)
        if missing:
            errors.append(f"skills/ is missing: {', '.join(missing)}")
        if unexpected:
            errors.append(f"skills/ has unexpected immediate directories: {', '.join(unexpected)}")

    for skill_name in sorted(REQUIRED_SKILLS):
        skill_path = skills_root / skill_name / "SKILL.md"
        if not skill_path.is_file():
            errors.append(f"{skill_name}/SKILL.md is missing")
            continue
        try:
            content = skill_path.read_text(encoding="utf-8")
        except (OSError, UnicodeError) as exc:
            errors.append(f"{skill_name}/SKILL.md cannot be read: {exc}")
            continue
        for message in _parse_frontmatter(content, skill_name):
            errors.append(f"{skill_name}/SKILL.md: {message}")


def _check_forbidden_content(root: Path, errors: list[str]) -> None:
    for filename in ("mcp.json", "plugin.yaml", "plugin.yml"):
        if (root / filename).exists():
            errors.append(f"unexpected {filename} at plugin root")
    workflows = root / ".github" / "workflows"
    if workflows.exists():
        errors.append("unexpected .github/workflows/ content")


def validate(root: Path) -> list[str]:
    errors: list[str] = []
    manifest = _read_manifest(root, errors)
    if manifest is not None:
        _check_manifest(manifest, errors)
    _check_skills(root, errors)
    _check_forbidden_content(root, errors)
    return errors


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    errors = validate(root)
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        print(f"Portable plugin validation failed with {len(errors)} error(s).", file=sys.stderr)
        return 1

    print("PASS: plugin.json manifest matches the Designwright 0.1.0 contract")
    print("PASS: five required Agent Skills have matching frontmatter names")
    print("PASS: no MCP, native Hermes, or GitHub workflow content is present")
    print("Portable plugin validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
