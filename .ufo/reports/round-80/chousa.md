# chousa round 80 — the scored set is drawn per run, and a Gate record becomes a line a counter re-opens

Attempt context: round 80 attempt 1 died mid-work (instruments/controls/claims preserved in
`0f59b985`); three later L1 relaunches died on provider errors before landing any report (amr 402
insufficient_balance, commandcode 401, opencode-go 402; markers moved to
`blocked/.chousa.run15-20261105-provider-failure-*` at 2026-11-05T02:20-03:00). The round is
unchanged. This attempt inherits the committed work of those attempts (lane tip `8e6a9c41`,
8 round-80 commits, local=remote, ahead=0), re-verifies it on this host, and lands the report.
Nothing was discarded; every inherited artifact was re-checked and is named below.

## Work performed

Two declared claims, two axes, causally separable, frozen before any seat scored
(`corpus/evidence/round80/claims.md`; freeze commit `0d253c95732c0ed19a9fa414e5d17769ddefa48d`;
instruments and both do-nothing controls `0f59b985933b2fe9b0b6a754d908ac6ae47399e6`; base
`b7803829922770b890e9f4efdd30d12c3695439a`):

- **C1 operability** (lowest scored non-retired axis; the historical 3/10 is held): the battery's
  scored subject set is drawn per run (`matrix-battery-v7.py`) instead of committed, so a
  classifier built from committed bytes cannot reach the PASS line. Before control: v6 accepts the
  structure-identity oracle (`corpus/evidence/round80/controls/oracle-structure-v6-accepted.txt`:
  `BATTERY_EXIT=0 BATTERY_VERDICT=PASS RECEIPT_LINES=113`, `ORACLE=ACCEPTED`, exit 1).
- **C2 calibration** (sourced on S200; C1 cites S199): round-79's prose Gate records become
  machine-checkable `GATE-RECORD` lines re-opened by `gate-grounding-check.py` over committed
  bytes at a named revision, resolving the three defective rows S196/S197/S198 by append-only
  supersession. Before control: `controls/grounding-before.txt` →
  `GATE_GROUNDING=FAIL unresolved=3 superseded_resolved=0 audited=S196,S197,S198`, exit 1.

Work items, each with evidence:

- Instruments, do-nothing controls and the claims text landed pre-freeze in one preserved commit
  `0f59b985` (`matrix-battery-v7.py` sha256 `35351b23…8914d`, `gate-grounding-check.py` sha256
  `d9e42621…c553`, `oracle-check.py`, `forgers/a10-payload-decode.py`; receipt sha256s pinned in
  `claims.md`). The preservation-commit shape is itself mined as a `## Mistakes` row
  (`corpus/lessons/round-80.md`).
- Claims frozen, wave spec filed and validated (`0d253c95`; `w1-validate.rc` = 0 under the run-15
  band 8–16, `stderr_bytes=0`).
- Registry rows S199–S202 registered with `GATE-RECORD` lines (`44d09edf`); all four are
  revision-pinned committed paths opened by `git show`, no URL fetched; the three superseded rows
  resolve through their replacements (counter output below).
- QUALITY 152–154, SKILL Gates table rows for the counter and battery, the round-79 erratum
  (`corpus/lessons/round-79-erratum.md`) and the after receipt landed (`5ba30d87`); QUALITY
  155–159 with the claim outcomes and verdict rows (`596c2f2a`); QUALITY 160 and the
  duplicate-record limit (`e3820839`).
- Wave **w1** — the round's one v1 wave, dispatched through the inline spawn handoff
  (`.ufo/waves/round-80/w1.ready` taken 2026-11-04T23:58:32): **12 seats** — executor×3, scribe×2,
  reviewer×2, scout/critic/mutation-tester/sentinel/connector×1. Attack share 5/12 ≈ 42 % (≥25 %);
  1 connector (≤2). All 12 seats settled with output, **0 dead seats**
  (`.ufo/waves/round-80/w1-results.json`; seat reports committed at `b20af227`, settlement at
  `03598f95`). No residual task call; round total 12. The orchestrator wrote the results handoff
  only after all seats settled; no wave launched by this attempt, so the WAVE-DONE precondition
  for filing is met by that settled handoff.
- Wave findings integrated: instrument limits 1–8, the record-class scope survey
  (33 records: 17 ok / 10 count-mismatched / 5 quote-absent / 1 no-quote across lessons 70–79;
  3 closed this round, 12 routed to round 81's plan), and both kill-rule firings recorded in
  `corpus/lessons/round-80.md` — reported, never repaired after scoring.
- Correction: the inherited attempt had relabelled the verdict cells of seven earlier rounds' rows
  in place; the seven rows are restored byte-for-byte and the relabel is withdrawn on the record
  (`8e6a9c41`; `git diff b7803829..HEAD -- SCORECARD.md` = 73 insertions, **0 deletions**; only the
  two rows inside `## Round 80 verdict` carry the new token). Recorded in SCORECARD §Correction
  and as a `## Mistakes` row.
- This attempt (2026-11-05) re-verification on this Linux host: census exit 0;
  `python3 -B corpus/evidence/round80/gate-grounding-check.py --rev
  44d09edfc20dba26ee8d58a93d365989916a2692` → `GATE_GROUNDING=PASS unresolved=0
  superseded_resolved=3 audited=S199,S200,S201,S202`, rc=0;
  `python3 -B corpus/evidence/round79/selfcheck-v2.py --lane .` → `SELFCHECK2=PASS
  unresolved=0/3`; `bash tools/research-gate.sh --selftest` → `RESEARCH_GATE_SELFTEST: PASS
  (275 cases, 0 skipped)`; one fresh `matrix-battery-v7.py` run reproduced the recorded
  draw-dependence (`BATTERY=FAIL forgers_rejected=11/11 positive=2/2 fresh_positive=1/2
  fresh_forgers=1/2 oracles_rejected=5/5` — a FAIL draw, matching the recorded run2/r80d
  receipts, confirming C1's honest stop rather than a stable PASS). Cleanup: the inherited
  ~2.1 GB `/tmp/r80-{base,decl,tip}` trees (named in `## Mistakes`) and the scratch root
  `/fast/scratch/hyaku/chousa-r80` are removed; misroot sweep clean (fleet dirty state is the
  orchestrator's `.scratch/run15-state.json` only — no seat wrote into the fleet root).
- Stray inherited artifact: `.ufo/waves/round-80/w2/Exec/SubjC2 RECEIPT/` (committed) — a wave-2
  directory the inherited attempt staged but never validated or dispatched (no `w2-dispatch.json`,
  no `w2.ready` ever existed). Its receipts (R80ExecC's subject-honest C2 reading and a 5-run v7
  stability note) are retained as committed evidence; no wave-2 counts toward this round.

## Landed changes

All changes are inside the lane repo, committed under the lane identity through `jj-lane.sh`, and
tied to the `LOG.md` entry `## Round 80` (LOG.md:2313) or to the round lesson's `## Mistakes`
table:

| change | commit | record |
|---|---|---|
| instruments, do-nothing controls, claims text | `0f59b985` | lesson `## Mistakes` row 1; claims freeze evidence |
| claims freeze + w1 wave spec | `0d253c95` | `corpus/evidence/round80/claims.md`; `w1-spec.json` |
| registry S199–S202 + GATE-RECORD lines + re-run controls | `44d09edf` | LOG `## Round 80`; lesson `## Gate` |
| QUALITY 152–154, SKILL Gates rows, round-79 erratum, after receipt | `5ba30d87` | LOG `## Round 80` |
| wave evidence, QUALITY 155–159, claim outcomes, verdict rows | `596c2f2a` | LOG `## Round 80`; SCORECARD `## Round 80 verdict` |
| QUALITY 160 + duplicate-record limit | `e3820839` | LOG `## Round 80` |
| twelve seat reports + record-class scope | `b20af227` | `corpus/lessons/round-80.md` §Scope |
| wave settlement (w1-results.json, 12/12) | `03598f95` | LOG `## Round 80` |
| seven verdict rows restored + correction + census | `8e6a9c41` | SCORECARD §Correction; lesson `## Mistakes` |

Lane tip `8e6a9c4178ede774bdfb4e320297315ce56644e4`; `git ls-remote origin refs/heads/master`
prints the same hash (on-branch, pushed). No tool installs were made by the lane or any seat this
round.

## Before → after measurements

**C1 operability** (measured against base `b7803829` for the before control, landing for the after
receipt):

```
python3 -B corpus/evidence/round80/matrix-battery-v7.py \
  --matrix corpus/evidence/round76/loader-matrix-v3.py --work DIR --runs 1 --fresh 2 \
  --rev b7803829922770b890e9f4efdd30d12c3695439a
```

- before (`controls/oracle-structure-v6-accepted.txt`, v6 + structure-identity oracle):
  `BATTERY_EXIT=0 BATTERY_VERDICT=PASS RECEIPT_LINES=113`, `ORACLE=ACCEPTED`, exit 1.
- after (`controls/v7-legit-matrix-r80.txt`): `BATTERY=PASS forgers_rejected=11/11 positive=2/2
  fresh_positive=2/2 fresh_forgers=2/2 oracles_rejected=5/5`, exit 0.
- verdict: **falsified by its own kill rule — honest stop.** The predicate is draw-dependent: run1
  PASS 2/2+2/2, run2 FAIL 1/2+1/2, `--fresh 3` FAIL 0/3+0/3 (wave receipts
  `R80ExecA/r80a-after-v7-run1.txt`, `r80d-v7-run2.txt`, `r80d-v7-run3-fresh3.txt`; cause: the
  fresh-leg name collision, `R80CriticA/receipts/c1-name-collision-probe.txt` — fails closed, not a
  false green); one of the five counted oracle rejections never produced a verdict
  (`_rename` AttributeError, `R80SentinelA/receipts/09-rename-defect-repro.txt`); the fresh leg's
  ground truth is the witness matrix itself (`06-fresh-leg-ground-truth.txt`). This attempt's fresh
  run reproduced a FAIL draw (1/2+1/2, oracles 5/5, forgers 11/11). The remaining content stands:
  the two known forged matrices no longer reach PASS on the drawn leg where v6 accepted them.
  Successor rules: QUALITY 156–159; round-81 plan.

**C2 calibration** (measured at `44d09edf` for the after state, base for the before control):

```
python3 -B corpus/evidence/round80/gate-grounding-check.py --rev 44d09edfc20dba26ee8d58a93d365989916a2692
```

- before (`controls/grounding-before-r80.txt`): `GATE_GROUNDING=FAIL unresolved=3
  superseded_resolved=0 audited=S196,S197,S198`, exit 1.
- after (`controls/grounding-after.txt`; re-run by this attempt, identical output, rc=0):
  `GATE_GROUNDING=PASS unresolved=0 superseded_resolved=3 audited=S199,S200,S201,S202`.
- verdict: **falsified by its own kill rule — honest stop** on the frozen third clause: a
  `GATE-RECORD` line naming bytes the counter never opened still yields `unresolved=0`
  (`R80CriticA/receipts/c2-unopened-superseded-record.txt` — a record attached to a non-tip row is
  parsed and never opened), and a hollow record passes (`c2-donothing-control.txt`). The mechanism
  lands and the three named defects are genuinely closed by supersession with measured counts
  (12/20/25/2 words); the counter's four grammar rules are discriminating only within their own
  scope (instrument limit 3, measured at `--since-round 70` = 17 unresolved). Successor rules:
  QUALITY 155, 160; round-81 plan.

Do-nothing controls: a round that does nothing cannot reach either after-state — at the base the
v6 battery accepts the structure-identity oracle and the C2 counter prints `unresolved=3` with
`record=none` on all three rows. Neither claim verifies as frozen, so this round is filed as an
honest stop on both claims; admission is the operator's after non-author verification.

## Sources & frontier

- Registry rows: **198 → 202** (S199–S202 added). Census command and outputs:

```
$ /home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin chousa
chousa	W04	S051 duplicate url www.w3.org/TR/2017/REC-html52-20171214/syntax.html across scopes
chousa	W04	S053 duplicate url docs.python.org/3/library/socket.html across scopes
chousa	W04	S073 duplicate url www.gnu.org/software/coreutils/manual/coreutils.html across scopes
chousa	W04	S074 duplicate url docs.python.org/3/library/hashlib.html across scopes
chousa	W04	S075 duplicate url www.gnu.org/software/coreutils/manual/coreutils.html across scopes
chousa	ok	/home/vgpnk/Projects/shokunin/chousa-shokunin/corpus/SOURCES.md
```

  Recorded at round start (`census-start.txt`, 2026-11-04T22:20) and round end (`census-end.txt`,
  2026-11-05T00:46) — identical output; both exit 0, and this attempt re-ran it at the tip: rc=0.
  The five W04 warnings are pre-existing and unchanged.
- Rows added by tier: B — S199, S200, S201; C — S202. All `own-work`, status `mined`, recheck
  `on-release`, `used-by corpus/lessons/round-80.md`.
- Rows touched old→new: **none** — the registry is append-only; no `status`/`recheck`/`used-by`
  cell of an existing row changed; S196/S197/S198 are superseded by the new rows S200/S201/S202
  with measured counts (12/20/25/2 words, `wc -w`) and a corrected anchor span (11 lines, not 20).
- Frontier rows advanced: all four opened this round by `git show <rev>:<path>` at pinned
  revisions (no external URL fetched); each carries a `GATE-RECORD` line that the counter re-opens
  on committed bytes.
- Sourced claim: C2 lands citing **S200** (frozen `claims.md`; the lesson's outcome table labels
  C2 "sourced on S199" — both rows are new this round, so the sourced-claim requirement is met
  either way; the frozen file's S200 binding is the authoritative one and is not amended).
  C1 cites S199.
- Mistake mined: `corpus/lessons/round-80.md` `## Mistakes` — four rows (class · evidence ·
  captured-by · fix): the preservation-commit shape; the ~2.1 GB inherited `/tmp` clones; the
  QUALITY criterion citing an uncommitted receipt (caught by the round-79 counter's S2 leg); the
  C2 predicate satisfied by rows the round itself added; plus the seven-row verdict relabel row.
- Assimilation: none — the `merge/chousa/` package stays closed (round 78 measured 111 of 114
  staged ids colliding with the live registry; the drift is not renumbered in scratch). No package
  bytes read into the lane, no campaign tool run, no shokuknow write.
- considerthese: `considerthese/2026-10-26.md` (newest) opened; proposal 4 — one independent CJK
  quote spot-check per review — adopted as QUALITY 158 (`wc -w` prints 2 for a 68-character CJK
  span, so the ≤25-word bound cannot measure such a row). Proposals 1–3 not picked (one proposal
  per round).

## Trend verdicts

- **expansion: unchanged** — `PROVINCE.md` untouched (`git diff b7803829..HEAD -- PROVINCE.md` is
  empty); no `corpus/knowledge/` entry; the four new registry rows are own-work tier B/C evidence
  records opened from the lane's own committed bytes, not new domain ground; the connector seat
  compared seven sibling revisions read-only and absorbed none.
- **quality: improved (narrowly)** — operability and calibration axis verdicts improved narrowly
  (SCORECARD `## Round 80 verdict`): two machine-checkable instruments landed and reproduced on
  this host this attempt (gate counter PASS rc=0; battery drawn leg rejects 11/11 committed
  forgers where v6 accepted the structure-identity oracle); the depth (unchanged) and freshness
  (unchanged) surfaces moved not at all; every defect the wave found is recorded and
  QUALITY-routed (155–160), not hidden.
- **discernment: improved (narrowly)** — both claims fired their own frozen kill rules and are
  filed as honest stops rather than prettified; the round caught its own in-place relabel of seven
  filed verdict rows and withdrew it byte-for-byte (self-assessment vs observed state now matches:
  0 deletions vs base); the counter's blind spots (unopened superseded record, hollow record,
  `--since-round` window) are measured and named instead of repaired after scoring.

No axis is harmed: the lane gate selftest is `PASS (275 cases, 0 skipped)`, the round-79 counter
is `SELFCHECK2=PASS unresolved=0/3` at the landing, the census is exit 0 at both ends, and every
change to a frozen artifact is append-only.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources —
  `SKILL.md` Gates table (gains the round-80 counter and battery rows, `5ba30d87`);
  `corpus/knowledge/metadata-screen-r25.md` (lane assertion; no non-author verifier this round)
- [~] At least one end-to-end domain task executed and logged in LOG.md — LOG.md `## Round 80`
  (LOG.md:2313): the two-claim battery/counter round executed end to end with before/after
  receipts (lane assertion)
- [~] Instructions executable by an agent without oral context — `bash tools/research-gate.sh
  --selftest` → `PASS (275 cases, 0 skipped)` re-run by this attempt;
  `corpus/evidence/round80/{matrix-battery-v7.py,gate-grounding-check.py}` runnable as documented
  (lane assertion)
- [~] No cross-domain bleed (PROVINCE.md still accurate) — `PROVINCE.md` diff vs base empty;
  `R80ConnectorA` read-only sibling comparison absorbed none (lane assertion)

## Extras

- **Stale-lane:** no — respawn-per-round driver only; no other mission of this lane is open.
- **Round shape:** one v1 wave (w1) of 12 seats under the run-15 band 8–16 (`w1-validate.rc` = 0);
  ≥25 % attack share met (5/12); 1 connector; no residual task call; **round total 12 seats**;
  0 dead seats. The §3 planner seat is held by this L1; no planner role was dispatched.
- **Inheritance:** all work reused is committed and named above; the discarded set is empty; the
  two filesystem cleanups (inherited `/tmp` clones, scratch root) are recorded in `## Mistakes`
  and this report.
- **Open L0 questions (routed around, non-blocking):** chousa round-62 (SKILL.md size threshold),
  round-70 (bare `## Capabilities` headings; flock gating on the Windows host — moot on this
  Linux host, still formally open), round-71/round-72 (sibling-lane host-load relief).
- **No-harm re-checks this attempt:** census rc=0; `SELFCHECK2=PASS unresolved=0/3`;
  `RESEARCH_GATE_SELFTEST: PASS (275 cases, 0 skipped)`; SCORECARD verdict-table diff vs base
  shows 0 deletions.
