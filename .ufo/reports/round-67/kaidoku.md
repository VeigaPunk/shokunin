# kaidoku — round 67 (attempt 1)

Lane: `/home/vgpnk/Projects/shokunin/kaidoku-shokunin` · base `a7a4ce6902204d5c6cc6c4e3e78b4bffe8312b92` ·
operative freeze `3663e6b21dccf4c4957f459301156664d8b151d6` · final lane tip
`451f3102c1be3fe476b8c600979eba5ecaade1f8` (`jj-lane.sh state` → local = remote, ahead 0) · prompt
`.ufo/prompts/kaidoku-round-67.md` (704 lines, committed `b8507c60` by the lane identity).

## Work performed

The round declared **two claims** on distinct axes, each with its own frozen counter, do-nothing control and
before-arm committed before data, and each causally separable:

- **R67-C1 — coverage, frontier → core.** `squashfs_v4_le` on LE AVM-marker (`hsqs`) SquashFS v4 members of the
  four chain-pinned vendor carriers moves Frontier → Core, re-scored under a round-67 gap rule that classes
  char-device entries as not-publishable instead of per-row required. Predicate: the pinned round-50 engine, run
  under the round-67 rule and bindings, reports `carriers_matched 4 of 4` with `met_target true` and exit 0, while
  the same four frozen envelopes under the round-50 rule report `gaps_ok` on 2 of 4.
- **R67-C2 — depth, counter repair.** A new selftest battery kills the two round-66 mutation survivors (the closure
  counter whose `arm()` returns `passed: true` unconditionally; the coverage counter whose `recipe_a_equivalence`
  returns equivalent without running the block) while both pristine counters stay green, and the round-66 selftests
  alone leave both alive.

Work items, each with its evidence pointer:

- **Protocol load and carry-in.** `skill://shokunin`, the canonical `protocol/` files, `skill://swarm`, the lane's
  `SKILL.md`/`PROVINCE.md`/`SCORECARD.md`/`corpus/`; the r66 non-author closure recorded before any claim is
  measured (`LOG.md:4083`; commit `cf705c53`; order receipt `.ufo/waves/round-67/l1/records/r67-order.txt`).
- **Instruments committed before the claims file (QUALITY #33).** `tools/round-67/avm-le-counter.py`,
  `tools/round-67/mutation-battery.py`, `tools/round-67/gap-rule-v2.json`, `tools/round-67/c1-run.sh` and the
  pre-freeze receipts (commit `39a91a99`); freeze `3663e6b2`.
- **Pre-freeze controls.** `.ufo/waves/round-67/l1/pre/control-dryrun.json` (round-50 rule `gaps_ok 2/4`,
  round-67 rule 4/4, both red fixtures true, exit 0), `control-dryrun-c2.json` (0 of 2 mutants killed, exit 0),
  `score-dryrun-at-base.json` (2 killed after, 0 before), `selftest-r50.txt` (169 cases), `selftest-c2.json`
  (10 cases).
- **Data run.** Four carriers fetched through the pinned chain (`tools/round-41/fetch-vendor.py`, cache
  `/fast/scratch/hyaku/kaidoku-r67/carriers`, never committed — AVM licence S249) and one rea-agents 6.5.0
  `extract-firmware --max-depth 1` run each into `corpus/evidence/round-67/c1/<id>/{after.json,run.json}`
  (commits `a4c1d0fc`, `454071dd`).
- **C1 measurement.** `l1/scores/c1-at-landing.json` (rev `83239917`) and `c1-at-record.json` (rev `7a3c21d4`):
  `carriers_matched 4`, `target 4`, `met_target true`, exit 0, `failing []`, `bindings_false []`,
  `carriers_unchanged true`, `gap_rule_unchanged true`, every one of the engine's 23 clauses true on all four
  carriers (including `evidence_id_ok` and `projection_ok`).
- **C2 measurement.** `l1/scores/c2-at-landing.json` (rev `2dd5f2cd`) and `c2-at-record.json` (rev `7a3c21d4`):
  `survived_before 2`, `killed_before 0`, `killed_after 2`, pristine 30/26 cases green, exit 0.
- **Coverage row re-derived at the record.** `l1/scores/coverage-selfcheck-at-record.json`: recipe A equivalent
  true, `recipe_a_hidden 5`, atoms A1 `10.0/10.0`, A2 `[147,147]/[147,147]`, `mismatches 0`, exit 0.
- **Documentation bindings.** `PROVINCE.md` `## Round-67 additions to Core` + frontier note; `corpus/README.md`
  coverage-map row, knowledge-index row, frontier note; entry
  `corpus/knowledge/2026-11-03-r67-avm-le-squashfs-core.md`; `corpus/SOURCES.md` S268; `corpus/QUALITY.md` rows
  107–110 (commit `2dd5f2cd`).
- **One batched v1 wave, 12 seats.** `r67-w1`: 3 executor, 1 reviewer, 1 critic, 2 mutation-testers, 1 sentinel,
  1 scout, 1 connector, 2 scribes; attack seats 4/12 = 33 %; 12/12 settled, 0 dead; per-seat status table
  `l1/records/r67-wave-status.json` (the r66 closure's routed defect 3). Dispatch evidence: `r67-w1.ready` /
  `.ready.dispatched`, `r67-w1-dispatch.json`, `r67-w1-results.json`; seat reports under `w1/`.
- **Wave findings integrated, not ignored.** Sentinel F1 (the rule's `removed.silent` deletion contradicted the
  docstring/atom), F2 (the rule was unpinned), F3 (the predicate's second conjunct unbound), F4 (dangling order
  receipt), F6 (exit-2 contracts); MutCounter M1 (the `carrier_fresh_ok` drop was a no-op with a false reason);
  MutBattery N1–N5 (containment kill test, unasserted inventory, control field swap); CriticClaims F0 (the first
  freeze was dead on arrival); ExecPins F1/F2/F4. Each is either repaired with a disclosed supersession or
  routed in `corpus/lessons/round-67.md` `## Mistakes` (M67-1 … M67-8).
- **Freeze ledger.** The missing `round-64` and `round-66` rows and the `round-67` row appended to
  `corpus/claim-freezes-v2.tsv`; the round-64 row's findings cell normalised to the gate's form (commit
  `451f3102`). The R29 gate at the tip: `exact 42 of 42`, no mismatch/missing/stray, exit 0.
- **Prefile gate (QUALITY #47), run on a clean tree at `451f3102`:**

```
prefile: tree clean
prefile: round-24 gate --disclosures corpus/claim-freezes.tsv at 451f3102c1be3fe476b8c600979eba5ecaade1f8 exit=1
prefile: round-29 gate --disclosures corpus/claim-freezes-v2.tsv at 451f3102c1be3fe476b8c600979eba5ecaade1f8 exit=0
prefile: FAIL
```

  The failure is the **superseded** round-24 ledger (`corpus/claim-freezes.tsv`), which stopped at round 52 and
  carries one stray `round-35` row whose `claims.json` was never committed (the round kept
  `claims-canonical.json`/`claims-frozen.json`). The current ledger (`-v2`) is exact. Disclosed as a conformance
  defect, not repaired by fabricating a round-35 claims file or by deleting a disclosure row; routed as next
  round's item.

## Landed changes

Every row is tied to its LOG entry and the commit that carries it (all in the lane repo, pushed):

| change | LOG entry | commit |
|---|---|---|
| carry-in: the r66 closure recorded | `## 2026-11-03 — round 67, KaidokuR67 — carry-in` | `cf705c53` |
| the two instruments, the rule, the run harness, the pre-freeze receipts, the r64/r66 ledger rows | `landing` (instruments) | `39a91a99` |
| claims frozen: plan + container, seven instrument pins, before-arms | `landing` | `3663e6b2` |
| four carrier `run.json` receipts | `landing` | `a4c1d0fc` |
| four carrier `after.json` envelopes | `landing` | `454071dd` |
| instrument supersessions 1–4 with re-taken before records | `landing` | `1e7fe7b7`, `ecc4de0e`, `7cfe83e4`, `3e7b59db` (+ disclosures `6dcc447e`, `66389549`, `eadc2188`, `83239917`) |
| PROVINCE Core section, README map/index/frontier, S268, the entry, QUALITY 107–110 | `landing` | `2dd5f2cd` |
| A4 correction and the order receipt | `landing` | `4c2c85d3` |
| SCORECARD section + coverage row at 147/147, wave evidence, landing receipts, status table, r66 record-tie correction | `record` (correction entry) | `7a3c21d4` |
| lesson, census end, record receipts, round-67 ledger row | `close` | `8672cf40` |
| round-64 ledger row normalisation | `close` | `451f3102` |

No filed round-66 byte was rewritten; corrections are appended entries (`LOG.md` is additions only).

## Before → after measurements

- **R67-C1 (coverage).** Counting command:
  `python3 -I -B tools/round-67/avm-le-counter.py --score --root <LANE> --rev <REV> --freeze 3663e6b2… --carrier-cache <CACHE> --work <SCRATCH> --out <RECEIPT>`.
  Before: the do-nothing rule control over the four committed envelopes — `gaps_ok_round50 2`, `gaps_ok_round67 4`,
  red fixtures true, exit 0 (`.ufo/waves/round-67/l1/pre/control-dryrun.json`, base `a7a4ce69`). After:
  `carriers_matched 4 of 4`, `met_target true`, exit 0, measured at `83239917` (`l1/scores/c1-at-landing.json`) and
  re-measured at `7a3c21d4` (`l1/scores/c1-at-record.json`). Surface moved: `PROVINCE.md` Frontier → Core and the
  `corpus/README.md` map row (same commit `2dd5f2cd`).
- **R67-C2 (depth).** Counting command:
  `python3 -I -B tools/round-67/mutation-battery.py --score --root <LANE> --rev <REV> --work <SCRATCH> --out <RECEIPT>`.
  Before: the r66 selftests alone on the two mutants — `killed_before 0`, `survived_before 2`
  (`l1/pre/control-dryrun-c2.json`, base `a7a4ce69`). After: `survived_before 2`, `killed_before 0`,
  `killed_after 2`, pristine 30/26 cases green, exit 0, measured at `2dd5f2cd` (`l1/scores/c2-at-landing.json`)
  and `7a3c21d4` (`l1/scores/c2-at-record.json`).
- **Coverage self-assessment (standing duty).** `tools/round-66/coverage-selfcheck.py --selfcheck --rev 7a3c21d4`:
  `mismatches 0`, `recipe_a_equivalent true`, `recipe_a_hidden 5`, exit 0 — the Owned-axes row cites 147/147 at the
  record that changes the population (`l1/scores/coverage-selfcheck-at-record.json`).

## Sources & frontier

- Registry before → after: **174 → 175 rows** (`grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`
  at `a7a4ce69` and at the tip); tier `A=160 B=9 C=5` → `A=161 B=9 C=5`; status `mined=165 rejected=9` →
  `mined=166 rejected=9`; malformed rows 0; the 19 standing W04 warnings unchanged.
- Census command and exits: `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kaidoku`
  exit 0 at round start (`l1/census-start.txt`, 174 rows) and exit 0 at round end (`l1/census-end.txt`, 175 rows).
- Rows added by tier: one, tier **A** — **S268** squashfs-tools-ng `doc/format.adoc` at commit `e3dcf177…`
  (`docs`, scope = the device special file inode layout, anchor = `=== Device Special Files` line 730 / quote
  line 732 / major-minor lines 742-746, opened 2026-11-03, recheck 180d, used-by the round-67 entry).
- Rows touched old→new: S268 added; S243/S244/S245/S249/S250 re-opened (digests match the registry) with no
  `status`/`recheck`/`used-by` change; no row superseded.
- Frontier rows advanced: "LE AVM members (`hsqs`)" moved from Frontier to Core for the four pinned carriers
  (`PROVINCE.md ## Round-67 additions to Core` and the round-67 frontier note; `corpus/README.md` map row and
  frontier note). Still Frontier: LE AVM kernels, LE AVM rootfs under REA's 120 s limit, nested sub-images below
  depth 1, vendor-mangled bodies.
- Gate decisions (for the non-author spot-check): **admit** S268; **reject** the kernel SquashFS page (names the
  device inode class but states no device-number field: `major`/`minor` occurrences 0); **reject** the
  `torvalds/linux.git` plain `.rst` (same scope, no revision identity); **reject** the receipt-as-source. Gate
  evidence: `.ufo/waves/round-67/w1/ScoutSource/{fetch.json,gate.md}`; the lesson's `## Gate` carries the URL,
  access date and the ≤25-word located quote for the admit.
- Assimilation: none — `merge/kaidoku/` has no theme fitting a SquashFS class rule (the jsc theme was adopted in
  round 64) and `considerthese/` is absent (`ls considerthese` exit 2).

## Trend verdicts

- **expansion: improved.** One admitted `corpus/knowledge/` entry on coverage-map ground the lane held only as
  Frontier, its `source:` citing the row opened this round (S268, `mined`), and the frontier→core move recorded in
  PROVINCE and the README map. Evidence: `corpus/SOURCES.md:185`, the entry, `2dd5f2cd`.
- **quality: improved.** Four disclosed instrument repairs closed real defects found by the wave (rule pinning,
  control binding, exact-set mutation kills, case inventory), the two r66 mutation survivors are killed, the two
  r66 counter receipts now carry their revision, and the coverage row is re-derived at the population it cites
  (`mismatches 0`). No admitted entry was found false; the r50 rule's over-generalisation is corrected by a class
  rule with red controls.
- **discernment: improved.** The wave's seats found defects the L1's own freeze missed (F0, F1–F6, M1, N1–N5) and
  every one is either repaired with a disclosed supersession or routed in the lesson's `## Mistakes`; the
  freeze-ledger drift of rounds 53–66 was found by the prefile gate and is disclosed. The outside non-author
  closure has not run; this report does not self-certify.

## SHONEN

- `[~]` SKILL.md contains real decision tables, error patterns, checklists, cited sources — pointer: `SKILL.md`
  instrument registry rows (round-66/67 counters), the `## Queue-drain craft` rule blocks, and this round's
  `tools/round-67/*` + entry; no non-author verifier this round.
- `[~]` At least one end-to-end domain task executed and logged in LOG.md — pointer: the four-carrier REA data run
  and the 4/4 score, `LOG.md` landing/close entries, `corpus/evidence/round-67/c1/`.
- `[~]` Instructions executable by an agent without oral context — pointer: `plans/round-67-claims.md` + the two
  instruments' docstrings and `--control`/`--score` modes reproduce the round's measurements; asserted, not
  exercised by a non-author.
- `[~]` No cross-domain bleed (PROVINCE.md still accurate) — pointer: the round-67 Core section and frontier note;
  the connector found no sibling owner of the device-class rule.

## Round shape, dead seats, tools, stale lane

- Shape: one v1 wave of 12 seats under `ufo-wave-policy.json` (band 8–16), attack share 4/12 = 33 %, one connector
  seat, L1 held the planner seat (the validator rejects a `planner` role). No residual call. Round total: 12 seats.
- Dead seats: none — 12/12 settled, each with a report (`l1/records/r67-wave-status.json`).
- Tools: none installed or upgraded. The npx `rea-agents` 6.5.0 package was re-resolved by a version probe, which
  rewrote the npx cache lock (M67-3, disclosed; the counter re-pins the package and records the substitution).
- Stale-lane: respawn-per-round driver; no other mission of this lane is open.

## Routed to the next round

1. The superseded `corpus/claim-freezes.tsv` (round-24 gate) is stale: 15 missing rows (rounds 53–67) and one stray
   `round-35` row; decide its retirement or backfill with the gate's own verdicts (prefile currently FAILs on it).
2. MutBattery Probe B: a mutant failing a *second* unrelated case still needs a "no extra failures" clause beyond
   exact-set equality.
3. The REA package pin should bind `package.json` plus a tree digest so the lock substitution is unnecessary.
4. ExecPins F1's reading — disclosed supersessions versus the kill rule's "post-freeze instrument edit" — is routed
   to the closure for a ruling; the report states the reading used (an *undisclosed* edit, QUALITY #33).
5. The r63 planned record-section sweep stays open; the r58/r60 bare-name findings and the r64 placeholder-token
   disposition stay named debt.
