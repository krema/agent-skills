# RAG and deferred tool discovery

Use for a retrieval pipeline or tool catalog. The patterns below are engineering inferences from E03 and E06–E20, with the host-specific interface distinction in E17. Parameters must be measured on the target workload.

## Separate three decisions

1. **Where to look:** discover domains, document families, or capabilities using metadata and the request.
2. **What to load:** retrieve passages or full procedures/schemas, retaining source identifiers, scope, and version.
3. **Whether it is enough:** assess the evidence against the subquestions and dependencies before answering or acting.

A domain router adds another place to lose recall. Support multiple domains, an unknown route, and a broader search path. For exhaustive inventories or global comparisons, use a coverage plan or full-source processing instead of treating top-k similarity as completeness.

## RAG design

Keep procedures and facts distinguishable even when both are searchable. Enforce tenant and document permissions before exposing content or sensitive metadata. Retrieval relevance is not authority: retain effective dates, document status, and the applicable source hierarchy. Resolve conflicting versions using that hierarchy and the task's date; do not blindly choose the newest timestamp.

When a chunk relies on a parent definition, table header, exception, or previous step, fetch the surrounding unit. Contextualized chunks, keyword-plus-semantic retrieval, and reranking are candidates when inspection shows lost context or exact-identifier misses. Validate generated chunk summaries against their originals. They should aid retrieval, not become an unverified replacement for the evidence.

Use iterative retrieval for dependencies learned only during answering: identify an entity, then query its relationship or governing rule. Stop when required claims are supported or a concrete missing source blocks them. A model's confidence alone does not establish completeness. If a search returns nothing, distinguish no hit from access denied, timeout, stale index, or unavailable source before drawing conclusions.

For multilingual free-text search, inspect generated arguments and backend matching when spelling or script variants produce empty results. Test representative user forms and supported normalization or semantic fallback. Preserve exact identifiers and verify candidate matches; do not apply lossy normalization indiscriminately. This conditional engineering recommendation follows E15, not a requirement to replace every search backend.

Avoid a universal chunk size, top-k, confidence cutoff, or number of retries. Set practical limits from context capacity, latency requirements, failure cost, and observed recall. At an exhausted limit, return the supported portion and name the unresolved dependency.

## Tools

Expose the discovery mechanism and any essential always-needed capabilities. Make deferred entries describe operation, resource, and differentiating constraints. Before invocation, load the actual schema and applicable usage requirements; do not guess arguments from a tool name. If tool search fails, broaden synonyms or inspect a bounded catalog segment. Discovery does not authorize invocation.

Use the host's deferred-tool mechanism where available. Dynamically rewriting the initial tool list may invalidate prompt caches; appending references through the supported protocol can behave differently. Verify current host/API semantics before implementation. Discovery can lower schema overhead, while enormous search results or tool outputs can still dominate context.

Separate API registration from model-visible context. Claude's documented deferred-tool interface still requires complete tool definitions in each request; defer_loading controls exposure to the model, not whether the server receives schemas. Do not replace those definitions with name-only stubs based on an architectural analogy (E17). Recheck the target API before implementing this host-specific behavior.

## Runtime and measurement

Keep a stable shared prefix where the API supports caching and append task-specific evidence through the supported mechanism. Cached text still occupies logical context. Distinguish context occupancy, billed input, cache reads/writes, output tokens, retrieval cost, and total wall time. For layered memory, also include preprocessing, on-demand view generation, and final answer generation; a fraction of sessions opened is not a token-cost reduction (E16). A shorter request can cost more if it causes extra searches, repeated reasoning, or cache misses.

For long tasks, persist decisions, source locators, source versions, unresolved questions, and completed actions before supported compaction. Do not reexecute a side effect just because its detailed tool result was removed. Refresh a fact when currency affects the result.

Compare selective loading with direct context and a simple hybrid baseline. Measure final correctness, prerequisite coverage, retrieval recall on labeled cases, false exclusions, unsupported assertions, tool errors, and recovery behavior alongside cost and latency. When comparing eligibility filters, count lost permitted evidence alongside improper prompt exposure; preserve unresolved metadata as unknown and test recovery without widening permissions (E18). Production suitability depends on these results, not on the existence of a router.
