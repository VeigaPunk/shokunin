# shokunin — 職人

**A skill that mints expert agents for any domain — and the roster of every
specialist it has minted.**

A minted shokunin is an agent that *learns a domain the way an artisan
learns a craft*: through continual rounds it builds a corpus of sources
and references, continuously upgrades its skills within its ever-expanding
domain of expertise — ever increasing in quality, in taste, in
resourcefulness, in capabilities, and in potential.

This repo is the **fleet root**: the canonical protocol, the roster, the
round history, and the coordination state. Every newly minted shokunin is
registered here (roster row → `shokunin-<domain>` repo link). Each
specialist lives in its own repository — linked below.

## How a shokunin learns

Each specialist owns a bounded domain (its `PROVINCE.md`) and improves
round over round:

1. **Curation** — gather candidate knowledge from the domain's real
   surfaces: tools, artifacts, shipped systems, primary sources, the
   lane's own verified work.
2. **Quality gating** — admit into `corpus/knowledge/` only what clears
   the lane's own bar (`corpus/QUALITY.md`). Rejections are kept —
   a rejection is evidence of taste.
3. **Understanding** — distill admissions into `SKILL.md`: decision
   tables, error patterns, executable checklists.
4. **Expanding perspective** — work the frontier: adjacent surfaces,
   other tools and schools, counter-examples, failure cases.

## The mechanics

### Lifecycle

```
mint → shonen (apprentice) → shokunin (artisan) → jin'i-ryu (self-iterating)
```

- **Shonen** — minted on proven *unplaceable* demand (two documented
  instances no existing province could absorb) or operator directive.
  Seed: `SKILL.md` + `PROVINCE.md` + `SHONEN.md` + `LOG.md` + `MINT.md`,
  its own `shokunin-<domain>` repo, and (after probation) a roster row here.
- **Shokunin** — promoted when it performs domain work end-to-end: every
  `SHONEN.md` box checked by a **non-author** reviewer — never
  self-attestation. On promotion `SHONEN.md` is deleted.
- **Jin'i-ryu** — promoted when it can iterate on itself.

### Six expertise axes (`AXES.md`)

`depth` · `coverage` · `operability` · `freshness` · `calibration` ·
`adjacency` — a round is one axis-move, measured before→after in
`SCORECARD.md` + `LOG.md`.

### Three learning trends (`LEARNING.md`)

Every round, one verdict per trend — `expansion`, `quality`, `discernment`
— as `improved / harmed / unchanged / unprovable-but-better`. No scalar
scores; verdicts cite evidence. Audits re-verify prior rounds — the
corpus catches its own mistakes.

### The corpus (`CORPUS.md`)

```
corpus/
  README.md     — index: coverage map, known gaps, frontier
  QUALITY.md    — the lane's own admission bar
  knowledge/    — facts with source:, verified-at:, recheck:
  lessons/      — per-round lessons with a ## Gate section
```

Append-only: errata are appended blocks. Every claim is falsifiable or
marked opinion. Sources and references accumulate — that is the craft
record.

### A round

Bounded candidate → work commit → **non-author verifier** → adjudicator
verdict → `LOG.md` + `SCORECARD.md` + report. Any lane may **mint a
sibling** when it finds unplaceable demand; the roster below is the
registry of every mint.

## Roster

`MANIFEST.json` is canonical; `ROADMAP.md` mirrors it. Local dirs follow
`$SHOKUNIN_ROOT/<id>-shokunin/`; remotes follow `shokunin-<domain>`.

### Active fleet

| Repo | Domain | Status |
|---|---|---|
| [shokunin-reverse-engineering](https://github.com/VeigaPunk/shokunin-reverse-engineering) (kaidoku) | Shipped-artifact RE with REA — ELF/PE, Electron/ASAR, APK, firmware, managed, runtime | shonen — promotion pending |
| [shokunin-binary-forensics](https://github.com/VeigaPunk/shokunin-binary-forensics) (revenger) | RE with evidence-ledger discipline — byte-oracle fixtures, forged-claim rejection | shonen, 60+ rounds |
| [shokunin-game-audio](https://github.com/VeigaPunk/shokunin-game-audio) (audio) | Game SFX + soundtrack, headless-verified | shonen, 61 rounds |
| [shokunin-godot-2d](https://github.com/VeigaPunk/shokunin-godot-2d) (game-dev-2d) | 2D production via executable Godot headless fixtures | shonen, 60 rounds |
| [shokunin-3d-engines](https://github.com/VeigaPunk/shokunin-3d-engines) (game-dev-3d) | 3D production via headless fixtures — Godot, three.js | shonen, 69 rounds |
| [shokunin-world-bible](https://github.com/VeigaPunk/shokunin-world-bible) (lore) | Fictional-world records + mechanical consistency | shonen, 85 rounds |

### Previous era — 2026-09 (archived remotes)

kasegi (bounty/security) · kengaku (LLM/model research) ·
kake (web properties) · kumitate (orchestration tooling) ·
kotoba (prompt/skill craft) · kagi (secrets/vault ops) ·
kama (minted post-r17) — history preserved in this repo's merged ancestry
and each archived `*-shokunin` remote.

## Files

`PROTOCOL.md` `AXES.md` `LEARNING.md` `CORPUS.md` `MISSION.md`
`PROTOCOL-APPENDIX.md` — canonical protocol, vendored from
[kimi-shokunin](https://github.com/VeigaPunk/kimi-shokunin) (upstream).
`MANIFEST.json` — machine roster + round history (79 rounds, both eras).
`ROADMAP.md` — human mirror. `shokunin.conf` + `scripts/` — the round
driver. `.ufo/` — fleet state (`waves/`, `reports/`, `prompts/`,
`l0-questions.md`).
