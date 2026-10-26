# kasegi — round 33 report (attempt 1, L1 KasegiR33)

Lane repo `/home/vgpnk/Projects/shokunin/kasegi-shokunin`, branch `master`, claim base `690b69dae23ab9f4ccf056ba2d619cadc2abb3c4`, lane HEAD `7963976e60b2564860553c6ab4838128d5ca06ea` (pushed; `jj-lane.sh state`: local = remote, ahead 0, untracked 0; `git ls-remote origin refs/heads/master` prints the same hash).

## Work performed

The round declared two claims (frozen in `.ufo/waves/round-33/claims.json`, claims-freeze commit `6e55c8d`):

- **C1 (depth:verifiability, lowest non-retired axis, score 4 held, measured):** committed `corpus/instruments/capture-binding-check.py` binds every capture-manifest record to its registry row URL and to fetch provenance (`fetched_utc` for round-32+ captures, declared `archival` for the 38 legacy records). Surface: `corpus/source-snapshots/*/manifest.json` (all 9 snapshot dirs), `corpus/SOURCES.md` registry row URLs, the new round-32 manifest (created this round — routed defect D5), and the new capability row. Counter: `python3 corpus/instruments/capture-binding-check.py` → `records=40 bound=40 unbound=0`, exit 0, twice byte-identical; `--selftest` cases=11 failures=0.
- **C2 (coverage, score 7 held, measured, sourced):** Frontier F16 admitted 15 → 16 — Chinese crowdsourced-testing platform scope and reward rules (CNVD 众测 helpList → row S049; 360SRC 外部漏洞处理和评分标准 V2.0 → row S050) — entry `corpus/knowledge/chinese-crowdsourced-testing-scope-and-rewards.md`, registry rows 48 → 50.

**Rule-B erratum 1** (`53bfa59`, filed before any seat scored; `RevClaimsFreeze.md` rules it a permissible interface clarification — the frozen global-URL reading was unreachable on immutable R8 rows S024/S029 and S006/S028): Rule B binds each record to its own id row, byte-exact URL equality, `no-row`/`url-mismatch`/`dup-id` failures, shared-URL rows informational (`multi_row_url=2`).

**Wave:** one v2 wave `kasegi-r33-build`, 64 seats (`wave1-spec.json`), dispatched via the inline spawn handoff (`wave1.ready` → orchestrator; `wave1-dispatch.json` schema `ufo-swarm-wave-dispatch-v1`). 64/64 seats settled, 0 dead (`wave1-results.json`; `wc -l` = 64, no dead/failed rows). Declared roles: executor 19, reviewer 12, scribe 10, mutation-tester 7, scout 5, critic 5, connector 3, sentinel 2, simplifier 1. Attack share 26/64 = 40.6%; m_flash share 37/64 = 57.8%. All seats logged `Installs: none`.

**Routed round-32 verifier defects** (D1–D6): D1 closed (round-32 LOG entry appended at the freeze commit); D2 closed (frontier step runs this round: lesson, mistakes, census before/after); D3 closed (this report's cross-domain line below); D4 closed (watchdog digest committed — `.ufo/waves/round-33/watchdog-digest.txt`, sha256 recorded; the report cites only committed evidence); D5 closed (round-32 manifest created inside C1, `fetched_utc` = capture commit author time `2026-10-25T23:14:00-03:00`); D6 closed (quarantine S037 spliced-quote verdict in the lesson Gate: refused; the contiguous field string in the live standard differs).

**Frontier step:** census before → after; lesson `corpus/lessons/round-33.md` with Gate (2 admits by document = S034→S049, S035→S050 URL byte-equal; 7 rejects; 7-row quarantine slice verdicts) and Mistakes M33-1 (round-32 captures committed without manifest → new QUALITY R20, closed by C1, closure able-to-fail proven by ExecErratumCheck red/green) and M33-2 (round-32 dispatcher-log misquote → committed watchdog digest); a sourced claim (C2); considerthese proposal 1 mined (committed wave-evidence growth measured in `ExecGrowthMeasurement.md`).

**Assimilation:** theme = Chinese crowdsourced-testing platform scope and reward rules (staged S034 → lane S049, S035 → lane S050, by document). Id-collision guard: `reg-ids` 48, `staged-ids` 5, collisions S031–S048 = 18 (staged numbers), guard proof in `assimilation/guard-proof.txt` (0-3-space indented-row pattern discriminates). Quarantine slice verdicts (7 rows) recorded in the lesson Gate.

## Landed changes

Every commit is pushed (`jj-lane.sh` printed `landed <hash>` for each).

| Commit | What | LOG.md entry |
|---|---|---|
| `6e55c8d` | claims freeze C1/C2 + do-nothing controls, census-before, assimilation guard, watchdog digest, LOG round-32 entry (D1) | Round 33 (LOG.md, last entry) |
| `a6a5023` | wave-1 spec (64 seats, v2 policy), validated plan + dispatch | same |
| `53bfa59` | dispatcher ready marker; C1 erratum 1; l1-ref sid-url table | same |
| `9f98488` | wave-1 integration: `capture-binding-check.py`, all-manifest binding, round-32 manifest, F16 entry, SOURCES S049/S050 rows, README F16 row, skill/province/quality/instruments/expected-list updates, wave receipts | same |
| `5b7a039` | closure: SCORECARD round-33 section + capability row, SHONEN refresh, lesson (placeholders filled), LOG round-33 entry, `wave1-results.json`, final receipts | same |
| `7963976e` | remaining wave-1 receipts (final 12 seats) | same |

Production files: `corpus/instruments/capture-binding-check.py` (new), `corpus/source-snapshots/round-32/manifest.json` (new), `corpus/knowledge/chinese-crowdsourced-testing-scope-and-rewards.md` (new), `corpus/SOURCES.md` (+S049/S050 rows, Search log note, R8 lines), `corpus/README.md` (frontier F16 row + r33 amendment), `PROVINCE.md` (frontier line), `SKILL.md` (registry row), `corpus/QUALITY.md` (R20/R21), `corpus/instruments/README.md`, `corpus/instruments/knowledge-expected.txt` (44 → 45), 8 legacy manifests (+url/archival), `SCORECARD.md`, `SHONEN.md`, `corpus/lessons/round-33.md`, `LOG.md`.

## Before → after measurements

- **C1.** Counting command: `cd /home/vgpnk/Projects/shokunin/kasegi-shokunin && python3 corpus/instruments/capture-binding-check.py`.
  - Before at base `690b69da` (`c1-controls/before.txt`): instrument absent (`ls_exit=2`); manifest audit `TOTAL records=38 with_url=0 with_fetched_utc=0`; round-32 dir holds `S049.txt`/`S050.txt` with no manifest; `source-recheck` on the absent manifest `recheck_exit=2`; fake checker prints `records=38 bound=38 unbound=0` exit 0 with no validation (kill-rule clause).
  - After at tip `7963976e`: `records=40 bound=40 unbound=0`, `binding_exit=0`, two runs byte-identical (stdout sha256 `1861fec8…`); per-manifest audit `AUDIT records=40 with_url=40 with_fetched_utc=2 with_archival=38 snapshot_dirs=9 manifest_dirs=9 missing_manifest=0 multi_row_url=2`; `--selftest` cases=11 failures=0 exit 0; mutant set all killed (`MutCtrUnbound/UrlMismatch/FetchMissing/SelftestSkip`, `MutManifestLegacy`, `MutLegacyManifestDrop` all report killed); fake checker rejected on base bytes (real checker `records=38 bound=0 unbound=38` exit 1). Capability `capture-binding-check` enters the SCORECARD table (round-33 section).
- **C2.** Counting commands in `claims.json` C2 (cmd1–cmd9), run verbatim in `ExecHarnessC2.md`.
  - Before: frontier 15; entries citing S049/S050 = 0/0; rows 0/0; total rows 48; census exit 0 (W04 S028/S029 only); harness entries=18 pass=18; recheck exit 2.
  - After: frontier =16; entries citing =1/1; rows =1/1; registry =50; census exit 0 with exactly `W04 S028`, `W04 S029`, `ok`; harness `PASS F16 knowledge/chinese-crowdsourced-testing-scope-and-rewards.md ids=S049,S050 exit=0`, entries=19 pass=19 exit=0; source-recheck S049 (Q1–Q8) and S050 (Q1–Q6) all `occurrences=1`, `sha256 OK`, exits 0. Entry Q1–Q10 all pass under non-author reviewer (`RevEntryF16.md` verdict `ADMIT`); `RevTranslation.md` verifies the Chinese renderings map to capture text; `CritExpansion.md` verdict `new-ground` (sweep zeros for CNVD/360SRC/众测/zc.cnvd.org.cn/security.360.cn).
- **No-harm.** `ExecNoHarmFinal.md` + `RevNoHarm.md`: SKILL.md append-only (19 insertions, 0 deletions), PROVINCE.md append-only (2 insertions, 0 deletions), density mean 191.5 → 201.7 (25 blocks, 710 cites; disclosed, no score move claimed), anchorcheck failure classes unchanged (0 bad, LOST-RECORDED=306, PIN-BROKEN=0, ORIGIN=0, OUTSIDE-BASE=0, BASE-ABSENT=0; in-range 7 → 12 because the round-33 SKILL append adds five resolvable anchors — deviation D-R33-1, documented in `ExecRegressionC1.md`). resolve.py lane rate matches the committed census figures.

**Author verdicts (the operator rules):**

- **C1: target met.** 40/40/0 with all mutants killed, fake rejected, selftest 11/11; D5 closed. The frozen kill rule's parenthetical global-URL reading is superseded by erratum 1 (id-scoped), disclosed in the SCORECARD section and the lesson.
- **C2: target met.** All nine counters hit; Q1–Q10 ADMIT on the entry; expansion `new-ground`; live drift re-open (ScoutLiveDrift): S049/S050 fresh fetches byte-identical to the committed captures (diff -u empty), bounding the source-recheck evidence.

## Sources & frontier

Census command: `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kasegi`.

- Round start: exit 0, last line `kasegi ok …/corpus/SOURCES.md`, W04 S028/S029 only (`.ufo/waves/round-33/census-before.txt`).
- Round end: exit 0, same last line, same W04 pair only, 0 errors (`.ufo/waves/round-33/wave1/ExecCensusAfter.md`).
- Rows: 48 → 50. Both added tier A: S049 (CNVD 众测 helpList, `https://zc.cnvd.org.cn/news/helpList`), S050 (360SRC 外部漏洞处理和评分标准 V2.0, `https://security.360.cn/Reward/rules`), both `mined`, opened 2026-10-26, used-by the F16 entry.
- Registry changes (old → new): S049, S050 absent → `mined`. No existing row changed (R8). Six contract census commands clean (rows 50, malformed 0, enum 0, dups 0, missing used-by 0).

**Gate** (URL, access date 2026-10-26 and ≤25-word located quotes for each row in `corpus/lessons/round-33.md` `## Gate`). Admits: F16/S049 with 「众测平台仅接收客户授权测试范围内的安全漏洞，不接受互联网漏洞。」 (S049.txt:214) and 「测试项目范围以外的系统不在客户的授权范围内」 (S049.txt:410); F16/S050 with 「本标准适用于 360 集团发布的产品和业务」 (S050.txt:69) and 「未纳入安全服务的资产一般情况下不收录相关漏洞」 (S050.txt:591). Rejects: 7 staged/standing entries with flip conditions, re-confirmed.

**Sourced claim:** C2 rests on S049/S050 (first registered this round; quotes verified exactly-once by source-recheck and by RevQuoteSweep).

**Mistakes mined** (`corpus/lessons/round-33.md` `## Mistakes`): M33-1 (round-32 captures committed without manifest; class landing/reference-drift; captured-by none → new QUALITY R20; fix = C1 instrument + manifest, shown able to fail) and M33-2 (round-32 report misquoted dispatcher log; fix = committed watchdog digest).

Frontier advanced: F16 admitted (15 → 16), entry `chinese-crowdsourced-testing-scope-and-rewards.md`.

## Trend verdicts

- **expansion: `improved`.** F16 is new ground (sweep zeros; CritExpansion `new-ground`); the `capture-binding-check` capability enters the table. One new knowledge entry, two new tier-A rows, two new QUALITY criteria (R20/R21).
- **quality: `improved`.** C1 instruments a real prevention surface (manifest binding) with a selftest and killed mutants; strict recheck audit 44/44 → 45/45; harness 18/18 → 19/19; source-recheck now passes on the round-32 manifest (was exit 2); density rose with no harm.
- **discernment: `improved`.** In favour: the Rule-B erratum was filed before any seat scored and is independently certified as an interface clarification (RevClaimsFreeze); three independent seats flagged the same registry-URL tension; the fake checker is rejected by the kill rule; quarantine verdicts are located; Refusals re-confirmed; a drift re-open of both sources is byte-identical.
  Against: ScribeScorecard's wave-time receipt initially recorded 54 receipts (the L1's post-WAVE-DONE commit brings the wave evidence to 64/64); one deviation (D-R33-1: anchor in-range count 7 → 12) was disclosed unrounded rather than restated.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — `SHONEN.md:4-5`. This round adds the capture-binding-check registry row (`SKILL.md`, `9f98488`). No non-author replay.
- [~] At least one end-to-end domain task executed and logged in LOG.md — `SHONEN.md:6-7`. Round-33 LOG entry. No non-author replay.
- [~] Instructions executable by an agent without oral context — `SHONEN.md:8-9`. Evidence: recheck-audit strict pass=45/45, frontier harness entries=19 pass=19, source-recheck S049/S050 exit 0 (all re-run by the L1 at tip `7963976e`).
- [~] No cross-domain bleed (PROVINCE.md still accurate) — `SHONEN.md:10-12`. F16 append-only line; sibling sweep (ConnSibling) found zero CNVD/360SRC/众测 hits across six sibling lanes; nothing absorbed.

**Cross-domain evidence (routed D3):** none beyond reported adjacency — F16 stays inside kasegi's province; no sibling holds the ground; no live bounty target was contacted; no credential material is reproduced (the CNVD help page's platform-issued VPN instructions appear in no new file; `SentCred.md` sweep clean).

Stale-lane: respawn-per-round driver; no other mission of this lane is open.

Tool installs: none (every seat reported `Installs: none`; no pacman transaction attempted under the paused-host rule).

Open L0 questions: the kasegi round-32 L0 row (`kasegi | round-32 | ruling wanted: re-dispatch vs L1-only landing`) remains open at the fleet; this round routed around it by re-dispatching the round-32 claims as round-33 claims — the operator's ruling on the round-32 row is still owed.
