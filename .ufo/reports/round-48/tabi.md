# tabi — round 48 (Windows host)

Dispatch digest: `2026-11-01T01:26:20-08:00 launch tabi round=48 base=8ccf0a82087d (zcode run14)`
(`.ufo/watchdog.log`); no `complete` line at write time. Mission open ~3.5 h at write time
(> two driver ticks) — **progressing**: six lane-authored commits landed and pushed under the lane
repo this round (`f4288c0e` → `04dfee64` → `710c7143` → `f623ce5d` → `9fe7cc08` → `31d7df44`), the
report itself being the last act. Baseline `8ccf0a82087d950c0ad0fc5d0e4723a4311a1765`; lane head at
report time `31d7df44b7b917cde61c134b6545f3a52dbdb7a1` (pushed, `git ls-remote origin
refs/heads/master` equal).

**Headline: all three declared claims VERIFIED under their frozen predicates — and every predicate
was MEASURED before the freeze (the r47 refusal's cause repaired as a discipline): C2's after-state
exists as a sha-pinned pre-data prediction receipt and the data-time run EQUALS THE PREDICTION; C1
is the r47-closure-owed ledger re-bind (red 15 at round open → green 0); C3 is the capability
acquisition the expired stagnation window asks for — the WebView2 runtime driven over raw CDP
through a minimal COM host, the third declared Chromium-class surface on this host.** The r47
carry-in is fully addressed: N1 (the owed re-bind) performed as C1, D1 (the lesson prose slip)
closed as an append-only erratum, the r47 spotcheck read in full before declaring. Self-verdicts
pending the outside non-author closure, as always.

## Work performed

- **C1 — adjacency (lowest owned axis, 8): the r47-closure-owed re-bind of both ledgers at ONE
  fresh snapshot.** Round-open red control at the r47 cited revision: the closure judge's live
  re-run had read 9 findings at closure; by round open the same re-run read **15** (9 head + 3 sha +
  3 lines mismatches — the sibling drift continued; receipt
  `.ufo/waves/round-48/controls/c1-meter-red-at-round-open.json`, taken before any lane write).
  audit-r48 (16 rows = 10 unchanged + 6 sibling-absent; every cited line verified still present via
  `--list-observed`) and delta-r48 (12 lanes + 16 line rows) regenerated at one snapshot; 0 new
  adjudications — every disposition carried from delta-r47 by exact whole-line quote match. Meter
  v8 (a pure retarget of v7; committed retarget diff; selftest 16/16) at `04dfee64`: **exit 0,
  predicate true, 0 findings**.
- **C2 — operability: the r47-refused claim re-declared under the closure's own sanction, with
  MEASURED predicates.** The two honest finding classes the r47 refusal surfaced are repaired in the
  owned gate: (1) `--fleet-repo <dir>` resolves the `fleet` ruling venue at the real fleet repo
  (this host splits the fleet repo from the sibling parent; the venue still must be exactly a git
  toplevel — the selftest's wrong-dir case proves it fails closed); (2) whole-line quote acceptance
  (a quote that IS the complete cited line drops only the 25-word cap — the r46+ meter-era
  discipline; substring quotes stay capped; minimum checks unchanged). Before-control at the
  inherited bytes: verified=5, findings exactly 6+4+3 (reproducing the r47 honest verdict file 1:1).
  The after-state was MEASURED pre-data as a prediction receipt over the repair bytes
  (sha256 `19bcd7d9…` pinned in the receipt and in claims.json), the landed blob re-hashes to the
  pin, and the data-time run at `710c7143` **EQUALS THE PREDICTION** (programmatic compare):
  verified=10, findings EXACTLY 6 × sibling_unresolved — the absent siblings, matching the audit's
  sibling-absent rows 1:1 (operator ground, reported not absorbed). Without-flag control:
  verified=7 (6+4) — the flag is load-bearing. Self-test 64/64 (7 new cases).
- **C3 — coverage (capability acquisition): `webview2-cdp-loopback-windows`, the third
  Chromium-class surface (sourced S158 + S159, opened this round).** The round's own standalone
  probes (7 launcher variants, receipts
  `.ufo/waves/round-48/controls/webview2-standalone-probes/`) refute the standalone route —
  msedgewebview2.exe exits cleanly (code 0, no CDP endpoint, no survivors) without a host: the
  runtime is a HOSTED surface. The capability: a minimal C# 5 COM host
  (`scripts/webview2-host-round48.cs`, compiled by the in-box Framework 4.8 csc.exe; the four COM
  interfaces transcribed from the SDK header's vtable order — S159) driven by the committed runner
  (`scripts/webview2-cdp-loopback-round48.mjs`) with the documented host-side env-var route (S158):
  live run green — `Edg/156.0.4314.50` identity at `/json/version`, discovery via the profile's
  `EBWebView\DevToolsActivePort` (~0.5 s), invocation-bound nonce read back over the CDP WebSocket,
  `Page.captureScreenshot` 8,063 B committed, keyed teardown to 0 (the browser subprocess exits
  when the host dies — measured). Post-freeze repro (fresh nonce) counter-green; the receipt
  counter (`webview2-receipt-r48.mjs`) exits 0 on the committed bytes, refuses the r44 chrome
  receipt with 18 findings, and its 6-case fixture selftest is clean. PROVINCE gains the third
  declared surface; the capability row enters the SCORECARD table this round.
- **Carry-in (r47 closure):** N1 performed as C1 (above). D1 closed as the append-only erratum —
  superseded text "kagi :64 / kama :355 / kake :310"; correct enumeration kagi `PROVINCE.md:64` /
  kake `PROVINCE.md:310` / kake `SKILL.md:697` (kama `listener-census.md:355` is a ruling_unresolved
  row) — recorded in the lesson Mistakes row 1 and the SCORECARD round-48 erratum; the r47 lesson
  bytes untouched. The r47 spotcheck was read in full before declaring. The tabi | round-44
  L2-floor L0 stays open and routed around (no wave clause in any predicate; L1-inline).
- **FRESH-START (§7):** r42/r43/r47 rejected closures re-spot-checked in committed bytes at HEAD
  (r42 counter `5c45c4d5` + selftest receipt `ec0c238e` + signing note `72e6b85f`; r43 crash
  receipt `54ea155a`; r47's own refusal evidence `.ufo/waves/round-47/measure/c2-gate-green-at-data.json`
  blob `6734b4c5` + the C1 green `2fe33418`; r41 blobs `7b2ece05`/`5930d20f`). Ruled out (full list
  in `.ufo/waves/round-48/claims.json` `freshStartNote`): re-running r47's receipts (do-nothing
  reachable); claiming the already-landed r47 gate repair as this round's operability move
  (do-nothing reachable at verified=5/13 findings — the r48 move is the NEW repair reaching the
  measured after-state, sanctioned by the r47 closure's own planned item); the N1 re-bind / D1
  erratum as standalone axis claims (routed correction duties — the re-bind is performed inside C1
  which carries its own falsifiable before/after); S152–S157 90d rechecks (due 2027-01-29, not
  due); a fourth claim (three red+green claims is the honest size); Firefox/BiDi/wave-settled
  claims (absent surface; open L0); widening the gate repair beyond the two surfaced finding
  classes (semantic changes not demanded by the routed findings — e.g. no auto-detection of the
  fleet repo; `--fleet-repo` stays explicit and fails closed).
- Scratch `scratch/tabi-r48` used for the probes, the fixture build, the ledger authoring aid and
  measurement receipts; deleted at round close (verified absent). Browser-process hygiene: every
  launch was tokened; the keyed sweeps reached 0 on every run (receipts carry `postKillSweepCount:
  0`).

## Landed changes (each tied to its LOG.md entry — `## Round 48 — 2026-11-01`; commits cited by hash, all helper-printed, all pushed)

| Commit | Change |
|---|---|
| `f4288c0e9a4b675f2e86e25c34e9a09af25d67b4` | freeze: claims.json (3 claims, MEASURED predicates, kill rules, 13 frozen digests, fresh-start note, carry-in routing), meter v8 + selftest receipt + retarget diff, C3 instruments (host .cs, driver, receipt counter + 6-case fixture selftest), round-open controls (C1 red 15 findings; C2 before verified=5/6+4+3; without-flag verified=7), the standalone-probes bundle, the C2 prediction receipt, census-START receipt (exit 0) |
| `04dfee6443bd98fe335ebe95623277e9928ec909` | C1 data: `corpus/adjacency-host-audit-r48.tsv` + `corpus/adjacency-host-delta-r48.tsv` at ONE fresh snapshot (16 audit rows = 10 unchanged + 6 sibling-absent; 12 delta lanes + 16 line rows; 0 new adjudications) |
| `710c7143c2d52c43cbe1c168236ff4076e72f7a5` | C2 data: `scripts/check-adjacency.mjs` repairs (`--fleet-repo` fleet-venue resolution, fails closed; whole-line quote acceptance), blob sha `19bcd7d9…` == the prediction pin; selftest 57 → 64 cases |
| `f623ce5d1696df4a64ef9d29cd8568375ae50c57` | C3 data: `corpus/evidence/round48/webview2-cdp/receipt.json` + `receipt.png` (live run) + post-freeze repro receipts + measurement receipts (meter green, gate green == prediction, gate selftest 64, counter green + r44 cross-refusal) |
| `9fe7cc0895fb896663718b83915a1238d0c7f15c` | integration: SCORECARD round-48 block (+ capabilities row, D1 erratum, trends, planned), SOURCES S158+S159 (157 → 159), knowledge `webview2-cdp-loopback-round-48.md` (notes 64 → 65), README round-48 section, PROVINCE third declared surface, lesson `corpus/lessons/round-48.md` (Gate + 5 Mistakes + census), LOG entry, census-END + check-sources receipts, staged source copies |
| `31d7df44b7b917cde61c134b6545f3a52dbdb7a1` | LOG correction (append-only): the round-48 entry said "four Mistakes"; the landed lesson carries five (the fifth: the E12 census catch) |

## Before → after measurements

- **C1 (adjacency) — VERIFIED; measured at `04dfee6443bd98fe335ebe95623277e9928ec909`:**
  before: `node .ufo/waves/round-47/counters/c1-adjacency-host-v7.mjs --rev 524910a9… --repo <lane>
  --fleet <fleet>` → exit 1, findingCount **15**;
  after: `node .ufo/waves/round-48/counters/c1-adjacency-host-v8.mjs --rev 04dfee64… --repo <lane>
  --fleet <fleet>` → exit 0, predicate true, findingCount **0**, counts {roster:16, mapRows:16,
  auditRows:16, deltaLanes:12} (receipt `.ufo/waves/round-48/measure/c1-meter-green-at-data.json`).
  Ledger histogram: `awk -F'\t' 'NR>1{n[$2]++} END{for(k in n) print k, n[k]}'
  corpus/adjacency-host-audit-r48.tsv` → `unchanged 10 / sibling-absent 6`. Instrument: `--selftest`
  → allPass=true 16/16; v7→v8 diff comment/const/schema/usage hunks only.
- **C2 (operability) — VERIFIED; measured at `710c7143c2d52c43cbe1c168236ff4076e72f7a5`:**
  before: `node scripts/check-adjacency.mjs --repo <lane> --fleet <fleet> --json` → exit 1,
  verdict=failed, rows=16, verified=**5**, findings 6 × sibling_unresolved + 4 × ruling_unresolved +
  3 × quote_too_long (`.ufo/waves/round-48/controls/c2-gate-before-at-r48-open.json`);
  prediction (pre-data, over the repair bytes): same + `--fleet-repo <fleet-checkout>` → exit 1,
  verified=**10**, findings exactly 6 × sibling_unresolved
  (`.ufo/waves/round-48/measure/c2-gate-prediction-at-freeze.json`, gate sha pinned `19bcd7d9…`);
  after: same command at the data revision → **EQUALS THE PREDICTION**
  (`.ufo/waves/round-48/measure/c2-gate-green-at-data.json`; landed blob re-hashed to the pin);
  control: without the flag → verified=7, 6+4 findings. Self-test: `ADJACENCY_SELFTEST
  verdict=clean cases=64 reasons=18 could_not_evaluate=6`
  (`.ufo/waves/round-48/measure/c2-gate-selftest-r48.txt`).
- **C3 (coverage capability) — VERIFIED; measured at `f623ce5d1696df4a64ef9d29cd8568375ae50c57`:**
  `git ls-tree -r --name-only <REV> -- corpus/evidence/round48/webview2-cdp | wc -l` → baseline
  **0** → **2**; counter on the committed bytes → exit 0, predicate true, 0 findings
  (`.ufo/waves/round-48/measure/wv2-counter-green-at-data.json`); post-freeze repro (fresh nonce)
  counter-green (`.ufo/waves/round-48/measure/wv2-counter-green-repro.json`); the same counter on
  the r44 chrome receipt → exit 1, **18 findings**; `--selftest` → cases=6 pass=6
  (`.ufo/waves/round-48/measure/wv2-counter-selftest.json`). Live-run facts: Edg/156.0.4314.50,
  discovery ~0.5 s via `EBWebView\DevToolsActivePort`, nonce-bound, PNG 8,063 B sha `dcd754c6…`,
  teardown sweep 0.
- Registry: `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md` 157 → **159**.
  Knowledge: `ls corpus/knowledge/*.md | wc -l` 64 → **65**.

## Sources & frontier

`SOURCES: 157 → 159` — counting command `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|'
corpus/SOURCES.md` (and `node scripts/check-sources.mjs` → exit 0, `verdict=clean rows=159
tiers=A:143,B:7,C:9 status=queued:15,mined:134,rejected:10 findings=0`, receipt
`.ufo/waves/round-48/measure/check-sources-at-integration.txt`). Rows added: **S158** (docs/A —
Microsoft Learn, Debug WebView2 apps with VS Code: the documented host-side remote-debugging route;
raw-fetched 65,545 B, staged, 23-word 1-hit quote; mined; used-by the round-48 knowledge note +
lesson), **S159** (code/A — the Microsoft.Web.WebView2 SDK's `WebView2.h` COM ABI header: the
interface GUIDs + vtable order the minimal host declares; package fetched, 2,951,155 B staged,
4-word 1-hit quote under the pinned `MIDL_INTERFACE`; mined). No rows touched in place. Census
START **and** END exit 0 (END carries the W04 set unchanged at 22 — S158/S159 URLs are new; the
intermediate END run that read **exit 1 with E12 for both rows** — my rows first appended at the
file end, outside the Registry table — is disclosed in the lesson Mistakes row 5; the rows were
moved inside the table before anything landed, and the passing receipt supersedes the failing one).
Sourced claims: C3's evidence cites S158 and S159, both opened this round. Knowledge notes 64 → 65.
Stale-count mining per §2b: five mistakes mined this round (the r47-closure D1 erratum; the
reasoned-predicate risk defused by the prediction-receipt discipline; the standalone-launch dead end
read honestly; the cp-overwrite producer slip; the E12 structural catch).

## Trend verdicts

| Trend | Verdict | Evidence |
|---|---|---|
| expansion | improved | New capability row `webview2-cdp-loopback-windows` (the third Chromium-class surface demonstrated on this host, staged sources S158/S159, committed receipt+PNG, digest-pinned counter); new sourced note on ground the coverage map did not hold (registry 157 → 159; notes 64 → 65); PROVINCE frontier moved to the real host surface. |
| quality | improved | The r47-closure debt closed in committed bytes with live red/green receipts (the owed re-bind: red 15 → green 0 under an instrument whose retarget diff is comment/const-only); the C2 re-declaration turned the r47 refusal's cause into a discipline — sha-pinned pre-data prediction receipt, landed-blob pin check, programmatic equality at data time; the gate selftest grew 57 → 64 with the wrong-venue fails-closed case; no admitted entry failed a re-check. |
| discernment | improved | Every predicate was MEASURED before the freeze and the one numeric after-state the round could have reasoned (C2's verified=10) exists as a prediction receipt instead; the standalone-launch dead end was read honestly (the probes bundle refutes the surface the lane hoped for) and the capability was built on the documented host route; the r47 closure's D1 defect is corrected by a named erratum, never an in-place rewrite; the round's own census refused its own SOURCES placement (E12) and the fix is disclosed. |

## SHONEN

- `[~] SKILL.md contains real decision tables, error patterns, checklists, cited sources` — unchanged this round (`SKILL.md` untouched; the round's new decision-table material lives in the knowledge note and the gate/selftest fixtures; prior pointer `SKILL.md` §Approval table, §Evidence ladder, §Runbook stands); asserted-by-author.
- `[~] At least one end-to-end domain task executed and logged in LOG.md` — this round's end-to-end task: driving a real browser surface end-to-end (compile host → launch → CDP discovery → invocation-bound evaluate → screenshot → keyed teardown to 0) plus the adjacency red→green cycle, logged in the LOG round-48 entry with committed receipts (`.ufo/waves/round-48/`, `corpus/evidence/round48/`); asserted-by-author.
- `[~] Instructions executable by an agent without oral context` — the round's instruments run from committed bytes alone (meter v8 usage line, gate CLI + `--fleet-repo`, the webview2 runner's `--help`-grade usage line, the knowledge note's decision table); asserted-by-author.
- `[~] No cross-domain bleed (PROVINCE.md still accurate)` — PROVINCE updated to the real host surfaces (the third declared surface + the not-standalone finding); the six absent-sibling findings and the binfor contested-open lines stay routed, not absorbed; asserted-by-author.

(All four remain `[~]`: only a non-author may write `[x]` — left to the operator per the r46/r47
closure notes; the round's evidence looks fully checkable by a non-author.)

Assimilation: `considerthese/` does not exist in the lane repo (checked 2026-11-01). Assimilation:
none — shokuknow unreachable.

L0: the tabi | round-44 line (L2 floor) remains open and was routed around — never treated as
answered; no new L0 question this round.
