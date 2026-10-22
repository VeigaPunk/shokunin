# kaidoku — round 27 report (attempt 1)

Lane repo `/home/vgpnk/Projects/shokunin/kaidoku-shokunin`, branch `main`. Pushed lane tip at filing: `29a76a637ad445f836b9b30382c0a6ee92a069a8` (every lane commit below came from `jj-lane.sh` printing `landed <hash>` after remote verification; `jj-lane.sh state` shows `local=remote=29a76a63… ahead=0 behind=0 tracked=0 untracked=0`). Lane-round base `cd32264f7ee356a9c0f48bd8e3fcdac222db22a0`. In-session hyaku L1, dispatched 14:41:34Z; no earlier attempt of this round (`.ufo/watchdog.log` has only the launch line for round 27).

## Work performed

Declared claims, frozen instruments-first at `a4f674b343d8564e21f7eb8984630a95089c82d6` (14:51:23Z): `.ufo/waves/round-27/claims.json`, both counters, their red selftests and the before receipts in one commit, before any data. One pre-freeze REA probe (14:45:23Z, to check the tinyxxd address) is disclosed there and committed at `.ufo/waves/round-27/pre-freeze-probe/`.

- **R27-C1, depth (learning claim, sourced claim).** A 16-row evidence-ID identity table at `rea-agents@6.5.0`: 8 verbs on `/usr/bin/jq` and `/usr/bin/tinyxxd`, each with a base run, a same-path repeat and a byte-identical copy under another directory, file name and extension; plus a knowledge entry citing the table and a new SOURCES row. Target 16 of 16 rows, `entry_ok` 1. **Result: missed, 15 of 16 (honest stop).**
- **R27-C2, operability (fleet axis; capability acquisition).** `tools/round-27/xpin-attribute.mjs` attributes a saved REA envelope to the 6.5.0 id rule, the 6.7.0 rule, both or neither, using each installed package's own code; capability row in SCORECARD; new SOURCES code row for the 6.7.0 package (routed defect 1). Target 24/24, 3/3, rows 1 and 1. **Result: met.**
- Calibration is not claimed (Main session note 2); the 11 stale SCORECARD statements were worked as hygiene.

Work items:

- C1 counter `tools/round-27/c1-rename-identity.py` (sha256 `e0a07995…43bb7`, 22 selftest cases, 0 failures, `.ufo/waves/round-27/before/c1-selftest.txt`), committed before its data. New gates against the round-26 forgery class: envelope sha256 per run and all distinct, `.meta.command`, run path present and other path absent, `subject.name`, package version and `package.json` sha256 per call, each id recomputed under the 6.5.0 rule, and run start and envelope first commit no earlier than the counter's own commit.
- C1 data: 48 REA 6.5.0 CLI calls by eight executor seats, 14:54:51Z–14:56:43Z, all exit 0, version `6.5.0` and `package.json` sha256 `a5003023…50a6c` read after each call (`corpus/evidence/round-27/c1/runs.tsv`, `envelopes/`, `table.tsv`; seat reports `.ufo/waves/round-27/w1/Run*.md`), committed at `9dca26df`.
- C1 result: 10 content-keyed, 6 rename-sensitive, 0 unstable. `analyze` and `inspect` change id with the file extension: the only differing hashed leaf is `normalized_result.document` (`target-<sha256[0:12]>.bin` against `.dat`), the Ghidra program name built from the snapshot suffix rule (S083). The five address verbs keep their ids; `inspect-binary-layout` hashes the path. Two scouts predicted all 8 verb verdicts from the code without reading round-27 envelopes (`w1/PredictWholeFile.md`, `w1/PredictAddressVerbs.md`).
- C1 miss: the tinyxxd `inspect-binary-layout` base and repeat runs (14:55:49Z, 14:55:50Z, separate files) returned byte-identical envelopes (`meta.duration` `132ms` twice), and the frozen counter refuses shared bytes. The seat's later extra run was not substituted (decision recorded in `w1/RunTxD.md`; `w2/CriticC1HonestStop.md` checked it).
- C1 entry `corpus/knowledge/2026-10-22-r27-renamed-copy-evidence-id-identity.md`, with an appended corrections section after wave 2; SKILL.md section "Evidence-ID identity under a renamed copy and on a second carrier — round 27" plus appended corrections; README coverage-map, Knowledge and Known-gaps lines; PROVINCE.md dated section; pointer appended to `corpus/knowledge/2026-10-20-r17-go-carrier-diagnostics.md`.
- Wave-2 live falsification of the mechanism (REA 6.5.0 `analyze`): a name-only copy kept the base id, an extension-only copy (`jq.dat`) changed it, and a 13-character extension mapped to `.bin` and kept the base id (`w2/FalsifyExtensionOnly.md`, `w2/FalsifySuffixMapping.md`).
- C2 checker `tools/round-27/c2-xpin-check.py` (sha256 `d8de667f…09bd3`, selftest 6 cases incl. 5 row fixtures, 0 failures at freeze), committed before the tool. Tool built by executor `BuildXpinTool` (sha256 `8ea63837…7f708`), with a `--parse` mode using each package's own `parseEvidence`; receipts `corpus/evidence/round-27/c2/` (24 round-26 envelopes: 21 `6.5.0`, 3 `both`; 48 round-27 envelopes: 42 `6.5.0`, 6 `both`; 37 keyless lane records: default `both`, `--parse` 6.5.0 accepts 37, 6.7.0 rejects 37).
- Routed defects from `corpus/lessons/round-26-verifier-spotcheck.md`: (1) S081 code row for the 6.7.0 projection, and S083 for the 6.5.0 snapshot-naming code; (2) both counters committed before their data at `a4f674b3`; (3) the round-26 C1 counter and K6 rule are not reused; the new C1 counter gates on `envelope_sha256`, `.meta.command` and the run path; (4) `runs.tsv` records `pkg_version` and `pkg_json_sha256` per call; (5) the 11 stale SCORECARD statements got appended corrected readings (hygiene, not a claim; wave 2 found 8 of 11 wrong as first written, and the appended corrections say so).
- QUALITY rows 38 (instrument with red fixtures before its data), 39 (package version per call) and 40 (a forgery gate ships a green case for a legitimate duplicate), each judged on real round-26 and round-27 bytes.
- Mined mistakes: `corpus/lessons/round-27.md` `## Mistakes` M27-1 (round-26 instrument committed after its data; fix: the instruments-first freeze whose counter refuses earlier runs, shown failing on a real round-26 envelope) and M27-2 (this round's duplicate-bytes gate refused a genuine repeat; shown failing on the committed row).
- Freshness: `w1/FreshnessR26.md` re-ran two round-26 rows on `/usr/bin/jq` and got the same ids; both carriers' sha256 equal their pacman mtree records (S082); `w2/ScoutCarrierDrift.md` found no drift.

## Landed changes

| commit | what | LOG.md entry |
|---|---|---|
| `a4f674b343d8564e21f7eb8984630a95089c82d6` | freeze: claims, both counters, red selftests, before receipts | "round 27", Freeze line |
| `9dca26df135a2c558aaa575534ad42662b372d5d` | C1 data (48 envelopes, runs, table), integration script `tools/round-27/assemble-c1.py` (L1), pre-freeze probe envelope | Measured line |
| `c6d619a3c50e39dbb830de28146362e360d170d7` | C1 entry, SKILL.md section, README rows, SOURCES S081 and S082, round-27 lesson | Learned line |
| `97358f759a531f7ebc0354fb937d546da8d3b8bd` | C2 tool, receipts, capability row; README and PROVINCE lines; QUALITY rows 38-40 (measured revision) | Measured line |
| `4084d8975b684a8837b1c858eea0008ce9ab49e0` | SCORECARD round-27 section with hygiene, LOG entry, claim-freezes row, after receipts, wave-1 records and 33 seat reports | Hygiene line |
| `c4ec7a2e04889ed3a07fa1bd03550fbf467e0c19` | falsify-wave corrections (entry, SKILL, README, PROVINCE, r17 pointer, SCORECARD, lesson) | Wave 2 line |
| `29a76a637ad445f836b9b30382c0a6ee92a069a8` | S083 row, S079 `used-by`, further corrections, LOG wave-2 lines, wave-2 records and 28 seat reports | Wave 2 and Disclosure lines |

## Before → after measurements

| claim | counting command | before (at `cd32264f`) | after (at `97358f75`) | at tip `29a76a63` |
|---|---|---|---|---|
| R27-C1 | `python3 -I -B tools/round-27/c1-rename-identity.py --root <LANE> --rev <REV>` | `rows_complete=0/16 entry_ok=0`, exit 1 (`.ufo/waves/round-27/before/c1-at-cd32264f.txt`) | `rows_complete=15/16 entry_ok=1`, exit 1 (`.ufo/waves/round-27/after/c1-at-97358f75.txt`) | same, exit 1 |
| R27-C2 | `python3 -I -B tools/round-27/c2-xpin-check.py --root <LANE> --rev <REV>` | `r26_rows_ok=0/24 red_ok=0/3 capability_row=0 source_row=0`, exit 1 (`before/c2-at-cd32264f.txt`) | `r26_rows_ok=24/24 red_ok=3/3 capability_row=1 source_row=1 (S081)`, exit 0 (`after/c2-at-97358f75.txt`) | same, exit 0 |

Re-derived by wave-2 seats: `w2/RecountC1.md`, `w2/RederiveC1Own.md` (own Node script with each package's own code: all 16 verdicts re-derive, exactly one row fails, only on the shared-bytes rule), `w2/RecountC2.md`. `tools/round-26/recompute-ids.py`, which the C1 counter loads unpinned, is byte-identical at base and `97358f75` (`after/recompute-pin.txt`). Width disclosures: "At rea-agents@6.5.0" rests on the invocation and the per-call `package.json` read; the C2 checker does not count the tool's exit code and cannot see a retyped projection (`w1/CriticClaimWidth.md`, `w1/ReviewC2Checker.md`, `w1/MutC2Checker.md`); the C2 selftest's `correct-stub` case exits 1 from `97358f75` on because it was anchored to the pre-row state (`w2/RecountC2.md`). Freeze ledger: `corpus/claim-freezes.tsv` row `round-27` FLAGGED `INSTRUMENT_ABSENT,INSTRUMENT_REVISED,INSTRUMENT_UNPINNED` (the C2 product tool absent at freeze by design; the recompute file unpinned), matching `freeze-gate.py`; its "sha256-pinned" wording covers only the two counters (`w2/ReviewFreezeRow.md`).

## Sources & frontier

- Census command `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kaidoku`: round start exit 0 (five W04 warnings S033, S047, S054, S062, S069, `kaidoku ok`); round end exit 0 (the same five plus W04 S083, whose tarball URL is shared with S079, `kaidoku ok`).
- Rows 80 → 83 (`git show <REV>:corpus/SOURCES.md | grep -cE '^\| S[0-9]{3} \|'` at `cd32264f` and `29a76a63`). Added by tier: tier A 3 (S081 code, 6.7.0 installed package and tarball; S082 dataset, tinyxxd pacman and Arch records; S083 code, 6.5.0 snapshot-naming runtime, `GhidraTargetSnapshot.js` and the bridge line). Rejected rows: none.
- Rows touched old → new: S079 `used-by` `corpus/knowledge/2026-10-22-r26-native-reader-evidence-id-identity.md, corpus/lessons/round-26.md` → that plus `corpus/knowledge/2026-10-22-r27-renamed-copy-evidence-id-identity.md, corpus/lessons/round-27.md` (logged in the lesson).
- Gate: `corpus/lessons/round-27.md` `## Gate`, with corrections after wave 2 (Arch page quotes are rendered-text composites and the page hash carries a CSP nonce; the JSON quote has a space after the colon; search-log counts corrected: 6 identified and screened, 5 included in 3 rows, 1 excluded). Re-opened by `w2/ReopenS081.md` (holds), `w2/ReopenS082.md`, `w2/ReopenS079Snapshot.md`, `w2/ReviewGate.md`.
- Sourced claim: R27-C1's entry cites S082 (counted by its `entry_ok` gate) and S083; R27-C2 rests on S081 (counted by `source_row`).
- Frontier: no `PROVINCE.md` Frontier bullet moved to Core. Core gained a dated round-27 section; README Known gaps gained round-27 sub-bullets. The round-26 spot-check's one disagreement (the S037 family decision) is reversed and recorded (QUALITY row 36 pointers in the lesson and the SCORECARD corrections).
- Sibling source routed by Main (tameshi `mte-report-interop.md@f4e8f7d8`): read by `w1/SiblingOverlap.md`; not opened as a SOURCES row (no claim uses mutation-tested gates as its basis).

## Trend verdicts

- **expansion: improved.** Ground the lane did not hold: the extension effect on `analyze` and `inspect` ids, a second carrier, and cross-pin attribution; knowledge 109 → 110 (recipe A 110/110 at `97358f75`), SOURCES 80 → 83, one capability row.
- **quality: improved.** The round-26 rule "seven verbs content-keyed across directories" is narrowed with a mechanism from code, live separation of name and extension, and appended pointers in SKILL.md, README and the r17 entry; QUALITY rows 38-40 are new criteria judged on real bytes; freshness re-run reproduced two round-26 ids. R27-C1's own target was missed and is reported as such.
- **discernment: unchanged.** Gains: the round-26 spot-check disagreement is learned (S081, S083), the C1 miss is reported without substitution, and two mistakes are mined with real-byte failures. Offsetting: 8 of the 11 hygiene corrections landed with wrong counts or framing and needed appended corrections from wave 2 (`w2/ReviewHygieneLanded.md`, `w2/CriticNoCalibrationClaim.md`).

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — `SKILL.md:81-314` (17/17 rule blocks, recipe A at `97358f75`); round-27 section appended at the end of SKILL.md.
- [~] At least one end-to-end domain task executed and logged in LOG.md — `corpus/lessons/2026-10-15-round-1.md`; round 27 adds 48 logged REA CLI calls (`corpus/evidence/round-27/c1/runs.tsv`).
- [~] Instructions executable by an agent without oral context — historical round-1 recipe; round-27 recheck lines in the entry.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — `PROVINCE.md:95-116` unchanged; round 27 appended only after line 303.

## Round shape, seats and conformance

- Shape: default, two v1 waves. Wave 1 (build plus first falsifiers): 33 seats — executor 10, scribe 7, reviewer 5, mutation-tester 5, critic 3, scout 2, connector 1; attack 13 (39%); all 33 returned, 33 reports (`.ufo/waves/round-27/w1/`). Wave 2 (falsify): 34 seats — reviewer 20, critic 6, mutation-tester 6, scout 2; attack 32; 28 returned, 28 reports (`.ufo/waves/round-27/w2/`). Round total 67 seats; attack roles 45 of 67 (67%). No residual call.
- Dead seats (6 of 34 in wave 2, 17.6%): `MutQualityRow38`, `MutQualityRow39`, `MutQualityRow40`, `MutXpinTool`, `MutLessonM27`, `MutC1DupGate`, each with last error text "Error: No model selected. Use /login, set an API key environment variable, or create /home/vgpnk/.omp/agent/agent.db". Not replaced or rerouted (Main route notice 15:40Z: the `@m_mim` route degraded from 15:14Z).
- §3 L2 floor met in wave 1 (connector, 10 executors, scribes, scouts, reviewers, critics). Planner seat: held by the L1 (frozen-topology seat); planning data-walk rode the scouts `PredictWholeFile` and `PredictAddressVerbs` and the connector.
- Seat gate: w1 `granted lane=kaidoku wave=w1 seats=33 live=17` at 14:54:22Z, released after all 33 returned; w2 `granted … seats=34 live=51` at 15:34:58Z after a 1009 s wait, released after all 34 settled. Each wave was one `task` call; the only change to the validated payload was one `solutionSpace` string per task (recorded in `w1-task-result.json`, `w2-task-result.json`). No refusal.
- Integration owner: the L1; seats wrote only their reports in the lane and artifacts under `/fast/scratch/hyaku/kaidoku-r27/`. `tools/round-27/assemble-c1.py` was written by the L1. Five wave-1 seats ran plain `git status` in the lane, which can rewrite `.git/index`; no tracked content, ref or commit changed (`w2/ReviewRoundShape.md`). No cancelled seat; `git status --porcelain` in the lane is empty at filing.
- Misroot sweep: `git -C /home/vgpnk/Projects/shokunin status --porcelain -uall` shows no round-27 kaidoku file at the fleet root (untracked `live_s228.html`, `tf_bavelas.html` and `write` contain no kaidoku text and are not this lane's); `w2/MisrootSweep.md` agrees.
- Inherited state: none; the lane was clean at base. Files not authored by this round (`corpus/lessons/round-26-verifier-spotcheck.md`) were read, not edited.
- Stale-lane: respawn-per-round driver; no other mission of this lane is open.
- Tool installs: none by the L1 or any seat (each seat report says so). Host pacman untouched.
- Open L0 questions: none from this lane.
- Next planned move (SCORECARD round-27 corrections list): coverage on the `PROVINCE.md` Frontier bullet "EVM bytecode (extended)", with counter and red and green selftests before any data; a third evidence-ID round would trip the session drift sentinel.
