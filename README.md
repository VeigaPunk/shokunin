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
registered here (a row in `MANIFEST.json`, then its own repository). Each
specialist lives in that repository — linked below.

**Wiki:** [fleet overview](https://app.devin.ai/org/veigapunk/wiki/VeigaPunk/shokunin?branch=master)

## Start here

1. This page, for the shape of the fleet.
2. [`PROTOCOL.md`](PROTOCOL.md) for the round contract, and [`MISSION.md`](MISSION.md) for the binding mission the driver relays.
3. [`MANIFEST.json`](MANIFEST.json) for the roster and the round ledger. [`ROADMAP.md`](ROADMAP.md) is the human mirror; the manifest is canonical.
4. The lane whose province matches the work. Inside that repo, open `PROVINCE.md`, then `SKILL.md` when the lane has one, then `corpus/`.

`shokunin.conf` declares the lanes the driver will dispatch. `scripts/shokunin-watchdog.sh` is the respawn-per-round driver.

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
  its own repository, and (after probation) a roster row here.
- **Shokunin** — promoted when it performs domain work end-to-end: every
  `SHONEN.md` box checked by a **non-author** reviewer — never
  self-attestation. On promotion `SHONEN.md` is deleted.
- **Jin'i-ryu** — promoted when it can iterate on itself.

Every lane in the roster table below is still **shonen**.

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
registry of every mint that has a `MANIFEST.json` row.

## Roster

Taken from `MANIFEST.json` on 2026-10-17: **13** objects in `roster`, **176**
records in `rounds`. Ranks below are the `rank` field on each row.

Canonical names are `<id>-shokunin`. 2026-09 remotes keep that shape;
2026-10 remotes use `shokunin-<domain>`.

| Id | Repository | Domain | Rank |
|---|---|---|---|
| kasegi | [kasegi-shokunin](https://github.com/VeigaPunk/kasegi-shokunin) | bounty & security research | shonen |
| kengaku | [kengaku-shokunin](https://github.com/VeigaPunk/kengaku-shokunin) | LLM/model research & evaluation | shonen |
| kake | [kake-shokunin](https://github.com/VeigaPunk/kake-shokunin) | web properties & publishing | shonen |
| kumitate | [kumitate-shokunin](https://github.com/VeigaPunk/kumitate-shokunin) | orchestration & tooling (OMP, scripts, Rust runtime) | shonen |
| kotoba | [kotoba-shokunin](https://github.com/VeigaPunk/kotoba-shokunin) | prompt & skill craft | shonen |
| kagi | [kagi-shokunin](https://github.com/VeigaPunk/kagi-shokunin) | secrets & vault ops | shonen |
| kama | [kama-shokunin](https://github.com/VeigaPunk/kama-shokunin) | local model serving & endpoint health | shonen |
| audio | [shokunin-game-audio](https://github.com/VeigaPunk/shokunin-game-audio) | game audio production — SFX + soundtrack, headless-verified | shonen |
| game-dev-2d | [shokunin-godot-2d](https://github.com/VeigaPunk/shokunin-godot-2d) | 2D game production via executable headless fixtures (Godot 4.7.2) | shonen |
| game-dev-3d | [shokunin-3d-engines](https://github.com/VeigaPunk/shokunin-3d-engines) | 3D game production via headless fixtures across Godot/three.js/Unity/Unreal | shonen |
| lore | [shokunin-world-bible](https://github.com/VeigaPunk/shokunin-world-bible) | fictional-world records + consistency verification | shonen |
| revenger | [shokunin-binary-forensics](https://github.com/VeigaPunk/shokunin-binary-forensics) | reverse engineering of shipped artifacts, evidence-ledger discipline | shonen |
| kaidoku | [shokunin-reverse-engineering](https://github.com/VeigaPunk/shokunin-reverse-engineering) | reverse engineering of shipped artifacts with REA on this host | shonen |

## Sibling repositories

These repositories describe themselves as shokunin lanes. They are **not**
objects in `MANIFEST.json`'s `roster` array (that array ends at `kaidoku`).
Each one's `PROVINCE.md` is its boundary. A roster row is a manifest edit.

| Repository | Domain, from that repo's `PROVINCE.md` |
|---|---|
| [chousa-shokunin](https://github.com/VeigaPunk/chousa-shokunin) | deep-research method (調査) |
| [mori-shokunin](https://github.com/VeigaPunk/mori-shokunin) | fleet & host observability (森) |
| [mado-shokunin](https://github.com/VeigaPunk/mado-shokunin) | desktop & compositor craft |
| [tabi-shokunin](https://github.com/VeigaPunk/tabi-shokunin) | browser & web-interaction craft (旅) |
| [tameshi-shokunin](https://github.com/VeigaPunk/tameshi-shokunin) | verification-fixture craft |
| [tsukuroi-shokunin](https://github.com/VeigaPunk/tsukuroi-shokunin) | host operability & system repair (繕) |
| [kotodama-shokunin](https://github.com/VeigaPunk/kotodama-shokunin) | linguistic-cultural worldbuilding (言霊) |

The portable Kimi Code CLI adaptation — protocol, mint kit, and a
substrate-neutral watchdog — is [kimi-shokunin](https://github.com/VeigaPunk/kimi-shokunin).

## Files

| Path | What it is |
|---|---|
| `PROTOCOL.md`, `PROTOCOL-APPENDIX.md`, `AXES.md`, `LEARNING.md`, `CORPUS.md`, `MISSION.md` | The fleet contract. Vendored from [kimi-shokunin](https://github.com/VeigaPunk/kimi-shokunin). |
| `MANIFEST.json` | Machine roster and round ledger. |
| `ROADMAP.md` | Human mirror of the roster and the phase gates. |
| `SCORECARD.md`, `LOG.md` | Axis verdicts and the append-only audit trail for the fleet-root lanes. |
| `shokunin.conf`, `scripts/` | Lane table and the round driver. |
| `templates/` | Round-prompt and agent role templates. |
| `.ufo/` | Fleet state: `waves/`, `reports/`, `prompts/`, `l0-questions.md`. |
