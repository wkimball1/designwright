# Designwright Video Studio

Status: proposed subsystem specification  
Date: 2026-09-24

Designwright Video Studio extends Designwright's existing evidence-first design-intelligence model into video direction, production QA, tool selection, and continuous improvement.

It does **not** turn Designwright into a monolithic video editor or hard-wire it to one provider. Designwright owns creative direction, acceptance contracts, evidence, critique, verification, tool selection policy, and learning. Specialized external tools remain replaceable adapters.

## Core decision

Designwright should become the:

- creative director;
- production-contract author;
- tool-selection policy;
- independent critic;
- verifier;
- evidence and learning system.

Designwright should initially **not** become the:

- TTS engine;
- video renderer;
- FFmpeg implementation;
- Remotion runtime;
- generative-video model;
- transcription engine;
- YouTube uploader implementation.

Those capabilities are selected from approved tools and providers.

## Human workflow

The target user experience is:

1. User asks ChatGPT/Claude to research a video idea.
2. Research agent returns angle, claims, sources, hook, and proposed formats.
3. User explicitly approves production.
4. Video Studio creates the production contract and storyboard.
5. Tool routing selects the best approved tools, preferring free/local options.
6. Voice, assets, graphics, screen captures, and selective generative media are produced.
7. An editorial system assembles the cut.
8. The video is rendered.
9. Independent AI systems watch **and** listen to the rendered artifact.
10. Findings trigger targeted revisions rather than full regeneration.
11. A distinct verifier checks the final artifact.
12. Long-form, Short/Reel, thumbnail, captions, metadata, and sources are packaged.
13. Upload automation may upload **private drafts only**.
14. The user reviews and explicitly decides whether to publish.
15. Post-publication performance and user feedback feed the learning loop.

## Free/local-first principle

The default marginal provider cost should be $0 where quality permits.

Tool routing follows:

`approved local/free -> approved free-tier external -> approved paid specialist`

Paid escalation must record why the free/local path failed a measurable acceptance gate.

## Documents

- [PRD](./PRD.md) — product goals, user flow, scope, and acceptance criteria.
- [Architecture](./ARCHITECTURE.md) — subsystem boundaries, data flow, adapters, artifacts, and safety.
- [Tool Policy](./TOOL-POLICY.md) — free-first routing, capability registry, provider evaluation, and fallback rules.
- [Realism QA](./REALISM-QA.md) — how AI watches/listens to completed media and rejects synthetic-looking or synthetic-sounding slop.
- [Learning Loop](./LEARNING-LOOP.md) — evidence memory, human feedback, performance feedback, and how Designwright improves without blindly self-modifying.

## Existing Designwright compatibility

This subsystem should preserve the existing Designwright model:

- project-specific evidence outranks generic guidance;
- direction precedes implementation;
- tool/component choice is inspectable and provenance-aware;
- implementer, critic, and verifier remain separate for material work;
- screenshots/renders alone are not proof;
- hard failures override aggregate aesthetic scores;
- external tools do not become trusted merely because they are reachable;
- human approval remains required at consequential boundaries.

Video Studio should extend these principles, not bypass them.
