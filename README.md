# Designwright Agent Plugins v1

Designwright is a skills-first package in the portable Agent Plugins v1 format. It carries a reusable design workflow without selecting a renderer, changing a product repository, or claiming public name, trademark, domain, or package-name clearance.

## Package boundary

This package provides exactly five portable Agent Skills:

- `designwright-init` maps a project and proposes metadata without editing product code.
- `designwright-direction` turns project evidence and user goals into an approved design direction.
- `designwright-component-intelligence` records ordered, evidence-backed component selection.
- `designwright-evidence-loop` runs the bounded design-to-verification workflow.
- `designwright-independent-critique` gives a separate reviewer a structured critique and closure contract.

Skills are discovered from the immediate child directories of `skills/`. The package contains no MCP server, native Hermes `plugin.yaml`, Python tool handler, remote service, credential, telemetry, or client-specific extension. The only portable component type shipped in v0.1.0 is Agent Skills.

The workflow is project-adaptive: project identity, canonical design memory, local components, tokens, constraints, and human decisions outrank central guidance. Component discovery always follows:

`project-local -> approved private -> approved curated external -> new`

A later tier cannot bypass a qualified earlier tier. New implementation requires evidence that no qualified candidate exists and explicit approval.

## Local-first validation

Run these commands from the repository root before sharing or installing the package:

```text
python tools/validate_portable_plugin.py
hermes plugins doctor --ci .
```

The first command checks the manifest values, the exact five skills, frontmatter name matches, and the deliberate absence of MCP, native-plugin, and workflow files. The Hermes command exercises the installed runtime's portable-plugin validation. Both are intended to run locally; this bootstrap intentionally adds no GitHub Actions workflow.

## Install and enable with Hermes

Install the public GitHub repository as a disabled portable plugin, then enable it only after reviewing the package:

```text
hermes plugins install wkimball1/designwright --no-enable
hermes plugins enable designwright
```

`--no-enable` is intentional. Installation and enabling are separate decisions. The package does not request tool overrides or any additional capability.

## Designwright and Design Studio are separate

This repository is the reusable design-intelligence package. `wkimball1/Design-studio` is a separate product and future editable renderer/environment. Designwright does not control it, modify it, or ship its source, prompts, UI, or assets. Software Factory governance remains the authority for project orchestration, approvals, QA, merge, release, deployment, credentials, and spend.

## Evidence-first operating model

Use the skills as a bounded sequence rather than as a visual-theme generator:

1. Inventory the project and state uncertainty before proposing writes.
2. Frame the user job, project identity, constraints, and approved references.
3. Search component sources in precedence order and record rejected candidates.
4. Implement only an approved, bounded slice.
5. Run the real app or fixture, exercise the critical path, capture required states, inspect runtime evidence, and critique independently.
6. Fix only accepted findings, then verify from clean instructions.

A screenshot alone is not proof. Material work separates implementer, critic, and verifier roles, uses actionable evidence, and limits critique/fix churn.
