# kotodama — round 96 report (hyaku run 15, attempt 1)

Lane: kotodama (linguistic-cultural worldbuilding). Lane repo `/home/vgpnk/Projects/shokunin/kotodama-shokunin`.
Lane HEAD at landing: `16c4759241cbe8687394657feb1d08ad4eff659f` (branch `main`; round commit `66d2e915bcff0a6de70d958f4174bc2677b5bb40`; raw-capture commit `16c47592…`). `git ls-remote origin refs/heads/main` → `16c4759241cbe8687394657feb1d08ad4eff659f`.
Base `0539276c0e329743200b60e98bf289c540f78864`. Freeze `deca7e6fff988061f01bfc501a91e18fca892822`. Before-prediction correction `063f70c9ab9aed5297741773292ded6d713d537a` (made before any seat ran).

## Work performed

Declared claims (`reports/round-96/claims.json`, 2 claims, distinct axes, causally separable):

- **Claim O — operability** (successor grader move v6 → v8; closes the round-95 routed survivors). Target: battery96 `survivors=0 unnamed=0 refused=24`, selftest ≥144, mutation96 killed == total ≥95 with 0 survived, REG identical. Lowest-axis note: freshness is the historically lowest non-retired axis and remains paused by L0 round-11/round-89 (`.ufo/l0-questions.md` lines 47, 303; no ANSWER); this round moves no freshness claim, and the lowest-axis obligation is neither met nor waived.
- **Claim C — coverage** (sourced frontier → core entry on oath, blessing and curse formulae; zero owned knowledge file at base). Target: entry + ≥3 new tier A|B rows opened 2026-11-05, all cited and captured, census and index rc 0.

Work items (wave `w1`, 12 seats, one v1 wave; spec `.ufo/waves/round-96/w1-spec.json`, dispatch `w1-dispatch.json`, results `w1-results.json`; each seat's report is `.ufo/waves/round-96/w1/<Seat>.md` and its stage is `.ufo/waves/round-96/w1/stage/<Seat>/`):

1. Freeze: counter `reports/round-96/predispatch.py` and do-nothing control `reports/round-96/predispatch-base.txt` — `PREDISPATCH-96: FAIL legs=3/12` (`LEG O0 FAIL` sha equals v6; `O1 FAIL 134/134 < 144`; `C1 FAIL entry absent`; `C2 FAIL rows=898 highest=S974`; guard legs C3–C5 pass by construction). Evidence: freeze commit `deca7e6f`.
2. ExecBattery96 — battery96 built from battery95 plus nine CriticO95 classes, F1 and the benign ZWNJ1/G0 controls; control over the frozen v6 bytes: `BATTERY-SUMMARY survivors=9 unnamed=0 refused=15 traceback=0 clean=2` (`.ufo/waves/round-96/w1/stage/ExecBattery96/control-v6.txt`); sha pin `reports/round-96/controls/battery96.sha256` = `9f80f594…21c`.
3. ExecGraderV7 — v7 (sha `2e28a289…053ec`): battery96 `survivors=0 refused=24`, selftest `145/145` (`stage/ExecGraderV7/battery-v7.txt`, `selftest.txt`).
4. MutationTester96 (attack) — `mutants96.py`, first measured on v7: `MUTATION-SCORE: 109/112 killed, 3 survived` (`stage/MutationTester96/mutation-score-v7.txt`): `fs-u001d-off`, `fs-u001e-off` (U+001D/U+001E unpinned), `id-lookalike-refuse-off` (shadowed duplicate branch). Red-before on v6: `95/112 killed, 17 broken-pattern` (`mutation-red-before-v6.txt`).
5. Repair (L1, same claim, v8 `f29ab0139b4590fa8da7232a7372574675ef60763c475eea003006eb1dbcd9c0`): pins FS2/FS3 added to the round-96 pin block; the duplicate ID1 branch (formerly v7 lines 335–345) deleted; the mutant whose target was deleted retired from `mutants96.py` (pre-retire copy `mutants96.py.pre-retire`, sha256 of the retired driver `84ee57cb…a08f2`). Re-measured: selftest `147/147` rc 0 (`reports/round-96/predispatch-lands.txt` leg O1); battery96 `24/24` refused (leg O2); mutation `111/111` killed, 0 survived, 0 broken-pattern (leg O3); REG 34/34 identical (leg O4).
6. CriticO96 (attack) — against v7: `CRITIC-O96 survivors=7 unnamed=0 refused=12 traceback=0` (v6: `survivors=11 refused=8`); the seven v7 survivors are CR1, US1, OGH1, IS1, NUL1, CM1, CMW2 (`stage/CriticO96/attacks.md`). Not a claim-O failure (predicate is battery96); routed to round 97. Not re-run on v8.
7. ScoutSurface96 — zero owned file at base (`grep` sweep, rc 1 on term set); adjacency map and planner data-walk (`stage/ScoutSurface96/surface.md`).
8. ScoutSources96 — 11 candidates opened by plain curl, located quotes recounted (`stage/ScoutSources96/candidates.{md,json}`, captures under `stage/ScoutSources96/captures/`); reject list R11–R31 with reasons.
9. ConnectorOverlap96 — 20 adjacent owners checked; contested-scope items routed (`stage/ConnectorOverlap96/overlap.md`).
10. ExecRegistry96 — the only registry writer: re-verified each candidate, assigned S975–S984, dropped C4 (fresh HTTP 404, `dropped.md`), append-only (`append-only.txt`: added=10 removed=0), census rc 0 (`census.txt`), evidence files and `reports/round-96/evidence/manifest.json`.
11. ScribeEntry96 — drafted `corpus/knowledge/linguistics/oath-blessing-curse-formulae.md`; first draft cited derived ids before the registry landed; re-keyed to the landed ids (see lesson R96-M4); self-check `stage/ScribeEntry96/self-check.txt`; README patch `README.new.md`/`README.diff`, applied by the L1 (four edits only, `git apply --check` rc 0).
12. CriticC96 (attack) — claim C survives: 14 of 4891 distinct 8-grams shared with `myth-symbol/binding-speech-complex.md` (0.29%), 0 copy-scale overlap, quotes count 1, census rc 0, `stage/CriticC96/critic.md`.
13. ReviewerThrenoi96 (non-author re-decision, frontier mistake) — round-95's access reject of Thrênoi to Moirológia did not hold (both URLs HTTP 200 on attempt 1; PDF 302080 B); content ADMIT-AS-CANDIDATE (tier A) for the professional-mourner facet; nominated, not written (`stage/ReviewerThrenoi96/decision.md`).
14. ReviewerC96 (attack, claim C) — **dead seat**: ended after a bounded wait with no DONE marker and no verdict (last text: "Still blocked on the DONE markers — continuing the wait"). Not substituted by a new seat; the L1 ran the frozen counter on the landed tree (`reports/round-96/predispatch-lands.txt`, PASS 12/12), and CriticC96 recounted the quotes and ids.

Lesson `corpus/lessons/round-96.md` records the mistakes, Gate rows and routed items; LOG entry `LOG.md` (round 96). The L1 ran the counter, the census, the integrity checks and the commits. Seats wrote only their stage files and the single files their items named, and committed nothing.

Round shape and seat mix: one v1 wave, 12 spawn seats, 0 resume, 0 residual calls (round total 12 seats). Roles: executor 3 (ExecBattery96, ExecGraderV7, ExecRegistry96), mutation-tester 1, critic 2 (CriticO96, CriticC96), scout 2, connector 1, scribe 1, reviewer 2 (ReviewerC96 dead, ReviewerThrenoi96). Attack seats 5/12 = 42% (≥25%). Planner: the canonical L2 planner is held by the L1 (validator refuses planner as a swarm role); the planning data-walk rode ScoutSurface96 and ConnectorOverlap96 (routed defect R4 of round 95 answered by this mapping). Dead seats: ReviewerC96 (above). Wave dispatch was deferred by host disk pressure (see Routing and holds) and the wave spawned at 17:42:59 -03.

Verification gates run by the L1 after the wave: frozen counter `predispatch.py` on the landed tree (12/12 PASS); census `sources-census.sh validate --root … kotodama` rc 0 at start and end (`.ufo/waves/round-96/census/census-start.txt`, `census-end.txt`); `tools/check-corpus-index.py` rc 0 (268/268/0, inside the counter); the grader's own selftest and battery96 (inside the counter).

Routed round-95 defects (from `corpus/lessons/round-95-verifier-spotcheck.md` §5):
- R1 (Thrênoi reject) — re-opened, decided, and the mistake is mined (R96-M1); criterion 38 added. Registry row not written (nominated).
- R2 (untracked `reports/round-95/census-head.txt`) — committed in the freeze commit `deca7e6f`.
- R3 (stale-lane grade) — see Stale-lane below.
- R4 (planner seat) — mapping recorded above.
- R5 (lowest-axis obligation) — stated above; freshness still paused by L0.
- R6 (before-value on exact set) — claim O's before is measured on the exact battery96 set (control `control-v6.txt`, survivors=9 refused=15), not on a predicted 88/95 set.

## Landed changes

| change | file(s) | LOG entry | commit |
|---|---|---|---|
| freeze of claims O and C, counter, do-nothing control, census-start, round-95 census-head receipt (R2) | `reports/round-96/claims.json`, `predispatch.py`, `predispatch-base.txt`, `.ufo/waves/round-96/census/census-start.txt`, `reports/round-95/census-head.txt` | round 96 | `deca7e6f` |
| claim-O before-prediction correction (pre-data) | `reports/round-96/claims.json` | round 96 | `063f70c9` |
| claim O: grader v8 (pins FS2/FS3; duplicate ID1 branch deleted) | `tools/check-advance-evidence.py` | round 96 | `66d2e915` |
| claim C: entry | `corpus/knowledge/linguistics/oath-blessing-curse-formulae.md` | round 96 | `66d2e915` |
| claim C: 10 registry rows (S975–S984), 0 removed | `corpus/SOURCES.md` | round 96 | `66d2e915` |
| claim C: index row, totals and footer (ScoutSurface96 recipe) | `corpus/README.md` | round 96 | `66d2e915` |
| frontier: criterion 38 (access rejects need retry evidence) | `corpus/QUALITY.md` | round 96 | `66d2e915` |
| lesson, scorecard, log | `corpus/lessons/round-96.md`, `SCORECARD.md`, `LOG.md` | round 96 | `66d2e915` |
| evidence: battery96 and its control, reg, mutation receipts, captures, manifest, predispatch-lands | `reports/round-96/**`, `.ufo/waves/round-96/**` | round 96 | `66d2e915` |
| raw capture bytes named by `raw_sha256` (the directory commit skipped files over 1 MiB) | `reports/round-96/evidence/S976.raw.pdf`, `S984.raw.html`, `.ufo/waves/round-96/w1/stage/ScoutSources96/captures/{C11.raw.html,C2.raw.pdf,rejected/R20-gutenberg-il.html}` | round 96 | `16c47592` |

Fleet side: `L0` line appended to `.ufo/l0-questions.md` (host disk pressure). Report committed by `fleet-commit.sh --as kotodama` (see Landing below).

## Before → after measurements

Counting command for all legs (frozen counter, paste-able): `python3 -B reports/round-96/predispatch.py --root <lane> --work <scratch> --base-rev 0539276c0e329743200b60e98bf289c540f78864`.

| claim | leg | before (base `0539276c`, control) | after (landed `16c47592`, tool v8 `f29ab013…`) |
|---|---|---|---|
| O | O0 tool sha ≠ v6 | FAIL (sha `f7981ba2…` = v6) | PASS (`f29ab013…`) |
| O | O1 selftest | FAIL 134/134 < 144 | PASS 147/147 |
| O | O2 battery96 | FAIL driver missing; over v6 measured survivors=9 refused=15 | PASS survivors=0 unnamed=0 refused=24 |
| O | O3 mutation96 | FAIL driver missing; v6 red-before 95/112 + 17 broken | PASS 111/111 killed, 0 survived (v7 first landing: 109/112 — FAIL, see lesson) |
| O | O4 REG | FAIL no output | PASS 34/34 byte-identical |
| C | C1 entry | FAIL absent | PASS 30143 B, 11 h2, table 19×5, 6/6 phrases, topic equal |
| C | C2 registry | FAIL 898 rows, highest S974, 0 qualifying | PASS 908 rows, highest S984, 10 qualifying |
| C | C3 append-only | PASS (guard, base) | PASS added=10 removed=0 |
| C | C4 census | PASS rc 0 (guard) | PASS rc 0 (`census-end.txt`) |
| C | C5 index | PASS rc 0 (guard, 267 files) | PASS 268/268/0 |
| C | C6 ids cited | FAIL | PASS 10/10 |
| C | C7 captures | FAIL | PASS 10/10 |

Measured on commit: landed tree `16c4759241cbe8687394657feb1d08ad4eff659f` (tool v8). Counter output: `reports/round-96/predispatch-lands.txt` (`PREDISPATCH-96: PASS legs=12/12`). Note: the counter's O2/O3 legs were run from the stage drivers pinned at freeze; the v7 first-landing O3 result (109/112) is recorded, not hidden.

**Honest verdict on claim O.** The frozen predicate is met on the landed bytes (v8). The first landed grader (v7) did not meet O3; the repair is in the same claim and is disclosed as such. The kill rule says a leg failing at the lands measurement fails the claim as declared; the lands measurement that counts is v8, and this is a choice the non-author closure should rule on. The retired mutant is disclosed; the mutation predicate itself was not changed.

## Sources & frontier

- `corpus/SOURCES.md` rows before → after: 898 → 908 (`grep -c -E '^ {0,3}\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`; base via `git show 0539276c…:corpus/SOURCES.md`). Highest id S974 → S984. Removed lines 0 (`append-only.txt`).
- Rows added by tier: A 5 (S975, S976, S977, S982, S983); B 5 (S978, S979, S980, S981, S984); C 0. Status `mined`, opened `2026-11-05`, recheck `180d`, used-by the entry path.
- Rows touched old→new: none (append-only).
- Dropped candidate: C4 (fresh HTTP 404, quote count 0; `dropped.md`).
- Rows nominated, not written: Thrênoi to Moirológia PDF (tier A; `ReviewerThrenoi96` §5).
- Census: `sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotodama` rc 0 at start (`census-start.txt`) and at end (`census-end.txt`).
- Frontier rows advanced: the oath, blessing and curse surface (Known gaps has no entry for it; `corpus/README.md` index now lists the entry under `## linguistics/ (41)`).
- Sourced claim: claim C cites S975–S984 (opened 2026-11-05 by the L1's and the seats' plain curl, `-L`, `--max-time 30`; HTTP 200 for all ten).
- Assimilation: none — `considerthese/` does not exist in this lane; shokuknow `merge/kotodama/` was not adopted (quarantine-first slice not re-run this round).
- Mined mistakes: R96-M1 (access reject without retry; criterion 38) and R96-M2…M5 in `corpus/lessons/round-96.md` `## Mistakes`.

## Trend verdicts

- **expansion: improved.** A coverage surface with zero owned file at base now has an entry (30143 B) and ten registry rows (5 tier A, 5 tier B), census rc 0. Evidence: counter C1–C7; `census-end.txt`.
- **quality: unchanged.** No admitted entry was re-verified, deepened or superseded. The grader gained refusals (claim O) and criterion 38 was added to `QUALITY.md`; the quality of existing knowledge is not measured by any leg this round. Evidence: `git diff --stat 0539276c… 16c47592… -- corpus/knowledge` (new file only).
- **discernment: improved.** One reject reason (Thrênoi, round 95) was shown wrong by a measured re-open (HTTP 200 on attempt 1), the mistake is mined, and criterion 38 is shown able to fail on the round-95 record (lesson, `QUALITY.md` criterion 38). Not a non-author verdict; the closure should check it.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — the new entry carries a decision procedure, error patterns and a checklist with ten cited sources (`corpus/knowledge/linguistics/oath-blessing-curse-formulae.md`); SKILL.md itself not changed this round. Pointer: `corpus/lessons/round-96.md` `## Gate`.
- [~] At least one end-to-end domain task executed and logged in LOG.md — round 96 wave: scouting, sourcing, entry drafting, registry landing, counter and census, logged in `LOG.md` (round 96). Pointer: `.ufo/waves/round-96/w1/`, `LOG.md`.
- [~] Instructions executable by an agent without oral context — frozen counter `reports/round-96/predispatch.py` PASS 12/12 on the landed tree; grader selftest 147/147. Pointer: `reports/round-96/predispatch-lands.txt`.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — overlap with the adjacent `binding-speech-complex.md` is 0.29% (14 of 4891 8-grams) and is routed as a duplicate-authority item, not absorbed. Pointer: `.ufo/waves/round-96/w1/stage/CriticC96/critic.md` §2; `ConnectorOverlap96/overlap.md`.

No box is `[x]`: no non-author verifier has checked these boxes yet; promotion is operator-owned.

## Stale-lane

Open missions for this lane: none beyond round 96 (respawn-per-round driver). Progressing: this round (landed). Silent: none.

## Tool installs

None. `pdftotext`/`pdfinfo` (poppler 26.10.0) were already present and used by ReviewerThrenoi96. No pacman transaction (paused host-wide). RULES.md read (operator 2026-10-19).

## Routing and holds

- Host disk pressure: `/fast` was 100% (2.3 GB free) at 17:28 -03; the dispatcher deferred the wave (`disk-defer`, `cap-defer`) until it dropped to 49% at 17:52. The L1 appended the L0 question (`.ufo/l0-questions.md`, kotodama round-96 line: which tenant should free space; whether the operator raises the dispatch soft threshold). Not cleaned by this lane. Open.
- Host sysctls: no seat changed them (round-95 incident in `.ufo/` is not repeated).
- Other lanes' scratch: a kake seat reported an `rm -rf` of its parent scratch; this lane's `kotodama-r96` tree survived (checked by ScribeEntry96).
- Fleet-root untracked `w4lines.txt` (numeric lines, not this lane's): left untouched; not committed.
- L0 open: freshness pause (`.ufo/l0-questions.md` lines 47, 303); ideophones overlap (line 356).

## Landing

Lane: `jj-lane.sh commit … --as kotodama` landed `66d2e915bcff0a6de70d958f4174bc2677b5bb40` and `16c4759241cbe8687394657feb1d08ad4eff659f`; `ls-remote origin refs/heads/main` prints `16c4759241cbe8687394657feb1d08ad4eff659f`. Report: `fleet-commit.sh --as kotodama` (this file and the L0 line).

## Misroot sweep

`git -C /home/vgpnk/Projects/shokunin status --porcelain` at report time: `.scratch/*` and `.ufo/l0-questions.md` (modified, orchestrator and other lanes), `w4lines.txt` (untracked, not this lane's). No round-96 seat file was found at the fleet root; nothing was copied or deleted.
