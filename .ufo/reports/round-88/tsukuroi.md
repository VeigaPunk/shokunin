# tsukuroi — round 88 report

L1: TsukuroiR88 (attempt 1; no earlier attempt of round 88 in `.ufo/watchdog.log`, no inherited round-88 files).
Lane `master` tip: `f1b27474ba2e89817d063c8ebe1373b15ca43bb8`. `git ls-remote origin refs/heads/master` prints this hash.

## Work performed

Declared claims, frozen at `01b2a9b091fe8af22b054bc061bbe14e9f96bf86` before the candidate battery existed
(`SCORECARD.md` "Round 88 — declaration"):

- **C1 (measured; operability 9, assurance arm of the `limine-pins` gate).** The r88 battery
  `tools/limine-pin-battery-r88.py`, driven by the frozen counter `tools/battery-discrimination-r88.py` over a frozen
  48-gate roster (3 POSITIVE, 45 NEGATIVE: the r87 forgers g01–g16 and gate mutants m02–m30), reads `met` for every
  positive and `unmet` for every negative in each of three runs, each gate renamed and nonce-perturbed inside a
  sandbox that hides the lane. Target 3/3 and 45/45 ×3.
- **C2 (exploratory; depth 8, the lowest-tied axis; sourced S355–S360).** Entry
  `corpus/knowledge/limine-pin-writers-r88.md` (+ `.json`), rows PW1–PW9: who writes a Limine pin on this host and
  under which setting, how the hash is computed, what the repair command does, and how limine-snapper-sync copies a
  stale main pin into new snapshot entries. The verdict comes from a non-author `unprovable-but-better` judgment
  (the hyaku closure).

Work items:

- **Inputs.** Round-87 closure (admitted) and `corpus/lessons/round-87-verifier-spotcheck.md` §5 routed 1–6; their
  disposition is the table in `corpus/lessons/round-88.md` "Inputs read". Routed 2 (C1 discrimination gap) is C1's
  surface and routed 6 (the operator-owned host incident) is C2's.
- **Freeze `01b2a9b0`.** Counter, roster, manifest (`.ufo/waves/round-88/before/freeze-manifest.sha256`, 57 lines),
  do-nothing control (the r87 battery: positives 3/3, negatives 29/45, 32/45, 30/45 → unmet) and five forgery
  controls ×3 (always-met, always-unmet, digest identity, embedded negative digests, roster-label oracle — all
  unmet), `.ufo/waves/round-88/before/controls/controls-summary.txt`.
- **Candidate `5b98ca98`.** Battery r88: 38 families (16 new, one per uncertified r87 clause or gate mutant),
  reporting contract R8, literal `FAMILY_ROSTER`, `--selftest` 14/14 with eight one-field lie wrappers; HOST-SHAPE no
  longer leaks digests. Entry PW1–PW9, SOURCES S355–S359, pinned sources `.ufo/waves/round-88/before/src/`, host
  receipt `.ufo/waves/round-88/before/host/receipt.txt` (read-only; the one `sudo` use was `find /boot | b2sum`
  and `cat /boot/limine.conf`, with the `/boot` list `cmp`-identical before and after).
- **Registry `1fac4195`.** Rows `limine-pin-battery-r88` and `battery-discrimination-r88` (`SKILL.md`).
- **C1 measurements.** 3/3, 45/45 in each of three runs at `5b98ca98` (clean clone,
  `.ufo/waves/round-88/after/measured/c1-receipt.txt`), at `1fac4195` (clone, `c1-receipt-1fac4195.txt`) and in the
  canonical lane layout (`c1-receipt-canonical.txt`); battery `ab6c1b33…` in all; freeze manifest OK in each.
  Per-gate kill map: every negative is killed by the family named for its clause
  (`.ufo/waves/round-88/after/killmap/killmap.txt`).
- **Wave w1 integration** (`.ufo/waves/round-88/w1/`; seats wrote their receipts to disk):
  - ExecReplicate: C1 3/3, 45/45 ×3 independently; selftest 14/14. Found D1: from a `clone --shared` the frozen
    roster-oracle control reads `met` (`w1/ExecReplicate.md` §4–5).
  - CriticClaims: F1 the sandbox masks one copy of the lane (roster walkers `met`; the freeze-time oracle `unmet` was
    144/144 crash rows); F2 the nonce is an appended comment, so digest batteries that strip it read `met`; F3 the
    manifest void clause is not in the code and `--roster` is unguarded; F4 the surface is battery calibration
    (`w1/CriticClaims.md`). No roster label disputed (48/48).
  - ExecLints: registry 140/140, header 104/104, gate selftest 15/15, entry/SOURCES cross-check PASS; L-1 = F3.
  - ReviewBattery: all 16 new families supported by Limine v12.9.4 source lines; F1–F5 low/info, no battery change
    needed (`w1/ReviewBattery.md`).
  - MutHeldOut: 24 held-out gate mutants (1 equivalent); r87 battery kills 13 of 23, r88 kills 18 of 23
    (`w1/MutHeldOut.md`).
  - CriticForgers: faithful docstring reimplementation `met` ×3; 9 of 19 one-clause forgers killed, 10 survive
    (`w1/CriticForgers.md`).
  - ReviewEntry: 7 support, 2 partial (PW2 source, PW5 inference); all fixed at landing (`w1/ReviewEntry.md`).
  - ExecResidual: r87 routed 1 closed — the residual clause probe on the landed gate bytes `e3b0fab4…` reads 11/11,
    rc 0 ×3, and its negative controls g07/g10 read rc 1 (`w1/ExecResidual.md`). It also notes the filed r87 report's
    "Landed byte-identical" sentence is false at byte level (erratum in the lesson).
  - ConnectorOverlap: r87 routed 3 closed — 20 sibling repos scanned, no conflicting fact
    (`w1/ConnectorOverlap/sibling-scan.txt`).
  - ScribeLesson: drafts of M1/M3, the R87-R6 erratum and the r87 provenance note, integrated into the lesson.
  - MutBattery: 26 single-point battery mutants; the frozen counter kills 8, 18 survive (1 equivalent; 14 redundant
    lines or families the roster does not need, `ALL-PIN-KEYS` whole; `hash_mismatch_panic.value` has no detector;
    two contract checks only the selftest sees). Six counter-killed mutants pass the selftest. `WHITESPACE-CRLF`
    draws CRLF with p 0.6, so `N-m22`/`N-g15` escape a run with p ≈ 2.6 %; the pristine battery read `met` on
    `N-m22` in 1 of the seat's 8 runs (`w1/MutBattery.md` §3–4). Routed R88-R2..R4.
  - ScoutSources: all 14 pinned files re-opened through tag clones (raw URLs HTTP 429) — byte-identical; upstream
    `limine-mkinitcpio`, `limine-install`, `limine-mkinitcpio-install` byte-identical to the installed copies
    behind S360; nothing contradicts PW5–PW8. Its patch scoped PW8 to entries created after the incident, added the
    copy site and path-line writer to PW6 (pinned by the L1 at landing), named two hashes per snapshot line (PW7)
    and the inactive enrolled-config `b2sum` surface (Limits) (`w1/ScoutSources.md`, lesson Gate addendum 2).
- **Post-freeze control re-run, both layouts** (QUALITY 126 (b), labelled post-freeze):
  `.ufo/waves/round-88/after/controls-clone-layout.txt` — from a clone, the do-nothing reads 32/45 (unmet) and four
  forgers stay unmet with 0 error rows, while the roster oracle reads 3/3, 45/45 `met`. No-harm check on the live
  gate at the tip: r87 battery 22/22 ×3, r88 battery 38/38 ×3, gate selftest 15/15
  (`.ufo/waves/round-88/after/harm-check.txt`).
- **PW5 correction from installed bytes (S360).** Upstream tag copies of the mkinitcpio scripts returned HTTP 429
  to the L1 and two seats; the installed `limine-mkinitcpio-install` shows the repair rebuilds each UKI with
  `mkinitcpio --uki` and re-adds it with `limine-entry-tool --add-uki`: new bytes and new pins together. The first
  draft's Operator action 2 ("accepts the rewritten bytes as trusted") was wrong and is corrected.
- **Landing `68ca60f5`.** Entry fixes, S360 and S355's Main.java anchor, lesson M1–M3 + errata + provenance,
  QUALITY 126, README frontier, LOG, measured outcome. Later commits: R88-REG-1 `45c60ac1`, routed list `78ea179c`,
  post-freeze both-layout controls + no-harm check `4ef5d916`, ScoutSources integration `35ca9e7e`, SCORECARD
  addendum `8189c754`; wave evidence `9fe5d385`, results `f1b27474`.

## Landed changes

LOG.md entry "Round 88 — Limine pin battery r88 and the pin-writer plane" covers every commit below.

| Commit | Change |
|---|---|
| `01b2a9b091fe8af22b054bc061bbe14e9f96bf86` | freeze: counter, roster, controls ×3, declaration |
| `5b98ca98c9a19641e77832bc57579d95fa5571a3` | candidate battery r88; entry PW1–PW9; S355–S359; pinned sources; host receipt |
| `1fac4195243e55e7d9d8a2eddd653443d8559bff` | registry rows for the two new tools |
| `68ca60f51d672ef53e6bf626e220c3784d4916fe` | landing: entry fixes, S360, lesson, QUALITY 126, README, LOG, measured outcome, receipts |
| `45c60ac15b8f1996e9dcba43ef148a9e6c42a9ca` | SKILL.md R88-REG-1 (counter self-check cell corrected, append-only) |
| `78ea179c80cde316f6e57136e15c9a35023edb01` | lesson wave summary, routed R88-R1..R6, final-tip C1 receipt |
| `4ef5d9166ea3669ee66625fb9d2b2e240393d667` | post-freeze controls from clone layout, live-gate no-harm check, r87 report erratum |
| `35ca9e7ebb80597a9967bfa402e04d69d8b5e9f8` | ScoutSources integration: PW6–PW8, Limits, SnapshotManager/ImageDetail pins, S359 anchor |
| `8189c75421b288a243f1d12ffbdc09bc70acaa92` | SCORECARD addendum (CR clause by chance; M18) |
| `9fe5d385e59295f6cec913d68f23a4b449b4bfe0` | wave w1 evidence (12 seat reports and receipts) |
| `f1b27474ba2e89817d063c8ebe1373b15ca43bb8` | `w1-results.json` |

## Before → after measurements

- **C1.** Command: `python3 tools/battery-discrimination-r88.py --battery <battery> --runs 3`. Before (do-nothing,
  r87 battery, freeze `01b2a9b0`): positives 3/3, negatives 29/45, 32/45, 30/45, unmet. After (r88 battery
  `ab6c1b33…`, measured at `1fac4195`, the battery unchanged since `5b98ca98`; the landing tip changes no tool):
  3/3, 45/45 in each of three runs, met, in both the clone and the canonical layout.
  **Verdict: target met by the frozen counter and kill rule; not verified as a forgery-resistant measurement.**
  The wave falsified the counter's isolation after scoring (F1–F3 above); the predicate's isolation sentence does
  not certify what the declaration said. The counter stays frozen; its successor and the gaps are routed.
- **C2.** Exploratory, no counting command. Prior state: `limine-pin-plane-r87.md` Limits "The repair command of the
  host's limine-entry-tool hook was not opened"; `git grep -n -i 'ENABLE_VERIFICATION\|computeBlake2\|blake2IntegrityCheck'
  3ba37eb0 -- corpus/knowledge` → empty. After: PW1–PW9 at `68ca60f5`. Verdict pending the non-author closure.

## Sources & frontier

- **Census.** Command: `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin tsukuroi`.
  - Before (round start, tip `029454fc`): rc 0, 354 rows, 52 W04, `tsukuroi ok`
    (`.ufo/waves/round-88/before/census-before.txt`).
  - After (tip `68ca60f5`): rc 0, 360 rows, 52 W04, `tsukuroi ok` (`.ufo/waves/round-88/after/census-after.txt`).
- **Rows added by tier:** A +6 (S355–S359 code/A `mined`; S360 own-work/A `mined`).
- **Rows touched, old → new:** S355 (added this round) anchor gains `Main.java raw lines 45-207` and its `teaches`
  gains "no hash-only refresh option exists". No pre-round row changed.
- **Rejected:** the installed native binaries' strings as a source (symbol names only; lesson Gate).
- **Sourced claim:** C2 rests on S355–S360, all opened this round.
- **Frontier advanced:** README "Round 88 — Limine pin writers; battery r88" (new ground, four frontier bullets).
- **Mined mistakes:** M1 `R88-CONTROL-PASSED-BY-CRASH`, M2 `R88-PROMISE-IN-DOCSTRING-NOT-CODE`,
  M3 `R87-PRE-LANDING-EVIDENCE-READ-AS-LANDED`; QUALITY 126 from M1.
- **Assimilation:** none (no `merge/tsukuroi/` theme fits the Limine-writer surface). considerthese: not mined
  this round (latest file `considerthese/2026-10-26.md`).

## Trend verdicts

- **expansion — unprovable-but-better.** New sourced ground on the writer side of the pin plane (+6 tier-A rows,
  354 → 360); whether the entry is new ground is the closure's judgment.
- **quality — improved.** Registry 138/138 → 140/140; header 103/103 → 104/104; the r87 residual probe now rests on
  landed bytes (11/11 ×3); the battery's selftest asserts a literal roster and eight one-field lies; held-out
  mutant kills 13/23 → 18/23. The C1 counter defects are a quality debt of this round's instrument, disclosed.
- **discernment — improved.** The lane's own wave falsified its frozen instrument's isolation and the L1 reports
  C1 as not verified on that property rather than reading 45/45 as proof; the freeze-time "unmet" was traced to a
  crash, and that became QUALITY 126. The PW5 repair story was corrected from installed bytes.

## SHONEN

- [~] SKILL.md decision tables / error patterns / checklists / cited sources. Evidence: registry rows
  `limine-pin-battery-r88`, `battery-discrimination-r88` (`SKILL.md` at `1fac4195`). Non-author verification owed.
- [~] End-to-end domain task logged in LOG.md. Evidence: LOG.md "Round 88" — host pin state → writer source →
  repair command read from installed bytes → the entry's Operator actions.
- [~] Instructions executable without oral context. Evidence: battery and counter docstrings, `--selftest`, the
  entry's `recheck:` line. No no-oral-context retest was run.
- [~] No cross-domain bleed. Evidence: PROVINCE.md unchanged; ConnectorOverlap's completed sibling scan
  (`w1/ConnectorOverlap/sibling-scan.txt`, 20 repos, no conflicting fact).

## Round shape and extras

- **Shape:** one v1 wave, w1, 12 seats: executor 3 (ExecReplicate, ExecResidual, ExecLints), mutation-tester 2
  (MutBattery, MutHeldOut), critic 2 (CriticForgers, CriticClaims), reviewer 2 (ReviewBattery, ReviewEntry), scout 1
  (ScoutSources), scribe 1 (ScribeLesson), connector 1 (ConnectorOverlap). Attack seats 6/12. The §3 planner seat is
  held by the L1. No residual call. Round total: 12.
- **Seat outcomes:** all 12 settled with output and a report on disk (`.ufo/waves/round-88/w1-results.json`); no dead
  seat, none replaced. ScoutSources was nudged once by the L1 to write up after the other 11 had reported.
- **Misroot sweep:** fleet `git status --porcelain` lists only orchestrator `.scratch/` files, this report, and
  `trail-ids.txt` (2 bytes, mtime 20:36:24, before this round's launch at 20:38:50; not this lane's, left alone).
  No misroot from this lane.
- **Scratch:** `/fast/scratch/hyaku/tsukuroi-r88` removed after landing.
- **Stale-lane:** respawn-per-round driver; no other mission of this lane is open.
- **Tool installs:** none.
- **Open L0 questions:** `tsukuroi | round-86 | HOST INCIDENT` — the pins on lines 30 and 38 still mismatch; the
  repair is the operator's (C2 PW5 now states what `limine-update` would do).
