# kaika (開花) — shokunin fleet campaign plan

## Operator goal (verbatim)

"make the shokunin and all related repos smarter, more elegant, they should explore,
build corpuses, keep the essence of the shokunin that's well outlined in the main repo;
while also using heavy parallelization to be able to research, refine, explore, develop,
unfold, new techniques, current art, learn by making mistakes, a continuous improvement;
that builds a continuous corpus and curation of sources of where to learn more from."

Operator directives: 64–100 delegations, dispatched continuously; models via OMP aliases
`m_luna`, `m_haiku`, `m_flash`, `m_zfl`; connectors on `m_antigravity`; code-heavy work on
`m_swe`. Standing fleet rule: **no push** (ledger notes "No push (standing rule)").

## Repos

| Repo | Path | Role in campaign |
|---|---|---|
| fleet root (main repo) | `~/Projects/shokunin` | protocol + aggregator lanes; MANIFEST/LOG/SCORECARD/.ufo reports; the essence lives here |
| 21 lane repos | `~/Projects/shokunin/<id>-shokunin` | one craft round each |
| canonical protocol | `~/Projects/kimi-shokunin` | lags the fleet root (multi-claim rounds, exploratory claims, registry home, capabilities table not upstreamed); HEAD bc7d690 reverted Craft-hours — do not reintroduce |
| out of scope | `~/Projects/ufo-fsd-alpha` (another live session), domain source trees, every remote | read-only |

Lanes: audio chousa game-dev-2d game-dev-3d kagi kaidoku kake kama kasegi kengaku kotoba
kotodama kumitate lore mado mori revenger souji tabi tameshi tsukuroi.

## Deliverables

- **D1 `corpus/SOURCES.md` per lane** — curated "where to learn more" registry (contract in the
  wave context). Every row opened in the round that writes it.
- **D2 one protocol-conformant craft round per lane** — 1–3 claims (≥1 on the lowest non-retired
  axis), falsifiable before→after with counting commands; new `knowledge/` entries on uncovered
  coverage-map ground from current art, through the lane's own `corpus/QUALITY.md`;
  `corpus/lessons/round-<N>.md` with `## Gate` (+ `## Mistakes` mined from the lane's own
  rejected rounds/errata); `SCORECARD.md` + `LOG.md` (append-only); fleet report
  `.ufo/reports/round-<N>/<id>.md`; `MANIFEST.json rounds[]` closure.
- **D3 fleet contract** — `CORPUS.md`, `LEARNING.md`, `templates/round-prompt.md` (+ PROTOCOL.md
  file-contract row) codify SOURCES.md, mistake mining, and a research/curation step in every
  round so the continuous loop keeps growing the corpus.
- **D4 fleet instrument** — `scripts/sources-census.sh`: aggregates lane SOURCES.md into a fleet
  index, flags malformed rows, overdue rechecks, sources shared across lanes; self-test.
- **D5 canonical sync** — kimi-shokunin `skills/shokunin/protocol/*`, `templates/`,
  `skills/shokunin/SKILL.md` brought to the fleet root's amended protocol + D3.

## Waves (≤100 members this round; spawn waves 16–32 lanes)

| Wave | Members | Work | Writes |
|---|---|---|---|
| W1 research | 32 | 21 lane dossiers + 11 fleet probes | `local://kaika-w1-*.md` only |
| W2 writers | ~23 | 21 lane executors + D3 + D4 | each in its own git worktree |
| W3 verify | ~24 | 21 non-author lane reviewers + D3/D4 review + D5 writer | D5 worktree only |
| W4 remediation | resumes | fix failed claims inside original scope | original worktrees |

## Ownership and isolation

- Parent (tower L1) is sole coordinator, judge-of-record and integrator: defines shared contracts,
  creates worktrees, commits with the lane git identity (`<id>-shokunin <<id>@shokunin.local>`),
  writes fleet reports + MANIFEST entries + root LOG/SCORECARD, merges, verifies.
- Lane writer scope: its lane worktree only (`.tower/worktrees/kaika/<id>-shokunin`, branch
  `kaika/<id>-r<N>`). D3 and D4 get separate fleet-root worktrees with disjoint file sets.
- Verifiers are fresh agents on a different model than the lane's writer (non-author).
- Executors do not commit; the parent commits after review.
