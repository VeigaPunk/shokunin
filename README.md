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

| If you want… | Open |
|---|---|
| The contract every lane obeys | [`PROTOCOL.md`](PROTOCOL.md) · [`MISSION.md`](MISSION.md) |
| How a round is judged | [`AXES.md`](AXES.md) · [`LEARNING.md`](LEARNING.md) |
| How knowledge is admitted | [`CORPUS.md`](CORPUS.md) |
| Who exists and what they own | Roster below · [`MANIFEST.json`](MANIFEST.json) · [`ROADMAP.md`](ROADMAP.md) |
| How the fleet is driven | `shokunin.conf` · [`scripts/`](scripts/) · [`.ufo/`](.ufo/) |
| A portable Kimi Code CLI install | [kimi-shokunin](https://github.com/VeigaPunk/kimi-shokunin) |

One axis-move per round. Verdicts, not scores. Evidence, or it did not happen.
Lane identity (`<id>-shokunin <<id>@shokunin.local>`) rides in every commit.

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

Out of province → report to the owning lane, never absorb.

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

A round is admitted only if at least one axis improved and none were
harmed.

## Roster

`MANIFEST.json` is canonical; `ROADMAP.md` mirrors it. Every minted
shokunin registers a row here and gets its own `shokunin-*` expert repo.
Canonical names are `<id>-shokunin`; 2026-09 remotes keep that shape
(private), 2026-10 remotes use `shokunin-<domain>` (public).

| Shokunin | Domain | Rank | Remote |
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
| [mori-shokunin](https://github.com/VeigaPunk/mori-shokunin) | fleet & host observability (森) | shonen | `mori-shokunin` |
| [chousa-shokunin](https://github.com/VeigaPunk/chousa-shokunin) | deep-research method (調査) | shonen | `chousa-shokunin` |
| [kotodama-shokunin](https://github.com/VeigaPunk/kotodama-shokunin) | linguistic-cultural worldbuilding (言霊) | shonen | `kotodama-shokunin` |
| [mado-shokunin](https://github.com/VeigaPunk/mado-shokunin) | desktop & compositor craft | shonen | `mado-shokunin` |
| [tabi-shokunin](https://github.com/VeigaPunk/tabi-shokunin) | browser & web-interaction craft (旅) | shonen | `tabi-shokunin` |
| [tameshi-shokunin](https://github.com/VeigaPunk/tameshi-shokunin) | verification-fixture craft | shonen | `tameshi-shokunin` |
| [tsukuroi-shokunin](https://github.com/VeigaPunk/tsukuroi-shokunin) | host operability & system repair (繕) | shonen | `tsukuroi-shokunin` |

The first thirteen rows match `MANIFEST.json` `roster`. Mori, chousa,
kotodama, mado, tabi, tameshi, and tsukuroi are later working lanes with
their own remotes; they appear here so a visitor can find them. Rank
stays `shonen` until a named non-author verifier checks every
`SHONEN.md` box.

The portable fleet driver — protocol, mint kit, watchdog — ships as
[kimi-shokunin](https://github.com/VeigaPunk/kimi-shokunin).

## Files

`PROTOCOL.md` `AXES.md` `LEARNING.md` `CORPUS.md` `MISSION.md`
`PROTOCOL-APPENDIX.md` — canonical protocol, vendored from
[kimi-shokunin](https://github.com/VeigaPunk/kimi-shokunin) (upstream).
`MANIFEST.json` — machine roster + round history (79 rounds, both eras).
`ROADMAP.md` — human mirror. `shokunin.conf` + `scripts/` — the round
driver. `.ufo/` — fleet state (`waves/`, `reports/`, `prompts/`,
`l0-questions.md`). `LOG.md` + `SCORECARD.md` — the fleet-root audit
trail and axis verdicts.
