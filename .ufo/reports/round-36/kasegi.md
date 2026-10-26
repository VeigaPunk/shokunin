# kasegi — round 36 report (2026-10-26)

Lane: `kasegi-shokunin` (bounty & security research; axes depth + coverage). Lane base `cc692008b0cfd58d18275aa6c4aed79620120799`; claims-freeze `b47f2cdf17d9f6021cbdb4db1add09a9dbf4f1d6`; final lane commit `a23dc4788aa7c98831eed6db953434034ce5ae8d` (pushed; `git ls-remote origin refs/heads/master` prints it). Measured content head `274fa9ae908db5800013778098f4d426281b46e2` (ancestor of the final lane hash). Stale-lane: respawn-per-round driver; no other mission of this lane open. Attempt 1 (no earlier `lane-dead-no-report kasegi round=36` line in watchdog.log).

## Work performed

The round declares **two claims**, frozen before dispatch in `.ufo/waves/round-36/claims.json`:

- **C1 — depth:verifiability (score 4, held):** `corpus/instruments/r36-closure.sh` — export-mode-only closure counter (`--export-ref <hash>`; plain run refused exit 2) with nine checks E1–E9 closing the round-35 verifier spot-check's routed defects plus the standing closure-order defects (quiescence, head-binding, exact-basename registration, false-evidence-line correction). It prints `closed=9/9 exit=0` on the round-36 final lane head, `--selftest` prints `cases=9 failures=0`, the round-35 base export prints `closed=0/9 exit=1` and the round-35 judged head export prints `closed=3/9 exit=1`.
- **C2 — coverage (score 7, held):** Frontier F19 admitted 18→19 (FIRST EPSS — exploitation-likelihood scoring, a 0–1 probability, distinct from CVSS severity and KEV catalog status); registry row S053 (tier A, mined, opened 2026-10-26); knowledge entry `corpus/knowledge/epss-exploit-prediction-scoring.md` cites `source: S053`; harness `entries=22 pass=22 exit=0` incl. `PASS F19 … ids=S053`; `source-recheck S053` exit 0; census exit 0; knowledge 47→48; junk twin `c2-controls/junk-f19.md` rejected.

**Wave.** One v2 wave `kasegi-r36-build`, 64 seats, dispatched via the inline spawn handoff (`wave1.ready` → `wave1.ready.dispatched`): executor 18, scribe 12, reviewer 10, critic 6, scout 6, mutation-tester 5, connector 3, sentinel 2, simplifier 2 — attack roles 23/64 = 35.9 %. The L1 held the planner seat (orchestrator ruling 2026-10-19); the planning data-walk rode `ScoutDatawalk`. Receipts under `.ufo/waves/round-36/wave1/`. **At filing, the dispatcher's `wave1-results.json` is not yet finalised** (late seat writes continued through integration; receipt count 60/64 and two seats' scratch dirs were swept before the final gate run) — WAVE-DONE for this wave was still pending; this is recorded as an open item, not a claim outcome.

**Work items by area** (evidence under `.ufo/waves/round-36/wave1/`):

- **C1 build/attack** — `ExecC1SuiteBuild` (suite draft, pinned digest `4db1ae70…`), `ExecC1Fixtures`, `ExecC1ExportMode`, `ExecC1BaseFail` (negatives), `RevC1Suite`, `RevC1Fixtures`, `RevC1Selftest`, `CritC1Kill` (attack matrix: 30 probes; three post-integration kill-rule-hit classes disclosed), `MutC1Suite`, `MutC1Fixtures`, `SimplC1`, `ExecQuiescenceProbe`, `ExecAncestry`, `ExecDatawalk`, `ExecGateReviewPrep`.
- **C2 build/attack** — `ExecC2Capture` (S053.txt + manifest), `ScribeEntryF19` (entry), `ScribeRowS053` (row/bullet/Paths), `ExecC2Harness` (four instruments on the proposed tree), `ExecC2JunkControl` (junk twin), `ExecC2QuoteOnce`, `RevEntryF19` (ADMIT + three landing touch-ups), `RevRowS053`, `RevSourceRecheck`, `RevHarnessSync`, `CritC2Kill`, `CritC2Claim`, `MutC2Entry`, `MutC2Row`, `MutJunkTwin`, `ScoutF19Open`, `ScoutCaptureAvailability`, `ScoutF19Sibling`, `ConnSibling`, `ExecSiblingSweep`.
- **Non-claim frontier items** — `ScoutIdCollisions` + `ScribeAssimilationGate` (assimilation: none), `ScoutQuarantine` (slice verdicts), `ScoutStandingRefusals`, `ScribeQualityRows` (R28/R29), `ScribeMistakes` (M36-1..4), `ScribeConsiderthese`, `ScribeScorecard`, `ScribeShonen`, `ScribeLOG`, `ScribeSOURCSCorrection` (R9 M35-6 fix), `SentScope`, `SentSecrets`, `CritBoundary`, `SimplReport`.

## Landed changes

Every change is tied to the round-36 `LOG.md` entry (heading `## Round 36`) and to the lane commits:

| Change | Commit |
|---|---|
| Claims freeze + before controls + census-before | `b47f2cdf` |
| Integration core: `corpus/instruments/r36-closure.sh`, capture `S053.txt`+`manifest.json`, entry `epss-exploit-prediction-scoring.md`, `SOURCES.md` S053 row/search-log/Paths/R9 correction, `knowledge-expected.txt` 48, `README.md` F19 row, PROVINCE F18+F19 amendments, QUALITY R28/R29, SKILL Gates & probes registry (r35+r36 exact basenames), junk `c2-controls/junk-f19.md`, LOG/SHONEN/lesson/scorecard drafts | `caa314625` |
| Wave evidence: spec/dispatch/ready + seat receipts | `e666d902` |
| E1 `Final lane commit:` line, E4 provenance note, lesson hash | `2c26a97e` |
| Late seat receipt updates | `e9c57c43`, `274fa9ae` |
| Final gate receipts + measured closure block | `a23dc478` (final lane head) |

## Before → after measurements

### C1 — depth:verifiability (measured at `274fa9ae…`)

| counter (frozen command) | before | after |
|---|---|---|
| `bash corpus/instruments/r36-closure.sh --export-ref <final>` | suite absent (`ls_exit=2`) | **`closed=9/9 exit=0`** |
| `… --selftest` | absent | **`cases=9 failures=0`** exit 0 |
| `… --export-ref 3266c993…` (r35 base) | — | `closed=0/9 exit=1` |
| `… --export-ref 0aee0ef…` (r35 judged head) | — | `closed=3/9 exit=1` |
| `grep -cF 'r35-defect-closure.sh' SKILL.md` / `r36-closure.sh` | 0 / 0 | 1 / 1 (registry rows) |
| `grep -cF 'filled by the L1' SCORECARD.md` | 0 | 0 |

Do-nothing control: untouched base export scores `closed=0/9` (target unreachable without landing). Suite header binds `lane=` and `suite-sha256=4db1ae70…` to the output line.

### C2 — coverage, F19 / S053 (measured at `274fa9ae…`)

| counter (frozen command) | before | after |
|---|---|---|
| `grep -cE '^\| F[0-9]+ \|' corpus/README.md` | 18 | **19** (F19 row) |
| `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md` | 52 | **53** (S053 row) |
| `grep -cE '^\|[[:space:]]*S053[[:space:]]*\|' corpus/SOURCES.md` | 0 | 1 |
| `grep -rlE '^source: S053 ' corpus/knowledge \| wc -l` | 0 | 1 |
| `ls corpus/knowledge/*.md \| wc -l` | 47 | 48 |
| `python3 corpus/instruments/frontier-recheck-count.py` | `entries=21 pass=21 exit=0` | **`entries=22 pass=22 exit=0`** incl. `PASS F19 … ids=S053` |
| `python3 corpus/instruments/source-recheck.py --manifest …/round-36/manifest.json --source S053` | manifest absent, exit 2 | exit 0, `sha256 OK` + Q1–Q4 `occurrences=1` (anchors 216/217/217/235) |
| `python3 corpus/instruments/recheck-audit.py` | `strict pass=47/47 expected=47` | `strict pass=48/48 … expected=48 missing=0 unexpected=0` exit 0 |
| `python3 corpus/instruments/capture-binding-check.py` | records=42 bound=42 | `records=43 bound=43 unbound=0` exit 0 |
| `scripts/sources-census.sh validate --root … kasegi` | exit 0, W04 S028/S029 | exit 0, W04 S028/S029 |
| junk twin `c2-controls/junk-f19.md` | absent | committed; fabricated sentence `grep -cF` = 0, pinned comparison `MISMATCH reason=quote-not-found` exit 1 |

## Sources & frontier

`corpus/SOURCES.md` before → after: **52 → 53 rows**. Rows added by tier: **1 × A** (S053 — FIRST EPSS documentation page, kind docs, tier A scoped to FIRST's own EPSS statements, status mined, opened 2026-10-26, recheck 90d, used-by `corpus/knowledge/epss-exploit-prediction-scoring.md`, anchor pinned to the round-36 capture). Tier histogram after: A 50 / B 1 / C 2. Rows touched old→new: none (no status/recheck/used-by cell changed on any pre-existing row); an R9 appended correction fixes the round-35 S052 Search-log bullet's digest abbreviation and row count (M35-6). Frontier rows advanced: **F18 → F19**. Search log: round-36 FIRST EPSS bullet appended. Assimilation: **none adopted** — id-collision rerun registry 52 × staged 94 → 22 standing collisions (S031–S052; guard load-bearing and fail-closed; 23 predicted once S053 lands against the staged S053, which is a different document); quarantine slice 7 rows, 0 adopted (1 present-and-located duplicate S040; 2 absent quote-form; 4 unreachable); seven standing staged-entry refusals unchanged.

## Trend verdicts

- **expansion: improved** — one admitted knowledge entry on ground the coverage map did not hold (exploitation-likelihood scoring vs severity S001/S002 and exploitation-status S052 ground), frontier 18→19, registry 52→53 at tier A, entry cites mined `source: S053`, harness 22/22. No capability row (capability window not restarted; last entry round 33).
- **quality: improved** — the round-35 verifier's routed defects are closed by a fail-closed export-bound counter (base 0/9 → 9/9 at the final head, selftest 9/9, negative judged-head 3/9); the round-35 lesson's false evidence line class is corrected (E8, M36-2); exact-basename registration closes the r35 D3 near-name literal gap (E3, M36-3, R29); recheck-audit strict 48/48; anchorcheck 0 bad; no admitted entry failed its re-check (S053 re-opened live, byte-identical).
- **discernment: improved** — the gate admitted F19/S053 after a reviewer REFUSE→repair→ADMIT cycle, rejected the junk twin by the counter it was built to fool, kept assimilation closed on measured collision/quarantine grounds, and recorded the round-36 lesson's disagreement with the round-35 Gate (M36-2) plus the score-gap (24/47 gated) as the calibration evidence.

## SHONEN

- [~] SKILL.md decision tables/error patterns/checklists/cited sources — Gates & probes registry rows for `r35-defect-closure.sh` and `r36-closure.sh` (exact basenames), anchorcheck 0 bad (`SHONEN.md` round-36 box 1).
- [~] End-to-end domain task executed and logged — none new; closest executed measurement: F19 live capture + source-recheck S053 + r36 closure suite (`SHONEN.md` round-36 box 2).
- [~] Instructions executable without oral context — recheck-audit 48/48, harness 22/22, r36 suite 9/9 on export, census exit 0 (`SHONEN.md` round-36 box 3).
- [~] No cross-domain bleed — PROVINCE amended with F18/F19; sibling sweep over 20 lanes zero EPSS ground, uncontested (`SHONEN.md` round-36 box 4).

**Tooling:** no installs/upgrades; no pacman transactions (host-wide pause). **Open L0:** kasegi round-15 (PROVINCE re-point), round-16 (second root loss), round-32 (re-dispatch vs L1-only landing) remain open; none blocks this round.

**Open item:** the dispatcher's `wave1-results.json` for wave `kasegi-r36-build` was not finalised at filing (two late seats were still writing); seat receipts 60/64 committed. ScribeGateLesson and SimplReport receipts landed after the integration commit and are included in the final lane commits.
