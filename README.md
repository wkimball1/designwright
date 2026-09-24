# Designwright Agent Plugins v1

Designwright is a skills-first package in the portable Agent Plugins v1 format. It carries reusable design and video-direction workflows without selecting a renderer, changing a product repository, or claiming public name, trademark, domain, or package-name clearance.

## Package boundary

This package provides exactly seven portable Agent Skills:

- `designwright-init` maps a project and proposes metadata without editing product code.
- `designwright-direction` turns project evidence and user goals into an approved design direction.
- `designwright-component-intelligence` records ordered, evidence-backed component selection.
- `designwright-evidence-loop` runs the bounded design-to-verification workflow.
- `designwright-independent-critique` gives a separate reviewer a structured critique and closure contract.
- `designwright-video-direction` turns approved research and channel evidence into a provider-agnostic video production contract.
- `designwright-video-critique` independently reviews rendered audiovisual evidence with timestamped findings and verifier handoff.

Skills are discovered from the immediate child directories of `skills/`. The package contains no MCP server, native Hermes `plugin.yaml`, Python tool handler, remote service, credential, telemetry, or client-specific extension. The only portable component type shipped in v0.2.0 is Agent Skills.

The workflow is project-adaptive: project identity, canonical design memory, local components, tokens, constraints, and human decisions outrank central guidance. Component discovery always follows:

`project-local -> approved private -> approved curated external -> new`

A later tier cannot bypass a qualified earlier tier. New implementation requires evidence that no qualified candidate exists and explicit approval.

## Local-first validation

Run these commands from the repository root before sharing or installing the package:

```text
python tools/validate_portable_plugin.py
hermes plugins doctor --ci .
```

The first command checks the manifest values, the exact seven skills, frontmatter name matches, and the deliberate absence of MCP, native-plugin, and workflow files. The Hermes command exercises the installed runtime's portable-plugin validation. Both are intended to run locally; this bootstrap intentionally adds no GitHub Actions workflow.

## Install and enable with Hermes

Install a reviewed, immutable Git commit as a disabled portable plugin. Read the package back with Plugin Doctor before enabling it:

```text
hermes plugins install wkimball1/designwright --ref <reviewed-commit> --no-enable
hermes plugins doctor --ci <installed-package-directory>
hermes plugins enable designwright
```

`--ref <reviewed-commit>` and `--no-enable` are intentional. Installation, read-back, and enabling are separate decisions. The package does not request tool overrides or any additional capability. Updating a plugin is another reviewed installation decision; do not use a generic updater or assume marketplace/client refresh behavior.

## Comparative external references

The Direction skill can use an owner-authorized external design-reference collection to inform a project-owned initial `DESIGN.md`. It does not import a brand system or turn a reference library into a theme selector.

- record an immutable source pin plus license/permission evidence before using it;
- fail closed if source provenance, authorship, or permission cannot be verified;
- retain only original, principle-level observations outside the target `DESIGN.md`;
- require project evidence, an original transformation, and an acceptance gate for every material influence;
- cap each reference to one adopted principle and at most one third of the packet's influence;
- require an independent, blind origin check before the resulting `DESIGN.md` can guide implementation.

See `skills/designwright-direction/references/comparative-reference-intake.md` for the complete protocol. It forbids reference-specific tokens, fonts, assets, copy, code, component APIs, signature layouts, and interaction patterns even when a project owner documents a separate broader right.

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


## Video Studio foundation

Designwright v0.2.0 adds two provider-agnostic video skills while keeping production engines external:

- `designwright-video-direction` creates the approved production, scene, shot, voice, evidence, privacy, and cost contract.
- `designwright-video-critique` independently evaluates rendered audio/video evidence and produces timestamped, bounded findings for a separate verifier.

The subsystem is specified in `docs/video-studio/`. It prefers qualified free/local capabilities before paid providers, keeps public publishing behind an explicit human boundary, and does not bundle a renderer, TTS engine, transcription engine, generative-media model, upload service, or provider credential.

The existing evidence-first separation remains: Designwright decides what good looks like and verifies evidence; replaceable external adapters perform production work.
