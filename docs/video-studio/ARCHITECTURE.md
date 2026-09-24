# Designwright Video Studio — Architecture

Status: proposed  
Date: 2026-09-24

## 1. Architectural principle

Designwright owns decisions and evidence. Replaceable tools own execution.

Do not tightly couple Designwright to OpenMontage, video-use, ffmpeg-skill, Remotion, Voicebox, ElevenLabs, or any single generation provider.

Represent production needs as capabilities and contracts.

## 2. High-level pipeline

```text
research
  -> human production approval
  -> production brief
  -> Designwright video direction
  -> storyboard / shot contract
  -> capability routing
  -> voice + assets + screen capture + graphics + selective generation
  -> editorial assembly
  -> deterministic render
  -> audiovisual realism QA
  -> targeted correction loop
  -> independent verification
  -> long + short + thumbnail + metadata package
  -> private upload
  -> human review
  -> optional public publish
  -> performance + feedback ingestion
  -> evidence-backed learning
```

## 3. Proposed Designwright additions

### designwright-video-direction

Creates the approved video design contract.

Inputs:

- research packet;
- factual/source evidence;
- target audience;
- channel memory;
- requested formats;
- reference packet;
- available capability registry;
- cost/privacy constraints.

Outputs:

- narrative thesis;
- hook contract;
- section structure;
- scene/shot plan;
- voice requirements;
- visual-source priority;
- caption/motion/audio rules;
- generated-media allowance;
- acceptance evidence;
- unresolved decisions.

It must not render or invoke paid providers.

### designwright-video-critique

Consumes the rendered artifact plus evidence packet.

Produces evidence-backed findings using:

`problem -> why it matters -> evidence -> proposed change -> unchanged invariants`

It cannot edit.

### video verifier

The verifier is distinct from the producer and critic.

It reruns required checks after accepted fixes and decides pass/fail for the review-ready gate.

### production capability registry

Stores approved execution options by capability rather than vendor.

Example capabilities:

- transcription;
- TTS;
- voice cleanup;
- screen capture;
- stock/archive retrieval;
- generated image;
- generated video;
- timeline editing;
- silence removal;
- caption burn-in;
- programmatic graphics;
- audio mixing;
- loudness normalization;
- render;
- thumbnail composition;
- upload.

## 4. External adapter model

Each adapter should publish metadata such as:

```text
capability
tool/provider
version
local_or_remote
license
privacy_class
credential_required
supported_formats
hardware_requirements
quality_evidence
cost_model
latency_evidence
failure_rate
known_limitations
approved_scope
```

No adapter is permanently preferred.

## 5. Candidate execution stack

The initial research/prototype set may include:

### Editorial reasoning
- browser-use/video-use
- OpenMontage

### Deterministic video/audio operations
- ffmpeg-skill
- FFmpeg directly where appropriate

### Programmatic motion graphics
- Remotion
- json-render Remotion renderer
- Manim for suitable diagram/math cases

### Local transcription
- faster-whisper
- whisper.cpp

### Local/free TTS
- Voicebox as a workbench/router
- Qwen-family TTS engines where supported
- Chatterbox variants where supported
- Kokoro where appropriate

### Paid fallback
- premium TTS or video/image providers only after local/free failure is documented.

These are candidates, not architectural dependencies.

## 6. Production artifacts

Every run should receive a stable production ID.

Suggested artifact tree:

```text
runs/<run-id>/
  research/
  sources/
  script/
  direction/
  storyboard/
  voice/
  assets/
  screen-captures/
  graphics/
  generated-media/
  timeline/
  renders/
    long/
    short/
  thumbnails/
  captions/
  qa/
  verification/
  metadata/
  publish/
  manifest.json
```

The manifest ties artifacts to:

- source revision;
- generation prompt/config;
- provider/tool version;
- timestamps;
- cost;
- hashes;
- rights/provenance;
- accepted/rejected status.

## 7. Shot model

Each shot/segment should have a stable ID and record:

- narrative purpose;
- transcript span;
- planned duration;
- actual duration;
- visual type;
- source/provenance;
- generated status;
- tool/provider;
- motion level;
- text/caption load;
- QA findings;
- revision history;
- final acceptance.

This enables targeted repair.

## 8. Reference handling

Reference videos may inform:

- pacing;
- density;
- high-level shot patterns;
- hierarchy;
- transition frequency;
- use of evidence;
- caption behavior;
- structural rhythm.

Do not reproduce:

- scripts;
- branding;
- exact sequences;
- assets;
- signature visual compositions;
- copyrighted footage without permission.

Preserve original transformation records.

## 9. Privacy classes

Capabilities should declare whether media leaves the machine.

Suggested classes:

- LOCAL_ONLY;
- REMOTE_NON_SENSITIVE;
- REMOTE_APPROVED_MEDIA;
- PAID_REMOTE.

Routing must respect project/channel privacy settings.

## 10. Revision strategy

Never default to full regeneration.

QA findings should resolve to the smallest replaceable unit:

- word/pronunciation;
- narration sentence;
- voice segment;
- caption;
- overlay;
- shot;
- scene;
- section;
- thumbnail;
- Short composition.

Full rerender is acceptable; full creative regeneration is not required when a bounded fix exists.

## 11. Failure handling

A failed provider/tool should:

1. preserve completed artifacts;
2. record failure evidence;
3. try the next approved adapter when safe;
4. avoid duplicate paid requests unless retry policy permits;
5. surface unresolved failures rather than fabricate completion.

## 12. Publication boundary

Upload is a separate adapter/capability.

It receives only verified artifacts.

Default output visibility is private.

The uploader does not own the public-publish decision.
