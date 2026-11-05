# kaidoku — round 90

Lane `kaidoku-shokunin`; round 90, attempt 1 on this L1 session. Three earlier attempts of the same
round died on provider failure (22:12:36, 22:31:25, 22:32:21 -03:00, `lane-dead-no-report` in
`.ufo/watchdog.log`) after the claim plan, the two counters, the wave spec and two base receipts had
reached the tree; those artifacts were re-verified here and reused, not re-declared, and the one thing
they lacked (a validated dispatch with substitutable prompts, a committed freeze container and a
`.ready`) was completed. Base `fc52cc9dc`; declaration `18b21f09`. Lane tip at filing: `6e47538b6bb8d42c64039a2feef2ae0e0548fbce` (`git ls-remote origin refs/heads/main`).

**Declared claims (2, distinct axes, causally separable).**
- **R90-C1 — coverage, capability acquisition (`T5-chain-szcpr-wrong-later`, Frontier → Core).** An
  *interior* first-segment `b_info` block's `sz_cpr`, overwritten with a different in-range value, is
  recoverable from the successor offset; the round-89 repair returns such a file byte-identical.
- **R90-C2 — depth, craft rule block 30.** The guard-and-control set a *superseding instrument
  revision* must inherit, as a ten-row table routing each revision defect class to the failure
  signature, the guard and the criterion.

Both axes are tied-lowest (all four owned axes sit at 10.0 on their finite proxies); round 88 entered a
capability, so the stagnation window restarted and no waiver is invoked.

## Work performed

- **Frozen the claims before data.** Plan `plans/round-90-claims.md`; container
  `.ufo/waves/round-90/claims.json`; freeze precheck at the declaration revision
  `18b21f09`: round-90 container `CLEAN`, red control (round-83 container) `FLAGGED` with
  `CLAIM_NO_COUNTER_PATH:R83-C1`, `met true`, exit 0 —
  `.ufo/waves/round-90/pre/freeze-precheck-at-declaration.json`.
- **Repaired the inherited wave spec and dispatched one v1 wave.** 11 of 13 seat prompts shipped a
  literal `{LANE}` because the substitution pass had touched `items[].task` while the payload field is
  `items[].prompt`; every string field was rewritten, the wave re-validated (13 spawn, 0 resume,
  policy band 8–16, attack 5/13 = 38.5 %, one connector) and the scan for `\{[A-Z][A-Z0-9_]*\}` printed
  `[]` before `<wave>.ready` was written (`.ufo/waves/round-90/r90-w1-spec.json`,
  `r90-w1-dispatch.json`, `r90-w1.ready`).
- **C1 measured at three revisions and re-taken after the wave's instrument findings.**
  `tools/round-90/upx-later-block-battery.py` against `tools/round-90/upx-break-repair.py`:
  `P1 6 of 6; P2 4 of 4; P3 4 of 4`, controls `N1-refuse-plain`/`N2-corrupt-payload`/
  `N3-intact-idempotent`/`isolation`/`carrier_blind`/`no_work`/`cheat_repack`/`rea` all true, exit 0 —
  `.ufo/waves/round-90/l1/scores/c1-at-499d2183.json` (8m41s, the landing receipt), with
  `c1-at-declaration.json` and `c1-at-5f8ea076.json` kept as the pre-fix bytes' history.
- **Instrument supersession closed four wave findings before the landing run** (CriticClaims): the
  battery's `met` now *requires* the REA arm (`--no-rea` exits 1), `--rev` must name a commit in the
  repo (`rev_not_committed`, exit 2) and the receipt records the resolved commit plus the worktree's
  dirty-path count, the isolation sentence states the code (`["in"]` or `["in","out"]`), and the repair
  docstring states the `u_len` filter its code applies — predicate, populations, tampers, controls,
  carrier pins and label unchanged; both selftests green (17 and 8 cases). Entry
  `instrument_supersessions` in the container; commit `499d2183`.
- **C2 landed as block 30 and measured at the landed bytes.** The scribe's ten-row table
  (the ScribeBlock30 seat's draft, integrated verbatim; `.ufo/waves/round-90/w1/ScribeBlock30/block-30.md`) was integrated in place of the L1's first draft: `blocks 30, resolved 30,
  expect 30, unresolved []`, exit 0 at `8346eacc`
  (`.ufo/waves/round-90/l1/scores/c2-at-8346eacc.json`); base arm red at `fc52cc9dc`
  (`blocks 29 … met False`, exit 1, `pre/c2-depth-at-base.json`), and two red worlds from the wave
  (citation-only stub, out-of-bounds range) are refused.
- **Sources curated and one Frontier class moved into Core.** S313 (`src/p_unix.cpp`,
  `PackUnix::unpackExtent`), S314 (`src/p_lx_elf.h`, `o_binfo`) admitted; S315 (`NEWS`) rejected — all
  three opened this round, `## Gate` in `corpus/lessons/round-90.md`. Entry
  `corpus/knowledge/2026-11-04-r90-interior-block-szcpr.md`, PROVINCE `## Round-90 additions to Core`,
  README coverage row + index row + round-90 frontier note, QUALITY 172–176.
- **Round-89 closure answered.** The non-author spot-check's D-89-1…D-89-7 each carry a disposition in
  `corpus/lessons/round-90.md`; D-89-6's two dead pointers are repaired in place with the correction
  noted, and the missing round-89 SCORECARD record is written retroactively, labelled as written at
  round 90 (D-89-5).
- **Wave r90-w1 (one v1 wave, 13 seats):** executor 4, scribe 2, scout 1, reviewer 2, critic 1,
  mutation-tester 1, sentinel 1, connector 1; attack roles 5/13 = 38.5 %; the L1 held the planner seat
  (the validator refuses `planner`). **All 13 seats settled** (`r90-w1-results.json`): 13 of 13 delivered an output, 12 wrote a report or a
drafted artifact (`w1/*.md`), 0 dead. The wave's material findings: CriticClaims' four instrument
defects (closed by the supersession at `499d2183` before the landing run), ExecBlind's `boxes` gap and
MutCounter's quantified source-free cheat (QUALITY 174), ScribeEntry's last-block fall-through
(QUALITY 176) and the REA count flake, ScribeBlock30's landed block and base-presence gate,
ExecMutation's 17-mutant table (2 killed), ReviewerC2's red/green reconstruction, ReviewerC1's
no-falsification pass, ScoutUpxPack's pack-side S316 and anchor drift, SentinelScope's 27 hostile
inputs (6 untyped crashes, QUALITY 177). Round total 13 seats; no residual call, no second wave.

## Landed changes

| change | commit | LOG.md entry |
|---|---|---|
| Claim freeze: container, validated dispatch, base receipts | `18b21f092429383d498572a422bc7294beb0ce7e` | round 90, "Declared claims" bullet |
| The interior later-block class in Core: entry, S313/S314 admit, S315 reject, PROVINCE Core row, README coverage/index rows, craft rule block 30's first draft, census receipts | `5f8ea07692f15db14b659924ccda6df542b6ad3a` | round 90, "Sources and frontier" bullet |
| Instrument supersession (four CriticClaims defects) and the supersession's retaken pointers | `499d2183a67058d5648b51a2abf50c10012b1292` | round 90, "Measured" bullet |
| Landing receipts (C1 with the REA arm required, C2 re-measured, census-after) | `d39837859da2a36a87ccb4b13606c74f10f8a5f9` | round 90, "Measured" bullet |
| The scribe's block 30 integrated, entry limits (last-block fall-through, REA count flake), QUALITY 172-176, LOG and SCORECARD records for rounds 89-90 | `8346eaccce7cce23a84f08dee96f9bbeaa03c8ff` | round 90, whole entry |
| Wave evidence (results file, 12 seat reports, receipts), S316 admit, S311 anchor drift, QUALITY 177, lesson | `c264f7a49651dc4c5c6a7b9a0be81cae33186b08` |
| The mutation-tester's ten mutant trees relocated from `tools/round-90/` into its seat dir (M90-4 family) — the lane tip at filing | `6e47538b6bb8d42c64039a2feef2ae0e0548fbce` | round 90, "Wave" bullet |

## Before → after measurements

**R90-C1 — coverage (capability).** Counting command (frozen in `plans/round-90-claims.md` and
`.ufo/waves/round-90/claims.json`):

```
python3 -I -B tools/round-90/upx-later-block-battery.py --root . --rev <measured> \
  --repair-cmd tools/round-90/upx-break-repair.py \
  --pkg /home/vgpnk/.npm/_npx/ad9a3fdbcad992c6/node_modules/rea-agents \
  --work <scratch> --expect "P1 6 of 6; P2 4 of 4; P3 4 of 4" --json-out <receipt>
```

| arm | before (unchanged round-89 repair) | after (round-90 repair) |
|---|---|---|
| P1 interior later block, jq/xxd/docker-init × `stored − 7`/`stored + 7` | `0 of 6`, controls true (`.ufo/waves/round-90/pre/c1-candidate-at-declaration.json` `controls.no_work`) | `6 of 6` |
| P2 block-0 wrong (round-89 class, 4 carriers) | `4 of 4` (composed) | `4 of 4` |
| P3 block-0 zeroed (round-88 class, 4 carriers) | `4 of 4` (composed) | `4 of 4` |
| `carrier_blind` re-scored P1 cells | — | `6 of 6` blinded, probe proves the pinned paths hold decoys |
| `cheat_repack` (reproduces the intact packed bytes) | killed | live unblinded, killed blinded |
| label / exit / `met_target` | `P1 0 of 6` context only | `P1 6 of 6; P2 4 of 4; P3 4 of 4`, exit 0, `met_target true` |

Measured at `499d2183a67058d5648b51a2abf50c10012b1292` (the superseded instruments, REA arm required):
`.ufo/waves/round-90/l1/scores/c1-at-499d2183.json`. Composition arms P2/P3 are the round-89 and
round-88 classes, so the claim does not consume its predecessors.

**Disclosed gap in the blind arm (the counter's, not the claim's).** The wave's mutation-tester ran 16
battery runs (8 single control mutants, 2 double mutants, 5 cheat baselines, 1 genuine reference): 7 of
the 8 control mutants are killed, and the survivor is exactly the `carrier_blind` requirement — a
*source-free provenance cheat* that ships its own copies of the four packed images rather than reading
the pinned paths returns `met_target true` on the pristine counter, because the blinding binds only the
pinned paths and the run root (QUALITY 174). The claim is therefore a capability claim, never a
mechanism claim (QUALITY 152); the repair's own derivation is separately re-derived by an independent
seat (`.ufo/waves/round-90/w1/ExecDeriveIndep/`). Evidence:
`.ufo/waves/round-90/w1/MutCounter/MutCounter.md` and its 16 `receipts/run-*.json`.

**Disclosed flake (both runs, not only the passing one).** A wave seat's independent battery run at
`18b21f09` returned `P1 6 of 6; P2 3 of 4; P3 4 of 4`, exit 1: on docker-init's P2 cell REA 6.5.0
reported 1267 procedures where the original reports 1268 (`.ufo/waves/round-90/w1/ScribeEntry/ScribeEntry.md`
§"What I found" 1 and its receipts; six other runs on identical bytes reported 1268). The L1's landing
run reports `P2 4 of 4` with `rea: true`. The claim stands on the landing receipt **and** the flake is
recorded as an instrument limit in the knowledge entry and in QUALITY's scope, never suppressed.

**R90-C2 — depth (craft rule block 30).**

```
python3 -I -B tools/round-89/depth-blocks-v2.py --root . --rev 8346eaccce7cce23a84f08dee96f9bbeaa03c8ff \
  --expect-blocks 30 --json-out .ufo/waves/round-90/l1/scores/c2-at-8346eacc.json
```

Before: `blocks 29, resolved 29, expect 30, unresolved []`, `met_target false`, exit 1 at `fc52cc9dc`
(`.ufo/waves/round-90/pre/c2-depth-at-base.json`). After: `blocks 30, resolved 30, expect 30,
unresolved []`, `met_target true`, exit 0 at `8346eacc`. The independent reviewer reproduced the base
red at both `fc52cc9dc` and `54c277868` (SKILL.md byte-identical between them) and the green at the
landed block, and the scribe's base-presence gate refuses three worlds the counter alone passes
(a `corpus/lessons/round-89.md` citation absent at base, a `tools/round-90/` citation, and `QUALITY 999`).

## Sources & frontier

`corpus/SOURCES.md`: 217 → 221 rows, census `scripts/sources-census.sh validate --root
/home/vgpnk/Projects/shokunin kaidoku` **exit 0 before** (receipt
`.ufo/waves/round-90/pre/sources-census-before.txt`, produced on a whole-tree extraction of the
declaration commit) **and exit 0 after** (`.ufo/waves/round-90/l1/scores/sources-census-after.txt`).
Tiers A 198 → 201, B 11 → 11, C 8 → 9; statuses mined 194 → 197, rejected 23 → 24 (the before side is the measured after side minus this round's four additions).

- Rows added: **S313** (UPX 5.2.0 `src/p_unix.cpp`, the `PackUnix::unpackExtent` block loop — tier A,
  admitted), **S314** (`src/p_lx_elf.h`, `o_binfo` — tier A, admitted), **S315** (`NEWS` — tier C,
  rejected: user-visible change prose says nothing about the block format; flip: a release entry that
  changes the block format or its bounds), **S316** (`src/p_unix.cpp` **pack side**,
  `PackUnix::packExtent` — tier A, admitted; a third scope on that URL, with no ELF class overriding it).
- Anchor drift recorded, not edited in place: S311's cited lines 7067/7098 measure 7069/7102 on the same
  bytes (the scout re-opened them); the correction is an old→new note in the lesson and a supersedes row
  is routed to round 91 (CORPUS rule 2).
- Rows touched old→new: `src/p_unix.cpp` stays **rejected** for `PackUnix::unpack` (rounds 87/89; flip
  condition unmet) while a *different scope* on the same URL is admitted as S313; both states are
  logged in the lesson's `## Gate`.
- Frontier advanced: the round-89 line "later-block `sz_cpr` values" is now **Core** for the three
  carriers whose chain accounts the full `u_len` (`PROVINCE.md` `## Round-90 additions to Core`,
  `corpus/README.md` round-90 frontier note). Still Frontier: the last block before a chain stop, a
  suffix that self-resumes, the shared object's `u_len` gap, `p_filesize`/`p_blocksize`, 32-bit
  carriers, `--lzma` output and other packers.
- Assimilation: none — `merge/kaidoku/` was not consumed this round (two-claim budget) and this lane
  holds no `considerthese/` directory (the connector seat re-confirmed `Path not found`).

## Trend verdicts

- **expansion — improved.** A new Frontier class became Core on four pinned carriers with a frozen
  counter, a new knowledge entry and a coverage-map row; the registry gained two admitted sources. The
  surface moved (interior block boundaries), not just a number.
- **quality — improved.** The instrument supersession closed four wave defects before the landing run
  (REA arm required, revision pinned, isolation wording, filter docstring), the depth table landed with
  a base-presence gate, and the entry carries its measured limits. Named limits: the last-block
  fall-through (QUALITY 176), the REA count flake, the blind arm's `boxes` tree (QUALITY 174), and the
  depth predicate not entailing a table (QUALITY 175). 15 of 17 declared-case mutants survive because
  the selftests lack the harness-level cases (`.ufo/waves/round-90/w1/ExecMutation/ExecMutation.md`),
  routed to round 91.
- **discernment — improved.** The wave's attack seats found real defects (CriticClaims 4, ExecBlind 1,
  ScribeEntry 1, ExecMutation 17-mutant table, ReviewerC2 3 negative probes), three of them were closed
  before the landing measurement, and the round-89 spot-check's seven routed defects each carry a
  disposition. The non-author closure remains the authority on admission.

## SHONEN

- [~] **SKILL.md contains real decision tables, error patterns, checklists, cited sources** — block 30
  (`SKILL.md:739-751`) is a ten-row routing table whose every criterion is a `corpus/QUALITY.md` row
  present at the base revision, on top of blocks 28-29; the block's `corpus/knowledge/…` citations
  resolve at the measured revision (C2 receipt). Resolvable pointer, no named non-author verifier yet.
- [~] **At least one end-to-end domain task executed and logged in LOG.md** — the four-carrier interior
  block repair scored `P1 6 of 6; P2 4 of 4; P3 4 of 4` with `upx -t`, `upx -d` to the carrier pin and
  REA counts as arms (`.ufo/waves/round-90/l1/scores/c1-at-499d2183.json`), recorded in the round-90
  `LOG.md` entry. Resolvable pointer.
- [~] **Instructions executable by an agent without oral context** — the entry's counting command and
  its limits reproduce from `corpus/knowledge/2026-11-04-r90-interior-block-szcpr.md`; the wave's
  ExecMatrix re-derived every carrier's block layout from the pins alone
  (`.ufo/waves/round-90/w1/ExecMatrix/ExecMatrix.md`). Resolvable pointer.
- [~] **No cross-domain bleed (PROVINCE.md still accurate)** — the new Core row is packed-ELF ground
  only (`PROVINCE.md` `## Round-90 additions to Core`) and the connector's exact-scope sweep found 0
  matches on that ground in any sibling lane
  (`.ufo/waves/round-90/w1/ConnectorOverlap/receipts/exact-sibling.json`). Resolvable pointer.

## Stale-lane

Respawn-per-round driver; no other mission of this lane is open. Round 90 is closed by this report; no
round-90+1 work was started.

## Tool installs

None. No tool was installed or upgraded by the L1 or by any seat (every instrument used was present:
`upx 5.2.0` at the pinned sha256, `bwrap` 0.13.1, `node`, REA 6.5.0 from the npx cache). `pacman`
transactions stayed paused host-wide and none was attempted.

## Open L0 questions

None raised this round.
