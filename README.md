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

## Start here

| If you want to… | Open |
|---|---|
| Understand the contract | [`PROTOCOL.md`](PROTOCOL.md) · [`AXES.md`](AXES.md) · [`LEARNING.md`](LEARNING.md) |
| See who exists | [`MANIFEST.json`](MANIFEST.json) (canonical) · roster table below |
| Run a fleet loop | [`shokunin.conf`](shokunin.conf) · [`scripts/shokunin-watchdog.sh`](scripts/shokunin-watchdog.sh) |
| Mint on Kimi Code CLI | the portable plugin [`kimi-shokunin`](https://github.com/VeigaPunk/kimi-shokunin) |
| Read one specialist | any repo in the roster — start at its `PROVINCE.md` and `SKILL.md` |

A round is admitted only when at least one expertise axis **improved** and
none were **harmed**. Evidence is the currency. Lane identity rides in
every commit.

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

### Six expertise axes ([`AXES.md`](AXES.md))

`depth` · `coverage` · `operability` · `freshness` · `calibration` ·
`adjacency` — a round is 1–3 claims, each an axis-move, measured before→after in
`SCORECARD.md` + `LOG.md`.

### Three learning trends ([`LEARNING.md`](LEARNING.md))

Every round, one verdict per trend — `expansion`, `quality`, `discernment`
— as `improved / harmed / unchanged / unprovable-but-better`. No scalar
scores; verdicts cite evidence. Audits re-verify prior rounds — the
corpus catches its own mistakes.

### The corpus ([`CORPUS.md`](CORPUS.md))

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

`MANIFEST.json` is canonical; `ROADMAP.md` mirrors it. Every minted
shokunin registers a row here and gets its own `shokunin-*` expert repo.
Canonical names are `<id>-shokunin`; 2026-09 remotes keep that shape
(private), 2026-10 remotes use `shokunin-<domain>` (public).

| Shokunin | Domain | Rank | Repo |
|---|---|---|---|
| [kasegi-shokunin](https://github.com/VeigaPunk/kasegi-shokunin) | bounty & security research | shonen | `kasegi-shokunin` |
| [kengaku-shokunin](https://github.com/VeigaPunk/kengaku-shokunin) | LLM/model research & evaluation | shonen | `kengaku-shokunin` |
| [kake-shokunin](https://github.com/VeigaPunk/kake-shokunin) | web properties & publishing | shonen | `kake-shokunin` |
| [kumitate-shokunin](https://github.com/VeigaPunk/kumitate-shokunin) | orchestration & tooling | shonen | `kumitate-shokunin` |
| [kotoba-shokunin](https://github.com/VeigaPunk/kotoba-shokunin) | prompt & skill craft | shonen | `kotoba-shokunin` |
| [kagi-shokunin](https://github.com/VeigaPunk/kagi-shokunin) | secrets & vault ops | shonen | `kagi-shokunin` |
| [kama-shokunin](https://github.com/VeigaPunk/kama-shokunin) | local model serving & endpoint health | shonen | `kama-shokunin` |
| [kaidoku-shokunin](https://github.com/VeigaPunk/shokunin-reverse-engineering) | shipped-artifact reverse engineering (REA) | shonen | `shokunin-reverse-engineering` |
| [revenger-shokunin](https://github.com/VeigaPunk/shokunin-binary-forensics) | binary forensics, evidence-ledger verification | shonen | `shokunin-binary-forensics` |
| [audio-shokunin](https://github.com/VeigaPunk/shokunin-game-audio) | game audio production | shonen | `shokunin-game-audio` |
| [game-dev-2d-shokunin](https://github.com/VeigaPunk/shokunin-godot-2d) | 2D game production, executable fixtures | shonen | `shokunin-godot-2d` |
| [game-dev-3d-shokunin](https://github.com/VeigaPunk/shokunin-3d-engines) | 3D game production, headless fixtures | shonen | `shokunin-3d-engines` |
| [lore-shokunin](https://github.com/VeigaPunk/shokunin-world-bible) | fictional-world records & consistency | shonen | `shokunin-world-bible` |

### Later mints (driver + workspace)

These lanes are declared in [`shokunin.conf`](shokunin.conf) and/or exist
as sibling repositories. `MANIFEST.json` remains the protocol roster of
record; a missing manifest row is not a denial that the repo exists.

| Shokunin | Domain | Repo |
|---|---|---|
| [mori-shokunin](https://github.com/VeigaPunk/mori-shokunin) | fleet & host observability (森) | `mori-shokunin` |
| [chousa-shokunin](https://github.com/VeigaPunk/chousa-shokunin) | deep-research method (調査) | `chousa-shokunin` |
| [mado-shokunin](https://github.com/VeigaPunk/mado-shokunin) | desktop & compositor craft (窓) | `mado-shokunin` |
| [tabi-shokunin](https://github.com/VeigaPunk/tabi-shokunin) | browser & web-interaction craft (旅) | `tabi-shokunin` |
| [tameshi-shokunin](https://github.com/VeigaPunk/tameshi-shokunin) | verification-fixture craft (試し) | `tameshi-shokunin` |
| [tsukuroi-shokunin](https://github.com/VeigaPunk/tsukuroi-shokunin) | host operability & system repair (繕) | `tsukuroi-shokunin` |
| [kotodama-shokunin](https://github.com/VeigaPunk/kotodama-shokunin) | linguistic-cultural worldbuilding (言霊) | `kotodama-shokunin` |

(2026-10-16: mori + chousa repos created and pushed after their 10-round
in-session craft runs — rounds 2–11 admitted on both lanes, ledgers in
`MANIFEST.json`.)

The portable Kimi Code CLI adaptation of this protocol lives at
[`kimi-shokunin`](https://github.com/VeigaPunk/kimi-shokunin) — not a
domain lane; it is the mint kit, round prompt, and watchdog driver.

## Files

| Path | Role |
|---|---|
| `PROTOCOL.md` `PROTOCOL-APPENDIX.md` | the contract, and why each rule exists |
| `AXES.md` `LEARNING.md` `CORPUS.md` `MISSION.md` | axes, learning path, corpus rules, fleet SSOT |
| `MANIFEST.json` | machine roster + round history |
| `ROADMAP.md` | human mirror of the roster and phase gates |
| `SCORECARD.md` `LOG.md` | protocol/aggregator axis verdicts and audit trail |
| `shokunin.conf` `scripts/` | the round driver |
| `.ufo/` | fleet state (`waves/`, `reports/`, `prompts/`, `l0-questions.md`) |
| `templates/` | round prompt and related fleet templates |

Protocol files are vendored from
[kimi-shokunin](https://github.com/VeigaPunk/kimi-shokunin) (upstream).
