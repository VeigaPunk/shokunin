# kengaku — round 33 (hyaku run 7, 2026-10-25)

Lane: `kengaku-shokunin` (novelty + calibration; LLM/model research and evaluation).
Baseline: `112091c2d9077e484b53512ca363d2fe6ba6fc5c`. Final lane tip: `4e6a8b1f124db8494cfb96fb85be1967ea11aa5f` (the pushed `master` tip matched `git ls-remote origin refs/heads/master`). Frozen prereg: `plans/round-33-claims.md` (`f0b20aea` + `c227e486`).

Round shape: two validated v1 waves — 36-seat build + 53-seat falsify = **89 seats** (32–64 per wave; 64–100 round band). Planner held at L1; bounded data-walk rode scout `R33ReconPackage`. No residual task call.

## Work performed

Declared claims: **C1 coverage** — admit the grader-semantics package under unused ids; **C2 calibration** — close six round-32 routed defects N1–N6; **C3 freshness** — retain bounded public-catalog response bytes and verify them offline.

- **C1 — admitted with a baseline-delta caveat.** Re-grounded the existing draft against Toolathlon `main.py` at `9be8d8fe` (S103, tier A) and arXiv `2412.05579v2` (S104, tier B); renumbered staged S094→S103 and S097→S104. The final source rows are blob-pinned (`main.py`) and version-pinned (`arXiv …v2`), and the landed rows exactly match `append-rows.md`/`append-block.md`. The final landed-row quote gate is 8/8 located and bound. Evidence: `corpus/SOURCES.md:118-119`, `corpus/knowledge/benchmark-grader-semantics.md`, `.ufo/waves/round-33/assimilation/gate-receipts.txt`.
- **C1 caveat, preserved rather than edited into the frozen claim:** S093's `used-by` already named this draft at the round-33 freeze; round 33 changed no S093 cell. The frozen “S093 gains” sentence is false as a transition, but the final state predicate passes because S093 and the two new rows all name the admitted entry. The frozen control also prints `entries=1`, not the claims file's `entries=0` wording. `R33FS093Delta.md`, `R33FControl.md`, and `R33FIndexTruth.md` record the discrepancies.
- **C2 — six repairs present.** Committed inherited round-32 wave evidence; added the missing scorecard section; appended the round-31/32 report errata and round-30/31 lesson corrections. Final counter is green. The falsify wave found the counter's semantic blind spots (index vs committed tree, heading/token-only checks, 300-vs-400 window, newline handling); the actual six repairs remain, but no calibration score increase is claimed. Evidence: `plans/round33_defects.py`, `corpus/evidence/round33/defects-after.txt`, `R33CounterAttack.md` and `R33F*` reports.
- **C3 — raw response evidence retained.** `hf.raw.json` is 27,698 B; OpenRouter `?limit=10` response is 16,010 B and carries `total_count=467`. Both raw bodies are under 64 KiB and digest-covered; capture now preserves exact fetched bytes. `--verify` passes offline. The 467 is the API's `total_count` field, not a count of the ten returned page records; HF's schema delta is first-record-only. Falsifiers show that `--verify` checks internal consistency, not endpoint authenticity, so the frozen “no fabricated bytes” kill-rule assurance is not supported. Evidence: `corpus/evidence/round33/catalogs/`, `plans/catalog_probe.py`, `R33FOpenRouter.md`, `R33FC3Provenance.md`.
- **Frontier/assimilation:** assimilated `merge/kengaku/`'s benchmark grader semantics; README now scopes discharge to one Toolathlon task and names S103/S104. Q22 landed from `considerthese/2026-10-25.md` proposal 2; proposal 3 is an L0 decision packet; proposal 1 remains operator-side.

## Landed changes

| Change | Lane commit(s) | LOG / evidence |
|---|---|---|
| Inherited round-32 wave tree (N1) | `c227e486a622ff82aae780c6fc58f023dcc82430` | `LOG.md` Round 33; `R33FControlFidelity.md` |
| N1–N6 repairs, round-32 scorecard section, Q22, initial C2 receipt | `78955888542258ba369f5aa72c200c913b4c3c90` | `LOG.md` Round 33; `corpus/lessons/round-33.md` |
| S103/S104 admission and bounded catalog captures | `b54fecad8b247e4761fc941b7ba75134a4ae14fc`, `66c734c0a1e1beabe08fd0e568b4860050ec4e6c`, `6cb5c82267c444eefbc6cd9cb3254cc8d22a242f`, `77ac8c1307ba60e9572a7e2789b71ae31b133440` | `LOG.md` Round 33; `corpus/SOURCES.md`; `corpus/evidence/round33/catalogs/` |
| Final source/entry corrections, C1 V8 cell fix, after receipts, lessons, scorecard and 89-seat wave evidence | `c1a520dd5334445004abce730c87e4c77cbfed5b`, `4e6a8b1f124db8494cfb96fb85be1967ea11aa5f` | `LOG.md` Round 33; `corpus/lessons/round-32.md`, `corpus/lessons/round-33.md`; final wave registry/reports |

## Before → after measurements

| Claim | Before | After at final lane tip | Score / verdict |
|---|---|---|---|
| C1 adoption | Frozen control `.ufo/waves/round-33/claims/control-nothing.txt`: `entries=1 indexed=1 cited_rows=3 rows_present=3 rows_mined=1 usedby_ok=0 census=ok`, exit 1. The frozen prose incorrectly says `entries=0`. | `python3 plans/adoption_check.py --expect .ufo/waves/round-33/claims/adoption-expect.json --census` → `entries=1 indexed=1 cited_rows=3 rows_present=3 rows_mined=3 usedby_ok=1 census=ok`, exit 0; `python3 plans/round33_c1_verify.py --lane .` → `checks=8 defects=0`, exit 0. Receipt: `corpus/evidence/round33/adoption-after.txt`. | **7→7 held**; end-state passes, but the S093 transition was already true at baseline. |
| C2 defects | `.ufo/waves/round-33/claims/defects-before.txt`: `checks=6 defects=6`, exit 1. | `python3 plans/round33_defects.py --lane .` → `checks=6 defects=0`, exit 0; after receipt points to repair commit `7895588` and re-derivation at tip. | **8→8 held**; repairs present, but the counter is gameable and has false-negative paths. |
| C3 catalog | `.ufo/waves/round-33/claims/control-verify.txt`: `raw=absent`, exit 1. | `python3 plans/catalog_probe.py --verify --lane .` → `raw=ok hf_models=50 or_models=467 hf_schema_delta=4 or_schema_delta=0 verify=ok`, exit 0. | **8→8 held**; bounded bytes and offline values verify, but origin authentication is not provided. |

### SOURCES census (before → after)

Command at both ends: `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kengaku`.

Before (`.ufo/waves/round-33/claims/census-before.txt`, exit 0):

```text
kengaku W04 S040 duplicate url arxiv.org/abs/2301.09633 across scopes
kengaku W04 S048 duplicate url aclanthology.org/2020.acl-main.442 across scopes
kengaku W04 S057 duplicate url arxiv.org/abs/2405.11874 across scopes
kengaku W04 S058 duplicate url github.com/UKGovernmentBEIS/inspect_ai/blob/63e45cc52d39b873b944124613da21fdad6f6dcc/src/inspect_ai/scorer/_pattern.py across scopes
kengaku W04 S059 duplicate url www.rfc-editor.org/rfc/rfc8259 across scopes
kengaku W04 S064 duplicate url spec.commonmark.org/0.31.2 across scopes
kengaku W04 S065 duplicate url docs.python.org/3/library/json.html across scopes
kengaku W04 S066 duplicate url doi.org/10.1017/S0950268810000385 across scopes
kengaku W04 S067 duplicate url doi.org/10.1017/S0950268810000385 across scopes
kengaku W04 S068 duplicate url raw.githubusercontent.com/web-arena-x/webarena/dce04686a56253aefba7b18a4fa0937cf1dc987b/config_files/test.raw.json across scopes
kengaku W04 S069 duplicate url raw.githubusercontent.com/web-arena-x/webarena/dce04686a56253aefba7b18a4fa0937cf1dc987b/evaluation_harness/evaluators.py across scopes
kengaku W04 S071 duplicate url docs.python.org/3/library/json.html across scopes
kengaku W04 S075 duplicate url docs.python.org/3/library/json.html across scopes
kengaku W04 S076 duplicate url docs.python.org/3/library/json.html across scopes
kengaku W04 S100 duplicate url github.com/laude-institute/terminal-bench-2 across scopes
kengaku ok /home/vgpnk/Projects/shokunin/kengaku-shokunin/corpus/SOURCES.md
```

After (`corpus/evidence/round33/census-after.txt`, exit 0), stdout was:

```text
kengaku	W04	S040 duplicate url arxiv.org/abs/2301.09633 across scopes
kengaku	W04	S048 duplicate url aclanthology.org/2020.acl-main.442 across scopes
kengaku	W04	S057 duplicate url arxiv.org/abs/2405.11874 across scopes
kengaku	W04	S058 duplicate url github.com/UKGovernmentBEIS/inspect_ai/blob/63e45cc52d39b873b944124613da21fdad6f6dcc/src/inspect_ai/scorer/_pattern.py across scopes
kengaku	W04	S059 duplicate url www.rfc-editor.org/rfc/rfc8259 across scopes
kengaku	W04	S064 duplicate url spec.commonmark.org/0.31.2 across scopes
kengaku	W04	S065 duplicate url docs.python.org/3/library/json.html across scopes
kengaku	W04	S066 duplicate url doi.org/10.1017/S0950268810000385 across scopes
kengaku	W04	S067 duplicate url doi.org/10.1017/S0950268810000385 across scopes
kengaku	W04	S068 duplicate url raw.githubusercontent.com/web-arena-x/webarena/dce04686a56253aefba7b18a4fa0937cf1dc987b/config_files/test.raw.json across scopes
kengaku	W04	S069 duplicate url raw.githubusercontent.com/web-arena-x/webarena/dce04686a56253aefba7b18a4fa0937cf1dc987b/evaluation_harness/evaluators.py across scopes
kengaku	W04	S071 duplicate url docs.python.org/3/library/json.html across scopes
kengaku	W04	S075 duplicate url docs.python.org/3/library/json.html across scopes
kengaku	W04	S076 duplicate url docs.python.org/3/library/json.html across scopes
kengaku	W04	S100 duplicate url github.com/laude-institute/terminal-bench-2 across scopes
kengaku	ok	/home/vgpnk/Projects/shokunin/kengaku-shokunin/corpus/SOURCES.md
exit=0
```
The before output (`census-before.txt`) contains the same 15 W04 lines and `kengaku ok …/corpus/SOURCES.md`, exit 0; W04 delta is 0 with no E errors.

Registry rows: **95→97**, one new tier-A row (S103) and one new tier-B row (S104); no existing source row changed in round 33. Knowledge files and README index rows were **41→41** (the frozen claim file's 40/40 baseline was wrong). The S093 `used-by` pointer was added in round 32, not round 33.

## Sources & frontier

S103 is the pinned Toolathlon `ab-testing/evaluation/main.py` code row; S104 is the version-pinned arXiv v2 survey row. Both are `mined`, opened 2026-10-25, recheck `180d`, and used by `benchmark-grader-semantics.md`. Existing refusal rows S094/S097/S101/S102 remain unchanged. The gate receipts record `collisions=0`, all eight quotes located and bound, and `append-rows.md`, `append-block.md`, `landed-rows.md` byte-identical.

The README Frontier now discharges “and for Toolathlon” only for this one task's scoring code. Other Terminal-Bench 2.0/SWE-bench Pro V2 scoring code and runtime task validity remain open; the latter is outside this lane's PROVINCE.

## Trend verdicts

- **Expansion: improved** — the previously refused grader-semantics candidate is admitted with two new, opened source rows, though it adds no new knowledge file/index row.
- **Quality: improved** — source IDs and pins are corrected, the entry's technical overstatements were corrected against captures, and raw catalog bytes plus runnable checks are committed. Measurement limitations remain explicit.
- **Discernment: improved** — the falsify wave identified the false S093/control/baseline transitions, C2 counter weaknesses, and C3 provenance/total-count limitations before final reporting.

No numerical axis score changed; no axis is claimed harmed.

## SHONEN

- [~] SKILL.md decision aids — unchanged this round; `SKILL.md` remains the current evidence pointer.
- [x] End-to-end domain task — pinned source capture, gate, catalog probe and receipt re-check; independently reviewed by `R33FEntryTruth.md`, `R33FOpenRouter.md`, and `R33FMeasurement.md`.
- [~] Instructions executable without oral context — claim files, wave specs, scripts and receipts are committed; counter limitations are disclosed in this report.
- [x] No cross-domain bleed — connector report `R33Connector.md` found no sibling contest; all accepted content remains in the LLM/model-evaluation province.

## Stale-lane

Respawn-per-round lane. `jj-lane.sh` landed the final lane tip above; `git ls-remote` matched it. A temporary direct-Git orphan (`2b4cef2e`) was abandoned and its work re-landed through the lane helper; no orphan is on the pushed branch.

## Disclosures, dead seats, and open questions

- **Seats:** 36 build + 53 falsify = 89; 0 dead seats and no residual call. Role mixes and flash/attack shares are in `corpus/lessons/round-33.md` §Seat ledger. One falsify report was misrooted to fleet `.ufo/waves/`; it was copied byte-exact into the lane, verified with `cmp`, then removed from the fleet root.
- **Claims:** C1's final state passes but its frozen S093/control/baseline transition prose is inaccurate; C2's actual repairs pass while its counter admits false greens; C3's committed bytes verify while the “no fabricated bytes” kill-rule guarantee is falsified. No frozen claim was rewritten.
- **Open L0 question:** what committed evidence lifts the round-25 coverage cap (coverage remains 7)? Candidate classes and evidence are in the append-only `kengaku | round-33` line of `/home/vgpnk/Projects/shokunin/.ufo/l0-questions.md`; the round did not block on an answer.
- **Tool installs:** none.
