# kagi-shokunin — Round 29 report (2026-10-31/11-01, new Windows host)

Frozen BASE `c49023b773b69de983f0e6eb7e5867ceb5c2c634`; plan + START census
`66d1a2c` (committed alone); plan corrections `47a46d1` (alone, before any
work commit, QM29); lane head `49d1d46e69bf83283a1b001ec4eff16000d6508e`,
pushed origin master. The round executed on a NEW host (Windows 10.0.26200
x64, Git Bash, Python 3.13.15 as `python`; `python3` is a Store stub) —
honest-absence protocol work is below. Stagnation nudge fired (all six axes
at the saturation line 9; rounds 26–28 capability-less), waiving the
lowest-axis obligation; C2 is the frontier/capability move. Claims declared
in the frozen `plans/round-29.md`: **C1 freshness** (routed D1 closure via
the frozen round-28 recipe) and **C2 capability acquisition**.

## Work performed

- **Host receipt (honest absence; no claim).** the-janitor handler,
  `~/.config/the-janitor` (the op.env fixtures) and
  `~/.local/state/the-janitor` are ABSENT on this host — receipt
  `fleet/kagi-shokunin/.ufo/waves/round-29/final/substrate-absence.txt`
  (ls exits 2 on all three). An `op` CLI 2.39.0 IS present via WinGet and
  was left untouched: nothing installed, signed in, provisioned or pinned;
  no vault/account contact at any point (§7 hard rule held). PROVINCE.md
  carries the dated round-29 host erratum (evidence pointer above).
- **C1 (freshness; frozen recipe).** Applied the round-28 §Attempt-3
  corrigenda 1 recipe verbatim: the three feed extractors
  (`STABLE_TITLE_RE`, `STABLE_TAG_HREF_RE`, `TEXT_VERSION_RE`) take the
  `STABLE_TOKEN_RE` right boundary `(?![A-Za-z0-9+-]|\.[0-9])` instead of
  `$`/`[ \t]*$`, plus the recipe's one positive and one negative selftest
  case on the feed path (114 → 116). Grounded by S052 (RFC 4287 §4.2.14,
  opened this round). BASE fail-open re-verified by direct probe before the
  fix (`final/base-probes.txt`: older-canonical-wins and
  canonical-invisible both reproduced at `c49023b`). One pre-existing,
  round-unrelated defect was found and routed by authorized correction:
  the selftest's receipt-mode case asserted POSIX `0o600`, failing on NTFS
  at BASE itself (`final/base-selftest-host.txt`) — POSIX-scoped per
  Correction 1 (M29-1, red-before committed).
- **C2 (capability; stagnation-nudge move).**
  `corpus/feed-token-agree.py` — the differential feed-token agreement
  gate from `considerthese/2026-10-25.md` proposal 1: imports the LIVE
  extractors and shared token grammar (never copies), runs a fixed
  12-shape corpus through all three extractors in their natural wrappers,
  fails naming shape + extractor on any deviation; hermetic `--selftest`
  (synthetic extractors only, seeded `$`-anchored divergence must be
  caught). Red witness retained: at `0229375` (gate present, BASE
  instrument bytes) the live run read DISAGREE with m3=0/m4=1
  (`final/c2-base-gate.json`); at BASE itself the artifact did not exist
  (`final/c2-base-plain.json`, all booleans false).
- **Frontier step.** SOURCES.md 51 → 52 (S052, tier A spec, opened
  2026-10-31, capture row in `source-fetches.tsv`); one new knowledge
  entry `corpus/knowledge/feed-token-boundaries.md`
  (source: S052, S045; Reverify: R29-01, R29-02). Mistakes M29-1..M29-3
  mined into `corpus/lessons/round-29.md` §Mistakes (host-property
  assertion; host environment: python3 stub + NTFS case collision; unrun
  full ledger verify → QM12 substitute). QM30 added to `corpus/QUALITY.md`.
- **L2 wave — honest miss.** MISSION.md's ≥8-subagent batched floor could
  not be met on this host: a 9-seat read-only verification script was
  authored and compiled cleanly, but CreateWorkflow reports "workflow
  execution is not available in this session". No seat ran; nothing is
  claimed on seats' behalf. The deterministic counter re-runs the wave
  would have gated were executed directly by the L1 and are recorded under
  Measurements. The script text is retained in the session record.
- **Refused work:** the 2026-10-21 refusal was not retried, rephrased,
  summarized or rerouted; the C1 tokenizer defect was touched only via the
  frozen recipe (operator ruling 2026-10-31). No secret values anywhere;
  no `op://` references.

## Landed changes

| Commit | Contents |
|---|---|
| `66d1a2c` | frozen `plans/round-29.md` + START census (pre-seeded, pre-work) |
| `47a46d1` | plan corrections 1–2 (host adaptation; sparse archive export) — alone, before work |
| `0229375` | instruments (`tools/c1-measure.py`, `tools/c2-measure.py`), `corpus/feed-token-agree.py`, BASE before-receipts (`c1-before.json`, `c2-base-plain.json`), host probes (`base-probes.txt`, `base-selftest-host.txt`, `substrate-absence.txt`) |
| `fc65112` | C1 fix in `corpus/release-clock.py` (3 regex lines + 2 selftest cases + Correction-1 POSIX scope); S052 + fetches row; knowledge entry; PROVINCE (erratum + 116 + gate bullet); SKILL.md 116; QUALITY QM30; self-counts +2 rows; lesson; SCORECARD (pre/post + capability row); LOG; ledger R25-03 migration + R29-01/R29-02; stamps 91 → 94; `c2-base-gate.json` |
| `bc2f3fd` | measured outcomes appended (lesson §Measured outcome, SCORECARD, LOG), after-receipts `c1-after.json`, `c2-after.json`, re-stamps |
| `49d1d46` | the S045 used-by back-reference committed (the one file commit D missed; closes the SC_ENTRY_CITE handshake IN the committed tree; instruments' measured revision `fc65112` differs from it only by this SOURCES.md cell, which no fixture reads — the observe fixtures narrow the registry away) |

LOG.md carries the round-29 entry with all evidence pointers. Stamps
verified 94/94 twice: against the working tree after the final append, and
against the committed HEAD blobs (every stamped path byte-equal in HEAD).

## Before → after measurements

Counting commands (Correction-1 host interpreter; frozen instruments):

    python -I -B .ufo/waves/round-29/tools/c1-measure.py <rev> <label> <out.json>
    python -I -B .ufo/waves/round-29/tools/c2-measure.py <rev> <label> <out.json>

- **C1** (receipts `final/c1-before.json` @ `c49023b`, `final/c1-after.json`
  @ `fc65112`): `C1_MEASURE before: NF mishandled=5/7 correct=2/7 … replay
  mishandled=0/4 typed=4/4 … control_clean=True` (exit 1) → `C1_MEASURE
  after: NF mishandled=0/7 correct=7/7 … replay mishandled=0/4 typed=4/4 …
  control_exit=0 control_clean=True` (exit 0). Regression: the round-28
  counter replay stays green at both revisions; default control CLEAN30;
  selftest 114 → 116 (only the recipe's two cases); NF6/NF7 refused-
  controls identical at both revisions. Do-nothing control fails the
  after-target by construction (the BASE receipt predates any candidate
  commit).
- **C2** (`final/c2-base-plain.json` @ `c49023b`, `c2-base-gate.json` @
  `0229375`, `final/c2-after.json` @ `fc65112`): `C2_MEASURE base-plain:
  m1=0 m2=0 m3=0 m4=0` → red witness `m1=1 m2=1 m3=0 m4=1` → after
  `m1=1 m2=1 m3=1 m4=1` (exit 0). The capability row entered the
  SCORECARD capabilities table on this measured after-state.
- **Regression battery at `fc65112`:** release-clock `--selftest` ⇒
  `RELEASE_CLOCK_SELFTEST: PASS (116 cases)` exit 0 (one explicit SKIP
  line on nt — M29-1's declared limit); default ⇒ `RELEASE_CLOCK: CLEAN
  (on_release=30 bound=30 unbound=0 observed=30 fired=3 derived=15)` exit
  0 (R25-04 unchanged); checklist-run selftest PASS 34; op-ref-probe
  selftest PASS 36; lane census CLEAN.
- **Bookkeeping receipts (QM12 substitute, M29-3):** touched/added ledger
  rows re-run individually, all exit 0 — R25-03 (migrated 114→116, old
  value + reason in the row note), R25-04, R29-01 (`PASS (4 cases)`),
  R29-02 (`AGREE (shapes=12 disagreements=0)`). New self-counts bindings
  verified individually (12/12, 4/4, 116). Full `claim-ledger verify`
  (>300 s) and `self-counts` (>240 s) do not complete on this host —
  recorded, not hidden; the round-28 Linux-host full-verify receipt stands
  for the ledger-wide claim.

## Sources & frontier

SOURCES.md rows 51 → 52. Counting commands and outputs:

    bash <fleet>/scripts/sources-census.sh validate --root <fleet> kagi
    START (2026-10-31): exit 0 — 14 W04 (S019…S051 duplicate-url warnings) + ok
    END   (2026-11-01): exit 0 — same 14 W04 + ok
    bash <lane>/corpus/sources-census.sh
    END: SOURCES_CENSUS: CLEAN (rows=52 A=50 B=0 C=2 queued=1 mined=48 rejected=3 entries_sourced=5 legacy=21 captures=52 inrow=16 inrow_only=0 inrow_nonreproducing=12) exit 0

S052 (RFC 4287 §4.2.14, tier A, 180d) was opened 2026-10-31 with the
declared curl profile; capture digest and located quote recorded in
`corpus/source-fetches.tsv` and the lesson Gate. One registry cell changed
old → new, logged in the lesson: S045 `used-by` gained the new knowledge
entry (the census's SC_ENTRY_CITE handshake fired once on first contact and
was closed by that back-reference). No source was rejected this round; no
re-opened row changed status/recheck.

## Trend verdicts

- **expansion: unchanged.** No new governed host surface and no knowledge
  ground beyond the lane's own token-extraction surface; registry +1 row on
  opened ground (`R21-02` population); the capability is a new repertoire
  entry (counted under capabilities, not coverage).
- **quality: improved (behaviour measured, scalars held).** C1 closed a
  real fail-open with the frozen recipe and green replay/control receipts;
  C2 turned the D1 class into a standing gate with a retained red witness.
  freshness/calibration/depth/operability/adjacency all 9 → 9 with the
  increments recorded per axis in SCORECARD (no double-counting).
- **discernment: unprovable-but-better.** Three mistakes mined with fixes
  shown able to fail (committed red-before states), QM30 added, the C2 red
  witness kept instead of smoothed, and the C1 "sourced" leg rests on a
  row opened this round — but outside admission stays with the operator;
  no non-author reviewer judgment was obtainable on this host (see the L2
  note), so self-admission is not claimed beyond the measured behaviours.

## SHONEN

SHONEN.md still exists (not promoted); all four boxes remain `[~]` with
resolvable evidence pointers, unchanged this round:

- [~] SKILL.md real tables/citations — evidence pointer LOG.md:758
  CITATION_GATE line (historical receipt; citations mode did not re-run on
  this host, recorded as M29-3).
- [~] end-to-end domain task logged — LOG.md round-3 entry (historical;
  substrate absent on this host, so no new end-to-end handler task was
  possible; honest absence recorded in PROVINCE).
- [~] instructions executable without oral context — this round adds two
  more runnable proofs on the new host: release-clock selftest PASS 116
  and feed-token-agree PASS 4 / AGREE 12 (commands re-run here).
- [~] no cross-domain bleed — PROVINCE round-29 host erratum reports the
  new host and the present `op` CLI without absorbing or provisioning it.

**Assimilation:** `considerthese/2026-10-25.md` proposal 1 (differential
tokenizer test) is mined as C2 — the one still-unimplemented proposal
taken this round, grounded through the frozen plan's bar;
`considerthese/2026-10-26.md` suggestions 2–3 remain noted for the
operator/HOLD path. The shokuknow register is not reachable from this
host. Assimilation: none — shokuknow unreachable.

## L2 wave note (honesty)

MISSION.md's L2 floor (≥8 subagents, one batched call) is UNMET this
round: the 9-seat batched verification script compiled cleanly but the
host exposes no workflow execution in this session ("workflow execution is
not available"). Nothing was simulated; the counters the wave would have
run deterministically were run and recorded by the L1 above, and every
verdict in this report is re-derivable from the committed receipts.
