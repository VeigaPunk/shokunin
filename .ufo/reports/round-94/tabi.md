# tabi — round 94 report

L1 `TabiR94` (attempt 1). Lane `tabi-shokunin`, base `d7744d043ca4b606124dfaa7f385acfa89b352ff`, final
lane hash `e0562f8a9cd352261d007b6c9f16c14bd86a7864` (`git ls-remote origin refs/heads/master` prints it).

## Work performed

Declared claims: ONE — **C1, coverage axis, capability acquisition `chromium-oopif-backendnode-collision-linux`**
(predicate `C1-BACKENDNODE-COLLISION-R94`, sourced S233/S234). It covers what a cross-site iframe file
chooser's `backendNodeId` B resolves to when it is sent on the PAGE session. With pad 0 it collides with
the parent's own root. With 300 painted spans before the input it misses. On the same-site control it is
the input. This is r93 declared limit 3. All six axes were at 9, so coverage was a lowest tie.

- Protocol load: the round prompt, the r93/r92 verifier spot-checks, the SCORECARD r93 section, the r93 plan and lesson, and the r93 wave artifacts. Pointer: `plans/round-94.md:1-12`.
- Pre-freeze probes found the M-arm fixture. Hidden padding leaves B = 2. Painted padding gives B = 302 and a miss. Receipts: `.ufo/waves/round-94/probes/`.
- Sources opened and staged: Blink `identifiers_factory.cc` and `node.cc` at tag 155.0.8059.84. Path: `.ufo/waves/round-94/sources/sha256.txt`.
- Instruments built: driver `scripts/chrome-cdp-backendnode-collision-round94.mjs` (`518f40ff9b34…`), counter `scripts/check-backendnode-collision-round94.mjs` (`d7fd2cbe0899…`) and battery `scripts/negatives-backendnode-collision-round94.mjs` (`b750ee17b778…`).
- Freeze commit `2308b6ce`. It carries the plan, `claims.json` (frozenAt 21:49:37, committed 21:49:42), the instruments and the controls. It was made before the scored run and before the wave.
- Controls, attempt 3 (`.ufo/waves/round-94/controls/rc.txt`):
  - no-work: base rc 128; the r93 receipt gives rc 1 with 14 ids.
  - wrong-site gives rc 1. pad-0 gives rc 1.
  - positive: rc 0 at 165 checks.
  - busy-port, counter-SIGTERM and driver-SIGKILL each give `setup` rc 2 with 0 chromium left.
  - battery: 74/74.
  - Attempts 1 and 2 are kept and disclosed (`rc-attempt1.txt`, `rc-attempt2.txt`, `rc-setup-attempt1.txt`).
- Scored commit `012776cf`: `--live` rc 0, `clean`, 165 checks, 0 findings, nonce `tabi-r94-live-240f4c5100c3`. Receipt sha256 `8070fcdc…` (`.ufo/waves/round-94/scored/c1-live.json`).
- Wave `w1` ran 12 seats; all settled and every one filed. Every C1 verdict is `neutral` (`.ufo/waves/round-94/claim-falsification.tsv`, 15 rows).
- Records commit `09479b6d`:
  - knowledge note `corpus/knowledge/chromium-oopif-backendnode-collision-round-94.md`
  - SOURCES rows S233/S234 plus a search-log entry
  - lesson `corpus/lessons/round-94.md` (gate, 2 mined mistakes, corrections, wave)
  - SKILL `## Round 94 gate registry`, README `## Round 94 coverage`
  - appended corrections to the r92 note, the r93 note and the README r93 summary (R94Connector)
  - SCORECARD and LOG round-94 sections
- Tip commit `e0562f8a`: tip `--live` re-run rc 0, `clean`, 165 checks, revision `09479b6d` (`.ufo/waves/round-94/scored/c1-live-final.json`). Census end exit 0. Freeze-stamp gate rc 0 and log-section-claims gate rc 0 at the tip (`scored/freeze-stamp-r94.json`, `scored/log-claims-tip.json`).
- Round shape: ONE v1 wave of 12 seats under `ufo-wave-policy.json` (band 8–16). No residual call; round total 12.
  - Roles: executor ×3, critic ×3, mutation-tester, reviewer, sentinel, scout, scribe, connector.
  - Attack roles (reviewer + critic + mutation-tester) are 5/12, 42 %. The prefile gate counts 7 attack seats.
  - The L1 held the planner seat. No seat died.
- Pre-file ledger: `PREFILE-FALSIFICATION: pass claims=1 rows=15 attack_seats=7 findings=0` (exit 0).

## Landed changes

| commit (lane) | what | LOG.md entry |
|---|---|---|
| `2308b6ce` | freeze: plan, claims.json, 3 instruments, controls (attempts 1-3), probes, staged sources, census start | `## Round 94` (LOG.md, freeze paragraph) |
| `012776cf` | scored `--live` run + corpus evidence receipt + `c1-live.record.json` naming the committed receipt | `## Round 94` (scored commit) |
| `09479b6d` | records: note, S233/S234, lesson, SCORECARD/LOG/SKILL/README, appended corrections, w1 evidence, ledger | `## Round 94` (records paragraph) |
| `e0562f8a` | tip re-run, census end, gates at tip | `## Round 94` (lane tip) |

## Before → after measurements

- **C1.** Counting command: `node scripts/check-backendnode-collision-round94.mjs --lane /home/vgpnk/Projects/shokunin/tabi-shokunin --expect-driver-sha256 518f40ff9b34727254a3bb0cd30603c70ce8488a911fa3a26a55273220f9686f --live --scratch <ABS> --ports <http,child,cdp> --json`.
  - Before, at base `d7744d04`: the counter is absent (`git cat-file -e` rc 128). The r93 receipt under the frozen counter gives rc 1 (14 ids). That is the do-nothing control.
  - After, measured at `012776cf`: rc 0, `clean`, 165 checks, 0 findings, 9 legs. Per-arm B values are 2/302/305.
  - Re-run at tip `09479b6d`: rc 0, `clean`, 165.
  - Seat reproductions:
    - R94Exec1: 2 runs, clean.
    - R94Exec2: 3 runs at 165 checks plus a `--reps 10` run at 522 checks, all clean.
    - R94Critic2: 1 run, clean.
- **Verdict: C1 verified on its frozen predicate** (pending non-author closure). Every wave artifact is neutral. No amendment and no narrowing.

## Sources & frontier

- SOURCES rows went 232 → 234. Counting command: `grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}' corpus/SOURCES.md`.
- Added by tier: A ×2 (S233 Blink `identifiers_factory.cc`, S234 Blink `node.cc`, both `mined`, recheck 90d). Rows touched old→new: none; S231/S232 are cited but not edited.
- Rejected: `dom_node_ids.h` (adds nothing S232 lacks). The R94Scout paint-path sites are leads, not rows. The lesson's `## Gate` records the URL, access date and a `wc -w`-counted ≤25-word quote (6 and 5 words).
- Frontier advanced: r93 declared limit 3 (whose node) is now measured. A new limit-3 frontier is recorded: which render pass mints the input's id (R94Critic3).
- Census, start → end: `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin tabi` gave exit 0 both times. Outputs: `.ufo/waves/round-94/census-start.txt` and `census-end.txt` (`tabi ok`; W04 warnings only, all on pre-existing rows).
- Mined mistakes, in `corpus/lessons/round-94.md` `## Mistakes`:
  1. Orphaned chromium / argv-rewrite sweep miss. It was shown able to fail: 12 and 13 survivors on attempts 1-2, then 0.
  2. r93 S232 word count: 8 recorded, 6 measured. Re-counted by R94Exec3.
- Sourced claim: C1 rests on S233/S234, which were opened this round.
- Assimilation: none. considerthese: this lane has no `considerthese/` directory.

## Trend verdicts

- **expansion: improved.** Knowledge went 106 → 107 (`ls corpus/knowledge | wc -l`), SOURCES 232 → 234, and one new capability row was added.
- **quality: improved.** The counter now maps a signalled or interrupted driver, and its own signals, to `setup`, and it sweeps orphaned chromium. Three setup controls show this, and they were shown able to fail in attempts 1-2. Three earlier tabi statements were corrected by appended sections. Battery 74/74; mutation kill 65/70.
- **discernment: improved.** S233/S234 were admitted. `dom_node_ids.h` and the paint-path leads were refused, each with a flip condition. The ledger rejects every seat artifact as a wording falsification, with reasons. Two glosses refuted by R94Critic2 were kept out of the note: "collision iff B ≤ parent max" and "always the parent root".

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — `SKILL.md` `## Round 94 gate registry` (verdict maps for counter/driver/battery); no non-author verifier named this round.
- [~] At least one end-to-end domain task executed and logged in LOG.md — `LOG.md` `## Round 94` (scored `--live` run `012776cf`, 9 legs, real Chromium 155); non-author closure pending.
- [~] Instructions executable by an agent without oral context — `plans/round-94.md` §Counting command, reproduced cold from the plan alone by lane-dispatched R94Exec1/R94Exec2/R94Critic2 (not non-author).
- [~] No cross-domain bleed (PROVINCE.md still accurate) — `PROVINCE.md` unchanged; R94Connector `.ufo/waves/round-94/w1/R94Connector.md` (0 sibling contradictions; own-lane corrections appended).

## Extras

- Stale-lane: respawn-per-round driver; no other mission of this lane is open.
- Tool installs: none (node 24, chromium 155, curl already present; pacman untouched).
- Routed to r95, also in the SCORECARD Planned line:
  - R94Sentinel F1: a same-UID writer can substitute the `--live` receipt.
  - F2: a chromium launch failure is scored `findings`.
  - F3: own-signal setup JSON lacks `driverRun`.
  - F4: a directory at the receipt path crashes the counter.
  - R94Mut battery gaps and over-reporting negatives.
  - Wave kill selectors must be scoped to the seat's own ports.
- Wave incident: R94Sentinel's mis-targeted kill ended R94Exec2's run3 attempt 1 (disclosed in `w1/R94Sentinel.md` §7). R94Exec2's cited run is the clean retry.
- Inherited state: none (clean tree at start; no earlier r94 attempt). Misroot sweep: `git -C /home/vgpnk/Projects/shokunin status --porcelain` shows only orchestrator-owned `.scratch/` entries; no seat file was misrooted.
- Open L0 questions: none.
