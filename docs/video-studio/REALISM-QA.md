# Designwright Video Studio — Realism and Audiovisual QA

Status: proposed  
Date: 2026-09-24

## 1. Goal

The QA system must evaluate the **rendered media itself**, not merely the script, storyboard, prompts, or producer's explanation.

"AI-generated slop" is treated as an operational quality failure, not as a vague aesthetic complaint.

The system should catch:

- robotic or obviously synthetic narration;
- unrelated generic B-roll;
- repeated stock/generative motifs;
- warped text or fake interfaces;
- temporal inconsistencies in generated footage;
- uncanny faces/hands/objects when present;
- visual claims that do not match source evidence;
- excessive motion, zooms, transitions, or caption animation;
- dead/static sections without narrative reason;
- narration-to-visual mismatch;
- caption overflow or unreadability;
- abrupt audio edits;
- clipping;
- music masking narration;
- inconsistent voice identity;
- unnatural pauses and sentence cadence;
- obviously regenerated segments with mismatched tone/room/noise;
- incorrect pronunciations;
- filler visuals used only because the system had nothing relevant to show.

## 2. Independence

The producer must not be the only reviewer.

Material productions require at least:

1. producer/self-check;
2. independent audiovisual critic;
3. verifier after accepted fixes.

For high-value or borderline artifacts, use a second model/tool as a challenger rather than relying on one model's taste.

## 3. Multi-pass QA

Do not ask one model one broad question such as "Does this look good?"

Run separate passes.

### Pass A — deterministic media integrity

Use FFmpeg/ffprobe or equivalent to check:

- duration;
- resolution;
- framerate;
- codec/container;
- black/frozen frames;
- corrupted frames;
- audio presence;
- clipping/true peak;
- integrated loudness;
- long unintended silences;
- channel configuration;
- abrupt cut-boundary audio discontinuities;
- subtitle/caption stream presence;
- output safe dimensions.

Failures here are objective and should not be delegated to aesthetic AI judgment.

### Pass B — transcript fidelity

Transcribe the final rendered narration/audio.

Compare final transcript to the approved script.

Flag:

- missing words/segments;
- duplicated text;
- material substitutions;
- unexpected hallucinated speech;
- timing discontinuities;
- suspicious pronunciation failures inferred from ASR divergence.

Do not assume ASR disagreement proves a pronunciation error; it is a trigger for listening review.

### Pass C — audio-only listener

Provide the final audio or segmented audio to an audio-capable model without showing the production rationale.

Evaluate:

- human-likeness;
- cadence diversity;
- breath/pause placement;
- sentence endings;
- emphasis;
- pronunciation;
- chunk boundary consistency;
- voice identity stability;
- emotional appropriateness;
- audible synthesis artifacts;
- audio edits/pops;
- music/narration balance.

Return timestamped findings.

The reviewer must distinguish:

- objective defect;
- likely defect;
- style preference;
- uncertainty.

### Pass D — visual-only reviewer

Review the rendered frames/clips without producer rationale.

Use:

- shot-boundary frames;
- regular interval samples;
- high-motion clips;
- generated-media clips;
- text-heavy shots;
- UI/screen-recording shots;
- thumbnail candidates.

Evaluate:

- relevance to narration;
- visual authenticity;
- generated-media artifacts;
- warped text;
- fake or misleading UI;
- hands/faces/object consistency;
- repeated visual motifs;
- overuse of generic B-roll;
- excessive stock feel;
- style consistency;
- caption readability;
- safe zones;
- hierarchy;
- pacing based on shot duration;
- jarring transitions.

### Pass E — synchronized audiovisual reviewer

This pass must actually consume the video with audio when the selected model/tool supports synchronized audiovisual input.

Candidate local/open reviewers may include Qwen3-Omni or another approved audiovisual model.

Evaluate:

- whether the visual supports what is being said at that moment;
- whether a cut lands naturally with the narration;
- whether sound/visual transitions feel coherent;
- whether the voice emotion matches the visual moment;
- whether generated visuals create an uncanny or misleading impression;
- whether the piece feels intentionally edited rather than automatically filled.

This pass is especially important because audio-only and visual-only checks cannot detect all cross-modal mismatches.

### Pass F — factual/source alignment

For every material factual claim:

- map claim to source/evidence;
- map visuals that imply factual proof to the source artifact;
- reject fabricated screenshots, fabricated UI, fabricated charts, or generated imagery presented as documentary evidence.

Generated illustrative media must not silently masquerade as source evidence.

### Pass G — format-specific review

#### Long-form

Check:

- hook clarity;
- unnecessary intro;
- section pacing;
- evidence density;
- repetitive visuals;
- long static intervals;
- CTA placement;
- narrative payoff.

#### Short/Reel

Check:

- first-frame comprehension;
- first-second visual interest;
- vertical composition;
- caption scale;
- safe zones;
- crop correctness;
- rapid but comprehensible pacing;
- self-contained context;
- payoff before the ending.

## 4. Realism rubric

Use an evidence-backed rubric rather than one aggregate "quality score."

Suggested dimensions:

- voice naturalness;
- pronunciation;
- audio continuity;
- visual authenticity;
- visual relevance;
- temporal consistency;
- edit intentionality;
- pacing;
- caption quality;
- graphics quality;
- factual integrity;
- channel/style consistency.

Each dimension receives:

- pass;
- conditional;
- fail;
- insufficient evidence.

Optional numeric scores may be recorded for comparison, but hard failures override averages.

## 5. Hard failures

A production cannot be marked review-ready when any of the following remain:

- obviously synthetic/robotic narration in a material segment;
- material visual/narration mismatch;
- misleading generated media presented as evidence;
- unreadable captions in a required format;
- clipping or audio defect that materially distracts;
- generated text/UI visibly broken;
- severe temporal artifact in a prominent generated shot;
- unsupported factual claim;
- required source/provenance missing;
- key mobile safe-zone failure;
- critic evidence missing;
- producer self-approved without independent verification.

## 6. Slop-pattern detectors

Maintain a versioned checklist of recurring low-quality patterns.

Initial candidates:

### Narration slop

- every sentence has the same cadence;
- repeated dramatic pauses;
- exaggerated enthusiasm;
- unnatural stress on product names;
- pronunciation inconsistent across segments;
- no variation in sentence rhythm;
- audible seam between TTS chunks;
- generic "In today's..." / "But here's the thing..." delivery when not justified by approved script.

### Visual slop

- abstract server-room/robot/neon footage for every AI concept;
- unrelated people typing on laptops;
- excessive generated camera motion;
- repeated zoom-in/zoom-out templates;
- every sentence triggering a new transition;
- visuals that merely decorate rather than explain;
- generated screenshots;
- fake browser/product UI;
- text morphing between frames;
- overly glossy synthetic humans;
- inconsistent object identity across adjacent frames.

### Editing slop

- cuts every fixed number of seconds regardless of narrative;
- random B-roll with no evidence tie;
- subtitles covering UI;
- huge captions with no hierarchy;
- excessive sound effects;
- music too loud;
- jump cuts that damage speech;
- every section using the same animation template.

A slop-pattern match is a finding, not an automatic rejection, unless the contract marks it as prohibited.

## 7. Targeted repair contract

Every finding should identify the smallest repairable unit:

```text
finding_id
severity
timestamp_start
timestamp_end
shot_id
audio_segment_id
problem
why_it_matters
evidence
recommended_change
unchanged_invariants
preferred_capability
```

Examples:

- regenerate one sentence, not the entire narration;
- replace one generated shot with a real screenshot;
- shorten a single static shot;
- move/reflow one caption;
- lower music under one segment;
- recreate one chart;
- replace one incorrect source image.

## 8. Blind A/B review

Use blind comparisons when evaluating:

- TTS providers;
- voice models;
- regenerated shots;
- thumbnail variants;
- caption treatments;
- motion-graphic alternatives.

The reviewer should not know which provider is expected to win.

## 9. Human calibration

User feedback has higher authority than model taste.

If the user says:

> this sounds fake

preserve:

- timestamp;
- rejected segment;
- provider/model;
- voice settings;
- reviewer results;
- replacement result.

Use the event to improve future routing and channel guidance.

Do not rewrite a global rule from one isolated preference unless the user explicitly asks.

## 10. Local-first reviewer policy

Prefer local/open reviewers when they clear the benchmark.

An audiovisual model should be evaluated on known-good/known-bad fixtures before being trusted.

Candidate models are replaceable.

Qwen3-Omni is an initial candidate because it accepts text, audio, images, and video. Qwen2.5-Omni-class models can be evaluated as lighter alternatives where hardware is constrained.

If local review is too slow or unreliable, a remote challenger may be used within approved privacy/cost policy.

## 11. Review-ready gate

A run is review-ready only when:

- deterministic checks pass;
- final transcript is reconciled;
- audio critic has no unresolved hard failure;
- visual critic has no unresolved hard failure;
- synchronized audiovisual review has no unresolved hard failure;
- factual/source audit passes;
- accepted findings have been rerun;
- verifier independently reproduces the evidence;
- remaining limitations are explicit.
