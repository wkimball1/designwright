---
name: designwright-init
description: Map a project before proposing design changes.
license: MIT
---

# Designwright Init

Use this skill before a design change touches an unfamiliar project. Produce a read-only, evidence-backed project map and a metadata proposal; do not install dependencies, rewrite product code, create a registry, or invent product identity.

## When to use

Use it for a new project, a new worktree, a missing or stale design record, or any change where routes, tokens, components, test commands, or ownership are uncertain. Do not use it as permission to apply a redesign or to “clean up” unrelated files.

## Procedure

1. Establish the boundary. Record the repository and worktree, intended non-production target, owner, safety limits, and the exact change being considered. Stop and surface a conflict instead of guessing which checkout or environment is authoritative.
2. Inventory the product surface. Read project documentation and manifests, then map routes or screens, entry points, layout shells, stateful journeys, styles, tokens, component directories, asset locations, and existing design records. Record paths and evidence for each observation.
3. Inventory verification. Find the documented build, unit, integration, browser, lint, and formatting commands. Record declared viewports, accessibility expectations, fixtures, and known test gaps. Do not run a command that would mutate data or production state merely to fill a blank.
4. Read project memory before central guidance. Reconcile `.design/project.json`, `DESIGN.md`, token files, component usage, decision logs, and current human decisions. Current project decisions outrank stale generated documents; verified code evidence outranks an unsupported assumption.
5. Map component sources without selecting one. Record local component roots and usage sites, approved private sources, approved curated external sources, and the policy for a new primitive. Preserve the order `project-local -> approved private -> approved curated external -> new` for later selection.
6. Surface uncertainty and conflict. Distinguish observed, inferred, missing, and contradictory facts. A “no signals found” result is a reportable result, not permission to invent a brand, layout, component, or command.
7. Prepare a proposal only. If a write is later approved, enumerate the intended `.design/` metadata paths, generated projections, conflicts, and rollback. Show the complete write set before any file change; the default result is a report, not a write.

## Report contract

Return a compact report with:

- scope and safety boundary;
- evidence-backed project identity, users, jobs, journeys, and page or screen families;
- routes, tokens, component paths, asset paths, and design-memory sources;
- commands, environments, viewports, and verification readiness;
- component-source tiers and unresolved ownership or licensing questions;
- observed facts, inferences, conflicts, and unknowns;
- proposed metadata writes, explicit non-actions, and rollback needs.

Every item should point to a file, command declaration, or human decision. Label assumptions and hypotheses in their values.

## Guardrails

Keep product identity, content, tokens, component decisions, references, and exceptions project-owned. Central guidance supplies method and contracts; it must not recolor or homogenize products. Design Studio is a separate future renderer or product, not the control plane. Existing project governance remains authoritative for approval, isolation, QA, merge, release, deployment, credentials, and spend.

## Verification

The initialization result is complete only when another agent can identify the inspected scope, reproduce the inventory, see every uncertainty, and review the exact proposed write set. A clean read-only diff is required when no write was approved. No package install, registry write, production action, or unsupported design claim may appear in the report.
