---
name: designwright-verify-visual
description: Verify a built UI with real browser screenshots. Capture required states at the viewport matrix, inspect the evidence, fix defects, and re-shoot until clean. Selects the client's Playwright MCP — no renderer or MCP server is bundled. Use after any UI implementation, before calling it done.
license: MIT
---

# Designwright Verify Visual

Gives the agent eyes. A UI is not done when the code is written; it is done
when captured evidence shows it renders correctly. This skill selects the
client's browser automation (Playwright MCP or equivalent) — it bundles no
renderer, MCP server, credential, or remote service.

## When to use

Use it after any UI implementation or material UI change, before reporting
completion. Use it again after any fix that touches layout, styling, or
responsive behavior. Do not use it for video rendering.

## Prerequisites

The client must expose browser automation (Playwright MCP or equivalent).
If none is available, stop and report that visual verification is blocked —
do not claim the UI is verified.

## Procedure

1. **Serve the real surface.** Screenshot the actual built page or app, not a
   mock or a cropped fragment. If the UI needs state (signed in, data
   loaded, error condition), establish that state first.
2. **Capture the required states.** At minimum: default view, primary
   interaction completed (e.g., row sorted, filter applied, dialog open),
   and the empty state. Include the error state where one exists.
3. **Capture the viewport matrix.** 390px (mobile), 768px (tablet), 1440px
   (desktop) — each in light and dark mode where the product supports themes.
4. **Inspect the evidence.** Read every screenshot and hunt these defect
   classes: overflow and clipped text, misaligned baselines, inconsistent
   spacing rhythm, low-contrast text, broken dark-mode surfaces, charts that
   render flat or fail to repaint on theme toggle, dead or misaligned
   controls, and mobile layouts that squeeze instead of re-patterning.
5. **Fix and re-shoot.** Batch all findings into one fix pass, then
   re-capture the affected states and viewports. Repeat until a full matrix
   capture is clean. Cap at three cycles; if defects persist, escalate to
   the user with the evidence attached.
6. **Hand off the evidence.** Keep the final clean captures with the
   deliverable. Note anything that could not be captured and why.

## Acceptance contract

A UI passes when: every required state is captured at every matrix viewport,
no defect from the hunt list is visible, interactions photographed actually
work (the screenshot proves the state, the control proves the behavior),
and the verifier role is separate from the implementer role.
