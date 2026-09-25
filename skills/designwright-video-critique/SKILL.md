---
name: designwright-video-critique
description: Independently critique rendered video and audio with timestamped evidence.
license: MIT
---

# Designwright Video Critique

Use this skill only after a producer has rendered a video artifact and assembled the required evidence packet. The critic evaluates the actual media, not the producer's intent or prompt.

## Independence boundary

The critic must be distinct from the producer for material work. The critic reports findings and cannot edit media, waive hard failures, approve its own repairs, change publishing visibility, or replace the final verifier.

## Required packet

Require, as applicable:

- production contract and revision;
- final or candidate rendered video;
- final audio track or accessible audiovisual artifact;
- reconciled transcript/captions;
- shot/segment manifest;
- source/provenance map;
- generated-media markers;
- deterministic media-check results;
- known limitations;
- target long-form or Short/Reel format.

Missing material evidence is itself a finding.

## Procedure

1. Reconstruct the contract. Identify audience, hook, narrative purpose, voice requirements, visual-source rules, source/evidence obligations, cost/privacy boundaries, and format-specific constraints.
2. Check hard evidence first. Review deterministic integrity checks, transcript reconciliation, source/provenance completeness, generated-media markers, caption/safe-zone checks, and any objective audio failures.
3. Listen independently. Evaluate narration naturalness, cadence, pause/breath behavior, pronunciation, emphasis, voice consistency, chunk seams, clipping/pops, and music masking. Use an audio-capable reviewer when available; do not infer sound quality from text alone.
4. Watch independently. Inspect shot-boundary samples, regular samples, high-motion/generated/text-heavy/UI segments, and transitions. Look for irrelevant filler, repeated B-roll, fake UI, warped text, uncanny generated artifacts, temporal inconsistency, excessive motion, and mobile readability failures.
5. Perform synchronized audiovisual review when an approved model/tool can consume video plus audio. Check whether the visual supports what is being said at that moment, cuts land naturally, voice emotion fits the scene, and the piece feels intentionally edited rather than automatically filled.
6. Audit factual representation. A screenshot, chart, quote, or documentary-looking visual that implies evidence must map to a source. Generated illustrative media cannot masquerade as evidence.
7. Review pacing and format. For long-form, inspect hook speed, evidence density, dead sections, repetitive visuals, section payoff, and CTA placement. For Short/Reel, inspect first-frame comprehension, vertical composition, caption scale/safe zones, self-contained context, and payoff timing.
8. Write timestamped findings using the finding contract. Separate objective defect, likely defect, opinion, and uncertainty. Prefer the smallest repairable unit.
9. Issue `pass`, `conditional`, or `fail`. Hard failures override aggregate aesthetic strengths.
10. Hand accepted-fix requirements to a separate verifier. Do not edit or silently close findings.

## Slop detection

Explicitly inspect for recurring low-quality AI patterns:

- robotic or uniform narration cadence;
- exaggerated announcer delivery;
- repeated generic phrases/pauses;
- generic server-room/robot/laptop B-roll unrelated to evidence;
- repeated zoom templates or transitions;
- random visual change on every sentence;
- filler stock footage;
- generated screenshots or fake product UI;
- morphing text;
- uncanny synthetic people/hands/objects;
- subtitles covering meaningful UI;
- audio seams between regenerated segments;
- music or effects masking speech.

A pattern match is a finding; severity depends on prominence and contract.

## Required finding shape

Every material finding includes:

- stable finding ID;
- severity;
- classification: objective defect | likely defect | opinion | uncertainty;
- timestamp start/end;
- shot/segment ID where available;
- problem;
- why it matters;
- evidence;
- bounded proposed change;
- unchanged invariants;
- owner;
- status.

See `references/finding-contract.md`.

## Hard failures

The artifact cannot be review-ready with unresolved:

- materially robotic/synthetic narration;
- material visual/narration mismatch;
- misleading generated media presented as evidence;
- unsupported factual claim;
- unreadable required captions;
- severe audio clipping/discontinuity;
- visibly broken generated text/UI in a prominent shot;
- severe temporal artifact in a prominent generated shot;
- key mobile safe-zone failure;
- missing required critique evidence;
- producer self-approval without independent verification.

## Verification handoff

The critic hands the verifier clean reproduction instructions, accepted findings, timestamps, repaired-unit expectations, unchanged invariants, and required evidence. The verifier reruns checks against the repaired render rather than trusting screenshots or producer claims.
