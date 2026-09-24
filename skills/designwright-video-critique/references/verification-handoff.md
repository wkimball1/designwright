# Video Verification Handoff

The verifier receives:

- production contract revision;
- repaired render hash/path;
- original and accepted findings;
- exact timestamps/shot IDs;
- deterministic checks to rerun;
- audiovisual checks to rerun;
- unchanged invariants;
- known limitations.

The verifier must confirm:

- each accepted finding is actually closed;
- no repair introduced a new hard failure;
- factual/source alignment remains intact;
- rendered audio/video, not just metadata, was reviewed;
- long-form/Short format gates still pass;
- publishing remains private/unpublished unless separately authorized.

The verifier returns pass/fail plus evidence. It does not infer approval from the critic's recommendation.
