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

<!-- WORK-ITEMS -->

## Landed changes

<!-- LANDED -->

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
