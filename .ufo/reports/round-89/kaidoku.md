# kaidoku — round 89

Lane `/home/vgpnk/Projects/shokunin/kaidoku-shokunin`; attempt 1; base revision
`0ec2bb4016655f605657d6e0e700ec2e6893ac27`. Round shape: one v1 wave `r89-w1` of 14 seats
(executor 4, scribe 3, scout 1, reviewer 2, critic 1, mutation-tester 1, sentinel 1, connector 1;
attack roles reviewer/critic/mutation-tester = 4 of 14 = 28.6 %, ≥ 25 %; one connector; the L1 held
the planner seat, which the wave validator rejects as a frozen-topology role).

## Work performed

**Declared claims (2, distinct axes, causally separable).**

- **R89-C1 — coverage (capability acquisition, Frontier → Core):** the wrong-value first-block
  `b_info.sz_cpr` class enters Core. A block-0 `sz_cpr` that is in range but wrong passes every bound
  the packer applies to the field and fails only at the payload stage; the round-88 repair leaves it
  alone. Target: `recovered 4 of 4` under `tools/round-89/upx-field-battery.py` with all four
  controls and the round-88 class regression arm.
- **R89-C2 — depth:** craft rule block 29 (the field-value-class decision table) lands, and the depth
  atom becomes target-aware (`--expect-blocks 29`; QUALITY 157). Target: `blocks 29, resolved 29,
  unresolved []`, with the base arm and a citation-only stub red.

- **Protocol load and claim choice.** Read MISSION/AXES/PROTOCOL, the lane's SKILL/PROVINCE/SCORECARD,
  `corpus/QUALITY.md`, `corpus/README.md` and the round-88 non-author spot-check; declared two claims on
  the tied-lowest owned axes (coverage, depth; all four sit at 10.0 on their finite proxies) from the
  spot-check's routed defects D1-D4 and the round-88 record's own limit "a non-zero but wrong `sz_cpr`
  is left alone".
- **Pre-freeze controls, all committed before data.** The frozen counter against the unchanged round-88
  repair: `recovered 0 of 4`, all four controls true (`.ufo/waves/round-89/pre/c1-base-r88-repair.json`);
  `identity` and `naive-global`: 0 of 4 each; the depth counter at base: `blocks 28, expect 29,
  met_target false`, exit 1 (`pre/c2-depth-at-base.json`); a citation-only stub world: `blocks 29,
  resolved 28`, exit 1 (`pre/c2-control-stub-world.json`); the red freeze-gate control (a container
  naming an absent counter) FLAGGED while the cheap `instruments-only` rule accepts it
  (`pre/freeze-precheck-at-declaration.json`, gate CLEAN, `met true`).
- **A pre-freeze miss caught by the round's own arm.** The first candidate scored `recovered 4 of 4`
  with every control true but the round-88 class regression arm unmet — it derived the field without
  composing the round-87 anchor path, so a magic-tampered carrier was returned unchanged
  (`pre/c1-candidate-first-run.log`). Fixed by composition + a selftest case; the regression arm is now
  part of the frozen predicate (M89-1, QUALITY 161).
- **Wave `r89-w1`, fourteen seats, one v1 wave** (see the shape note below). Twelve of the fourteen
  delivered a report; two (`CriticClaims`, `MutationR89`) wrote nothing and are reported dead. The
  delivered seats produced the independent derivation (16 of 16 cells equal), the 48-cell field matrix,
  a 28-mutant table, the no-harm regression, the source adjudication, two attack reports, the hostile
  input/cost/integrity review, the sibling scan and the three drafts.
- **Two in-round instrument revisions, both before the measured run**, each with an
  `instrument_supersessions` entry and re-taken receipts: (1) typed refusals and the inherited input
  guards — the declared bytes let the round-87 `Refused` escape as a traceback (rc 1), hung on a FIFO
  and raised `MemoryError` on `/dev/zero`, while the counter's `N1-refuse-plain` asserts only
  `rc != 0`; (2) output-path hardening — `..`/absolute `--out`, a followed `<out>.tmp` symlink and
  untyped write errors. The claim's predicate, counter, label, kill rule and target never changed.
- **Frontier step.** Census before exit 0 (215 rows) and after exit 0 (217 rows); S311 and S312 opened,
  admitted at tier A with located quotes, S312's scope corrected in-round to the NE32 `p_unix.h` copy
  the carriers use (old→new in the lesson); `src/headers.h` re-checked (404) and `src/p_unix.cpp`
  re-opened (rejection kept). Seven mistakes mined; QUALITY criteria Rows 161-171 written from them.
  `Assimilation: none` (no `merge/kaidoku/` theme consumed in a two-claim round; the lane has no
  `considerthese/` directory).


## Landed changes

| change | LOG entry | commit |
|---|---|---|
| plan, three instruments and the pre-freeze controls for both claims | `LOG.md` `## 2026-11-04 — round 89` | `9da6c980d7853c1bc0850201e90c8ed9b67587e2` |
| frozen claim container (`claims.json`) | same | `4be89be3e928fa172a5291ca2aa4a3b2dde1ac79`, pins fixed at `4ab027b2799cb5045fd13d0296f2f6c4afb4b145` |
| red freeze-gate control + the gate's CLEAN receipt | same | `18b6a2a4fabc097ec84f81987c0394ac1399a5c3`, `09f44212169bcac469fc84144fc169aeb1d101d9` |
| craft rule block 29 and its 2-carrier cell receipt | same | `8bbb40cc09fadd211b1aa473605553c9caeef511` |
| knowledge entry, S311/S312, `PROVINCE.md` Core row, `corpus/README.md` coverage/index/frontier rows, QUALITY Rows 161-165, instrument-registry rows, the two class-regression receipts | same | `5a46542a5f411e427afee374ab2f494691f070ff` |
| round-88 plan corrections routed by the spot-check (D2 rule drift, D6 attack-share arithmetic) | same | `5068ba6417f3cfc6693ca5e4dbe106c08e305174` |
| entry carries the four-carrier matrix classes, the carrier-dependent gate and the exit-code remit; QUALITY 166-167 | same | `fd9f840bdc1ec16dd1a1d36ff52500b8ede03cdc` |
| repair revision 1 (typed refusals, input guards) + supersession + re-taken receipts; QUALITY 168 | same | `7edab6ae5072778511ab76904e5758548518e251`, receipt re-pin `fc52cc9dc4a7ae294bdea5661e703e978e434f17` |
| S312 scope corrected to the NE32 copy (old→new logged); QUALITY 169-171 | same | `81cd0d73ba11bd3e197445e4fd8f7b1a53a9ad21` |
| `corpus/README.md` rows in the tables' declared shapes | same | `1c7c364769f6af490dc5acd8ff6bbfee5eb54cf2` |
| repair revision 2 (output paths, atomic writes, typed write errors) + supersession + final receipts | same | `bc0e0c20ce73d09bc4bd2622ced138c3462329a9` |
<!-- FINAL-LANDED -->


## Before → after measurements

<!-- MEASUREMENTS -->

## Sources & frontier

<!-- SOURCES -->

## Trend verdicts

<!-- TRENDS -->

## SHONEN

<!-- SHONEN -->

## Notes

<!-- NOTES -->
