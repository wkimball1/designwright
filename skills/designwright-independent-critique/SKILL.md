---
name: designwright-independent-critique
description: Critique rendered work with evidence and role separation.
license: MIT
---

# Designwright Independent Critique

Use this skill after an implementer has produced a bounded rendered result and its evidence bundle. Judge the result against the approved project contract and observable user experience, not against the implementer's explanation. The critic cannot edit, waive evidence, approve its own work, or turn taste into an unsupported universal rule.

## Independence boundary

The critic must be distinct from the implementer for material work. Where practical, review neutralized rendered evidence before reading implementation rationale. The verifier is a separate role again: the critic identifies and prioritizes problems; the verifier reproduces the path and decides whether gates pass.

## Procedure

1. Confirm the packet. Check source revision, approved direction, project memory revision, component decision IDs, route and state matrix, viewport list, runtime commands, screenshots, interaction trace, DOM or accessibility evidence, console and network results, and known limitations. Missing or contradictory evidence is a finding.
2. Reconstruct the user job. Identify the named user, critical action, content hierarchy, protected behavior, responsive policy, accessibility requirements, and project identity. Do not score a surface that has no stated job or acceptance contract.
3. Inspect hard gates first. Check critical-path completion, keyboard and focus path, accessible names and roles, required states, responsive overflow, component provenance and precedence, console or request failures, and evidence integrity. A hard failure overrides aesthetic strengths or an aggregate score.
4. Evaluate the observable result across job clarity, information hierarchy, product specificity, system consistency, structural diversity, component reuse, responsive quality, accessibility, interaction completeness, craft, technical UX, and evidence integrity. Tie every nontrivial judgment to an artifact or label it as an opinion.
5. Write actionable findings. Use exactly this chain: `problem -> why it matters -> evidence -> proposed change -> what remains unchanged`. Include severity, stable finding ID, route or state, viewport, locator or region, and owner. Prefer the smallest change that resolves the observed problem without erasing project identity.
6. Check reference and source discipline. Flag copied or untraceable assets, missing permission labels, pixel-cloning behavior, unapproved external components, skipped earlier component tiers, and new primitives without `no-qualified-candidate` evidence and human approval.
7. Issue a bounded recommendation. Mark the packet pass, fail, or conditional on named fixes. Recommend no more than one default critique/fix cycle; a second is only for unresolved high severity. Escalate a third cycle or a direction conflict to a human instead of adding churn.
8. Hand off without editing. Return the findings, hard-failure list, evidence gaps, unchanged invariants, required fixes, and verification instructions. Do not modify source, rewrite baselines, or silently close findings.

## Finding format

```text
Finding: VIS-<stable-id>
Severity: blocker | high | medium | low
Scope: <route, state, viewport, or component>
Problem: <observable defect>
Why it matters: <user, accessibility, responsive, identity, or technical consequence>
Evidence: <artifact path or ID, locator or region, viewport, and environment>
Proposed change: <bounded corrective action>
Unchanged: <behavior, destination, token, copy, or other invariants>
Owner: implementer | designer | project owner
Status: open
```

A finding without reproducible evidence remains an uncertainty, not a claimed defect. A finding that requires a new component or external source must reference the component decision process and its precedence record.

## Verification handoff

The verifier receives clean reproduction instructions, the accepted-finding list, the original contract, and the exact evidence requirements. The verifier must rerun the path and confirm closure rather than trusting a changed screenshot. The final result cannot infer approval from a critic pass; project governance and any human approval boundary still apply.
