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

**Wiki:** [fleet overview](https://app.devin.ai/org/veigapunk/wiki/VeigaPunk/shokunin?branch=master)

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

`PROTOCOL.md` is the contract. In short:

- **Shonen** — minted on proven *unplaceable* demand (two documented
  instances no existing province could absorb) or operator directive.
  Seed: `SKILL.md` + `PROVINCE.md` + `SHONEN.md` + `LOG.md` + `MINT.md`,
  its own repo, and — after probation — a roster row here.
- **Shokunin** — promoted when it performs domain work end-to-end: every
  `SHONEN.md` box checked by a **non-author** reviewer. On promotion
  `SHONEN.md` is deleted. Every lane linked below still carries
  `SHONEN.md`, so every one of them is still an apprentice.
- **Jin'i-ryu** — promoted when it can iterate on itself.

### Six expertise axes (`AXES.md`)

`depth` · `coverage` · `operability` · `freshness` · `calibration` ·
`adjacency` — a round is 1–3 claims, each an axis-move, measured before→after in
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

`MANIFEST.json` → `roster` is the registered list. `ROADMAP.md` is a human
mirror and lags this file. Canonical names are `<id>-shokunin`. 2026-09
remotes keep that shape; 2026-10 remotes use `shokunin-<domain>`.

| Shokunin | Domain | Rank | Repository |
|---|---|---|---|
| kasegi-shokunin | bounty & security research | shonen | [kasegi-shokunin](https://github.com/VeigaPunk/kasegi-shokunin) |
| kengaku-shokunin | LLM/model research & evaluation | shonen | [kengaku-shokunin](https://github.com/VeigaPunk/kengaku-shokunin) |
| kake-shokunin | web properties & publishing | shonen | [kake-shokunin](https://github.com/VeigaPunk/kake-shokunin) |
| kumitate-shokunin | orchestration & tooling | shonen | [kumitate-shokunin](https://github.com/VeigaPunk/kumitate-shokunin) |
| kotoba-shokunin | prompt & skill craft | shonen | [kotoba-shokunin](https://github.com/VeigaPunk/kotoba-shokunin) |
| kagi-shokunin | secrets & vault ops | shonen | [kagi-shokunin](https://github.com/VeigaPunk/kagi-shokunin) |
| kama-shokunin | local model serving & endpoint health | shonen | [kama-shokunin](https://github.com/VeigaPunk/kama-shokunin) |
| kaidoku-shokunin | shipped-artifact reverse engineering (REA) | shonen | [shokunin-reverse-engineering](https://github.com/VeigaPunk/shokunin-reverse-engineering) |
| revenger-shokunin | binary forensics, evidence-ledger verification | shonen | [shokunin-binary-forensics](https://github.com/VeigaPunk/shokunin-binary-forensics) |
| audio-shokunin | game audio production | shonen | [shokunin-game-audio](https://github.com/VeigaPunk/shokunin-game-audio) |
| game-dev-2d-shokunin | 2D game production, executable fixtures | shonen | [shokunin-godot-2d](https://github.com/VeigaPunk/shokunin-godot-2d) |
| game-dev-3d-shokunin | 3D game production, headless fixtures | shonen | [shokunin-3d-engines](https://github.com/VeigaPunk/shokunin-3d-engines) |
| lore-shokunin | fictional-world records & consistency | shonen | [shokunin-world-bible](https://github.com/VeigaPunk/shokunin-world-bible) |

### Minted, roster row withheld

These lanes have `type: mint` entries in `MANIFEST.json`. Each note says
probation is at least three verified rounds and **the roster row is
withheld**. They are real repositories. They are not rows in `roster`.

| Shokunin | Domain (from the mint note) | Repository |
|---|---|---|
| tameshi-shokunin | verification-fixture craft | [tameshi-shokunin](https://github.com/VeigaPunk/tameshi-shokunin) |
| mado-shokunin | desktop & compositor craft (Hyprland/waybar/walker) | [mado-shokunin](https://github.com/VeigaPunk/mado-shokunin) |
| tsukuroi-shokunin | host operability & system repair | [tsukuroi-shokunin](https://github.com/VeigaPunk/tsukuroi-shokunin) |
| tabi-shokunin | browser & web-interaction craft | [tabi-shokunin](https://github.com/VeigaPunk/tabi-shokunin) |
| mori-shokunin | fleet & host observability (森) — detection and report, never remediation | [mori-shokunin](https://github.com/VeigaPunk/mori-shokunin) |
| chousa-shokunin | deep-research method (調査) | [chousa-shokunin](https://github.com/VeigaPunk/chousa-shokunin) |

[kotodama-shokunin](https://github.com/VeigaPunk/kotodama-shokunin) is a
sibling repository for linguistic-cultural worldbuilding (言霊). A search
of this checkout's `MANIFEST.json` finds no `kotodama` row, so it is not
registered here.

The portable Kimi Code CLI adaptation — protocol, mint kit, and a
substrate-neutral driver — is
[kimi-shokunin](https://github.com/VeigaPunk/kimi-shokunin).

## Files

| Path | Role |
|---|---|
| `PROTOCOL.md`, `PROTOCOL-APPENDIX.md`, `MISSION.md`, `AXES.md`, `LEARNING.md`, `CORPUS.md` | The fleet contract, vendored from [kimi-shokunin](https://github.com/VeigaPunk/kimi-shokunin) |
| `MANIFEST.json` | Machine roster plus the append-only round ledger |
| `ROADMAP.md` | Human mirror of the roster; update the manifest first |
| `SCORECARD.md`, `LOG.md` | Fleet-meta axis claims and the audit trail |
| `shokunin.conf`, `scripts/shokunin-watchdog.sh` | Round driver. The script's opening pins `SK` and `UFO` to absolute paths on the operator host, so it is the historical driver for that machine |
| `.ufo/` | Fleet state: `waves/`, `reports/`, `prompts/`, `l0-questions.md` |
| `research/` | Fleet research records, including the deep-research archives chousa verifies |

The root also holds operator scratch (conf snapshots, forge logs, timing
dumps). Those files are not the protocol.
