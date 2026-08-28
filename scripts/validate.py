#!/usr/bin/env python3
"""Validate the public Lantide Data plugin without third-party dependencies."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MANIFEST_PATH = ROOT / ".codex-plugin" / "plugin.json"
NAME_PATTERN = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


def fail(message: str) -> None:
    raise ValueError(message)


def parse_frontmatter(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    if "[TODO]" in text:
        fail(f"placeholder remains in {path.relative_to(ROOT)}")
    lines = text.splitlines()
    if not lines or lines[0] != "---":
        fail(f"missing YAML frontmatter in {path.relative_to(ROOT)}")
    try:
        end = lines.index("---", 1)
    except ValueError as error:
        raise ValueError(f"unterminated frontmatter in {path.relative_to(ROOT)}") from error

    metadata: dict[str, str] = {}
    for line in lines[1:end]:
        if not line.strip():
            continue
        if ":" not in line:
            fail(f"invalid frontmatter line in {path.relative_to(ROOT)}: {line}")
        key, value = line.split(":", 1)
        metadata[key.strip()] = value.strip()
    return metadata


def main() -> int:
    manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    plugin_name = manifest.get("name", "")
    if not NAME_PATTERN.fullmatch(plugin_name):
        fail("plugin name must be lowercase kebab-case")
    if plugin_name != ROOT.name:
        fail(f"plugin name {plugin_name!r} must match directory {ROOT.name!r}")
    if manifest.get("version") != "0.1.0":
        fail("initial plugin version must be 0.1.0")

    skill_root = ROOT / manifest.get("skills", "")
    if not skill_root.is_dir():
        fail("manifest skills directory does not exist")

    skill_dirs = sorted(path for path in skill_root.iterdir() if path.is_dir())
    if not skill_dirs:
        fail("plugin must include at least one skill")
    for skill_dir in skill_dirs:
        metadata = parse_frontmatter(skill_dir / "SKILL.md")
        if metadata.get("name") != skill_dir.name:
            fail(f"skill name must match directory: {skill_dir.name}")
        description = metadata.get("description", "")
        if not description or len(description) > 1024:
            fail(f"invalid description for skill {skill_dir.name}")
        if not (skill_dir / "agents" / "openai.yaml").is_file():
            fail(f"missing agents/openai.yaml for skill {skill_dir.name}")

    interface = manifest.get("interface", {})
    for asset_key in ("composerIcon", "logo"):
        relative = interface.get(asset_key)
        if not relative or not (ROOT / relative).is_file():
            fail(f"missing interface asset: {asset_key}")

    print(f"Validated {plugin_name} with {len(skill_dirs)} skills.")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, ValueError, json.JSONDecodeError) as error:
        print(f"validation failed: {error}", file=sys.stderr)
        raise SystemExit(1)
