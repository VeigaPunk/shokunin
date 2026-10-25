# exec-gate-standard — draft text for PROTOCOL.md §Gate standard (L1 applies; this seat does not)

Seat: executor, round 12. Answers the gate questions filed by **kengaku r10** ("Promote the gate
convention … to a fleet-wide standard") and **kumitate r10** ("Should the fleet adopt round-gate.mjs at
the driver level?"). Cited by lane+round, never by line number; every figure carries its command, run
this session from `/home/vgpnk/projects/shokunin`.

## Candidate text

```markdown
## Gate standard

A **gate** is a committed, re-runnable verdict script a lane owns: it reads surfaces, compares them
against in-repo expected values, and returns a verdict. A tool that cannot fail is a **probe**.

- **Verdict.** `0` = `clean`, `1` = `failed` fleet-wide; every other code (`2`, `3`, `64`, …) is
  declared in the registry entry and mapped onto `clean | failed | could-not-evaluate`, an
  undeclared nonzero code reading as `could-not-evaluate`. Nothing else is pinned: a gate's own
  vocabulary — WARN vs HIT, a missing baseline, finding kinds — stays lane-owned, and this section
  governs the outer interface only.
- **Self-test.** Every gate exposes a self-invocation mode over isolated fixtures (temp trees, no
  network, no live-tree write) asserting both the exit code and a stable expected finding-id, with
  expected values committed in the owning repo and independent of the recomputation. The flag
  spelling is the lane's (`--selftest`, `--self-test`, `run_selftest()`); the registry records it.
  A helper-only self-check does not satisfy this clause.
- **Two evidences.** Self-test green is capability, not a measurement (§Evidence standard). A gate
  whose verdict depends on a mutable fleet artifact also ships a fixture run over a committed input
  snapshot with its committed expected verdict — the self-test may be that run; closure reads both.
  Expected values live in-repo per §Evidence standard, "Drift pins".
- **Registry.** The schema is this section's; the rows live in each lane's `SKILL.md`: name,
  `gate|probe`, entry command, verdict map (code → class), self-test command + spelling,
  pinned-value path, write scope, owner. The aggregator ledger stays the routed-defect queue, not a
  second inventory; a fleet index is pointers to lane rows, never copied expected values.
- **Scope.** Read-only over surfaces it does not own; never acts on an external surface —
  publishing, vault approval, claim submission, driver mutation stay operator-owned (§Invariants,
  local-first). A verdict is lane-local evidence: it never defines the host runtime's loop-stop
  conditions (`loop_stop`/`mission_goal`) or stands in for the native judge — host doctrine.
- **Closure consequence.** A red gate is a conformance defect recorded in the round notes and
  routed — status-neutral unless the round's rules already prescribe `failed` (closure step 1). The
  integrator verifies the gate's *committed evidence*; it does not execute a sibling's gate.
```

## Placement

- Insert as a new top-level `## Gate standard` immediately above `## File contract per shokunin repo`
  (line **319**, `grep -n '^## ' PROTOCOL.md`), i.e. after §Evidence standard's last bullet ("Drift
  pins", 313–317) — one blank line above the heading (318 is blank), one after the last bullet. The
  section's only cross-reference is one heading away and §File contract's `SHONEN.md` seed is untouched.
- Live anchors: `wc -l PROTOCOL.md` → **446**; `wc -c` → **39718**; `git status --short PROTOCOL.md
  MANIFEST.json` → empty at HEAD `46e9ec3`.
- Cost (this file's fence, `awk … | wc -lc`): block **30 lines / 2504 bytes** → `PROTOCOL.md` **477
  lines / 42223 bytes** (+1 line/byte = the blank separator). P4's metric is `wc -l`: 446 → 477 = **+31 (+7.0%)**.
- Incident detail → §Appendix, **3 new dated rows** (+3 lines → 480; ~+700 B), in the
  | Rule | Round | Incident | Pointer | shape:
  `| Gate standard | 10 | 14 committed verdict scripts in the six child lanes (corpus/evidence/** helpers excluded, git ls-files): 13 declare a 0/1 map; reserved codes in 5 — kotoba 3 no-baseline (2 scripts), kumitate 64 usage (3); kake scripts/probe-delta.mjs self-declares "a report, not a gate" | l0 kengaku r10; r12 |`
  `| Gate standard | 10 | kagi corpus/transcript-scan.sh:72-77 HIT/WARN tiers and kotoba's no-baseline code are lane vocabulary the standard must not flatten | r10/kagi; r12 |`
  `| Gate standard | 12 | three gates red at the round-12 reading, none attributable to a closed lane-round: kengaku's worktree grades in-flight r11 evidence (CHECKS n=280 mismatches=1) while its cited commit passes (n=149); kagi transcript-scan HITS=2 and kotoba 25/27 checks pass are host-coupled | r12 |`
- Optional: append to the §File contract `SKILL.md` row (line **323**) `` `SKILL.md` also carries the gate registry (§Gate standard) `` — not required; the section is self-contained.

## Interactions

| Existing clause | Line(s) | New text's effect |
|---|---|---|
| §Evidence standard, "Drift pins": "a pin only counts if its expected values are **persisted inside the repo** … Recommended where the surface drifts outside lane control"; and "A status command printing configured values is not evidence of capability" | 313–317; 293–294 | **Pointer, no duplicate.** One clause names the pin rule; the second grounds "Two evidences" (a green self-test is capability, not a measurement). Record one modality change in the round notes: for gates the pin goes from "Recommended where …" to required. |
| Marker vs report, and closure step 1: "…is a marker, not a report: the integrator records that lane-round `failed`"; "…recorded as a conformance defect in the round notes — this does not change the lane's status unless the round's rules already prescribe `failed`." | 146–155; 178–186 | **Consistent refinement, one sentence duplicated by design.** The marker clause is exactly the "round rule that already prescribes `failed`" the Closure-consequence bullet defers to; the step-1 sentence is restated in nine words so the ruling reads without a jump — the L1 may collapse it to "(closure step 1)". The new closure duty adds a step-1 sub-check without editing step 1: keep 178–186 untouched. |
| `rounds[]` status semantics: "where `<status>` is `ok \| failed \| not-dispatched \| in-flight`" | 204–206, 209–212, 233–241, 244–249, 250–255, 256–262 | **Different axis — say so.** A gate verdict class `failed` ≠ a lane-round status `failed`: one lives in a registry row, the other in `rounds[].lanes`. No new status token; 204–262 unchanged. |
| §Invariants: "`MISSION.md`, `AXES.md`, and `scripts/` are operator-side integrator files"; "Lanes write only inside their own child repo and their lane report"; "**domain-facing actions are operator-owned**" | 357–358, 363–364, 375–381 | **Cross-reference only.** Gates and registries live in child repos = lane write scope; the Scope bullet quotes local-first instead of widening it. `scripts/` stays untouched. |
| `CORPUS.md` §Layout/§Rules (ledger reviews corpora, files gaps as lessons); `ROADMAP.md` §Phase gates (round-robin development, protocol aggregation) | CORPUS.md:7–21; ROADMAP.md:17–29 | **No duplication, no second inventory.** The ledger is the routed-defect queue and a corpus reviewer; the registry is a schema here with rows in lane `SKILL.md`. ROADMAP owns lifecycle phases, and protocol aggregation already owns closure — this adds no phase. Also a pointer only for the `SHONEN` heading rule (136–142) and §Promotion gates (29–54): the registry just names `SKILL.md` as the surface the promotion gate already reads. |
| Appendix, kumitate `report_of()` defect | — | **Brief premise falsified:** `grep -n report_of PROTOCOL.md` → line **147 only** (body); the Appendix names the marker *incident* (rows 427–428), not the function. |
| Question-queue citation in `SCORECARD.md` | SCORECARD.md:57 | **Stale citation, flag it.** It cites "`.ufo/l0-questions.md` line 6" for kengaku's question; the live file has kengaku on line **7**, kumitate on **8** (driver appends shift lines) — hence lane+round citation. "both still UNCOMMITTED" is falsified too: `git status --short .ufo/l0-questions.md` → empty; last touch `46e9ec3` (HEAD). |

## Enforcement at closure — measured

The integrator verifies the gate's **committed evidence**, because a fresh run is not the measurement.
Settling measurement: kengaku's gate grades the tree it runs against — worktree (in-flight r11
evidence, `?? corpus/evidence/round11-fleet/`) → `CHECKS n=280 mismatches=1 VERDICT: FAIL` exit 1; the
same gate over the cited commit, read-only (`T=$(mktemp -d); git -C kengaku-shokunin archive HEAD |
tar -x -C "$T"; (cd "$T" && python3 grader.py)`) → `CHECKS n=149 mismatches=0 … VERDICT: PASS` exit 0,
`06cdc98`. Hermetic self-tests are portable — run as a non-owner from the main repo, all exit 0:
`drift-pins.sh --selftest` → `DRIFT_SELFTEST: PASS (13 cases)`; `transcript-scan.sh --selftest` →
`SELFTEST OK …`; `grader.py --selftest` → `[selftest] ALL PASS`, each case asserting its check-id
(`r8.replay.A-INC.ok`, `r8.summary.A-INC`, `r9.replay.A-MONO.got`); `verify_harness_claims.py
--self-test` → `0 failure(s) over 10 assertions`; `round-gate.mjs --selftest` →
`ROUND_GATE_SELFTEST: 57/57 pass`. Total ≈ **8.4 s**, which is why the standard can require the tally
as an artifact rather than as integrator work.

Dependencies confirm why the integrator cannot own the verdict: `node --version` v24.19.0 (gate needs
≥20); `python3 --version` 3.14.7 (stdlib only for `grader.py`); `sqlite3 --version` 3.53.4; kotoba's gate
reads `~/.local/bin/omp`, `~/.opencode/bin/opencode`, `~/.omp/agent/skill-descriptions.db` and the
opencode log; kagi's read `~/.config/the-janitor` and the live opencode DB. Those are lane write scope,
so a closure-time red there is a routed finding, never a lane-round status — and this session's
default-mode runs were red on exactly that class: `TRANSCRIPT_SCAN: HITS=2` exit 1; kotoba `25/27 checks
pass` (`DRIFT omp.db.rows observed=18 expected=17`) exit 1; versus `DRIFT_PINS: CLEAN (files=15
symbols=20)` and `ROUND_GATE: CLEAN (round=10 lane=kumitate checks=10 errors=0 warnings=0)` green.

**Kumitate question — ruled (a)+(b), not (c).** `round-gate.mjs` stays lane-local and reusable, and any
lane MAY run it in its own ritual (`--lane/--repo/--main-repo` parameterize it; 57/57 selftest); porting
its findings into `report_of()`/driver closure is operator-side work, named exactly at
**`scripts/shokunin-watchdog.sh:44`** — `report_of() { [ -f "$SK/.ufo/reports/round-$2/$1.md" ]; }`, the
file-existence completion signal — and the protocol lane does not patch `scripts/` (§Invariants 357–358).
Not a rejection of the defect: it is already filed in protocol r10's question, and the marker clause
(146–155) supplies the retroactive consequence. Routed item found while reading it: `round-gate.mjs`'s
header cites `PROTOCOL.md:263-267` for the integrator's step — now §Round-robin's aggregator paragraph
after the round-11 compaction (step 1 is 178–186) → route to kumitate as a stale citation.

## Rejection alternative

Record a reasoned rejection instead: (1) the divergence is narrow — 13 of 14 committed verdict scripts
already declare 0/1, and the outliers are reserved high codes no runner compares across gates; (2) the
binding constraint is actuator debt, not convention — the prompt template carries 1 of 5 contract items
(M7) and `report_of()` is content-blind, so a new section reaches only lanes that re-read `PROTOCOL.md`;
(3) it extends protocol scope over child-repo tooling, which §Invariants treats as lane-owned; (4) it
costs 31 tracked lines for a norm those 13 scripts satisfy already. Counterweight: without a written
standard the integrator cannot tell a defect from a convention difference — kengaku's self-test asserts
check-ids, kotoba's asserts only its model, and that difference in *kind* is invisible today.

## Gaps

- `loop_stop`/`mission_goal` came from the binding ruling; I confirmed the tokens appear in
  `kumitate-shokunin/corpus/knowledge/native-judge-pipeline.md:103-117` and `failure-telemetry.md:44`
  (`grep -n`) but did not re-read the host's doctrine file (outside this repo).
- `.ufo/waves/round-12/closure-check.py` does **not** exist (`ls .ufo/waves/round-12/` → 8 `.md` files), so
  the `--frozen` instance the ruling anticipates is another seat's artifact; verify before citing it.
- kengaku's `grader.py` is being edited in flight (`git status --short` → ` M grader.py`; a line that
  resolved earlier no longer does) — cite by symbol (`run_selftest()`) and commit `06cdc98`.
- kotoba's `--self-test` is model-only (`help="check the script's model only"`) — the one named
  non-conformance under the new self-test clause; route to kotoba, do not fix it in the standard.
- The "13 of 14 declare 0/1" figure rests on per-file header reads (`grep`), spot-checked by running four
  gates; I did not execute all 14. `kagi corpus/op-ref-probe.sh` is untracked (`git ls-files … | wc -l` → 0).
- `kumitate round-gate.mjs`'s audit defaulted to `round=10` while kumitate's counter is 11; I did not read
  the default's derivation (`opts.round ?? null`), and the header documents no default round.