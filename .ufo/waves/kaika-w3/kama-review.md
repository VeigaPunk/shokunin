# kaika W3 — non-author verification: kama round 10

Reviewer: W3ReviewKama (fresh, non-author; orchestrator-dispatched). Subject: lane commit `1e41928ab` (branch `kaika/round`, base `35e9175fc`). Recommendation only; the orchestrator adjudicates and records closure. Read-only: no edits, no staging, no branch changes. Host-state and live-endpoint probes were NOT re-run (see §12).

## 0. Summary

- **Recommendation: ADMIT, conditional** on three appended errata (§13). Not a clean admit.
- Verified: provenance, append-only (for LOG/lessons/QUALITY), C1 counting claim (narrow), C3 census + coverage, no-harm, credential sweep, report contract.
- Blocking-for-clean: (D-1) campaign documentation-only rule breached by the L1 live gate runs, disclosed but not excluded; (D-2) SCORECARD axes table not updated for round 10; (D-3) lesson's Mistake-14 count contradicts its own "15 → 0" target (29 at head).

## 1. Provenance — PASS

```
git log --format='%h %an <%ae> | %cn <%ce> | %s' 35e9175fc..1e41928ab
1e41928 kama-shokunin <kama@shokunin.local> | kama-shokunin <kama@shokunin.local> | round-10: sources registry (30 rows) + 3 cross-engine entries; 50 stale anchors re-anchored by appended corrections; KQ6-KQ10
```
One round commit; author and committer both `kama-shokunin <kama@shokunin.local>`. Lane HEAD = `1e41928aba2b81dd65ea75084918a7fadf453720`; report cites `1e41928` (kama.md line 3) — hash is HEAD, ancestry holds.

## 2. Append-only — PASS for LOG.md, corpus/lessons/*, corpus/QUALITY.md; 5 disclosed in-place line edits elsewhere

```
git diff 35e9175fc..1e41928ab -- LOG.md corpus/lessons corpus/QUALITY.md   → only '+' lines (LOG +9/-0; QUALITY +12/-0; lessons all +N/-0)
git diff 35e9175fc..1e41928ab | grep -nE '^-[^-]'
  443  -| — none yet — | | | |                                   SCORECARD.md capability placeholder row → replaced
  450  -The lane's saturation line ... not asserted by this conformance change.   SCORECARD.md → replaced
  482  -  availability is not inferred from this lane's dated alias census.   SKILL.md last line (no final newline) → same text + newline
  516  -  `.ufo/round-5/continuation.md`; no outside-repo repair is absorbed here.   corpus/README.md last line → same text + newline
  625  -   crash-loop ends in a silently dead endpoint that no consumer registry watches.   knowledge/consumer-registry.md last line → same text + newline
```
No deletion in LOG.md, QUALITY.md, lessons, or any knowledge/ file other than the newline-only last line. The three newline-only rewrites are byte-identical in text (verified by the diff pairs). SCORECARD replacements are disclosed in LOG.md (lane's own "append-only exceptions" bullet). `corpus/SOURCES.md` is new (no in-place change).

## 3. Claims

### C1 — freshness: 50 stale anchors → 0 uncorrected — VERIFIED (narrow)

Counting loop: the lesson's §Corrections loop, extracted verbatim into a script and run with the tree and ledger path as parameters. Ledger = `1e41928:.ufo/round-10/audit/stale-anchors.tsv`.

| Tree | Command | Output | Report says |
|---|---|---|---|
| head `1e41928` | `bash count.sh <head> <ledger>` | `rows=50` / `0` | rows=50, uncorrected **0** — match |
| base `35e9175` | `bash count.sh <base> <ledger>` | `rows=50` / `50` | uncorrected **50** — match |
| base, non-circular | for each row, `sed -n "${line}p" base/$f \| grep -qF "$old"` | `0` MISS | "all 50 old_pointers present on their base lines: 0 MISS" — match |

Caveat (D-6): the base value 50 is definitional — at `35e9175` the correction tag cannot exist, so the loop counts absence of the tag. What the before-state actually shows is the non-circular check: ledger pointers sit on the lines they name. The 50→0 movement measures correction coverage, not staleness.

Staleness evidence, repo-local rows: 30 of 50 ledger rows have a `stale_check` that reads only repo files (`nl`, `sed`, `grep`). I re-ran them at head (`/tmp` scratch copy). Sampled and matching their correction text: A01 (`tools/kama-probe.sh` 47-48 "Persisted rows…", 61-62 timeouts, 83-85 cleanup), A40 (`tools/kama-probe.sh` now exists; probe-mutation-matrix line 3 "repository currently has no" is stale), A41 (`kama-probe.sh` 799-803 result-path, 932-934 transitions), A44 (SCORECARD 10 vs 19), A48 (`alias-endpoint-normalization.md:11` holds m_flash; SKILL 120/317 do not), A50 (free-tier status board rounds 6-9 only, `free-tier-provider-limits.md:26-33`). A02/A10 partially checked.

Not re-run: 20 host-state rows (§12, D-4).

Side finding (D-3): the lesson's Mistake 14 count (`stale_named_lines`, round-10.md §Mistakes row 14 and its code block), run with the lesson's own grep set:
```
base: 15     head: 29
```
The head value is not reported anywhere. The correction blocks themselves re-quote the stale pointers (e.g. `corpus/lessons/round-1-safety.md:106`), so the count rises as corrections land and cannot reach 0 under append-only corrections.

Score 7→8 (freshness): recommend accept narrowly; see §9.

### C3 — capability `sources-registry` + expansion (coverage) — VERIFIED

Census (contract v1, validate mode) at the lane root:
```
bash fleet-census/scripts/sources-census.sh validate <kama-shokunin> → kama-shokunin	ok	…/corpus/SOURCES.md   exit=0
```
Contract §Census commands at head: rows **30**; malformed **0**; tiers **A=27 C=3**; status **mined=17 queued=8 rejected=5**; duplicate ids none; enum/tier-inflation none; missing used-by none. All match the report's C3 row.

Coverage (base → head), `ls corpus/knowledge/*.md | wc -l` / `grep -lE '^source: S[0-9]{3}' … | wc -l` / coverage-map awk:
```
base: knowledge=9 sourced=0 coverage_rows=19
head: knowledge=12 sourced=3 coverage_rows=24
```
Matches the report (9→12; 0→3; 19→24).

### No-harm — VERIFIED
```
md5sum tools/kama-probe.sh → 1f81e859c2d7f43f87d1f7e01327b2cf (base and head)
md5sum tools/test-snapshot.sh → 860f26ac05938cdfc1a8816eff1570b4 (base and head)
bash tools/test-snapshot.sh (hermetic, mktemp fixtures) → RESULT pass=24 fail=0 (base and head)
git diff --stat 35e9175fc..1e41928ab -- tools registry → empty
```

### Plan claim 2 (gate-bundle refresh as operability) — closed-not-claimed: agree.

## 4. SOURCES — validate exit 0 — PASS

```
$ bash fleet-census/scripts/sources-census.sh validate <kama-shokunin>
kama-shokunin	ok	/home/vgpnk/Projects/shokunin/.tower/worktrees/kaika/kama-shokunin/corpus/SOURCES.md
exit=0
```

Rows re-opened (fetch 2026-10-19 by reviewer; quotes checked against fetched text):

| Row | Tier / status | Re-opened | Gate quote | Anchor check | Verdict |
|---|---|---|---|---|---|
| S001 llama.cpp server README | A / mined | `raw.githubusercontent…/master/tools/server/README.md` | "Explanation: the model is successfully loaded and the server is ready." | line 490 (§GET /health, 200 branch); line 486 `503 "Loading model"`; line 1133 "only accessible if `--metrics` is set"; line 1148-1149 `llamacpp:requests_deferred`, `llamacpp:n_tokens_max` | match (master, not pinned c0fd7862; pin is in SOURCES row) |
| S004 vLLM health handler | A / mined | `docs.vllm.ai/…/instrumentator/health/` | "Render-only servers have no engine; they are always healthy." | source block `health(raw_request)`: `if client is None: # Render-only …  return 200`; `except EngineDeadError: 503` | match |
| S005 vLLM quantization | A / mined | `docs.vllm.ai/en/stable/features/quantization/` | "This compatibility chart is subject to change as vLLM continues to evolve" | Supported Hardware table GGUF row: ✅ Volta–Hopper, ✅ AMD GPU, ❌ Intel GPU, ❌ x86 CPU, ❌ Arm CPU; page dated September 14, 2026 | match |
| S020 SGLang v0.5.22 | A / mined | `github.com/sgl-project/sglang/releases/tag/v0.5.22` | "[Fix][DP] Prevent health checks from perturbing user request routing" | release notes line present; commit `baa9bef`; "released this 19 Oct" | match |
| S026 llama.cpp PR #18001 | A / **rejected** | `github.com/ggml-org/llama.cpp/pull/18001` | "the `/v1` is reserved for openai-compatible API" (ngxson, Dec 14 2025) | PR state Open; quote present | match — rejection holds |
| S013 Ollama import | A / mined | `docs.ollama.com/import` | "Ollama does not quantize GGUF models during import." | present verbatim | match |
| S015 llama.cpp quantize README | A / mined | `github.com/ggml-org/llama.cpp/blob/master/tools/quantize/README.md` | "Quantization is done in two phases" / "can severely reduce quality compared to quantizing from 16bit or 32bit" | both present | match |
| S007 SGLang production metrics | A / mined | `docs.sglang.io/docs/references/production_metrics` | "…ends when the first output arrives after detokenization…" | present; `--enable-metrics` present | match |
| S003 vLLM metrics | A / mined | `docs.vllm.ai/en/stable/usage/metrics/` | "Every bucket boundary creates one extra time series per metric and per label combination" | present (line-wrapped in source) | match |
| S009 Ollama API intro | A / queued→mined | `docs.ollama.com/api/introduction` | "Ollama's API isn't strictly versioned, but the API is expected to be stable and backwards compatible." | text present, but page apostrophe is U+2019 (’), Gate quote is ASCII ' | substance match; quote bytes differ (D-8) |
| S010 Ollama OpenAI compat | A / mined | `docs.ollama.com/api/openai-compatibility` | "Ollama supports a subset of the OpenAI API" | present (inside link markup); 0 "health" hits in S009/S010 | match (supports "no health route in opened pages") |

Gate-quoted metric names verified in S001/S003/S007 by grep: all 9 llama.cpp names, all 9 vLLM names, all 12 SGLang names in the crosswalk table exist; "TTFT" absent from S001 (0 hits), consistent with "not documented in opened page".

Not re-opened: S008 (table cells present; row mapping and quote not parsed), S014, S017, S019, S002, S006, S018, S021–S025, S011, S012, S016, S027–S029 (C-tier, queued/rejected by rule).

## 5. Discernment spot-check (LEARNING.md) — agree on 7 of 7 sampled decisions

| # | Decision | Item | Reviewer check | Verdict | Reason |
|---|---|---|---|---|---|
| 1 | admit | `knowledge/runtime-health-surface-matrix.md` — vLLM `/health` row | fetched S004 source | **agree** | vLLM 503 only on EngineDeadError and render-only 200 both verbatim in source |
| 2 | admit | `knowledge/serving-metrics-crosswalk.md` — llama.cpp metric names | grep S001 for 9 names; TTFT 0 hits | **agree** | names verbatim; "not documented in opened page" is accurate for the opened page |
| 3 | admit | `knowledge/gguf-runtime-compatibility-boundary.md` — vLLM GGUF hardware row | fetched S005 table; S013/S015 quotes | **agree** | hardware row and quotes match; "not a support certificate" framing is correct |
| 4 | reject | S026 (llama.cpp PR #18001) | fetched PR | **agree** | open PR, maintainer objection quoted; not a released contract. Tier A is scoped to "proposal history only", defensible (D-10) |
| 5 | reject | S027, S028 (community issues) | registry rows; contract rule "community is never A" | **agree** | feature requests cannot establish released behaviour (not re-opened) |
| 6 | reject | S024 (SGLang Model Gateway) | registry row (domain: kumitate) | **agree** | gateway routing is adjacent (AXES adjacency rule); flip stated (not re-opened) |
| 7 | reject (rule) | S030 (L1 `check` sample) | lesson §Contested L1 gate runs | **agree** on rejection, flag D-1 | correct under the documentation-only binding; the L1 should not have produced the sample |

Result: no disagreement on admits or rejects. Discernment trend: improved, provisional (n=7; §10).

## 6. New knowledge entries — header trio present; recheck citations re-run; claims match sources

- All three open with `source:` / `verified-at:` / `recheck:` on lines 2–4 (checked in diff hunks and `head`).
- `recheck:` values are citations + cadence (e.g. "on-release — S001 §GET `/health`; S004 `health(raw_request)` source…"), which the contract accepts ("the command or citation that re-verifies it"). I re-ran the cited checks for S001, S004, S005, S007, S003, S013, S015, S020 (§4).
- Claim-vs-source: no false claim found in the sampled sentences. Absence claims are scoped ("not documented in the opened page"; Ollama "no health route in the two opened pages" — confirmed 0 "health" hits in S009/S010).
- Unverified sub-claims: llama.cpp `/v1/health` alias and `--alias` behaviour; SGLang TPOT boundary wording; SGLang gguf "Yes/No" row mapping; OTel names (S019 not fetched).

## 7. Credentials — PASS

```
git diff 35e9175fc..1e41928ab | grep -nE 'op://[A-Za-z0-9]|BEGIN [A-Z ]*PRIVATE KEY|ghp_[A-Za-z0-9]{20,}|AKIA[0-9A-Z]{16}|xox[baprs]-[A-Za-z0-9]'
(no output; exit 1)
```
Broader sweep (`authorization:|api[_-]?key|sk-…|bearer |password|secret`): 2 hits, both prose — lesson round-10.md Mistake 10 description ("Redaction regex matched `token` inside a route alias") and round-2.md carry-forward rule ("without printing provider secret values"). No credential value in the diff. Gate JSON files (`.ufo/round-10/gates/*.json`) read: no secrets; they carry command stdout only.

## 8. Report — contract PASS

`fleet-ledger/.ufo/reports/round-10/kama.md` sections present in order: Work performed (names declared claims C1, C3 — line 7-9); Landed changes; Before → after measurements; SHONEN; Sources & frontier; Mistakes; Trend verdicts; L0 questions; Integrator notes. SHONEN: four lines, all `[~]` with pointers; zero `[x]`, so no unnamed verifier. Cites round commit `1e41928` (line 3). Protocol items not checked by me: L2 floor (12 seats; `history://W2RoundKama.*` not read).

## 9. Recommended per-axis verdicts (axes the lane scores)

| Axis | Lane self-verdict | Recommended | Basis |
|---|---|---|---|
| operability | unchanged | **unchanged** — agree | md5 identical; test RESULT 24/0; L1 live runs are not operability evidence (D-1) |
| freshness | 7→8 | **improved, narrow (7→8), provisional** | C1 count reproduces; 30 repo-local rows sampled; 20 host-state rows unverified (D-4); accept only with §13 C1 |
| depth | unchanged | **unchanged** — agree | no decision rows added; one pointer line in SKILL.md |
| coverage | 8→9 | **improved (8→9)** | C3 census clean; 3 entries on uncovered ground; fix SCORECARD axes table (D-2) |
| calibration | unchanged (score) | **unchanged score; discernment trend improved (provisional)** | §5 spot-check; no self-attested score change |
| adjacency | unchanged | **unchanged** — agree | boundary sentences present; A18 config-body read is a KQ5 slip, not a harm (D-5) |

SCORECARD axes table (head `SCORECARD.md` lines 17-24) still reads freshness "6 → 7 | … | round 2" and coverage "1 → 8 | … | round 1". The round-10 moves appear only in §Round 10 (D-2). A scorecard row without its last-change round is the contract failure AXES.md §SCORECARD contract names.

## 10. Trend verdicts (LEARNING.md)

- **Expansion: improved.** Evidence: `knowledge/` sourced entries 0→3 on uncovered ground (base coverage map has no metrics or GGUF row; base README §Known gaps says "Real-runtime reconciliation is proven for llama.cpp only"). Cited-anchor defect D-7.
- **Quality: improved.** Evidence: 50/50 ledger anchors carry an appended correction (§3); no admitted entry found false in the sampled sentences (§4–§6). Caveats: D-3, D-4 (host rows), D-6 (correction coverage ≠ staleness).
- **Discernment: improved (provisional).** Evidence: §5, agree on admits and rejects, n=7. The lane's "unchanged pending outside check" is superseded only if the orchestrator accepts this reviewer as the non-author check.

## 11. Defects by severity

**HIGH**
- **D-1 — campaign documentation-only rule breached by the kama L1 (process).** Binding text: "kagi, kasegi, kama, chousa, kake, tabi: no live-target probing, scanning, logins or submissions — documentation only." (`kama-round-10.md` §6.5, bullet 4). The L1 ran `check` (text and `--json`), `consumers`, an isolated `snapshot`, `ss -ltn` on 8080/34113, `systemctl --user show qwen-coder.service`, and `kama-probe.sh listeners` (out of scope; Mistake 25). Evidence: `corpus/lessons/round-10.md` §Contested L1 gate runs; `.ufo/round-10/gates/*.json` (7 files, `sampled_utc: 2026-10-19T21:35:49Z`); report line "Re-verification for the record only (contested, see L0)". The lane disclosed this and did not claim on it, but the outputs are committed and cited in LOG, SCORECARD §Round 10 and the report. My reading: the rule names kama and binds its own L1 gate. Recommendation: orchestrator rules; lane appends an erratum marking those outputs out-of-rule; no claim cites them. Do not delete (append-only).

**MEDIUM**
- **D-2 — SCORECARD axes table not updated** (`SCORECARD.md` lines 17-24 vs §Round 10 lines ~192-196). Fix: appended erratum or table update with last-change round 10 for freshness (8) and coverage (9).
- **D-3 — lesson's Mistake-14 count contradicts its own target.** `round-10.md` Mistakes row 14 + code block: "target 15 to 0". Measured: base 15, head 29 (§3). Count is contaminated by correction text. KQ7 is met by the ledger count (0), but the lesson presents the 15→0 count as the strongest criterion and never reports the head value. Fix: appended erratum retiring the Mistake-14 count (or redefining it to exclude correction blocks).
- **D-4 — 20 of 50 ledger rows rest on host-state reads**: A06, A16–A29, A31, A33, A35, A36, A38 (`wc -l ~/.config/opencode/…`, `test -e ~/.config/systemd/user/qwen-coder.service`, fleet-root `MISSION.md`, `~/Projects/ufo-fsd-alpha/…`). They are shape-only but not reproducible from the repo and fall under D-1. Fix: re-anchor to repo-local evidence, or mark as lane-observed and unverified.

**LOW**
- **D-5 — repeat of a captured class.** A18: the executor read 4 body lines of `~/Projects/ufo-fsd-alpha/config/l1-max-context.yml` after the lesson's own Mistake 9 (config body reads). Disclosed and reduced to `wc -l`. Not used by any admitted claim.
- **D-6 — C1 before-state is definitional.** Base count 50 = absence of the correction tag. Report's "0 MISS" (non-circular check) is the meaningful before. Label in report.
- **D-7 — mis-cited anchor.** Expansion evidence cites `corpus/README.md` §Known gaps for "llama.cpp-only evidence, and no metrics or GGUF rows" (report §Trend verdicts; lesson §Admissions). §Known gaps (base README lines 49–64) has the llama.cpp-only line but not the metrics/GGUF claim; that gap is visible only in the 19-row coverage map.
- **D-8 — quote bytes.** S009 Gate quote uses ASCII apostrophes; the live page uses U+2019 (fetched 2026-10-19). Substance identical; fix the quote bytes.
- **D-9 — append-only literalness.** Five in-place line edits outside the checked paths (§2): three newline-only rewrites (text identical) and two SCORECARD rows replaced. Disclosed in LOG. Accept as recorded exceptions.

**INFO**
- **D-10** S026 tier A is scoped to "proposal history only" (open PR). Defensible under "maintainer statement"; a stricter reading would be B. No status change needed.
- **D-11** Not verified by me: L2 floor, godspeed prefix on prompts, sentinel/critic transcripts (`history://W2RoundKama.*`).

## 12. Not verified / scope limits

- Host-state and live-endpoint checks were not re-run (documentation-only binding; D-1). Affects 20 ledger rows (D-4) and all L1 gate outputs.
- Not re-opened: S008 mapping, S014, S017, S019, S002, S006, S018, S021–S025, S011, S012, S016, S027–S029 (see §4).
- SCORECARD capability row: "census runs clean" is verified; whether the census is a capability or a coverage move is an operator ruling (L0 Q2).

## 13. Admit / reject recommendation

**ADMIT, conditional.** Scope of admission: C3 capability (`sources-registry`) with the 3 knowledge entries, coverage 8→9; C1 freshness narrow (7→8) for the 30 repo-local rows.

Conditions (appended errata; no in-place rewrites):
1. **D-1:** orchestrator/L0 rules on the documentation-only binding; the lane records the L1 gate outputs as out-of-rule and no claim cites them.
2. **D-2:** SCORECARD axes table updated with round-10 scores and last-change round.
3. **D-3:** Mistake-14 count retired or redefined; the "15 → 0" target stated as not met by that count.

Non-blocking for round 11: D-4 (re-anchor host rows), D-5 to D-9, D-10 (note only).

Recommended L0 rulings:
- **Q1 (does the documentation-only rule bind kama's own L1 gate?):** yes — the binding names kama. Round 11 may cite repo-file reads only; live checks are out of rule.
- **Q2 (SOURCES.md: capability or coverage?):** the binding (§6.4) and AXES §Capabilities accept the census run as the capability demonstration, and it ran clean in-round (§4). Accept as capability, recording the critic's coverage reading as dissent.

## Scratch

`/tmp/kaika-verify/kama/` removed after this file was written.
