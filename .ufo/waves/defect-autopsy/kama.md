# Kama defect autopsy — rejected rounds 91, 92, 93 (`rejected-honest-stop`)

Fleet root: `/home/vgpnk/Projects/shokunin`. Read-only. Evidence pointers are `file:line`, command + output, or commit hash. Structure follows the sibling `.ufo/waves/defect-autopsy/tameshi.md` (§ Round-by-round, Counts, Pre-file gate, Dominant mechanism).

## Rounds 89/90 (admitted — baseline for contrast)

Both admitted closures state the same admission rule:

- 89 spot-check:8–9 — "Both declared claims verify on their frozen predicates, re-measured live by this closure (not only from receipts)" (`kama-shokunin/corpus/lessons/round-89-verifier-spotcheck.md:8`)
- 90 spot-check:8–9 — "Both declared claims verify on their frozen predicates, re-measured live by this closure at every measured revision" (`kama-shokunin/corpus/lessons/round-90-verifier-spotcheck.md:8`)

89: C1 operability (unloadable router model files, 11 cells) base 5/0 exit 1 → 0/0 exit 0; C2 depth (8 signature rows bound to wire answers) 0 → 8/8 bound. Closure re-measured both live against committed bytes, recaptured the signature receipt byte-identical (spot-check:79–87).
90: C1 operability (13 hostile answers) base 8/0 → 0/0, but only at M′ `a09effae`: "M carried held-out harm the wave found; the repair landed in-round and re-measures clean, per the r89 precedent" (spot-check:65). C2 depth (24 reason rows) 0 → 24/24, receipt recaptured byte-identical (spot-check:80–88).

Both allowed the lane to intervene on a wave finding in-round (89 12-seat repair `5b1e0fb3`; 90 repair `a09effae`) and file only the repaired tip. MANIFEST rows 89/90 record the same shape.

## Round-by-round

### Round 91 — C1 operability (VERIFIED) + C2 depth (K2 FIRED, honestly recorded)

**Rejection reason, verbatim** — `kama-shokunin/corpus/lessons/round-91-verifier-spotcheck.md:8`:
> "Verdict: status `ok`, **not admitted** (`rejected-honest-stop`). C1 (operability) verifies and was re-measured independently by this closure; C2 (depth) is not verified — its frozen kill rule K2 fired, which the lane itself recorded and this closure confirms against the pinned binary and the pinned upstream sources."

MANIFEST corroborates (`MANIFEST.json` rounds[91] `notes`): "Not admitted: C2 (depth) not verified, K2 fired and honestly recorded by the lane (dated SKILL/knowledge corrections, lesson M1, KQ146 + failing falsifier)."

**Claim vs measured.** Lane report `.ufo/reports/round-91/kama.md:65–66`: C1 `cells=12 mismatches=5 positive_mismatches=0` (base, T1/T2/T4/T5 killed 120 s) → `mismatches=0 positive_mismatches=0`, all cells ≤ 2.1 s at `3decfa36`; C2 `rows=0` → `rows=14 bound=14` exit 0 at `3f317ecd`.
Closure spot-check:44–70: C1 independently re-measured (200 000 ids > 120 s base → 0.38 s tip, rule preserved via `ENVIRON` backslash match) — **verified, operability improved**. C2 counter green (14/14 bound, tip same), but K2 re-checked independently: pinned binary `--help` prints `-np, --parallel N number of server slots (default: -1, -1 = auto)`; `arg.cpp:1373` sets `params.n_parallel = -1`, `server.cpp:126–129` resolves 4 slots — while row T07 states `1` from `common.h:464` (spot-check:77–82).
Lane's own report:20–23: "C2 **K2 fired**: `w1/RV02ThresholdRows.md` … (BLOCKER-1: T07 states `n_parallel` 1 from `common.h:464`; llama-server b12177 sets `-1` auto at `common/arg.cpp:1373` …). C2 is recorded **not verified**."

**Instruments / class.** The C1 instrument ran green and survived closure twice (lane counter + closure re-run). The C2 instrument also ran green (`bound=14`, exit 0) — the green did not survive because the *wording* of the row, not the binding, was false: the counter binds a line number in a shared struct; the binary's parser overrides that line. Class **(a) green but unprovable wording/scope**. The designated reviewer missed it; a scout (SC01) and the pinned binary caught it. In 89/90 the depth claim was a *receipt* bound to observed wire answers; in 91 the depth claim was a *default* derived from upstream source without running the pinned binary's `--help` (which KQ146, created in-round, now requires).

### Round 92 — C1 depth (K2 FIRED via SC01; RV02 passed all 15) + C2 operability (VERIFIED)

**Rejection reason, verbatim** — `kama-shokunin/corpus/lessons/round-92-verifier-spotcheck.md:8`:
> "Verdict: status `ok`, **not admitted** (`rejected-honest-stop`). C2 (operability, capability `linear-probe-paths`) verifies and was re-measured by this closure at base, M2 and tip. C1 (depth) is not verified: its frozen K2 ("a non-author read finds a misstating row") fired on R01 and R08 through wave-1 SC01; the lane recorded this itself and this closure confirms it against the pinned upstream bytes."

MANIFEST (`MANIFEST.json` rounds[92] `notes`): "Defects (status-neutral): terminal pre-report gate red on carried round75-instruments, APPEND_DEBT unaccepted 16->18 (events 95->97); report commit author date 23:05:08 precedes cited tip 23:06:51 … Routed: R1 round75-instruments + 2 new append-debt events; R2 superseding R01/R08 rows under KQ149; R3 C1-class counter able to fail on decision overreach (CR02/MT02/V7)."

**Claim vs measured.** Lane report:73–74: C1 `rows=0` → `rows=15 bound=15 … help_checked=7 help_disagree=0 supersedes=14` exit 0; C2 `mismatches=6` → `0/0` exit 0 at `fa8aedb7`.
Closure spot-check:64–78: C1 counter re-measured green at M1 and tip; K2 confirmed independently — `common/arg.cpp:4608–4616` (`--embd-gemma-default` sets `port=8011`, `n_parallel=32`), `server-http.cpp:93/96/125` (`AIP_MODE=PREDICTION` rewrites port), `server-models.cpp:1218` (router children get free port) make R01/R08 decision cells false for those starts. Lane report:35–38: "C1 not verified (author): wave-1 scout SC01 … shows R01's and R08's decision cells overstate the binary … although the designated reviewer RV02 passed all 15 rows."
Closure spot-check:82–100: C2 re-measured base 6/0 → M2/tip 0/0, D1–D9 byte-equal, doubling ≈linear — **verified, operability improved**.

**Instruments / class.** Same as 91: C1 counter green (15/15 bound, 7/7 help-defaults equal) but decision cells overstate the binary under other setters. Class **(a)**. Two structural details matter: (i) the same designated reviewer RV02 **passed all 15 rows** (report:43–44) while the scout SC01 found the overstatement — the reviewer instrument is checking the row values against the parser default, not against other setters; (ii) closure R3 states the counter *cannot* discriminate decision overreach: "CR02: 14 wrong C1 tables pass; MT02 16/23 counter mutants exit-identical; V7 `TYPE_CHECKING` binds" (spot-check:147–149). The green is structurally blind to the kill class. [INFERENCE] That is why the same reviewer passed in both rounds and only the scout caught it.

### Round 93 — C1 operability (VERIFIED) + C2 depth (K2 FIRED via RV02 + SC01)

**Rejection reason, verbatim** — `kama-shokunin/corpus/lessons/round-93-verifier-spotcheck.md:8`:
> "Verdict: status `ok`, **not admitted** (`rejected-honest-stop`). C1 (operability, capability `router-file-repeat`) verifies: this closure re-ran the frozen counter at base, M1 (`fe5f031c`), the repaired M1b (`b3765799`) and the tip. C2 (depth) is not verified: its frozen K2 ("a non-author read finds a misstating row or decision") fired through wave-1 RV02 and SC01; the lane recorded this itself and this closure confirms both RV02 findings against the pinned upstream bytes."

MANIFEST (`MANIFEST.json` rounds[93] `notes`): "C1 verified; C2 not verified (K2 fired, author agrees) -> rejected-honest-stop."

**Claim vs measured.** Lane report:83–84: C1 `cells=10 mismatches=5` → `mismatches=0 positive_mismatches=0 probe=rev` exit 0 at `fe5f031c`, repaired at `b3765799` (adds `st_ctime_ns`); C2 `population=48 rows=0 missing=48` → `rows=48 bound=48 … derived_disagree=0 decisions=2 decisions_bound=2` exit 0.
Closure spot-check:53–81: C1 re-measured green at loads 135–202 (two non-green runs at load ≈245 are fixture-sanity exit 2 and R01 single-entry deadline — "Not a falsification", spot-check:67–72); RV01 DEFECT-1 (same-size rewrite, mtime restored) red at `fe5f031c`, green at `b3765799` 3/3; harm suites identical md5. **C1 verified, operability improved.**
Closure spot-check:95–111: C2 K2 confirmed independently — `arg.cpp:2524–2531/2529` (P06/P07 same variable as P03, labelled `-`/`unrelated` against the section's own glossary); `arg.h:91–95` + `preset.cpp:44` + `arg.cpp:4753/4764` (argv `std::map` order puts `--port` before preset options, so `params.port = 8014` wins — R16 router-child clause defeated by a child preset). Lane report:37–40: "C2 not verified (author): wave-1 reviewer RV02 … reports P05–P07 as misstating (labels `-`/`unrelated` … against the section's own glossary) and R16's router-child clause defeated by a child preset carrying `--vision-gemma-*` … That is K2."

**Instruments / class.** C2 counter green again (`bound=48`, `decisions_bound=2`, `derived_disagree=0`). The failure this time is not a wrong value but a wrong *label*: P05–P07 text cells are archive-exact (spot-check:109–111: "not harmed, because the misstatement is marked in the same round … and the rows' text cells are archive-exact") while the row's relational label contradicts the section's own glossary. Class **(a)**: the counter verifies textual binding, not the semantic decision the row asserts. The reviewer this round *did* fire (RV02), drawing the closure's note: "the round's one disagreement (RV02/SC01 vs the author's C2 table) became lessons M4/M6/M8 and QUALITY KQ151" (spot-check:137–138).

**Ancillary conformance defects (status-neutral, not the kill).** Terminal gate red all three rounds (carried `round75-instruments`, `APPEND_DEBT` growing 16 → 18 → 21 across 91–93; spot-check:38–40); report author date precedes tip in 92 and 93 (spot-check:24); 93 filed without `WAVE-DONE` (spot-check:30, 43). None of these is the admission failure per the closures ("No owned axis is harmed").

## Counts and the 89/90-vs-91/92/93 contrast

| Class | Count |
|---|---|
| (a) instrument green but claim wording/scope unprovable | **3/3 depth claims** (T07, R01/R08, P05–P07/R16) — the killing claim in all three rounds |
| (b) instrument never reached green | 0/3 (every killed C2 counter printed exit 0 at M and tip) |
| (c) before/after numbers did not re-derive | 0/3 (closure re-ran every frozen counter at base/M/tip; all matched — only the load-sensitive R01 note at 93) |
| (d) independent non-author re-run disagreed (veto) | 0/3 (closure agreed with every author verdict 3/3) |
| (e) structural defect invisible to the lane | 0/3 (every kill was filed by the lane's own wave: RV02/SC01/RV02) |

The operability claim verified in **all three** rejected rounds (spot-check 91:44, 92:80, 93:48), exactly as both claims verified in 89/90. So the mechanism is not "the instruments fail" — the *probe* claims pass every time. What changed is which claim the lane called depth: 89/90's depth was a **receipt** (wire answers recaptured byte-identical); 91–93's depth was a **default/decision derived from upstream source text**, verified only by a textual binding counter. Each round's depth claim read one more source layer than the counter could understand, the counter stayed green, and a wave seat found the semantic overstatement in the same round.

Criteria above only partially discriminate the classes: 91/92/93 and 89/90 all satisfy "falsifiable predicate + counter + K2 + counter frozen before freeze + honest record". The structural difference the evidence supports is narrow: **scout/reviewer seats finding what the counter cannot see** (91 SC01, 92 SC01-not-RV02, 93 RV02+SC01) versus **helpers firing in 89/90** (RV01/EX03 in 90, CR02/EX02/SN01 in 89 — all repaired and re-measured before filing). The lane now reports the same finding honestly instead of treating the counter-green as admission. [INFERENCE] 89/90 were admitted because the wave-found harm was repairable in-round; 91–93 were not because the wave-found kill was a source of truth the lane had cited — re-reading the binary/upstream after data would be moving the predicate, so the only honest move was to record the kill and re-claim next round under a new criterion (KQ146 → KQ149 → KQ151).

## Pre-file gate — YES (with the caveat that catches-shape, not green-shape)

A lane-side pre-file gate could have caught all three kills **before filing**, because in each round the killing artifact existed in lane custody before the report: `w1/RV02ThresholdRows.md` (91), `w1/SC01SourceReopen.md` (92), `w1/RV02SetterRows.md` + `w1/SC01` output (93, partly unsettled at filing). The gate did not fail for lack of signal; it was not run — or not enforced — before the depth claim was filed. What the gate must check (all computable from lane-held evidence before filing):

1. **Every K2-designated non-author read has settled and been graded against the claim.** No depth claim files while a reviewer/scout seat on that claim is unsettled or un-read (93 filed without `WAVE-DONE`; SC02's sweep was graded only next round per R6).
2. **The depth counter must be shown able to fail on the decision class, not just on binding.** Pre-freeze forgery battery must include a *wrong decision* mutant (a row with the right line but the wrong semantic label/value) and must refuse it by name. Closure R3 in 92 already states the bar: 14 wrong tables pass today (spot-check:147–149). Any `PASS` on a decision-mutant is a freeze failure.
3. **Row values must be re-checked against every setter, not only the parser default.** KQ146 (binary `--help`) checks one layer; KQ149 (preset/argv-order sweep) checks the next; the gate must run **both** before filing — 92 ran KQ149 after SC01 found it; 93's R16 was defeated by the same argv-order class KQ149 names. Permissible version: gate = "no unsettled scout/reviewer on the depth claim + decision-forgery battery refused + KQ146 and KQ149 both executed as committed receipts."
4. **Report author date ≥ cited tip** (92, 93 both violated; self-checkable in seconds: 92 spot-check:24, 93 spot-check:24). This is a conformance hygiene gate, not an admission gate.

[INFERENCE] Why this is "yes, but": the lane *did* have the firing signal pre-file and behaved honestly once it landed; the gate would not have made the depth claim true — it would have prevented freezing a claim whose own wave had not yet been allowed to read it. The protocol still requires the honest stop; the gate only moves the stop before filing.

Tooling directive: no tool installed or updated during this autopsy (read-only `read`/`grep`/`eval` of MANIFEST and committed evidence only).
