---
name: designwright-video-direction
description: Turn approved research into a provider-agnostic video production contract.
license: MIT
---

# Designwright Video Direction

Use this skill after research and factual/source evidence are ready and a human has explicitly approved video production. It converts that approval into a bounded, reviewable production contract without selecting a permanent vendor or performing rendering.

## Boundary

This skill may define what production capabilities are needed. It must not:

- render or edit media;
- install production tools;
- create or use credentials;
- invoke a paid provider merely because it is configured;
- upload media;
- authorize public or unlisted publishing;
- treat a reference video as permission to clone it.

Production approval and publishing approval are separate human decisions.

## Procedure

1. Confirm approval. Record the approved topic, audience, thesis, hook, claims/sources, requested formats, privacy constraints, cost ceiling, and unresolved questions. If production approval is absent, stop.
2. Read channel/project memory. Apply current human decisions, `VIDEO.md` or equivalent channel guidance when present, pronunciation records, visual-source policy, accessibility/caption rules, anti-patterns, and prior accepted evidence.
3. Define the narrative contract. Specify hook, sections, payoff, required factual evidence, call to action if any, and the distinct Short/Reel thesis. Do not pad runtime with filler.
4. Build the scene and shot plan. Every material segment needs a purpose, transcript span, intended visual, duration range, motion/text requirements, evidence/provenance expectation, and fallback path.
5. Apply visual-source precedence: `real evidence/source -> real screen/product capture -> deterministic/programmatic graphics -> licensed stock/archive -> generated still -> generated video`. A lower tier cannot replace a qualified higher tier only because it is easier.
6. Define voice requirements as qualities, not vendor names: character, energy, pace, pause behavior, pronunciation, emotion, and realism gate. Long-form narration should remain segment-addressable for targeted repair.
7. Request capabilities through the tool policy. For each need, state capability, quality gate, privacy class, acceptable formats, budget, and fallback. Routing follows `approved local/free -> approved free-tier external -> approved paid specialist`.
8. Record paid-escalation conditions. A paid capability is allowed only if lower-cost approved options fail or cannot satisfy a named gate. Production direction never silently spends.
9. Define acceptance evidence. Name required render(s), transcript reconciliation, audio review, visual review, synchronized audiovisual review when available, factual/source audit, format-specific checks, and independent verification.
10. Return the production contract for execution by external adapters. Do not imply that a named tool has been run.

## Required output

The production contract must contain:

- production ID or proposed stable identifier;
- approved research/source revision;
- channel/project memory revision;
- long-form and Short/Reel goals;
- narrative/section structure;
- scene/shot contracts;
- voice contract;
- visual-source precedence decisions;
- capability requests;
- cost/privacy constraints;
- generated-media disclosure requirements;
- realism and QA gates;
- unresolved decisions and risks;
- publishing boundary;
- approver and approval status.

Use the reference contracts in `references/`.

## Hard failures

Reject or stop when:

- production approval is missing;
- a material factual claim has no evidence plan;
- a reference would require copying protected identity/assets/composition;
- a paid provider is mandated without evidence-based escalation;
- private/sensitive media would be routed to an unapproved remote tool;
- the Short is specified only as a crop of the long-form video;
- public publishing is treated as implicitly authorized.

## Verification

Another agent should be able to execute the contract using different approved tools without inventing the creative direction, evidence requirements, spend authority, or publishing permission.
