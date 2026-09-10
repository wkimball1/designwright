# Comparative Reference Intake for Initial `DESIGN.md`

Use this guide when a project owner authorizes external design references as **comparative research** for a project-owned initial `DESIGN.md`.

A reference library is not a theme picker, an implementation source, or a substitute for user and product evidence. It can help an agent name tradeoffs; it must never decide a product's identity by itself.

## 1. Eligibility and provenance

Before using an external design-reference collection, record a reference packet outside the target `DESIGN.md`:

- source repository and exact commit or release;
- catalog license and the fact that underlying brands, marks, assets, and brand identities remain third-party property;
- capture date and whether the material is public-site-derived, official, supplied by the project owner, or otherwise;
- permitted-use label: `principle-only`;
- reviewer and approval scope.

`principle-only` is non-negotiable for an initial project `DESIGN.md`. An owner-documented broader right may authorize a separately reviewed source-use decision, but it does **not** authorize copying source-specific tokens, fonts, assets, copy, code, component APIs, signature layouts, or interaction patterns into this workflow.

Attach verification evidence to every record: the source URL, resolved commit/release, direct license text or authoritative permission record, and capture date. If license, permission, authorship, or source revision cannot be verified, mark the item `unverified` and fail closed: it cannot influence the direction or generated `DESIGN.md`.

Do not vendor reference files into a customer repository by default. Keep URLs, commit pins, verification evidence, and compact, original observations in a private/project decision record. A mutable branch such as `main` is discovery evidence only, never a reproducible source pin.

## 2. Curate a small, role-based packet

Choose **three to five** references based on the project and its users—not on a desire to mimic a familiar brand.

Each candidate must earn a distinct role:

- **journey reference** — a comparable emotional or operational job;
- **information reference** — a useful density, navigation, or state-management lesson;
- **interaction reference** — an accessible control, feedback, or mobile-transformation lesson;
- **craft reference** — typography, visual hierarchy, or surface-restraint lesson.

Use fewer sources when they do not add independent evidence, but never fewer than three for a comparative packet. Assign each source exactly one role. A source may contribute at most one adopted principle and may account for no more than one third of all adopted principles in the packet. Never select a reference merely because it is popular, in the same broad software category, or has a large token list.

## 3. Extract only design principles

For **every source-derived observation that influences the draft**, record a short, original observation under these headings:

- user/job fit and context;
- information hierarchy and density;
- semantic color roles—not color values;
- type roles—not fonts, sizes, tracking, or brand styles;
- surface, depth, and geometry intent—not exact tokens or shadows;
- interaction and feedback intent;
- responsive transformation and touch/accessibility implications;
- anti-patterns to avoid for this project.

Do **not** copy or paraphrase a reference's code samples, CSS variables, token values, exact type scale, font names, prompt text, logo/asset descriptions, signature composition, copy, screenshots, or component APIs. Do not ask an agent to “design like [company].” A material source influence that is not enumerated in this record is prohibited; do not relabel it as “inspiration” to bypass the matrix.

## 4. Transform evidence into project identity

Designwright Init remains the first step. It must inspect the actual product, user journey, existing components/tokens, product records, responsive policy, accessibility requirements, and protected behavior before references are considered.

Designwright Direction then writes a **reference matrix**. Every adopted principle must contain:

1. the relevant project fact;
2. the reference principle, stated originally;
3. the project-specific transformation;
4. a distinctly original structural, interaction, or content decision;
5. an acceptance test or evidence gate;
6. a source-influence weight, with the packet total checked against the one-third source cap.

If the project fact is missing, leave the decision unresolved. A reference cannot fill a product-identity gap by guessing.

## 5. Draft the initial `DESIGN.md`

Create a project-owned, **proposed** `DESIGN.md` only after the direction is approved. The file must:

- describe the product's own user, critical journey, tone, hierarchy, content states, responsive rules, accessibility invariants, and anti-patterns;
- define only original semantic tokens and component roles justified by the project;
- keep project decisions and source evidence separate: reference names/URLs belong in the decision record, not in runtime styling instructions;
- use the standard `DESIGN.md` structure and lint it with `designmd lint` before it is treated as an agent input;
- remain explicitly provisional until the project owner accepts the direction and runtime evidence validates it.

The initial file is a useful starting contract, not a permission to overwrite existing project tokens, install components, or change production UI.

## 6. Independent review gate

Before a generated `DESIGN.md` guides implementation, an independent reviewer checks:

- every external reference has a verified provenance record, immutable source pin, and `principle-only` boundary;
- no brand names, marks, source-specific tokens, fonts, copy, assets, or code appear in the generated spec;
- every material source-derived observation is enumerated and each material decision has project evidence, an original transformation, and an influence weight within the one-third source cap;
- accessibility, mobile behavior, states, and evidence gates are explicit;
- the document passes `designmd lint` and does not contradict existing approved project records.

Use a blind origin check for material directions: give the reviewer the proposed `DESIGN.md`, project record, reference matrix, and the project’s intended routes/states—but not the source-brand names. The reviewer must be able to trace every material choice to a project fact and distinct transformation, find no unenumerated influence, and reject a direction that reconstructs a distinctive source hierarchy, composition, or interaction pattern. Reject the packet when this check fails, provenance is unclear, or a generic aesthetic substitutes for the actual user job.
