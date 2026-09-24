# Designwright Video Studio — Evidence and Learning Loop

Status: proposed  
Date: 2026-09-24

## 1. Principle

Designwright should improve from evidence, not from vague self-reflection.

The system must not autonomously rewrite its own canonical skills or quality rules after every video.

Learning produces **proposals** backed by:

- human feedback;
- critic findings;
- tool benchmark results;
- production reliability;
- post-publication performance;
- repeated evidence across multiple runs.

Human-approved project/channel memory remains authoritative.

## 2. Three memory layers

### Global Designwright knowledge

Contains portable principles supported across projects.

Examples:

- deterministic edits are preferable to generative edits when both satisfy the contract;
- rendered artifacts require independent review;
- paid escalation requires evidence.

Global knowledge should change slowly.

### Channel profile

A channel-specific `VIDEO.md` or equivalent.

Possible sections:

- audience;
- positioning;
- voice character;
- hook behavior;
- pacing;
- visual-source priority;
- shot-duration tendencies;
- caption treatment;
- motion-graphics rules;
- music rules;
- thumbnail rules;
- Short/Reel rules;
- anti-patterns;
- approved tools;
- known pronunciation dictionary;
- evidence behind rules.

### Production history

Immutable or append-oriented run records.

Stores what happened, not what the system wishes happened.

## 3. Production record

Each run should preserve:

```text
run_id
topic
research_revision
script_revision
channel_profile_revision
direction_revision
production_tool_versions
provider_versions
voice_profile
format
duration
render_time
local_compute_notes
external_cost
qa_findings
repair_cycles
human_feedback
publish_state
published_video_id
```

## 4. Shot/segment record

Each accepted and rejected shot should preserve enough evidence for analysis:

```text
shot_id
purpose
transcript_span
planned_duration
actual_duration
visual_type
source_type
source_id
generated
generation_provider
edit_tool
critic_findings
repair_count
human_feedback
accepted
```

Voice segments similarly record:

- provider;
- model;
- reference/profile;
- instructions;
- pronunciation overrides;
- duration;
- critic findings;
- replacement history.

## 5. Tool performance memory

For every tool/provider:

Track:

- attempted runs;
- successful runs;
- failure modes;
- average repair cycles;
- benchmark quality;
- human acceptance;
- cost;
- latency;
- hardware/resource use;
- privacy limitations;
- license changes.

Do not promote a tool because it was new or popular.

## 6. Human feedback hierarchy

Evidence priority:

1. explicit human decision/preference;
2. hard deterministic defect;
3. repeated independent critic findings;
4. repeated production outcome evidence;
5. post-publication performance signals;
6. one-off model aesthetic opinion.

Model taste cannot override an explicit human preference.

## 7. Performance feedback

When a video is published and platform data is available, ingest metrics such as:

### Long-form

- impressions;
- click-through rate;
- average view duration;
- average percentage viewed;
- retention at meaningful timestamps;
- retention curve events;
- likes;
- comments;
- shares;
- subscribers attributed when available.

### Shorts/Reels

- views;
- viewed vs swiped where available;
- average percentage viewed;
- completion;
- loops/replays;
- likes;
- comments;
- shares.

Treat platform analytics as noisy observational evidence, not proof of causality.

## 8. Decision-to-outcome linkage

Whenever practical, relate performance to production decisions.

Examples:

- hook length;
- first evidence/demo timestamp;
- intro animation presence;
- voice provider;
- average shot duration;
- generated-media percentage;
- screen-recording percentage;
- caption density;
- thumbnail structure.

Do not claim "X caused retention" from a single correlation.

## 9. Rule promotion

A new channel rule may be proposed when:

- the user explicitly requests it; or
- the same issue appears repeatedly; or
- repeated performance evidence supports it.

Example proposal:

```text
Proposal:
Move first demonstration before 0:08 for technical explainers.

Evidence:
- Run A: demo 0:21, 30s retention 54%
- Run B: demo 0:09, 30s retention 67%
- Run C: demo 0:06, 30s retention 72%
- Human feedback on A: "intro feels slow"

Confidence:
moderate

Scope:
this channel, technical-explainer format

Action:
update VIDEO.md after human approval
```

Never silently edit canonical guidance.

## 10. Anti-overfitting policy

Do not create a canonical style rule from:

- one video's performance;
- one critic's aesthetic preference;
- one viral anomaly;
- one provider failure;
- one platform metric change.

Require either repeated evidence or explicit human direction.

## 11. Continuous tool improvement

On a schedule or after a meaningful new candidate appears:

1. identify capability challengers;
2. run stable benchmark fixtures;
3. compare against current champion;
4. review quality/cost/privacy/license;
5. propose promotion/demotion;
6. require approval for material production-routing changes.

This lets Designwright improve as external tools improve without importing every tool into the plugin.

## 12. Pronunciation memory

Maintain channel/project pronunciation records for:

- product names;
- people;
- acronyms;
- technical terms;
- unusual brand names.

When a reviewer or human corrects a pronunciation:

- preserve the failed rendering;
- preserve corrected phonetic/provider instruction;
- add a scoped pronunciation entry after approval.

## 13. Rejected-output memory

Rejected media is useful evidence.

Record why a shot or voice segment was rejected using normalized categories.

Examples:

- generic_broll;
- fake_ui;
- temporal_artifact;
- warped_text;
- robotic_voice;
- pronunciation;
- pacing;
- irrelevant_visual;
- excessive_motion;
- caption_readability;
- factual_mismatch.

Future tool routing can use rejection history.

## 14. Learning review

Periodically produce a review packet:

- what improved;
- repeated failures;
- tools that are becoming unreliable;
- expensive capabilities;
- rules proposed;
- rules that appear unsupported;
- new challengers worth testing.

This packet is advisory.

A human or project governance process approves canonical changes.
