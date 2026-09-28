# DynamicProcessGenome

DynamicProcessGenome is a single reusable GenLayer primitive for evidence-bound process mutation review.

Owners define a process graph and explicit invariants. A mutation includes a candidate graph plus a public specification URL and exact SHA-256 commitment. During `review_mutation`, the leader and validators independently fetch the specification, recompute the full-response hash, and use GenLayer semantic reasoning to decide whether the candidate preserves every stated invariant and the fetched specification permits the changed behavior. Both the candidate and stored graph have bounded, deterministic structural checks. Consensus compares the full evidence context and a bounded `SAFE` / `UNSAFE` / `UNKNOWN` verdict, not free-form LLM prose.

`APPLY` advances the graph version and immutable mutation root. `REJECT` and `INCONCLUSIVE` are recorded without state advancement. Caller-supplied summaries and scores do not control the result.

Workflow: `create_process_space → add_process_node → connect_process_nodes → review_mutation`. `review_insert_step` is a compact, equivalent entrypoint for replacing one sequence edge with two edges through a new step; it uses the same review and consensus path. The public demo specification is in `examples/process-spec.txt`.
