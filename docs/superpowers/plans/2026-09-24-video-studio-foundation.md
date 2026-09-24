# Designwright Video Studio Foundation Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Add provider-agnostic video direction and audiovisual critique skills to the portable Designwright plugin without bundling a renderer, model, credential, or publishing runtime.

**Architecture:** Designwright remains the decision/evidence layer. Two new portable Agent Skills define production direction and independent audiovisual critique; external production and review tools remain replaceable adapters governed by the Video Studio specs.

**Tech Stack:** Agent Plugins v1 manifest, Markdown Agent Skills, Python package validator.

**Spec:** `docs/video-studio/`

## Global Constraints

- Bump the portable plugin contract from 0.1.1 to 0.2.0.
- Enforce exactly seven approved Agent Skills.
- Add no MCP server, provider credential, renderer, remote service, native Hermes plugin file, or GitHub Actions workflow.
- Prefer free/local production capabilities before paid providers.
- Video production approval never grants public-publishing permission.
- Video critique must evaluate rendered audiovisual evidence and remain independent from the producer.

## Review Focus

1. An eighth accidental skill directory must fail validation.
2. A video skill whose frontmatter name differs from its directory must fail validation.
3. Video direction must not authorize a paid provider or public publish.
4. Video critique must not edit media or self-verify fixes.
5. Existing five skill names and package boundaries must remain unchanged.

---

### Task 1: Add video direction contracts

Create `skills/designwright-video-direction/SKILL.md` plus focused references for production, shots, and capability requests. Verify the skill is provider-agnostic and free/local-first.

### Task 2: Add audiovisual critique contracts

Create `skills/designwright-video-critique/SKILL.md` plus review, finding, and verifier-handoff references. Verify it requires rendered evidence and timestamped findings.

### Task 3: Version the portable plugin contract

Update `plugin.json`, `README.md`, `CHANGELOG.md`, and `tools/validate_portable_plugin.py` for version 0.2.0 and exactly seven skills.

### Task 4: Validate package consistency

Run the portable validator against the resulting branch contents. Confirm the seven-skill manifest passes and package-boundary checks still reject MCP/native-plugin/workflow content.
