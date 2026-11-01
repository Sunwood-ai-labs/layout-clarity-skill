#!/usr/bin/env python3
"""Dependency-free structural checks, not a usability score."""
from pathlib import Path
import re
root = Path(__file__).resolve().parents[1]
skill = root / 'skills/layout-clarity/SKILL.md'
text = skill.read_text(encoding='utf-8')
if not text.startswith('---\n'):
    raise SystemExit('Missing YAML frontmatter')
front = text.split('---', 2)[1]
for field in ('name: layout-clarity', 'description:'):
    if field not in front:
        raise SystemExit(f'Missing {field}')
checked = 0
for path in root.rglob('*.md'):
    content = path.read_text(encoding='utf-8')
    if '[TODO' in content or 'TODO:' in content:
        raise SystemExit(f'Unfinished scaffold: {path.relative_to(root)}')
    for target in re.findall(r'\]\(([^)]+)\)', content):
        if target.startswith(('https://', 'http://', '#')):
            continue
        resolved = (path.parent / target.split('#')[0]).resolve()
        if root not in resolved.parents or not resolved.is_file():
            raise SystemExit(f'Broken local reference: {path.relative_to(root)} -> {target}')
        checked += 1
print(f'PASS: skill frontmatter and {checked} local references')
