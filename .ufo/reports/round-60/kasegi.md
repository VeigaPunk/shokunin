# kasegi round 60 — the derive gate becomes escape-aware and refuses the in-program/write-flag probe set Q1–Q7 (C1, depth:verifiability, nominal per QUALITY R58, held 4), and frontier F41 on S093, Project Zero's own Fuzzilli-vs-BigSleep comparison (C2, coverage, held 8)

Round shape: ONE v1 wave (policy band 8–16) of **13 seats** — scouts 2, scribe 1, connector 1, reviewers 2, critic 1, mutation-tester 1, sentinel 1, executors 4; attack share 4/13 = 31%, connector 1/13; the L1 holds the planner seat (the validator refuses a planner role). Residual call: none — the round is 13 seats total, inside the band. Routing: the orchestrator's `task.agentModelOverrides`; no model alias was passed or named by the lane. WAVE-DONE received for the one launched wave (`.ufo/waves/round-60/w1-results.json`); 13/13 seat evidence files, 0 dead, 0 resumed.

## Work performed

Declared claims (frozen at `66e6241`, base `cdeea55`; implementation `7f7dd26`; lane tip at filing `e63ba11`):

- **C1 — depth:verifiability** (lowest non-retired axis, 4; nominal per QUALITY R58): the figure-audit derive gate (`corpus/instruments/figure-audit.py`) gains an escape-aware quote model, drops `awk`/`sed` from the allow-list, refuses the flagged write forms `sort -o` and `git show --output`/`--ext-diff` by a write-flag screen, keeps its ledger green after the five `awk` derives are re-expressed, and pins its docstring to the allow-list it enforces (R74).
- **C2 — coverage** (8): frontier F41 — Project Zero's own dated comparison of Fuzzilli and BigSleep on V8 — admitted on S093, with the stale SOURCES lead bullet corrected.

Work items (each with an evidence pointer):

1. **Round-start census** — `scripts/sources-census.sh validate --root … kasegi` → exit 0; `.ufo/waves/round-60/controls/census-round-start-r60.txt` (the round-59 closure's defect 7).
2. **Base red-before probes** — `controls/c1-probes-base-r60.txt`: Q1–Q6 execute (`markers=1`), Q7 is admitted and run; both controls pass; the python-traversal residual is admitted.
3. **Base do-nothing controls** — `controls/do-nothing-c1-r60.txt` (selftest 14, ledger 35/35, docstring limb 0) and `controls/do-nothing-c2-r60.txt` (rows=40, registry=92, entries=43, knowledge 78, binding 75, F41 absent).
4. **Candidate instrument** (stand-in clone at base) — escape-aware `split_segments`, `awk`/`sed -n` out of `READ_ONLY_HEADS`, `tr` in, `DENIED_FLAGS` screen, docstring allow-list, six new selftest cases; `controls/c1-standin-after-r60.txt` (20/0, mutbat 2/2, ledger 35/35, red stale, limb 1), `controls/c1-probes-standin-r60.txt` (Q1–Q7 refused).
5. **Ledger rewrite** — five `awk` derives re-expressed as `cut`/`tr`/`wc` and `grep`/`wc`; each prints its recorded want (38/39/40/0/0) before the freeze (`corpus/instruments/figure-audit-ledger.json`).
6. **C2 source** — `capture-source.py --kind html` fetched the post (HTTP 200, 64812 bytes, 40649-byte snapshot, sha256 `46f69d32…`); `corpus/source-snapshots/round-60/S093.txt` + `manifest.json` (15 pinned quotes, max 25 words).
7. **C2 corpus delta** — entry `corpus/knowledge/project-zero-fuzzilli-vs-bigsleep-comparison.md`; registry row S093 (`corpus/SOURCES.md:100`); README round-60 admission block and F41 row (`corpus/README.md:1005`); PROVINCE r60 amendment (`PROVINCE.md:209`); `knowledge-expected.txt` 79 = 79 sorted; the stale lead bullet corrected (`corpus/SOURCES.md:142`) and logged old → new (`:221`).
8. **Extended neighbor screen** — `controls/neighbor-screen-r60.txt` (eight limbs; only F40/F41 files hold the surface, no sibling PROVINCE hit, the post URL appears in no prior row). Run after the freeze — recorded as M60-6/R80, not hidden.
9. **Assimilation id check** — `.ufo/waves/round-60/assimilation/`: registry 92 ids, staged 94, `collisions=62`, staged contains S093, nothing adopted.
10. **Carry-in fixes (non-claims)** — capability rows (defect 2), round-59 calibration and quote corrections of record (defects 3–4), SHONEN box-2 reconciliation (defect 5), lead correction (defect 8), Gate wording scoped (defect 9), receipt labels (defect 10), literal-runnable counting commands (defect 1/R77); the new entry's recheck line carries no absolute `cd` (ExportReplay class fixed for itself — ReviewerC2 §E13).
11. **Wave w1** — 13 seats, results `.ufo/waves/round-60/w1-results.json`, evidence `.ufo/waves/round-60/w1/`; verdicts in the wave section below.

## Landed changes

| Change | LOG.md entry | Commit |
|---|---|---|
| Freeze: claims, base/do-nothing/stand-in receipts, probe runner, S093 capture+manifest, assimilation id check | `## Round 60` bullet 1 | `66e6241cd7afd6184273ce7df1dcd5328c187367` |
| Implementation: instrument (escape-aware + deny screen + docstring + selftest 20), ledger rewrites, F41 entry, S093 row, README block, PROVINCE amendment, expected list, SKILL registry cells, QUALITY R78, claims erratum | `## Round 60` bullets 2–5 | `7f7dd267283d2a16ca38d4cb05bed92165cb35cd` |
| Wave spec, validated plan and dispatch (13 seats, policy v1) | `## Round 60` bullet 7 | `b8c77fb9fa13710f46d8f564a00af640de5108cd` |
| Lesson (M60-1..M60-7, Gate S093, Sources & frontier, Limits), neighbor-screen receipt, SHONEN box-2 reconciliation | `## Round 60` bullets 6, 8–9 | `fb6a92888f4a912e7d9931c7225978c4572827df` |
| SCORECARD round-60 section (axes, move log, capabilities rows, round-59 corrections of record, planned 61) and LOG round-60 entry | `## Round 60` | `228118a8cfba679c1d97841aa3af38e5ec83d84a` |
| Wave evidence + integration: results and 13 seat files, entry Limits boundary bullet, SKILL r60 residual correction, committed-tree and base-vs-candidate receipts, QUALITY R81–R82, lesson wave section and M60-8..M60-10, SCORECARD/LOG wave verdicts | `## Round 60` bullet "Wave-1 outcome" | `e63ba11a12e7376bbdc35be14abfd942e0a500ba` |

## Before → after measurements

### C1 — depth:verifiability (nominal, held 4), base `cdeea55` → implementation `7f7dd26`

Counting command (literal, from the lane root):

    bash .ufo/waves/round-60/controls/c1-probe-run-r60.sh corpus/instruments/figure-audit.py /fast/scratch/hyaku/kasegi-r60/l1/c1-after

| measure | before (`controls/c1-probes-base-r60.txt`, `do-nothing-c1-r60.txt`) | after (`controls/c1-lane-after-r60.txt`; `c1-lane-after-committed-r60.txt` from committed bytes at `7f7dd26`) |
|---|---|---|
| Q1 escaped single quote | `exit=1 markers=1` | `exit=2 markers=0` |
| Q2 escaped double quote | `exit=1 markers=1` | `exit=2 markers=0` |
| Q3 `sed` in-program `e` | `exit=1 markers=1` | `exit=2 markers=0` |
| Q4 `awk system()` | `exit=1 markers=1` | `exit=2 markers=0` |
| Q5 `sort -o` | `exit=1 markers=1` | `exit=2 markers=0` |
| Q6 `git show --output` | `exit=1 markers=1` | `exit=2 markers=0` |
| Q7 `git show --ext-diff` | admitted, run (`exit=1`) | `exit=2 markers=0` |
| CTRL-quoted-semicolon | `exit=0 derived=35` | `exit=0 derived=35` |
| CTRL-plain-count | `exit=0 derived=1` | `exit=0 derived=1` |
| RESIDUAL-python-traversal | admitted (python fails) | admitted (named open) |
| selftest | `cases=14 failures=0` | `cases=20 failures=0` (host-conditional: bare `python`, see H1) |
| mutant battery | `killed=2/2 survivors=0 controls=pass` | `killed=2/2 survivors=0 controls=pass` |
| ledger | `figures=35 ok=35 stale=0` | `figures=35 ok=35 stale=0` |
| red fixture | `stale` | `stale` |
| R74 docstring limb | `0` | `1` |
| digests | instrument `32e1cddb…` | `35f7bcd3…`; ledger `28ad7fef…` |

### C2 — coverage (held 8), base `cdeea55` → implementation `7f7dd26`

Counting command: `python3 corpus/instruments/frontier-recheck-count.py | grep -E 'FRONTIER-CENSUS|FRONTIER-PASS F41|entries='`

| measure | before (`controls/do-nothing-c2-r60.txt`) | after (`controls/c2-lane-after-r60.txt`; `c2-lane-after-correction-r60.txt` after the entry bullet) |
|---|---|---|
| frontier census | `rows=40 admitted=40 closed=40 problem-rows=0 registry=92` | `rows=41 admitted=41 closed=41 problem-rows=0 registry=93` |
| F41 line | absent | `FRONTIER-PASS F41 ids=S093` |
| entries | `entries=43 pass=43 exit=0` | `entries=44 pass=44 exit=0` |
| source-recheck S093 | — | `sha256 OK` + 15 `Q… OK` lines, exit 0 |
| capture binding | `records=75 bound=75 unbound=0` | `records=76 bound=76 unbound=0` |
| knowledge files / expected | 78 / 78 | 79 / 79, `sort -c` exit 0 |
| README F41 row | 0 | 1 |
| lead bullet | `3ed4f54d…` (stale text) | `6a67537e…` (corrected) |
| census `--file` | exit 0 | exit 0 |

The C2 counting command 8 `want` was hand-typed 1 and prints 2; `.ufo/waves/round-60/claims-erratum-1.md` supersedes it to 2 (both occurrences are the declared lead correction; the kill rule does not reference it), and R78 names the class.

## Sources & frontier

- Registry rows 92 → 93 (`grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`); rows added by tier: **A 1** (S093, mined, recheck 90d, used-by the F41 entry, opened 2026-11-04); rows touched old → new: none in the registry cells — the `## Leads (unopened)` bullet was corrected and logged old → new under `## Registry changes` (`corpus/SOURCES.md:221`); frontier rows advanced: **F41** (new).
- Knowledge 78 → 79 (`ls corpus/knowledge/*.md | wc -l`; expected 79, `LC_ALL=C sort -c` exit 0); capture binding 75 → 76 (`capture-binding-check.py`, exit 0); census exit 0 at round start (`controls/census-round-start-r60.txt`) and at the tip (`controls/c2-lane-after-correction-r60.txt`).
- Assimilation: **none** — `merge/kasegi/` is not adopted this round. The id check ran in scratch: registry 92 ids, staged 94, **collisions=62** (pre-existing registry/staged overlap), staged contains S093; because nothing is admitted, nothing is renumbered (S093 continues the lane registry; a future adoption must re-point staged ids by document). considerthese: no proposal taken (newest file `2026-10-26.md`; proposal 7 is covered by R31, proposal 2 is the SHONEN box-2 route).
- Gate: S093 opened 2026-11-04, HTTP 200, 64812 fetched bytes → 40649-byte capture, sha256 `46f69d32…`, 15 pinned quotes (max 25 words); admitted F41; rejects recorded (the DeepMind 404 lead, the unopened 2024 Naptime post, the crbug references, the hotlist queries the lane did not run). The quadrant checks: ScoutS093 AGREE with a byte-identical independent conversion; EntryClaimTable 29/29 GROUNDED; ExecAnchors REFERENTS-HOLD; SiblingOverlap SCOPE CLEAR.

## Trend verdicts

- **expansion: improved** — F41 admitted on ground the coverage map did not hold (an agent-vs-fuzzer production and re-discovery comparison), with a first-party publisher record (S093) and the frontier 40 → 41, registry 92 → 93, knowledge 78 → 79, all re-measured.
- **quality: unchanged** — no admitted entry was modified or superseded and none failed its recheck; the C1 move is nominal (QUALITY R58) and kept the ledger at 35/35 rather than adding knowledge; the docstring limb that was red at the round-59 tip is now green (R74), a defect closure rather than a quality gain. The wave's F1 class is a defect in the new screen, reported not prettified.
- **discernment: improved** — the round's own erratum superseded a hand-typed `want` (M60-1/R78); the base receipts caught a control that measured grep's grammar (M60-2) and a vacuous write-class red-before (M60-3/R79); and the wave's non-author seats found what the lane's own gate missed: the token-spelling screen bypass and the comment-phantom class (ExecEscapes, ReviewerC1 §F1, CriticC1's DEFEATED reading), the harness defects (ScoutHostBound H1–H5), and the connector's boundary omission (applied). Those disagreements became R81–R82 and the next round's plan.

## Wave-1 integration

13 seats, one v1 wave, 0 dead, 0 resumed; results `.ufo/waves/round-60/w1-results.json`, evidence `.ufo/waves/round-60/w1/`.

| seat | role | verdict as filed | round use |
|---|---|---|---|
| ScoutS093 | scout | AGREE — independent conversion byte-identical to the capture; 15/15 quotes | confirms the Gate |
| ScoutHostBound | scout | FAIL — H1–H5 in the round's harness (bare `python` in the selftest; GNU `realpath -m`/inetutils `hostname`; not fail-closed; host-stamped receipts; unguarded scratch); H6 carried | M60-10/R82; selftest value named host-conditional |
| EntryClaimTable | scribe | PASS — 29/29 GROUNDED, quotes ≤ 25 words, anchors hold | none |
| SiblingOverlap | connector | SCOPE CLEAR + one Limits recommendation | recommendation applied; counters re-run |
| ReviewerC2 | reviewer | VERIFIED — all nine C2 commands reproduce at `7f7dd26` and `228118a`; pure-append holds; ExportReplay fixed for this entry | observations recorded |
| ReviewerC1 | reviewer | VERIFIED on the frozen checks; F1 MAJOR token-spelling screen bypass (7 writing forms), F2 wording (R75), F3 selftest blindness, F4 `--compress-program`, F5 receipt header | M60-9/R81; SKILL r60 correction; F5 closed with the committed-tree receipt |
| CriticC1 | critic | DEFEATED on the security reading — 24 write/execute derives admitted, 9 green, none Q1–Q7 | named open + escalated (L0); frozen predicate intact |
| MutationC1 | mutation-tester | killed 5/13 one-limb mutants; 8 survived | named open (R17) |
| ExecCounters | executor | ALL-MATCH — 17 commands, C2 #8 at the erratum value | none |
| ExecAnchors | executor | REFERENTS-HOLD | none |
| ExecDiffScope | executor | OUT-OF-SCOPE relative to the item's own premise (a SKILL line deletion and two instrument deletions outside the parenthetical; "lane HEAD" stale) | M60-8 (item text defect; change set in scope) |
| SentinelCred | sentinel | CLEAN — no credential material, no non-public personal data | none |
| ExecEscapes | executor | 43 derives: 14 admitted-and-executing (2 with the audit green), 10 safe, 19 refused | M60-9; `controls/c1-xclass-base-cand-r60.txt` shows no regression vs base |

**Claim verdicts read against the frozen predicates:** C1 verifies (Q1–Q7 refused; controls admitted; selftest 20/0; mutbat 2/2; ledger 35/35; red stale; limb 1; digests exact; ReviewerC1 VERIFIED; ExecCounters ALL-MATCH). C2 verifies (ReviewerC2 VERIFIED; ScoutS093 AGREE; EntryClaimTable PASS; ExecAnchors REFERENTS-HOLD; SiblingOverlap SCOPE CLEAR). No axis is harmed: the base gate admits the same 14 forms (and more), and the candidate refuses strictly more — no class exists that the candidate admits and the base refused (`controls/c1-xclass-base-cand-r60.txt`).

**Residual classes named open (not claimed):** the write-flag screen compares undecoded tokens, so quoted (`sort "-o"F`), clustered (`sort -noF`), abbreviated (`sort --o=F`, `--out=F`), ANSI-C (`sort -$'\x6f'F`) and `sort --compress-program` forms are admitted and write, and `cat g.txt #'⏎touch MARK #'` phantom-opens a quote so a commented separator runs with the audit green; the `python3` head still admits a `..` traversal; any allow-listed counter can write; `$'…'`/`#` are not modelled; the new runner is host-bound and not fail-closed, and the selftest's `cases=20` is host-conditional; 8 of 13 one-limb mutants survive the selftest. Escalated on the kasegi round-60 L0 line; the next round's instrument claim targets the token decoding and the comment model.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — evidence: `SKILL.md` (Gates and probes registry, including the round-60 cell corrections and the r60 residual correction at `SKILL.md:1228`); outside promotion verification remains required.
- [ ] At least one end-to-end domain task executed and logged in LOG.md — no live end-to-end bounty task is claimed; both former domain roots are absent and live-target testing stays refused by PROVINCE.md; the round-59 report's `[~]` is corrected here (defect 5) and `SHONEN.md` says why the box stays open.
- [~] Instructions executable by an agent without oral context — evidence: `corpus/lessons/round-47-verifier-spotcheck.md`; the round-60 counting commands run literally from the lane root in a fresh clone (ExecCounters ALL-MATCH; R77).
- [~] No cross-domain bleed (PROVINCE.md still accurate) — evidence: `PROVINCE.md` (r60 amendment for F41) and `controls/neighbor-screen-r60.txt` (no sibling PROVINCE hit); live-target testing remains refused.

## Stale-lane

`Stale-lane: no — this round is the lane's respawn-per-round driver work; no other kasegi mission is open.`

## Tool installs

None — no package install or upgrade by the L1 or by any seat this round (no seat recorded an install in its evidence file).

## Inherited state

- At round start the lane tree carried only the untracked driver markers `.ufo/waves/round-{57,58,59}/w1.ready.dispatched` (named, not authored by this round). The round-60 handoff markers (`w1.ready`, `w1.ready.dispatched`) are this round's; `w1.ready` is committed as evidence, `.dispatched` stays driver-owned and untracked (as in rounds 57–59).
- No uncommitted lane-authored leftovers from an earlier attempt of round 60 existed.
- A duplicate `w1-run.json` (byte-identical to the committed `w1-dispatch.json`) and two empty `.err` files were removed before the wave-evidence commit (named here for the record).

## Open L0 questions (not blocking)

- kasegi | round-60 (new): the gate's scope ruling — model bash token decoding and comments, move the ledger to a sandboxed runner (the round-59 question), or scope the gate to literal spellings with the residual classes named. Appended to `.ufo/l0-questions.md`.
- kasegi | round-59: the derive gate's security boundary (not a sandbox). Unanswered; re-asked in substance by the round-60 line.
- kasegi | round-57/58: the frontier counter's body-substance limb (R67) and the census freshness range base (R69). Operator decisions; not re-declared as lane targets.

## Host-bound and harness notes (wave findings, non-claim)

- H1: `figure-audit.py`'s selftest shells out to bare `python`, so `cases=20 failures=0` is host-conditional (20/20 fail on a python3-only host). Pre-existing; the claim's value is measured on this host and named so. The instrument bytes are frozen by C1's digest, so the `sys.executable` repair lands next round under a new freeze.
- H2–H5: the round's probe runner uses GNU `realpath -m`/`hostname`, is not fail-closed, stamps host paths in receipts, and does not guard its scratch argument. Routed to round 61 (R82); the frozen runner bytes stay because they are the claim's evidence.
- H6: the C2 census command's absolute `/home/vgpnk/…/scripts/sources-census.sh` path is a carried convention, not new this round.
