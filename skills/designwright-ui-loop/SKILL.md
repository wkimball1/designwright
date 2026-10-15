---
name: designwright-ui-loop
description: "Run the standardized UI build loop end to end: pick a surface mode, build through the designwright skills, pass the craft gate, take an independent critique, verify visually, and log decisions. Use for ANY UI task."
license: MIT
---

# Designwright UI Loop

The mandatory conveyor belt for UI work. It sequences the designwright skills
into one bounded loop so agent teams produce consistent, production-ready
interfaces without per-project improvisation.

## When to use

Use it for any UI task: new screens, redesigns, components, polish passes.
Do not use it for video work (see `designwright-video-direction`) or for
non-visual engineering.

## Procedure

1. **Pick the mode from the surface, not the product.** State it in one line.
   - **Operate** (default): dashboards, admin tools, data tables, settings,
     editors. The visitor completes a task — scanability, consistency, and
     native expectations outrank expression.
   - **Persuade**: landing pages, marketing, pricing. The visitor decides.
   - **Read**: docs, changelogs, help. The visitor understands something.
2. **Establish the project record.** Run `designwright-init` if the project
   has no `.design/project.json`. For greenfield identity or material IA
   change, run `designwright-direction`: it presents two or three genuinely
   different directions — layout thesis, color/type/spacing roles, responsive
   rules — and the loop PAUSES for your pick before any code is written.
   For constrained changes, reuse the approved direction.
3. **Select components in order.** Run `designwright-component-intelligence`.
   `project-local -> approved private -> approved curated external -> new`.
   A later tier never bypasses a qualified earlier tier.
4. **Implement the approved slice.** Build only what the direction approves.
   For data-dense screens, apply `designwright-data-density` during the
   build. Use project-owned shared tokens when they exist; record new tokens
   in the project record (start from `templates/design-tokens.template.json`).
5. **Pass the craft gate before calling it done.** No UI edit ships without it:
   - no lorem ipsum — every label, number, and empty state is realistic;
   - type has exactly three roles (display, body, data/mono) with tabular
     numerals on every figure;
   - status is a color language: dot + text badge, never color alone;
   - contrast meets WCAG AA on every text/background pair;
   - dark mode is a designed second theme, not an inversion;
   - mobile is an intentional layout (bottom tab bar or equivalent native
     pattern), not a squeezed desktop.
   Fix every gate failure in one batch. One pass, then stop. If the
   `impeccable` skill is installed alongside designwright, its audit
   playbook may be used as the mechanical half of this gate; the checklist
   above remains the acceptance authority.
6. **Take an independent critique.** Run `designwright-independent-critique`
   with a reviewer role separate from the implementer. Fix only accepted
   findings. Limit churn: critique once, fix once.
7. **Verify visually.** Run `designwright-verify-visual`: capture required
   states at the viewport matrix, inspect the evidence, fix, re-shoot.
   A screenshot alone is not proof — the verifier role stays separate.
8. **Log decisions.** Append to the project's `.design/decisions.md`: date,
   decision, rationale, alternatives rejected, approver. Future sessions
   read it instead of re-litigating settled choices.

## Default quality bar

Unless the project record overrides them, these hold:
- Zero external requests: no CDN, webfonts, or remote images. System font
  stack, hand-drawn inline SVG.
- Every control works: sort, filter, search, toggles. A dead control is
  a defect.
- Copy is domain-native: name real concepts from the project's domain,
  not generic placeholders.

Project constraints outrank these defaults. Central guidance supplies
method; the project supplies identity.

## Report contract

Report: the mode and one-line design thesis; the direction and component
sources used; what the craft gate, critique, and visual verification each
found and what was fixed (counts suffice); absolute paths to deliverables;
and anything unverified. Do not ask the user to do the critiquing — the
loop is the review.
