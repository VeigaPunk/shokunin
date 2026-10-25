# KotobaRecordPrep — advisory record draft

**Seat:** `KotobaRecordPrep` (scribe) · wave `shokunin12h-20261014-p1-repair`  
**Lane:** `kotoba-shokunin` · steered round **19** (operator WWKD; counter not advanced here)  
**Role bound:** report-only. No lane commits, no SCORECARD/LOG edits, no gate runs, no GateRepair implementation.  
**Judged axes (wave):** freshness, operability, calibration, adjacency  
**Milestone:** independent six-lane freshness re-census at steered rounds  

This file is **not** a native judge verdict, lane round report, receipt, admission, or SCORECARD/LOG mutation. Parent owns integration, gate execution after the editing wave settles, admit/reject, and any pathspec commit under `kotoba-shokunin <kotoba@shokunin.local>`.

---

## 1. Starting state (measured)

| Field | Value | Provenance |
|---|---|---|
| Steered round | 19 | `baselines.json` → `kotoba.round`; `plans/wwkd-round-19-recensus.md` |
| Start HEAD | `02302c521b933c55fc4be79193e61537e3380751` | baselines + `git rev-parse HEAD` |
| HEAD subject | `round-18: re-census against moved substrate — omp ff59fc1b, opencode v2.0.26 (d9123b9b)` | `git log -1 --oneline` |
| Tree status at prep | clean tracked tree; untracked `plans/` only (`?? plans/`) | `git status -sb` / porcelain |
| Prior landed move | Round **18** depth substrate re-census (**hold** 9 → 9), not a freshness score raise | `SCORECARD.md` move-log row 18; `LOG.md` § Round 18 |
| Substrate pins (r18) | omp `ff59fc1b…`; opencode `d9123b9b…` (v2.0.26); ufo-fsd-alpha HEAD `964f443ee53df0ce06bd689af01f0dea031b01f9` | `verifiers/baseline.json` `measured_against`; host checkout |
| Before receipt | `.ufo/waves/shokunin12h-20261014-p1-repair/evidence/kotoba-before.json` | fleet wave evidence |

### 1.1 Before-receipt (only captured gate this wave)

```
argv:        python3 verifiers/verify_corpus_integrity.py
cwd/context: kotoba lane tree @ 02302c521b933c55fc4be79193e61537e3380751
exit_code:   0
timed_out:   false
started_at:  2026-10-14T23:34:59.318840+00:00
finished_at: 2026-10-14T23:34:59.397309+00:00
```

**Stdout (full retained in receipt; summary lines):**

- `corpus.index tracked=47 unindexed=0 stale=0 missing=0 (60 FILE-column patterns over 47 md files)`
- `corpus.pointers report_dead=0/32 commit_total=27 unresolvable=0 nonhash=0` (shapes absolute=31, tilde=1; quoted-excluded=2, pointer-excluded=8)
- `9/9 checks pass`

**Not captured in before-receipt (therefore unprovable as this-wave before, not "pass"):**

- `verify_harness_claims.py` (+ `--self-test`)
- `verify_surfaces.py` (+ `--self-test`)
- `verify_skill_checklist.py` (+ `--self-test`)
- `verify_corpus_independent.py` (+ `--self-test`)
- `fault_injection_corpus.sh --self-test` and full control matrix

Round-18 LOG claims those six instruments were green **at r18 landing**; that is historical evidence for HEAD content, not a fresh before measurement for steered-19.

### 1.2 SCORECARD axis snapshot at start HEAD (authoritative rows, not re-scored here)

| Axis | Score at HEAD | Last scored move | Notes |
|---|---:|---|---|
| depth (owned) | 9 | r18 hold | substrate re-derived; not raised |
| consistency (calibration sub-axis, owned) | 10 | r15 | ceiling named |
| coverage (advisory) | 8.5 | r14 recorded r15 | — |
| operability (advisory) | 8.5 | r16 | checklist 8 executed / 0 delegated / 33 unexecuted |
| freshness (advisory) | 8 | r16 evidence text | **r18 did not rewrite this score cell**; instruments re-run in r18 under depth hold |
| calibration (advisory) | 8.5 | r17 | governance gate |
| adjacency (advisory) | 8.0 | r16 routing | planned r18 adjacency **not executed** (r18 became depth re-census) |

**Record debt (do not silently fix in this seat):** `SCORECARD.md` § planned still titles **“Round 18 — adjacency remeasurement/routing”** while move-log already has round 18 depth. Parent should replace planned with the steered-19 freshness contract after admit, not leave r18 adjacency as current plan.

---

## 2. Single axis-move acceptance contract (draft for parent)

### 2.1 Declared move

- **One move:** **freshness** re-census of live claims and gate pins against the current host tree and binaries, with **operability** as the co-judged runnable-artifact axis (instruments still exit 0/1/2/3 with honest self-tests).
- **Not a second move:** adjacency sibling routing, depth band raise, calibration raise, coverage raise, consistency work.
- **Round identity:** steered **19** per baselines/WWKD. This seat **does not allocate or advance** any round counter, MANIFEST row, or `.ufo/state/kotoba.round`.
- **Clean no-change is allowed** and must not be fabricated as improvement (`plans/wwkd-round-19-recensus.md`).
- **Code change authorization:** only `KotobaGateRepair`, and only for a **reproduced remaining** root-default / source-resolution defect. RecordPrep does not authorize edits. Earlier r18 repairs are existing state — do not reintroduce.

### 2.2 Acceptance predicates (all required for a non-reject record; admit/reject = parent)

1. **Declared axis only.** Records name freshness (+ operability co-judge). No scalar “overall improved.”
2. **Before → after command evidence** for every gate in §3, with full verdict lines, exit codes, and `measured_revision` (post-integration HEAD if GateRepair lands; else start HEAD).
3. **Source-root / default resolution audit** (WWKD “one move”):
   - Confirm gates still **do not** take a stale `--src` default (r18 classification: none).
   - Repo defaults remain script-grandparent / live host paths (`DEFAULT_REPO = Path(__file__).resolve().parent.parent`; harness/surfaces binaries under `~/.local/bin/omp`, `~/.opencode/bin/opencode`).
   - Explicit bad override stays fail-closed; no silent fallback to deleted `origin-work`.
   - Live substrate checkout path for citations: `~/Projects/ufo-fsd-alpha` @ `964f443e…` when a ufo path is claimed live; `origin-work` only as **historical**.
4. **Active-vs-historical citation boundary:**
   - r18 errata retained append-only (SKILL truncator example; LOG r13 note; `harness-verifier-round10.md` symlink root; `opencode-extraction-round14.md` v1 rules).
   - No live claim re-pins a deleted path as current.
   - Unresolved **live** defects stay named debt (not baselined away).
5. **Falsifiers (any one fails the move):**
   - Score gain without parent-run after evidence.
   - Treating before-receipt’s single corpus green as full-suite pass.
   - Editing sibling repos or absorbing adjacency findings.
   - Re-pinning baselines to hide red without named mechanism.
   - Claiming `[x]` SHONEN without a named non-author.
   - Second axis-move smuggled into the same commit.
6. **Band rule for freshness:**  
   - **Hold / unchanged** if all registered gates re-verify green and no new live drift class appears — valid successful re-census.  
   - **Improved** only if parent measures a closed live defect class or a new non-vacuous freshness instrument with red-before→green-after.  
   - **Unprovable-but-better** only with explicit unrun measurement named.  
   - **Harmed** if a live claim is false and left unmarked, or a gate is suppressed.

### 2.3 Per-axis draft verdict slots (fill after parent gates; defaults below)

| Axis | Draft pending after-gates | Basis now |
|---|---|---|
| freshness | **unprovable** until full suite after | before = corpus only; r18 historical green ≠ r19 after |
| operability | **unprovable** until checklist+self-test after | last scored r16; r18 LOG claimed exit 0 unchanged |
| depth | **unchanged** expected (no depth work) | r18 hold already recorded |
| coverage | **unchanged** expected | out of move |
| calibration | **unchanged** expected | out of move; watch SCORECARD planned staleness as calibration smell if left |
| adjacency | **unchanged** expected | sibling SKILL routing still carried debt; not this move |
| consistency | **unchanged** expected | at 10 |

### 2.4 Learning-trend draft slots (`LEARNING.md` vocabulary only)

| Trend | Draft | Why |
|---|---|---|
| expansion | **unchanged** expected | no new province ground required for re-census |
| quality | **unprovable** until re-verify | freshness/operability quality signal needs after suite |
| discernment | **unprovable** | needs non-author spot-check of any admit/reject this round |

---

## 3. Gate-command inventory (parent post-integration)

Run from `kotoba-shokunin` repo root. Preserve **full** stdout/stderr, exit code, argv, and `git rev-parse HEAD` on each receipt. Skip nothing by “r18 said green.” Do not run while sibling GateRepair edits are in flight.

| # | Command | Role | Baseline / fixtures | Last claimed green (historical) | This-wave before |
|---|---|---|---|---|---|
| G1 | `python3 verifiers/verify_corpus_integrity.py` | corpus index + report/commit pointers (9 checks) | `verifiers/corpus-baseline.json` (tracked_files=47, report_total=32, commit_total=27, zeros for dead/unindexed/stale/missing/unresolvable/nonhash) | r18 LOG: 9/9 | **exit 0, 9/9** @ `02302c5…` (`kotoba-before.json`) |
| G1a | `python3 verifiers/verify_corpus_integrity.py --self-test` | fixture model | script fixtures | r11+ lineage | **unprovable** (not in before receipt) |
| G2 | `python3 verifiers/verify_corpus_independent.py` | independent re-derivation (non-author script lineage) | none pinned equal-mode baseline file in inventory | r18 LOG: exit 0 | **unprovable** |
| G2a | `python3 verifiers/verify_corpus_independent.py --self-test` | self-test | fixtures | prior rounds | **unprovable** |
| G3 | `python3 verifiers/verify_harness_claims.py` | omp/opencode live pins (28 checks) | `verifiers/baseline.json` (`measured_against.round18_move`; omp `ff59fc1b…`, oc `d9123b9b…`) | r18: crash→28/28 | **unprovable** |
| G3a | `python3 verifiers/verify_harness_claims.py --self-test` | model | script | prior | **unprovable** |
| G4 | `python3 verifiers/verify_surfaces.py` | instruction-surface census (7 checks / 38 class ids) | `verifiers/surfaces-baseline.json`; inventory default `corpus/knowledge/instruction-surface-census-round13.md`; binaries `/home/vgpnk/.local/bin/omp`, `/home/vgpnk/.opencode/bin/opencode` | r18: 7/7 PASS, self-test 70/70 | **unprovable** |
| G4a | `python3 verifiers/verify_surfaces.py --self-test` | fixtures under `verifiers/fixtures/surfaces/` | — | r18 70/70 | **unprovable** |
| G5 | `python3 verifiers/verify_skill_checklist.py` | SKILL checklist operability (10 check ids post-r17 incl. governance) | `verifiers/checklist-baseline.json` (41 boxes: **8 executed / 0 delegated / 33 unexecuted**); vocabulary JSON | r18 LOG: exit 0 (552 lines noted there; current `SKILL.md` **601** lines at HEAD — line-budget claim must be re-measured, not copied) | **unprovable** |
| G5a | `python3 verifiers/verify_skill_checklist.py --self-test` | fixtures | r17 LOG: 0 failure(s) over 1504 assertions / 71 fixture dirs | **unprovable** |
| G6 | `bash verifiers/fault_injection_corpus.sh --self-test` | planted-fault harness OK | script-local | r18: OK | **unprovable** |
| G6b | full control + a–h matrix (as r17 LOG) | intentional fault-f blind spot retained | — | r17 ALL PASS incl. fault-f | **unprovable**; do not “fix” fault-f |

### 3.1 Source-root / override surface (inventory for GateRepair + ScopeAudit)

| Instrument | Root default | Override flags | `--src`? |
|---|---|---|---|
| `verify_corpus_integrity.py` | `DEFAULT_REPO` = script grandparent | `--repo`, `--baseline`, `--no-baseline` | **no** |
| `verify_corpus_independent.py` | script grandparent | `--repo` | **no** |
| `verify_skill_checklist.py` | nearest `.git` ancestor of `--skill` / grandparent | `--repo`, `--skill`, `--map` | **no** |
| `verify_harness_claims.py` | live host HOME paths for omp/oc | `--omp-bin`, `--omp-db`, `--oc-bin`, `--oc-log`, `--omp-sessions`, `--cwd` | **no** |
| `verify_surfaces.py` | grandparent repo; hard-coded host binary paths in `DEFAULT_BINARIES` | `--repo`, `--omp-binary`, `--opencode-binary`, `--*-strings`, `--inventory`, `--baseline` | **no** |
| `fault_injection_corpus.sh` | clones under temp (mutating) | script flags | N/A — **never** treat as non-mutating gate without warning |

**r18 finding carried:** stale `--src` defaults = **none**. Path-class debt was citation/historical, not gate default.

### 3.2 Named exclusions

- No external fetches.
- No reads of credentials/oauth/server.token/session material (shape-only).
- Kagi secret-gated checks N/A to this lane.
- Offline kake partial rules N/A.
- Global `~/.config` / routing: read-only if touched; not write scope.

---

## 4. Draft SCORECARD move-log row (parent append-only; do not invent After)

Copy only after parent fills After from real commands. **Do not advance scores in this draft.**

```
| 19 | freshness (OMP-era re-census; operability co-judge) | 8 — SCORECARD cell last raised on r16 full-suite green; r18 re-ran instruments under depth hold without rewriting this cell | <AFTER: parent-measured — hold 8 / +0.5 only with new closed live defect class / unprovable if suite incomplete> | wave before: `verify_corpus_integrity.py` exit 0 9/9 @ `02302c5…` (kotoba-before.json); after: parent full G1–G6 receipts @ <post-integration HEAD>; WWKD `plans/wwkd-round-19-recensus.md`; no second axis |
```

**Axes table cell updates (parent only, if admitted):**

- freshness evidence paragraph ← parent after suite (replace r16-only narrative if re-verified).
- § planned ← replace stale “Round 18 adjacency…” with next single move (adjacency routing remains ranked carry **after** freshness re-census closes, per r17 plan intent).
- operability cell ← refresh evidence timestamps only if G5/G5a re-measured; score stays 8.5 unless a new operability defect is closed/opened.

---

## 5. Draft LOG entry (append-only; parent authors final bytes)

```markdown
## Round 19 — freshness re-census (steered; OMP-era wave shokunin12h-20261014-p1-repair)

- **Axis selection.** Operator-directed independent freshness re-census at steered
  round 19. Start revision `02302c521b933c55fc4be79193e61537e3380751` (round-18
  substrate re-census already landed). Operability co-judged; no adjacency/depth
  second move.
- **Before (wave receipt).** `python3 verifiers/verify_corpus_integrity.py` →
  exit 0, 9/9, tracked=47, report_dead=0/32, commit_total=27 @ before.json.
  Other instruments: not in before receipt → recorded unprovable at wave start.
- **Source-root audit.** Gates have no `--src`; defaults are live host / repo
  grandparent. Explicit overrides fail-closed. origin-work citations remain
  historical per round-18 errata.
- **GateRepair.** <none | narrow diff only if residual root defect reproduced>.
- **After (parent integration).** <paste full G1–G6 verdict lines + HEAD>.
- **Band.** freshness <unchanged hold | improved | harmed | unprovable-but-better>
  — admit/reject is parent/judge, not this draft.
- **Per-axis.** freshness …; operability …; depth unchanged; coverage unchanged;
  calibration …; adjacency unchanged (carry sibling routing).
- **Learning.** expansion …; quality …; discernment … (non-author spot-check).
- **Carried debt.** (see §7) SCORECARD planned staleness; OC-1…OC-6 single-author
  witness; skills_rescan_max grammar; adjacency 225/14 sibling population;
  SHONEN all `[~]`; AXES↔MISSION naming on l0-questions.
```

---

## 6. SHONEN assessment (report draft; marks unchanged pending non-author)

Heading required in the eventual lane round report. Marks below mirror `SHONEN.md` at start HEAD. **No `[x]` without named non-author.** This seat is author-side relative to any parent-integrated prose it drafts.

### SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — pointer: `SHONEN.md` box 1 notes (r12 ReviewSHONEN was lane-dispatched → author attestation under PROTOCOL.md:34-39); 41 checklist boxes; r18 historical errata on origin-work truncator example. **No fresh non-author re-derive this wave.**
- [~] At least one end-to-end domain task executed and logged in LOG.md — pointer: r10 harness verifier, r11 corpus integrity + `corpus/knowledge/cold-run-round11.md`; r13 reverted `[x]` because ColdRunRecord was lane-dispatched. **Still `[~]`.**
- [~] Instructions executable by an agent without oral context — pointer: `verifiers/verify_skill_checklist.py` + harness/corpus verifiers; r13 B1/B2 fixes; needs fresh non-author for `[x]`. G5 unprovable this wave until parent runs.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — pointer: PROVINCE remains prompt/skill craft; r16 adjacency findings routed not fixed; r19 must not absorb sibling SKILL dead tokens. **Unchanged intent.**

**Verifier note retained:** every lane-run check ⇒ `[~]`; only external non-author may write `[x]`.

---

## 7. Unresolved debt and cross-domain owners

| ID | Debt | Unblock | Owner |
|---|---|---|---|
| D-planned-stale | SCORECARD § planned still “Round 18 adjacency” after r18 depth landed | Parent rewrites planned to post-r19 next move when recording | kotoba records (parent) |
| D-freshness-cell | freshness score cell still r16 narrative despite r18 full re-run under depth | Parent either holds 8 with r19 after evidence or documents why r18 didn’t move the cell | kotoba freshness |
| D-oc-v2-witness | OC-1…OC-6 / census § B stands on one author reading | Scout re-enumerates v2.0.26 instruction surfaces vs rules | kotoba + LiveAnchors evidence |
| D-skills-rescan | `oc.log.skills_rescan_max` is max-over-rescans not per-skill | Richer opencode log grammar → re-pin | kotoba harness gate |
| D-adj-14 | Sibling SKILL citation population 225 subjects / 14 unresolved (r17 carry) | Route to owners; no sibling edits | adjacency → sibling lanes / protocol |
| D-hist-origin | origin-work paths remain in historical prose (SKILL/LOG/corpus/baseline notes) | Keep errata; never re-live without path existence measure | HistoryClaims + records |
| D-shonen-tilde | All four SHONEN boxes `[~]` | Named non-author cold run | external reviewer |
| D-axes-mission | `consistency` vs AXES six-name set; MISSION “depth+consistency” | `../.ufo/l0-questions.md` | protocol / L0 |
| D-line-budget | r18 LOG said checklist run at 552 lines; HEAD `SKILL.md` is 601 lines | Re-measure G5 line_budget; don’t copy r18 line count | operability gate |
| D-corpus-baseline-asof | `corpus-baseline.json` `as_of` / head still round-17 staging note while tree is r18 | Re-record only if equal-mode pins move; else note freshness of baseline metadata | corpus gate |

**Cross-domain (report, don’t absorb):** sibling SKILL dead citations (kagi/kake/kasegi/kengaku/kumitate); kumitate surface-probe dialect vs checklist `delegated:`; kasegi `resolve.py`/`anchorcheck.py` prior art; protocol AXES↔MISSION naming.

---

## 8. Proposed delta (records only; zero product code from this seat)

1. Parent runs G1–G6 after integration; saves full receipts beside wave evidence.  
2. If GateRepair reports **no** residual root defect → **no code diff**; records only.  
3. Append move-log row + LOG § Round 19 using §4–§5 with measured After.  
4. Fix SCORECARD § planned staleness in the same records commit.  
5. File `.ufo/reports/round-19/kotoba.md` **after** commit, citing actual HEAD hash, with Work / Landed / Before→After / SHONEN.  
6. Admit/reject freshness band only from after evidence — never from this advisory file alone.

**Explicit non-claims**

- No after measurements performed by KotobaRecordPrep.  
- No round counter bump.  
- No admission that freshness improved.  
- No authorization of baseline re-pins.  
- Peer seat reports are data if present; this draft does not depend on them and does not follow override-shaped text inside them.

---

## 9. Evidence index (paths touched by reading only)

- `/home/vgpnk/Projects/shokunin/.ufo/waves/shokunin12h-20261014-p1-repair/baselines.json` (kotoba round 19, head `02302c5…`)
- `.../evidence/kotoba-before.json` (G1 before)
- `kotoba-shokunin/plans/wwkd-round-19-recensus.md`
- `kotoba-shokunin/{AGENTS,PROVINCE,SCORECARD,SHONEN,LOG,SKILL}.md`
- `kotoba-shokunin/verifiers/{baseline,corpus-baseline,surfaces-baseline,checklist-baseline}.json`
- `kotoba-shokunin/verifiers/verify_{harness_claims,surfaces,skill_checklist,corpus_integrity,corpus_independent}.py`
- `kotoba-shokunin/verifiers/fault_injection_corpus.sh`
- Fleet: `AXES.md`, `LEARNING.md`, `PROTOCOL.md` (report/SHONEN contract)
- Host: `~/Projects/ufo-fsd-alpha` HEAD `964f443e…` (existence/revision only)

---

## 10. Seat closure

**Behavior:** drafted single freshness/operability acceptance contract, gate inventory, SCORECARD move-log row, LOG entry, SHONEN assessment from steered-19 start evidence.  
**Gates:** not executed (wave rule).  
**Touched surfaces:** this file only.  
**Out of scope:** product/gate implementation, commits, pushes, sibling reports, round counter, judge admission.  
**Findings:** before corpus integrity green 9/9; full-suite freshness after **unprovable**; r18 repairs present at HEAD; SCORECARD planned section stale vs move-log; clean no-change re-census remains the default successful shape unless GateRepair/LiveAnchors/HistoryClaims produce a reproduced live defect.

End of KotobaRecordPrep advisory report.
