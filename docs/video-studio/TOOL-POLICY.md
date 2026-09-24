# Designwright Video Studio — Tool Policy

Status: proposed  
Date: 2026-09-24

## 1. Purpose

Video Studio must use the best approved tool for a capability without making Designwright dependent on one vendor, model, repository, or provider.

The default policy is:

`approved local/free -> approved free-tier external -> approved paid specialist`

Quality is a hard gate. "Free" does not justify publishing poor output, but paid escalation must be evidence-backed rather than automatic.

## 2. Designwright owns selection, not implementation

Designwright defines:

- the capability required;
- quality and realism gates;
- privacy constraints;
- licensing constraints;
- budget;
- acceptable latency;
- evidence required to qualify a tool;
- fallback order.

External adapters implement the work.

Do not encode a rule such as "always use Voicebox" or "always use OpenMontage." Encode "TTS capability" and select among approved candidates using current evidence.

## 3. Capability registry

Every candidate should have a versioned registry record:

```text
tool_id
capability
name
source_url
version_or_commit
local_or_remote
open_source_license
commercial_use_notes
credential_required
supported_platforms
hardware_requirements
input_formats
output_formats
privacy_class
marginal_cost_model
measured_quality
measured_latency
measured_failure_rate
known_limitations
approved_scope
last_benchmarked_at
status
```

Statuses:

- candidate;
- approved;
- preferred;
- fallback;
- suspended;
- rejected.

A tool can be preferred for one capability and rejected for another.

## 4. Initial candidate set

These are starting candidates, not permanent winners.

### Transcription

Preferred free/local candidates:

- faster-whisper;
- whisper.cpp.

Requirements:

- word or segment timestamps where available;
- deterministic artifact output;
- no source-media upload for local mode;
- confidence or alignment metadata where available.

Do not accept a paid transcription dependency merely because an editing tool's default setup uses one.

### Voice / TTS

Preferred free/local workbench:

- Voicebox.

Candidate engines may include:

- Qwen3-TTS;
- Chatterbox Turbo;
- Chatterbox Multilingual;
- TADA;
- Kokoro;
- other approved engines discovered later.

Voicebox is a candidate workbench/router, not a permanent architectural dependency.

For each channel/voice profile, run blind A/B evaluation on representative passages before choosing the default engine.

A paid TTS provider is a fallback only if local/free candidates fail the realism gate.

### Deterministic editing and rendering

Preferred candidates:

- ffmpeg-skill;
- direct FFmpeg where a narrower deterministic operation is safer.

Use deterministic tools for operations such as:

- cut/join;
- silence handling;
- aspect conversion;
- captions;
- overlays;
- loudness;
- audio cleanup;
- fades;
- delivery checks;
- final render.

An LLM decides *what* should change. A deterministic tool should perform the change where possible.

### Editorial assembly

Candidate:

- browser-use/video-use.

Use for transcript-oriented editorial reasoning, cut planning, assembly, and self-evaluation experiments.

Do not inherit its default paid transcription dependency when a qualified local transcription adapter is available.

### Programmatic motion graphics

Candidates:

- Remotion;
- json-render Remotion renderer;
- Manim for appropriate diagram/math use cases.

Prefer a curated catalog of reusable video primitives over arbitrary generated React for routine graphics.

### Broad production orchestration

Candidate/reference:

- OpenMontage.

Use as:

- an architecture reference;
- a benchmark competitor;
- a production adapter when it wins the required benchmark.

Do not make Designwright's video subsystem dependent on OpenMontage.

Review AGPL implications before embedding, modifying, or redistributing its code.

### Generated imagery/video

Treat generated media as a lower-priority visual source.

Candidate adapters may include:

- approved local workflows such as ComfyUI-compatible pipelines;
- approved remote image/video models;
- future providers.

Selection depends on:

- visual realism;
- temporal consistency;
- text/UI fidelity;
- rights and policy;
- price;
- latency;
- available hardware.

Do not force local generated video when local hardware produces visibly inferior results. Prefer real footage, screen capture, graphics, or stock before escalating to a paid generated shot.

### Audiovisual QA

Preferred architecture:

- deterministic media checks;
- local multimodal reviewer when hardware permits;
- optional remote multimodal challenger for borderline/high-value cases.

Candidate local/open models include:

- Qwen3-Omni for native text/audio/image/video understanding where suitable hardware is available;
- Qwen2.5-Omni 7B or quantized variants as a lighter audiovisual candidate;
- future models that beat them in Designwright's benchmark.

Do not make one model the sole realism judge.

### Upload

Use the official YouTube upload API or another explicitly approved platform API.

Automated upload defaults to private.

Publishing visibility changes require a human authorization boundary.

## 5. Quality-before-cost gate

For each capability:

1. identify qualified local/free candidates;
2. run the relevant benchmark;
3. choose the least expensive candidate that clears quality;
4. if none clear quality, evaluate free-tier remote candidates;
5. if still inadequate, propose paid escalation;
6. record the reason and estimated cost;
7. after the run, record actual cost and result quality.

Paid escalation without a recorded failed/unsupported lower-cost path is a policy failure.

## 6. Tool benchmarks

Every important adapter should have a benchmark suite using stable fixtures.

### TTS benchmark

Use at least:

- conversational paragraph;
- technical paragraph with acronyms/names;
- emotionally mild hook;
- numbers/currency/versions;
- long sentence;
- short punchy lines.

Evaluate blindly for:

- naturalness;
- pronunciation;
- cadence;
- emotion;
- stability;
- chunk boundaries;
- synthesis artifacts;
- generation speed;
- hardware cost.

### Transcription benchmark

Measure:

- word error on known transcript;
- timestamp usefulness;
- punctuation;
- names/acronyms;
- runtime;
- memory use.

### Editor benchmark

Use the same source package and requested edit.

Measure:

- correct cuts;
- audio continuity;
- subtitle timing;
- visual continuity;
- instruction adherence;
- render success;
- number of repair cycles;
- total time.

### Audiovisual reviewer benchmark

Create known-good and deliberately defective clips:

- unrelated B-roll;
- repeated shots;
- bad AI hands/faces;
- warped text;
- fake UI;
- subtitle overflow;
- audio pop;
- clipped narration;
- robotic cadence;
- mispronunciation;
- music masking speech;
- abrupt voice-character change;
- visual/narration mismatch.

A reviewer is qualified only if it reliably identifies defects without excessive false positives.

## 7. Champion / challenger policy

Each capability may have:

- one preferred champion;
- one or more challengers.

Periodically rerun challengers against the benchmark.

Promote a challenger only when evidence supports improvement in the required dimensions.

Do not switch tools because of GitHub popularity alone.

## 8. Privacy and rights

A candidate must be rejected or restricted when:

- license/commercial-use terms are unclear for the intended use;
- required media upload violates project privacy;
- provider retention is unknown where sensitive content is involved;
- generated-media rights are incompatible with intended publication;
- source asset provenance is missing.

## 9. Cost reporting

Every production report should include:

```text
local compute: informational
paid provider calls: count
paid provider cost: actual or best available estimate
stock/media purchases: cost
total external marginal cost
paid escalation reasons
```

Target external marginal cost for ordinary videos: $0 whenever the quality contract can be met.

## 10. Re-evaluation

Re-evaluate a preferred tool when:

- a repeated critic finding points to the tool;
- a provider changes price or license;
- a new tool clears the same benchmark materially better;
- hardware changes;
- reliability drops;
- privacy requirements change;
- a user explicitly rejects the tool's output style.
