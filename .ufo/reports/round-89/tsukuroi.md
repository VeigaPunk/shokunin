# tsukuroi — round 89 report

L1: TsukuroiR89 (attempt 1; `.ufo/watchdog.log` line 3109 `launch tsukuroi round=89 … attempt=1`, no earlier
attempt, no inherited round-89 files). Lane `master` tip: `7f3f30b3898adf77af1035608621ffdbbabaa9d9`. `git ls-remote origin refs/heads/master`
prints this hash.

## Work performed

Declared claims, frozen at `fba764ca2a72dc2321f1c5d8cd228e92aa9382a9` before any candidate score
(`SCORECARD.md` "Round 89 — declaration"):

- **C1 (measured; surface: battery calibration of the `limine-pins` gate; operability 9, assurance arm).** The r89
  battery `tools/limine-pin-battery-r89.py`, driven by the frozen counter `tools/battery-discrimination-r89.py` over a
  frozen 65-gate roster (3 POSITIVE, 62 NEGATIVE), reads `met` for every positive and `unmet` for every negative with
  zero error rows in each of three runs, the battery seeing each gate only as an opaque launcher inside an allowlist
  sandbox. Target 3/3 and 62/62, 0 errors ×3.
- **C2 (exploratory; depth 8, the lowest-tied axis; sourced S361–S363, S350–S353 anchors).** Entry
  `corpus/knowledge/limine-uri-failure-r89.md` (+ `.json`), rows UF1–UF8: what each Limine v12.9.4 URI resource
  resolves to, what an unopenable `path:` does to an `efi` entry, why Secure Boot's no-hash rule skips `efi`
  chainload, what `panic` means on screen, and what this host can reach. Verdict only from a non-author
  `unprovable-but-better` judgment (the hyaku closure).

Work items:

- **Inputs.** Round-88 closure (`rejected-honest-stop`) and its spot-check §5 routed 1–5, disposition table in
  `corpus/lessons/round-89.md` "Inputs read": routed 2 and 5 are C1; routed 1 is mistake M1 (README fixed); routed 3
  is an erratum (the CR flake is the seat's **2/24**, `.ufo/waves/round-88/w1/MutBattery.md:23,113`); routed 4 — this
  report is written after the last lane commit and committed at once.
- **Freeze `fba764ca`.** Counter r89, roster `.ufo/waves/round-89/before/roster/roster-r89.json` (r88's 45 negatives;
  r88 positive g00 relabelled NEGATIVE on `config.c` raw 527-551 with probe witness `cr-internal`; 15 r88 survivors
  f01 f03 f06 f07 f08 f12 f14 f16 f18 f19 h01 h10 h11 h19 h20; `m31` panic-value lie), roster probe
  (`before/roster-probe/probe-receipt.txt`: 3 positives exact 16/16, every r89 negative witnessed), manifest 76 lines,
  host receipt.
- **Controls `dddc82c6`** (committed before the candidate `81f68d00`; both layouts, 3 runs each,
  `.ufo/waves/round-89/before/controls/controls-summary.txt`): K1 r88 battery 46/46/45 of 62 (canonical) and
  46/46/46 (clone); always-met 0/62; always-unmet 0/3; roster oracle and source-fingerprint oracle 0/62 with 0 hits
  (65/65 correct and 65 hits outside the counter, `potency-receipt.txt`); crash battery 65 error rows, rc 3.
- **Candidate `81f68d00`.** Battery r89: 50 families (12 new), CRLF in every `WHITESPACE-CRLF` case, selftest 15/15
  with a `hash_mismatch_panic.value` lie; registry rows `limine-pin-battery-r89`, `battery-discrimination-r89`. The
  first uncommitted candidate read 61/62 in one run on a random `KEY-EQUALS` draw and was fixed before commit
  (`.ufo/waves/round-89/after/dev/README.txt`; lesson M2). Entry UF1–UF8, SOURCES S361–S363, pinned sources
  `.ufo/waves/round-89/before/src/`, README r88 frontier correction.
- **C1 measured.** 3/3, 62/62, 0 errors in each of three runs at `81f68d00` from a clean `git clone --shared`
  (`after/measured/c1-receipt-81f68d00.txt`) and in the canonical lane at `665408cc` (`c1-receipt-canonical.txt`);
  battery `3bae11e9…`, counter `c666323a…` = manifest.
- **C1 falsified as an instrument.** Wave seats ExecIsolation (b) and CriticClaims §2-a: the counter runs each roster
  gate under its roster file name, and the gate's argparse usage text returns it through the launcher. The L1's
  usage oracle (`after/forgeries/usage-oracle.py`, evaluates no rule) reads 3/3, 62/62, `verdict met` rc 0 in three
  runs on the frozen counter, 65 hits per run (`after/forgeries/usage-oracle.receipt.txt`). Honest stop (lesson M3,
  QUALITY 129).
- **Wave w1** (13 seats, `.ufo/waves/round-89/w1/`): ExecReplicate replicated C1 3/3, 62/62, 0 errors ×3 (clone at `665408cc`); ExecIsolation and CriticClaims found the file-name leak (above), CriticClaims also `--runs 0` → `met`, extra roster files not voided, vacuous preflight clauses, the AF_UNIX path crash (exit 1 at a scratch root over 45 bytes) and that the KEY-EQUALS fix left `path =` uncertified (`w1/CriticClaims.md` §2, §6); MutCounter 11 counter mutants, 4 killed by committed controls, 6 survive; MutBattery 19 battery mutants, 16 killed, every r89 family load-bearing, 62/62 negatives 10/10 over 10 runs; MutHeldOut held-out gate mutants r88 10/22 → r89 11/22; CriticForgers 37/38 docstring forgers killed; ReviewBattery 11/12 families sound, R1 wrong for blanks before CRLF (F1, routed R89-R2); ReviewEntry 7 support + UF1/header partial (fixed); ScoutSources pins byte-identical to the tag, v12.9.5/v12.9.6 upstream, 4 of 22 candidate rows folded into UF7/UF8; ConnectorOverlap 17 sibling hits, no conflict; ExecLints registry 142/142, headers 105/105, census rc 0, selftests 15/15, 14/14. Per-seat table: `corpus/lessons/round-89.md` "Wave w1". All 13 seats settled; `w1-results.json` carries `output: null` for every seat (orchestrator kernel restart note); each seat's report file is its evidence; no dead seat.
- **Integration.** Entry UF1, UF3, UF6, UF8 and header reworded on ReviewEntry P1–P5; QUALITY 127 (correction sweep),
  128 (no certify-by-draw), 129 (one control per channel); lesson `corpus/lessons/round-89.md` (Inputs, Gate,
  Errata, Mistakes M1–M3, wave summary, Routed); README r89 section; LOG entry; SCORECARD measured outcome.
- **Misroot sweep.** `git -C /home/vgpnk/Projects/shokunin status --porcelain`: untracked `trail-ids.txt` (1 byte,
  mtime 20:36:24, before this round's launch at 21:41:53; content `,`, no lane/round name) and
  `.scratch/run15-wrapup/…` (orchestrator-owned): neither is this round's; nothing moved.

## Landed changes

| Commit | What | LOG.md |
|---|---|---|
| `fba764ca` | freeze: counter r89, roster 65 gates, probe, controls sources, host receipt, census-before, declaration | Round 89 "Freeze" |
| `dddc82c6` | control receipts, both layouts | Round 89 "Controls" |
| `81f68d00` | candidate battery r89, registry rows, entry UF1–UF8, S361–S363, pinned sources, README r88 correction, dev receipt | Round 89 "Candidate" |
| `665408cc` | C1 receipt at `81f68d00` (clone), wave spec + dispatch | Round 89 "C1 measured" |
| `96a582c8` | measured outcome, usage-oracle forgery receipt, canonical receipt, robustness probe, M1 sweep, entry fixes, QUALITY 127–129, lesson, README r89 | Round 89 "Landing" |
| `7f3f30b3` | wave w1 evidence (13 seat reports + receipts), results, UF7/UF8 narrowing + S352 anchor, SCORECARD addendum, lesson wave summary + Routed, LOG, C1 receipt at `96a582c8`, census-after | Round 89 "Wave w1" / "Landing" |

## Before → after measurements

| Claim | Counting command | Before | After | Measured at | Verdict |
|---|---|---|---|---|---|
| C1 | `python3 tools/battery-discrimination-r89.py --battery tools/limine-pin-battery-r89.py --runs 3 --scratch "$S"` | do-nothing (r88 battery) 3/3, 46/46/45 of 62 (canonical), 46/46/46 (clone), at freeze `fba764ca` | 3/3, 62/62, 0 errors ×3 | `81f68d00` (clone), `665408cc` (canonical), `96a582c8` (clone; `after/measured/c1-receipt-96a582c8.txt`); tools unchanged since `81f68d00` | target met on the frozen predicate; **NOT VERIFIED** — a non-behavioural usage-text oracle reads the same 3/3, 62/62 ×3 (`after/forgeries/usage-oracle.receipt.txt`) |
| C2 | none (exploratory); prior state `git grep -n -i 'boot_dispatch\|uri_hdd\|fslabel_dispatch\|allow_menu\|measured_boot' dfeaab29 -- corpus/knowledge` → empty | — | entry UF1–UF8 | `81f68d00`, reworded at `96a582c8` | pending non-author `unprovable-but-better` |

## Sources & frontier

Census `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin tsukuroi`: round start rc 0,
360 rows, 52 W04, `tsukuroi ok` (`.ufo/waves/round-89/before/census-before.txt`) → round end rc 0, 363 rows, 52 W04,
`tsukuroi ok` (`.ufo/waves/round-89/after/census-after.txt`). Row count: `grep -c '^| S[0-9]' corpus/SOURCES.md`
360 → 363. Rows added by tier: A +3 (S361 chainload.c code, S362 panic.s2.c code, S363 own-work host receipt).
Rows touched old→new: S350 anchor + `157-160 (measured_boot)`, used-by + r89 entry; S351 anchor + `46-63`, `109-243`,
`344-366`, `372-376`, used-by + r89 entry; S352 anchor + `488-492` (UF7, after ScoutSources SR11), used-by + r89 entry; S353 anchor + `1719-1730`, used-by + r89 entry; no status/recheck change.
Gate (URL, access date, ≤25-word located quote, one REJECT — Limine trunk as a host-behaviour source):
`corpus/lessons/round-89.md` `## Gate`. Frontier rows advanced: README "Round 89" frontier (counter successor R89-R1,
rule fidelity R89-R2, held-out clauses R89-R4); the r88 bullets "Counter successor owed" and "Clauses r88 leaves
uncertified" are answered except the name leak. Sourced claim: C2 cites S361/S362/S363 opened this round.
Mined mistake: three (M1 correction not swept, M2 certify-by-draw, M3 uncontrolled name channel), each with a fix
shown able to fail (QUALITY 127–129 receipts).
Assimilation: none (no `merge/tsukuroi/` theme fits the Limine URI-failure surface). considerthese: latest
`considerthese/2026-10-26.md`, not mined this round.

## Trend verdicts

- **expansion — unprovable-but-better.** New ground (prior grep empty; UF1–UF8 on resource dispatch, efi failure,
  Secure Boot chainload, panic semantics), three tier-A rows; admission rests on C2's exploratory ruling.
- **quality — improved.** r88 routed 1 fixed with a sweep receipt; entry partials fixed before admission; QUALITY
  127–129 each shown able to fail; battery determinism probe 19/19 negatives killed 10/10; registry 142/142,
  headers 105/105.
- **discernment — improved.** The lane's own wave falsified its frozen counter and the L1 refused to read 62/62 as
  proof, re-ran the forgery on the frozen counter (3 runs) and filed C1 as not verified; g00's relabel was attacked
  and upheld (CriticClaims §4).

## SHONEN

- [~] SKILL.md decision tables / error patterns / checklists / cited sources. Evidence: registry rows
  `limine-pin-battery-r89`, `battery-discrimination-r89` (`SKILL.md` at `81f68d00`, coverage PASS 142/142).
  Non-author verification owed.
- [~] End-to-end domain task logged in LOG.md. Evidence: LOG.md "Round 89" — host entry protocols and Secure Boot /
  TPM state read → Limine resolver and `efi` loader read at the installed tag → UF8's host consequence and the entry's
  Operator actions.
- [~] Instructions executable without oral context. Evidence: battery and counter docstrings, `--selftest`, the
  entry's `recheck:` line; the counter's undocumented scratch-length limit (≤ 45 bytes) is a counter-example found by
  the wave. No no-oral-context retest was run.
- [~] No cross-domain bleed. Evidence: PROVINCE.md unchanged; ConnectorOverlap's sibling scan
  (`.ufo/waves/round-89/w1/ConnectorOverlap.md`, 17 hits, no conflict with UF1-UF8 or LP1-LP8).

## Other

- Author-side admission reading: C1 does not verify (falsified instrument; honest stop) and C2 awaits its non-author
  ruling, so the round is not admissible as declared on the author's reading; verdicts are left to the closure and
  the operator. No axis harmed (SCORECARD "Axes now" unchanged; census, registry and header gates PASS).
- Round shape: ONE v1 wave (`ufo-wave-policy.json`, band 8–16) of 13 seats; no residual call; round total 13.
  §3 planner seat held by the L1 (validator rejects `planner`).
- Stale-lane: respawn-per-round driver; no other mission of this lane is open.
- Tool installs: none.
- L0 questions: none new; `tsukuroi | round-86 | HOST INCIDENT` (pins on `/boot/limine.conf` lines 30 and 38) stays
  open and operator-owned.
- Scratch: `/fast/scratch/hyaku/tsukuroi-r89/L1` removed after landing.
- r88 routed 4 (report author date): the first fleet commit of this report, `ea28e55b`, carries author date
  23:08:53 (commit date 23:15:41), earlier than the lane commit `7f3f30b3` (23:15:01) it cites, although the file was
  written after it. Cause, read in `scripts/hyaku/fleet-commit.sh` lines 82-84: the helper runs `jj metaedit
  --update-author` (identity only) and `jj commit`, so the author timestamp is the creation time of the fleet's jj
  working-copy change, not the commit time. This amendment is committed through the same helper to give a readable
  chronology; the helper is fleet-owned and not edited (an `--update-author-timestamp` flag would fix it).
