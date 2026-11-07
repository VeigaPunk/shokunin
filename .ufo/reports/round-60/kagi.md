# kagi — round 60 (secrets & vault ops)

Lane: kagi. Round 60, attempt 1. Claim BASE `a677c78ece8e3d3b4a43dda55254f2a7b33cc1d2`
(round-59 verifier spot-check tip). Predeclaration `cd631737` (frozen plan
`plans/round-60.md`, §Amendments A1–A6, every amendment landed before the recorded
candidate reading). Lane HEAD at filing: `818d2a82fcc568a95db5207c256597cb7d181dc5`
(`git ls-remote origin refs/heads/master` prints it). Axes at BASE: all six at 9.

Round shape: ONE v1 wave, **16 seats** (`.ufo/waves/round-60/w1-dispatch.json`, band 8–16;
`ufo-swarm-wave.mjs run` rc 0, `counts spawn=16 resume=0 total=16`), attack share 4/16 =
25 % on the addendum's literal list (reviewer, critic, mutation-tester, labrat — no labrat
exists; the validator refuses the role) and 6/16 = 38 % counting sentinel and revenger.
Residual calls: none. Round total: 16 seats.

## Work performed

Declared claims (two, distinct axes, each with its own before→after):

- **C1 (calibration)** — the seven round-59 spot-check routed record defects (D1–D7) are
  resolved and re-checkable; `C1_ROUTED` 7 → 0 over population 7.
- **C2 (operability, capability acquisition)** — an executed OpenBao **AppRole
  `secret_id` custody** trial with its own fixture-driven `--selftest`;
  `C2_APPROLE_TRIAL` 0 → 5.

Work items:

- **Predeclaration and shape.** `plans/round-60.md` committed alone at `cd631737`; A1/A2
  the seat count (15 → 16, six disjoint executable write sets), A3 the measured AppRole
  setup preconditions (mount, JSON content type, `{}` on secret-id creation, the measured
  refusal texts), A4 the frozen T1 text reachable unamended, A5 six item defects found by
  the attack seats, A6 the scope receipt's `ADJACENCY_SCOPE:` token.
- **C1 instrument.** `plans/round-60-c1-check.py` (46-case `--selftest`) and
  `plans/round-60-c1.sh` (driver: `git archive` of the revision or `--tree DIR`, a
  challenge copy outside the measured tree, symlink refusal). Seven items, every compared
  number derived from a named revision or the measured tree.
- **C1 record repairs (append-only).** I1 `LOG.md` `## Round 59 — correction`
  (`results=14 dead seats=0`, derived from `w1-results.json`); I2
  `corpus/lessons/round-59.md` `supersedes R31` naming the receipt's 33 cases; I4
  `SCORECARD.md` `supersedes SCORECARD.md:1971` stating 20 controls; I5 the three re-taken
  gate receipts and the `supersedes the round-59 gate-evidence pointer` line; I6
  `supersedes the round-59 measured-commit citation` naming
  `c1-driver: measured=revision 160caf750dcf15892b78ec066e66bc605ba57a5c`; I3 the round-60
  lesson's unique routed ids superseding the duplicated `R20`/`R21`/`R22`.
- **I7 — the gate-selftest gap.** `corpus/openbao-transit-trial.sh` gains a fixture-driven
  `--selftest` (`TRANSIT_SELFTEST: PASS (cases=9)`, no `bao`, no network) and its
  `SKILL.md` registry row is re-registered with it; a mutated copy reads
  `TRANSIT_SELFTEST: FAIL (cases=9 failed=5)` with named `FINDING TRANSIT-ST-*` ids, and
  the trial still reads `HOLDS 5/5` on a real run after the edit.
- **C2 instrument.** `corpus/openbao-approle-trial.sh` (T1 `bind_secret_id`, T2
  `secret_id_num_uses`, T3 `secret_id_ttl`, T4 accessor lookup/destroy, T5
  `secret_id_bound_cidrs`), PATH-only `bao`, one throwaway `bao server -dev` on 127.0.0.1
  under `setpriv --pdeathsig KILL`, credentials on stdin only, five shims, and a 45-case
  fixture-driven `--selftest`. `plans/round-60-c2.sh` scores the frozen predicate.
- **Sources and entry.** S123 (`https://openbao.org/docs/auth/approle/`, 78543 B) and S124
  (`https://openbao.org/docs/api/auth/approle/`, 145203 B) opened live 2026-11-07 with a
  desktop browser agent, captured at `.ufo/waves/round-60/capture/` with sha256 + byte
  counts and a 19-row quote checker (`QUOTE_VERIFY: rows=19 failures=0`); entry
  `corpus/knowledge/openbao-approle-secret-id-custody.md` (measured table, seven
  docs-vs-binary rows, bounds, falsifiers), `Reverify: R21-02`, stamp row,
  `DOC_AUDIT: CLEAN (entries=41 row_linked=38 by_hand=3 …)`.
- **Pre-freeze battery.** `plans/round-60-controls.sh`, 20 controls, receipt
  `.ufo/waves/round-60/controls/controls-prefreeze.txt` reads
  `CONTROLS: match=20 mismatch=0` (rc 0) with the five instrument pins equal to the
  shipped `sha256sum` values.
- **Frontier step.** `corpus/QUALITY.md` gains QM76 (a `kind: gate` row carries a runnable
  self-invocation mode, shown able to fail) and QM77 (an amendment cites a receipt carrying
  every observable it restates); both criteria come from this round's mined mistakes.
- **Self-counts.** `python3 -I -B corpus/self-counts.py` ⇒
  `SELF_COUNTS: POLICY (claims=63 stale=0 unlocated=0 ambiguous=0 policy=2 setup=0)` after
  five stale statements (stamps 147→148, docs 37→38 / 40→41) were corrected.

### Wave seats

16 seats, 16 reports in `.ufo/waves/round-60/w1/`, **0 dead seats** (`w1-results.json`:
16 results, every `output` non-empty). Role mix: 2 scout, 6 executor, 2 scribe, 1
reviewer, 1 critic, 1 mutation-tester, 1 sentinel, 1 connector, 1 revenger. The
mutation-tester settled late but delivered a full mutant table (16 mutants, 9 killed,
7 survived).

### Attack findings and what happened to them

- **reviewer** (`build/R60ReviewerC1/findings.md`, 35 probes): I6's anchor did not exist
  at BASE; controls K1-REF/C1-F2 were mismatched by a wrapped bullet; C1-F7 was inert;
  C1-F6 mutated a comment; I7 could not tell a real selftest from a PASS printer; I2 had a
  decoy anchor; I5 accepted one-line stubs; a symlinked `LOG.md` let the challenge write
  outside the copy. **All eight are fixed in the instruments** (§A5) and the battery now
  reads them green; the symlink path is refused with `SETUP`.
- **critic** (`build/R60CriticClaims/attack.md`): C1.5 (I6 anchor) and C1.4 (guard field)
  confirmed and fixed; C2.7 (A3's receipt did not carry the observables it restated)
  confirmed and answered by §A4 withdrawing A3 item 4; C2.4/C2.5 (the `--selftest` free
  pass and the argv clause's missing instrument) are named ceilings, routed as R32/R33;
  H5's attack-share arithmetic is reported both ways (R36).
- **sentinel** (`build/R60SentinelTrial/review.md`): six security checks, five PASS and one
  PARTIAL (in-file documentation of the unsafe `bind_secret_id=false` leg, routed R35);
  `strace` over the trial's tree reads `EXEC total=171 argv_hits=0` and
  `WRITES total=97 outside=0`; five selftest mutations are killed with finding ids.
- **mutation-tester** (`build/R60MutCounters/mutants.md`): `MUTANTS: total=16 killed=9
  survived=7`; the four instrument survivors are routed R40–R43 with proposed kills (the
  guard's printer-stub clause is vacuous; a checker fallback mutant survives; the C2
  counter's `real2` and `error=1` mutants survive the battery's control set). None changes
  a claim reading; each is a battery/selftest coverage gap.
- **revenger** (`build/R60RevContext/intent.md`): reconstructed D1–D7's intent and judged
  each repair; the `Mislleading-but-passing` list is empty on the landed corrections.
- **connector** (`build/R60ConnectorSiblings/sweep.md`): no sibling lane holds AppRole,
  `secret_id` or the trial+shim+counter-with-selftest pattern; the shokuknow `merge/kagi/`
  package stages no AppRole material.
- **scouts**: S123/S124 captured with located quotes and digests; the routed scout
  re-derived all seven BASE facts and found no wrong number in the plan.

## Landed changes

| change | LOG entry | commit |
|---|---|---|
| frozen plan `plans/round-60.md` (predicate, items, kill rules, ceilings) | §Round 60 | `cd631737` |
| wave spec + dispatch + builder, §A3 measured preconditions, L1 probe receipt | §Round 60 | `5e1649a3` |
| §A4 — frozen T1 reachable unamended (sentinel + L1 re-measurement) | §Round 60 | `a177161c` |
| §A5 — six attack-seat item defects amended before the candidate reading | §Round 60 | `b662e114` |
| §A6 — I5 scope receipt token corrected to `ADJACENCY_SCOPE` | §Round 60 | `cad84270` |
| instruments, record repairs, transit selftest, entry, rows S123/S124, gates, SCORECARD/LOG/SKILL/PROVINCE, wave evidence | §Round 60 | `14a6c07d` |
| revision-bound candidate readings at `14a6c07d` + the wave results file | §Round 60 | `9cc59014` |
| end-of-round census receipt (124 rows, `kagi ok`) | §Round 60 | `2a44708b` |
| LOG dead-seat count corrected to the measured 0 (16/16 seats settled) | §Round 60 | `818d2a82` |

## Before → after measurements

| claim | before | after | counting command | measured commit |
|---|---|---|---|---|
| C1 calibration | `C1_ROUTED: value=7 population=7 i1..i7=0 guard=0` (diagnostic, rc 1) | `C1_ROUTED: value=0 population=7 i1=1 i2=1 i3=1 i4=1 i5=1 i6=1 i7=1 guard=1` (rc 0) | `bash plans/round-60-c1.sh <rev>` (`--no-challenge` for the diagnostic leg) | `14a6c07d` (`.ufo/waves/round-60/final/c1-landed.txt`) |
| C2 operability | `C2_APPROLE_TRIAL: value=0 tests=5 pass=0 shims=0 vectors=0/5 selftest=0 guard=0 (absent)` | `C2_APPROLE_TRIAL: value=5 tests=5 pass=5 shims=5 vectors=ok/5 selftest=1 guard=1` (rc 0) | `bash plans/round-60-c2.sh <rev>` | `14a6c07d` (`.ufo/waves/round-60/final/c2-landed.txt`) |

Named ceilings: C1's seven items are a closed set and each is a structural read (a forged
receipt passes; the guard's +1 challenge cannot fire on a tree where I1 is unresolved);
C2's counter reads the trial's own `--selftest` PASS line, so a PASS printer is a ceiling
(R32), and the trial measures one binary, one host, one dev server.

## Sources & frontier

SOURCES: 122 → 124 rows (`grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|'
corpus/SOURCES.md` ⇒ 122 at BASE, 124 at the tip); census before `kagi ok` rc 0 at 122
rows (run at round start, output pasted in `corpus/lessons/round-60.md` §Sources &
frontier), after `kagi ok` rc 0 at 124 rows
(`.ufo/waves/round-60/final/census-end.txt`, rc 0, the same 19 standing W04 warnings).
Rows added: **S123, S124** (both tier A, `mined`, `180d`, `used-by`
`corpus/knowledge/openbao-approle-secret-id-custody.md`), each with a fetch-provenance row
in `corpus/source-fetches.tsv` bound to its capture digest and byte count. Rows touched
old→new: none. Frontier rows advanced: none — the two rows are core ground for the entry;
the round's frontier step is the curated pair plus the recorded rejection class (both
pages document no refused-login shape: `grep -cE '\b4[0-9][0-9]\b'` ⇒ 0 on both captured
bodies, so every refusal text the trial quotes is measured, never cited).
Assimilation: none — the shokuknow `merge/kagi/` package stages no AppRole material
(connector sweep) and the claim cap is spent on C1 + C2. considerthese: the latest file
(2026-10-26) carries one still-unimplemented proposal (a repair-only release path under a
HOLD); it is not mined this round because no HOLD is in force and the proposal adds no
surface the lane lacks — proposal 2 (machine-readable lane status) was already implemented
as the `lane-status:` line, and proposal 3's release-clock defect is fixed at BASE
(`STABLE_TITLE_RE` excludes a period-suffixed version since round 45).

## Trend verdicts

- **expansion: improved** — a registry delta of two admitted tier-A rows and one executed
  entry on ground the coverage map did not hold (AppRole custody), plus a coverage-map row
  and a new capability row in `SCORECARD.md`.
- **quality: improved** — the seven routed record defects now read true against derived
  numbers, the transit gate carries a real selftest with a red witness, and the entry
  states its measured limits, the pages' silence on refusal shapes and its bounds. The
  round introduced no new record defect that it did not itself route (R32–R43).
- **discernment: improved** — the wave's attack seats changed the instruments before
  admission (reviewer: eight instrument defects, all fixed; critic: the A3 provenance
  overreach, withdrawn by A4; sentinel: six security checks and five killed selftest
  mutations; mutation-tester: 16 mutants with the four survivors routed), and the
  outside-closure defects of round 59 are all closed on the record.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources
  Evidence: `SKILL.md` §Vault-ops decision table, §Failure table, §Credential-hygiene
  checklist, and the round-60 gate-registry rows (`plans/round-60-c1-check.py`,
  `corpus/openbao-approle-trial.sh`, `plans/round-60-c2.sh`); citation run
  `CITATION_GATE` is scoped and carried (see the round-59 entry's named scope).
- [~] At least one end-to-end domain task executed and logged in LOG.md
  Evidence: `LOG.md` §Round 60 — the AppRole custody trial executes five mechanics against
  a throwaway OpenBao 2.7.2 dev server with two independent real runs, five shim vectors
  and a 45-case selftest (`.ufo/waves/round-60/build/R60ExecTrial/receipt-*.txt`).
- [~] Instructions executable by an agent without oral context
  Evidence: `corpus/lessons/round-60.md` §Bounds and the frozen plan's item conditions;
  the runnable gates are `plans/round-60-c1.sh`, `plans/round-60-c2.sh`,
  `plans/round-60-controls.sh`, `corpus/openbao-approle-trial.sh --selftest`.
- [~] No cross-domain bleed (PROVINCE.md still accurate)
  Evidence: `PROVINCE.md` §Surfaces plus `corpus/scope-gate.sh` ownership rules;
  `.ufo/waves/round-60/final/scope-candidate.txt` reads `ADJACENCY_SCOPE: DEFECT` for the
  carried breadth debt only (`stale_basis=0`, `breadth_drift=5`, `breadth_unverified=1`),
  which the round names rather than absorbs.

Stale-lane: the round is `progressing`, not stale — launch 15:09:28 -03, lane commits at
15:10 (`5e1649a3`), 15:23 (`a177161c`), 15:44 (`b662e114`), 15:59 (`cad84270`), 16:22
(`14a6c07d`) and 16:33 (`9cc59014`), all inside the mission window; the report lands after
the last of them. Respawn-per-round driver; no other mission of this lane is open.

Tool installs: none this round (python3/git/curl/bao as shipped; the operator tooling
authorization went unused by the L1 and by every seat that reported).

Fleet-root note: `git -C /home/vgpnk/Projects/shokunin status --porcelain` shows
untracked `f.txt` (2 B, 04:40) and `trail-ids.txt` (1 B, 2026-11-06 20:36) — neither names
this lane or round and both predate the round's seats, so they are another lane's strays
and were left untouched; no misrooted file of this round was found.
