# kaidoku — round 20 report (hyaku phase 2, attempt 3 — recovery)

Lane `kaidoku-shokunin`, branch `main`. Baseline `14f0260ad319ecc26994381b2415d5a999003375`; measured
verification source **`37e10c545a05cf8ede9a2da0e45d44eb13c7835f`**; final census record commit and pushed lane tip
**`4cc8a74cefb91bab7a847e20a18f4d181f43b6e3`**. Attempt 1 (`KaidokuR20`) and attempt 2 (`KaidokuR20Recovery`, Devin
weekly quota) ended before filing a report. Attempt 3 is an operator-authorized failed-coordinator recovery: it spawned
**no seat**, reused/re-verified the retained work, integrated all wave reports, and filed this report. No promotion,
mint or admission is claimed; admission belongs to the non-author closure.

## Work performed

Declared claims (`.ufo/waves/round-20/claims.json`, declared `d1d981d` before any wave):
- **C1 calibration (tied-lowest owned, 10.0):** close the eleven items routed by the round-19 outside check (D1–D6f) with
  named corrections plus revision-scoped substance checks; census FAIL/1 → PASS/0; QUALITY 22 → 23+ with rows 1–22
  byte-identical. **Verdict: improved** (numeric proxy 10.0→10.0, delta 0). Measured at V: routed items **11 → 1** (only
  D5, the final-census witness this claim's own delivery adds); at the delivered record tip `4cc8a74`: **11 → 0**, exit 0.
- **C2 coverage (owned, 10.0):** admit knowledge for five first-held REA CLI verbs with retained run evidence and mined
  sources: `inspect-wasm-artifact`, `compare-wasm-interfaces`, `execute-rizin-command`, `list-objdump-architectures`,
  `project-harmony-application-graph`. **Verdict: improved** (10.0→10.0). CLI commands named in admitted knowledge
  **128/153 → 133/153**; five targets `exercised`; README map 102/102. Bounds: mention-level coverage; the objdump list
  verb is pathless (`subject: null`); Harmony is two recipe-retained synthetic HAPs, path-hint only.
- **C3 depth (owned, 10.0):** masked-variadic v2 emulator forecasts the first Go-analysis failure for 19 go1.24.6
  toolchain ELFs, frozen and pushed at `808cbb3` before the first analyze. **Verdict: improved** (10.0→10.0). At V:
  `first_failure_bound=19`, `matched=19`, 19/19 bound receipts valid; 8 exact `Invalid index` values, 11 silent.

Frontier step: nine SOURCES rows (S040–S048), one mined mistake series (`## Mistakes` 1–17 in
`corpus/lessons/round-20.md`), census before→after, and C2/C3 sourced claims (S040–S048).

Integration work in this attempt:
- Re-read every retained wave report and re-ran the counters instead of trusting attempt-2 prose. Wave 2 found real
  defects; the reachable ones were fixed and re-measured (below). Unreachable/structural findings are named as residuals.
- Fixed and re-verified: D6d decoy (successor validator, pinned bytes preserved), D6e/no-harm wrapper regression,
  D5 record-shape closure, D2 timestamp text-size skip and grammar, D3 disarm rule, C1 `--live` scope, SKILL registry
  rows, S048 source identity, QUALITY #23–#25 narrowing, wave-outcome cause records.
- Wave integration: W1 **100 spawned / 98 reports**, W2 **71 spawned / 71 reports** = **169 delivered**, **2 missing**
  (`ConnSiblingHarmony`, `ConnJjSelftests`), **171 spent**. No seat was respawned or replaced. The two missing seats are
  terminal `session_exit` reason `dispose` at 2026-10-20T21:29:58Z (cancelled after 50 / 25 requests with a pending tool
  call); their raw transcript paths and the `cause unknown`-style record are in
  `.ufo/waves/round-20/evidence/wave-outcomes/w1-causes.json`; outcomes read `seats=100 reports=98 missing=2 uncaused=0`,
  exit 0. W2 outcomes read `seats=71 reports=71 missing=0`, exit 0.
- Reused after re-verification: attempt-1 commits `d1d981d`…`aad0869`, W1 reports and C2/C3 evidence, W2 reports,
  `verify/recovery/*`. Discarded: attempt-2 prose treating D1–D6f as closed before the D5 record existed; the in-run
  `runs/*/compare.json` records (Mistake 6; superseded by the frozen-comparator rerun); the routed-r19 blob at `7a1e0df`.

## Landed changes

Every change is tied to `LOG.md` “2026-10-20 — round-20 …” (line 2289) and its attempt-3 continuation, and carried by a
lane commit (`kaidoku-shokunin <kaidoku@shokunin.local>`):

| Commit | Change |
|---|---|
| `d1d981d` | claims C1–C3, seat contract, wave-1 spec; carrier exec bits cleared |
| `808cbb3` | W1 tool integration; C3 v2 predictions frozen (19 labels, link excluded) and pushed before any analyze |
| `8451e47` | C2 knowledge entries, SOURCES S040–S047, QUALITY 23–25, lesson, registry rows |
| `fe23112` | verb-coverage evidence binding and objdump op alias |
| `aad0869` | C3 runs (19 go1.24.6 labels), per-label guard checks, frozen-comparator rerun 19/19, receipt validation |
| `aa78b0d`, `7a1e0df` | attempt-1 checkpoints: retained tools/patches/corpus (admission pending) |
| `81c2021` | attempt-2 recovery: RoutedR19Fix counter patch, revexec work base/private tmp/host-home, D5 shape, SCORECARD/LOG rows |
| `5c0b46c` | guard checks + disarm (modes restored), D3 disarm rule, W2 generator |
| `a65bb98` | attempt-3 integration: W2 reports/JSONs/verify, wave outcomes, D5/D6d/D6e/D2 fixes, S048 + entry errata, QUALITY/SKILL corrections |
| `3e9fbf5` | pin-safe D6d successor (`receipt-validate-v2.py`), D6d decoy+control check, timestamp allow/cutoff corrections |
| `37e10c5` | D6d positive control from a retained validated receipt |
| `106fe31` | measured records, receipts under `verify/round20/`, SCORECARD/LOG measured sections |
| `4cc8a74` | final-census record (adds only `verify/final-census.json` and `.stdout`) |

No lane file outside this round's work and corpus/SKILL/SCORECARD/LOG was edited; no sibling repo, config, route,
MANIFEST, operator file or fleet script was touched. No install or update occurred in this attempt (WABT 1.0.42 was
installed earlier in the round, recorded in `corpus/lessons/round-20.md` §Installs).

## Before → after measurements

Environment: `L=/home/vgpnk/Projects/shokunin/kaidoku-shokunin`, `V=37e10c545a05cf8ede9a2da0e45d44eb13c7835f`,
`C=4cc8a74cefb91bab7a847e20a18f4d181f43b6e3`, `B=14f0260ad319ecc26994381b2415d5a999003375`.

1. **C1 — routed items.** `python3 -I -B .ufo/waves/round-20/tools/routed-r19.py --root "$L" --rev V --strict --live`
   → exit 1, `open_count=1` (D5 only; all other ten name+substance true). At the record tip:
   `… --rev C --strict --live` → **exit 0, open_count=0** (D1–D6f all true). Baseline red at B is retained from wave 1
   (`open_count=11`). Census: `python3 -I -B .ufo/gates/c1-census-v10.py --root "$L"` → exit 0,
   `VERDICT: PASS (stale=0 ambiguous=0 undeclared=0 unresolved=0)`. Controls: `controls-r20.py B C` → exit 0,
   `pass: true`, `failed: []`.
2. **C2 — verb coverage.** `python3 -I -B .ufo/waves/round-20/tools/verb-coverage.py --root "$L" --rev V` → exit 0,
   `mentioned=133` of `cli_commands=153`, targets `inspect-wasm-artifact=true, compare-wasm-interfaces=true,
   execute-rizin-command=true, list-objdump-architectures=true, project-harmony-application-graph=true`. Base `B` was
   128/153 with 0/5 exercised (w1 `RerunVerbB`, retained).
3. **C3 — first-failure.** `python3 -I -B .ufo/waves/round-20/measure.py V --freeze
   808cbb31a1e24656da5ba4967497e602fbca7415` → exit 0, `c3.first_failure_bound=19`, `matched=19`,
   raw `receipt_valid=19 receipt_invalid_or_unusable=0`, `compare_records=19 compare_matched_records=19`,
   `freeze_equal_predictions=19`. Freeze committer time 18:01:54 -03; first run 18:02:05 -03 (after the push).
4. **No-harm / evidence.** `evidence-timestamps.py --root "$L" --rev V --path .ufo/waves/round-20 --strict
   --allow w2/AttackD2.md:6` → exit 0 (975 text files scanned, 15 binary blobs reported as skipped, one applied allow);
   at C the same command additionally allows `verify/round20/timestamps.json:1` (the tool’s own receipt quotes the same
   2030 fixture literal) → exit 0, `unexempted_finding_count=0`. Without allows the only findings are those two 2030
   fixture literals; no lane claim carries them. Append-only prefixes and prior runs/predictions hold (`controls-r20`).
5. **Final census record.** `final-census.py --root "$L" --out-dir "$L/.ufo/waves/round-20/verify"` at the measured tip
   `106fe31` → exit 0, `worktree_clean=true`, `stdout_sha256=224032edd344bc000d1346ee8b66f1a88b01d2e4adf5079cca68d8c24d9e84f4`;
   the transcript carries `VERDICT: PASS` and the `kaidoku ok` source-census marker. The record commit `4cc8a74` adds
   only the record and transcript; `routed-r19` D5 validates the parent/argv/markers/two-path diff at that commit.

## Sources & frontier

Census command: `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kaidoku`
→ **exit 0** at the delivered tip (W04 only for S033 and S047, both carried duplicate-URL scopes).
- Rows **39 → 48** (nine added: S040–S048); tiers **A 42, B 5, C 1** at the tip; status **mined 46, rejected 2**.
- Added by tier: eight tier-A (S040–S043, S045–S048) and one tier-B (S044). S048 is the installed non-Harmony REA
  CLI/service source added in recovery; S040 stays Harmony-only and its used-by cell is unchanged.
- Rows touched old→new: S003/S023/S035 gained the C3 entry in `used-by` (append-only suffixes); the rest of their cells
  are byte-prefixes. No status or recheck cell changed; no row rewritten.
- Frontier rows advanced: none. C2 enters operation ground for five verbs, not a coverage-map (F1–F10) row; README map
  integrity 97/97 → 102/102.
- Opened sources and located quotes are in `corpus/lessons/round-20.md` `## Gate`; wave-2 reopens found S041/S045/S046
  quotes are rendered text (not byte-contiguous raw HTML/Markdown) and S043’s `-c` anchors are incomplete — corrections
  are appended in the lesson, not rewritten. S048’s quote is in the Gate addendum.

## Trend verdicts

- **Expansion: improved.** Nine new mined source rows and five first-held verb entries on ground the corpus did not
  hold; every new entry cites mined rows (S040–S048); the coverage map gained the new entries with no loss.
- **Quality: improved, bounded.** Stronger anchors supersede weaker ones (S078-style corrections, QUALITY #23–#25),
  wave-2 defects were repaired with red/green or retained fixtures, and the strict C3/receipt bindings re-verify; the
  bounded residuals (separability, pathless subject, exact-artifact holdout, token-level verb evidence) are named below.
- **Discernment: improved.** The wave-2 attacks falsified parts of the round’s own claims (D6d decoy, D6e no-harm
  regression, missing D5 witness, S040 mis-scope, registry rows, wave outcomes); each produced a named correction with
  a check that can fail. The independent outside admit/reject sample remains the closure’s duty, not self-attested.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — lane assertion, `SKILL.md:81-314`, `SCORECARD.md` command A; no promotion verifier.
- [~] At least one end-to-end domain task executed and logged in LOG.md — lane assertion, 2026-10-15 libjq run and round-20 five-verb runs; complete record at `evidence/round-1-2026-10-15/rea-bundle.json` and `evidence/c2/`; no outside verifier.
- [~] Instructions executable by an agent without oral context — lane assertion, historical round-1 recipe plus the round-20 counting commands; no current outside audit.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — lane assertion, `PROVINCE.md:88-116`; revenger-shokunin’s PROVINCE still claims the REA toolset (adjacency note, reported not absorbed).

## Waves, cancellations, conformance

- W1: 100 spawn seats — executor 28, scout 22, reviewer 16, scribe 10, connector 8, critic 8, revenger 4, sentinel 2,
  simplifier 2; 98 reports. First dispatch refused 100 by the 100-job cap and spawned none; the identical retry spawned
  100. Two seats missing with retained causes (above); no replacement. `RoutedR19Fix` is a resumed `RoutedR19Tool-2`
  turn, not a separate seat.
- W2: 71 spawn seats — reviewer 27, scout 16, critic 14, executor 5, mutation-tester 4, connector 2, sentinel 2, scribe 1;
  71 reports, no dead seat. Attempts 1 and 2 were refused 71/71 by the job cap and spawned none; the third identical
  payload spawned 71. Total 171; attempt 3 added 0; residual seats used: **0** (≤8 allowance unused).
- Planner seat: the L1 holds the canonical §3 planner seat; bounded planning/data-walk rode scouts/connectors/revengers.
- Provider/coordinator failures: attempt 1 ended before its report on provider 429/quota/cyber errors; attempt 2 ended on
  the Devin weekly quota; attempt 3 ran with automatic fallbacks only. No dead seat was respawned.
- REA work was CLI-only (`npx -y rea-agents@6.5.0`); no `xd://mcp__rea_*` device was used. No live secrets or private
  config were read into evidence; no host/package/service/compositor mutation was performed.
- Stale-lane: respawn-per-round driver; this is attempt 3 of the same round-20 mission, no next round started and no
  other kaidoku mission is open.
- Misroot sweep: `git -C /home/vgpnk/Projects/shokunin status --porcelain` shows only `.ufo/watchdog.log`, driver
  `.ufo/state/*.report-baseline`, and another lane’s untracked `.ufo/waves/round-38/`; no file written by a kaidoku seat
  was found at the fleet root.

## Named residuals (not closed by prose)

C1/C3 share the receipt validator as a verification authority (claim separability, w2 `CriticSeparabilityS.md`); D6a’s
duplicate-name nested-read limitation; D6b exposes a read-only host HOME (including `.ssh` names) under `--host-home`;
QUALITY #23 still skips binary blobs (15 reported and reviewed as binary); QUALITY #25 remains a token check, not receipt
authentication; census DATED shelter and same-line laundering; carrier-guard covers direct `execve` only (loader-mapped,
copy+exec, memfd, same-owner chmod are bypasses); C3 is exact-artifact outcome-held-out, comparator checks kind+index
only, `t1246-link` excluded, `t1246-objdump` ended on a later Java heap OOM, and the predicate/vacuity limits are in
`## Open`; C2’s pathless objdump target is not carrier-bound and Harmony is synthetic path-hint only; S041/S045/S046
quotes are rendered text and S043’s `-c` anchors remain unadded; the two 2030 fixture literals require the documented
timestamp allows.

## Round-21 author erratum — recovery failure chronology and review boundary

Appended by KaidokuR21 under Main's explicit authorization on 2026-10-21; the filed round-20 bytes above are preserved.

This corrects the incomplete attempt-2 account in the opening paragraph and **Waves, cancellations, conformance**: Main recovered an actual Codex `cyber_policy` flag for `KaidokuR20Recovery` at **2026-10-21T07:34:34Z**, before the Devin quota error at **07:34:36Z**. Attempt 2 therefore did not have a quota-only failure. The quota observation neither erases nor resolves the safety flag; provider retry/fallback is not safety authorization. This erratum does not reproduce or replay the historically flagged request.

Main commissioned independent scope-only review by **ScopeKaidokuFlag**. Main's resulting instruction reports that inspection of the reviewed prompts/report and pre-flag retained JSON/TOON found no exploitation, vulnerability reproduction, intrusion, or offensive request in that inspected material. This is a bounded scope assessment, not proof about every unreviewed historical action and not a retroactive rewrite of the flag or round-20 closure.

Main expressly permits only the current round-21 C1/C2 offline receipt/schema/observation-envelope validation with synthetic fixtures, already-retained static evidence, public documentation and owned validators. It does not authorize replaying/rerouting the historically flagged request, executing analyzed carriers or live provider targets, or using `--host-home` paths. No sandbox, security-containment or cryptographic-authentication claim follows from revexec, a receipt, or a carrier guard. Round-21 wave dispatch remains separately subject to Main's counter-gate prerequisite.

Evidence authority: Main's safety-hold and subsequent scope-review messages to **KaidokuR21**, naming **ScopeKaidokuFlag**, the two recovered event timestamps, and this explicit append-only correction permission. This author performed no new target execution to confirm either event.
