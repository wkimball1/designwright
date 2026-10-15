---
name: designwright-data-density
description: Design or review data-dense UI: tables, dashboards, and screens where data is the interface. Covers density, empty/loading/error states, truncation, sorting and filtering, pagination, keyboard access, and chart annotation. Use for any screen dominated by data.
license: MIT
---

# Designwright Data Density

Data-dense screens fail differently from marketing pages: they fail on ten
thousand rows, on the empty Monday morning, on the truncated identifier the
user needed. This skill is the checklist that keeps them production-ready.

## When to use

Use it when designing or reviewing any screen where data dominates: tables,
dashboards, audit logs, reconciliation views, admin lists. Apply it during
the build (via `designwright-ui-loop` step 4) or as a standalone review of
an existing screen.

## Checklist

**Tables**
- Columns: every column earns its place; truncate with ellipsis and full
  value on hover/focus, never mid-word clipping.
- Headers: sticky on scroll; sort indicators visible and unambiguous.
- Rows: tabular numerals, mono for identifiers, consistent row height.
- Selection and actions: row selection, bulk actions, and per-row actions
  are keyboard reachable.

**States (every data surface needs all four)**
- Loading: skeletons that match the final layout, not spinners alone.
- Empty: explains why it is empty and what to do next — never a blank panel.
- Error: names the failure, preserves context, offers retry.
- Partial: shows what loaded, marks what did not.

**Scale**
- Pagination, virtualized scrolling, or explicit row caps for large sets —
  chosen deliberately and stated in the direction, not discovered in prod.
- Sorting, filtering, and search are server-honest: the UI never implies it
  searched what it did not fetch.

**Charts**
- Every chart has a point of view: annotate what matters (incidents,
  threshold crossings, expected dips) — a chart without annotation is
  decoration.
- Axes labeled, units stated, time ranges explicit. No truncated axes
  without a visible break marker.

**Density and input**
- Information density matches the operator's job; density is a feature
  for ops tools, a bug for onboarding.
- All data interactions are keyboard accessible with visible focus.

## Review contract

Return: the screen reviewed; checklist items passed, failed, or not
applicable (with one-line reasons for failures); and the fixes required
before the screen is production-ready. Failures are defects, not polish.
