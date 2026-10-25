# round-3 findings — kengaku-shokunin (LLM/model research & evaluation)

Date: 2026-09-28. Commit in child repo: `a4c056e round-3` (tree clean).

## Gap selected

Corpus README round-1 gaps: "no executed benchmark run" + "no local
route-telemetry corpus." Root cause identified as a round-1 search-then-judge
failure: `find -iname "*telemetry*"` had already surfaced both artifacts;
I pattern-matched filenames to "irrelevant harness" without reading them.

## Executed this round (real surfaces, command-verified)

1. **`~/bench-arena/`** — completed 33-task, two-model coding battery.
   - Telemetry schema captured: `task,status,opencode_rc,closed_fence,output_sha256,prompt_tokens,predicted_tokens,inference_latency_ms,tokens_per_sec,test_runtime_ns,telemetry_source,telemetry_available`.
   - Results: qwenlocal-v2 PASS 21/33 vs grok45 19/33.
   - Complementarity: win-sets near-disjoint — grok45-only 8 (regex/log/SQL/format-transform class), qwenlocal-only 10 (DS/algorithms/concurrency class), both-fail 4 (semver-regex, knapsack-reconstruct, rwlock-writer-pref, metaclass-shadowing).
   - FAIL median latency 60.9 ms < PASS 79.5 ms — early-bail signature.
   - `20-csv-group-sum` carries `inference_latency_ms:"NULL"`, `telemetry_available:"n"` — real parsing hazard documented.
2. **`~/Projects/bounties/ledger/telemetry.jsonl`** — 7,218-line live
   lane-routing corpus (the PROVINCE.md "route telemetry" surface).
   - Event taxonomy profiled: `dispatcher_tick` 3,680, `mission_parked` 1,188, `mission_dispatched` 1,167, `attempt_reset` 68 vs `mission_done` 26 — resets 3× completions.
   - Reroute grammar: `lane_parked`+`cause` (`usage_limit*`, `empty_output`, `EROFS`, `subagent exit 1`) → `action:reroute`+`to:`; `scope:GROUP` preserves lane identity; `local degrade (I3)` = bucket walk exhausted.
   - Lane→model counts: `grok-4.6:low` 621, `gpt-daybreak-blue-latest:max` 276, `gpt-6-astra:max` 123, `grok-4.6:xhigh` 91, `qwen3.8-max:xhigh` 42, `kimi-code/k3:max` 24.
   - Interpretation rule: a lane's effective model is a sequence — replay `lane_parked`/`reroute` chains per `run_id`; usage-limit causes ≠ model failures.

## Files landed (kengaku-shokunin only)

- `corpus/knowledge/local-bench-arena.md` — battery schema, results, 3 falsifiable claims (win-set complementarity; task-class failure clustering → router hypothesis; discriminating-task set to keep).
- `corpus/knowledge/ledger-route-telemetry.md` — event taxonomy, reroute/degrade signatures, 3 falsifiable claims (model-as-sequence; meter-vs-failure attribution; park/dispatch symmetry ≈ congestion-bound).
- `corpus/lessons/round-3.md` — 4 lessons: filename-judging search failure; pass-rate hides complementarity; NULL defensive parsing; FAIL-latency signature.
- `corpus/README.md` — index + gap list updated; route-telemetry and executed-run gaps closed (fresh authored execution still open).
- `SKILL.md` — new "Local telemetry surfaces" subsection under Route-telemetry: two-corpus distinction, ledger taxonomy, parsing rules (NULL, FAIL-latency, win-set diff); cited-sources list extended.
- `LOG.md` — round-3 entry with all evidence above.

## Anti-pattern check (SHONEN)

- Zero-width chars: `grep -P '[\x{200B}-\x{200D}\x{FEFF}]'` clean on all touched files.
- No changes to `MANIFEST.json`, other shokunin repos, or files outside `kengaku-shokunin/` + this report.
- Round-1 report filename was `kengaku-shokunin.md`; this round's prompt specifies `kengaku.md` — written as instructed (round-3 path).

## Still open

- Fresh benchmark execution authored *in* this repo (SHONEN checkbox) — bench-arena analysis is artifact interpretation, not an authored run.
- `wiki/ai/alignment-and-training/`, `wiki/ai/foundations/`, `wiki/karpathy/` undigested.
- `llm-wiki-site`/`llm-wiki-public` siblings uninspected.
