# mado — round 74 (hyaku run 15, attempt 1)

lane: mado · repo: `mado-shokunin` · base `bd5a971532f37df85a78f6f566dd1e649b79de11` ·
lane tip **`2fbcfbabdbaf078d0bddfe9f47ef4310c4a0397a`** (pushed; `git ls-remote origin
refs/heads/master` prints it) · round shape: ONE v1 wave, 13 seats, 13 settled, 0 dead · round
total 13.

Declared claims (frozen at `b73db773aaf67c9b26c8cf1a4cd567dec3af11f4`, before any candidate data):

- **C1 · calibration** — the landing kill credit requires the run's own echo of a caller-generated
  per-run challenge, closing the round-71/72/73 declared replay limit on the rule; the held
  round-72 rule credits all four replay cases. **Verdict: improved** (`cases=12 correct=12
  base_correct=8`, TARGET_MET).
- **C2 · operability** — the guard census counts a one-hop object alias stored at one dotted
  spelling and handed at the other, and a one-hop `os.environ` alias whose store reaches
  `env=alias`, `dict(alias)` or `{**alias}`; the held round-73 classifier misses exactly those
  four positives. **Verdict: improved** (`controls=36/36 base_controls=32/36`, TARGET_MET).

Neither claim touches a desktop, compositor, service, session or sibling surface; no tool was
installed or upgraded; no pacman transaction ran.

## Work performed

1. **Freeze before data.** Two control sets, a two-claim declaration with predicates, counting
   commands, kill rules, targets and limits, and a pre-freeze do-nothing baseline produced by an
   uncommitted prototype — `.ufo/waves/round-74/claims-declaration-r74.md`,
   `controls/c1-replay-cases-r74.json` (sha256 `17c95774…74727c`),
   `controls/c2-cases-r74.json` (sha256 `4db4cc70…b3a73d0`), `control-baseline-r74.txt`,
   `proto/held-r74.py`, committed with the instruments at `b73db773…`. The baseline showed the
   held denominators miss the targets (held credit 8/12; held classifier 32/36).
2. **C1 rule and counter.** `quality/counters/c1-r74-witness-rule.py` is `credit(out, nonce)` —
   the round-72 arithmetic plus the run's last parsed `MADO_LANDING_WITNESS: <16 hex>` echo of the
   caller's challenge (selftest 23/23). `quality/counters/c1-r74-replay-witness.py` builds twelve
   real `bash` fixture lanes inside the caller-declared scratch root, each with the landing
   harness's zero-citation clause deleted exactly once, gives every child its own fresh
   `secrets.token_hex(8)` challenge, and scores the successor rule against the held round-72
   `credit` on the same outputs (selftest 21/21).
3. **C2 instrument.** `quality/counters/c2-r74-shapes.py` is the round-73 guard census plus
   `twohop_guard` (object-alias canonicalisation both directions, binding-time and replacement
   bounds) and `environ_alias_guard` (one-hop `os.environ` alias, `dict(alias)` / `{**alias}`
   copies, rebinding and delete cancellation). Thirty-six frozen cases (28 carried byte-identically
   from round 73, hash-checked at run time); population unchanged at 20/13/13/0; selftest 86/86.
4. **Measurement.** First at the instrument commit `b73db773…`
   (`measurement-c{1,2}-r74.txt`), then re-measured after the review repairs at
   `4cfa5ddc8f884385e79d4348f01c748447a50e7e` (`measurement-c{1,2}-r74-final.txt`); identical
   counts, both `TARGET_MET`, rc 0.
5. **Curation (frontier step).** Three rows opened this round with three byte-identical fetches
   each — S450 (`secrets.token_hex`), S451 (assignment statements, attribute-reference targets),
   S452 (`os.environ` mapping modification, superseding S448's false digest, round-73 D1); S446's
   re-opened reject now carries its located quote (round-73 D5). Two knowledge entries admitted,
   one lesson with five `## Mistakes` and a `## Gate`, six QUALITY criteria at the canonical path
   (118–119 repaired from round-73 D4, 120–123 new), README index 89 → 91, PROVINCE round-74
   refinement, ledger 127 → 130, three SKILL Gate-registry rows.
6. **Wave (13 seats, one v1 wave).** Roles: executor 3, scribe 2, scout 2, reviewer 2, critic 1,
   mutation-tester 1, connector 1, sentinel 1 — attack share 4/13 = 30.8 %. The L1 holds the
   planner seat (the validator rejects `planner`); no planner was dispatched. Per-seat
   deliverables below.
7. **Review-driven repair at `4cfa5ddc…`.** The wave's two reviewers, the critic, the
   mutation-tester and the sentinel found eight defects; all repaired without touching a frozen
   predicate, label, control set, kill rule or target (SCORECARD § Review-driven repair, LOG
   repair bullet).
8. **Harm watch at `a0b6b2a0…`** (`.ufo/waves/round-74/receipts/harm-watch-r74.txt`, each line
   carrying the command's own rc): index 91/91, ledger 130/130 `uncovered=0`, axis table 3/3 MATCH
   (navigation 91/91, calibration 86/86, operability 12/12), census exit 0, five frozen
   instrument blob pairs identical, gate `MADO_SELFTEST: 460/460` (the L1-run leg,
   `receipts/gate-selftest-r74.txt`).

### Wave seats — what each delivered

| seat | role | deliverable | outcome |
|---|---|---|---|
| R74ExecC1 | executor | independent replay of the C1 counter, selftests and the rule's four-conjunct reading; one extra probe (witness after summary) | reproduced 12/12 vs 8/12, rc 0; only the per-run nonce differs from the receipt |
| R74ExecC2 | executor | independent replay of the C2 counter and selftest; population re-count; the four base misses named | byte-identical stdout, rc 0; 86/86 |
| R74ExecHarm | executor | harm watch: index, ledger, axis, census, frozen blobs; gate selftest recorded NOT RUN under its stricter no-`/tmp` bound and routed (`tools/mado-verify.sh:418`) | four of five green; ledger rc 1 at the pre-registration revision (expected, L1-confirmed) |
| R74ScribeC1 | scribe | draft of `corpus/knowledge/replay-witness-credit-r74.md` (applied by the L1) | draft landed as the committed entry |
| R74ScribeC2 | scribe | draft of `corpus/knowledge/guard-carrier-twohop-environ-alias-r74.md` plus scoped findings | draft landed as the committed entry |
| R74ScoutSources | scout | three-fetch digests, quote line numbers/word counts, D1 sweep, 0–3-space id-guard proof | all nine fetches byte-identical; F1 word-count defect (fixed), F2 S448 span (recorded) |
| R74ScoutFrontier | scout | `considerthese/` sweep (picks proposal 4, the live-tool `last live run` cell, for round 75), D1–D7 dispositions, frontier/planned cross-check, sibling overlap | nothing adopted this round; candidate handed over |
| R74RevC1 | reviewer | 15 fixtures against the C1 rule; two disagreements with the frozen grammar and the shared-challenge caller | both repaired (grammar widened, per-child challenge) |
| R74RevC2 | reviewer | 17 fixtures against the C2 classifier; one P1 (parameter shadow) and three P2 (AnnAssign, alias binding time, carried root rebinding) | the four new defects repaired; the carried root-rebinding stays a declared limit |
| R74Critic | critic | re-derived both targets, case distinctness, held-leg provenance, freeze order, padding | both claims stand; one latent duplicate pair and one unstamped baseline recorded |
| R74Mutant | mutation-tester | eight literal mutants scored on the frozen sets, pristine/mutated/restored | 5/8 killed; C1-M4, C2-M3, C2-M4 survive — coverage limits recorded |
| R74Conn | connector | shared pattern, per-case separators, historical instrument candidates with exclusions, sibling overlap | two grounded candidates named; two suggested ones positively ineligible |
| R74Sentinel | sentinel | static write/process/environment audit, scratch refusals, privacy scan, lane/fleet status | D1 (symlink ancestor), D2 (selftest no-follow), D3 (child env) — all repaired |

## Landed changes

Every change is tied to the round-74 LOG entry (`LOG.md`, "Round 74 — the rule's own witness and
two more guard carriers") and to the commit that carries it.

| change | commit |
|---|---|
| Frozen declaration, two control sets, pre-freeze baseline, prototype, the three instruments | `b73db773aaf67c9b26c8cf1a4cd567dec3af11f4` |
| Witness rule + replay counter + C2 census (first generation), corpus entries, lesson, SOURCES rows, README, SCORECARD, LOG, PROVINCE, QUALITY (both), SKILL registry, ledger, fetches, receipts | `a9e994307f132358939a4d074ce122c7a379da03` |
| Review repairs (C1 grammar + per-child challenge; C2 AnnAssign/binding/shadow; symlink ancestors; `O_NOFOLLOW`; child-env allowlist), wave seat evidence, corrected word counts, fifth mistake row, carried errata | `4cfa5ddc8f884385e79d4348f01c748447a50e7e` |
| Axis publication (navigation 91/91), ledger pointer fix, review-repair records in SCORECARD and LOG | `a0b6b2a0532fbf68c61ae598dd91e2ff7ffa7748` |
| Final measurement receipts and the harm watch | `63b2a4ab2c53f384bbd30b768579fca57b07bf5c` |
| First measurement receipts and dispatch markers | `2fbcfbabdbaf078d0bddfe9f47ef4310c4a0397a` |

Frozen rounds 72–73 untouched: identical blob ids at `bd5a9715` and the tip for
`c1-r72-landing-controls.py`, `c1-r73-summary-mutants.py`, `c2-r73-shapes.py`,
`tools/mado-verify.sh`, `quality/landing-counters.sh` (`receipts/harm-watch-r74.txt`).

## Before → after measurements

| claim | counting command | before (held) | after (candidate) | measured commit |
|---|---|---|---|---|
| C1 calibration | `python3 -I quality/counters/c1-r74-replay-witness.py --repo . --rev REV --base-rev bd5a971532f37df85a78f6f566dd1e649b79de11 --controls .ufo/waves/round-74/controls/c1-replay-cases-r74.json --scratch-root DIR` | `base_correct=8/12` (6.6667) — the held round-72 `credit` credits all four replay modes | `cases=12 correct=12 base_correct=8 verdict=TARGET_MET` rc 0 → 10.0000 | `b73db773…`, re-measured `4cfa5ddc…` |
| C2 operability | `python3 -I quality/counters/c2-r74-shapes.py --repo . --rev REV --base-rev bd5a971532f37df85a78f6f566dd1e649b79de11 --controls .ufo/waves/round-74/controls/c2-cases-r74.json --scratch-root DIR` | `base_controls=32/36` (8.8889) — the held round-73 classifier misses exactly the four new positives | `population=20 readers=13 guarded=13 unguarded=0 controls=36/36 base_controls=32/36 verdict=TARGET_MET` rc 0 → 10.0000 | `b73db773…`, re-measured `4cfa5ddc…` |
| — coverage / admitted-note reachability | `python3 -I quality/check-index.py --repo . --rev REV` | 89/89 at base | 91/91 at the landing tip | `a0b6b2a0…` |
| — operability / instrument ledger | `python3 -I quality/check-tool-ledger.py --repo . --rev REV` | 127/127 at base | 130/130, `uncovered=0` | `a0b6b2a0…` |
| — operability / hermetic gate | `bash tools/mado-verify.sh --selftest` | 460/460 | 460/460 | `receipts/gate-selftest-r74.txt` |

Receipts: `.ufo/waves/round-74/measurement-c1-r74.txt`, `measurement-c2-r74.txt` (first run),
`measurement-c{1,2}-r74-final.txt` (repair run), `control-baseline-r74.txt` (pre-freeze held
legs), `receipts/m74-1-red.txt` and `receipts/m74-2-red.txt` (the two mistake red states).

## Sources & frontier

Census before → after, same command both times:

```sh
/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin mado
```

- round start: 386 rows, exit 0 (W04 duplicate-URL warnings only)
- round end: 389 rows, exit 0 (`mado ok …/corpus/SOURCES.md`; W04 for S451/S447 and S452/S448)

Rows added by tier: **3 × tier A** — S450 (`Doc/library/secrets.rst`, `token_hex`), S451
(`Doc/reference/simple_stmts.rst`, attribute-reference assignment), S452 (`Doc/library/os.rst`,
`environ` mapping modification, `teaches` opens `supersedes S448 — `). Every row was opened this
round with three byte-identical fetches (`fetch/*.rst.{1,2,3}`); the lesson's `## Gate` carries
each URL, the 2026-11-04 access date and a ≤25-word located quote (S450 20 words at
secrets.rst:80-81, S451 23 at simple_stmts.rst:160-162, S452 15 at os.rst:196-197).

Rows touched old→new: none of the held rows' `status`/`recheck`/`used-by` cells changed; S448's
false digest is corrected by S452 (append-only), and the re-opened reject S446 now carries its
located quote (23 words at stdtypes.rst:5525-5527). Frontier rows advanced: the round-73
`control-set-mutant-kill` frontier bullet (the rule's own limit) and the `guard-carrier-global-
environ` bullet (the alias grammar) are superseded in `corpus/README.md` § Frontier by the
round-74 bullet naming both new entries.

`Assimilation: none` — `considerthese/` was mined by `R74ScoutFrontier` (it selects proposal 4,
the live-tool `last live run` cell, for round 75) and nothing from
`/home/vgpnk/Projects/shokuknow/merge/mado/` was adopted: this round's claims are instrument work
on the lane's own harness chain, and the package's staged entries are domain material for a later
assimilation round.

## Trend verdicts

- **expansion: improved.** Two admitted entries, README index 89 → 91, three tier-A rows opened
  this round with three byte-identical fetches each, and the round-73 frontier's replay limit
  becomes a landed rule. No generic material: both entries cite the lane's own receipts plus a
  located CPython sentence.
- **quality: improved.** Both claims `TARGET_MET` with their do-nothing controls at the declared
  scores; eight wave-found defects repaired with red-before/green-after evidence (the reviewers'
  fixtures flip as named in SCORECARD); six QUALITY criteria now sit at the canonical path;
  the frozen rounds 72–73 instruments are blob-identical.
- **discernment: improved.** The wave's scouts/reviewers/critic/mutation-tester/sentinel produced
  the eight repairs, five `## Mistakes` rows and the carried errata (the C1 duplicate pair, the
  unstamped baseline, S448's span); three surviving mutants and four carried limits are reported
  rather than hidden. The outside admit/reject spot-check remains the closure's duty.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — this
  round adds three Gate-registry rows and keeps the tables; no new outside-lane verifier.
- [~] At least one end-to-end domain task executed and logged in LOG.md — the round is instrument
  work (two counters measured end to end on real children and committed bytes); no desktop task.
- [~] Instructions executable by an agent without oral context — the declaration, controls and
  counters reproduce from committed bytes (two executors and the critic did), but the
  outside-lane promotion rule is still not satisfied.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — PROVINCE.md gains one append-only
  refinement naming the three instruments; no config/compositor/sibling write occurred, but no
  fresh outside-lane approval exists.

## Round mechanics

- **Wave**: one v1 wave, 13 seats, validated under `ufo-wave-policy.json` (band 8–16, counts
  `spawn=13 resume=0 total=13`), dispatched through the inline spawn handoff
  (`.ufo/waves/round-74/w1.ready` → `w1.ready.dispatched`); `w1-results.json` carries 13 seats with
  non-empty output; **0 dead seats**.
- **Misroot sweep**: `git -C /home/vgpnk/Projects/shokunin status --porcelain` shows only
  `.scratch/*` (orchestrator-owned) and an unexplained `after`; no mado round-74 file landed at the
  fleet root. Nothing copied back.
- **Stale-lane**: respawn-per-round driver; no other mission of this lane is open.
- **Tool installs**: none; no pacman transaction. Routed defect for round 75:
  `tools/mado-verify.sh:418` hardcodes a `/tmp` selftest scratch (scratch rule 4).
- **L0 questions**: no new question this round. Carried operator-owned: r57–r60, the L2 floor, the
  host-recovery pacman pause, and the r37/r38 session-material history question; the run-15
  routing sentence's staleness (round-73 D7) is operator-owned, not lane debt.
- **Report commit**: filed through `scripts/hyaku/fleet-commit.sh --as mado` after the lane tip
  `2fbcfbabdbaf078d0bddfe9f47ef4310c4a0397a` was confirmed on the remote
  (`git ls-remote origin refs/heads/master`).
