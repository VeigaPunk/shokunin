# Kasegi round 65 — signal-fail-closed derive gate (depth:verifiability) and F44, the FIRST PSIRT services catalogue (coverage)

Lane `kasegi` · attempt 1 · base `a283189b6c8d86ee1a06e4aa2b701a2b6c6b068b` · final lane hash `a33573291dd1867eed2c283516fc1ce38b7dae69`
· report commit: the fleet commit carrying this file (`git -C /home/vgpnk/Projects/shokunin log --format=%H -1 -- .ufo/reports/round-65/kasegi.md`) · prompt `.ufo/prompts/kasegi-round-65.md` (814 lines, §1–§7 plus the hyaku
addendum and the run-15 notes).

## Work performed

**Declared claims (2).**

- **C1 — depth:verifiability (lowest non-retired axis, nominal 4 held under QUALITY R58).** The figure-audit
  derive gate treated every negative (signal) upstream status as success: a SIGTERM- or SIGKILL-killed
  producer that leaves output matching the `want` read `ok`. The round makes signal termination fail closed
  with a reason naming the signal, replaces the malformed final-stage label `derive-exit--15` with
  `derive-signal-15`, keeps SIGPIPE (-13) on a non-final stage benign by documented rule, and preserves the
  grep-exit1 and clean-pipeline positives. Frozen: `.ufo/waves/round-65/claims.json` at `57cb8dec1cd3a688b0f8a23f5b6b434656592577`;
  erratum 1 `.ufo/waves/round-65/claims-erratum-1.md` at `a333d8ef7183a9d8bb969c6ec5c29b8db01f7481`.
- **C2 — coverage (8 held).** Frontier F44 admitted on S098, FIRST's PSIRT Services Framework v1.1: the
  receiving team's service catalogue (six service areas, 28 services, 84 functions) with intake, documented
  qualification gates and bug bars fed by CVSS, the established-finder bypass, reproduction as validation in
  an isolated environment, and disclosure audiences. This is the round's **sourced claim** (S098 opened this
  round).

**Work items (evidence pointer per item).**

1. **Protocol load and claim choice.** Read `skill://shokunin`, `skill://swarm`, PROTOCOL, MISSION, AXES,
   CORPUS, LEARNING, the lane SKILL/PROVINCE/SCORECARD, corpus QUALITY/README and the newest lessons; the
   round-64 spot-check is at `corpus/lessons/round-64-verifier-spotcheck.md` (`.ufo/reports/round-64/kasegi.md`
   is its report). Claim choice follows the round-64 plan: one distinct observed gate residual (not the six
   exit1 cases) plus one frontier admission.
2. **Predata wave (one v1 wave, 12 seats).** Spec `.ufo/waves/round-65/w1-spec.json`, validated by
   `ufo-swarm-wave.mjs run` under `ufo-wave-policy.json` (band 8–16) → `w1-dispatch.json`, handoff
   `w1.ready` (L1 `KasegiR65`); the orchestrator spawned all 12 (`w1.ready.dispatched`). Seat roles: 4
   executor, 1 scribe, 1 scout, 1 connector, 2 reviewer, 1 critic, 1 mutation-tester, 1 sentinel = attack
   5/12 (42 %). L1 holds the planner seat (validator forbids a planner lane).
3. **Base residual measured before the freeze.** `controls/do-nothing-signal-base-r65.txt`: the production
   gate prints `FIG p1-sigterm-upstream … derived=0 ok`, `FIG p2-sigkill-upstream … ok`, with native stage
   returncodes `-15`/`-9` printed in the same receipt; `FIG p3-final-signal … reason=derive-exit--15 stale`.
   `controls/ledger-stage-status-r65.txt` shows no current ledger derive carries a signal status (24 git/12
   grep/7 head/3 tr/3 cut/2 tail upstream at rc 0, 2 grep at rc 1), so fail-closed on signals costs no
   ledger figure.
4. **Candidate gate built and falsified by seats.** `w1/ExecSignalGate/figure-audit.py` (sha256
   `86becbde…`, selftest 59→63 cases, ledger 35/35); `w1/ExecSignalProbes/c1-signal-probes.py` six probes
   with native statuses (`probes-base.txt` exit 1 with `PROBES probes=6 failures=1`; `probes-candidate.txt`
   exit 0) and an always-green selfcheck (`failures=6`); `w1/ExecSignalMutants/signal-mutbat.py`
   (`mutbat-base.txt` limb absent, `mutbat-candidate.txt` `killed=4/4 survivors=0 equivalents_held=2
   controls_held=1 invalid_rejected=1`).
5. **Committed-input driver.** `.ufo/waves/round-65/verify-r65.py` enumerates 8 measurements over a scratch
   `--shared` clone (the ledger's `git show` derives need the object database), materialises the probe
   collector, the battery and the candidate from the commits that added them, and guards `--work` with a
   900 s child timeout. Base do-nothing `controls/driver-base-donothing-r65.txt` →
   `VERIFY measurements=8 failures=3`, exit 1; construction `controls/driver-construction-r65.txt` → 8/0;
   final `controls/final-verification-r65.txt` → 8/0 at `1c36d724` and
   `controls/final-verification-tip-r65.txt` → 8/0 exit 0 at the final tip `03a239212633411cf2dbc96beedc672b9c3d0790`.
6. **Counter history, honestly recorded.** Two counter defects were found by the round's own runs and attack
   seats before the final measurement, never after: erratum 1 (the driver read the base gate from the tree
   under test — the first final-mode run printed 8/2, `controls/final-verification-pre-erratum-r65.txt`; base
   revision and pin scope fixed) and erratum 2 (the driver trusted the mutable worktree and left `--work`
   unguarded — fixed by revision-bound inputs, a work guard and a timeout; receipt
   `w1/CriticC1.md` § D2, `w1/SentinelScope.md` S-02/S-03/S-08), and erratum 3 (the driver now verifies its
   own bytes against `.ufo/waves/round-65/driver.sha256`, `GUARD driver-self-pin PASS`, and fails closed when
   the pin is missing). No seat had scored the claim on any amended driver, and every amendment re-ran the
   before/construction/final receipts.
7. **Named residual from the critic: the SIGPIPE exemption can mask an error** (`cat big.txt missing.txt |
   head -n 1` reads green while `cat missing.txt | wc -l` is stale; `w1/CriticC1.md` § H1). The frozen
   predicate keeps the SIGPIPE positive control, so this is reported as a named residual and a round-66
   candidate (single-input-operand restriction), never claimed away.
8. **Partial-output control (r64 routed defect 1).** `controls/partial-output-truncation-r65.txt`: a producer
   that writes one line then dies by SIGKILL makes the base gate print `derived=1 ok` and the landed gate
   print `derive-upstream-signal-9 stale`.
9. **C2 source and entry.** `corpus/source-snapshots/round-65/S098.txt` (1573 lines, 170137 bytes, sha256
   `cfa42e23…b7a3c2`; `fetched_utc` 2026-11-04T19:26:27Z) + `manifest.json` (18 anchored quotes);
   `corpus/knowledge/first-psirt-services-framework.md`; registry row S098; frontier row F44
   (`corpus/README.md` § Round-65 admission); `corpus/instruments/knowledge-expected.txt` 83→84 lines.
   Independent reproducibility: ScoutS098's capture is byte-identical (`w1/ScoutS098/S098.candidate.txt`),
   ReviewC2Base re-fetched twice with identical raw and snapshot digests (`w1/ReviewC2Base/source-check.md`).
10. **Frontier step.** `controls/prefreeze-screen-r65.txt` (extended pre-freeze screen, timestamp
   2026-11-04T19:32:30Z, before the freeze at 19:35Z), with nav-hit adjudication; `w1/ScopeF44/screen.md`
   (C2 UNCOVERED, closest rows F43/F06/F11 with their narrowing sentences; C1 sibling scan); id-collision
   check and its guard proof `.ufo/waves/round-65/assimilation/id-collision-check.txt` (registry 98, staged
   94, collisions 68, all staged ids already adopted; the indented-row fixture proves the 0–3-space guard;
   the column-zero-only pattern reads 0 on the same fixture).
11. **Calibration.** Ten Mistakes rows in `corpus/lessons/round-65.md` § Mistakes (all under that heading);
    QUALITY R84–R91 land with them; the five round-64 lane-routed defects are closed (§ Carry-in). The three
    late rows are the wave's own finds: M65-7 (the SIGPIPE exemption can mask a later operand's error,
    `w1/CriticC1.md` § H1 — named residual, round-66 candidate), M65-8 (driver trust root and work guard,
    erratum 2), M65-9 (the manifest's `body_lines` stopped inside Annex 2 and excluded the glossary —
    `w1/EntryS098/gate.md`; widened to [216,1536] before the final counters) and M65-10 (the L1's own appended
    maturity bullet claimed "no assessment method" while L675 states one; the scribe's post-append audit
    refuted it and the bullet now says "only maturity *definition*" and quotes L675 — R91).
12. **Fresh-clone reproduction (R77).** `controls/fresh-clone-r65.txt`: a `--shared` clone at `2f6017fa`
    re-runs the frozen C1 command (8/0) and the C2 counters (rows 44, registry 98, `FRONTIER-PASS F44`,
    `records=79 bound=79`, 18 Q-OK) with the literal commands.
13. **Wave seat verdicts.** | seat | role | verdict (from the seat's report file) | effect on the round |
|---|---|---|---|
| ExecSignalGate | executor | candidate built; selftest 59→63/0; ledger 35/35; production untouched | candidate adopted byte-identically (`86becbde…`) |
| ExecSignalProbes | executor | base `PROBES probes=6 failures=1` (P1/P2 `ok`, P3 `stale reason=derive-exit--15`); candidate 0; always-green selfcheck 6 | probe set + selfcheck became driver measurements | 
| ExecSignalMutants | executor | base `killed=0/4 limb=absent`; candidate `killed=4/4 survivors=0 equivalents_held=2 controls_held=1 invalid_rejected=1` | driver measurements 4–5 |
| ExecDriver | executor | independent 8-measurement driver, base `failures=6` on its own enumeration | corroborating predata, not the counter (R86) |
| ScoutS098 | scout | capture byte-identical (`cfa42e23…`); 28 anchored quotes; scope screen | Gate and distinguishes |
| EntryS098 | scribe | 73/73 GROUNDED draft entry + gate + 45-quote proposal (not merged: frozen 18) | found M65-9 (body range) and M65-10 (maturity overreach) |
| ScopeF44 | connector | C2 **UNCOVERED**, closest F43/F06/F11; no held signal claim | pre-freeze screen + distinguishment |
| ReviewC1Base | reviewer | **PREMISE HOLDS** (four receipts, base blob) | independent base reproduction |
| CriticC1 | critic | **SURVIVES** on the literal predicate; **DEFEATED** on H1 (SIGPIPE masks a later operand) and D2 (driver trust root) | M65-7, M65-8; errata 2–3 |
| MutationC1 | mutation-tester | 6/6 and 9/9 exact-once mutants killed; a semantic emulator passes the documented probes and dies only on the held-out pair | M65-5 |
| ReviewC2Base | reviewer | base counters reproduce; raw/snapshot digests stable across fetches; `Last-Modified` 2026-01-26 | base receipt + manifest note |
| SentinelScope | sentinel | `FINDINGS critical=0 high=3 medium=5 low=6 info=5`; highs are the inherited configured-program exec path and the driver guard/provenance items | errata 2–3; named residuals |

## Landed changes

Every change below is a LOG.md entry (§ Round 65) and one commit.

| Change | LOG entry | Commit |
|---|---|---|
| Predata controls: wave spec/dispatch/ready, driver and its frozen inputs, base counters, do-nothing receipts, capture receipt, census before, the four inherited `w1.ready.dispatched` markers | LOG bolts 1–3 | `462ed24a7f64744a474101842e1c7e89a71198e4` |
| Frozen claims C1/C2 (predicate, counters, kill rules, residuals) | LOG bolt 2 | `57cb8dec1cd3a688b0f8a23f5b6b434656592577` |
| Signal-fail-closed `corpus/instruments/figure-audit.py` (byte-identical to frozen candidate `86becbde…`), S098 capture+manifest, entry, registry row, frontier F44, expected list | LOG bolts 4, 8 | `1c36d724c91cdd8585219798ea7cf60bb4f24b5b` |
| Counter erratum 1, amended driver, base/construction receipts with that driver | LOG bolt 6 | `a333d8ef7183a9d8bb969c6ec5c29b8db01f7481` |
| Final verification receipt, partial-output control, fresh-clone receipt, lesson, QUALITY R84–R87, SCORECARD, LOG, SKILL registry cells + current-execution amendment, r64 Gate pointer, assimilation receipts | LOG bolts 5, 7, 9–11 | `2f6017fab9d135267bed4bc9f6508a5a0537e71c` |
| Counter erratum 2 (revision-bound inputs, work guard, child timeout), amended driver, base/construction/final receipts re-run | LOG bolt 6 | `155737d0863fc4463998f060b58d1c7510f5f96d` |
| Attack seats' findings as M65-7/M65-8 and criteria R88/R89; tip final-verification receipt | LOG bolts 5, 10 | `55b26e7a273b2fbd2b6171f1d840f6b3e39cb735` |
| Driver self-pin (`driver.sha256`, erratum 3), amended driver, base/construction receipts re-run | LOG bolt 6 | `51951470996a97058c705269144e057fb637dd0b` |
| Maturity Limits bullet, Scope wording, S098 cadence cell, maturity lead, final receipt at the erratum-3 tip | LOG bolts 8–9 | `2cf503986d3cd1261d3405803cc27d447c94726a` |
| Maturity-bullet correction after the scribe's audit (M65-10, R91) | LOG bolt 10 | `308e57286a83b884e5bcd1470eb1c63f7a60de00` |
| Wave evidence (12 seat outputs, `w1-results.json`) | LOG bolt 12 | `90e8f94df3030e30a9adef66fbd77425b4a022e1` |
| Census-after and fresh-clone receipts cited above | LOG bolts 9, 12 | `a33573291dd1867eed2c283516fc1ce38b7dae69` |

## Before → after measurements

**C1 — depth:verifiability.** Metric: driver failures over 8 enumerated measurements.

```
before (a283189, exact final driver):
  python3 -B .ufo/waves/round-65/verify-r65.py --revision a283189b6c8d86ee1a06e4aa2b701a2b6c6b068b --work /fast/scratch/hyaku/kasegi-r65/L1/base-finaldrv2
  → VERIFY measurements=8 failures=3   (exit 1)
after (final tip 03a23921, carrying the gate, the pins, the driver and its self-pin):
  python3 -B .ufo/waves/round-65/verify-r65.py --revision 03a239212633411cf2dbc96beedc672b9c3d0790 --work /fast/scratch/hyaku/kasegi-r65/L1/final-tip --final
  → VERIFY measurements=8 failures=0   (exit 0)
```

Discrimination is inside the same driver: `probes-base` keeps the base gate's false greens (P1 `audit_exit=0`,
P2 `audit_exit=0`), `probes-candidate` reads `derive-upstream-signal-15`, `derive-upstream-signal-9`,
`derive-signal-15`, `mutbat-candidate` is `killed=4/4 survivors=0` while `mutbat-base-limb-absent` is
`killed=0/4 survivors=4 limb=absent`, and `collector-selfcheck` rejects an always-green instrument
(`failures=6`). The real ledger stays `FIGURE-AUDIT figures=35 ok=35 stale=0 exit=0`. Two disclosures: the selftest's `cases=63` is host-conditional under QUALITY R82 (the selftest's helper scripts run through `python3` from PATH while the driver runs the gate with the driver's interpreter), and the sentinel's pre-existing finding stands as a named residual — an unscreened `sort` invocation executed a helper 121900 times while the audit read `ok` (`w1/SentinelScope/07-parser-sort-compress-exec.txt`), which is the already-documented unscreened-flag class, not something this round claims to fix.

**C2 — coverage.** Metric: admitted frontier rows plus the binding counters.

```
python3 corpus/instruments/frontier-recheck-count.py
  before: FRONTIER-CENSUS rows=43 admitted=43 closed=43 problem-rows=0 registry=97; entries=46 pass=46
  after:  FRONTIER-CENSUS rows=44 admitted=44 closed=44 problem-rows=0 registry=98; FRONTIER-PASS F44 ids=S098; entries=47 pass=47
python3 corpus/instruments/capture-binding-check.py
  before: records=78 bound=78 unbound=0        after: records=79 bound=79 unbound=0
python3 corpus/instruments/source-recheck.py --manifest corpus/source-snapshots/round-65/manifest.json --source S098
  after: 18 × "OK occurrences=1" (anchors L1…L1231), exit 0
knowledge: 81 → 82 files; knowledge-expected.txt 83 → 84 lines, LC_ALL=C sort -c exit 0
```

Before numbers: `controls/base-counters-r65.txt`; after: the same commands re-run at `2f6017fa`
(`controls/fresh-clone-r65.txt`).

## Sources & frontier

**SOURCES.md rows: 97 → 98** (`grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`
before 97, after 98). Rows added by tier: **A +1 (S098), B +0, C +0**. Rows touched old→new: **one cell**, S098's own
recheck cadence `90d` → `180d` (logged; the page carries no publication date, its HTTP `Last-Modified` is
2026-01-26 and its prose is mutable), plus a **lead** added (FIRST's separate PSIRT Maturity document, opened
only for boundary screening, HTTP 200, sha256 `334aeb01…`, not admitted). No pre-existing row changed: the
base→tip diff of `corpus/SOURCES.md` adds the S098 row, the cadence-correction bullet and the lead line, and
deletes nothing. Registry-changes bullet: "Round-65 S098 added
… Registry 97 rows pre-append -> 98 post-append (R8); no pre-existing status, recheck, used-by, id or URL
cell changed."

**Frontier rows advanced:** F43 → **F44 admitted** (FIRST PSIRT Services Framework v1.1, S098,
`knowledge/first-psirt-services-framework.md`). The README section names the distinguishment from F43,
F06/S018, S043/S044 and S053/S054; the one genuinely new surface is the receiving team's service catalogue
with its intake/qualification/reproduction gates. Unopened leads unchanged: the Fuzzilli primary docs and
the OpenSSF aggregate-score/API portion.

**Census before → after** (same command both times, `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh
validate --root /home/vgpnk/Projects/shokunin kasegi`):

```
before (controls/census-before-r65.txt): 6 × W04 duplicate-URL-across-scopes warnings (S028, S029, S072,
                                          S076, S080, S085 — all pre-existing) then "kasegi ok …/corpus/SOURCES.md", exit 0
after  (controls/census-after-r65.txt):  the same 6 W04 warnings, "kasegi ok …/corpus/SOURCES.md", exit 0
```

**Assimilation: none.** `merge/kasegi/MERGE-REPORT.md` read; no package entry adopted (the round's two
claim slots are the gate and F44; the package's unadopted surface is doctrine/duplicate of held rows).
`considerthese/2026-10-26.md` proposal 2 remains domain-task-open; proposals 1 and 3 stay landed. The
campaign register's 7-row kasegi slice was hand-checked in rounds 24 and 26 and is not re-adopted here;
this round re-derived the slice and the id-collision state
(`.ufo/waves/round-65/assimilation/id-collision-check.txt`).

## Trend verdicts

- **Expansion — improved.** F44 admits a new source kind on ground the lane did not hold: the receiving
  team's service catalogue (six service areas, 28 services, 84 functions) with the intake/qualification/
  reproduction gates (capture `corpus/source-snapshots/round-65/S098.txt`, entry
  `corpus/knowledge/first-psirt-services-framework.md`, census above).
- **Quality — unchanged.** No admitted entry was superseded, or found false and left unmarked; QUALITY.md
  gained only the four criteria R84–R87, no existing criterion changed; the gate change is an instrument
  improvement, not corpus quality. `recheck-audit.py` still reports `entries=47 pass=47` with the known
  `22/82` lost-base-gated lines and `cwd_fail=9` (pre-existing, named).
- **Discernment — improved.** The wave's independent seats disagreed in writing where the spec was wrong:
  the probe seat's base receipt refuted the spec's P3 claim (M65-1), the mutation seat showed the documented
  probe set cannot reject a semantic emulator (M65-5), and the reviewer reproduced the base premise
  independently (`w1/ReviewC1Base.md`, PREMISE HOLDS). Two counter defects were caught by the round's own
  final-mode run and turned into erratum 1 before any final measurement (M65-2, M65-3).

## SHONEN

`grep -c '^## SHONEN' <report>` = 1; one line per box of `SHONEN.md`:

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — SKILL.md registry
      row updated with the signal rule and selftest 63; outside promotion verification remains required.
- [ ] At least one end-to-end domain task executed and logged in LOG.md — untouched this round; the source
      roots are absent and live-target testing stays refused (box stays open, as in rounds 59–64).
- [~] Instructions executable by an agent without oral context — the frozen commands re-run literally in a
      fresh clone (`controls/fresh-clone-r65.txt`); an agent can reproduce both claims with two commands.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — the connector recorded no sibling conflict for
      F44 and scope is unchanged; the C1 gate is lane-local tooling.

**Stale-lane:** respawn-per-round driver; no other kasegi mission is open.

**Round shape:** ONE v1 wave, 12 seats (8–16 band), 5 attack seats (42 %), 1 connector, L1 planner; no
residual `task` call. Round total 12 seats. Dead seats: none — all 12 settled; `w1-results.json` retains no seat output (one shared note: the orchestrator kernel restarted mid-wave), so every verdict above is read from the seat's own report file in `w1/`. Seat-model routes: not asserted (the
artifacts carry no route field; the run-15 route map defers to `task.agentModelOverrides`).

**Tool installs:** none (no install or upgrade was needed; pacman stayed paused).
