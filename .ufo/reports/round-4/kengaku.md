# round-4 findings — kengaku-shokunin (LLM/model research & evaluation)

Date: 2026-09-28. Commit in child repo: `round-4` (tree clean).

## Gap selected

Three open fronts from `corpus/README.md` gaps + SHONEN promotion checklist:
(1) no *authored* end-to-end eval — SHONEN box 2 blocker; (2) un-digested
wiki branches (`karpathy/`, `foundations/`, `alignment-and-training/`) and
un-digested gemini suite pages (aggregator audit flagged); (3) sibling
repos `llm-wiki-site`/`llm-wiki-public` uninspected. An uncommitted
aggregator audit (`corpus/lessons/round-1-aggregator-audit.md`) landed in
the tree mid-round and filed 3 citation defects + 3 next-round gaps — all
closed this round.

## Executed this round (real surfaces, command-verified)

1. **Authored eval slice vs live local model** — first end-to-end run
   owned by this domain (SHONEN box 2 now checked).
   - Endpoint drift found and proven: `~/.config/opencode` provider
     `qwen-local` targets `localhost:8080` — now Jitsi (404 on
     `/v1/models`); the real llama-server (`qwen-coder.service`,
     Qwen3-Coder-30B-A3B-Instruct-UD-IQ2_XXS) listens on `127.0.0.1:34113`
     (`/health` ok, `/v1/models` returns served id). Root-causes v2's
     `"NULL"`/`journal`-source telemetry rows.
   - Ran 4-task slice (01, 02, 03, 05) via direct `chat/completions`
     (temp 0.2) + repo `grade.sh`: **1/4 PASS vs ex-ante predicted 2/4**.
     `03-extract-isodatetimes` flipped PASS→FAIL on a fresh generation
     (different sol_sha) — n=1 sampling noise at the boundary.
     Artifacts: `/tmp/bench-r4/` (ephemeral), permanent record in
     `corpus/knowledge/bench-arena-fresh-run.md`.
2. **Eval-theory digest** — `yao-second-half` (autonomy + IID assumptions),
   `creative-benchmark` (RLHF mode collapse, diversity primitives),
   `llm-trueskill-sorting` (judge-vs-aggregator split, μ−3σ, 1–2
   matches/item), `rlhf` (proxy gap, Bradley-Terry), `bitter-lesson`
   (regime caveat via Gigerenzer) → `knowledge/eval-theory-notes.md`.
   Plus `gemini-3.1-pro-godspeed-{benchmarks,test-battery}` →
   `knowledge/gemini-benchmark-suite.md` (audit gap closed).
3. **Bailian CLI telemetry profiled** — `~/.bailian/telemetry.jsonl`:
   4,274 records, 2026-08-21→09-16. `usage token-plan` 85% fail
   (429 quota × 675), auth-expiry is dominant error (2,685), `video
   task get` 75% fail = async-poll noise →
   `knowledge/bailian-cli-telemetry.md` (audit-requested surface).
4. **Open model catalogs** — HF `api/models` and OpenRouter
   `api/v1/models` (460 models) probed live, schemas captured →
   `knowledge/open-model-catalogs.md`; local GGUF inventory rule added.
5. **Audit defects closed**: `telemetry-run-design.md` source re-pointed
   to `iteration-3.md:156`; `PROVINCE.md` stale `~/wikillm` path fixed;
   README dangling paths corrected (`wiki/ai/books/` exists;
   `are-we-smart-enough` is under `wiki/biology/books/` — out of domain).

## Files landed (kengaku-shokunin only)

- `corpus/knowledge/`: +`bench-arena-fresh-run`, +`eval-theory-notes`,
  +`gemini-benchmark-suite`, +`bailian-cli-telemetry`,
  +`open-model-catalogs`; `telemetry-run-design.md` citation fixed.
- `corpus/lessons/`: +`round-4.md` (5 lessons); +`round-1-aggregator-audit.md`
  (orchestrator-authored, committed as landed).
- `corpus/README.md`: index + coverage map + gap list fully reconciled.
- `SKILL.md`: new "Running a battery against the local model" ops rules,
  "Model catalogs (non-Bailian)", "Eval-theory rules"; FAIL-latency claim
  re-scoped to population level; production checklist gained
  endpoint-probe (step 2) and n≥2 repeat rule (step 7); sources extended.
- `PROVINCE.md`: stale path corrected. `SHONEN.md`: executed-task box
  checked. `LOG.md`: 2 evidence-dense round-4 entries.

## Anti-pattern check

- Zero-width scan clean on all touched files (`grep -P '[\x{200B}-\x{200D}\x{FEFF}]'` → no hits).
- No writes outside `kengaku-shokunin/` except this report; user config
  untouched (endpoint drift reported, not "fixed" — operator decision).

## Still open

- `karpathy/talks/`, `projects-and-tools/`, `standards-and-specifications/`,
  `wiki/ai/foundations/complexity.md`, `wiki/ai/books/` undigested.
- Full 33-task re-run under corrected endpoint config (would produce the
  first apples-to-apples drift measurement vs Aug-29 baseline).
- Operator decision pending: repoint `qwen-local` baseURL 8080→34113.
