# shokunin — 職人

**A shokunin is a domain specialist that earns its domain through
demonstrated craft — iterated by swarm rounds until it can iterate itself.**

This repo is the **fleet root and reference**: it holds the canonical
protocol, the roster, the round history, and the coordination state.
Each specialist lives in its own repo, linked below.

## What the skill does

A shokunin owns a bounded domain (its **PROVINCE**) and improves itself
round over round through a disciplined loop:

1. **Curation** — gather candidate knowledge from the domain's real
   surfaces (tools, artifacts, shipped systems, its own work).
2. **Quality gating** — admit into `corpus/knowledge/` only what clears
   the lane's own bar in `corpus/QUALITY.md`. Rejections are kept —
   a rejection is evidence of taste.
3. **Understanding** — distill admissions into `SKILL.md` (decision
   tables, error patterns, checklists) and sharpen the quality bar.
4. **Expanding perspective** — work the province frontier: adjacent
   surfaces, other tools, counter-examples, failure cases.

## How it works

### Lifecycle

```
mint → shonen (apprentice) → shokunin (artisan) → jin'i-ryu (self-iterating)
```

- **Shonen** — minted on proven unplaceable demand or operator directive;
  seeds `SKILL.md` + `PROVINCE.md` + `SHONEN.md` + `LOG.md`.
- **Shokunin** — promoted when it performs domain work end-to-end: every
  `SHONEN.md` box checked by a **non-author** reviewer (never
  self-attestation), then SHONEN.md is deleted.
- **Jin'i-ryu** — promoted when it can iterate on itself.

### The six expertise axes (`AXES.md`)

`depth` · `coverage` · `operability` · `freshness` · `calibration` ·
`adjacency` — each round is one axis-move, measured before→after and
recorded in `SCORECARD.md` + `LOG.md`.

### The three learning trends (`LEARNING.md`)

Every round gets one verdict per trend — `expansion`, `quality`,
`discernment` — using `improved / harmed / unchanged / unprovable-but-better`.
No scalar scores; verdicts cite evidence.

### The corpus contract (`CORPUS.md`)

```
corpus/
  README.md     — index: coverage map, known gaps, frontier
  QUALITY.md    — the lane's own admission bar
  knowledge/    — domain facts with source:, verified-at:, recheck:
  lessons/      — per-round lessons with a ## Gate section
```

Every claim is falsifiable or marked opinion. Corpora are **append-only** —
errata are appended blocks, never rewrites. The refined human-legible layer
per lane lives in the operator's `shokoknowledge` Obsidian vault.

### Round shape

Bounded candidate → work commit → **non-author verifier** → adjudicator
verdict → `LOG.md` + `SCORECARD.md` + report. A lane that finds domain
demand no province owns may **mint a sibling** (see `PROTOCOL.md` §Sibling
mint). Two unproductive dispatched rounds flag dormancy — a review trigger,
never auto-retirement.

## The fleet

Each lane's repo is `shokunin-<domain>`; locally each lives at
`$SHOKUNIN_ROOT/<id>-shokunin/` (gitignored here). `MANIFEST.json` is the
canonical roster; `ROADMAP.md` mirrors it for humans.

### Current lanes

| Specialist | Repo | Domain | Status |
|---|---|---|---|
| kaidoku | [shokunin-reverse-engineering](https://github.com/VeigaPunk/shokunin-reverse-engineering) | Shipped-artifact RE with REA (native ELF/PE, Electron/ASAR, APK, firmware, managed, runtime) | shonen — probation complete, promotion pending |
| revenger | [shokunin-binary-forensics](https://github.com/VeigaPunk/shokunin-binary-forensics) | RE with evidence-ledger discipline — byte-oracle fixtures, forged-claim rejection | shonen, 60+ verified rounds |
| audio | [shokunin-game-audio](https://github.com/VeigaPunk/shokunin-game-audio) | Game SFX + soundtrack, headless-verified (duration/loudness/spectral/loop-seam) | shonen, 61 rounds |
| game-dev-2d | [shokunin-godot-2d](https://github.com/VeigaPunk/shokunin-godot-2d) | 2D game production via executable Godot 4.7.2 headless fixtures | shonen, 60 rounds |
| game-dev-3d | [shokunin-3d-engines](https://github.com/VeigaPunk/shokunin-3d-engines) | 3D production via headless fixtures — Godot, three.js; Unity/Unreal format-level | shonen, 69 rounds |
| lore | [shokunin-world-bible](https://github.com/VeigaPunk/shokunin-world-bible) | Fictional-world records + mechanical consistency checking | shonen, 85 rounds |

### Previous era (2026-09 roster — archived remotes)

kasegi (bounty/security research) · kengaku (LLM/model research) ·
kake (web properties) · kumitate (orchestration tooling) ·
kotoba (prompt/skill craft) · kagi (secrets/vault ops) · kama (minted
post-round-17) — history preserved in this repo's merged ancestry and
each `*-shokunin` archived remote.

## Files

`PROTOCOL.md` `AXES.md` `LEARNING.md` `CORPUS.md` `MISSION.md`
`PROTOCOL-APPENDIX.md` — the canonical protocol (vendored from
[kimi-shokunin](https://github.com/VeigaPunk/kimi-shokunin) —
upstream source of truth).
`MANIFEST.json` — machine roster + full round history (79 rounds, both eras).
`ROADMAP.md` — human roadmap. `shokunin.conf` — fleet driver config.
`scripts/shokunin-watchdog.sh` — the round driver.
`.ufo/` — fleet state: `waves/` (dispatch artifacts), `reports/round-N/`,
`prompts/`, `l0-questions.md` (append-only open questions).
