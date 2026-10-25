# KotobaGateRepair — advisory (wave shokunin12h-20261014-p1-repair)

Seat: `KotobaGateRepair` (L2 leaf, gate-default implementation only).  
Lane: `kotoba-shokunin` @ `/home/vgpnk/Projects/shokunin/kotoba-shokunin`  
Steered round: **19**  
Measured starting revision (baselines.json + `git rev-parse HEAD` at open): **`02302c521b933c55fc4be79193e61537e3380751`**  
Before receipt: `.ufo/waves/shokunin12h-20261014-p1-repair/evidence/kotoba-before.json`  
(`argv=["python3","verifiers/verify_corpus_integrity.py"]`, `exit_code=0`, `9/9 checks pass`)  
Plan: `kotoba-shokunin/plans/wwkd-round-19-recensus.md`  
Code mutations this seat: **one** (pin-mode only in `verify_harness_claims.py`).

This file is an advisory worker report only — not a native judge verdict, lane round report, receipt, or admission.

---

## 1. Scope owned

Gate-default implementation files discovered from `SKILL.md` registry + `verifiers/`:

| Path | Role |
|------|------|
| `verifiers/verify_harness_claims.py` | harness claim gate (live host binaries/db/log) — **edited** |
| `verifiers/verify_surfaces.py` | instruction-surface census gate |
| `verifiers/verify_skill_checklist.py` | SKILL checklist + governance citations |
| `verifiers/verify_corpus_integrity.py` | corpus index/pointer/commit integrity |
| `verifiers/verify_corpus_independent.py` | independent second-witness corpus derivation |
| `verifiers/fault_injection_corpus.sh` | planted-fault harness (`--self-test` safe; full path mutating) |

Persisted expectations (`baseline.json` **expect**/notes, other baselines), `SCORECARD.md`, `LOG.md`, corpus notes: **out of write scope** (untouched).

---

## 2. `--src` / source-root resolution inventory

### 2.1 Established fleet pattern (reference only)

`$UFO_SRC` env → first existing of `~/Projects/ufo-fsd-alpha` then `~/Projects/origin-work/ufo-fsd-alpha` → fail-closed; explicit bad `--src`/`--ufo-src` stays bad.

Host fact this wave:

- `~/Projects/ufo-fsd-alpha` → **present**
- `~/Projects/origin-work/ufo-fsd-alpha` → **absent**

### 2.2 Kotoba gate CLI surfaces (static)

| Script | Source-root / UFO flags | Default roots actually used |
|--------|-------------------------|-----------------------------|
| `verify_harness_claims.py` | **none** | `Path.home()` harness paths |
| `verify_surfaces.py` | **none** | `DEFAULT_REPO` = script grandparent; fixed binary paths |
| `verify_skill_checklist.py` | **none** | grandparent / nearest `.git` of `--skill` |
| `verify_corpus_integrity.py` | **none** | `DEFAULT_REPO` = script grandparent |
| `verify_corpus_independent.py` | **none** | script grandparent |
| `fault_injection_corpus.sh` | **none** | `${TMPDIR}` scratch; fleet `.ufo/reports` fixtures only |

**rg** over those implementation files for `origin-work|ufo-fsd-alpha|UFO_SRC|--src|source_root|source-root`: **0 hits** each. No UFO checkout default chain to repair. `LOG.md` r18 already classed stale `--src` as **none**.

**`--src` verdict: measured unchanged** (no invented plumbing).

---

## 3. Reproduced remaining gate defect (pin mode)

### 3.1 Source

Peer `KotobaScopeAudit` (report-only) reproduced:  
`evaluate()` treats mode `at_least` as `value >= expect`.  
`CHECKS` pinned `oc.permission.skill_lines` and `oc.permission.skill_allow` as `at_least` while `baseline.json` **expect is 0** for both. Any non-negative count (including historical 471) **PASS**es. Round-18 text states those log lines are **absent (expected 0)**; the pin did not enforce absence.

Authority for mode is the **`CHECKS` tuple** in `verify_harness_claims.py` (not `baseline.json` `"mode"`). `evaluate()` reads the tuple; baseline supplies `expect` only under `equal`/`at_least`.

### 3.2 Proposed → landed delta

File: `kotoba-shokunin/verifiers/verify_harness_claims.py` lines 549–550

```diff
-    "oc.permission.skill_lines": ("at_least", "permission_skill_lines"),
-    "oc.permission.skill_allow": ("at_least", "permission_skill_allow"),
+    "oc.permission.skill_lines": ("equal", "permission_skill_lines"),
+    "oc.permission.skill_allow": ("equal", "permission_skill_allow"),
```

- **Unchanged:** `baseline.json` `expect: 0` for both ids; notes; SCORECARD; LOG; all other CHECKS; the `at_least` branch in `evaluate()` (retained for future ids).
- **Documentary drift left for parent errata:** `baseline.json:110` and `:114` still say `"mode": "at_least"` while runtime mode is now `equal`. Not edited (persisted baseline fields out of seat write scope).

### 3.3 Behavior after fix

With live `expect: 0`, both checks now require `observed == 0`. Non-zero skill-permission log lines → `DRIFT` exit 1. Absence continues to PASS. Other pins not raised to fit red.

### 3.4 Defect classification (this seat)

| Class | Count | Finding |
|-------|------:|---------|
| (a) stale `--src` / root-default path | **0** | No UFO default in gates |
| (d) genuine lane gate defect | **1** | `at_least`+`expect 0` vacuous absence pins → fixed to `equal` |
| Baseline expect re-pin | **0** | forbidden; expects already correct |

---

## 4. Unresolved debt (named; not fully GateRepair-owned)

| Debt | Owner | Unblock |
|------|-------|---------|
| `baseline.json` documentary `mode: at_least` on the two permission rows | parent / RecordPrep errata | Align mode string to `equal` in a deliberate baseline metadata pass (do not touch `expect`) |
| Historical origin-work / deleted-path citations in prose | HistoryClaims / LiveAnchors | Append-only errata; no live pin resurrection |
| OC-1…OC-6 single-author witness | LiveAnchors | Second blind re-enumeration |
| Full `fault_injection_corpus.sh` (non-`--self-test`) mutating | parent / operator | Deliberate campaign only |

---

## 5. Parent integration — exact commands to run

Cwd: `/home/vgpnk/Projects/shokunin/kotoba-shokunin`  
GateRepair did **not** commit; working tree should show only `verifiers/verify_harness_claims.py` dirty (plus any sibling seats).  
Save full stdout/stderr, exit codes, and `git rev-parse HEAD` / `git diff -- verifiers/verify_harness_claims.py` per run.

```bash
cd /home/vgpnk/Projects/shokunin/kotoba-shokunin

git rev-parse HEAD
git diff -- verifiers/verify_harness_claims.py
git status --porcelain

# Pin-mode smoke (expect PASS when observed permission counts are 0;
# DRIFT if log still emits evaluated permission=skill lines):
python3 verifiers/verify_harness_claims.py; echo EXIT:$?
python3 verifiers/verify_harness_claims.py --self-test; echo EXIT:$?
python3 verifiers/verify_harness_claims.py --json > /tmp/kotoba-harness-after.json; echo EXIT:$?
# Inspect results rows for oc.permission.skill_lines / skill_allow:
# mode must be "equal", expected 0, verdict PASS only if observed==0

python3 verifiers/verify_surfaces.py; echo EXIT:$?
python3 verifiers/verify_surfaces.py --self-test; echo EXIT:$?

python3 verifiers/verify_skill_checklist.py; echo EXIT:$?
python3 verifiers/verify_skill_checklist.py --self-test; echo EXIT:$?

python3 verifiers/verify_corpus_integrity.py; echo EXIT:$?
python3 verifiers/verify_corpus_integrity.py --self-test; echo EXIT:$?
python3 verifiers/verify_corpus_integrity.py --json > /tmp/kotoba-corpus-after.json; echo EXIT:$?

python3 verifiers/verify_corpus_independent.py; echo EXIT:$?
python3 verifiers/verify_corpus_independent.py --self-test; echo EXIT:$?

bash verifiers/fault_injection_corpus.sh --self-test; echo EXIT:$?
```

**Named exclusion:** default (non-`--self-test`) `fault_injection_corpus.sh` clones/mutates temp worlds — not smoke.

**Optional hermetic proof parent may run** (does not change baselines): feed a fake observed dict through `evaluate` with `permission_skill_lines=471` and confirm `DRIFT` under the new CHECKS — not required if live log is already zero.

Do not re-pin `expect` values to force green.

---

## 6. Axis notes (advisory, non-scalar)

| Axis | GateRepair effect |
|------|-------------------|
| freshness | Permission absence claim now fail-closed against log reappearance |
| operability | Same CLI; stronger verdict when grammar returns |
| calibration | CHECKS mode matches r18 “expected 0” semantics; baseline mode string still stale doc |
| adjacency | `--src` still N/A; no cross-lane UFO default invented |

---

## 7. Files changed

| Path | Change |
|------|--------|
| `kotoba-shokunin/verifiers/verify_harness_claims.py` | `oc.permission.skill_lines` / `oc.permission.skill_allow` CHECKS mode `at_least` → `equal` |
| `.ufo/waves/shokunin12h-20261014-p1-repair/members/KotobaGateRepair.md` | this report |

No stage/commit/push. No sibling report overwrite. No SCORECARD/LOG/`expect` edits.
