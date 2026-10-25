# mori — round 45 (attempt 2: documentary finish)

Lane repo `/home/vgpnk/Projects/shokunin/mori-shokunin`, branch `master`. Entering tip
(contract) `554ff416459c92f0dea9762f834a556df2990187`; round-44 closure tip `b1d7269f`.
Round work landed by attempt 1 at `3ad8faaa`, `18fd68b0`, `baabc9929f0f272f3a99cd0a7816a2cb35fda835`.
Attempt 2 added one LOG entry: **lane HEAD `12c89ea63491fcca0f46169d809740711d3d052e`**
(`jj-lane.sh` printed `landed 12c89ea6…`; `git ls-remote origin refs/heads/master` →
`12c89ea63491fcca0f46169d809740711d3d052e`).

**Attempt 1 refusal.** Attempt 1 (launched 07:31:38 -03) did the round's work and landed it. Its
session then died about 50 minutes in, before it filed this report, on a provider content-policy
refusal. Error text: `[openai-codex/gpt-6-luna] Codex error event: Invalid prompt: your prompt was flagged as potentially violating our usage policy`
(`.ufo/watchdog.log:1325`, `lane-dead-no-report mori round=45`). Attempt 2 follows the kagi r28
precedent: a safety refusal is never rephrased, rerouted or retried. So attempt 2 ran **no craft
work, no wave and no swarm**, and did not re-attempt whatever attempt 1 was doing when it was
refused. It read the landed bytes, re-ran each claim's committed counter, added a LOG entry and
filed this report.

## Work performed

Declared claims (frozen in `.ufo/waves/round-45/contract.md` before any seat scored them; three
distinct axes):

- **C1, operability (7):** the ledger gate stops being vacuous. A ledger must be
  revision-sensitive with distinct rows, and the three vacuity witnesses (`W-REVCONST`, `W-HEAD`,
  `W-DUP`) must be rejected.
- **C2, calibration (5, tied lowest):** the gate registry stops overstating. One audit reads all
  seven eight-cell tables in `SKILL.md`, attributes each path to the row that names it, rejects
  duplicate rows, requires a real `--selftest` argv branch, and reports `unregistered=0` over the
  39-member declared population.
- **C3, depth (5, tied lowest), assimilation:** the shokuknow level-naming theme. One admitted
  entry is grounded in S473, which this lane opened this round. Its row is `mined`, and its
  `used-by` names the entry. The census goes green without a `TMPDIR` override, and the README
  gains a coverage-map row.

Work items, by evidence:

- Frozen contract, wave-1 spec and dispatch, opened sources: commit `3ad8faaa`
  (`.ufo/waves/round-45/contract.md`, `w1-spec.json`, `w1-dispatch.json`). The contract's
  `Correction 1` (`contract.md:111-137`) was appended before any after-measurement, and it closes
  four holes `w1/CritContract.md` proved: `moved>=1`, `tables>=7`, `--entering-rev` novelty, and the
  freeze manifest.
- C1 instrument: `.ufo/waves/round-45/count-c1.py` (sha256 `5f2deea0…`), ledger `figures.tsv`
  (15 rows; 5 move, 10 carry `CONST=`), witnesses `fixtures/witnesses/w-{revconst,head,dup}.tsv`,
  and mutant `fixtures/mutants/count-c1.py`. All in commit `baabc992`.
- C2 instruments: auditor v2 `tools/mori-gate-registry.py` (sha256 `8b82ac99…`, 743 lines; commit
  `18fd68b0`), counter `count-c2.py` (`153423c4…`), write-scope fixture and runner
  (`fixtures/write-scope.json`, `write-scope-run.py`; commit `baabc992`). Commit `18fd68b0` also has
  the `SKILL.md` registry refresh (orphan rows, r45 rows, superseding r44 rows) and real `--selftest`
  branches in `tools/mori-disk-rate.py`, `mori-round41-calibration.py`, `mori-routed-r24.py`,
  `mori-routed-check.py`, `mori-round19-regressions.py` and `mori-silence-cases.sh`.
- C3: entry `corpus/knowledge/census-cgroup-levels-r45.md`, row `corpus/SOURCES.md:252` (S473), and
  the `corpus/README.md` map row, all in commit `18fd68b0`. Counter `count-c3.py` (`37fd7c24…`) and
  opened bytes `assimilation/opened/cgroup-v2.rst.src` are in commit `baabc992`.
- Lesson `corpus/lessons/round-45.md` (Sources, Gate, Quarantine, Renumber, mistakes M1–M11) and
  `corpus/QUALITY.md` criteria 120–122 (commit `18fd68b0`).
- Freeze manifest `evidence/freeze-r45.txt`, entering-tip controls `evidence/control-c{1,2,3}.txt`,
  round-44 witnesses `evidence/witness-r44*.txt`, and the census baseline
  `evidence/census-baseline.txt` (commit `baabc992`).
- Round-44 verifier spot-check routed defects (`corpus/lessons/round-44-verifier-spotcheck.md`):
  1. S472 was re-opened: HTTP 200, 61889 B, quote located (`evidence/s472-reopen-l1.txt`).
  2. C3's `TMPDIR` dependence is now a predicate failure (P-C3 item 3), and C3 measures `met` with
     `env -u TMPDIR` (below).
  3. Promoting the SHONEN boxes is operator-owned, so the boxes stay `[~]`.
- Attempt 2's own work:
  - Verified the freeze manifest at `baabc992`: `grep -v '^#' evidence/freeze-r45.txt | sha256sum -c`
    gave 29/29 OK, rc 0. The external census script digest `3fb72615…` matches.
  - Re-ran all three counters at `baabc992`, plus their selftests and the frozen counters at the
    entering tip (outputs below).
  - Ran the round-end census.
  - Ran the misroot sweep.
  - Wrote the LOG entry (`12c89ea6`).

## Landed changes

| commit | carries | LOG.md entry |
|---|---|---|
| `3ad8faaa` | frozen contract, wave-1 spec and dispatch, opened sources | `LOG.md` "Round 45 (L1 mori-r45; entry written by attempt 2…)" |
| `18fd68b0` | SKILL.md registry refresh, entry, row S473, README map row, QUALITY 120–122, lesson, auditor v2, six tool selftest branches | same entry |
| `baabc992` | counters, ledger, witnesses, mutants, write-scope fixture and runner, freeze manifest, evidence, 39 seat reports, swarm registry, assimilation scratch | same entry |
| `12c89ea6` | the LOG entry itself (attempt 2; `LOG.md` only) | it is the entry |

Attempt 1 wrote no LOG.md entry and no SCORECARD.md claim rows (`git diff b1d7269f baabc992 --
SCORECARD.md LOG.md` is empty). Attempt 2 wrote the LOG entry. **SCORECARD.md still lacks the
round-45 claim rows**, because that file is outside attempt 2's documentary scope. This is a
conformance defect, routed to the closure and round 46.

## Before → after measurements

All after-runs are attempt 2's, at `baabc9929f0f272f3a99cd0a7816a2cb35fda835`, with the frozen
instrument bytes (freeze manifest verified). `12c89ea6` changes only `LOG.md`, so it does not move
any counter input. The before rows are attempt 2's re-runs of the frozen counters at the entering
tip `554ff416459c92f0dea9762f834a556df2990187`. The committed controls
`evidence/control-c{1,2}.txt` ran pre-freeze counter digests (`d908aa9a…` and `e8ee29eb…`); they
print the same verdicts.

**C1, operability**

```
python3 .ufo/waves/round-45/count-c1.py <rev> --repo /home/vgpnk/Projects/shokunin/mori-shokunin \
  --ledger .ufo/waves/round-45/figures.tsv --other-rev 554ff416459c92f0dea9762f834a556df2990187 \
  --witness-dir .ufo/waves/round-45/fixtures/witnesses
```

- Before (rev and other-rev both `554ff416…`):
  `C1=unmet mismatches=? rows=0 … witnesses=3/3 witnesses_vacuous=3/3 failed=ledger_present`, rc=1.
  The fair before is in `w1/RevBeforeAfter.md` §2 and `w1/ExecWitnesses.md:120-127`: the
  **round-44** counter prints `C1=met mismatches=0` on all three witnesses, so it was vacuously
  green.
- After (`baabc992…`):
  `C1=met mismatches=0 rows=15 classes=checks,corpus,evidence,registry,wave floor_rows=12 floor_classes=4 rev=baabc9929f0f272f3a99cd0a7816a2cb35fda835 … other_rev=554ff416459c92f0dea9762f834a556df2990187 witnesses=3/3 witnesses_vacuous=3/3`,
  rc=0. It reports `revision_moves PASS (moved=5 floor=1)` and
  `const_cap PASS (const=10 cap=13 rows=15 …)`. The selftest
  `python3 .ufo/waves/round-45/count-c1.py --selftest` prints `C1_SELFTEST pass=16 fail=0`, rc=0.

**C2, calibration**

```
python3 .ufo/waves/round-45/count-c2.py <rev> --repo /home/vgpnk/Projects/shokunin/mori-shokunin
```

- Before (`554ff416…`):
  `C2=unmet tables=unmeasured registered=21 unregistered=14 no_selftest=1 duplicate=unmeasured wrong_row=unmeasured writescope_mismatch=0 mode=absent … mutant=absent checks_failed=auditor_v2,auditor_mode,population_members,tables,unregistered,no_selftest,duplicate,wrong_row,auditor_rc,mutant_present,mutant_kill`,
  rc=1.
- After (`baabc992…`):
  `C2=met tables=7 registered=39 unregistered=0 no_selftest=0 duplicate=0 wrong_row=0 writescope_mismatch=0 mode=population population_digest=2d1e9096f7622639f3bb45624ffee594caa81c05ee200c9a22323f86d4a9c056 population_members=39 auditor_selftest=pass=15/fail=0 mutant=killed`,
  rc=0. The selftest `count-c2.py --selftest` prints `C2_SELFTEST pass=14 fail=0`, and
  `tools/mori-gate-registry.py --selftest` prints `GATE_REGISTRY_SELFTEST pass=15 fail=0`.
- At the intermediate tip `18fd68b0`, before the counters were committed, the same counter measured
  `C2=unmet wrong_row=3` (`w1/RevBeforeAfter.md` §1). It is `met` only from `baabc992`.

**C3, depth (assimilation)**

```
env -u TMPDIR python3 .ufo/waves/round-45/count-c3.py <rev> \
  --entering-rev 554ff416459c92f0dea9762f834a556df2990187 \
  --entry corpus/knowledge/census-cgroup-levels-r45.md --row S473 \
  --repo /home/vgpnk/Projects/shokunin/mori-shokunin --root /home/vgpnk/Projects/shokunin
```

- Before (`554ff416…`): `C3=unmet rev=554ff416… entering=554ff416… entries=1 rows=S473 census_sha256=3fb72615…`,
  rc=1. `entry_present`, `rows_present` and `readme_row` fail.
- After (`baabc992…`):
  `C3=met rev=baabc9929f0f272f3a99cd0a7816a2cb35fda835 entering=554ff416459c92f0dea9762f834a556df2990187 entries=1 rows=S473 census_sha256=3fb7261569f46423dd80ecc23e0a23789a7926f667c7a3fc559d2439d4a64e30`,
  rc=0. It passes all eight checks, including `entering_absent` and
  `census_ok … PASS (exit=0)` with `TMPDIR` unset. The selftest prints `C3_SELFTEST pass=19 fail=0`.

**Axis harm: reported for the operator to rule on, not claimed absent.**

- `SKILL.md` registry cells quote instrument states that no longer exist at `baabc992`. The
  committed auditor reads tools, not cell tallies, so `C2=met` coexists with these false cells:
  - `:190`: `C1_SELFTEST pass=10` at `f80e75ac…`; measured `pass=16` at `5f2deea0…`.
  - `:191`: auditor `64db765e…`, 622 lines; measured `8b82ac99…`, 743 lines.
  - `:194`: `GATE_REGISTRY_SELFTEST pass=10`; measured 15.
  - `:184`: `pass=6`; measured 15.

  Attempt 2 checked these with `git show baabc992:SKILL.md | grep -noE '…SELFTEST pass=[0-9]+|64db765e60e3|f80e75ac7421|622 lines'`
  and `wc -l tools/mori-gate-registry.py` → 743. The finding first appeared at `18fd68b0` in
  `w1/CritAxisHarm.md` §1b. **This is a candidate calibration harm** (false self-description
  introduced this round), routed to round 46 as a re-pin.
- `.ufo/waves/round-44/figures.tsv` is inadmissible under the new C1 grammar. Attempt 2's re-run of
  `count-c1.py 554ff416… --ledger .ufo/waves/round-44/figures.tsv --other-rev 1429c791…` gives
  `C1=unmet … failed=revision_sensitivity`. The frozen round-44 counter still scores it `met`, and
  SCORECARD's round-44 pointer is not harmed (`w1/CritAxisHarm.md` item 2).

## Sources & frontier

- Rows before → after: **245 → 246**, from
  `git show <rev>:corpus/SOURCES.md | grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}'` at `554ff416` and
  `baabc992`.
- Rows added by tier: one tier-A `docs` row, **S473** (`corpus/SOURCES.md:252`; cgroup-v2.rst at
  Linux v7.2, opened 2026-10-25, quote located `:1474-1477, :1518-1519` per the lesson's Sources
  table), status `mined`, `used-by` names the entry.
- Rows touched old → new: none changed status. S472 was re-opened (200, quote present;
  `evidence/s472-reopen-l1.txt`), and its cells were not altered.
- Frontier rows advanced: **none**. The README row states its boundary as "no FR1 or FR12 advance".
- Census:
  - Round start: `sources-census.sh validate --root /home/vgpnk/Projects/shokunin mori` →
    `mori ok`, rc=0 (`evidence/census-baseline.txt:29-30`).
  - Round end (attempt 2, at lane tree `baabc992`): `mori ok`, rc=0, with 19 W04 duplicate-URL
    warnings only.
- Sourced claim: C3 rests on S473, opened this round.
- Mined mistakes: M1–M11 in `corpus/lessons/round-45.md` `## Mistakes`. For example, M1 is the
  round-44 auditor's under-read plus comment-credited `--selftest`. Captured-by is `none`, and the
  fix is P-C2 item 4, shown able to fail.
- **Assimilation (one theme: level naming):**
  - Admitted: 1 entry re-grounded in-round. It is the lane's own entry citing S473, not a staged
    file copied verbatim.
  - Rejected: `who-sets-the-scope-cap-r45.md` (own-work `file://` source, kumitate-owned subject);
    `cap-control-wording-r52.md` (a remediation argument, against PROVINCE "detection and report
    only"); staged `file://`-only rows S558 and S559. Reasons and flip conditions are in the
    lesson's `## Gate`.
  - Collision check: `assimilation/reg-ids` has 245 ids and `staged-ids` has 136, giving **2
    collisions, `S471` and `S472`** (`assimilation/collisions`). The renumber map is
    `assimilation/renumber-map.tsv`: 136 mapping rows, `S471→S474` … `S606→S609`, with S473
    reserved. It is unused because no staged row was appended.
  - Quarantine slice (3 rows, `assimilation/quarantine-slice`): S244 `quote-present` (arXiv PDF
    carrier); S262 `quote-present` (OpenAlex abstract); S268 `unverifiable`, which is not
    fabrication (measured 2026-10-25).
- considerthese: QUALITY 122 cites `considerthese/2026-10-24.md` proposal P24-3
  (`corpus/QUALITY.md:1013-1015`).

## Trend verdicts

These are the lane's own reading. The non-author closure is pending.

- **expansion — improved:** one new knowledge entry, one tier-A row (245 → 246), and one README map
  row; C3 is `met` at `baabc992`. No frontier row advanced.
- **quality — improved, with a disclosed harm candidate:**
  - The C1 and C2 instruments now reject the round-44 vacuity classes (witnesses 3/3; tables 7;
    population 39; `unregistered=0`).
  - However, four `SKILL.md` registry cells are false at `baabc992` (see Axis harm).
  - Lesson M3–M5 show that v2's `--selftest` rule still over-accepts a help string and a `--help`
    escape, and under-accepts a named-parameter branch.
- **discernment — unchanged:** the Gate records 1 admit, 2 entry rejects, 2 row rejects and 3
  quarantine verdicts, each with a reason. No non-author has spot-checked them yet, and the lesson
  explicitly does not claim LEARNING's `disagree` half.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources: seven
  eight-cell registry tables read at `baabc992` (`count-c2.py` → `tables=7 registered=39`), plus
  QUALITY 120–122 (`corpus/QUALITY.md:983-1015`). Four stale cells are disclosed above
  (`SKILL.md:184,190,191,194`).
- [~] At least one end-to-end domain task executed and logged in LOG.md: the C3 entry plus census
  run is logged with commands and verdicts in `LOG.md` "Round 45 …" at `12c89ea6`.
- [~] Instructions executable by an agent without oral context: every r45 instrument carries a
  `--selftest` (count-c1 16/0, count-c2 14/0, count-c3 19/0, gate registry 15/0, run by attempt 2),
  and each `SKILL.md` row names its entry and verdict map.
- [~] No cross-domain bleed (PROVINCE.md still accurate): both entry rejects cite the PROVINCE
  boundary and kumitate ownership (`corpus/lessons/round-45.md` `## Gate`). The admitted entry's
  README row says "no census change … no remediation".

## Report extras

- **Round shape: one v1 wave (wave 1, build plus first falsifiers). No wave 2.**
  - Wave 1: **37 seats** (`w1-spec.json` items = `w1-dispatch.json` `counts.spawn` = 37; policy
    band 32–64; `resumeSends` empty).
  - Role mix: executor 12, scout 6, scribe 5, reviewer 5, critic 3, mutation-tester 2, connector 1,
    sentinel 1, simplifier 1, revenger 1.
  - All 37 filed a report under `.ufo/waves/round-45/w1/`. The swarm registry has no per-member
    status field, so **dead seats: 0 observable** (no dispatched seat lacks a report).
  - Two more executor reports, `w1/ExecSelftestOrphans.md` and `w1/ExecSelftestRoutedR24.md`, call
    themselves "residual" seats. Neither appears in a committed spec or dispatch. The prompt's
    residual call allows ≤8 reviewer/critic seats, so two executors there are a shape deviation,
    recorded here.
  - **Round total in the committed evidence: 39 seats.**
  - No wave 2: attempt 1 died before dispatching one. Attempt 2 dispatched no swarm, because the
    refusal precedent forbids retrying the refused session's work and this attempt is documentary.
    The round therefore gets no wave-2 falsification credit.
- **Planner seat:** the L1 held the §3 planner seat. The bounded planning data-walk rode the scout
  item `PlanDataWalk` (`w1/PlanDataWalk.md`), and the connector item is `ScoutSiblings`.
- **Inherited state:** attempt 1 left the lane clean (`jj-lane.sh state` → `tracked=0 untracked=0`,
  `ahead=0`, local = remote = `baabc992`). Nothing uncommitted was inherited or discarded.
- **Misroot sweep** (`git -C /home/vgpnk/Projects/shokunin status --porcelain`, attempt 2): no
  mori round-45 file at the fleet root.
  - The untracked `s795.pdf s796.pdf s804.html s814.html s816.html s817.html s820.pdf` (mtimes
    08:21–08:22) contain zero `mori` bytes.
  - `.ufo/waves/round-24/` and `round-69/` belong to other lanes' rounds.
  - `w1/ExecMisroot.md` found zero seat misroots during the wave.
  - Copies 0, deletions 0.
- **Routed to round 46:**
  1. Re-pin `SKILL.md:184,190,191,194`.
  2. Add the round-45 SCORECARD.md claim rows and measured outcome.
  3. Key the `--selftest` rule on parser keys or `case` patterns (lesson M3–M5).
  4. Scrub `GIT_*` in selftests (M11).
  5. Make the round-44 ledger admissible or supersede it (CritAxisHarm item 2).
- **Stale-lane:** respawn-per-round driver; no other mission of this lane is open.
- **Open L0 questions:** none.
- **Tool installs:** none by attempt 2.
