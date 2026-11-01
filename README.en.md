# Layout Clarity

**Improve the layout before adding another explanation.** A Codex skill for reducing redundant headings, generic slogans, and narration of obvious controls through hierarchy, proximity, grouping, and precise action labels.

[日本語](README.md) · [Skill](skills/layout-clarity/SKILL.md) · [Examples](skills/layout-clarity/references/examples.md) · [Evaluation cases](skills/layout-clarity/references/evaluation-cases.md)

## Keep the meaning, remove duplication

This is not a “delete all text” rule. Preserve visible form labels, accessible names, measurement scope, errors and remedies, consequential warnings, legal/safety information, and guidance for unfamiliar choices.

## Install

Ask Codex:

> Install skills/layout-clarity from Sunwood-ai-labs/layout-clarity-skill as a skill.

Alternatively, copy `skills/layout-clarity` into the skill directory for your Codex environment (usually `~/.codex/skills/layout-clarity`). Follow that environment's discovery mechanism and use a new session. Cloning this repository alone does not install it into your personal environment.

## Use

```text
$layout-clarity Refine this dashboard's redundant copy and hierarchy.
Preserve important data qualifiers and accessibility, then verify the implementation.
```

Optional project-specific AGENTS.md guidance:

```text
Avoid redundant secondary labels and explanations. Communicate relationships through
hierarchy, placement, and precise action names. Preserve decision-critical context,
form labels, error recovery, safety/legal information, and accessibility semantics.
```

Do not treat this snippet as permission to change unrelated project configuration.

## Check the package

```sh
python scripts/validate_package.py
```

This checks package structure and local references, not usability effectiveness. Seven manual evaluation cases are included; use observed behavior rather than a word-count target.

## Inspiration and rights

Inspired by a user-provided screenshot of a 22 October 2026 post by Zihua (@luinlee). The workflow, examples, and evaluation cases here are independently written. The screenshot and full post are not redistributed. The exact post URL has not been verified and is not invented here. No endorsement is implied.

No license has been designated yet. Public availability alone should not be interpreted as permission to redistribute.
