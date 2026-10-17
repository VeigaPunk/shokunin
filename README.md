# shokunin — 職人

A skill that mints expert agents for any domain, and the roster of every
specialist it has minted.

A minted shokunin learns a domain the way an artisan learns a craft. Round
after round it builds a corpus of sources, and the skill that sits on that
corpus gets sharper: more coverage, tighter taste, checks a stranger can
re-run.

This repository is the **fleet root**: the protocol, the roster, the round
history, and the coordination state. Each specialist lives in its own
repository. A new mint registers here.

**Wiki:** [fleet overview](https://app.devin.ai/org/veigapunk/wiki/VeigaPunk/shokunin?branch=master)

## Start here

| If you need | Open |
|---|---|
| The contract a round must satisfy | [`PROTOCOL.md`](PROTOCOL.md) |
| What "better" means | [`AXES.md`](AXES.md) — depth, coverage, operability, freshness, calibration, adjacency |
| How a round is judged | [`LEARNING.md`](LEARNING.md) — expansion, quality, discernment |
| What may enter a corpus | [`CORPUS.md`](CORPUS.md) |
| The machine roster and round ledger | [`MANIFEST.json`](MANIFEST.json) |
| The human mirror of that ledger | [`ROADMAP.md`](ROADMAP.md) |
| One specialist's craft | that lane's repository, then its `PROVINCE.md` and `SKILL.md` |

The Kimi Code CLI plugin that carries this protocol is
[kimi-shokunin](https://github.com/VeigaPunk/kimi-shokunin). Protocol files
here are vendored from that upstream.

## How a shokunin learns

Each specialist owns a bounded domain (`PROVINCE.md`) and improves round
over round:

1. **Curation** — gather candidate knowledge from the domain's real
   surfaces: tools, artifacts, shipped systems, primary sources, the
   lane's own verified work.
2. **Quality gating** — admit into `corpus/knowledge/` only what clears
   the lane's own bar (`corpus/QUALITY.md`). Rejections are kept.
   A rejection is evidence of taste.
3. **Understanding** — distill admissions into `SKILL.md`: decision
   tables, error patterns, executable checklists.
4. **Expanding perspective** — work the frontier: adjacent surfaces,
   other tools and schools, counter-examples, failure cases.

## Lifecycle

```
mint → shonen (apprentice) → shokunin (artisan) → jin'i-ryu (self-iterating)
```

- **Shonen** — minted on proven unplaceable demand (two documented
  instances no existing province could absorb) or operator directive.
  Seed: `SKILL.md` + `PROVINCE.md` + `SHONEN.md` + `LOG.md` + `MINT.md`,
  its own repository, and (after probation) a roster row here.
- **Shokunin** — promoted when it performs domain work end-to-end: every
  `SHONEN.md` box checked by a **non-author** reviewer. On promotion
  `SHONEN.md` is deleted.
- **Jin'i-ryu** — promoted when it can iterate on itself.

## A round

One to three claims. Each claim is an axis-move, measured before → after
in `SCORECARD.md` and `LOG.md`.

Every round, one verdict per learning trend — `expansion`, `quality`,
`discernment` — as `improved` / `harmed` / `unchanged` /
`unprovable-but-better`. Audits re-verify prior rounds. The corpus is
expected to catch its own mistakes.

```
bounded candidate → work commit → non-author verifier → adjudicator
verdict → LOG.md + SCORECARD.md + report
```

Any lane may mint a sibling when it finds unplaceable demand. The roster
below is the registry.

## Corpus shape

```
corpus/
  README.md     index: coverage map, known gaps, frontier
  QUALITY.md    the lane's own admission bar
  knowledge/    facts with source, verified-at, recheck
  lessons/      per-round lessons with a Gate section
```

Append-only: errata are appended blocks. Every claim is falsifiable or
marked opinion.

## Roster

`MANIFEST.json` is the machine roster. Its `roster` array, read with this
README, lists the thirteen lanes minted 2026-09-28 through 2026-10-13
(kasegi through kaidoku). Canonical names are `<id>-shokunin`. 2026-09
remotes keep that shape. 2026-10 public remotes use `shokunin-<domain>`.

| Shokunin | Domain | Rank | Repo |
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

### Repositories present, not yet rows in `MANIFEST.json`

These specialist repositories exist and still carry `SHONEN.md` (promotion
deletes that file). They are part of the workshop. They are not entries in
the `roster` array of `MANIFEST.json`.

| Shokunin | Domain | Repo |
|---|---|---|
| mori-shokunin | fleet & host observability (森) | [mori-shokunin](https://github.com/VeigaPunk/mori-shokunin) |
| chousa-shokunin | deep-research method (調査) | [chousa-shokunin](https://github.com/VeigaPunk/chousa-shokunin) |
| mado-shokunin | desktop & compositor craft | [mado-shokunin](https://github.com/VeigaPunk/mado-shokunin) |
| tabi-shokunin | browser & web-interaction craft (旅) | [tabi-shokunin](https://github.com/VeigaPunk/tabi-shokunin) |
| tameshi-shokunin | verification-fixture craft | [tameshi-shokunin](https://github.com/VeigaPunk/tameshi-shokunin) |
| tsukuroi-shokunin | host operability & system repair (繕) | [tsukuroi-shokunin](https://github.com/VeigaPunk/tsukuroi-shokunin) |
| kotodama-shokunin | linguistic-cultural worldbuilding (言霊) | [kotodama-shokunin](https://github.com/VeigaPunk/kotodama-shokunin) |

The previous README already recorded mori and chousa as created and pushed
on 2026-10-16 after their 10-round in-session craft runs. That note stands.
Adding them to `MANIFEST.json` is a roster edit, and this README does not
perform it.

## Files

| File | Role |
|---|---|
| `PROTOCOL.md`, `PROTOCOL-APPENDIX.md`, `MISSION.md` | round contract |
| `AXES.md`, `LEARNING.md`, `CORPUS.md` | expertise, verdicts, corpus rules |
| `MANIFEST.json` | machine roster + round history |
| `ROADMAP.md` | human mirror |
| `SCORECARD.md`, `LOG.md` | fleet-root verdicts and audit trail |
| `shokunin.conf`, `scripts/shokunin-watchdog.sh` | round driver |
| `templates/` | round prompt and agent seeds |
| `.ufo/` | fleet state: waves, reports, prompts |
