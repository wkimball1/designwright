# Designwright Video Studio — Agent Team Handoff

Status: proposed implementation handoff  
Date: 2026-09-24

## Mission

Extend the Designwright portable plugin so it can direct and independently critique video production while keeping renderers, TTS engines, editors, transcription systems, multimodal reviewers, and upload services replaceable.

Do not turn Designwright into a monolithic editor.

Read in this order:

1. `docs/video-studio/README.md`
2. `docs/video-studio/PRD.md`
3. `docs/video-studio/ARCHITECTURE.md`
4. `docs/video-studio/TOOL-POLICY.md`
5. `docs/video-studio/REALISM-QA.md`
6. `docs/video-studio/LEARNING-LOOP.md`
7. existing Designwright skill contracts
8. `tools/validate_portable_plugin.py`

## Current repository constraint

Designwright v0.1.1 intentionally validates exactly five skills:

- designwright-init;
- designwright-direction;
- designwright-component-intelligence;
- designwright-evidence-loop;
- designwright-independent-critique.

The validator treats any additional immediate skill directory as an error.

Therefore adding Video Studio skills is a deliberate plugin-contract/version change, not a file-drop.

## Proposed first plugin milestone

Add two portable skills:

### designwright-video-direction

Responsibilities:

- convert approved research/script/channel evidence into a video production contract;
- define scene/shot intent;
- define voice requirements;
- define visual-source precedence;
- define tool capabilities required;
- define acceptance evidence;
- prohibit hidden paid escalation;
- prohibit public publishing authorization.

Must not:

- render;
- upload;
- require one named provider;
- create credentials;
- silently install tools.

### designwright-video-critique

Responsibilities:

- consume rendered-video evidence;
- enforce the Realism QA contract;
- produce timestamped findings;
- separate objective defects, likely defects, opinions, and uncertainty;
- identify the smallest repairable unit;
- preserve unchanged invariants;
- hand off to a separate verifier.

Must not:

- edit source/media;
- waive hard failures;
- approve its own fixes;
- publish.

## Supporting reference contracts

Each new skill should ship focused references rather than becoming an oversized SKILL.md.

Likely references:

```text
skills/designwright-video-direction/
  SKILL.md
  references/
    production-contract.md
    shot-contract.md
    channel-video-memory.md
    tool-capability-request.md

skills/designwright-video-critique/
  SKILL.md
  references/
    audiovisual-review.md
    slop-patterns.md
    finding-contract.md
    verification-handoff.md
```

Exact decomposition may change if a smaller clearer structure is found.

## Versioning

Because the plugin contract changes from five to seven skills:

- bump plugin version;
- update README claims;
- update validator expected manifest/version;
- update validator required skills;
- update CHANGELOG;
- run portable validation;
- run Hermes plugin doctor where available.

Do not weaken validation merely to allow arbitrary future directories.

## Parallel agent workstreams

The following workstreams can be researched independently before integration.

### Workstream A — Direction skill

Deliver:

- proposed SKILL.md;
- production/shot schema;
- examples for long-form and Short;
- tests/validation expectations.

### Workstream B — Critique skill

Deliver:

- proposed SKILL.md;
- timestamped finding contract;
- audiovisual review rubric;
- hard-failure list;
- verifier handoff.

### Workstream C — Free/local tool benchmark

Do not edit Designwright production contracts yet.

Benchmark candidates for:

- transcription;
- TTS;
- deterministic editing;
- editorial assembly;
- motion graphics;
- audiovisual QA.

Output evidence and recommended registry records.

### Workstream D — Realism fixture suite

Create synthetic/non-sensitive fixtures that intentionally contain:

- robotic voice;
- mispronunciation;
- TTS seam;
- clipping;
- bad mix;
- unrelated B-roll;
- repeated B-roll;
- broken generated text;
- fake UI;
- generated temporal artifact;
- subtitle overflow;
- narration/visual mismatch.

Use these to evaluate critic/reviewer tools.

### Workstream E — Learning data model

Design portable JSON/Markdown schemas for:

- production run;
- shot;
- voice segment;
- tool result;
- human feedback;
- QA finding;
- rule proposal.

Do not create a remote database dependency in the Designwright plugin.

## Integration rule

External tools are not added to Designwright merely because they benchmark well.

What Designwright may adopt:

- capability vocabulary;
- selection rules;
- evidence formats;
- critique rules;
- adapter expectations;
- proven reusable production heuristics.

What remains external:

- binaries;
- model weights;
- credentials;
- rendering runtime;
- upload runtime;
- paid-provider clients.

## First proving experiment

Before broad implementation, produce one controlled 60–90 second technical explainer using only non-sensitive source material.

Required comparison:

### Voice

At least two free/local candidates.

### Editing

At least:

- video-use-style editorial path;
- deterministic FFmpeg operations.

### Graphics

At least one Remotion/json-render composition.

### QA

At least:

- deterministic media checks;
- audio-only AI review;
- visual-only AI review;
- synchronized audiovisual AI review where supported;
- independent verifier.

### Result

Produce:

- final render;
- QA packet;
- rejected/replaced segments;
- cost report;
- tool comparison;
- human review notes.

Do not promote tools or rules until evidence from this experiment is reviewed.

## Completion criteria for first plugin milestone

The milestone is complete only when:

- the two skills are valid portable Agent Skills;
- plugin validation knows about exactly the intended skills;
- README and CHANGELOG accurately describe the new scope;
- direction skill is provider-agnostic;
- critique skill requires rendered audiovisual evidence;
- free/local-first routing is represented in contracts;
- public publishing remains human-authorized;
- no provider credential is introduced into Designwright;
- external production tools remain adapters;
- an independent reviewer confirms the new skills do not weaken existing provenance/evidence/governance boundaries.
