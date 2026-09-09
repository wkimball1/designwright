---
name: designwright-evidence-loop
description: Run a bounded design-to-verification evidence loop.
license: MIT
---

# Designwright Evidence Loop

Use this skill after a direction and component decisions are approved and a bounded slice is ready to implement. A plausible screenshot is not proof. The output is a reproducible evidence bundle tied to the project, source, environment, state, and independent review.

## Required sequence

Run the steps in this order:

`design -> implement -> run -> interact -> screenshot -> inspect -> critique -> fix -> verify`

Do not skip `run`, `interact`, or `inspect`, and do not let the implementer approve the rendered outcome.

## Procedure

1. Freeze the test contract. Record project and adapter versions, source revision, target route or state, fixture and data policy, commands, required viewports, browser and font environment, accessibility target, protected invariants, component decisions, and evidence locations. Keep credentials, production data, and unapproved external inputs out of the slice.
2. Design. Read the approved direction, project memory, component decision records, target requirements, and acceptance gates. List what is allowed to change and what must remain unchanged.
3. Implement. Change only the bounded slice. Record deviations, added or removed dependencies, component imports, token changes, and any unresolved assumption. Do not expand scope to repair unrelated design debt.
4. Run the real local app or isolated fixture. Capture the command, revision, environment, startup result, and route or state reached. A static mock or unexecuted markup cannot stand in for runtime evidence.
5. Interact with the critical path using semantic controls. Exercise default, loading or disabled, validation, error, recovery, success, and other target-required states. Record failures, focus behavior, keyboard path, and same-origin request outcomes.
6. Screenshot required states at 320, 375, 414, 768, and 1280x800, plus project-declared breakpoints when applicable. Bind each image to route, state, viewport, source revision, and environment. Compare to a human-approved baseline only when one exists.
7. Inspect runtime evidence. Collect the DOM or accessibility tree, console errors, failed requests, relevant performance signals, trace or interaction log, layout overflow, focus order, names, contrast, reduced-motion behavior, and evidence-manifest hashes. Automated accessibility output is input to review, not a conformance certificate.
8. Critique independently. Give the rendered evidence and contract to a critic who is not the implementer. Findings must identify problem, why it matters, evidence, proposed change, and what remains unchanged. The critic reports; the critic does not edit.
9. Fix only accepted findings. Apply one bounded fix cycle by default. Permit a second cycle only for unresolved high-severity findings. A third cycle requires a human decision because repeated churn indicates a brief, system, or scope problem.
10. Verify from clean instructions. A verifier distinct from the implementer reruns the critical path, required states, responsive checks, accessibility and diagnostics, confirms the evidence manifest, and decides pass or fail. A failure reopens critique or the direction; it does not get hidden by updating a baseline.

## Evidence bundle

At minimum, preserve the approved direction, change manifest, source revision, environment and commands, route and state matrix, screenshots, interaction trace, DOM or accessibility evidence, console and network results, performance notes, component decision IDs, findings, fixes, verifier result, and hashes or stable paths for each artifact. Record missing evidence as a failure or explicit limitation.

## Hard failures

Stop the loop for a broken critical path, inaccessible primary action, serious or critical accessibility regression, horizontal scroll at a required width, unapproved component source, missing required state or screenshot, failed request without an approved fixture explanation, fabricated or untraceable evidence, or self-approval where independent review is required.

## Verification

The loop passes only when a clean verifier can reproduce the bounded path, every required artifact maps to the frozen contract, accepted findings are closed with evidence, unchanged invariants remain true, and the result is approved through the existing project governance path. No renderer, browser tool, or external service is selected by this skill alone.
