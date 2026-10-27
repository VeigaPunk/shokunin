# kengaku round 48 — fresh-start C1/C2 claims tested; neither admitted

## Work performed

Declared claims: **R48-C1** (calibration — repair fixture-fence honest over-refusal under a frozen v3 counter) and **R48-C2** (coverage — admit the committed TB2 `polyglot-c-py` grader package under a Q40 counter). Neither verifies at a committed landing tip; neither is admitted.

- Read the last three rejected closures (r45 `73540ccc`, r46 `a5ed97f1`, r47 `98a0cb51`) and their verifier spot-checks before freezing claims: `kengaku-shokunin/corpus/lessons/round-45-verifier-spotcheck.md`, `round-46-verifier-spotcheck.md`, `round-47-verifier-spotcheck.md`.
- Froze two causally separable claims at `plans/round-48-claims.md` (`a543d92083557dd9b33ee674e9b99b03411f80af`). The round-46 evidence was read first; the fresh-start do-nothing controls were set to fail before scoring. C2's S166 source was reopened by L1 at the pinned URL on 2026-10-27; its exact quote and a rejected Docker Hub candidate are in `corpus/lessons/round-48.md`.
- Dispatched one v2 wave inline: 64 seats, 41 attack roles (critics 15, mutation-testers 14, reviewers 12); remaining role counts: connectors 4, executors 10, revenger 1, scouts 3, scribes 4, sentinel 1. L1 held the canonical planner seat. `w1-results.json` confirms all 64 settled. Seven seats left no report file; no explicit status/error text was supplied (named with last-output state in the lesson). No residual task call or second wave was made.
- Dispatch conformance defect: the generated wave context embedded the run-10 role→alias map in `build_spec.py`/`w1-spec.json` despite the no-alias-in-lane rule; no per-seat `model` field was passed and OMP role routing remained active. The taken dispatch is preserved as evidence and was not rewritten (`.ufo/waves/round-48/build_spec.py`, `w1-dispatch.json`).
- R48-C1 scratch evidence: the candidate v3 counter on a clone of stage-1 `REV a543d920…` measured the base fence `HONEST fixtures=120 admitted=112 refused=8`, `PREDICATE R48-C1 fail`; a candidate fence measured 120/120 honest admissions, 20/20 refusal modules refused and 12/12 sealed modules refused. No stage-2 counter/pins/controls or landing-tip run was committed; the candidate C1 mutation floor was not demonstrated. Evidence: `.ufo/waves/round-48/w1/R48C1ExecCounter.md`, `R48C1ExecHonest.md`, `R48C1ExecFenceA.md`, `R48C1ExecControls.md`.
- R48-C1 discrepancy: the r46 “9/9 refused” override evidence used `{WORK}` placeholder argv, not repository-state over-refusal. On the re-authored 120-fixture population the base fence refused 8; the frozen base-fence control still failed as required. The `refused=9 minimum` note was not silently changed; see `R48C1ExecControls.md` and `R48C1ExecCounter.md`.
- R48-C2 scratch evidence: the v4 candidate's `--dry` run still reports V7 missing committed violations for `both-print` and `toolchain`; the pre-receipt controls run with P10 disabled and fail as controls. The case-author seat left no report/artifact. The frozen probe candidate `22b7779e…` fails the permitted `--stage-check` 18/18 and its `mode="all"` path omits seed/recipe setup; no full probe run was made. Evidence: `.ufo/waves/round-48/w1/R48C2ExecCounter.md`, `R48C2ExecProbe.md`, `R48C2ExecControls.md`, `R48C2TagInv.md`.
- Reopened S166 (`tests/test_outputs.py`) and Docker Hub tag metadata directly; no registry row was appended or changed. Mined the unsatisfiable frozen-tag mistake into `corpus/lessons/round-48.md`; mined Proposal 2 from `considerthese/2026-10-26.md` after opening its r36/r37 evidence. Assimilation: none — the staged package is 175 rows/65 entries; no one-theme, 1–3-entry subset was selected.
- Connector boundary scan reports reusable verification/mutation methodology to **Tameshi** only; Kengaku retains its product-specific fence/counter and no **Kama** serving-plane overlap was found. The scan was bounded to the directly relevant Province declarations; it did not claim fleet-wide absence of overlap (`.ufo/waves/round-48/w1/R48C1ConnOverlap.md:23-36`).
- Re-ran the source census at round end (details below). Freshness observations: `:34113/health` HTTP 000 and no `llama-server` process; `~/archive/bench-arena` and `~/bench-arena` did not resolve in the searched home paths. No claim depended on those host surfaces. Fleet-root misroot sweep: `git -C /home/vgpnk/Projects/shokunin status --porcelain` showed only `?? .scratch/closure-mado-r50.json`; this is orchestrator-owned run state, untouched.

## Landed changes

- Stage-1 claims freeze: `plans/round-48-claims.md`, lane commit `a543d92083557dd9b33ee674e9b99b03411f80af`.
- Wave builder/spec/dispatch evidence: `.ufo/waves/round-48/{build_spec.py,w1-spec.json,w1-dispatch.json,w1-validate.err}`, lane commit `453ddfdb4e8f69068aaf25084756188012cfcb10`; ready marker `.ufo/waves/round-48/w1.ready`, lane commit `bf783c1ee4dc61a5e4fa1b12a87c6d547eba2767`.
- Round lesson, SCORECARD, LOG and README index, plus wave reports/results: lane commit `d4eacdfb56307c069c245270f4d78e2ec314829e`; `LOG.md` `## Round 48` records each disposition. No `SOURCES.md` row, knowledge entry, capability or production fence/probe change landed. The temporary L1 C1 counter candidate was removed and `plans/fixture_fence.py` restored to the committed lane version because stage 2 and the required C1 mutation evidence were absent.
- Final lane tip is `d4eacdfb56307c069c245270f4d78e2ec314829e`; `git ls-remote origin refs/heads/master` printed the same hash.

## Before → after measurements

| claim | before → after | counting command and measured revision | verdict |
|---|---|---|---|
| R48-C1 calibration | Base fence on the stage-1 120-fixture population: `HONEST fixtures=120 admitted=112 refused=8` → candidate fence: `120/120 admitted`, refusals 20/20 and sealed 12/12; **no committed landing-tip result**. | Frozen command: `python3 plans/round48_c1_verify.py --lane .`; scratch implementation run on a clone of `REV a543d92083557dd9b33ee674e9b99b03411f80af` (counter candidate at scratch `REV abb08e2…`, repaired fence evidence `R48C1ExecFenceA.md`). Stage-2 freeze absent, so command was not run on the final lane tip. | Unverified / not admitted; score 8→8 held. |
| R48-C2 coverage | Round-46 baseline `checks=13 defects=2` (V7/V8) at `e9d20145` → r48 scratch v4 `--dry` still has V7 defects for `both-print`/`toolchain`; candidate hardened probe `--stage-check` 18/18 failures; no full probe run. | Frozen command: `python3 plans/round48_c2_verify.py --lane .`; scratch candidate/control runs on stage-1 `REV a543d92083557dd9b33ee674e9b99b03411f80af` (`R48C2ExecCounter.md`, `R48C2ExecProbe.md`, `R48C2ExecControls.md`). Stage-2 freeze absent, so no scored full command at final tip. | Not admitted; score 7→7 held by the round-33 L0 cap. |

## Sources & frontier

**SOURCES registry census (start → end):**

Counting command: `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md` → 165 rows before and 165 after. Tier histogram command: `awk -F'|' '/^\|[[:space:]]*S[0-9][0-9][0-9]+[[:space:]]*\|/ {t=$5; gsub(/[[:space:]]/,"",t); n[t]++} END{for(k in n) printf "%s=%d ",k,n[k]; print ""}' corpus/SOURCES.md` → `A=141 B=22 C=2`; status histogram command: `awk -F'|' '/^\|[[:space:]]*S[0-9][0-9][0-9]+[[:space:]]*\|/ {s=$9; gsub(/[[:space:]]/,"",s); n[s]++} END{for(k in n) printf "%s=%d ",k,n[k]; print ""}' corpus/SOURCES.md` → `mined=149 queued=8 rejected=8`. Added by tier: A=0, B=0, C=0. Rows touched old→new: none. Frontier rows advanced: 0. No `used-by`, `status` or `recheck` change.

Start command: `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kengaku` → output below, exit 0.

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
exit=0
```

End command: `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kengaku` → output below, exit 0.

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
exit=0
```

Assimilation: none.

## Trend verdicts

- **expansion: unchanged** — no new knowledge entry, capability, mined SOURCES row or frontier row landed.
- **quality: unchanged** — the defective `22b7779e…` probe is a candidate not integrated into lane production or the admitted corpus; no existing admitted entry was found false or left unmarked. R48-C1/R48-C2 remain unadmitted.
- **discernment: unchanged** — the L1 opened S166 and a rejected Docker Hub source, but no outside non-author spot-check had returned by filing. The round-48 lesson marks these as candidate gate decisions only; independent closure is still required.

## Stale-lane

Respawn-per-round driver; this report closes only kengaku round 48. No other kengaku mission is claimed open. Seven wave seats settled without report files; their result outputs are retained and identified in `corpus/lessons/round-48.md`.

## SHONEN

[~] SKILL.md contains real decision tables, error patterns, checklists and cited sources — `SKILL.md:23-46`.
[~] An end-to-end domain task is executed and logged — historical pointer `LOG.md:7`; round 48 itself did not admit a new task result.
[~] Instructions are executable without oral context — `corpus/lessons/round-8-aggregator-box3-coldrun.md:48`.
[~] No cross-domain bleed; PROVINCE remains accurate — `PROVINCE.md:129`.

## Tool installs

None. No pacman transaction was attempted.

## L0 questions

No new L0 question filed. Existing coverage cap `kengaku | round-33` remains open.
