---
name: layout-clarity
description: Improve text-heavy or AI-looking interfaces by replacing redundant explanatory copy with clear hierarchy, grouping, and interaction cues. Use when designing or refining UI, not for general prose shortening.
---

# Layout Clarity

Make the next action and the relationships between elements understandable through the interface itself. The goal is clarity, not a lower word count.

## Work from the actual task

Inspect the screen, implementation, or supplied design. Identify its audience, primary action, and meaningful states. If only a screenshot is available, distinguish visible evidence from assumptions; do not claim implemented behavior was tested.

For each secondary label or paragraph, ask: **What does the user learn here that the layout or a precise control label does not already communicate?**

- Remove duplication, decorative slogans, and narration of obvious controls.
- Replace ambiguity with grouping, alignment, spacing, heading hierarchy, or a specific action label before adding another paragraph.
- Keep information that changes a decision: scope, units, time period, uncertainty, price, consequences, prerequisites, or recovery steps.
- Move genuinely optional detail into an accessible disclosure only if users can predict what it contains. Do not hide information required before a decision.

Read [the examples](references/examples.md) when choosing a concrete transformation.

## Preserve meaning and access

Do not remove visible form labels in favor of placeholders, accessible names, errors and remedies, destructive-action consequences, consent/legal/safety information, or unfamiliar-domain guidance simply to make a screen look cleaner. An icon alone is not automatically clearer. Do not rely on color, hover, position, or animation as the sole carrier of meaning. Keep status labels where the state would otherwise be ambiguous.

Respect the user's design language, product scope, and supported interaction patterns. This skill does not authorize publishing, changing permissions, adding tracking, or rewriting unrelated product behavior.

## Apply and verify

Make the smallest coherent change that fixes the hierarchy. Preserve the information architecture unless the task calls for redesign. Test realistic content lengths and relevant empty, loading, error, disabled, and success states; do not create states the product does not have.

For implementation work, check the primary task at a narrow and wide viewport, keyboard order and focus visibility, accessible names, and touch-friendly discovery without hover. A reviewer should be able to identify the action, object, state, and important consequence without reading decorative prose.

Report the key changes, what information was preserved, and which checks actually ran. Do not invent usability scores or claim that deleting copy proves better usability. Use [evaluation cases](references/evaluation-cases.md) for a bounded review when needed.
