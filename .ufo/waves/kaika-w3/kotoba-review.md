# kaika W3 — non-author verification: kotoba round 46

Reviewer: W3ReviewKotoba (non-author; fresh dispatch). Lane head `04192c252` (landing `f2f9ee1`), base `78ee57e5e`. Verdicts below are recommendations for the orchestrator.

**Recommendation: ADMIT, with the corrections in §8.** C1 verifies (improved; score held at 9). C2 and C3 verify as `improved-bounded` (scores held at 8.5). No claim is falsified, no axis is harmed on re-measurement, and provenance, append-only, census and credential checks are clean. The defects are conformance errors, one overstated repair, and one residual false-red door. None is a false green.

Setup: `git clone --shared` canonical trees at both commits under `/tmp/kaika-verify/kotoba/canon/{base,land}` (fleet entries symlinked). Frozen HOME `/tmp/kaika-verify/kotoba/home` = `cp -a` of `~/.omp/agent/sessions` (1298 `*.jsonl`). Lane worktree was not written (`git status --porcelain | wc -l` → 0).

## 1. Provenance — PASS
`git log --format='%h %an <%ae> | %cn <%ce> | %s' 78ee57e5e..04192c252`
- `f2f9ee1 kotoba-shokunin <kotoba@shokunin.local> | kotoba-shokunin <kotoba@shokunin.local> | round-46: land r46 …`
- `04192c2 kotoba-shokunin <kotoba@shokunin.local> | kotoba-shokunin <kotoba@shokunin.local> | round-46: landing pin …`

## 2. Append-only — PASS for scoped paths
`git diff --numstat 78ee57e5e..04192c252 -- LOG.md corpus/lessons corpus/QUALITY.md corpus/knowledge/harness-independent-round41-census.md`
- `LOG.md` 17 insertions / 0 deletions. `corpus/QUALITY.md` 33/0 (new file). `corpus/lessons/round-46.md` 81/0 (new file). `census.md` 8/0.
- Deleted or modified prior lines in the scoped paths: **0**.
- `corpus/SOURCES.md` is a new file (87/0), so no prior row can have changed. Status/recheck/used-by cannot be audited as "in place" changes because there was no prior version.

Out-of-scope observations (reported, not scoped by check 2):
- `SCORECARD.md` 22/3. Three rows (depth, operability, calibration) were prefixed with new segments. Scripted check: each removed old line survives as a suffix of its new row (`True` ×3).
- `SHONEN.md` 4/42. Regeneration is protocol-mandated (`PROTOCOL.md:417`, "regenerates `SHONEN.md` verbatim from the template"). Canonical form holds: 12 lines, 4 boxes, all `[~]`.
- `verifiers/*` floor and baseline edits, intentional and in step with the 328→330 move.

## 3. Claims — counting commands re-run at both commits

### C1 depth — **verified (improved on registered payload); recommend score HOLD at 9, not 9.5**
Command: `python3 -B c1_runner.py --worktree <tree> --scratch <s> --comparator <cmp> --source {frozen|committed|worktree} --arm {planted-relative|absolute-control} [--committed-source <base cmp>]`. This is the lane's `c1/runner.py` with `SNAPSHOT_HOME` repointed to my frozen HOME and `receipts/` pre-created (see D-4).

| arm | comparator (at) | comparator exit | stderr class | receipt scope sha | enforced sha |
|---|---|---|---|---|---|
| planted-relative | frozen `1101213a` (before) | **0** | receipt-notice | `3d8500ed` (honest) | `aa62e813` (planted superset) |
| planted-relative | `ccf41c23` (78ee57e) | **2** | `laundering` | — | — |
| planted-relative | `778b367e` (04192c2) | **2** | `laundering` | — | — |
| absolute-control | `ccf41c23` (78ee57e) | **0** | receipt-notice | `aa62e813` = enforced | `aa62e813` |
| absolute-control | `778b367e` (04192c2) | **0** | receipt-notice | `c335b8e8` = enforced | `c335b8e8` |

- Honest join (`r46_l1_matrix.py`, honest-control case), base and land: exit 0; `total 24, protocol 24, strict 20, adjudicated 4, scoped-out 4, disagree 0`.
- `--self-test`: base `0 failure(s) over 328 assertions`; land `0 failure(s) over 330 assertions`.
- Floors: `battery.sh` floors on base 9/9 at 328; on land 9/9 at 330; both exit 0.
- Caveat: the planted file's sha depends on the scratch carrier path, so the report's `886b1393` cannot be reproduced byte-for-byte from a different scratch. The attested-vs-enforced split and the exits reproduce.
- Not re-run: critic probe P1 (symlinked relative `--cwd`), cited from the seat report.

### C2 operability — **verified as `improved-bounded`; recommend score HOLD at 8.5**
Command: `HOME=/tmp/kaika-verify/kotoba/home python3 -B <tree>/.ufo/round-46/evidence/w2/l1-matrix/r46_l1_matrix.py` (run at each tree; the base tree receives the landing matrix file as a scratch copy because the file does not exist at 78ee57e).

| arm | frozen `055d3b9` | `ccf41c23` (78ee57e) | `778b367e` (04192c2) |
|---|---|---|---|
| honest-current-producer-control | 0 | 0 (24/24) | 0 (24/24) |
| live-mode-row-shadow-vs-mirror | 0 | **2** `live mode shadow` | **2** |
| live-summary-path-shadow | 0 | **2** `live summary shadow` | **2** |
| live-nonstring-verdict | 0 | **2** `live verdict shadow` | **2** |
| live-same-id-mode-duplicate | 0 | **2** `live mode shadow` | **2** |
| raw-nested-duplicate-value | 0 | **2** `duplicate JSON member 'nested'` | **2** |
| live-summary-and-mirror-optout (surviving) | 0 | 0 | 0 |
| scopeout-committed-reason-fabricated-observable | 2 | 2 | 2 |

Seat arms via `c2/run_c2.py` (inputs = the matrix's honest-control captures; scope = committed file). Frozen 0 → base 2 → land 2 for `raw-duplicate-top-level-results` (`duplicate JSON member 'results'`) and `raw-duplicate-record-rederived` (`'re_derived'`). The seat's own source captures lived in `/tmp/kotoba-r46-c2b`, outside the tree, so these arms are not re-runnable from committed evidence (D-4).

MED-3 false-red repro (`.ufo/round-46/evidence/w2/l1-matrix/med3/` plus two variants I built):

| input | frozen | 78ee57e (`ccf41c23`) | 04192c2 (`778b367e`) |
|---|---|---|---|
| clean payload | 0 | 0 | 0 |
| duplicate fragment **ahead** of payload (`live-prose`) | 0 | **2** (new false red) | **0** (repaired) |
| fragment ahead + payload + trailing non-object prose | 0 | 2 | 0 |
| duplicate **inside** payload (`live-dupsel`) | 1 | 2 | 2 (class-named) |
| trailing prose, no braces | 0 | 0 | 0 |
| payload then non-results object `{"x":1}` | 2 | 2 | 2 (`payload is not a results list`) |
| payload then duplicate object `{"a":1,"a":2}` | 2 | 2 | 2 |

Verdict: C2 verifies as `improved-bounded` (six registered arms 0→2; honest 24/24 unchanged). The landing repairs leading-prose duplicates only. Trailing prose objects remain a false red on all three comparators (D-2).

### C3 calibration — **verified as `improved` as registered, class `improved-bounded`; recommend score HOLD at 8.5**
Same matrix run, scope-out arms:

| arm | frozen | 78ee57e | 04192c2 | class at 04192c2 |
|---|---|---|---|---|
| scopeout-reason-evidence-drift | 0 | 2 | 2 | `scope reason drift` / `scope evidence drift` |
| scopeout-committed-reason-fabricated-target | 0 | 2 | 2 | `scope evidence drift` (matrix stderr) |
| scopeout-false-record-probe-shadow | 0 | 2 | 2 | `scope probe channel split` |
| scopeout-committed-reason-fabricated-observable | 2 | 2 | 2 | pre-existing reject |
| honest control | 0 | 0 | 0 | 24/24 |

Surviving shapes not re-run: record-level `kind` drift (critic P5), payload-selectable committed scope-outs (reviewer HIGH-2). The mirror opt-out survives and I re-confirmed it (C2 table).

### Gate battery (`battery.sh`, both canonical trees)

| gate | 78ee57e (base) | 04192c2 (land) |
|---|---|---|
| checklist | exit 1, 9 PASS / 1 FAIL `governance.citation_resolves` @ `LOG.md:2111` | same; 9 PASS / 1 FAIL |
| corpus-integrity | exit 0, 9/9 | exit 0, 9/9 |
| corpus-independent | exit 0 | exit 0 |
| surfaces | exit 1, stdout sha `8432070a` | exit 1, stdout sha `8432070a` (byte-identical) |
| pins | exit 1, stdout sha `16e71a19` | exit 1, stdout sha `16e71a19` (byte-identical) |
| floors | exit 0, `compare_harness_independent 328` | exit 0, `compare_harness_independent 330`; 9/9 exact |

No gate moved red at landing. The red gates are the same as at base.

## 4. SOURCES — PASS
- `bash …/sources-census.sh validate <lane>` → `kotoba-shokunin	ok	…/corpus/SOURCES.md`, **exit 0**.
- Contract census: `rows 11`; `malformed 0`; `tier A=10 C=1`; `status mined=4 queued=6 rejected=1`; duplicate ids none; enum/tier-inflation none; mined used-by missing none.
- Re-opened rows (six; I used `_read`/`_grep` on live pages on 2026-10-19):
  - **S006** (new tier-A, queued) RFC 8259 §4: "The names within an object SHOULD be unique." Found.
  - **S007** (new tier-A, queued) Python json, Standard Compliance: "Repeated names within an object are accepted, and only the value of the last name-value pair is used." Found, line 575–576.
  - **S008** (mined) YAML 1.2.2 §7.3.3: "Plain scalars must never contain the “: ” and “ #” character combinations." Found, line 3326.
  - **S002** (mined) client guide, Lenient validation: "Name doesn't match the parent directory name → warn, load anyway." Found, line 134; "Skill files authored for other clients may contain technically invalid YAML…" found, line 121.
  - **S003** (mined) Claude best-practices: "Cannot contain XML tags" (name and description bullets). Found. "Keep SKILL.md body under 500 lines" found.
  - **S011** (rejected, C) Agentman: "must match the parent folder name exactly or the skill will not load" Found. Its "avoid angle brackets … from the spec" line is attributed to the spec; the spec (agentskills.io/specification) contains no "angle", "bracket" or "XML" text (`_grep`, the only hits are `<`/`>` glyphs). The rejection's cross-check holds.
- Gate-table quotes in the lesson match these locations. The `accessed_utc` `18:40Z` labels are disclosed as local time mislabelled `Z` (lesson § Gate). I did not correct them.

## 5. Discernment spot-check (LEARNING.md) — table

| sample | gate decision | reviewer verdict | reason |
|---|---|---|---|
| S003 (Claude best-practices, mined → SKILL.md) | admit | **agree** | Quoted rule present at the cited section; the portability-floor paragraph rests on it. |
| S006 (RFC 8259 §4, queued, tier A) | admit (row) | **agree** | Normative SHOULD and the "unpredictable" paragraph are present; scope matches the comparator's duplicate check. |
| S011 (Agentman, rejected C) | reject | **agree** | Its name-mismatch claim contradicts S002 (warn and load); its spec attribution is false (spec has no angle-bracket rule). |
| knowledge entry admitted this round | — | **n/a** | Zero knowledge entries admitted (lesson § Gate; `corpus/knowledge/` file count 35 at both 78ee57e and 04192c2). The admit sample is therefore a registry row, not a knowledge entry. |

## 6. New knowledge entries — PASS (none new)
- No new `corpus/knowledge/*.md` file (35 at both commits).
- The appended § Round 46 landing in `harness-independent-round41-census.md` carries the old header trio (`source:` / `verified-at:` / `recheck:`).
- `recheck:` runner `.ufo/round-45/drafts/v10/post-r44-hunt.py` does not exist (`test -e` → exit 1). The lane discloses this and appends a correction. The focused replacement recheck (`r46_l1_matrix.py`) runs, and its numbers match the appended text. Q04 is still not met by this entry's header line (D-5).

## 7. Credentials — PASS
- Contract grep: `git diff 78ee57e5e..04192c252 | grep -nE 'op://[A-Za-z0-9]|BEGIN [A-Z ]*PRIVATE KEY|ghp_[A-Za-z0-9]{20,}|AKIA[0-9A-Z]{16}|xox[baprs]-[A-Za-z0-9]'` → no output.
- Broader keyword sweep (`op://|secret|password|api[_-]?key|Bearer |sk-[A-Za-z0-9]{10,}`) on added lines → no output. A looser `token|session=` pattern hit 53 added lines. I did not inspect those 53 line by line; they are prose and evidence paths, not credential-shaped strings.

## 8. Report — PASS for structure; one defect
`/home/vgpnk/Projects/shokunin/.tower/worktrees/kaika/fleet-ledger/.ufo/reports/round-46/kotoba.md` exists. It has, in order: Work performed (names C1–C3), Landed changes, Before → after measurements, SHONEN, Sources & frontier, Mistakes, Trend verdicts, L0 questions, Integrator notes. It cites `f2f9ee1` and `04192c2`. It has no `[x]` mark (only `[~]`). Fleet-root strays named in Integrator notes are absent now (`ls` of the patterns → none).

## Per-axis verdicts (recommended)

| axis | lane score | this round | recommended |
|---|---|---|---|
| depth (owned) | 9 | C1 measured improved | **9 (hold)**; 9.5 not granted |
| operability (advisory) | 8.5 | C2 improved-bounded | **8.5 (hold)** |
| calibration (advisory) | 8.5 | C3 improved-bounded | **8.5 (hold)** |
| consistency (calibration sub-axis) | 10 | no claim | unchanged |
| coverage | 8.5 | no claim | unchanged |
| freshness | 8 | no claim (surfaces 5/7, pins 1/3 identical to base) | unchanged |
| adjacency | 8.0 | no claim | unchanged |

## Trend verdicts (LEARNING.md)
- **Expansion: unchanged (agree).** No knowledge entries admitted; SOURCES rows are registry, not expansion (contract rule 4).
- **Quality: unchanged (agree).** The census entry is marked by append (not left unmarked), but its header `recheck:` stays dead, and no entry was strengthened.
- **Discernment: unchanged, leaning toward improved, not there yet.** Row-level spot-check agrees on 2/2 (S003 admit, S006 admit, S011 reject). Against that: Q13 and Q14 are grounded in M6 and M2, which do not show the missing-count-command or negative-sweep classes; and the lane's own SKILL.md front door violates Q08 at landing (D-3).

## Defects by severity

**HIGH** — none.

**MEDIUM**
- **D-1. Printed C1 counting command does not run.** Report § Before → after: `PYTHONDONTWRITEBYTECODE=1 python3 -B .ufo/round-46/evidence/w2/c1/runner.py`. Verified: exit 2, argparse "the following arguments are required: --worktree, --comparator, --source, --arm". The contract requires a pasteable counting command. Fix: print the full argv set (the summary holds it).
- **D-2. "Prose false-red repaired" overstated; a residual false red remains.** Any balanced JSON object after the payload is selected as the payload and exits 2 on frozen, 78ee57e and 04192c2 alike (`payload is not a results list` or `duplicate JSON member`). This is pre-existing and not a regression, but Q18 says "prose around the payload" must stay green. Fix: add trailing-prose arms, or record this as an open door.
- **D-3. The lane's SKILL.md front door violates the rule it adds.** `SKILL.md` line 14 (inside the frontmatter that ends at line 16) carries the literal `<skills>` token in `description:`. The same commit adds the portability floor ("no XML tags") and QUALITY Q08 ("no XML tag inside `description:`"). Disclosed as a planned r47 repair, but the criterion fails on the shipped file at landing.

**LOW**
- **D-4. Counting inputs not self-contained.** `c1/runner.py` exits 2 ("receipt path unwritable") on a fresh scratch because it does not create `receipts/`. It hard-codes `/var/tmp/kotoba-r46-home`, which the report says was deleted. The C2 seat runner's source captures live in `/tmp/kotoba-r46-c2b`, outside the tree. The planted-file sha also depends on the scratch path.
- **D-5. Census entry recheck dead.** `recheck:` points at `.ufo/round-45/drafts/v10/post-r44-hunt.py`, which does not exist. Disclosed by appended correction, but Q04 ("every recheck resolves") fails for this entry.
- **D-6. Lesson § Gate count wrong.** "admitted as rows: 10 (9 `queued` A-tier, incl. 2 own-work)". Actual: 11 rows; queued 6, mined 4, rejected 1.
- **D-7. S009 scope mismatch.** Scope says "at the round-46 landing commit"; anchor and quote are `78ee57e` / 328 assertions; landing is 330.
- **D-8. Q13 and Q14 weakly grounded.** Both copy CORPUS.md rules. Their "grounded in" rows (M6, M2) do not show the count-command or negative-sweep classes. Discernment (LEARNING "a criterion added with no lesson behind it") is at risk.
- **D-9. Timestamp labels.** `accessed_utc` 18:40Z on S001–S008 is local time labelled Z. Disclosed; uncorrected.

## Residual risk and verification gaps
- Not re-run: critic P1 (C1), critic P5 and reviewer HIGH-2 (C3), the mirror opt-out beyond the matrix arm, and the 2 L0 questions (judgement, not counts).
- The matrix is host-dependent: `REAL_HOME_TARGET=/home/vgpnk/.omp/agent/sessions`. I ran it against a frozen snapshot of that tree, not the live one.
- `verify_surfaces` and `check_substrate_pins` depend on the installed omp binary; I re-ran them on the same host, and their outputs match the report.

## 9. Admit / reject recommendation
**ADMIT.** Record: C1 verified (improved; depth held 9); C2 verified as improved-bounded (operability held 8.5); C3 verified as improved as registered, class improved-bounded (calibration held 8.5). Require the lane to correct D-1, D-2 wording, D-3 and D-6 in its next round or as appended corrections, and to log D-2, D-3 and D-5 as open doors. None blocks admission: no claim is falsified and no axis is harmed.

## Checks for the orchestrator to re-run
`bash …/fleet-census/scripts/sources-census.sh validate <lane>` (exit 0); `git -C <lane> log --format='%h %an <%ae> | %cn <%ce> | %s' 78ee57e5e..04192c252`; `git -C <lane> diff --numstat 78ee57e5e..04192c252 -- LOG.md corpus/lessons corpus/QUALITY.md`; the C1 runner with full args (`--source worktree --arm planted-relative --committed-source <base cmp>`) and the L1 matrix at both commits.
