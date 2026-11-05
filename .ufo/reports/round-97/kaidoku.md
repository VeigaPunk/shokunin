# kaidoku — round 97 report (attempt 1)

Lane repo `/home/vgpnk/Projects/shokunin/kaidoku-shokunin`, branch `main`. Lane HEAD pushed: `b30bb749359d48160a0e29b0fd6614ed7f8b8ac4` (`git ls-remote origin refs/heads/main` prints the same hash; `jj-lane.sh state` shows `ahead=0 behind=0`). Freeze commit `e859a88d78567c44bc1ecfd211afe123755ae1c7`; landing commit `867ed98d85f45a18265441c1760386ef353b3d43`. Round lesson `corpus/lessons/round-97.md`; LOG entry `LOG.md` `## 2026-11-05 — round 97`; SCORECARD section `## 2026-11-05 — round 97`.

## Work performed

**Declared claims (2, distinct axes, both on tied-lowest axes).**
- **R97-C1 — calibration, measured.** A receipt's pins are the bytes at the revision it names; `met_target` typed; counts allow-listed; the receipt write durable; the kill rule re-reads its own receipt; a crash is not a kill. **Verdict: NOT ADMITTED.** The frozen predicate is met literally, but the public path is harmed (see below).
- **R97-C2 — depth, measured.** Craft block 36 names the receipt-byte-binding class and the depth stack refuses the round-96 false-green classes. **Verdict: verified on the frozen predicate.**

**Work items (evidence pointers).**
- Protocol load and round-96 read: `skill://shokunin`, canonical SKILL/PROTOCOL/MISSION/AXES/CORPUS/LEARNING, lane SKILL/PROVINCE/SCORECARD/QUALITY/README, `corpus/lessons/round-96.md`, `corpus/lessons/round-96-verifier-spotcheck.md` (§6 routes adopted).
- Claims and freeze: `plans/round-97-claims.md`; pins `.ufo/waves/round-97/pins.sha256` (59 entries, `sha256sum -c` 59/59 OK at L by ReviewerScope); commit `e859a88d`.
- Instruments (frozen at F): `tools/round-97/stop-boundary-repair-battery-v7.py` (verifier and writer), `tools/round-97/kill-rule-v3.py` (command A), `tools/round-97/craft-citation-v2.py`, `tools/round-97/depth-blocks-v4.py`, `tools/round-97/gen-forgery-fixtures.py`; `.ufo/waves/round-97/mutants.json` (21 real mutants + M0), `mutants-before-noc1.json`, `forgery/` (13 fixtures), `manifests/`, `c2-fixtures/`.
- Before-side receipts: `.ufo/waves/round-97/pre/` (see caveat M97-q below: measured on the base commit plus uncommitted round-97 instruments, not a clean checkout).
- Landing (L): `SKILL.md:810-819` craft block 36; `corpus/QUALITY.md:335-337` rows 195–196; `corpus/SOURCES.md:238-239` S322 (admit) and S323 (reject); `corpus/knowledge/2026-11-05-r97-receipt-byte-binding.md`; `corpus/README.md:277` row.
- Bookkeeping (B): `corpus/QUALITY.md:339` row 197 (supersedes row 195's binding clause, corrects row 196's N9 citation); `corpus/lessons/round-97.md`; SCORECARD and LOG entries; `.ufo/waves/round-97/l1/` (landing receipts and public-path runs under `l1/public/`).
- Measurements: R97-C1 command A at L: `.ufo/waves/round-97/l1/scores/c1-at-867ed98d85f45a18265441c1760386ef353b3d43.json` (exit 0, label `mutants killed 21 of 21; forgeries refused 17 of 17; negctl refused 3 of 3; probe consistent 1 of 1; honest accepted 1 of 1; wlink 2 of 2; durability 2 of 2; bytes 5 of 5; dirtyrefuse 1 of 1; ownrec 1 of 1`). Public path at L (lane re-run): v6 exit 0 (`l1/public/v6-public.json`), v7 exit 1 with five `counts-extra-key` refusals (`l1/public/v7-public.json`). R97-C2 at L: `.ufo/waves/round-97/l1/scores/c2-*-at-867ed98d….json`.
- **Finding that drives the verdict (M97-j).** The landed v7 allow-list accepts the nine label keys only, while the verdict emits fourteen; every honest public run is refused. The frozen kill rule's honest legs replace the verdict with a nine-key stub (`K-dmain pos`, `K-wlink`, `K-bytes`), so command A never ran the real counts. Confirmed by the lane (v6 vs v7 public runs above) and by wave seat CriticC1 F1.
- Other binding defects recorded, not amended: imported pins not bound to the revision and a fail-open when a named file is absent at the revision (CriticC1 F2, F3; M97-k); the `ownrec` clause of the label is a literal `1` and the green receipt on disk lacks the `ownrec` key (M97-m, `kill-rule-v3.py:735-738, 778-780`); the K-ownrun leg recurses without bound (M97-r, orchestrator relay of ScribeLimits L27; command A not re-run); the K-cwd leg cannot fail (M97-s, ScribeLimits L25; `c_cwd` passes no `cwd=`).
- Frontier step: S322 admitted (`fsync(2)`, tier A, located quote 19 words in DESCRIPTION, fetched 2026-11-05, sha256 `f0a986d2…`); S323 rejected (`rename(2)`, tier A scope narrow; reason and flip condition in the row); the knowledge entry cites S322. Search log and Gate block in `corpus/lessons/round-97.md`.
- Mistakes mined: M97-a through M97-s in `corpus/lessons/round-97.md` `## Mistakes`, plus M97-q (before-side measurement root) and M97-r/s; each with class, evidence, captured-by, fix. The `## Mistakes` section is the round's mined set.
- **Wave `r97-w1`** (one v1 wave, band 8–16, validated `counts {spawn 12, total 12}`, no refusal; `.ufo/waves/round-97/r97-w1-spec.json`, `r97-w1-dispatch.json`, `r97-w1.ready`, dispatched 2026-11-05 16:48:33 per `r97-w1.ready.dispatched`; `r97-w1-results.json` settled, WAVE-DONE received). Seats: executor 2 (ExecRepro, ExecC2Repro), scout 1 (ScoutSources), scribe 2 (ScribeCrossLink, ScribeLimits), connector 1 (ConnectorOverlap), reviewer 2 (ReviewerV7, ReviewerScope), critic 2 (CriticC1, CriticC2), mutation-tester 1 (MutationC1), sentinel 1 (SentinelWrite). Attack seats 6 of 12 (50 %). Reports under `.ufo/waves/round-97/w1/`. Key seat results: ExecRepro and ExecC2Repro reproduce the landing numbers exactly; ReviewerScope PASS on frozen bytes (`git diff --name-status e859a88d 867ed98d -- tools/round-97 .ufo/waves/round-97 plans/round-97-claims.md` lists one added file, `pre/s323-rename2-fetch.html`); CriticC1 F1–F6 (public-path refusal, imported pins, fail-open, unchecked fields, last-wins duplicate keys, and a hand-written receipt that verifies); CriticC2 vocabulary holes (rows a2, a4, a5, b1, b3, b4, c1); SentinelWrite F1 (HIGH for a hostile manifest: `build_copy` path confinement), F2 (MED latent), F3 (MED: C2 receipt writers follow a symlink), F4 and F5 (LOW); MutationC1 (six mutants in scratch; M-C, M-F, M-A survive command A; M-B, M-D, M-E killed; three command-A legs cancelled at my wrap-up steer and marked not measured); ScoutSources re-verified both quotes and the census; ScribeCrossLink found the N9 citation error (M97-l); ConnectorOverlap confirmed the kake writer defect and a sibling revenger round-97 working the same v6 ground.
- Lane hygiene: a seat's stray clone at the lane root (`clone/`, a copy of the lane at `867ed98d`) was moved to `/fast/scratch/hyaku/kaidoku-r97/misroot/` and is not committed.

## Landed changes

- `e859a88d` — freeze: `plans/round-97-claims.md`, `tools/round-97/`, `.ufo/waves/round-97/` (pins, mutants, forgery, manifests, C2 fixtures, before-side receipts). LOG entry `## 2026-11-05 — round 97`.
- `867ed98d` — landing: `SKILL.md` craft block 36; `corpus/QUALITY.md` rows 195–196; `corpus/SOURCES.md` S322 and S323; `corpus/knowledge/2026-11-05-r97-receipt-byte-binding.md`; `corpus/README.md` knowledge row; `.ufo/waves/round-97/pre/s323-rename2-fetch.html`.
- `b30bb749` — bookkeeping: `corpus/QUALITY.md` row 197; `corpus/lessons/round-97.md`; `SCORECARD.md` round-97 section (capability row withdrawn before commit: never landed); `LOG.md` round-97 entry; wave evidence `.ufo/waves/round-97/w1/`, `.ufo/waves/round-97/l1/`, `.ufo/waves/round-97/r97-w1-*.json`, `.ufo/waves/round-97/r97-w1.ready`, `.ufo/waves/round-97/r97-w1.ready.dispatched` (orchestrator marker, committed as wave evidence, not edited).
- Each change is tied to the LOG entry `## 2026-11-05 — round 97` and to its commit above.

## Before → after measurements

**R97-C1 (calibration) — NOT ADMITTED.**
- Before, at base `2a54af0785f75d50912e1136443c8e78e62adf27` plus uncommitted round-97 instruments: `python3 -I -B tools/round-96/kill-rule-v2.py --root . --work <scratch> --mutants .ufo/waves/round-97/mutants-before-noc1.json --fixtures .ufo/waves/round-97/forgery --prefix forge --decl 2a54af0785f75d50912e1136443c8e78e62adf27 --json-out .ufo/waves/round-97/pre/c1-v2rule-at-base.json` → exit 1, label `mutants killed 17 of 10; forgeries refused 4 of 10; negctl refused 3 of 3; probe consistent 1 of 1; honest accepted 0 of 1` (17 of 18 real mutants killed; M-p1 survived; the `of 10` is a stale constant; the forgery count is confounded, M97-g). Dirty-tree leg: `pre/c1-dirty-v6-admits.json` `v6_dirty_exit 0`.
- After, at `867ed98d`: command A `python3 -I -B tools/round-97/kill-rule-v3.py --root . --work <scratch> --mutants .ufo/waves/round-97/mutants.json --fixtures .ufo/waves/round-97/forgery --prefix forge --decl e859a88d78567c44bc1ecfd211afe123755ae1c7 --json-out <receipt>` → exit 0, label as above (the frozen predicate, met literally). Public path at `867ed98d`: `python3 -I -B tools/round-97/stop-boundary-repair-battery-v7.py --root . --repair-cmd tools/round-92/upx-stop-boundary-search-repair.py --work <scratch> --rev 867ed98d… --expect '<frozen label>' --json-out <receipt>` → exit 1 with five `counts-extra-key` reasons; v6 on the same run exits 0.
- Commit measured: `867ed98d`. Verdict: NOT ADMITTED (public path harmed; two binding gaps; the honest leg of the frozen counter is a stub).

**R97-C2 (depth) — verified on the frozen predicate.**
- Before, at base `2a54af07`: `python3 -I -B tools/round-97/depth-blocks-v4.py --root . --rev 2a54af07… --expect-blocks 36 --shape-from 36` → exit 1, `blocks 35, resolved 35, required-shaped 0/0` (`pre/c2-depth-v4-at-base.json`); craft `--manifest .ufo/waves/round-97/manifests/block36-after.json --block 36 --rev 2a54af07…` → exit 1, block 36 missing (`pre/c2-block36-manifest-at-base.json`). The base receipt reads base data with the lane's v4 counter (the counter file does not exist at base; ExecC2Repro item 6).
- After, at `867ed98d`: command C `python3 -I -B tools/round-97/depth-blocks-v4.py --root . --rev 867ed98d… --expect-blocks 36 --shape-from 36 --expect 'blocks 36, resolved 36, required-shaped 1/1'` → exit 0; command D (after manifest) → exit 0; command E (junk manifest) → exit 1 on four keyword atoms. Discrimination: round-93 checker accepts rule-free and wrong-row fixtures where craft v2 refuses them; `depth-blocks-v4.py --decoy-proof` → `control_killed true`.
- Commit measured: `867ed98d`. Verdict: verified on the frozen predicate (named limits 6–8; the wave's vocabulary holes are routed to round 98).

## Sources & frontier

- Census, round start: `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kaidoku` exit 0; registry rows `git show 2a54af07:corpus/SOURCES.md | grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}'` = 226.
- Census, round end (at B `b30bb749`): same command exit 0 (`kaidoku ok`); `grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}' corpus/SOURCES.md` = 228. Warnings: W04 duplicate-URL warnings, unchanged in kind.
- Rows added by tier: S322 tier A (`mined`, admitted, `used-by` the knowledge entry); S323 tier A (`rejected`, `REJECTED: … flip: …`). Rows touched old→new: none (no existing row's status, recheck or used-by changed).
- Frontier rows advanced: one, receipt durability (directory fsync after rename), entered through S322 into the receipt-writer family; no coverage-map row added.
- Sourced claim: the knowledge entry and craft block 36 cite S322.
- Assimilation: none (`merge/kaidoku/` and `considerthese/` absent in this lane).
- Local-source gate (`tools/round-41/local-source-gate.py --root . --rev <L>`) reports FAIL on rows S082, S302, S321 at base and at L: pre-existing debt, recorded, not repaired.

## Trend verdicts

- **expansion: unchanged.** S322 is a source on held ground (the receipt-writer family already in Core); no new coverage-map ground; S323 rejected.
- **quality: harmed.** The landed v7 counter regresses the public honest path (v6 exit 0, v7 exit 1 on the same battery), and two landed statements overstated the binding (QUALITY 195; craft block 36's "every pin" sentence). Both are corrected by QUALITY 197 (new row) and the lesson, not rewritten in place. Evidence: `l1/public/`, `w1/CriticC1.md`, `corpus/lessons/round-97.md` M97-j and M97-k.
- **discernment: unchanged.** The lane's gate admitted C1 on a stubbed honest leg; the wave's critic found the gap; no non-author spot-check of this round exists yet (the closure writes `corpus/lessons/round-97-verifier-spotcheck.md`). Wave seats are lane-dispatched and are not counted as non-author.

## SHONEN

- [~] box 1 "SKILL.md contains real decision tables, error patterns, checklists, cited sources": `SKILL.md:810-819` (craft block 36 table, four rows, cited to QUALITY 195–196 and `corpus/knowledge/2026-11-05-r97-receipt-byte-binding.md:1`); lane-asserted, no non-author verifier.
- [~] box 2 "At least one end-to-end domain task executed and logged in LOG.md": `LOG.md` `## 2026-11-05 — round 97` (public-path battery runs `.ufo/waves/round-97/l1/public/`, command A and C/D/E at L); lane-asserted.
- [~] box 3 "Instructions executable by an agent without oral context": commands in `corpus/lessons/round-97.md` `## Measured` and `plans/round-97-claims.md`; re-run by ExecRepro and ExecC2Repro (`.ufo/waves/round-97/w1/ExecRepro.md`, `ExecC2Repro.md`); lane-asserted.
- [ ] box 4 "No cross-domain bleed (PROVINCE.md still accurate)": untouched this round (`PROVINCE.md` not edited; ConnectorOverlap notes a sibling revenger round-97 on the v6 admission ground, reported not absorbed).

## Round shape and housekeeping

- Round shape: one v1 wave `r97-w1`, 12 seats (executor 2, scout 1, scribe 2, connector 1, reviewer 2, critic 2, mutation-tester 1, sentinel 1), attack share 6/12 (50 %), connector seats 1. Planner seat held by the L1 (validator rejects planner). No residual call. Round total: 12 seats. Dead seats: none (12 of 12 settled with reports; MutationC1 cancelled three command-A legs at my wrap-up steer, marked not measured).
- Stale-lane line: no other mission of this lane is open.
- Tool installs: none. No pacman, sysctl, namespace or host change by this lane's L1; no seat report names one. `pacman` untouched.
- Misroot sweep: `git -C /home/vgpnk/Projects/shokunin status --porcelain` shows `.scratch/run15-kernel.py`, `.scratch/run15-state.json` and `.ufo/l0-questions.md` modified and `w4lines.txt` untracked at the fleet root; none is this lane's and none was moved or committed. The lane's own stray `clone/` (a seat's copy of the lane) was moved out of the lane to scratch.
- Open L0 questions: none appended this round.
- Inherited state: attempt 1; no `lane-dead-no-report kaidoku round=97` line in `.ufo/watchdog.log`; the lane was clean at `2a54af07` at start.
- Scratch: `/fast/scratch/hyaku/kaidoku-r97/` removed at landing.
- Caveats carried: before-side measured on base plus uncommitted round-97 instruments (M97-q); K-ownrun leg unbounded recursion (M97-r; command A not re-run after the relay); K-cwd vacuous (M97-s).

## Verdict for the operator

Round 97 is **not admitted**: R97-C1 is not verified in substance and harms calibration on the public path; R97-C2 verifies on its frozen predicate. Progression halts at round 97 (no round 98 launched). Round 98 must start from a fresh declaration (the lesson's Planned list: allow-list equal to the verdict's 14 keys, honest arm running the real public battery, imported pins bound at the revision, fail-closed absent files, K-ownrun single-mutant depth bound, K-cwd with a real `cwd=`, C2 receipt writers migrated, craft criterion-cell restatement).
