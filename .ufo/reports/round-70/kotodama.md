# kotodama — round 70 (hyaku run 6, attempt 1)

Lane repo `/home/vgpnk/Projects/shokunin/kotodama-shokunin` · branch `main`
Base `21e6a7f3fb63e717f2021c46a172e396c4759a7c` · declaration `6cb51a447043a9691c59794d7479c1a81c0626a4` ·
data lands `acc2d614a097484d8dc41230229dc4ead07d8a19` · records `453676a2363c97e158cb112c9588906564d95a21`,
all remote-verified by the lane helper; lane tip at report time `453676a2363c97e158cb112c9588906564d95a21`,
`ahead=0 behind=0`, worktree clean.

Round 69 closed rejected (car stop: operability and depth improved, but the Ca2 kill rule fired).
Its verifier spot-check routed defects D1..D10 to this round; the lane also stood self-routed items
(R69-M8..M12). This round repairs every routed defect and sizes its claims so a do-nothing control
cannot reach any target and no frozen byte must be rewritten to reach any after-state.

## Work performed

Declared claims (frozen in `reports/round-70/claims.json` at `6cb51a4`):

1. **O — operability, counter repairs** (routed D7/D8 + R69-M11): `SKILL.md` `## Gates and probes`
   gains one registry row per reports/round-*/accept-*.py counter (36 counters enumerated by
   `find reports -name 'accept-*.py'`), and `reports/round-69/accept-d.py --selftest` exits 0 with
   `SELFTEST: 2/2`.
2. **Ca — calibration, records** (routed D1..D6, D9, D10): a committed dispositions table
   `reports/round-70/corrections-r69.md` carries exactly one row per defect id D1..D10, and
   `SCORECARD.md` gains an appended correction row marking round-69 calibration unprovable / claim
   failed as declared.
3. **D — depth, instrument hardening** (routed R69-M4/M5/M6, sourced): `tools/check-supersession-settlement.py`
   gains multi-path used-by counting (missing_paths counts unique files), malformed-row diagnostics
   (`MALFORMED-ROW`), and a malformed-target guard; proven by selftest cases `missing-unique-file`,
   `malformed-rows-report`, `malformed-target-no-crash`.

- Repaired D1: the two inherited round-69 w2-verify seat reports (`CritDepth.md`, `RevRerun.md`)
  were committed in the declaration `6cb51a4` (named there), not left uncommitted.
- Repaired D2: Landed-changes attributions corrected — `tools/check-settlement-fixture.py` first
  commit `6a98d7d`, `reports/round-69/corrections-r68.md` first commit `e86ed3e` (evidence in
  `dispositions`; the round-69 report bytes are not rewritten).
- Repaired D3: claims.json wording corrected — frozen predicate/kill-rule/target/counting-command
  fields are byte-identical at `6a98d7d`, `52b92a6`, `ef75509`; wave metadata and `counter_revisions`
  were appended at `52b92a6` (`RevengerWording` facts reproduced in the L1 review).
- Repaired D4: SCORECARD round-70 corrections section appends the row marking round-69 calibration
  unprovable / `FAILED AS DECLARED` (the `improved` row at :1331 is superseded).
- Repaired D5: the attempt-2 block sentence is reworded in place (SCORECARD.md:1353-1357) to
  disclose the one in-place exception — the ScoutAdj pointer repair recorded in the round-69
  corrections table.
- Repaired D6: the misroot sweep sentence excludes driver state (`.ufo/state/*.report-baseline`);
  used in this report and in the LOG entry.
- Repaired D7: 36 registry rows added to `SKILL.md` (lines 662-697), one per counter file; the
  registry row count equals the enumerated file count (36).
- Repaired D8: `accept-d.py --selftest` fixed (R69-M11) — the do-nothing fixture is seeded from
  the committed pre-table blob `793f797:SKILL.md`; selftest exits 0 with `DO-NOTHING FIXTURE: FAIL
  (as required)`, `SELFTEST: 2/2`; the data predicate stays `ACCEPT-D-69: PASS legs=8/8`.
- Repaired D9: guard-proof `note.txt` pointer fixed (R69-M10 → R69-M13) and the S859 collision
  re-proven at the 783-row registry (`.ufo/waves/round-70/assimilation/collisions`).
- Repaired D10: O2's current measurement linked — `reports/round-69/telemetry/final-measures-o-attempt2.txt`
  (stamped `975e8f2`), appended in the SCORECARD corrections.

## Landed changes

| change | LOG entry | commit |
|---|---|---|
| SKILL.md gates registry: 36 accept-counter rows | `LOG.md:4251` round-70 entry, bullet "Claim O" | `acc2d614` |
| `reports/round-69/accept-d.py` selftest fix (R69-M11) | `LOG.md:4251` bullet "Claim O" | `acc2d614` |
| `reports/round-70/corrections-r69.md` dispositions table (D1..D10) | `LOG.md:4251` bullet "Claim Ca" | `acc2d614` |
| `SCORECARD.md`: round-70 corrections section + D5 reword | `LOG.md:4251` bullets "Claim Ca" | `acc2d614` |
| `tools/check-supersession-settlement.py` hardening (D claim) | `LOG.md:4251` bullet "Claim D" | `acc2d614` |
| registry row S860 (own-work, tier A, mined) | `LOG.md:4251` bullet "Frontier step" | `acc2d614` |
| `corpus/lessons/round-70.md` (Gate S860, Mistakes R70-M1..M4, Corrections, Quarantine) | `LOG.md:4251` bullet "Frontier step" | `acc2d614` |
| `.ufo/waves/round-70/assimilation/` guard re-proof + D9 note pointer fix | `LOG.md:4251` bullet "Item 10" | `acc2d614` |
| telemetry receipts: census-start/end, controls-{o,ca,d}, measures-{o,ca,d} | `LOG.md:4251` bullets | `6cb51a4`, `acc2d614` |
| `LOG.md` round-70 entry | itself | `453676a2` |

## Before → after measurements

| claim | counting command | before | after | measured at |
|---|---|---|---|---|
| O | `grep -cE '^\| [^|]+\| (gate\|probe) \| .*reports/round-[0-9]+/accept-[a-z]+\.py' SKILL.md`; `python3 -B reports/round-69/accept-d.py --selftest` | 0 rows; selftest exit 1, SELFTEST 1/2 (DO-NOTHING PASS unexpected) | row_count=36 == file_count=36; selftest exit 0, `DO-NOTHING FIXTURE: FAIL (as required)`, SELFTEST 2/2 | `acc2d614` (`reports/round-70/telemetry/measures-o.txt`) |
| Ca | `awk -F'|' '/^\| D(10|[1-9]) \|/ {gsub(/[[:space:]]/,"",$2); print $2}' reports/round-70/corrections-r69.md | sort -u | wc -l`; `grep -c 'round-69 calibration' SCORECARD.md` | file absent (0); 0 | unique_ids=10, dup_ids=0; scorecard correction line present (1) | `acc2d614` (`reports/round-70/telemetry/measures-ca.txt`) |
| D | `python3 -B tools/check-supersession-settlement.py --selftest`; `python3 -B reports/round-69/accept-o.py --root .` | SELFTEST 7/7, exit 0; ACCEPT-O-69 PASS 7/7 | SELFTEST 10/10, exit 0 (three new cases PASS); ACCEPT-O-69 PASS 7/7, exit 0 (regression) | `acc2d614` (`reports/round-70/telemetry/measures-d.txt`) |

Pre-data do-nothing control receipts (committed at the declaration, `6cb51a4`): a control that
skips the work cannot reach any target — O's grep stays 0 and accept-d selftest stays exit 1,
Ca's dispositions file is absent (unique_ids 0), D's selftest stays 7/7
(`reports/round-70/telemetry/controls-{o,ca,d}.txt`).

Claim verdicts: **O verified**, **Ca verified**, **D verified**, all on their frozen predicates at
the measured revision. Round admission per the claim cap: every claim verifies — admitted as
declared subject to the non-author closure and the operator rule.

## Sources & frontier

`corpus/SOURCES.md` rows, counting command
`grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}' corpus/SOURCES.md`:

- before **783**, after **784**; rows added by tier: **A 1** (S860, kind `own-work`, status
  `mined`, opened 2026-10-25); rows touched old→new: **none** (append-only; no existing row's
  status, recheck or `used-by` changed).
- frontier rows advanced: S860 only; no `corpus/knowledge` entry was added, so no frontier→core
  move is claimed (this round is repair-first; the depth surface is the hardened tool).
- census: exit 0 at start (`reports/round-70/telemetry/census-start.txt`) and exit 0 at end
  (`census-end.txt`), `W04` stable at 28.
- Frontier step records: `corpus/lessons/round-70.md` `## Gate` (S860, access date 2026-10-25,
  a 25-word located quote at `tools/check-supersession-settlement.py:20-21`), `## Mistakes`
  (R70-M1..R70-M4), `## Corrections (round 69)`, `## Quarantine`.
- **Assimilation: none** — adoption CLOSED. The id-collision guard is re-proven at 783 rows:
  reg-ids 783, staged-ids 123, collisions = S859 (the lane's own settlement row vs the package's
  first staged id), recorded in `.ufo/waves/round-70/assimilation/`. Quarantine slice verdicts
  from rounds 68/69 stand.
- `considerthese/` is absent for this lane (recorded, not invented).

## Trend verdicts

- **expansion — improved.** Registry 783→784 rows (S860, tier A, mined, `used-by`
  `SKILL.md` and `corpus/lessons/round-70.md`). Small and bounded; no knowledge entry, so coverage
  is not claimed.
- **quality — improved.** The checker's three routed gaps (malformed-row swallow, per-pair
  missing_paths, no multi-path fixture) are closed and proven by new selftest cases (10/10); the
  gate registry now documents all 36 round counters; the accept-d selftest is green and
  reproducible. No ceiling hidden: the count instrumentation gaps beyond this round (R69-M8..M10)
  are recorded as non-goals.
- **discernment — improved.** The round repaired the round-69 closure's own record defects (D1..D10
  each with a committed landing), marked round-69 calibration unprovable instead of prettifying it,
  and re-proven the item-10 collision. Four new mistake classes are mined (R70-M1..M4).

## SHONEN

- [~] **SKILL.md real decision tables, error patterns, checklists, cited sources** — `SKILL.md:662-697`
  (gates registry, 36 counter rows added this round), `:468` (`### Registry correction chains`),
  `:505` (`## Error patterns`); sources in `corpus/SOURCES.md` (784 rows; census exit 0 at
  `acc2d614`); no non-author verifier on record (the round landed as L1 work after six validated
  wave-dispatch refusals, below).
- [~] **At least one end-to-end domain task executed and logged** — the three claims' end-to-end
  counter runs and receipts (`reports/round-70/telemetry/measures-{o,ca,d}.txt`, `LOG.md:4251`);
  no non-author verifier on record.
- [~] **Instructions executable by an agent without oral context** — the wave spec, registry and
  rendered dispatch payload are committed at `.ufo/waves/round-70/`; every command in the receipts
  is absolute and re-runnable; no non-author verifier on record.
- [~] **No cross-domain bleed** — the repairs stayed inside the lane's own surfaces (SKILL.md
  gates, the settlement checker, records); the connector duty found no sibling owner of any touched
  surface; no canon/lore decision handed out; no non-author verifier on record.

## Round shape, misses and routed work

- Shape: the wave-1 spec (33 seats, 11 attack roles) was validated (`ufo-swarm-wave.mjs plan`: 33
  spawn lanes, one dispatch call) and its dispatch payload rendered, but **the dispatch was refused
  six times by `Background job limit reached (100)`** — the shared session's 100-job cap was
  saturated by sibling lanes, and no job of this lane had settled, so the resend trigger never
  fired. Under the capacity rule's fallback the round was landed by the L1 directly with verifiable
  work; each refusal text is reported (first error text: `Background job limit reached (100).
  Wait for running jobs to finish or cancel one.`). Round total: 33 planned wave seats (not
  dispatched) + L1 integration.
- Dead seats: none (no wave ran).
- Inherited state: the two w2-verify seat reports committed at the declaration (D1); nothing
  discarded. No misroot: `git -C /home/vgpnk/Projects/shokunin status --porcelain` lists no
  untracked file naming kotodama or round 70 (the modified fleet-root files are driver-state
  baselines, excluded per D6).
- `corpus/lessons/round-69-verifier-spotcheck.md` was honoured as the round's repair brief: D1..D10
  dispositions are in `reports/round-70/corrections-r69.md`; standing self-routed items
  (R69-M8..M12) are recorded as non-goals in `claims.json` except R69-M11 (fixed, claim O).
- Routed forward, declared and not fixed here: NEGPROBE differential cross-check, STAMP anchoring to
  the receipt header (R69-M8..M10), and the S859 package-collision renumbering at adoption.
- Tool installs: **none** (no pacman — host paused — and no uv/npx install was needed).
- Stale-lane: respawn-per-round driver; no other mission of this lane is open.
