# Test vectors

- Valid specification and invariant-preserving candidate produce `APPLY`.
- A candidate violating an explicit invariant produces `REJECT`.
- Hash mismatch, unavailable evidence or ambiguous AI output produces `INCONCLUSIVE`.
- Stale versions, duplicate mutation IDs and missing graph references are rejected before nondeterministic execution.
