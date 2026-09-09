---
name: designwright-component-intelligence
description: Select components with ordered provenance and hard gates.
license: MIT
---

# Designwright Component Intelligence

Use this skill whenever a design need could be met by an existing primitive, shared component, catalog entry, or new implementation. It turns component selection into an inspectable decision instead of a convenience install. Search is read-only until a separately approved implementation action exists.

## Source precedence

Always search and qualify sources in this order:

`project-local -> approved private -> approved curated external -> new`

The order is a boundary, not a soft preference. A qualified earlier-tier candidate blocks a later-tier choice. An earlier candidate may be rejected, but only with recorded evidence against a hard gate or the stated need.

## Procedure

1. Normalize the need before searching. Describe behavior, states, semantic role, keyboard and accessibility requirements, responsive behavior, framework constraints, token slots, dependency limits, and visual constraints. Do not begin with a catalog component name.
2. Search project-local sources. Inspect component directories, imports, usage sites, stories or previews, styles, tokens, tests, and known states. Record every plausible candidate and why it qualifies or fails.
3. Search approved private sources only if no qualified local candidate remains. Use read-only list, search, view, dependency, license, and pin information. A private source is not approved merely because it is reachable.
4. Search approved curated external sources only if earlier tiers have no qualified candidate. Inspect source, provenance, license and permitted use, dependency graph, update policy, behavior, tests, and exact version or commit before proposing use. Never treat catalog size or novelty as evidence of fit.
5. Propose a new implementation only when the record contains `no-qualified-candidate` evidence for every earlier tier. Name the owner, intended scope, semantic API, token slots, states, tests, and human approver. Rerun duplicate detection before merge.
6. Apply hard gates. Reject a candidate with an incompatible or unclear license, unreviewed install or generation script, mutable or missing pin, unresolved dependency, missing required state, broken keyboard semantics, failed responsive behavior, incompatible tokens, unsafe provenance, or duplicate local primitive. Hard gates override any score.
7. Score surviving candidates visibly from 0 to 2 for behavioral fit, token fit, accessibility and states, responsive evidence, dependency fit, maintenance and provenance, adaptation cost, and duplication risk. Use the score to compare candidates within the highest qualifying tier, not to bypass precedence.
8. Record the decision. Include need ID, candidates, source tier, exact path or pin, scores, hard-gate results, rejection reasons, files and dependencies affected, reviewer, approval scope, and a recheck trigger. Keep rejected candidates so a later reviewer can audit the choice.

## Decision record

A complete record answers:

- What user capability and states were needed?
- Which local, private, curated, and new tiers were searched?
- Why did each earlier candidate pass or fail?
- What exact source, version, commit, or project path was selected?
- Which dependencies, tokens, states, keyboard paths, responsive rules, and tests are affected?
- Who independently reviewed provenance and behavior?
- What must change before the decision expires or is reconsidered?

A component decision does not authorize a package install, registry write, production mutation, or baseline change. Those actions remain under the project governance boundary.

## Verification

Before implementation, confirm that the selected source is the highest-precedence tier with a qualifying candidate, all hard gates pass, the exact pin is reproducible, and the decision record is complete. After implementation, verify the selected component's actual imports, states, accessibility behavior, responsive behavior, and dependency diff against the record. Any mismatch reopens the decision.
