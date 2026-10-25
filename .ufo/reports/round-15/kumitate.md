# kumitate — round 15

Lane `/home/vgpnk/projects/shokunin/kumitate-shokunin`. Axis move: **coverage**
— the round-14 pre-registration, executed in its declared fallback form. Round
identity **round 15**; report path `.ufo/reports/round-15/kumitate.md`.

## Decision

Round 14 pre-registered one move for round 15: name the last uncovered registry
family `R11` at internals level (⇒ `C1 19/19` ⇒ the frozen aggregate's terminal
value 10), and *either* split `coverage` in the same round *or* — if the split is
judged too large — retire the axis as saturated with the split recorded as its
successor. The fallback ran, for a reason that measurement, not taste, supplied:

- The pre-registration fixed the **partition** (`S1`–`S8` vs `R1`–`R11`) and
  "each keeping its own C1/C2 pair", but not the terms. That form is terminal:
  `C2_layer` is 1.0 by construction (every note a layer's rows reference already
  has a README row: 50 rows / 50 notes after this round's two notes), so both
  successors would have read `floor(10 × 1.0 × 1.0)` = 10 **under two new
  names**. Splitting with an unmeasured honesty term is a definition change
  slipped into the round that measures it — the failure this lane's `## Limits`
  names and rounds 12–14 avoided by pre-registering.
- Kasegi states the fleet's test at `kasegi-shokunin/SCORECARD.md:69-78`: a split
  must expose a *worse* number, not conceal it. A split that reproduces 10 fails
  it by construction.

So: `R11` landed alone; `coverage` is recorded at its terminal 10 and **retired**
in `## Retired`; the successors `coverage:script-layer` (S1–S8, 114 members) and
`coverage:runtime-layer` (R1–R11, 98 members) are declared with their terms
pre-registered in `## Planned` for round 16 to measure — each
`floor(10 × C1_layer/C1_total_layer × V_layer)`, where `V_layer` is the fraction
of that layer's declared members whose member section the claims gate verifies
(74 script-layer, 63 runtime-layer today, 137 total). Forecast integers 6 and 6
are labelled arithmetic, not measurements.

Operability was not touched (`A=5`, `C=10` — the round adds a note and a `yes`
cell, no script and no `- [` line); `f_O` stays `15/18 = 0.8333 ⇒ 8`, which is
still the intact axis.

## The artifact

`corpus/knowledge/runtime-remainder-census.md` (594 L): registry family `R11`,
**47 of 47 members / 24,874 L** — the `crates/ufo-core-runtime/src/*.rs` files
`R1`–`R10` do not name (93 − 51 = 42) plus all five `crates/ufo-cli/src/*.rs` —
one `## ` section per member, each with a live own-file anchor and a verbatim
symbol, plus a two-arm probe (the gate run and the `LC_ALL=C`-collated boundary
diff) and a size/class census (28 modules 14,081 L + 15 test files 7,912 L + 4
fixtures 2,881 L).

Measured before → after, same tools both sides:

```
before  PROXY: MATCH (A=5 C=10 operability=8; C1=18/19 C2=48/48 coverage=9; pins=5 match)
after   PROXY: MATCH (A=5 C=10 operability=8; C1=19/19 C2=50/50 coverage=10; pins=5 match)
before  CLAIMS: MATCH (rows=19 yes=18 notes=26 sections=90 adv=16)
after   CLAIMS: MATCH (rows=19 yes=19 notes=27 sections=137 adv=16)
gate    node scripts/claims-check.mjs --row R11
        → CLAIMS: MATCH (rows=1 yes=1 notes=1 sections=47 adv=0)
```

`adv=16` before **and** after: the last `no` cell closed without adding an
advisory, because `R11` is the only 47-member row written entirely in section
form.

## What the round found unplanned

1. **`R1`'s members were unenumerated.** The cell read ``8 `native*.rs` core
   modules`` — a glob matching 26 files in the crate — so `R11` could not be
   subtracted from the registry at all. The 8 are *forced*:
   `93 − 43 (R2–R10) − 42 = 8`, and the same set is exactly the `native*.rs`
   files the judge-pipeline note mentions ≥2× (both sorted lists hash
   identically). The cell now names them — registry **text** only; `R1` stays one
   `yes` cell (`--row R1` against a scratch scorecard → `CLAIMS: MATCH` exit 0,
   repo-wide advisories unchanged at 16).
2. **`comm` across collations is not a comparison.** The member list is
   `en_US.UTF-8`-ordered; `comm -3` against a C-ordered list printed *empty* once
   and a bogus `round.rs` line plus `comm: input is not in sorted order` the
   next. Both sides are now `LC_ALL=C sort`ed. Recorded in the note's probe.
3. **The residue diagnostic's recalled numbers were off by one.** Re-running the
   walk `SCORECARD.md` describes reproduces round 13's `195/211` only when
   `lessons/round-14.md` and the third-party
   `lessons/round-9-aggregator-corpus-verdict.md` are excluded; over the actual
   pre-round-15 corpus it reads **196/211**. This round moves it
   **196 → 201 / 211 ≈ 0.952** (5 basenames no earlier note carried:
   `bounded_fixture.rs`, `bounded_fixture_tests.rs`, `proposal_tests.rs`,
   `provenance.rs`, `provenance_tests.rs`; uncited remainder now 10). The
   diagnostic is unscored, which is exactly why nothing gated the stale recall —
   recorded in `## Limits`, not quietly fixed.

Doc repairs in scope of the move: `SKILL.md` (claims verdict line, the "four
pins" prose that has been five since round 14, the stanza key list, the
four-gate composition table → five instruments, a new `R11` corpus pointer) and
`corpus/knowledge/executable-scorecard.md` (line refs re-anchored after the
`SCORECARD.md` edits, the pins list, a new "Terminal values and retirement"
section, and a "round 12 = current readings" block that was two rounds stale).

## Verification

Ten-lane batched L2 dispatch, routed per the fleet map (planner/connector
`@m_lunamax`; executor/scout `@m_flash`; reviewer/critic/labrat/distiller
`@m_zfl`). Independent work that could falsify, and mostly did not:

- **Boundary** (`kx-scout-flash`): rebuilt the 47 from the tree and the registry
  cells — `comm -3` empty, `wc -l` 24,874, union pairwise disjoint over all 90
  ordered pairs, no basename collision in the 47 or against `R1`–`R10`, no
  member modified that day.
- **Sections** (`kx-reviewer`): independent derivation of all 47 (not a sample),
  then a gate-mirror replay of every footer claim → `47/47 VERIFIED`, zero
  defects, no `REF_OWNER_AMBIG`, `build_json.rs` correctly full-pathed against
  its same-basename sibling.
- **Gate arms** (`kx-labrat`): 8 doctored fixtures (absent note · 1-of-3 members ·
  anchor past EOF · blank anchor endpoint · no verbatim symbol · section outside
  the declared patterns · ambiguous basename · non-path-like heading) — 8/8 as
  the tool's header claims; `--strict` promoted the warning; a missing `--src`
  failed closed (exit 2).
- **Duplicates** (`kx-distiller`): heading scan of 51 corpus files → no duplicate
  member section for any of the 47; uniform heading style; `R1`'s old glob
  textually matched 8 `R11` basenames, which the enumeration removed.
- **Cross-lane** (`connector`): no contested scope, no R11 basename overlap in
  any sibling repo, and the only split precedent is kasegi's unsaturating one
  (which records "No axis retired") — this lane's retirement-at-saturation is the
  fleet's first.

Cites repaired in-round: one `UNRESOLVED epoch.json` (a runtime receipt under
`.ufo/`, not an origin path) and one `AMBIG directive.md` (35 same-basename
matches) were reworded out of the new note, which now yields **zero** plain-mode
findings; the repo-wide `errors=14` remain exactly the two third-party
aggregator artifacts, and no lane document is in that list.

Close evidence (lane HEAD after the `round-15` commit, pushed):

```
$ node scripts/round-gate.mjs --close
ROUND_GATE: CLEAN (round=15 lane=kumitate checks=13 errors=0 warnings=0)   # exit 0
$ node scripts/surface-probe.mjs --checklists
CHECKLIST: 10/10 pass   CHECKLIST_SKIPPED: 0   VERDICT: PASS
$ node scripts/surface-probe.mjs
SURFACE_PROBE: CLEAN (surfaces=2 checks=12 errors=0 warnings=1)
$ for f in cite-check surface-probe round-gate proxy-check claims-check; do \
    node scripts/$f.mjs --selftest; done
20/20 · 38/38 · ROUND_GATE_SELFTEST: 57/57 · PROXY_SELFTEST: 55/55 · CLAIMS_SELFTEST: 35/35
```

Prior-round anchors for this move: lane commit `dffbf0e` (round-14 artifact) and
`637d181` (round-14 close evidence), both ancestors of lane HEAD.

## SHONEN

`SHONEN.md` unchanged — still a shonen repo. Promotion needs the checklist's four
boxes; none is claimed here, and this round's own record names the reason: the
axis that just saturated is retired with its successors **unscored**, the
file-level residue is 0.952, and 9 of 19 registry rows are still note-existence
only. The honest state is "one live axis, one retired terminal value, two
successors declared".

## L0 side channel

Nothing filed this round: no decision was needed that the repo or the fleet SSOT
could not answer. The one candidate — "is retiring a saturated axis the right
call, or should the split have landed with it?" — is answered by this lane's own
pre-registration text and by kasegi's stated split test, so it is recorded in
`SCORECARD.md` `## Retired` rather than escalated.