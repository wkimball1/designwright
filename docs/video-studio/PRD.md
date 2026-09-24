# Designwright Video Studio — Product Requirements

Status: proposed  
Date: 2026-09-24

## 1. Product definition

Designwright Video Studio is an evidence-first system for turning approved research into polished faceless long-form and short-form video drafts.

The system should make the high-level interaction feel like:

> Research this idea.

Then, after the user reviews the research:

> Yes, make the video and the Short.

From that approval, the system should autonomously produce a review-ready package while maintaining explicit provenance, cost controls, realism checks, and human publishing authority.

## 2. Primary outcome

Produce a draft that:

- sounds like a real person rather than generic TTS;
- looks intentionally edited rather than generated from unrelated AI B-roll;
- uses real evidence and real product/source visuals whenever possible;
- uses programmatic graphics where they communicate better than generated footage;
- uses generative imagery/video selectively, not by default;
- has coherent pacing, audio, captions, and visual hierarchy;
- is independently watched and listened to before being marked review-ready;
- can be revised at the shot/segment level;
- can be uploaded privately for final human review;
- gets measurably better across future productions.

## 3. Non-goals

V1 is not:

- a replacement for FFmpeg;
- a new TTS model;
- a new video-generation model;
- an all-in-one editor;
- a public autonomous publishing bot;
- a system that optimizes solely for engagement at the expense of factuality;
- a system that silently learns style rules from one weak datapoint;
- a system that copies a reference creator's protected identity, exact composition, assets, or script.

## 4. Production approval boundary

Research and production are separate decisions.

Before production begins, preserve:

- topic;
- target viewer;
- thesis;
- claims and sources;
- angle;
- hook;
- long-form target;
- Short/Reel target;
- known risks;
- estimated provider cost if non-zero.

The user must explicitly approve production.

Production approval does not authorize public publishing.

## 5. Required deliverables

For an approved long-form request, produce where applicable:

- final long-form video draft;
- dedicated 9:16 Short/Reel composition, not merely an automatic crop;
- thumbnail candidates and selected draft;
- title candidates and selected draft;
- description;
- chapters;
- captions/subtitles;
- source/evidence package;
- production report;
- quality/realism report;
- provider/tool cost report;
- private upload result when upload credentials and permission are available.

## 6. Production hierarchy for visuals

For every scene, prefer:

1. real evidence/source media;
2. real screen recording or product capture;
3. deterministic/programmatic graphics;
4. properly licensed stock/archive media;
5. generated still imagery;
6. generated video.

A lower tier must not replace an available higher-quality/higher-trust tier merely because it is easier to generate.

Generated media must be labeled in production metadata.

## 7. Voice requirements

Voice must be evaluated for:

- conversational prosody;
- pacing;
- sentence-final cadence;
- breath/pause realism;
- pronunciation;
- emphasis;
- emotional appropriateness;
- consistency across generated chunks;
- absence of obvious synthesis artifacts;
- absence of exaggerated "YouTube announcer" delivery.

Long narration should be generated in controlled segments where that improves naturalness and editability.

The system must support provider A/B tests.

## 8. Long-form requirements

The production contract should define:

- hook;
- sections;
- evidence required per section;
- narration;
- planned visual for each segment;
- shot-duration targets;
- motion level;
- caption policy;
- music policy;
- generated-media allowance;
- CTA policy;
- acceptance evidence.

No segment should use unrelated filler footage merely to avoid visual silence.

## 9. Short/Reel requirements

Short-form is a separate edit.

It should have:

- its own hook;
- a self-contained payoff;
- 9:16-specific composition;
- mobile-readable text;
- tighter pacing;
- source-appropriate visuals;
- safe-zone-aware captions;
- no dependency on context that existed only in the long video.

## 10. Realism and quality gate

A rendered artifact is not review-ready until independent QA has:

- watched sampled and high-risk visual segments;
- listened to narration and audio transitions;
- compared transcript timing to visuals;
- inspected captions;
- checked factual/source alignment;
- checked synthetic-media authenticity concerns;
- identified repetitive or generic AI visual patterns;
- inspected audio for clipping, discontinuity, unnatural speech, or music masking;
- checked mobile readability for Shorts;
- rerun accepted fixes;
- issued a pass or named limitations.

The producer cannot approve its own final output.

## 11. Human review

The user should be able to say things such as:

- intro feels too slow;
- voice sounds fake at 1:42;
- this B-roll feels generic;
- the chart is confusing;
- I do not like this thumbnail;
- cut this entire section.

Feedback must be bound to timestamp, shot, transcript segment, or artifact where possible so future revisions are targeted.

## 12. Publishing safety

Automated publishing may upload only as **private** by default.

Public or unlisted publication requires explicit human authorization at the publishing boundary.

The system must never infer public-publishing permission from production approval.

## 13. Cost requirement

Preferred marginal provider cost: $0.

Every paid operation must record:

- provider;
- capability;
- estimated/actual cost;
- reason local/free options did not satisfy the gate.

The final production report must show total external provider cost.

## 14. Success criteria

V1 succeeds when a user can approve a researched topic and receive a coherent review-ready video package without manually assembling the timeline, while:

- using local/free tools for most operations;
- retaining source provenance;
- passing independent audiovisual QA;
- allowing targeted correction;
- keeping public publishing human-controlled.

Longer-term success means measurable reductions in:

- manual edit time;
- paid-provider spend;
- realism defects;
- repeated critic findings;
- unnecessary full rerenders;

while improving:

- human acceptance rate;
- retention/engagement where available;
- provider/tool reliability;
- consistency with channel identity.
