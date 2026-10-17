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

`MANIFEST.json` is canonical for the rows it carries; `ROADMAP.md` mirrors
it. Every minted shokunin registers a row here and gets its own expert
repo. Canonical names are `<id>-shokunin`; 2026-09 remotes keep that shape
(private), 2026-10 remotes use `shokunin-<domain>` (public).

Lanes minted after the last `MANIFEST.json` roster close are listed from
their own `MINT.md` / `PROVINCE.md` until the integrator absorbs them.

| Shokunin | Domain | Rank | Minted |
|---|---|---|---|
| [kasegi-shokunin](https://github.com/VeigaPunk/kasegi-shokunin) | bounty & security research | shonen | 2026-09-28 |
| [kengaku-shokunin](https://github.com/VeigaPunk/kengaku-shokunin) | LLM/model research & evaluation | shonen | 2026-09-28 |
| [kake-shokunin](https://github.com/VeigaPunk/kake-shokunin) | web properties & publishing | shonen | 2026-09-28 |
| [kumitate-shokunin](https://github.com/VeigaPunk/kumitate-shokunin) | orchestration & tooling | shonen | 2026-09-28 |
| [kotoba-shokunin](https://github.com/VeigaPunk/kotoba-shokunin) | prompt & skill craft | shonen | 2026-09-28 |
| [kagi-shokunin](https://github.com/VeigaPunk/kagi-shokunin) | secrets & vault ops | shonen | 2026-09-28 |
| [kama-shokunin](https://github.com/VeigaPunk/kama-shokunin) | local model serving & endpoint health | shonen | 2026-09-29 |
| [kaidoku-shokunin](https://github.com/VeigaPunk/shokunin-reverse-engineering) | shipped-artifact reverse engineering (REA) | shonen | 2026-10-13 |
| [revenger-shokunin](https://github.com/VeigaPunk/shokunin-binary-forensics) | binary forensics, evidence-ledger verification | shonen | 2026-10-11 |
| [audio-shokunin](https://github.com/VeigaPunk/shokunin-game-audio) | game audio production | shonen | 2026-10-11 |
| [game-dev-2d-shokunin](https://github.com/VeigaPunk/shokunin-godot-2d) | 2D game production, executable fixtures | shonen | 2026-10-11 |
| [game-dev-3d-shokunin](https://github.com/VeigaPunk/shokunin-3d-engines) | 3D game production, headless fixtures | shonen | 2026-10-11 |
| [lore-shokunin](https://github.com/VeigaPunk/shokunin-world-bible) | fictional-world records & consistency | shonen | 2026-10-11 |
| [mori-shokunin](https://github.com/VeigaPunk/mori-shokunin) | fleet & host observability (森) | shonen | 2026-10-14 |
| [chousa-shokunin](https://github.com/VeigaPunk/chousa-shokunin) | deep-research method (調査) | shonen | 2026-10-14 |
| [mado-shokunin](https://github.com/VeigaPunk/mado-shokunin) | desktop & compositor craft | shonen | 2026-10-14 |
| [tabi-shokunin](https://github.com/VeigaPunk/tabi-shokunin) | browser & web-interaction craft (旅) | shonen | 2026-10-14 |
| [tameshi-shokunin](https://github.com/VeigaPunk/tameshi-shokunin) | verification-fixture craft | shonen | 2026-10-14 |
| [tsukuroi-shokunin](https://github.com/VeigaPunk/tsukuroi-shokunin) | host operability & system repair (繕) | shonen | 2026-10-14 |
| [kotodama-shokunin](https://github.com/VeigaPunk/kotodama-shokunin) | linguistic-cultural worldbuilding (言霊) | shonen | 2026-10-17 |

Portable substrate (not a domain lane):
[kimi-shokunin](https://github.com/VeigaPunk/kimi-shokunin) — the Kimi Code CLI
plugin that vendors this protocol, the mint kit, and the round driver.

## Start here

| If you want to… | Open |
|---|---|
| Run or judge a craft round | `PROTOCOL.md` → `AXES.md` → `LEARNING.md` |
| Understand why a rule exists | `PROTOCOL-APPENDIX.md` |
| See the fleet shape and push scope | `MISSION.md` |
| Check who is minted and what ran | `MANIFEST.json` (machine) · `ROADMAP.md` (human) |
| Drive rounds across lanes | `shokunin.conf` + `scripts/` |
| Inspect live coordination | `.ufo/` (`waves/`, `reports/`, `prompts/`) |

## Files

`PROTOCOL.md` `AXES.md` `LEARNING.md` `CORPUS.md` `MISSION.md`
`PROTOCOL-APPENDIX.md` — canonical protocol, vendored from
[kimi-shokunin](https://github.com/VeigaPunk/kimi-shokunin) (upstream).
`MANIFEST.json` — machine roster + round history (79 rounds, both eras).
`ROADMAP.md` — human mirror. `shokunin.conf` + `scripts/` — the round
driver. `.ufo/` — fleet state (`waves/`, `reports/`, `prompts/`,
`l0-questions.md`).
