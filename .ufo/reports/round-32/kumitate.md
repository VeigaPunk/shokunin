# round-32 — kumitate · OMP-era layer re-census

Lane: `kumitate-shokunin`. Steered round 32. Axis-move: `coverage:script-layer` +
`coverage:runtime-layer` (the tied lowest live axis, both 6). Round-work commit: `5d250b468ecb764da2857e3ab8034ae3dc489b63`
(lane identity). Wave: `Shokunin12hP2Kumitate20261014` (32 members). Sole L1: Sol 6.1.

## Work performed

- Pre-registered the round in `SCORECARD.md` `## Planned` BEFORE measuring.
- 8 script-family + 11 runtime-family member enumerations, 2 derivation seats, 8 audits
  and 5 note-verification seats; every enumeration carries its command and an `LC_ALL=C`
  `comm -3` proof. Reports: `.ufo/waves/shokunin12h-20261014-p2-kumitate/members/`.
- Parent integrated: committed the member note work, corrected registry cells, bound the
  stanza and Axes to the measured values, re-ran both gates.

## Landed changes

- `SCORECARD.md` — stanza terms, `## Axes` rows, registry cells, round-32 record, K-block
  boundary clause. `corpus/knowledge/*` — member sections added, phantoms removed.

## Before → after measurements

| Term | Before | After | Command |
|---|---:|---:|---|
| `S_members` | 114 | 91 | `ls scripts/*.mjs` + `find scripts -mindepth 2 -type f` |
| `S_sections` | 74 | 91 | `node scripts/claims-check.mjs --json` (in-family) |
| `R_members` | 98 | 92 | `ls crates/ufo-core-runtime/src/*.rs` + `crates/ufo-cli/src/*.rs` |
| `R_sections` | 69 | 75 | `node scripts/claims-check.mjs --json` (in-family) |
| `coverage:script-layer` | 6 | **10** | `node scripts/proxy-check.mjs` |
| `coverage:runtime-layer` | 6 | **8** | `node scripts/proxy-check.mjs` |

`PROXY: MATCH` exit 0; `--selftest` `VERDICT: PASS`.

## SHONEN

- [~] SKILL craft — unchanged this round (the round moved measurement, not prose).
- [~] End-to-end task — the re-census measurement, logged in `LOG.md`.
- [~] No-oral-context — every enumeration names its command.
- [~] PROVINCE accurate — no scope change; the K-block census/ownership boundary is now stated.

## Carried debt

`claims-check` exit 1 on R11's 13 dead anchors after the file shrink (owner kumitate;
unblock: re-anchor). Six cross-domain defects routed to `ufo-fsd-alpha`. The
`membrane-seal write` argv defect stays filed, never absorbed.
