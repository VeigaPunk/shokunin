# W1 ART dossier — kama

**Lane:** `kama` — local model serving and endpoint health  
**Scope:** documentation-only research on llama.cpp server, vLLM, SGLang, Ollama, OpenAI-compatible model inventory, health/readiness probes, GGUF and quantization, and serving metrics.  
**Evidence date:** sources in the registry were opened on 2026-10-19.

## Scope and evidence limits

This is a source dossier, not a live-service report or an integration result. No local endpoint was contacted, no model request was sent, no service was started, no credentials were read, and no lane files were changed. The lane’s `PROVINCE.md` records a dated 2026-10-15 sample in which registered endpoints were dead and states that llama.cpp is the only runtime with real-runtime reconciliation evidence; vLLM/Ollama fixtures are parser evidence, not integration. That is repo-recorded history, not a fresh host observation. See `PROVINCE.md` §Observed state and §Actual round-5 sample; `corpus/README.md` §Known gaps.

A docs statement below describes what its cited implementation or API documentation says. It does not prove that a runtime is installed here, that its current implementation matches the page, or that a current local endpoint serves the described model. All external registry rows remain `queued` or `watch`: candidate entries have not yet cited them, so none is `mined` under the SOURCES.md contract.

## Uncovered ground in the lane corpus

The inspected corpus index already names `knowledge/endpoint-identity.md` for classification, health/readiness, thresholds and probes, and `knowledge/served-model-identity.md` for `/v1/models` vs `--alias` reconciliation. Other mapped entries cover consumer pins, listener ownership, drift history, aliases, and invocation snapshots. These are good lane anchors; the research should extend rather than replace their local llama.cpp evidence.

The index’s explicit known gap is that real-runtime reconciliation is proven for llama.cpp only; vLLM/Ollama-shaped fixtures do not establish either runtime integration. The map has no explicit SGLang runtime comparison, serving-metrics crosswalk, or GGUF/quantization compatibility entry. The free-tier provider-load entry is separately described as provider dispatch/load-test work, not local engine metrics. A declared-versus-served context-size comparison is explicitly still a frontier item, and the snapshot schema does not currently carry it. Evidence: `corpus/README.md` §Coverage map, §Known gaps and §Frontier; `PROVINCE.md` §Owns and §Observed state.

| Existing holder or gap | What the inspected index says it covers | ART opening |
|---|---|---|
| `knowledge/endpoint-identity.md` | Health/readiness classification and local probe conventions | Compare each engine’s documented health semantics without generalizing llama.cpp behavior. |
| `knowledge/served-model-identity.md` | Served-model reconciliation against expected IDs and aliases | Compare runtime inventory surfaces and their model-ID/digest meaning. |
| `corpus/README.md` §Known gaps | llama.cpp-only real-runtime reconciliation; vLLM/Ollama fixtures are not integration | Treat other engines’ docs as source leads, not local compatibility evidence. |
| `corpus/README.md` §Coverage map | Existing local listener, consumer, alias, drift and snapshot topics | No explicit local engine metrics or GGUF/quantization row is listed. |
| `corpus/README.md` §Frontier | Context-size reconciliation awaits a separate authorized feature move | Keep any context-capacity entry separate from model identity and health. |

## Current art — documentation opened in this session

### Engine-specific health and identity are not interchangeable

- **llama.cpp:** the current server README documents `GET /health` as a model-load readiness surface: it returns 503 while the model is loading and 200 when loaded. It documents `GET /v1/models` IDs as a model path by default or an explicitly configured `--alias`; the OpenAI-compatible surface is described as useful for many clients, not as a blanket conformance guarantee. `GET /slots` exposes slot state and `n_ctx`; `GET /metrics` exists only when `--metrics` is enabled. The current docs describe several of these as monitoring endpoints, but this does not turn a port listener, arbitrary 200, or request completion into model-identity proof. Sources: [S001] §GET `/health`, §GET `/v1/models`, §GET `/slots`, §GET `/metrics`.
- **vLLM:** stable online-serving docs list `/health`, `/v1/models`, `/load`, `/version`, and `/metrics` as distinct instrumentator surfaces. Its health API calls engine `check_health()` and reports 503 on `EngineDeadError`; the same handler returns 200 for render-only servers that have no engine. Thus even one engine’s `/health` is not a universal promise that the model was loaded for generation. No local vLLM integration is established by the API docs. Sources: [S002] §Instrumentator APIs; [S004] `health(raw_request)`.
- **SGLang:** native API docs distinguish `/health` from `/health_generate`; the latter checks health by generating one token. `/get_model_info` returns documented model metadata including `model_path`, `weight_version`, model type and architectures; `/server_info` returns CLI arguments, token limits and memory-pool sizes. These are engine-native observations, not a shared OpenAI contract. The v0.5.22 release notes also contain a health-check routing fix: “Prevent health checks from perturbing user request routing” ([S020], §Parallelism & Disaggregation). It is a versioned release note, not proof of a current local defect. Sources: [S006] §Get Model Info, §Get Server Info and §Health Check; [S020].
- **Ollama:** the current API introduction documents distinct local roots (`/api` and OpenAI-compatible `/v1`). Its `/api/tags` endpoint lists available local models and metadata; `/api/ps` lists models currently running and documents `digest`, `context_length`, VRAM size and expiry. Its OpenAI-compatibility page explicitly describes a supported subset. The pages opened here did not establish an Ollama Prometheus metrics endpoint; that is an unopened lead, not a claim that none exists. Sources: [S009] §Base URLs; [S010] §OpenAI compatibility and §Endpoints; [S011]; [S012].

**Implication for kama:** the common URL shape does not make route meanings or returned model fields portable. The repository’s real-runtime evidence remains llama.cpp-specific. Record engine/version and the exact native or compatible route used; do not promote documentation or parser fixtures into an assertion about a running local engine. OpenAI’s `/models` schema is a list of available IDs and basic metadata; it is a useful contract reference, not a runtime-health or loaded-weight proof. Sources: [S001], [S002], [S004], [S006], [S009]–[S012], [S016].

### GGUF and quantization are runtime facts, not identity shortcuts

- The GGUF specification describes a metadata-bearing, extensible inference format and explains model filename components. It explicitly cautions that the naming convention is not intended to be perfectly parsable across the diversity of filenames. Therefore a filename/quant suffix should not be treated as a canonical model-identity parser or a guarantee that a serving backend accepts the file. Source: [S014] §GGUF Naming Convention.
- llama.cpp’s official quantizer documentation separates conversion to GGUF from quantization, describes `llama-quantize` options such as importance matrices and tensor overrides, and warns that quantization can incur accuracy loss. Its published performance/size examples are model- and setup-specific; kama should not turn those examples into a model-quality verdict. Sources: [S015] §Overview, §Quantize and §Quantization; lane boundary in `SKILL.md` §Domain.
- vLLM and SGLang both publish hardware/method compatibility tables, with support dependent on runtime and backend. SGLang distinguishes offline pre-quantized weights from online dynamic quantization and warns against layering its online quantization option on a pre-quantized model. Ollama’s GGUF import guide says import does not quantize the file. Together, these sources support an engine-compatibility inventory, not a cross-engine guarantee from a GGUF suffix alone. Sources: [S005] §Supported Hardware; [S008] §Platform Compatibility; [S013] §Importing a GGUF model.

### Serving metrics are opt-in and have engine-specific semantics

- **llama.cpp** exposes Prometheus-compatible `/metrics` only with `--metrics`; its documented signals include prompt/generation token totals and throughput, processing/deferred request gauges, and slot/decode activity. `/slots` is separately enabled by default and can be disabled. Source: [S001] server flags and §GET `/metrics`.
- **vLLM** exposes `/metrics` on its OpenAI-compatible server. Its documented signals include running/waiting requests, KV-cache use, admission rejections, queue time, end-to-end latency, TTFT, inter-token latency and per-request phase timings. Custom histogram buckets add series per bucket and label combination, so metric cardinality and storage cost are explicit design concerns. Source: [S003] §General Metrics and §Custom Histogram Buckets.
- **SGLang** requires `--enable-metrics`; its documented signals include running/queued requests, token/cache usage, throughput and latency histograms. It defines streaming and non-streaming TTFT differently at the observation boundary and documents request-level TPOT separately from token-weighted inter-token latency. Example names include `sglang:time_to_first_token_seconds`, `sglang:request_time_per_output_token_seconds` and `sglang:num_queue_reqs`. Source: [S007] §Language model metrics and §Request-level time per output token.
- OpenTelemetry’s GenAI model-server conventions describe request duration, time per output token and time to first token, but the opened conventions page marks the material **Development**. Treat it as a potential naming/measurement crosswalk, not a stable mandatory contract. Prometheus recommends base units, unit/type suffixes and low-cardinality labels. Sources: [S019] §Generative AI model server metrics; [S018] §Metric names and §Labels.

These surfaces support a common operational question set—request success/error, queue/running pressure, cache use, TTFT, inter-token or per-request TPOT, end-to-end latency and token throughput—but not a universal metric-name or probe policy. Document each signal’s source, enablement flag and measurement boundary before comparing runtimes. Metrics are observability, not proof of configured consumer pins or served-model identity.

### Probe lifecycle concepts

Kubernetes’ official probe guidance separates startup (initialization), liveness (restart decisions) and readiness (traffic admission); it cautions that a bad liveness check can trigger cascading restarts under load. This is a useful lifecycle vocabulary if a kama-owned deployment later needs it, but Kubernetes policy is not evidence that a local non-Kubernetes service uses those semantics. A slow model load is a reason to distinguish startup/readiness from liveness, not to invent a health endpoint or restart policy. Source: [S017] §Types of probe, §When to use each probe and §Caution.

## Source registry — proposed `corpus/SOURCES.md` rows

Every row below names a first-party or standards-authority page opened in this session. `queued` means opened and worth mining; `watch` means fast-moving or development-stage material merits rechecking on release. None is marked `mined` because no lane knowledge entry currently cites these proposed rows. The table is append-only when transferred to the lane registry; later corrections should supersede, not rewrite, an admitted row.

| id | source | kind | tier | teaches | status | opened | recheck | used-by |
|---|---|---|---|---|---|---|---|---|
| S001 | llama.cpp server README — https://github.com/ggml-org/llama.cpp/blob/master/tools/server/README.md | docs | A | Engine routes, model IDs, readiness, slots and opt-in Prometheus signals for llama-server. | watch | 2026-10-19 | on-release | — |
| S002 | vLLM Online Serving — https://docs.vllm.ai/en/stable/serving/online_serving/ | docs | A | Stable server API inventory, including distinct health, model-list and metrics routes. | watch | 2026-10-19 | on-release | — |
| S003 | vLLM Production Metrics — https://docs.vllm.ai/en/stable/usage/metrics/ | docs | A | Current request, queue, cache, latency and token metric families plus histogram-cardinality caveats. | watch | 2026-10-19 | on-release | — |
| S004 | vLLM health API — https://docs.vllm.ai/en/stable/api/vllm/entrypoints/serve/instrumentator/health/ | docs | A | `/health` checks engine health; render-only mode is a distinct always-healthy case. | watch | 2026-10-19 | on-release | — |
| S005 | vLLM Quantization — https://docs.vllm.ai/en/stable/features/quantization/ | docs | A | Quantization formats and hardware support vary by implementation and device. | watch | 2026-10-19 | on-release | — |
| S006 | SGLang Native APIs — https://docs.sglang.io/docs/basic_usage/native_api | docs | A | Native health, one-token health generation, model information and server limits are separate surfaces. | watch | 2026-10-19 | on-release | — |
| S007 | SGLang Production Metrics — https://docs.sglang.io/docs/references/production_metrics | docs | A | Metrics opt-in, queue/cache/latency signals and distinct TTFT/TPOT accounting semantics. | watch | 2026-10-19 | on-release | — |
| S008 | SGLang Quantization — https://docs.sglang.io/docs/advanced_features/quantization | docs | A | Offline/online quantization behavior and platform-specific backend support. | watch | 2026-10-19 | on-release | — |
| S009 | Ollama API Introduction — https://docs.ollama.com/api/introduction | docs | A | Local native API and OpenAI-compatible base URLs are distinct. | watch | 2026-10-19 | on-release | — |
| S010 | Ollama OpenAI compatibility — https://docs.ollama.com/api/openai-compatibility | docs | A | Ollama exposes a documented subset of OpenAI API behavior and local client conventions. | watch | 2026-10-19 | on-release | — |
| S011 | Ollama List models — https://docs.ollama.com/api/tags | docs | A | `/api/tags` lists available local model names, digests and quantization metadata. | queued | 2026-10-19 | 90d | — |
| S012 | Ollama List running models — https://docs.ollama.com/api/ps | docs | A | `/api/ps` returns running-model digest, context, VRAM and expiry fields. | queued | 2026-10-19 | 90d | — |
| S013 | Ollama Importing a Model — https://docs.ollama.com/import | docs | A | GGUF import consumes a prepared file; Ollama does not quantize it during import. | queued | 2026-10-19 | 90d | — |
| S014 | GGUF specification — https://github.com/ggml-org/ggml/blob/master/docs/gguf.md | spec | A | GGUF structure/metadata and a naming convention explicitly not guaranteed to parse every filename. | watch | 2026-10-19 | on-release | — |
| S015 | llama.cpp quantize README — https://github.com/ggml-org/llama.cpp/blob/master/tools/quantize/README.md | docs | A | Quantization process, options, importance matrices and the limits of quality/performance examples. | watch | 2026-10-19 | on-release | — |
| S016 | OpenAI List models — https://developers.openai.com/api/reference/resources/models/methods/list | docs | A | Reference shape for the OpenAI `/models` list; not local-server readiness evidence. | queued | 2026-10-19 | 90d | — |
| S017 | Kubernetes Liveness, Readiness, and Startup Probes — https://kubernetes.io/docs/concepts/configuration/liveness-readiness-startup-probes/ | docs | A | Lifecycle distinction between initialization, restart health and traffic readiness. | queued | 2026-10-19 | 90d | — |
| S018 | Prometheus Metric and label naming — https://prometheus.io/docs/practices/naming/ | docs | A | Base units, informative type/unit names and high-cardinality label cautions. | queued | 2026-10-19 | 90d | — |
| S019 | OpenTelemetry GenAI metric conventions — https://github.com/open-telemetry/semantic-conventions-genai/blob/main/docs/gen-ai/gen-ai-metrics.md | spec | A | Development-stage model-server request-duration, TTFT and time-per-output-token conventions. | watch | 2026-10-19 | on-release | — |
| S020 | SGLang v0.5.22 release — https://github.com/sgl-project/sglang/releases/tag/v0.5.22 | docs | A | Versioned current-art release notes, including a health-check routing fix and serving changes. | watch | 2026-10-19 | on-release | — |

## Candidate knowledge entries

### Candidate K01 — `runtime-health-surface-matrix.md`

- **Falsifiable claim:** The documented `/health` route does not encode one portable readiness meaning across these engines: llama.cpp reports loading vs loaded state; vLLM invokes engine health (with a render-only exception); SGLang separately offers health and a health check that generates one token.
- **Source and exact location:** S001 §GET `/health`; S004 `health(raw_request)`; S006 §Health Check. S006 says: “Check the health of the server by generating one token.”
- **Coverage row:** extend `knowledge/endpoint-identity.md`; do not replace the llama.cpp-specific proof or introduce an unverified local endpoint.
- **Recheck:** revisit the cited engine docs on release; specifically S001 `GET /health`, S004 `health(raw_request)`, S006 `Health Check`.
- **QUALITY fit:** KQ1 is respected because this is a documented route contract, not a current local verdict; KQ3 by preserving exact source/section and recheck cadence; KQ4 by explicitly not treating fixtures/docs as runtime integration; KQ5 by not starting a service or sending a generation request.

### Candidate K02 — `provider-model-inventory-boundaries.md`

- **Falsifiable claim:** A shared `/v1/models` path does not guarantee shared identity semantics or identify the same runtime fact: llama.cpp defaults its listed `id` to a model path unless aliased, while Ollama’s native `/api/ps` lists currently running models with a digest and context/VRAM fields. Use the engine’s documented loaded-model surface when the question is “what is loaded”; keep that separate from a consumer’s configured pin.
- **Source and exact location:** S001 §GET `/v1/models`; S010 §Endpoints `/v1/models`; S011 `/api/tags`; S012 `/api/ps` schema. S001 says: “By default, model `id` field is the path to model file, specified via `-m`.”
- **Coverage row:** extend `knowledge/served-model-identity.md` with an engine-scoped inventory crosswalk; preserve the existing llama.cpp normalization rule.
- **Recheck:** compare the cited `/v1/models`, `/api/tags` and `/api/ps` docs on release; a real local digest/model assertion still requires an authorized current probe and its command/exit evidence.
- **QUALITY fit:** KQ1/KQ2 remain hard gates for any live claim (configured pin, loaded-model response and endpoint verdict stay separate); KQ3 requires re-anchoring moving API docs; KQ4 prevents documentation or fixtures being called integration; KQ5 keeps endpoint credentials and consumer configuration out of the entry.

### Candidate K03 — `serving-observability-signal-crosswalk.md`

- **Falsifiable claim:** `/metrics` enablement and names differ by runtime; a useful cross-engine panel must state each source flag and metric definition before comparing queue pressure, cache usage, TTFT, TPOT/inter-token latency, end-to-end latency or token throughput. Metrics do not establish pin correctness or model identity.
- **Source and exact location:** S001 §GET `/metrics`; S003 §General Metrics and §Custom Histogram Buckets; S007 §Language model metrics and §Request-level time per output token; S018 §Labels; S019 §Generative AI model server metrics. S007 says: “For streaming requests it ends when the first output arrives after detokenization.”
- **Coverage row:** add a dedicated local serving-observability row to `corpus/README.md` and a new knowledge entry, separate from the free-tier provider-load entry.
- **Recheck:** on each serving-engine release, compare those route/flag/measurement sections; keep the OTel crosswalk labeled Development until its authority changes.
- **QUALITY fit:** KQ1 is respected by making no present health/readiness claim; KQ3 requires exact version/section anchors; KQ4 forbids calling a scrape/sample continuous monitoring; KQ5 forbids collecting credentials or prompt content as telemetry.

### Candidate K04 — `gguf-compatibility-metadata-boundary.md`

- **Falsifiable claim:** A GGUF filename or quantization suffix alone is not a robust identity parser or cross-runtime support certificate: GGUF naming is explicitly not perfectly parseable, backend/hardware support differs across vLLM and SGLang, and Ollama import does not quantize the file.
- **Source and exact location:** S014 §GGUF Naming Convention; S005 §Supported Hardware; S008 §Platform Compatibility and its offline/online quantization note; S013 §Importing a GGUF model. S014 says: “It is not intended to be perfectly parsable in the field due to the diversity of existing gguf filenames.”
- **Coverage row:** add a GGUF/quantization-runtime-compatibility row to `corpus/README.md`; keep actual model-quality judgments outside kama’s domain.
- **Recheck:** on release, recheck the GGUF spec and both runtime support tables; recheck Ollama’s import guide before claiming an importer behavior.
- **QUALITY fit:** KQ1/KQ2 are preserved by not turning a filename into live served identity; KQ3 by date/versioning changing compatibility tables; KQ4 by not claiming a real backend load; KQ5 and the lane boundary prohibit quantization evaluation or service changes.

### Candidate K05 — `context-capacity-is-a-separate-serving-fact.md`

- **Falsifiable claim:** The opened runtime APIs expose context-related values through engine-specific fields (`/slots` `n_ctx` for llama.cpp, `/api/ps` `context_length` for Ollama, and token-limit information in SGLang `/server_info`); these values should be compared only as a separate declared-versus-served-context measurement, not inferred from model ID or a historical default.
- **Source and exact location:** S001 §GET `/slots`; S006 §Get Server Info; S012 `/api/ps` schema. S012 describes `context_length` as: “Context length for the running model.” The repo’s explicit target is `corpus/README.md` §Frontier.
- **Coverage row:** fills the named context-size frontier item without expanding the model-identity rule or mutating the snapshot schema in this research wave.
- **Recheck:** recheck S001 `/slots`, S006 `/server_info` and S012 `/api/ps` on release; do not claim a local served context until an authorized runtime permits a current probe.
- **QUALITY fit:** KQ1 requires a sampled command/revision/verdict/exit for any local value; KQ3 requires historical context claims to remain dated; KQ4 keeps this docs-only finding distinct from runtime integration; KQ5 leaves runtime authorization and schema changes to a later explicitly authorized feature move.

## Paths

- **Health and readiness —** S001 → S004 → S006 → S020 → S017: start with kama’s actual llama.cpp evidence, compare vLLM and SGLang endpoint behavior, inspect the current SGLang health-routing release note, then use Kubernetes lifecycle vocabulary without importing Kubernetes assumptions into a local service.
- **Served identity and GGUF boundary —** S016 → S001 → S010 → S011 → S012 → S014 → S015 → S005 → S008 → S013: establish the generic model-list shape, compare each engine’s identity and running-model surfaces, then inspect format/quantization and runtime support separately.
- **Serving observability —** S001 → S003 → S007 → S019 → S018: learn each server’s exporter and signal definitions first, then compare with the development-stage GenAI metric vocabulary and Prometheus naming/cardinality guidance.

## Rejected candidates — evidence of taste

- **One universal `/health` pass rule:** rejected because the opened first-party docs give different health/readiness meanings and a one-token generation check is not equivalent to an HTTP liveness check. Preserve runtime-specific semantics; do not weaken KQ1.
- **“OpenAI-compatible” means full OpenAI behavioral equivalence:** rejected because Ollama describes a subset and llama.cpp disclaims strong compatibility claims. Probe the exact route/field the consumer needs; do not let a working client request stand in for identity evidence.
- **A completion request is a harmless model-identity probe:** rejected because the lane’s existing `SKILL.md` §Request-time id does not validate the model records a 200 response for a bogus requested model ID. Keep identity on documented inventory routes; no generation request was made for this dossier.
- **A regex over GGUF filenames can recover canonical identity and runtime support:** rejected because S014 says the convention is not perfectly parseable; the existing lane rule is deliberately narrower (basename, optional `.gguf` suffix, case-sensitive comparison). Keep format metadata separate from the expected served ID.
- **Rank quantizations or claim a “best” format from published speed/size tables:** rejected as model-quality/eval work, explicitly outside kama’s province. S015 describes accuracy-loss measures and setup-specific examples; neither is a local authorized quality evaluation.

## Mistakes mined from the existing lane rules

| ID | Mistake class | Evidence pointer | Already captured? Sweep result |
|---|---|---|---|
| M01 | Treating `/health` as served-model identity. | `SKILL.md` §Anti-patterns, “Reading `/health` as identity”; `corpus/QUALITY.md` KQ1. | Yes: the complete SKILL anti-pattern section and all listed QUALITY criteria were read; KQ1 explicitly rejects health-only identity claims. |
| M02 | Comparing a path-shaped served ID to a bare configured ID as a raw string. | `SKILL.md` §Served-id normalization and §Anti-patterns, “Comparing ids as raw strings.” | Yes: the existing rule specifies source-field precedence, basename, `.gguf` stripping and case-sensitive comparison. |
| M03 | Treating HTTP 200 from a completion with an incorrect requested model ID as identity proof. | `SKILL.md` §Request-time id does not validate the model; §Anti-patterns, “Validating identity with a completion request.” | Yes: KQ1 and the existing runbook direct identity to `/v1/models`; a completion response is explicitly rejected. |
| M04 | Treating a configured/inherited pin, status line, or one working consumer as a live/effective endpoint. | `SKILL.md` §Anti-patterns, items on configured status, registry coverage and inherited/raw rows; `corpus/QUALITY.md` KQ2. | Yes: KQ2 separates pin provenance, endpoint verdict and effective runtime selection; reconcile the registry, not a single consumer. |
| M05 | Treating an open port/listener as a model-serving endpoint without fingerprinting its responder. | `SKILL.md` §Anti-patterns, “Treating a listening socket as a model”; `corpus/README.md` coverage row for `knowledge/listener-census.md`. | Yes: the lane requires listener classification and prefers authorized declared pins; no new criterion proposed. |
| M06 | Treating vLLM/Ollama parser fixtures as real-runtime integration. | `corpus/README.md` §Known gaps; `corpus/QUALITY.md` KQ4. | Yes: the lane explicitly distinguishes fixtures from integration; the opened docs add no local-runtime evidence. |

## Coverage gaps and defect boundary

These are ART coverage gaps, not evidence of a faulty runtime or a failed round. The sampled files state important gaps rather than concealing them. No full lane contract audit was performed: the ART read set did not include the scorecard, lane log, manifest, or every knowledge-entry body, so this dossier does not claim those files are structurally defect-free.

| ID | Gap found in the inspected ART surface | Evidence and bounded consequence |
|---|---|---|
| D01 | Cross-engine health/model-identity semantics are not yet an admitted lane knowledge row. | The coverage map centers the llama.cpp runbook; README §Known gaps says real-runtime reconciliation is llama.cpp-only and vLLM/Ollama fixtures are not integration. The docs here are a source crosswalk only. |
| D02 | The corpus map has no explicit local serving-metrics/observability row. | The existing `endpoint-identity.md` summary names health/readiness/probes, and the free-tier entry is described separately as provider load tests. Engine metrics remain uncovered in the inspected map. |
| D03 | The corpus map has no explicit GGUF/quantization/backend-compatibility row. | Current docs expose materially different runtime/hardware support and import behavior; this dossier proposes a scoped source entry, not a quality ranking. |
| D04 | Declared-versus-served context-size comparison remains frontier debt. | README §Frontier explicitly requires a separate feature move under authorized runtime conditions; no context value was sampled here. |

## Leads (unopened)

These are discovery leads only, not source-registry rows; none was opened in this session.

- llm-d, **Model-Aware Readiness Probes** — https://llm-d.ai/docs/dev/operations/lifecycle/readiness-probes — specialized inference readiness policy to assess without importing gateway/dispatch ownership.
- vLLM, **Per-Request Metrics** — https://docs.vllm.ai/en/latest/features/per_request_metrics/ — determine how request-level measurements complement server histograms.
- vLLM, **Prometheus and Grafana** — https://docs.vllm.ai/en/latest/examples/observability/prometheus_grafana/ — inspect an official scrape/dashboard example and its version assumptions.
- SGLang, **Model Gateway** — https://docs.sglang.ai/advanced_features/sgl_model_gateway.html — assess only whether gateway health is relevant; dispatch and routing mechanism remain outside kama.
- Ollama, **API usage** — https://docs.ollama.com/api/usage — inspect whether current usage/performance documentation adds an observability surface; do not infer a metrics endpoint from absence in this dossier.
- llama.cpp, **merged `/v1/metrics` change** — https://github.com/ggml-org/llama.cpp/pull/18001 — inspect the change history only if needed to anchor metrics endpoint evolution beyond the current README.

## Top recommendations

- Add a runtime-scoped health/model-inventory crosswalk, keeping llama.cpp’s current proven runbook authoritative and all other engines explicitly documentation-only until authorized real-runtime evidence exists.
- Add a small serving-metrics knowledge entry with exact exporter flags, signal definitions, measurement boundaries and cardinality cautions; keep it distinct from liveness and model identity.
- Add a separate GGUF/quantization compatibility note and preserve the existing context-size frontier as an independent authorized feature move; do not admit quality rankings or infer support from filenames.
