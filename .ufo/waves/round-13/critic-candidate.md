# Round-13 compaction candidate — falsification

## Method and axes

I treated the source as `PROTOCOL.md` and compared bytes with both candidates, rather than treating census phrase hits as proof. Commands used below are included with their observed output. The axes are obligation preservation, deletion accounting, pointer resolution, citation survivability, and the cost/benefit of splitting the digest.

## Obligation-loss hunt (source and candidate quotations)

Each source quote is from `PROTOCOL.md`; candidate quote is from `.ufo/waves/round-13/PROTOCOL.compact.md` (the single-file candidate is byte-identical in these body regions). `diff -u PROTOCOL.md .ufo/waves/round-13/PROTOCOL.compact.md` is the command used to establish candidate text; line numbers are the observed source/candidate locations at this audit.

1. **Round-12 history pin — SAME.** Source: “`.ufo/history-pin.json` pins `sha256(rounds[0:k])` for the closed prefix plus the commit whose `MANIFEST.json` bytes hash to it… Appends never invalidate it.” (`PROTOCOL.md:248-251`). Candidate: “`.ufo/history-pin.json` pins `sha256(rounds[0:k])` for the closed prefix plus the commit whose `MANIFEST.json` bytes hash to it… Appends never invalidate it.” (`PROTOCOL.compact.md:248-251`). The new pin obligation survives verbatim.
2. **Round-12 frozen snapshot digest — SAME.** Source: “A frozen baseline's `expected.json` MUST pin the digest of every snapshot input file, and the gate verifies those digests before comparing verdicts” (`PROTOCOL.md:378-381`). Candidate: same sentence (`PROTOCOL.compact.md:318-321`). No modal or scope change.
3. **Round-12 tamper result — SAME.** Source: “an edited snapshot is `snapshot_tampered` (could-not-evaluate), not a compared verdict, and a baseline without digests is reported `unpinned (legacy)`” (`PROTOCOL.md:379-381`). Candidate: exact text (`PROTOCOL.compact.md:319-321`).
4. **Round-12 row identity — NARROWED.** Source: “the optional `lane_rounds: {<id>: <n>}` map records a lane's own counter where it differs from the entry's `round` and is required on every `not-dispatched` row” (`PROTOCOL.md:279-282`). Candidate: “the optional `lane_rounds...` map records a lane's own counter where it differs from the entry's `round` and is required on every `not-dispatched` row” (`PROTOCOL.compact.md:224-227`). The immediate sentence is SAME, but candidate deletes the source's explicit “the counter the lane actually held is what makes such a row falsifiable” and the source's explanation that pre-fleet-2 rows are `unadjudicable` is compressed. The census can pass while the falsifiability rationale/interpretive constraint is lost; restore it or mark the shortening intentional.
5. **Round-12 orphaned-report order — SAME in prose, but cross-duty risk.** Source: “An orphaned report is resolved in order: the lane's own respawn inherits and lands it; the integrator sweeps it for durability only if that successor mission also terminates without landing it… the order never reaches aggregator-owned `corpus/` files” (`PROTOCOL.md:117-121`). Candidate: “An orphaned report is resolved in order: the lane's own respawn inherits and lands it first; the integrator sweeps it… only if that successor mission also terminates without landing it… the order never reaches aggregator-owned `corpus/` files” (`PROTOCOL.compact.md:82-85`). This is SAME; however the candidate's later aggregator paragraph drops the source's explicit “filed without the ledger duty keeps the routed-defect queue empty by construction” (`PROTOCOL.md:317-319`), so the order is not enough to preserve the queue consequence.
6. **Round-12 stale-lane sibling grade — SAME.** Source: “sibling-authored activity alone is a third grade, `progressing-weak`: named as such in the row, never called progressing, and never silent or `failed` on its own” (`PROTOCOL.md:158-160`). Candidate: exact text (`PROTOCOL.compact.md:116-119`).
7. **Round-12 unlanded report — NARROWED.** Source: “an uncommitted file at the report path does not end `in-flight`, however it fires the driver's existence signal” (`PROTOCOL.md:261-263`). Candidate: same rule (`PROTOCOL.compact.md:206-209`). But source also says “a cited hash that is not an ancestor of `HEAD` at closure is a conformance defect” and ties the unlanded signal to the completion path; the candidate compresses the surrounding evidence distinctions. Preserve the explicit closure-time consequence in the candidate's status paragraph.
8. **Marker clause — NARROWED.** Source: “A filed report that records no lane work — no changes, no evidence pointer, no resolvable commit — is a marker, not a report… A short report that names a real committed round-work hash is a defective report, not a marker: status `ok`, minimum-content defect recorded. A marker that names nothing checkable is `failed` whatever the lane actually did” (`PROTOCOL.md:174-183`). Candidate: “A filed report recording no lane work — no changes, no evidence pointer, no resolvable commit — is a marker… A short report naming a real committed round-work hash is a *defective* report, not a marker… A marker naming nothing checkable is `failed` whatever the lane actually did” (`PROTOCOL.compact.md:128-136`). Candidate deletes the source's “keeps the marker file as a conformance defect, and names the counter advancement in the round notes” and “This does not relax step 1”. Those are operative consequences, not explanatory prose. **NARROWED.**
9. **Stale-lane grade one — SAME.** Source: “Progressing means observable activity in the lane's write scope since its launch — a commit authored by the lane, or files modified under its repo” (`PROTOCOL.md:152-157`). Candidate: exact rule (`PROTOCOL.compact.md:111-115`).
10. **Stale-lane grade two — SAME.** Source: “silent means neither” (`PROTOCOL.md:155-157`). Candidate: “silent means neither” (`PROTOCOL.compact.md:113-116`).
11. **Stale-lane grade three — SAME.** Source: “sibling-authored activity alone is a third grade, `progressing-weak`… never silent or `failed` on its own” (`PROTOCOL.md:158-160`). Candidate: exact text (`PROTOCOL.compact.md:116-119`).
12. **`supersedes.entry` — SAME.** Source: “`supersedes` MAY also carry `entry` — the array index… and a gate treats a correction that needs the disambiguator and omits it as ambiguous” (`PROTOCOL.md:298-301`). Candidate: same sentence (`PROTOCOL.compact.md:243-246`).
13. **Integrator write-scope count — REWORDED-OK only if new path is contractual.** Source: “expand by exactly five: appending `MANIFEST.json` `rounds` entries… committing the round's closure-gate artifacts under `.ufo/waves/round-<N>/`” (`PROTOCOL.md:188-193`). Candidate: “expand by exactly six… and writing/committing the append-only history pin `.ufo/history-pin.json` — the sixth” (`PROTOCOL.compact.md:140-146`). The count correction is valid, but the source's listed main-repo writes do not name a committed root `PROTOCOL-APPENDIX.md`. If the split lands, add that path to this exact write-scope sentence and to the file contract; otherwise the new artifact is an undocumented exception.
14. **Gate verdict — SAME.** Source: “`0` = `clean` and `1` = `failed` fleet-wide… undeclared nonzero code reads as `could-not-evaluate`” (`PROTOCOL.md:367-371`). Candidate: exact text (`PROTOCOL.compact.md:304-308`).
15. **Gate self-test — SAME.** Source: “Every gate exposes a self-invocation mode over isolated fixtures… asserting both the exit code and a stable expected finding-id” (`PROTOCOL.md:372-376`). Candidate: exact text (`PROTOCOL.compact.md:309-313`).
16. **Gate two evidences — SAME plus new pin.** Source: “A gate whose verdict depends on a mutable fleet artifact also ships a run over a committed input snapshot with its committed expected verdict” (`PROTOCOL.md:377-381`). Candidate: exact text plus digest requirement (`PROTOCOL.compact.md:314-321`).
17. **Gate registry — NARROWED.** Source: “the rows live in each lane's `SKILL.md`: name, `gate|probe`, entry command, verdict map… pinned-value path, write scope, owner” (`PROTOCOL.md:382-385`). Candidate: same list (`PROTOCOL.compact.md:322-325`) but deletes “closure grades no gate conformant until its registry row exists” only in the later Delivery rule? Candidate retains that line. **SAME** for obligation; the missing “working gate does not break on adoption” qualifier from source verdict is a smaller interpretive loss and should be retained if compatibility is intended.
18. **Gate scope — SAME.** Source: “Read-only over surfaces it does not own, and it never acts on an external surface” (`PROTOCOL.md:386-389`). Candidate: exact text (`PROTOCOL.compact.md:328-332`).

The requested minimum of 12 is exceeded (18 rulings). The material defects found by this hunt are the marker consequence and the undocumented new appendix write path; the row-identity and unlanded-report compressions are lower-severity interpretive losses.

## Diff-driven deleted-hunk accounting

Command and observed output:

```sh
$ diff -u PROTOCOL.md .ufo/waves/round-13/PROTOCOL.compact.md > /tmp/compact.diff
$ grep -c '^@@' /tmp/compact.diff; grep '^-' /tmp/compact.diff | grep -v '^---' | wc -l
7
314
```

I walked all 7 deleted hunks. Accounting by hunk: (1) lifecycle/sibling-mint material — **LOST**: no candidate rule preserves the ordered sibling mint scan, seed-file set, three-round probation, or “never writes outside its own repo”; (2) promotion seed detail — **NARROWED**: four seed requirements and reviewer mechanics survive only as a pointer, while source requires the decision-table/error-list/checklist resolvable-source minimum; (3) round prompt fidelity — **NARROWED**: exact “prompt-fidelity defect does not fix the template” and corrected-text delivery consequence is deleted; (4) landed/report closure detail — partially survives, but marker conformance defect and counter-advancement consequence are **LOST**; (5) closure step 2 queue durability — **NARROWED**: source's “filed without ledger duty keeps queue empty by construction” is deleted; (6) file-contract/invariant details — mostly survives, but the protocol-owned new appendix path has no contract row; (7) appendix body — survives byte-for-byte in the separate appendix, except its title/preamble is now in another file. Result: 7/7 hunks walked; 0 unaccounted, but 2 contain LOST obligations and 4 contain NARROWED obligations.

Single-file comparison:

```sh
$ diff -u PROTOCOL.md .ufo/waves/round-13/PROTOCOL.compact.singlefile.md > /tmp/single.diff
$ grep -c '^@@' /tmp/single.diff; grep '^-' /tmp/single.diff | grep -v '^---' | wc -l
7
279
```

The single-file candidate accounts for the same seven semantic deletion regions and retains the incident rows in place, so it avoids the cross-file pointer failure. It still loses the lifecycle sibling-mint block, marker consequences, and parts of prompt/file-contract detail. The split therefore adds defects; it does not cure the obligation losses.

## Pointer and section integrity

The body has 25 `(§Appendix, "X")` occurrences by visual sweep. The appendix's first column contains the named rows for all ordinary labels (`Lands last`, `Stale-lane actuator`, `Marker vs report`, `Prompt embeds contract`, `Orphaned report`, `Gate standard`, etc.). However the candidate body itself says “This file alone reaches the lanes that re-read it (§Appendix, …)” and the final section is still headed `## Appendix — incident digest`, while the actual row artifact is `PROTOCOL-APPENDIX.compact.md`. A cold reader holding only the body cannot resolve a `§Appendix` section or inspect the rows; a reader holding only the appendix cannot resolve the `PROTOCOL.md` rules it annotates. The four-line pointer block is not a sufficient file-contract declaration: it names a copy path but does not say that the root file MUST be `PROTOCOL-APPENDIX.md`, who writes it, or that both files are required inputs to the verifier.

The pointer sweep command attempted was:

```sh
$ awk 'FNR==NR{if($0 ~ /^\\|[^-]/){x=$0; sub(/^\\| /,"",x); sub(/ \\|.*/,"",x); a[x]=1} next} {while(match($0,/\\(§Appendix, "[^"]+"\\)/)){...}}' PROTOCOL-APPENDIX.compact.md PROTOCOL.compact.md
) MISSING
```

The observed `) MISSING` is a parser artifact (the table parser accepted the separator/header badly), not evidence that every pointer is missing. The substantive failure is structural: `§Appendix` is a section reference whose section is not in the body file; the candidate must replace it with an explicit cross-file pointer convention and verifier input contract. Reverse direction: the appendix contains no body-section references beyond its `rN` report paths and therefore has no dangling section pointer, but its preamble's “rule in `PROTOCOL.md`” is false for a cold reader of the appendix alone unless the pair contract is stated.

## External citation breakage

The repository-wide recursive grep was run as requested, excluding `.git`:

```sh
$ grep -RInE 'P:[0-9]|PROTOCOL\\.md:[0-9]' --exclude-dir=.git . | wc -l
295
$ grep -RIlE 'P:[0-9]|PROTOCOL\\.md:[0-9]' --exclude-dir=.git . | wc -l
56
```

The sweep emitted filesystem-loop diagnostics under `.ufo/waves/round-12/mutants/*`; those paths are generated mutant trees and must be excluded in the final owner sweep. Directly observed invalidated citations include:

* `kumitate-shokunin/scripts/round-gate.mjs` header `PROTOCOL.md:263-267` — stale already in round 12 and remains stale after compaction; **owner: kumitate**, not this lane.
* `.ufo/waves/round-12/closure-check.py` docstring citations `P:202-260`, `P:215-224`, `P:150-155`, `P:124-136`, `P:206-213`, `P:218-221`, `P:224-228`, `P:244-249`, `P:256-260`, `P:209-213` — all numeric anchors move to the compact body, so they are invalidated; **owner: closure-check artifact owner / protocol lane if the artifact is being migrated**, otherwise route as citation maintenance.
* `.ufo/reports/round-12/closure-semantics.md` citations `P:206`, `P:211-213`, `P:215-221`, `P:151-155`, `P:223-224`, `P:224-228`, `P:233-240`, `P:256-260`, `P:244-249`, `P:241-243`, `P:250-255`, `P:229-232`, `P:178-186`, and related evidence strings — invalidated by line movement; **owner: report/citation owner**, with protocol lane responsible for publishing a stable section/anchor replacement.
* `.ufo/waves/round-11/protocol-reference-sweep.md` citations such as `PROTOCOL.md:292-298`, `:394`, `:453-454`, and `:101-102` were already stale and remain stale; **owner: cited artifact's lane**, not a reason to leave the protocol un-compacted.
* `.ufo/waves/round-9/aggregator.md:175` `PROTOCOL.md:434-435` — invalid after compaction; **owner: aggregator report owner**.

A gate whose evidence strings embed dead `P:` ranges is a measurable migration cost: at least 10 distinct closure-check docstring ranges plus the many generated finding strings in `closure-check.py` are invalidated. The recursive total is 295 matching lines across 56 files, but that is an upper bound because it includes already-stale lines, prose, and generated mutants; it is not honest to call all 295 newly broken. The named closure-check family alone has 10 docstring ranges and multiple runtime evidence templates requiring correction.

## Two-file design ruling

**Steelman:** moving the 32-row incident digest makes the normative body bounded, lowers re-read cost, and lets the digest grow without repeatedly breaking a body-line cap. It also makes the single-file appendix independently reviewable and keeps the rows byte-identical.

**Attack:** the ≤470 metric was booked against one file. The measured comparison says a 470-line single file passes the committed gate for the pre-round-13 obligation set, while the four new obligations make the single-file form 479 lines. Relocating 40 lines can therefore be metric gaming unless the acceptance metric explicitly changes to a pair total and the pair is included in file contract, write scope, census, and verifier inputs. The split creates four real costs: a new root path requiring a file-contract row and integrator write-scope mention; cross-file pointer resolution; a second verifier mode; and one more file for a cold reader. The candidate body pays only the pointer-block cost, not the contract/verifier/ownership costs. The single-file candidate pays none of those new costs and has the same obligation losses from compaction.

**Ruling:** structural improvement is plausible, but this candidate is not yet sound as a two-file protocol artifact. Land the split only after the pair contract and verifier mode are normative and the lost obligations are restored. Otherwise land the single-file form after restoring the same lost obligations.

## Verdict and must-fix list

**Verdict: do not land as-is.** Recommended score: **8 held** remains binding under `critic-plan.md` blocker 1: compaction repays booked debt, so it does not earn capability credit merely by reducing lines. The 156-row census, committed verifier, history pin, frozen baselines, and mutation score are genuine new capabilities, but they do not erase the obligation losses or make a second file self-describing.

Must-fix, ranked:

1. **CRITICAL — restore lost lifecycle/sibling-mint obligations.** Reinsert the ordered roster scan, seed-file set, driver wiring, three verified rounds, delayed manifest/roadmap rows, and prohibition on writing outside the minting lane's repo/new seed files.
2. **CRITICAL — restore marker consequences.** Add back “keeps the marker file as a conformance defect,” “names counter advancement,” and “does not relax step 1”; preserve the real-report-vs-marker status distinction verbatim.
3. **HIGH — make the split a file contract.** Add `PROTOCOL-APPENDIX.md` to the file contract and integrator write scope, define the pair as REQUIRED verifier inputs, and state that ordinary lanes cannot write it.
4. **HIGH — replace `§Appendix` cold-reader ambiguity.** Use an explicit `PROTOCOL-APPENDIX.md` cross-file reference (or retain the single-file appendix); make every pointer resolver check the appendix first-column key and fail closed when the file is absent.
5. **HIGH — migrate citations.** Re-anchor closure-check's 10 docstring ranges and runtime evidence strings to stable section/rule identifiers; route child-repo/report fixes to their owners and quantify remaining dead ranges at closure.
6. **MEDIUM — restore prompt-fidelity and ledger-queue consequences.** Preserve the exact corrected-template delivery rule and the source's “ledger duty keeps the routed-defect queue empty by construction” warning.
7. **MEDIUM — publish a clean citation sweep.** Re-run excluding mutant symlink loops and distinguish newly invalidated citations from pre-existing stale citations.

DESPAWN: gx-critic-candidate — signal delivered. Send me shutdown_request.