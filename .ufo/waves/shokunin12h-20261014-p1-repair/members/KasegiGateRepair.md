# KasegiGateRepair — advisory (wave shokunin12h-20261014-p1-repair)

Seat: GateRepair executor (L2 leaf). Lane: `kasegi-shokunin` @ steered round 20.
Starting revision (baselines.json): `d1e6e8f3931a2bfbeb4319b9b41980c1e801e9f1`.
Measured HEAD at seat open: `d1e6e8f3931a2bfbeb4319b9b41980c1e801e9f1` (unchanged; no implementation edit).

This report is advisory data only — not a native judge verdict, lane round report, receipt, or admission.

## Gate registry discovered (SKILL + instruments)

From `corpus/instruments/README.md` (depth instruments of record) and SKILL/SCORECARD round-19 gate language:

| Gate | Path | Role |
|---|---|---|
| anchor range gate | `corpus/instruments/anchorcheck.py` | `path:NN[-MM]` range-check vs lane / mirror / origin / pin / lost-* |
| citation resolvability census | `corpus/instruments/resolve.py` | live path-like token census → `citation-survival.{md,tsv}` |
| density instrument | `corpus/instruments/density.py` | form-sensitive density only; **no** source-root resolution |

No other gate-default scripts under the lane (no `--src` CLI surface on any of the three).

Before-receipt already captured: `.ufo/waves/shokunin12h-20261014-p1-repair/evidence/kasegi-before.json`
(`python3 corpus/instruments/anchorcheck.py SKILL.md`, exit 0, rev `d1e6e8f…`).

## Existing `--src` / source-root resolution (inspected)

### `anchorcheck.py` (r19 landed)

```text
_MIRROR_CANDIDATES = ~/Projects/the-bounty-hunter, ~/Projects/origin-work/the-bounty-hunter
_ORIGIN_CANDIDATES = ~/Projects/origin-work/open-bug-bounties, ~/Projects/open-bug-bounties
_derive_root(env, candidates):
  env override if set → expanduser(override)   # explicit override retained even if absent
  else first existing isdir(candidate)
  else candidates[0]                            # canonical absent path (names expected base)
MIRROR = _derive_root('KASEGI_MIRROR', …)
ORIGIN_ROOT = _derive_root('KASEGI_ORIGIN_ROOT', …)
MIRROR_ABSENT / ORIGIN_ABSENT → BASE-ABSENT (own class, not bad)
```

Cite prefixes remain literal write-forms:
- `MIRROR_CITE_PREFIX = '~/Projects/the-bounty-hunter/'`
- `ORIGIN_CITE_PREFIX = '~/Projects/origin-work/open-bug-bounties/'`

Lane root: `KASEGI_LANE_ROOT` else nearest ancestor with `SKILL.md`/`.git`.

### `resolve.py` (r19 landed)

```text
MIRROR_CANDIDATES = ~/Projects/the-bounty-hunter, ~/Projects/origin-work/the-bounty-hunter
_derive_mirror(): $KASEGI_MIRROR | first existing | canonical absent
MIRROR_ABSENT recorded in generated census
```

Absolute `~/Projects/ufo-fsd-alpha…` tokens resolve via `os.path.expanduser` + existence (no indirection needed).

### `density.py`

No root / env / candidate logic.

## Measured root-default state (this host, seat-time)

| Root | env | derivation outcome | isdir |
|---|---|---|---|
| mirror | `KASEGI_MIRROR` unset | canonical-absent `~/Projects/the-bounty-hunter` | false |
| origin | `KASEGI_ORIGIN_ROOT` unset | canonical-absent `~/Projects/origin-work/open-bug-bounties` | false |
| ufo-fsd (hypothetical fleet pattern) | `UFO_SRC` unset | would select `~/Projects/ufo-fsd-alpha` | true |
| explicit bad override | `KASEGI_MIRROR=/no/such/mirror` | override retained → `/no/such/mirror` | false (stays bad → BASE-ABSENT path) |

- `UFO_SRC` string: **absent** from `anchorcheck.py`, `resolve.py`, `density.py`.
- `ufo-fsd-alpha` string: **absent** from those three gate files.
- Line-anchored `` `…ufo-fsd-alpha…:N` `` cites in lane `*.md`: **0**.
- Anchorcheck `CITE` regex does **not** match `~/Projects/ufo-fsd-alpha/…:N` shapes (by design of current cite surface).
- Live unanchored `~/Projects/ufo-fsd-alpha` tokens already `RESOLVES` under `resolve.py` (census TSV row).

## UFO_SRC claim vs gate bytes

Round-19 `LOG.md` / `SCORECARD.md` prose mention derived `$UFO_SRC` / ufo-fsd candidates in instruments. **Git diff of `d1e6e8f` on `anchorcheck.py` only added `KASEGI_MIRROR` + `KASEGI_ORIGIN_ROOT` derivation + `BASE-ABSENT`.** That is existing landed state, not a still-open gate defect:

- No gate consumes `$UFO_SRC/<rel>` tokens.
- No supported `path:line` form targets the ufo-fsd tree.
- Adding UFO_SRC wiring without a falsified gate failure would invent code against the wave rule.

Fleet pattern (`$UFO_SRC` → first existing `~/Projects/ufo-fsd-alpha` then `~/Projects/origin-work/ufo-fsd-alpha` → fail-closed; explicit bad `--src` stays bad) is the kama-style consumer pattern; kasegi's gates are domain-base (mirror/origin) consumers and already implement the analogous derive+fail-closed-absent semantics for those bases. No `--src` flag exists to harden further.

## Code changes

**None.** Measured unchanged. No gate-default implementation file edited. SCORECARD/LOG/notes/expected values untouched (out of seat scope).

## Proposed delta

N/A — no remaining falsified root-default defect on the registered gates.

## Unresolved debt (named; not gate-repair scope)

| Debt | Owner | Note |
|---|---|---|
| `MIRROR-SOURCE-LOST` | operator / restore `the-bounty-hunter@1cfbd86` or set `KASEGI_MIRROR` | already named in SCORECARD r19 |
| `ORIGIN-REPO-LOST` / `RECEIPT-STORE-LOST` | operator | historical; live ufo-fsd claims already re-anchored to `~/Projects/ufo-fsd-alpha` |
| LOG/SCORECARD `$UFO_SRC` wording vs instrument bytes | RecordPrep / HistoryClaims (prose) | documentation overclaim from r19; **do not** “fix” by inventing unused UFO_SRC gate code in this seat |
| LOST-RECORDED semantic audit (SCORECARD planned) | live-claims / history seats | verifiability floor debt; not root derivation |

Cross-domain: none for gate defaults. Adjacency to kama’s `tools/kama-probe.sh` UFO_SRC resolver is pattern-reference only; kasegi does not share that CLI.

## Parent gate commands (post-integration only)

Run from lane root `/home/vgpnk/Projects/shokunin/kasegi-shokunin` after any sibling edits land. Do **not** re-pin expectations; capture full stdout/stderr + exit + `git rev-parse HEAD`.

```bash
cd /home/vgpnk/Projects/shokunin/kasegi-shokunin
git rev-parse HEAD
python3 corpus/instruments/anchorcheck.py SKILL.md
python3 corpus/instruments/density.py SKILL.md --label r20-recensus
# resolve writes census beside the script; parent should snapshot or diff intentionally
python3 corpus/instruments/resolve.py /home/vgpnk/Projects/shokunin/kasegi-shokunin
```

Optional override smoke (fail-closed explicit bad base stays bad → BASE-ABSENT, not silent fallback):

```bash
KASEGI_MIRROR=/no/such/mirror python3 corpus/instruments/anchorcheck.py SKILL.md
# expect BASE-ABSENT (or LOST-RECORDED) paths naming /no/such/mirror; exit semantics per current script (summary only; no non-zero on bad cites today)
```

Before-receipt baseline for comparison: `.ufo/waves/shokunin12h-20261014-p1-repair/evidence/kasegi-before.json` (exit 0; summary class `7 in-range, 0 bad, LOST-RECORDED=306, BASE-ABSENT=0, …`).

## Axes note (advisory, unjudged)

- **freshness:** root derivation already r19-current for domain bases; no stale hardcoded present-path default remaining.
- **operability:** gates remain runnable with absent mirror/origin (BASE-ABSENT / GONE honesty).
- **calibration:** no code change → no score movement claimed.
- **adjacency:** UFO_SRC fleet pattern does not bind kasegi gate cite shapes; leave kama/kagi consumer gates to their seats.

## Verdict line for parent

`KasegiGateRepair: MEASURED UNCHANGED — no root-default defect; zero files edited; HEAD d1e6e8f3931a2bfbeb4319b9b41980c1e801e9f1`
