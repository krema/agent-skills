# A — Support orchestration audit

Evaluate a shared conversation loop for orders, returns, and shipping, with direct tools and an occasionally loaded returns procedure. Keep the current implementation recoverable until that candidate passes an outcome comparison.

The boundaries currently cut across the same evolving state: signed-in customer, current order, size 42, and the Friday deadline. The exchange trace repeatedly returns to the returns specialist and loses the size; the arrival trace confuses dispatch with delivery after a handback. These traces support a coupling and information-loss diagnosis. They do not establish traffic prevalence, production latency, or a measured benefit from folding because traffic counts and end-to-end evaluations are absent.

The proposed responsibilities are:

- The main loop owns the conversation and exact customer, order, replacement-size, and deadline state, including any unresolved condition on the exchange.
- `get_order` supplies purchase and dispatch facts. It cannot supply a delivery estimate.
- Every delivery answer uses `get_shipping`, preserving the carrier estimate and its source timestamp. If the lookup is absent, unavailable, or insufficient, report that limitation rather than infer delivery from dispatch or promise arrival by Friday.
- A returns skill holds procedural judgment and required checks. Preserve backend ownership and 30-day eligibility enforcement in `stage_return`; keep its effect limited to a proposal. The response must distinguish a staged proposal from an applied return.

The deterministic lookups and staging operation need no separate model loop. The fixture gives no evidence that a specialist needs an extended user conversation or independent investigation. A router is unnecessary for these tightly coupled reasoning phases; normal tool selection can remain in the conversation loop.

The next concrete step is to prepare an obligation map and one sandbox candidate that folds these specialists, then compare it with the recoverable baseline on the two supplied incidents and adjacent combined cases. Check retained size and deadline, authoritative shipping estimates, ownership and eligibility denials, and accurate proposal status. Include missing shipping data and repeated runs for intermittent failures; measure completed tasks before latency and all-agent cost. Adopt only after the requirements hold. This is an architecture recommendation; no application was edited or run.
