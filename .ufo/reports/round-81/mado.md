# mado round 81 — the overflow rounding, the auto-zone gate, and two matcher classes

Lane: `mado` (`mado-shokunin`). Round 81, hyaku run 15, attempt 1. Base
`c702094ace5dd9b2b5e152951b4b2f4dd578f8b6`; freeze `0e2ccd2a8692825cac534f57246053b276be9f13`;
landing tip `2cbd3a137d16ed8f81874ed9b566acc270b9cb79` (lane `master`, pushed). Frozen declaration:
`mado-shokunin/.ufo/waves/round-81/claims-declaration-r81.md`. Round shape: ONE v1 wave of 14 seats
(policy band 8–16) and zero residual seats; the L1 holds the canonical planner seat (the validator
rejects `planner`) and the bounded planning data-walk rides the two scout items.

## Work performed

Declared claims (frozen before data):

- **C1 — coverage (capability acquisition).** The bar-footprint join models the three reachable
  classes round 80 recorded as `NOT_MODELLED` (`corpus/knowledge/bar-footprint-composition-r80.md`
  §11): hyprutils `CBox::round`'s coupled origin/far-edge rounding (a panel one pixel wider than its
  bounds lands at `x=-1, w=1002`, not `0/1001`), gtk-layer-shell's auto exclusive zone (gated on
  `horiz XOR vert`, sized from the allocation, plus the unanchored margins — so a corner, a parallel
  pair and an all-four anchor set reserve nothing even with an explicit `exclusiveEdge`; a left
  dock's zone reaches the left rule and the attribution vector; a dynamic band is a named refusal),
  and the `hyprutils >= 0.14.0` pin that licenses the tag.
- **C2 — operability.** The read-only runbook gains an action-column matcher
  (`omarchy menu keybindings --print | cut -c36-`: the `%-35s` padding pins the separator's column,
  the action is non-empty and trimmed and carries no second arrow — and no entity rule, because the
  payload escapes markup only on some lines) and a `pgrep -x waybar` matcher that binds the PID list
  with the exit status (a state pair, never a frozen value).

Work items, each with its evidence pointer:

- **Instrument build (C1).** `tools/mado-barfoot.py` `r80-v1` → `r81-v1`: `std_round`/`cbox_round`
  (the coupled rounding), `arranged_box` in doubles, `surface_zone` rewritten to gtk-layer-shell's
  gate and allocation rule, and the refusal deferred past the empty-box skip so the carried
  `empty-box-skip` case still skips. Selftest 111 → 121 checks (`git show 0e2ccd2a:tools/mado-barfoot.py`;
  `python3 -I tools/mado-barfoot.py --selftest` → `MADO_BARFOOT_SELFTEST: 121/121`).
- **Frozen control sets.** `.ufo/waves/round-81/controls/c1-cases-r81.json` (39 cases; 33 carried
  parsed-equal, sha256 `ab8154a1…`) and `c2-runbook-cases-r81.json` (26 cases, 26 distinct anchors,
  sha256 `ae7ee90e…`), each with its generator (`make-c1-cases-r81.py`, `make-c2-cases-r81.py`)
  whose comments name the source arithmetic for every new expectation.
- **Instruments (C2).** `quality/counters/c1-r81-overflow-auto.py` (selftest 72/72, 28 mutants) and
  `quality/counters/c2-r81-runbook.py` (selftest 88/88, 23 mutants), plus the two new SKILL.md
  runbook rows and the three r81 registry rows (`SKILL.md:798-800`).
- **Do-nothing controls, before any data.** The held round-80 tool on the 39-case set:
  `cases=39 correct=33 mutants=28 killed=20 base_correct=33/39 carried=33/33 tool_selftest=111/111
  verdict=TARGET_MISSED` rc 1 (`receipts/control-c1-r81-at-base.txt`). The held round-80 runbook
  instrument exits 2 on the 26-case set (`receipts/control-c2-held-instrument-r81.txt`); the r81
  counter at the base rev exits 2 (`receipts/control-c2-r81-at-base.txt`).
- **Freeze and measurement.** Freeze committed at `0e2ccd2a`; measured there
  (`receipts/measurement-c{1,2}-r81.txt`) and again at the content tip `f3eb70c7`
  (`receipts/measurement-c{1,2}-r81-at-tip.txt`).
- **Sources (frontier).** Three rows opened and pinned: S478 (hyprutils `v0.14.0` `src/math/Box.cpp`,
  `CBox::round` `:51-63`, sha256 `2d04de99…`), S479 (Hyprland `CMakeLists.txt` `:150`,
  `set(HYPRUTILS_MINIMUM_VERSION 0.14.0)`, sha256 `97b8028a…`) and S480 (hyprutils `v0.14.2`, the
  installed version, byte-identical to S478 — `pacman -Q hyprutils` → `0.14.2-1`, `cmp` empty);
  `fetch/sha256-r81.txt` verifies 3/3.
- **Knowledge.** `corpus/knowledge/bar-footprint-rounding-auto-r81.md` (six sections plus a
  same-round errata block, every proposition anchored to S478/S479/S480/S464/S470), indexed in
  `corpus/README.md:183` with the
  `## Frontier` bullet at `corpus/README.md:133`.
- **Lesson and mistakes.** `corpus/lessons/round-81.md` with four `## Mistakes` rows (M81-1…M81-4),
  each shown able to fail, and a `## Gate` block (census, the two rows, the assimilation verdict).
- **Record.** `SCORECARD.md` round-81 section (claims, observations, capabilities, planned 82, axis
  table), `LOG.md` round-81 entry, `PROVINCE.md` round-81 refinement.
- **Wave.** One v1 wave, 14 seats (`w1-spec.json`, `w1-dispatch.json`, `w1.ready`, `w1.ready.dispatched`);
  seats: 2 scout, 1 connector, 3 executor, 3 scribe, 2 reviewer, 1 critic, 1 mutation-tester, 1
  sentinel. Attack share by the policy list (reviewer ×2, critic, mutation-tester) = 4/14 = 28.6 %;
  the sentinel is a security seat and is named separately. Connector seats: 1 (≤2).
- **Live observation (freshness).** The host join on today's capture is CLEAN
  (`receipts/live-join-r81.txt`): DP-1 3440x1440, waybar level 2 at `0,0,3440,26`,
  `band=26 expected=26 CLEAN`; the monitor's `description`/`serial`/`make`/`model` were replaced
  with `<redacted>` before the capture was kept.
- **Repairs of the round-80 closure.** D1 appended errata only (this report is filed once); D2 the
  report's registry pointers are measured at the tip (`SKILL.md:795-797` for the r80 rows,
  `:798-800` for the r81 rows); D3 every pointer carries its `grep -n` line; D4 the blank line
  before M80-6 in `corpus/lessons/round-80.md` is removed; D5 every seat is named with its artifact
  count below; D6 the attack share is stated by the policy list with the sentinel separate; D7 the
  wave-done line has a committed receipt (`receipts/wave-done-r81.txt`) — and that receipt's
  verdict is `MISSING`: `check-wave-done` requires a report per dispatched seat, and the five empty
  attack seats fail it (`dispatch-mismatch missing=5`, exit 1). The round discloses that rather than
  claiming D7 closed.

## Landed changes

| Change | LOG entry | Commit |
|---|---|---|
| Freeze: `tools/mado-barfoot.py` `r81-v1` (coupled `CBox::round`, the auto gate, the deferred dynamic-band refusal), the two runbook rows and the `(round 81)` heading, both successor counters, their generators and frozen sets, the declaration, two ledger rows, the two source pins | `LOG.md` round-81 «Instruments» | `0e2ccd2a` |
| Measured receipts at the freeze, the one-v1-wave spec/dispatch/ready | `LOG.md` round-81 «Claims» | `6fffb0db` |
| The C1 knowledge entry, S478/S479 in `corpus/SOURCES.md`, the lesson, the README index row and frontier bullet, the SCORECARD round section, the LOG entry, the PROVINCE refinement, the D4 repair, the assimilation collision evidence | `LOG.md` round-81 (whole entry) | `f3eb70c7` |
| The at-tip measurements and the harm-watch receipt (index 100/100, ledger 148/148, axis `mismatched=0`, held instruments byte-identical) | `LOG.md` round-81 «Instruments» | `6006feb5` |
| The scribe's entry adopted, the host-version row S480 (hyprutils 0.14.2 byte-identical to S478), the lesson's routed repairs (M81-2's receipt, the F1 correction, F2/F3/F6), the end census | `LOG.md` round-81 «Sources»/«Mistakes» | `2034761b` |
| Wave evidence: nine seat reports, the results file with the five empty seats, the wave-done receipt (verdict `MISSING`, exit 1), the S480 pin (host hyprutils 0.14.2 byte-identical to S478) | `LOG.md` round-81 «Wave» | `6ac5863f` |
| The wave-done receipt and the LOG/SCORECARD disclosure of the five empty attack seats (the final lane tip) | `LOG.md` round-81 «Wave» | `2cbd3a13` |

## Before → after measurements

**C1 — coverage.** Counting command (the declaration prints the same argv):

```sh
python3 -I quality/counters/c1-r81-overflow-auto.py --repo . \
  --rev REV --base-rev c702094ace5dd9b2b5e152951b4b2f4dd578f8b6 \
  --controls .ufo/waves/round-81/controls/c1-cases-r81.json \
  --carried .ufo/waves/round-80/controls/c1-cases-r80.json --scratch-root DIR
```

- **Before** (`REV=c702094a`, the unchanged round-80 tool, receipt `receipts/control-c1-r81-at-base.txt`):
  `cases=39 correct=33 mutants=28 killed=20 base_correct=33/39 carried=33/33 tool_selftest=111/111
  verdict=TARGET_MISSED`, rc 1. The held model passes its own thirty-three and fails all six new
  cases; the six new mutants' anchors do not exist in it, so they print `killed=no
  reason=anchor-absent` and `killed=20`.
- **After** (`REV=f3eb70c7`, receipt `receipts/measurement-c1-r81-at-tip.txt`): `cases=39 correct=39
  mutants=28 killed=28 base_correct=33/39 carried=33/33 tool_selftest=121/121 verdict=TARGET_MET`,
  rc 0. The same line at the freeze `0e2ccd2a` (`receipts/measurement-c1-r81.txt`).
- Bounded `10 × 39/39` → 10.0000 on this finite model-space (the six new classes plus the carried
  thirty-three); it is not a re-score of the lane's earlier coverage rubrics.

**C2 — operability.** Counting command:

```sh
python3 -I quality/counters/c2-r81-runbook.py --repo . \
  --rev REV --controls .ufo/waves/round-81/controls/c2-runbook-cases-r81.json \
  --carried .ufo/waves/round-80/controls/c2-runbook-cases-r80.json --scratch-root DIR
```

- **Before** (`REV=c702094a`): the r81 counter refuses at setup (`SKILL.md in the working tree is
  not the measured revision's bytes`, rc 2 — `receipts/control-c2-r81-at-base.txt`), and the held
  round-80 instrument refuses on the successor set (`control set carries 26 cases, frozen target
  expects 24`, rc 2 — `receipts/control-c2-held-instrument-r81.txt`). The before state is the
  capability's absence, declared as such, not an invented measurement.
- **After** (`REV=f3eb70c7`, receipt `receipts/measurement-c2-r81-at-tip.txt`): `cases=26 executed=26
  matched=26 shapes=21/21 anchors=26/26 rows=26/26 control_new=0/2 mutants=23 killed=23
  verdict=TARGET_MET tree=bound`, rc 0. `control_all=15/26` is printed as an observation, never a
  predicate.

**Harm watch** (`receipts/harm-watch-r81.txt`, measured at `f3eb70c7`): index 99/99 → **100/100**
(`indexed=100/100 missing=0 dangling=0 duplicates=0 coverage=10.0000/10`); ledger 146 → **148**
(`population=148 ledger_rows=148 uncovered=0 dangling=0 bad_pointer=0 empty_desc=0`); axis table
`checked=3 mismatched=0`; gate `MADO_SELFTEST: 460/460` with `tools/mado-verify.sh` blob identical
at base and tip; the five held checkers/instrument blobs identical at base and tip
(`landing-counters.sh`, `check-tool-ledger.py`, `check-axis-scores.py`, `check-index.py`,
`mado-verify.sh`); no older SOURCES row's `status`/`recheck`/`used-by` cell moved.

## Sources & frontier

Census counting command:

```sh
/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin mado
```

- **Before** (round start, `receipts/census-start-r81.txt`): **412** registry rows
  (`grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}' corpus/SOURCES.md` → 412), exit 0 with the standing
  W04 duplicate-URL warnings and W01 S277.
- **After** (landing tip, after the wave's S480): **415** rows, exit 0 (the same standing warnings;
  the three new URLs are not duplicates).
- **Rows added:** 3, all tier A, all `mined`: **S478** (hyprutils `v0.14.0` `src/math/Box.cpp`),
  **S479** (Hyprland `CMakeLists.txt` `:150` pin) and **S480** (hyprutils `v0.14.2`, the installed
  version's bytes, byte-identical to S478). Pinned under `.ufo/waves/round-81/fetch/`;
  `sha256sum -c fetch/sha256-r81.txt` → 3/3 OK.
- **Rows touched old→new:** none. No `status`, `recheck` or `used-by` cell of an older row moved; no
  row was superseded or rejected this round.
- **Frontier rows advanced:** the round-80 entry's `NOT_MODELLED` class list (§11 items 1–3) is
  superseded by anchored ground in `corpus/knowledge/bar-footprint-rounding-auto-r81.md`; item 4 (a
  declared surface without an `exclusive` key) stays open and is named as such in the entry and the
  SCORECARD's planned row.
- **Sourced claim:** C1 rests on S478 (opened and pinned this round), S479 (the tag pin) and
  S480 (the installed version's identity).
- **Assimilation:** none — the staged `/home/vgpnk/Projects/shokuknow/merge/mado/` package was built
  against a 192-row registry and collides with the lane's id space on **94** ids
  (`.ufo/waves/round-81/assimilation/collisions`; `reg-ids` 414, `staged-ids` 147), and no staged
  entry touches this round's ground. Reject sample (read, not adopted):
  `knowledge/corpus/knowledge/host-bar-producers-r28.md` — it amends a sibling entry from the same
  package, so adopting it alone dangles the parent, its ids collide, and its 6354 B host-config claim
  is a 2026-10-23 read the r80 connector flagged for re-measurement. Flip: adopt both entries
  together after the host config is re-read and the ids are renumbered by document. No admit is
  claimed because nothing was adopted.
- **considerthese:** `/home/vgpnk/Projects/shokunin/mado-shokunin/considerthese/` exists;
  `2026-10-28.md` proposal 4 (the live-tool table) remains available and unimplemented, as the
  SCORECARD's planned row records. Nothing was mined from it this round.

## Trend verdicts

- **expansion — improved.** One net-new admitted knowledge entry on ground the coverage map did not
  hold (the composition's rounding and the auto gate), `source:` S478/S479; index 99/99 → 100/100;
  registry 412 → 414; two capability rows demonstrated this round.
- **quality — improved.** The round-80 §11 limits for the overflow tie, the auto gate and the
  vertical zone are superseded by anchored accounts; four mistakes are mined with byte-exact
  pointers (two of them caught inside the round before the freeze and pinned as positive/negative
  samples); 28 + 23 mutants are killed; the gate and every held instrument are byte-identical.
- **discernment — improved.** The round's own rules were falsified against live output before the
  freeze — the entity rule died on a bare `&` in the real payload and the `pid_state` matcher died
  on a padded PID — and both corrections are now bound by samples/negatives rather than prose. The
  assimilation verdict is a refusal with a count (94 collisions) and a flip condition, not an
  adoption. The limits the round keeps (dynamic allocation refused; the declaration default open;
  pinned versions not host reads) are named, not smoothed.

## Wave findings

Seats: 14 in one v1 wave (`w1-spec.json`, `w1-dispatch.json`, `w1.ready`,
`w1.ready.dispatched`); role mix: 2 scout, 1 connector, 3 executor, 3 scribe, 2 reviewer, 1 critic,
1 mutation-tester, 1 sentinel. **Nine seats settled with an artifact and `STATUS: ok`; five settled
empty and wrote nothing** — both reviewers (`R81ReviewerC1`, `R81ReviewerC2`), the critic
(`R81CriticClaims`), the mutation-tester (`R81MutC1Counter`) and the sentinel (`R81Sentinel`). The
wave results (`w1-results.json`, 14 entries) carry `output` length 0 for those five and no seat
directory exists for any of them. That is an evidence gap, disclosed and not backfilled (QUALITY
115): this round's claims are **not** independently attacked by a reviewer/critic seat, and the
closure's non-author check is the only outside attack they receive. The nine productive seats
include two independent re-derivations of the new case arithmetic and one independent mutation
census, which is what the round can honestly offer against the frozen instruments. Per-seat findings
(each in `.ufo/waves/round-81/w1/`, `STATUS: ok` in the seat report or its `findings.md`):

- **R81ScoutLive** (scout) — live recon: the host join reproduces `receipts/live-join-r81.txt`
  (`box=MATCH reserved=EQ band=26 expected=26 verdict=CLEAN`, DP-1 3440x1440, waybar level 2 at
  `0,0,3440,26`); the host carries exactly two layer surfaces (waybar level 2, wallpaper level 0);
  three named limits — the reply is already rounded (`fractional coords: []`), the join's default run
  asserts a zero static reserve instead of reading `monitors.conf`, and `swaybg`'s no-zone state is an
  inference. It also read the installed hyprutils as **0.14.2**, which the round closes with S480
  (byte-identical to the v0.14.0 pin).
- **R81ScoutModel** (scout) — re-derived all six new case expectations by hand from the bytes and
  agreed field-for-field; its one substantive note is that `auto-left-dock`'s fixture `gt` vector
  (`0,26,0,0`) does not carry the left band, so `reserved=EQ` certifies the top 26 only — adopted as
  the entry's §7 item 5. It probed four unpinned classes (P1 auto-left margins: right; the rest
  recorded in its report) as round-82 ground, proposing no target.
- **R81ConnSiblings** (connector) — **no sibling lane claims either ground**, and no sibling
  instrument implements either mechanism; it names the disclaimers (`game-dev-3d/PROVINCE.md:75`,
  `kotoba`, `tsukuroi`) and four lexical homonyms a token census must not merge (browser input
  "chords", kake's `is-active` line, `kimi-webbridge`'s pgrep, a `waybar` count). The staged
  `merge/mado/` package touches neither ground.
- **R81ExecC1Run** (executor) — ran the C1 counting command verbatim at the freeze: `TARGET_MET`;
  hand-derived `overflow-tie-negative` and `auto-left-dock` from S478/S470/S464 without reading the
  tool, then compared every field of the tool's run: **AGREE on every field for both cases**.
- **R81ExecC2Run** (executor) — ran the C2 command verbatim: `TARGET_MET`; executed both new rows by
  hand (193 lines, byte 36 = space, arrow at bytes 37-39, `pgrep -x waybar` → `1720` rc 0); measured
  exactly one bare `&` in the live action column and explained it from the payload's
  `if (action == "")` branch (`S473:141` vs `:143`, escaping `:156-160`), confirming the frozen
  grammar's bound outcome.
- **R81ExecMutants** (executor) — independent mutation census (each mutant hand-applied, scored
  against the six new fixtures, separating field named): all six new mutants are killed, each by a
  named case (`tie-round-trunc`/`round-width-spec` → `overflow-tie-negative`; `auto-gate-open` →
  `auto-corner-edge` + the other two; `auto-gate-and` → `auto-left-dock` + the two balanced-anchor
  cases; `auto-axis-swapped` → `auto-left-dock`; `auto-dynamic-kept` →
  `auto-dynamic-band-refused`), and deleted anchors print `reason=anchor-absent` with no traceback.
- **R81ScribeEntry** (scribe) — drafted the 363-line C1 entry that is adopted as
  `corpus/knowledge/bar-footprint-rounding-auto-r81.md` (its §2 arithmetic and §7 limits, including
  the non-bar-edge limit and the still-open declaration default, are the published text).
- **R81ScribeSources** (scribe) — drafted and verified the two rows against the pinned bytes and
  the census; found and removed four self-referential symlinks it had created inside the lane while
  probing path resolution (M81-5).
- **R81ScribeLesson** (scribe) — drafted the lesson and routed six observations: its **F1** (the
  Gate's reject sample wrongly said the staged ids collide — they are free) is corrected here and in
  the lesson; **F2** (the frozen C2 counter's tree-binding means the freeze rev is no longer
  re-runnable once SKILL.md moves) is answered by the at-tip measurement; **F3** (no unit checks for
  the two new matcher kinds) and **F6** (the C2 docstring still says `PRED-C2-r79-v1`) are deferred
  to round 82 because editing the frozen instrument would break its cited sha256; **F4/F5** are
  resolved (the at-tip receipt is now committed, and M81-2 cites the committed strip-regression
  control).


## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — the r81
  registry rows are `SKILL.md:798-800` (probe, C1 gate, C2 gate) and the two new runbook rows are
  `SKILL.md:270-271`; `corpus/lessons/round-81.md` M81-1…M81-4 are the round's error patterns.
- [~] At least one end-to-end domain task executed and logged in LOG.md — the two counting commands,
  the live join (`receipts/live-join-r81.txt`, `CLEAN`) and the host captures are executed and logged
  in `LOG.md` round 81; no outside-lane verifier stands behind it this round.
- [~] Instructions executable by an agent without oral context — nine of the wave's 14 seats executed
  from the frozen declaration and the runbook rows (two independent case re-derivations and one
  independent mutation census among them); five attack seats settled empty, so this box's evidence is
  the nine reports plus the frozen commands, not a clean 14/14.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — `PROVINCE.md`'s round-81 refinement names
  the new refusal class and the two read-only verbs; the connector seat's sibling scan is reported
  below; PROVINCE.md remains the read-only boundary, not a fresh outside-lane approval.

## Stale-lane

`Stale-lane: no` — respawn-per-round driver, attempt 1; no earlier `lane-dead-no-report mado
round=81` line was present at round start (`.ufo/watchdog.log` checked), so no inherited uncommitted
output existed to reuse or discard.

## Tool installs

None. No tool was installed or upgraded this round; the pacman pause was respected (no `pacman`
transaction ran).

**Seat tally (D5).** 14 dispatched, 14 settled, 0 running; artifacts: 9 seat reports and 9
`findings.md`, 0 dead-with-artifact, 5 empty-with-no-artifact (`R81ReviewerC1`, `R81ReviewerC2`,
`R81CriticClaims`, `R81MutC1Counter`, `R81Sentinel`). Attack share as dispatched: 4/14 by the policy
list (2 reviewer, 1 critic, 1 mutation-tester = 28.6 %) plus the sentinel named separately; attack
share with an artifact: 0/14, because every attack seat settled empty. The round reports that
plainly rather than counting seats that produced nothing.
