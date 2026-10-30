# chousa — round64 attempt2 — honest stop

## Work performed

Declared inherited claims: **C1 operability** (G02 v3 knowledge-index behavior, lowest numerically scored non-retired axis), **C2 calibration** (12-mutant claims-audit discrimination), **C3 sourced depth** (__file__-derived roots and exact missing-file assertions). **All three frozen targets missed; none admitted.** The historical operability 3/10 score and other scores remain unchanged. Freeze: `corpus/evidence/round64/claims.md`, inherited at `bf40d99bda9eefdad3ed6276da077cfb24ba82f1`; base `759c6cbef4cf9cdc81b68afc709f3b82ecd1a9d9`.

- Preserved the original frozen counters; restored an inherited uncommitted counter edit and retained its fixture repair only as `corpus/evidence/round64/c1-battery-supplement.py`. The inherited reference remains evidence, not production. Reused committed before/null/sibling receipts and the frozen v2 audit; discarded no inherited evidence. Nine erratum items distinguish false prose, equivalent-mutant/discriminator gaps, and source-vs-output provenance (`corpus/evidence/round64/claims-erratum.md`).
- Implemented recursive, nonvacuous G02 inventory, complete filename matching, Unicode/nested phantom checks, symlink handling, safe invalid-byte reporting and --work refusal. The first production lexer wrongly treated documented globs as actual files; red receipts at `controls/pre-glob-repair/` remain, and changed bytes restore the real lane to PREFLIGHT=8/8. Evidence: `tools/lane-preflight.py`, `controls/measurement-summary.json`, wave Attack05/06/08 and G02Probe06.
- Admitted a narrow explanation of positional parents, normalization, explicit existence and intended identity; S150–S152 opened locally, S153 rejected (`corpus/knowledge/lane-root-derivation-r64.md`; lesson `## Gate`; `source-openings.json`). No external fetch or staged adoption.
- One validated **v2 wave, 64 seats**: executor 20, critic 12, reviewer 12, scribe 12, scout 6, connector 2; **24/64 attack seats**, round total 64, no residual, **0 reported dead seats**. L1 holds the canonical planner seat; ConnectClaims supplies bounded planning data-walk. Main sent WAVE-DONE before this report; `w1-results.json` contains 64 outputs and no error notes. Result format lacks per-seat IDs/answering models; none invented. Live host role routing was used without model overrides, rather than editing the stale prompt map. Evidence: `.ufo/waves/round-64/w1-spec.json`, `w1-dispatch.json`, `w1-results.json`.
- Learned from the previous outside spot-check: sibling receipt retained (`controls/sibling-g0405.txt`), old 5/5 prose explicitly superseded by its historical 8/8 receipt, instrument attacks performed, scratch origin separated from durable evidence. QUALITY 128/129 cite actual red states; no future counter is preclaimed (`corpus/lessons/round-64.md`, `corpus/QUALITY.md`).
- Scope: generic testing remains contested with tameshi; dispatch orchestration belongs to kumitate; filesystem cleanup authority is not absorbed. No sibling/domain-source writes (`w1/ConnectScope/report.md`). Stale-lane: respawn-per-round; no other chousa mission is open in this assignment. No next round started. Tool installs/updates: none. Pacman remained paused. Disk guard printed free-space status then timed out listing consumers; no full-success claim. Owned `/fast/scratch/hyaku/chousa-r64` removed after lane landing.

## Landed changes

All work is logged under **LOG.md “Round64 (attempt2)”** and supported by `corpus/lessons/round-64.md`.

- `34cbd847fa374ce7baa61147209b5772212a3d64`: sourced entry/S150–S153, inherited reference and distinct supplement, initial G02 work, lesson, validated wave/ready.
- `344cb55521581ed10dadbaf4204be562eea99529`: complete-name/recursive semantics and revision-bound measurement harness; its false-positive regression is preserved, not hidden.
- `944955cc1aaf94cbfdc0eda68fa9fc995ca3bec8`: concrete-reference/glob distinction and red receipts; **final measured implementation revision**.
- **`10e1b84e1b56b0f81f785fc73d7be0cb149a23fd`**: 64-seat results and findings, final receipts, SCORECARD verdicts, LOG, gate registrations, source search log, QUALITY criteria, lesson and errata. No frozen target changed. `git ls-remote origin refs/heads/master` printed `10e1b84e1b56b0f81f785fc73d7be0cb149a23fd` before filing.

Required misroot sweep `git -C /home/vgpnk/Projects/shokunin status --porcelain` printed only modified `.scratch/goal-20261029-hyaku-run12.md` and `.ufo/l0-questions.md`; both left untouched. No untracked chousa seat artifact required migration. No aggregator/operator-owned lane file was swept.

## Before → after measurements

Run from `/home/vgpnk/Projects/shokunin/chousa-shokunin`, fresh --work directories under the round scratch root. Final child receipts name **944955cc1aaf94cbfdc0eda68fa9fc995ca3bec8** and record code digests; those code files were not edited afterwards. Final receipt commit: **10e1b84e1b56b0f81f785fc73d7be0cb149a23fd**. `measure-after.py` captures child codes: its own exit 0 means collection completed, **not** claims passed.

| Claim | Counting command | Before → after and verdict |
|---|---|---|
| C1 operability | `python3 corpus/evidence/round64/c1-battery-v3.py --tool tools/lane-preflight.py --fleet /home/vgpnk/Projects/shokunin --work DIR --jobs 2` | Base before receipt: CLEAN=1/1 DEFECTS=17/28 BENIGN=8/11 ZERO=3/3 FAIL, exit 1 → final CLEAN=1/1 DEFECTS=28/28 BENIGN=9/11 ZERO=3/3 FAIL, exit 1 **three runs**. **unprovable/not admitted**: E12/E13 independently draw file/link identities; the frozen PASS target is missed. `controls/c1v3-before-full.txt`, `c1-frozen-after-0.txt` through `-2.txt`. |
| C2 calibration | `python3 corpus/evidence/round64/c2-mutrun.py --target tools/claims-audit.py --matrix v1 --work DIR`; after target `tools/claims-audit-v2.py --matrix v2` | 6/12 killed, exit 1 → **9/12 killed, exit 1**, A07/A10/A11 survive. Target 12/12 missed: **unprovable/not admitted**. `controls/c2-mutrun-v1-final.txt`, `c2-mutrun-v2-final.txt`; independent Counter01/02. Ten-case selftest PASS exit 0 and forced fault exit 1 are insufficient. |
| C3 depth, sourced | `python3 corpus/evidence/round64/c3-count.py --work DIR` | Before shifted mutant names no missing file (`controls/c3-before.txt`, SHIFT_MUTANT_UNNAMED=1/1) → **SMOKE=3/3 RELOCATION_MATCH=0/3 SHIFT_MUTANT_UNNAMED=1/1 C3=FAIL**, exit 1. Expected-path oracle is wrong and relocation is same-depth: **unprovable/not admitted**. `controls/c3-after.txt`; source-supported prose does not validate the oracle. |

Supplementary, **not substituted for frozen predicates**: repaired C1 fixture supplement PASS 43/43 exit 0; old round63 v2 battery PASS twice; both nulls FAIL exit 1; actual full preflight **8/8 exit 0**. Paths: `controls/c1-supplement-after.txt`, `c1-v2-cross-0.txt`, `c1-v2-cross-1.txt`, `c1-null-pass.txt`, `c1-null-diff-oracle.txt`, `preflight-full-run-r64.txt`. The first production run at 344cb555 failed preflight 7/8 and both old batteries; those red outputs remain in `controls/pre-glob-repair/`. The concrete-reference change is the only subsequent implementation delta.

Known unresolved limits: path-recognition forge passes the supplement, ZERO summary parser accepts malformed summaries, C2 runner lacks unmutated control and counts injected timeouts as kills, A07 is ineffective on its stated history, A10/A11 fixtures miss their defects, and Counter04's recorded fault channel disagrees with the revision-bound L1 receipt. Both channel records retained (`claims-erratum.md` item 6). The optional index-rule entry listed in the freeze was not admitted; no missing path is presented as landed knowledge.

## Sources & frontier

Command: `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin chousa`.

**Before output, exit 0** (`.ufo/waves/round-64/census-start.txt`):
```text
chousa	W04	S051 duplicate url www.w3.org/TR/2017/REC-html52-20171214/syntax.html across scopes
chousa	W04	S053 duplicate url docs.python.org/3/library/socket.html across scopes
chousa	W04	S073 duplicate url www.gnu.org/software/coreutils/manual/coreutils.html across scopes
chousa	W04	S074 duplicate url docs.python.org/3/library/hashlib.html across scopes
chousa	W04	S075 duplicate url www.gnu.org/software/coreutils/manual/coreutils.html across scopes
chousa	ok	/home/vgpnk/Projects/shokunin/chousa-shokunin/corpus/SOURCES.md
```
**After output, exit 0** (`.ufo/waves/round-64/census-end.txt`):
```text
chousa	W04	S051 duplicate url www.w3.org/TR/2017/REC-html52-20171214/syntax.html across scopes
chousa	W04	S053 duplicate url docs.python.org/3/library/socket.html across scopes
chousa	W04	S073 duplicate url www.gnu.org/software/coreutils/manual/coreutils.html across scopes
chousa	W04	S074 duplicate url docs.python.org/3/library/hashlib.html across scopes
chousa	W04	S075 duplicate url www.gnu.org/software/coreutils/manual/coreutils.html across scopes
chousa	ok	/home/vgpnk/Projects/shokunin/chousa-shokunin/corpus/SOURCES.md
```
Counts: `python3 corpus/evidence/round64/source-stats.py --revision 759c6cbef4cf9cdc81b68afc709f3b82ecd1a9d9` versus `python3 corpus/evidence/round64/source-stats.py` (both exit 0): **rows 149→153; A/B/C 116/26/7→118/27/8; mined/queued/rejected 121/19/9→124/19/10**. New rows: S150 code A, S151 docs A, S152 own-work B (mined); S153 own-work C rejected. Held status/recheck/used-by changes: **none**. Gate carries access date and <=25-word located quotes; source byte pins in `source-openings.json`. Frontier detail advanced: concrete distinctions between positional root derivation, existence and intent; no province expansion claimed. Outside admit/reject spot-check remains pending; wave reviewers are still the lane.

**Assimilation: none.** Quarantine-first occurred historically in round42; current read-only register slice remains 24 rows (Recon03), not its stale 20-row summary. No fresh external adjudication or adoption. Collision extraction (Recon04 evidence) finds registry 153, staged 114, **72 collisions**; no renumber map needed because nothing adopted. Exact lists retained under `.ufo/waves/round-64/assimilation/`:
```text
reg-ids: S001 S002 S003 S004 S005 S006 S007 S008 S009 S010 S011 S012 S013 S014 S015 S016 S017 S018 S019 S020 S021 S022 S023 S024 S025 S026 S027 S028 S029 S030 S031 S032 S033 S034 S035 S036 S037 S038 S039 S040 S041 S042 S043 S044 S045 S046 S047 S048 S049 S050 S051 S052 S053 S054 S055 S056 S057 S058 S059 S060 S061 S062 S063 S064 S065 S066 S067 S068 S069 S070 S071 S072 S073 S074 S075 S076 S077 S078 S079 S080 S081 S082 S083 S084 S085 S086 S087 S088 S089 S090 S091 S092 S093 S094 S095 S096 S097 S098 S099 S100 S101 S102 S103 S104 S105 S106 S107 S108 S109 S110 S111 S112 S113 S114 S115 S116 S117 S118 S119 S120 S121 S122 S123 S124 S125 S126 S127 S128 S129 S130 S131 S132 S133 S134 S135 S136 S137 S138 S139 S140 S141 S142 S143 S144 S145 S146 S147 S148 S149 S150 S151 S152 S153
staged-ids: S082 S083 S084 S085 S086 S087 S088 S089 S090 S091 S092 S093 S094 S095 S096 S097 S098 S099 S100 S101 S102 S103 S104 S105 S106 S107 S108 S109 S110 S111 S112 S113 S114 S115 S116 S117 S118 S119 S120 S121 S122 S123 S124 S125 S126 S127 S128 S129 S130 S131 S132 S133 S134 S135 S136 S137 S138 S139 S140 S141 S142 S143 S144 S145 S146 S147 S148 S149 S150 S151 S152 S153 S154 S155 S156 S157 S158 S159 S160 S161 S162 S163 S164 S165 S166 S167 S168 S169 S170 S171 S172 S173 S174 S175 S176 S177 S178 S179 S180 S181 S182 S183 S184 S185 S186 S187 S188 S189 S190 S191 S192 S193 S194 S195
collisions: S082 S083 S084 S085 S086 S087 S088 S089 S090 S091 S092 S093 S094 S095 S096 S097 S098 S099 S100 S101 S102 S103 S104 S105 S106 S107 S108 S109 S110 S111 S112 S113 S114 S115 S116 S117 S118 S119 S120 S121 S122 S123 S124 S125 S126 S127 S128 S129 S130 S131 S132 S133 S134 S135 S136 S137 S138 S139 S140 S141 S142 S143 S144 S145 S146 S147 S148 S149 S150 S151 S152 S153
```
Only still-unimplemented considerthese proposal selected: **CT-20261026-4**, independent CJK quote check per daily review, carried as a lesson pointer without credit; its required outside independence/cadence cannot be supplied by our seats. The initial lesson reference to already-implemented CT-20261026-3 is explicitly corrected by its appendix (Draft08).

Open operator questions unchanged: chousa round29/41/42 fetch-scope, round43 register staleness, and round62 SKILL-size threshold. No approval inferred; no L0 append this round.

## Trend verdicts

- **expansion: unchanged** — one narrow depth entry, not a demonstrated new province surface/capability; no staged adoption, no capability or scalar increase.
- **quality: improved narrowly** — actual G02 defect classes fixed, initial glob false positive corrected, full lane preflight restored to 8/8 and historical v2 battery passes twice; the frozen targets still fail. QUALITY criteria cite retained failures rather than unobserved fixes.
- **discernment: unchanged** — errata and attacks are recorded; fresh outside non-author admit/reject judgment remains pending. No dispatched seat is promoted to that role.

No lasting regression observed in the enumerated old-v2/full-lane checks; not a universal no-harm claim. **Round admission withheld** for all three missed frozen targets; progression stops for outside closure.

## SHONEN

- [~] Decision tables/error patterns/checklists/sources: `SKILL.md` Decision table, Error patterns, Checklist and Gates; author assertion only.
- [~] End-to-end work executed/logged: `LOG.md` Round64; revision-bound final measurements and wave results; no non-author verifier claimed.
- [~] Executable without oral context: `corpus/evidence/round64/measure-after.py`, explicit commands/child exits in `controls/measurement-summary.json`; historical gates retained.
- [~] Province accuracy/no bleed: `PROVINCE.md` unchanged; `w1/ConnectScope/report.md`; no sibling write or scope absorption. Await outside verifier.
