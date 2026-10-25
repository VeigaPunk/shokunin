# kaika W3 — non-author verification: kaidoku round 12

Reviewer `W3ReviewKaidoku` (fresh orchestrator dispatch; not the lane's author). Round head `2a0d6c198` (= `2a0d6c19840dbc30728c2ca2a061e25c12ade8cb`), base `de77d7545`. Read-only: `git status --porcelain` in the lane worktree = 0 lines after review. Scratch under `/tmp/kaika-verify/kaidoku/` and `/var/tmp/kaika-verify/kaidoku/` (the entry's recheck requires TMPDIR under `/var/tmp`; deleted at end). No web access used (no SOURCES rows exist to re-open).

## 0. Recommendation

**ADMIT the three claims (C1 coverage, C2 depth, C3 operability) as measured-verified, with conditions.** Every declared counting command reproduces at `2a0d6c198`; the new Evidence-ID entry reproduces independently; the citation-drift probe is clean at head and at base; no axis is harmed at head. Literal check 4 **fails** (`sources-census.sh validate` exit 1, `missing corpus/SOURCES.md`; identical at base, no regression). Conditions (appended corrections, not a re-open): D1 ruling, D2 ruling, D3 and D4 disclosures/lesson Gate, D5 wording. SHONEN stays `[~]`; nothing here supports `[x]`.

## 1. Provenance — PASS

`git log --format='%h %an <%ae> | %cn <%ce> | %s' de77d7545..2a0d6c198` → 3 commits (`4072ebb`, `6a35398`, `2a0d6c198`), each `kaidoku-shokunin <kaidoku@shokunin.local>` as **both** author and committer.

## 2. Append-only — PASS (one in-place README edit noted)

`git diff --numstat de77d7545..2a0d6c198 -- LOG.md corpus/lessons corpus/QUALITY.md corpus/SOURCES.md` → `31 0 LOG.md`, `41 0 corpus/lessons/round-12.md` (new file), QUALITY.md absent from diff. `git diff -U0 ... | grep -nE '^-[^-]'` over those paths → no output (zero deleted or modified prior lines). `corpus/SOURCES.md` absent at both revisions (`git cat-file -e` → fatal), so no status/recheck/used-by cells exist to change.

Other files, numstat (`SCORECARD.md 95/0`, `SKILL.md 22/0`, `SHONEN.md 2/0`, `pointer-table.json 24/0`, `corpus/README.md 1/1`, `expected.json 1/1`): only additions except:
- `corpus/README.md:41` Evidence-model row rewritten in place ("three verb families" → "four", token added). Outside the append-only list; prose changed, not only appended. Minor (D7).
- `expected.json` sha pin re-pinned `1b3ab955…` → `7994eec7…` (by design: frozen-run guard).

## 3. Claims — VERIFIED by measurement

Commands: Command A = `SCORECARD.md:94-122` extracted from `2a0d6c198` and run with `REV=<rev>`; pointer count = `git show <rev>:.ufo/gates/citation-drift/pointer-table.json | python3 -c "…recheck…"` (report's command).

| claim | command | de77d7545 (base) | 2a0d6c198 (head) | report says | verdict |
|---|---|---|---|---|---|
| C1 coverage | Command A | knowledge 90, mapped 90, missing [], dangling [] | knowledge 91, mapped 91, missing [], dangling [] | 90→91 | **verified** |
| C2 depth | Command A | rule_blocks 16, citation_resolved 16, depth 10.0 | rule_blocks 17, citation_resolved 17, depth 10.0 | 16→17 | **verified** |
| C3 operability | pointer count | 0 (entries 57; sha256 `1b3ab955…`) | 3 (entries 60; sha256 `7994eec7…`) | 0→3 | **verified** |

Also at `6a35398` (same as head): Command A 91/91 and 17/17 (identical). Pointer-table sha256 recomputed: `git show 2a0d6c198:.ufo/gates/citation-drift/pointer-table.json | sha256sum` = `7994eec7e764e8c3195dd79efb850b63d437aa610e6a9d96ed24484bb53789d1` (matches `expected.json:12`).

Score effect (saturated proxies, same as before): coverage 10.0 → 10.0, depth 10.0 → 10.0 (Command A `coverage_score`/`depth_score` at both revisions). The claims verify on counts; the lane's card convention labels count moves at 10.0 as "improved" (precedent `SCORECARD.md:1961-1962`, `:2012`), so this is wording, not a defect (see D5).

## 4. SOURCES — NOT VERIFIED (literal); no regression

`bash …/fleet-census/scripts/sources-census.sh validate <worktree>` → exit **1**:
```
kaidoku	missing	/home/vgpnk/Projects/shokunin/.tower/worktrees/kaika/kaidoku-shokunin/corpus/SOURCES.md
```
Same command on the base tree (`git archive de77d7545`) → exit **1**, same `missing`. The census script reports all 20 lanes as `missing` at fleet level (`FLEET missing 20`). The round made no SOURCES capability claim (report `Sources & frontier`: "absent → absent"; contract v1 says a capability enters SCORECARD only if census is clean; `SCORECARD.md` `Planned:` line defers SOURCES to r13). Literal exit-0 cannot hold; ruling needed (D1).

Re-open of rows: **not possible** — zero rows exist (`FLEET rows 0`; no file). Substitute anchor re-opens (all against the pinned package at `/home/vgpnk/.npm/_npx/a1722018f28f9df2/node_modules/rea-agents`):
- `dist/domain/evidence.js:155-185` — `semanticProjection` = `{subject:{digest,format,architecture}, provider, …, locations, evidence_links}`; `computeEvidenceId = ev_ + digestCanonicalValue(semanticProjection(e), "Evidence")` — matches the entry's claim (`corpus/knowledge/…:11`), excludes subject `name`/`local_path`.
- `dist/application/go/GoBinaryService.js:50-80` — `parameters: input.data`, `normalized_result` = `report.data` with `artifact.path`, `locations: [{ kind: "artifact-path", path: value.artifact.path }, …]` — matches entry `:13`.
- `package-source-hashes.txt` vs `sha256sum` of the four files: all four identical (e.g. `evidence.js a3fb9f02…`, `canonicalDigest.js f46d6bd4…`, `GoBinaryService.js 5494185f…`, `GoBinaryProvider.js bdea4f88…`).

## 5. Discernment spot-check (LEARNING.md) — n=1 admit, n=1 reject

| sample | gate decision | my verdict | reason |
|---|---|---|---|
| ADMIT `corpus/knowledge/2026-10-19-arc3-r12-go-evidence-id-domain.md` | admitted (C1) | **agree** (content); caveat D2 on source form | Independently reproduced (§6): same-path repeat stable; copies path-distinct; display-only mutation no change; three-field substitution reproduces copy-a ID; single-field does not. |
| REJECT PL-4 substring-needle form of the C3 pin (`claims/c3/PL-4.md`, recommended by VZ-1:7) | rejected in favour of order-free lookaheads | **agree** | Counted `table1-rerun.md` (`awk` over the per-mutant table): old column killed 17 of 24 breaking, 0 of 9 harmless flagged; seven survivors named (`r7 …-legacy`, `round99`, `…-recheck-old`; `r10 round99`, `claims/c2`; `r11 /tmp`, `round99`). Full-line pin (tightened): 24/24 but 1/9 false alarm. Landed lookahead form (`lookahead-regex-check.py` rerun: 20/20 breaking, 0/12 harmless). Independent extra mutants (§5a): 5/5 breaking killed; 0/2 harmless flagged (one "double space" mutant was a no-op, excluded). |

§5a independent mutants (`/tmp/kaika-verify/kaidoku/indep.py`, needles from `2a0d6c198` pointer table): `REA 6.7.0→6.7.1` killed; `rederive-commands.txt→.txt.bak` killed; `rea-agents@6.7.0→-rc` killed; `identity.txt` mention removed killed; `expected id last hex char` killed; clause reorder (r10, r11) survived (harmless, correct).

## 6. New knowledge entry — headers present, recheck runs, claim matches

- Headers: `source:` line 3, `verified-at: 2026-10-19` line 5, `recheck:` line 7 — PASS.
- Recheck run (CLI `rea-agents@6.7.0`, `/usr/bin/docker` sha256 `70f68a77…f45c9`, `TMPDIR=/var/tmp/kaika-verify/kaidoku/tmp`, copies `cp -p`):
```
/usr/bin/docker                      -> ev_87621921fc54a38ee60f85c9f81a47508dcdebd1c6f70569ec78da3a3a055dcd (twice)
/var/tmp/.../copy-a/docker           -> ev_b2a3ff1ef849bdd31414a1b13108ae7e54a5ae9e85962f8b07a9d8d7870a9665
/var/tmp/.../copy-b/docker-copy      -> ev_6b8ab6a9cdb270a7b15da62ba6eb9d8b29c5c810921e7df324f2426c02dd89e5
```
  Repeat ID matches entry line 7/22 (`ev_87621921…055dcd`). Copy IDs differ from the lane's live copy IDs only because the copy paths differ (entry line 22: "differ … only because their paths differ"); path dependence confirmed.
- Recompute (`/tmp/kaika-verify/kaidoku/recompute.mjs`, using the package's own `digestCanonicalValue`): stored = recomputed for all three envelopes; display-only mutation (`subject.name`, `local_path`) → unchanged base ID; base with three path fields (`parameters.path`, `normalized_result.artifact.path`, `locations[0].path`) set to copy-a path → `ev_b2a3ff1e…` = copy-a stored ID; `parameters.path` alone → `ev_9ccfe35f…` (not the copy ID). This matches the entry's "field set, not sole causality" language (`:23`, `:26`).
- Reconcile: `node .ufo/waves/arc3-loop1-round12/integration/c1/reconcile-all-go-ids.mjs` (cwd worktree) → `records=27 matched=27 bundles=CR-1,CR-4,EX-2,EX-4,EX-5,EX-6,EX-8`, exit 0.
- Lane's "live" envelopes not re-run by me (they are in the repo; the recheck above is the independent run).
- Entry `source:` line names repo-relative bundles that exist at head (`git ls-tree -r --name-only 2a0d6c198 -- …/CR-4/evidence` → 12 files incl. `base-1.json`, `copy-a.json`, `calls.txt`, `package-source-hashes.txt`).
- QUALITY (`corpus/QUALITY.md`, 15 criteria at head): lane's `integration/c1/quality-check.md` says 15/15 PASS. I agree with criteria 4, 5, 6, 8, 14, 15 on the text. Criterion 1 is met only in the lane's reading (repo paths accepted). See D2.
- Custody: the live legs behind `integration/c1/live-*.json` ran without a pre-pair (lesson `round-12.md` row 3). The entry does not say so (grep `custody|pre-pair|unpaired` → 0 hits in entry). The ID claims do not depend on custody (recomputed); a zero-drift claim is not made. See D4.

## 7. Credentials — PASS

`git diff de77d7545..2a0d6c198 | grep -nE 'op://[A-Za-z0-9]|BEGIN [A-Z ]*PRIVATE KEY|ghp_[A-Za-z0-9]{20,}|AKIA[0-9A-Z]{16}|xox[baprs]-[A-Za-z0-9]'` → no output (exit 1).

## 8. Instruments (re-run; all at `2a0d6c198` in a worktree or `git archive` tree)

- `citation-drift-probe.py --root <wt> --rev 2a0d6c198 … --strict` → `clean findings=0 exit=0`.
- same at `--rev de77d7545` → `clean findings=0 exit=0`.
- same at `--rev 4072ebb` → `failed findings=5 exit=1` (lesson #9 reproduced; fix `6a35398` is the repair).
- `citation-drift-probe.py --selftest` → `13/13 passed`.
- `c1-census-v10.py --root <wt>` (head and base) → `VERDICT: PASS (0/0/0/0)`, exit 0.
- `custody-pair.py verify config-post-only.txt config-post-only-2.txt` → `CUSTODY_PAIR_VERIFY: CONTENT-DRIFT paths=4/5 drift=1 exit=10`; drift on `/home/vgpnk/.bashrc` only (`moved=sha256`).
- `custody-pair.py selftest` → `CLEAN cases=28 passed=28`.
- Receipts: `sha256sum -c` not run; `sha256sum config-post-only.txt` = `528b038c…` (matches sidecar read).
- Lesson Gate greps: `grep -c 'remains pending' …arc3-r11…md` → 1 (matches #5); verdict count `claims/verdicts/*.md` → 11 (matches #6); `c1-census-v10.py:629` `ap.add_argument("--root", default="/home/vgpnk/Projects/shokunin/kaidoku-shokunin")` (matches #10).
- `PROVINCE.md` `wc -l` → 162; PROVINCE diff vs base empty.

## 9. Report — PASS on sections; cites commit

`/home/vgpnk/Projects/shokunin/.tower/worktrees/kaika/fleet-ledger/.ufo/reports/round-12/kaidoku.md` has Work performed, Landed changes, Before→after, SHONEN, Sources & frontier, Mistakes, Trend verdicts, L0 questions, Integrator notes. `grep -n '\[x\]'` → none. Commit `2a0d6c1` cited 5×. Claims named at the top of Work performed. Unverifiable from repo: the 10-member batched swarm and verbatim godspeed bytes (transcripts not in repo) — verification gap, not a finding.

## Per-axis verdicts (recommended; lane card owns coverage, depth, calibration; operability is fleet-owned per frozen claims)

| axis | lane score | this round | recommended verdict |
|---|---|---|---|
| coverage | 10.0 → 10.0 | C1 verified (90→91, mapped 91/91) | **verified; score unchanged (saturated)**; not harmed |
| depth | 10.0 → 10.0 | C2 verified (16→17, 17/17) | **verified; score unchanged (saturated)**; not harmed |
| calibration | 10 → 10 | no claim; discernment spot-check agrees (§5) | unchanged; not harmed |
| operability (fleet) | not in owned table | C3 verified (0→3; probe clean; seeds 3/3) | verified; fleet axis, no lane score |
| freshness | not in owned table | no claim; live recheck re-derived stored id (§6) | unchanged; not harmed |
| adjacency | not in owned table | PROVINCE untouched (diff empty, 162) | unchanged; not harmed |

Stagnation nudge applies (SCORECARD round-12 saturation note; all owned proxies 10.0; no capability since arc2-r8). The round finished the frozen claims as steered; the lane's Planned r13 honours the nudge. No axis harmed at head.

## Trend verdicts (LEARNING.md rules)

- **Expansion: improved** (LEARNING reading: one admitted entry on uncovered ground, citing its map row, `corpus/README.md:41`). Caveat: contract v1 rule 4 counts only entries whose `source:` cites a `mined` SOURCES row; under that definition the count is 0 (D2).
- **Quality: unchanged.** LEARNING's `improved` needs a stale or weaker entry re-verified, deepened, or superseded with no failure. No existing entry was re-run (reconcile covers only round-12 seat bundles; C3 grades recheck text, does not run it). The report's "improved" rests on the new entry's own QUALITY pass, which is an admission gate, not a trend move.
- **Discernment: improved (narrow).** LEARNING's `improved` includes "the spot-check agrees with the gate on admits *and* rejects" — met by §5 on n=1+1. The second clause (a disagreement → QUALITY criterion) is not met: zero criteria added (D3 context).

## Defects by severity

**Major (ruling needed)**
- **D1 — check 4 literal fail.** `sources-census.sh validate` exit 1 (`missing corpus/SOURCES.md`), identical at base. The round made no SOURCES claim, so this is a planning-state finding, not a regression. Orchestrator should rule: N/A for this round, or fail. Recommended: N/A, record in the report.
- **D2 — C1 entry `source:` form.** Prompt §6.4 says each expansion entry "opens with `source:` (its `S###` row, URL, anchor)"; contract v1 rule 4 counts only `mined` rows. The entry's `source:` is a repo-path bundle list and package paths; no S### row; no URL. The frozen C1 claim is `coverage (owned)` and the round classifies the entry as C1, not campaign expansion. Orchestrator must rule whether this entry counts as expansion under contract v1 (I recommend: it counts as coverage under the frozen claim; it does not count under contract v1 expansion until a `mined` row exists).

**Moderate**
- **D3 — lesson `## Gate` incomplete vs LEARNING.** LEARNING requires `corpus/lessons/round-N.md` `## Gate` to carry "candidates considered, admitted, rejected (with reasons), and the spot-check result." `corpus/lessons/round-12.md:27-41` gates mistake rows #1–#10 only; no candidate admit/reject list (C1: Go vs path-free `search_bytes`, VZ-1:32; C3: PL-4 vs final lookahead form; C2: EX-16 wording) and no spot-check result (this review's §5). Fix: append a `## Gate (candidates and spot-check)` section; do not edit prior lines.
- **D4 — custody SOP breach not stated in the entry.** `SKILL.md:328-329`: "Freeze the pre-pair before the round's first probe — no probe runs on an unpaired round." The live legs behind the C1 entry ran unpaired (lesson row 3). The round discloses this in the lesson and SCORECARD round section, not in the entry. The ID claims survive (recomputed §6); the config-drift claim is not made. Fix: append one disclosure line to the entry.

**Minor**
- **D5 — wording.** Round table and Before→after mark coverage/depth/operability "improved" at saturated 10.0 → 10.0. Lane convention (`SCORECARD.md:1961-1962`, `:2012`) uses the same wording, so this is house style. Recommend a parenthetical "(score unchanged, saturated)".
- **D6 — instrument trap (disclosed).** `c1-census-v10.py:629` default `--root` = lane main checkout. Bare worktree runs grade the wrong tree. Lane-owned; disclosed in Integrator notes; not fixed. Gate-owner follow-up.
- **D7 — in-place README edit.** `corpus/README.md:41` changed "three verb families" → "four" and added a token in the same row. Not in the append-only list; the report says "token on the Evidence-model row" but not that prose changed. Minor.
- **D8 — frozen C3 text vs landing.** Frozen C3 says "seats never write the instrument" and "lands as a patch TEXT". The integrator (L1) wrote `pointer-table.json` and `expected.json` directly. This is the integrator, not a seat, so not a breach; noted for completeness.

**Info / verification gaps**
- Swarm composition (10 members, one batched call, verbatim godspeed bytes) not verifiable from repo.
- `~/.bashrc` change at 21:46:35Z: operator-side; verified only that the custody tool flags `.bashrc` drift.
- Recheck run needed `/var/tmp` scratch (deviation from my `/tmp` scratch rule, required by the entry's own recheck text).
- Lookahead mutant matrix is the lane's; my 5/5 + 0/2 independent set is small.

## Admit / reject recommendation

- **C1, C2, C3: ADMIT as measured-verified.** Counts reproduce at head; no axis harmed at head.
- Conditions before the round is closed (appended corrections, no rewrites): D1 ruling; D2 ruling; D3 lesson Gate append; D4 disclosure line on the C1 entry. D5–D7 optional.
- Do **not** mark SHONEN `[x]`; no named non-author verifier is closed by this review beyond the recommendation itself, which is a recommendation, not an admission.

## Commands (reproduce)

```
git -C <wt> log --format='%h %an <%ae> | %cn <%ce> | %s' de77d7545..2a0d6c198
git -C <wt> diff --numstat de77d7545..2a0d6c198 -- LOG.md corpus/lessons corpus/QUALITY.md corpus/SOURCES.md
git -C <wt> diff -U0 de77d7545..2a0d6c198 -- LOG.md corpus/lessons corpus/QUALITY.md | grep -nE '^-[^-]'   # empty
REV=<rev> python3 /tmp/kaika-verify/kaidoku/commandA.py   # extracted from SCORECARD.md:94-122 @2a0d6c198
bash …/fleet-census/scripts/sources-census.sh validate <wt>   # exit 1 (missing SOURCES), base exit 1
python3 <wt>/.ufo/gates/citation-drift/citation-drift-probe.py --root <wt> --rev <rev> --table … --expected … --strict
node <wt>/.ufo/waves/arc3-loop1-round12/integration/c1/reconcile-all-go-ids.mjs   # records=27 matched=27
TMPDIR=/var/tmp/kaika-verify/kaidoku/tmp node <rea>/scripts/rea.mjs inspect-go-binary <path> --format json --full-output
python3 <wt>/.ufo/waves/arc3-loop1-round12/integration/mutation/lookahead-regex-check.py   # 20/20, 0/12
python3 <wt>/.ufo/gates/custody-pair/custody-pair.py verify <receipt-a> <receipt-b>   # CONTENT-DRIFT paths=4/5 drift=1
```
