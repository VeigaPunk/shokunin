# KasegiRecordConformance — round-20 record audit (advisory)

**Seat:** `KasegiRecordConformance` (UFO-FSD scribe, L2 leaf, read-only)  
**Lane:** `/home/vgpnk/Projects/shokunin/kasegi-shokunin`  
**Wave:** `shokunin12h-20261014-p1-audit`  
**Steered identity commit (contract):** `a5cbf77cd21ed87d5a368a1f9456dfdc40faeadc`  
**Observed HEAD:** `a5cbf77cd21ed87d5a368a1f9456dfdc40faeadc` — `round-20: OMP-era freshness re-census (measured gates; records + scoped repair)`  
**This file is data only.** Not a judge verdict, receipt, admission, or lane edit.

Axes in scope for this seat (judgment context): **freshness, operability, calibration, adjacency**.  
Contract slice audited here: **record conformance** for steered round 20 — lesson file, `LOG.md` entry, `SCORECARD.md` move-log row, and whether the lesson’s evidence pointers resolve.

---

## 1. Executive verdict (record surface)

| Criterion | Result | Notes |
|---|---|---|
| `corpus/lessons/round-20-recensus.md` exists | **PASS** | Present on disk; in identity commit pathspec |
| `LOG.md` carries round-20 entry | **PASS (thin)** | Section `## 20 — re-census round (freshness axis-move)`; body is a pointer, not a measured narrative |
| `SCORECARD.md` carries move-log row | **PASS** | Move-log table row `\| 20 \| freshness \| … \| corpus/lessons/round-20-recensus.md \|` — **only** move-log row in file |
| Lesson evidence pointers resolve | **MIXED** | Lane-local instrument + census paths OK; monorepo advisory glob OK only via parent `../.ufo/…`; six debt IDs resolve only in advisory HistoryClaims; orphan-root / 970-deletion sentence is **unbound to a repo** inside the lesson and **does not resolve in the lane git db** |

Overall record triad (lesson + LOG + SCORECARD row): **present**.  
Lesson claim graph: **not fully closed** — see §4 broken/weak pointers.

---

## 2. Binding observations (measured, not re-run gates)

### 2.1 Identity / tree (context only; Identity seat owns full judgment)

```
git -C kasegi-shokunin rev-parse HEAD
→ a5cbf77cd21ed87d5a368a1f9456dfdc40faeadc

git -C kasegi-shokunin show --name-only --pretty=format: a5cbf77
→ LOG.md
→ SCORECARD.md
→ corpus/lessons/round-20-recensus.md

git -C kasegi-shokunin status --porcelain
→ ?? plans/          (untracked; contains plans/wwkd-round-20-recensus.md)
→ tracked tree clean
```

Lane is `master...origin/master [ahead 1]` at audit time (no push performed by this seat).

### 2.2 Core record files

| Path | Exists | In `a5cbf77` |
|---|---|---|
| `kasegi-shokunin/corpus/lessons/round-20-recensus.md` | yes (1.7K) | yes |
| `kasegi-shokunin/LOG.md` §20 | yes (file 824 lines; §20 = lines 819–824) | yes (delta) |
| `kasegi-shokunin/SCORECARD.md` move-log row 20 | yes (file 186 lines; move-log ends at row 20) | yes (delta) |

### 2.3 LOG §20 (verbatim shape)

```
## 20 — re-census round (freshness axis-move)

2026-10-14 · steered round 20 · axis: freshness · 32-lane fleet wave + parent integration.

Full round detail: `corpus/lessons/round-20-recensus.md`. Advisory inventories:
`.ufo/waves/shokunin12h-20261014-p1-repair/members/`.
```

Contrast: round-19 is a long measured bullet in the same LOG. Round-20 **defers** all gate numbers to the lesson. That still **is** a LOG entry under the triad test; calibration note: it is thinner than prior re-census practice.

### 2.4 SCORECARD move-log (verbatim row)

```
| 20 | freshness | measured at HEAD (see lesson) | verdicts recorded per gate, no scalar | `corpus/lessons/round-20-recensus.md` |
```

No separate “Round 20 result” narrative section exists (r17–r19 have dedicated result sections). Move-log row alone satisfies the named criterion; adjacency/freshness scoring prose for r20 is lesson-only.

---

## 3. Lesson body — claims inventory

Source: `kasegi-shokunin/corpus/lessons/round-20-recensus.md` (full file, 35 lines).

### 3.1 Path / artifact pointers

| # | Pointer as written | Resolution rule used | Result |
|---|---|---|---|
| P1 | `corpus/lessons/round-20-recensus.md` (self; via LOG/SCORECARD) | lane-relative | **RESOLVES** |
| P2 | `.ufo/waves/shokunin12h-20261014-p1-repair/members/Kasegi*.md` (lesson L4) | lane-relative | **MISS** — no `kasegi-shokunin/.ufo/…` |
| P2b | same | monorepo-relative `shokunin/.ufo/…` | **RESOLVES** — 5 files: `KasegiGateRepair.md`, `KasegiHistoryClaims.md`, `KasegiLiveAnchors.md`, `KasegiRecordPrep.md`, `KasegiScopeAudit.md` |
| P2c | same | `kasegi-shokunin/../.ufo/…` | **RESOLVES** (equivalent to P2b) |
| P3 | LOG bare dir `.ufo/waves/shokunin12h-20261014-p1-repair/members/` | same as P2/P2b | **MISS lane-local; OK monorepo** |
| P4 | `corpus/instruments/citation-survival.tsv` | lane-relative | **RESOLVES** |
| P5 | `corpus/instruments/citation-survival.md` | lane-relative | **RESOLVES** |
| P6 | gate scripts `corpus/instruments/{anchorcheck,density,resolve}.py` | lane-relative | **RESOLVES** (all three present) |

**Broken as lane-absolute path:** P2 / P3 when evaluated from the lane worktree root without a parent-prefix convention.  
**Resolves under fleet monorepo convention:** parent `shokunin/.ufo/waves/…` (observed).

### 3.2 Named debt IDs

Lesson lists:

- New (r20 advisory set): `TRIAGE-LOST-BASE-MISPREFIX`, `CLAIM-CHECK-96-MIRROR-MISBASE`, `BLOB-PIN-LOWERCASE-PATH`, `CENSUS-NOTE-NEVER-LANDED`, `UFO-DOT-LISTING-DRIFT`, `UFO-HISTORY-NOT-INTACT`
- Standing (r19): `RECEIPT-STORE-LOST`, `MIRROR-SOURCE-LOST`, `ORIGIN-REPO-LOST`

| Debt ID | In lesson | In lane `LOG.md` / `SCORECARD.md` | In repair advisory members | Verdict |
|---|---|---|---|---|
| `RECEIPT-STORE-LOST` | yes | yes (r19) | yes | **RESOLVES** (lane + advisory) |
| `MIRROR-SOURCE-LOST` | yes | yes (r19) | yes | **RESOLVES** |
| `ORIGIN-REPO-LOST` | yes | yes (r19) | yes | **RESOLVES** |
| `TRIAGE-LOST-BASE-MISPREFIX` | yes | **no** | `KasegiHistoryClaims.md` only | **WEAK** — not landed in lane SCORECARD/LOG debt tables; resolves only via advisory inventory P2b |
| `CLAIM-CHECK-96-MIRROR-MISBASE` | yes | **no** | HistoryClaims only | **WEAK** (same) |
| `BLOB-PIN-LOWERCASE-PATH` | yes | **no** | HistoryClaims only | **WEAK** (same) |
| `CENSUS-NOTE-NEVER-LANDED` | yes | **no** | HistoryClaims only | **WEAK** (same) |
| `UFO-DOT-LISTING-DRIFT` | yes | **no** | HistoryClaims only | **WEAK** (same) |
| `UFO-HISTORY-NOT-INTACT` | yes | **no** | HistoryClaims only | **WEAK** (same) |

If “lesson claims resolve” requires **lane-owned** durable records for named debt, the six new IDs are **unrowed debt** (pointer hangs off non-committed advisory prose). If advisory inventories cited by the lesson count as evidence, they resolve there with owners/unblock text in `KasegiHistoryClaims.md` debt table (~rows 318–325).

### 3.3 Quantitative / history claims

| # | Claim | Independent check | Result |
|---|---|---|---|
| Q1 | anchorcheck → exit 0; `7 in-range / 0 bad / LOST-RECORDED=306 / PIN-BROKEN=0 / OUTSIDE-BASE=0 / BASE-ABSENT=0` | Repair after-receipt `kasegi-after-corpus_instruments_anchorcheck.py-SKILL.md.json`: exit 0; stdout summary matches (also `ORIGIN=0`). `measured_revision` on receipt = `d1e6e8f…` (pre-`a5cbf77`). | **RESOLVES** against receipt + instrument path (receipt rev is parent of record commit) |
| Q2 | density `--label r20-recensus` → exit 0; `645` path-citation instances / 18 blocks | After-receipt density JSON: exit 0; tail `Total path-citation instances: 645 across 18 blocks.`; mean dens 154.0 (lesson omits mean). | **RESOLVES** |
| Q3 | `resolve.py .` → exit 0; regenerated survival tsv/md | After-receipt resolve JSON: exit 0; `corpus=116/1144 all=132/1471`; wrote both survival files. On-disk survival header: corpus **116/1144**, lane **132/1471**. Last *commit* touching survival files remains `d1e6e8f` (r19); r20 commit did **not** pathspec the survival pair (content match / no tracked diff at audit). | **RESOLVES** as files + rates; **note:** regeneration not uniquely evidenced by r20 commit pathspec |
| Q4 | Scorecard corpus/lane rates (`116/1142`, `132/1469`) ≠ regenerated (`116/1144`, `132/1471`) | SCORECARD r19 prose contains `116/1142` and `132/1469` once each; survival has `116/1144` and `132/1471`; SCORECARD has **zero** of the regenerated pair. | **RESOLVES** (both sides exist; mismatch is real) |
| Q5 | “reachable history is an orphan 3-commit line rooted at `72ab84a8`” | **Lane** `git cat-file -t 72ab84a8` → not a valid object. Lane root commit = `aeddcd2…` (“seed: kasegi shonen”); `rev-list --count HEAD` = 29. **ufo-fsd-alpha** (`~/Projects/ufo-fsd-alpha`): `72ab84a8` → `72ab84a80c4033aa1182654fb3f288bb7ff446c4`; `rev-list --count HEAD` = 3; sole root = that hash; HEAD `964f443e`. | **BROKEN in lesson as written** — repo not named; fails in lane DB; true only for ufo-fsd-alpha |
| Q6 | “cross-history `--diff-filter=D` is 970. Do not adopt 50.” | Lane unique deleted names across history ≈ 1 (not 970). ufo-fsd-alpha: `git diff --diff-filter=D --name-only 5725fa7d3 HEAD \| wc -l` → **970**; `merge-base --is-ancestor 5725fa7d3 HEAD` fails (exit 1). Kumitate environmental “50” paraphrase lives in sibling SCORECARD / root-loss note, not re-checked here beyond pointer class. | **BROKEN in lesson as written** without ufo-fsd / `5725fa7d3` binding; numbers match ufo-fsd-alpha + HistoryClaims/LiveAnchors advisories |

### 3.4 Gate command strings vs safe contract list

Contract safe gates for kasegi:  
`python3 corpus/instruments/anchorcheck.py SKILL.md`; `density.py SKILL.md --label audit`; `resolve.py .`.

Lesson uses density label **`r20-recensus`** (not `audit`). That is consistent with the repair after-receipt filename and is not a missing pointer; label divergence from the audit-wave command table is noted for GateRerun, not scored as a missing file here.

---

## 4. Missing / broken pointers (named)

1. **Lane-relative advisory path (broken local):**  
   `.ufo/waves/shokunin12h-20261014-p1-repair/members/` and `…/Kasegi*.md`  
   - Missing under `kasegi-shokunin/.ufo/…`  
   - Present under `/home/vgpnk/Projects/shokunin/.ufo/waves/shokunin12h-20261014-p1-repair/members/`  
   - **Owner/unblock:** record authors — prefix monorepo path (`../.ufo/…` from lane, or `shokunin/.ufo/…` from fleet root) so lane-local resolution matches intent; or document the monorepo-root convention once in the lesson.

2. **Unqualified git object `72ab84a8` (broken in lane; foreign-repo true):**  
   - Lesson states orphan 3-commit history rooted at `72ab84a8` without naming `~/Projects/ufo-fsd-alpha`.  
   - **Owner/unblock:** HistoryClaims / RecordPrep errata — bind the sentence to `ufo-fsd-alpha` HEAD line (`964f443e` ← `5ace2559` ← `72ab84a8`) and mark describe-don’t-pin relative to kasegi’s own history (`aeddcd2` seed).

3. **Unqualified `cross-history --diff-filter=D` = 970 (broken in lane; foreign-repo true):**  
   - Requires ufo-fsd-alpha and non-ancestor pin `5725fa7d3`.  
   - **Owner/unblock:** same as (2); cite LiveAnchors/HistoryClaims measurement command explicitly.

4. **Six new debt IDs without lane SCORECARD/LOG rows (weak / non-lane-durable):**  
   `TRIAGE-LOST-BASE-MISPREFIX`, `CLAIM-CHECK-96-MIRROR-MISBASE`, `BLOB-PIN-LOWERCASE-PATH`, `CENSUS-NOTE-NEVER-LANDED`, `UFO-DOT-LISTING-DRIFT`, `UFO-HISTORY-NOT-INTACT`  
   - Only co-occur in lesson + `.ufo/waves/…/KasegiHistoryClaims.md`.  
   - **Owner/unblock:** parent integrator / RecordPrep — append-only SCORECARD carried-debt bullets (or LOG) if fleet requires lane-durable names; else keep advisory-only and state that boundary in the lesson.

5. **Not broken (explicit non-miss):**  
   - Lesson file, LOG §20, SCORECARD move-log row 20, instruments, survival census files, standing three r19 debts, rate-mismatch claim (Q4), measured gate summary strings vs after-receipts (Q1–Q3).

---

## 5. Agree / disagree with lane’s own round-20 record

| Lane claim (surface) | This seat |
|---|---|
| Round 20 lesson landed at `corpus/lessons/round-20-recensus.md` | **Agree** |
| LOG points at that lesson | **Agree** |
| SCORECARD move-log cites that lesson on freshness with no scalar | **Agree** |
| Advisory inventories under `.ufo/waves/shokunin12h-20261014-p1-repair/members/` | **Agree** contents exist at **monorepo** path; **disagree** that the bare path resolves from the lane root |
| Instruments already derive roots; no gate change this round | **Not re-executed** here (GateRerun owns). Record claims are internally consistent with r19 LOG + after-receipts on `d1e6e8f` |
| Named debt list including six new IDs | **Agree** IDs are written; **disagree** that they are fully lane-record-backed (advisory-only) |
| 50-deletion sentence does not reproduce; use 970 / orphan `72ab84a8` | **Agree** as ufo-fsd-alpha forensics (measured here); **disagree** that the lesson text is self-resolving without that repo binding |
| Scorecard vs census denominator drift | **Agree** (116/1142 & 132/1469 in SCORECARD vs 116/1144 & 132/1471 in survival) |

---

## 6. Calibration / adjacency / freshness notes (seat axes)

- **Freshness:** triad files timestamp with identity commit `2026-10-14 21:15:36 -0300`; lesson and LOG/SCORECARD are contemporaneous with steered round 20. Survival census last *committed* on r19; r20 lesson asserts regeneration — operability of `resolve.py` is evidenced by repair after-receipt, not by a new blob in `a5cbf77`.
- **Operability:** pointers to the three instruments and survival outputs are openable; advisory path operability depends on cwd (lane vs monorepo).
- **Calibration:** LOG §20 is pointer-thin vs r19; move-log is the sole SCORECARD r20 surface (no r20 result table). Risk: readers treating SCORECARD r19 rates as current census without reading the lesson drift bullet.
- **Adjacency:** lesson correctly defers six debts and history disputes to repair-wave advisories and (implicitly) ufo-fsd-alpha / kumitate environmental text; those edges are real but under-qualified in the lesson prose.

---

## 7. Out of scope (not done by this seat)

- No lane file edits, commits, pushes, builds, lints, tests, or formatters.  
- No live re-run of `anchorcheck` / `density` / `resolve` (receipts + static paths only).  
- No identity/pathspec judgment beyond noting observed HEAD and commit name list.  
- No content-read of credentials/oauth/session material.  
- No subagent dispatch.

---

## 8. Artifact paths

| Role | Path |
|---|---|
| This advisory | `/home/vgpnk/Projects/shokunin/.ufo/waves/shokunin12h-20261014-p1-audit/members/KasegiRecordConformance.md` |
| Lesson | `kasegi-shokunin/corpus/lessons/round-20-recensus.md` |
| LOG | `kasegi-shokunin/LOG.md` (§20) |
| SCORECARD | `kasegi-shokunin/SCORECARD.md` (move-log row 20) |
| Survival census | `kasegi-shokunin/corpus/instruments/citation-survival.{md,tsv}` |
| Repair advisories | `shokunin/.ufo/waves/shokunin12h-20261014-p1-repair/members/Kasegi*.md` |
| After-receipts (supporting, not re-run) | `shokunin/.ufo/waves/shokunin12h-20261014-p1-repair/evidence/kasegi-after-*.json` |

---

## 9. One-line seat result

**Record triad for kasegi round 20 is present (lesson + LOG §20 + SCORECARD move-log row). Lesson pointer graph is mixed: instruments/census/standing debts OK; advisory path fails lane-local resolution; six new debt IDs are advisory-only; `72ab84a8` / 970 history claims are broken without an explicit ufo-fsd-alpha binding.**
