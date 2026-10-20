# shokunin — 職人

**A skill that mints expert agents for any domain — and the roster of every
specialist it has minted.**

A minted shokunin is an agent that *learns a domain the way an artisan
learns a craft*: through continual rounds it builds a corpus of sources
and references, continuously upgrades its skills within its ever-expanding
domain of expertise — ever increasing in quality, in taste, in
resourcefulness, in capabilities, and in potential.

This repo is the **fleet root**, a deployment of the
[canonical shokunin protocol](https://github.com/VeigaPunk/kimi-shokunin).
Its vendored protocol copies and local incident evidence are not a second
protocol authority. `MANIFEST.json` is the operator-controlled roster and round
history; `ROADMAP.md` mirrors that roster. A physical local lane repo does not
become a roster member merely by existing or appearing in `shokunin.conf`.
Existing repository links below distinguish rostered entries from other links.

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

Every round also curates `corpus/SOURCES.md`: opened sources, scoped tiers,
rejections with flip conditions, search logs, and ordered study paths. Source
rows are not admitted knowledge; expansion is counted from newly admitted
knowledge on uncovered frontier ground, not from added rows or tools. Lessons
record the round's `## Mistakes` and quality-gate decisions; a non-author
spot-checks at least one admission and one rejection. At the fleet root,
`bash scripts/sources-census.sh census|validate|overdue|shared` gives the
registry census, structural validation, freshness queue, and shared-source
view. The CLI is read-only unless `--out` is supplied; clean structure or a
freshness queue does not prove that a source supports a semantic claim.

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
  SOURCES.md    — opened source registry, scoped tiers, rejections, study paths
  knowledge/    — admitted facts, sourced notes, decision records
  lessons/      — training lessons, including the round's gate and mistakes
```

Corrections are append-only. Every claim is falsifiable or marked opinion.
Sources and references accumulate as the craft record; the sources registry
does not replace the lane's quality gate or chousa's research method.

### A round

Bounded candidate → work commit → **non-author verifier** → adjudicator
verdict → `LOG.md` + `SCORECARD.md` + report. Any lane may propose a sibling
when it finds unplaceable demand; only the operator-controlled roster in
`MANIFEST.json` establishes registered membership.

## Roster records and existing repository links

`MANIFEST.json` is the canonical **operator-controlled roster**; `ROADMAP.md`
is its human mirror. It currently records 13 entries, while the local fleet
contains 21 physical `*-shokunin` directories; the report's inventory command
and result are recorded in `.ufo/reports/round-12/aggregator.md`. These are
different populations: an unlisted local repo is not registered. Canonical
repo names are `<id>-shokunin`; remotes use both historical naming patterns.

| Shokunin | Domain | Manifest status |
|---|---|---|
| [kasegi-shokunin](https://github.com/VeigaPunk/kasegi-shokunin) | bounty & security research | rostered — shonen |
| [kengaku-shokunin](https://github.com/VeigaPunk/kengaku-shokunin) | LLM/model research & evaluation | rostered — shonen |
| [kake-shokunin](https://github.com/VeigaPunk/kake-shokunin) | web properties & publishing | rostered — shonen |
| [kumitate-shokunin](https://github.com/VeigaPunk/kumitate-shokunin) | orchestration & tooling | rostered — shonen |
| [kotoba-shokunin](https://github.com/VeigaPunk/kotoba-shokunin) | prompt & skill craft | rostered — shonen |
| [kagi-shokunin](https://github.com/VeigaPunk/kagi-shokunin) | secrets & vault ops | rostered — shonen |
| [kama-shokunin](https://github.com/VeigaPunk/kama-shokunin) | local model serving & endpoint health | rostered — shonen |
| [kaidoku-shokunin](https://github.com/VeigaPunk/shokunin-reverse-engineering) | shipped-artifact reverse engineering (REA) | rostered — shonen |
| [revenger-shokunin](https://github.com/VeigaPunk/shokunin-binary-forensics) | binary forensics, evidence-ledger verification | rostered — shonen |
| [audio-shokunin](https://github.com/VeigaPunk/shokunin-game-audio) | game audio production | rostered — shonen |
| [game-dev-2d-shokunin](https://github.com/VeigaPunk/shokunin-godot-2d) | 2D game production, executable fixtures | rostered — shonen |
| [game-dev-3d-shokunin](https://github.com/VeigaPunk/shokunin-3d-engines) | 3D game production, headless fixtures | rostered — shonen |
| [lore-shokunin](https://github.com/VeigaPunk/shokunin-world-bible) | fictional-world records & consistency | rostered — shonen |
| [mori-shokunin](https://github.com/VeigaPunk/mori-shokunin) | fleet & host observability (森) — census gate, silence oracle, drift pin | repository link only — not in MANIFEST |
| [chousa-shokunin](https://github.com/VeigaPunk/chousa-shokunin) | deep-research method (調査) — research gate: claims/chains/sweeps/integrity verification | repository link only — not in MANIFEST |
| [kotodama-shokunin](https://github.com/VeigaPunk/kotodama-shokunin) | linguistic-cultural worldbuilding (言霊) — languages, myths, symbols, eras & costumes coupled; hands off to the lore world bible | repository link only — not in MANIFEST |

(2026-10 inventory note: mori, chousa, and kotodama have repository links here
but are not among the current 13 `MANIFEST.json` roster entries. The physical
local-directory count is 21; see the Round 12 audit for the exact census and
revision-bound lane verdicts.)


## Files

`PROTOCOL.md`, `PROTOCOL-APPENDIX.md`, `AXES.md`, `LEARNING.md`, and `CORPUS.md`
carry the reusable contract and its incident rationale; protocol and appendix
remain a required pair. Canonical synchronization revision:
`kimi-shokunin@e737d2ea97f6b0198503e077676c3f2ea07974a9` (recorded in
`MANIFEST.json`). `MISSION.md` and `shokunin.conf` bind this deployment; local
configuration and historical annotations do not override canonical rules.
`MANIFEST.json` — operator-controlled roster + append-only round history.
`ROADMAP.md` — human roster mirror. `scripts/` — source-aware round driver and
`sources-census.sh`. `.ufo/` — fleet evidence and state (`waves/`, `reports/`,
`prompts/`, `l0-questions.md`).
