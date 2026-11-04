# mori round 86 — report

lane: mori-shokunin · round 86 (attempt 1) · date 2026-11-04 · L1 `MoriR86`
entering revision: `fec2b328a4c83e0c61bc09d70e254ca47d547d34` (branch `master`, pushed, clean)
freeze commit: `5e80229a450fa007d73ad0fb8bc3147e4adf5438` · pre-data amendments A1 `98d15d8f`,
A2 `c2bfded0`, each disclosed in `.ufo/waves/round-86/contract.md` · landing commit (the two
subject files) `87644619078308ee523cd0c976c72bf079b0ff77` · receipt commit
`50d80df0b02e57642a71091d29978da7f231c9dd` · C3 target-enforcement fix
`b0aa564ca0dec352a9b42d5d74ecba9bdaab3d7f` · after receipt (re-measured there) `6e77fe0e6bd4e71156276fe46880c758df0fc000`
(first after evidence `8b4b4ad7f4b1b8a924b6b831fb9f8f3361847c8d`) · docs commit `095bd1f6d90460267666a7642aa987a9a7d03c5f` · final lane tip
`6e77fe0e6bd4e71156276fe46880c758df0fc000` (pushed; `ls-remote origin refs/heads/master` prints it; wave settlement
`w1-results.json` committed at `6e77fe0e6bd4e71156276fe46880c758df0fc000`)

## Work performed

Declared claims (frozen in `.ufo/waves/round-86/contract.md` before any seat ran; two pre-data
amendments, each disclosed in the contract):

- **C1 — operability (7):** the six surviving r85-C3-counter mutants the r85 mutation probe measured
  (`H-C3-metverdict`, `C3-01-rc-range`, `C3-02-rc-dropped`, `C3-03-order`, `C3-04-agreed-skip`,
  `C3-07-subject-tokens`) get the failing arm each needs in `.ufo/waves/round-85/count-c3.py`,
  taking its selftest 20 → 26 arms. Target `C1=met mutants=6 killed=6 survivors=0 total=6 arms=26`.
- **C2 — calibration (5, tied lowest):** each `# replay: required` receipt's body is bound to its
  command — the replay pass executes `# cmd:` in a scratch export of the receipt's own `# rev:` and
  compares stdout to the body modulo trailing newlines; two r86 receipts (one a stale-body defeat)
  join the three header-bound r85 receipts. Target `C2=met receipts=5 bindings=7 bound=7 revs=5
  limits=5 cmd=5 summary=5 replay=2 matched=4 defeated=1 legacy=3 unexpected=0`.
- **C3 — depth (5, tied lowest; capability acquisition):** `.ufo/waves/round-86/count-c3.py`
  observes the census twice through two surfaces (drift token line; full report's values) and
  reconciles the r82 classification's 14 bare-key `value-changed` rows with a value channel. Target
  `C3=met observations=2 aa=stable tokens=64 derived=64 name_agree=64 value_rows=14
  contradicting=2`.

Work items and evidence:

- **Contract, three counters, do-nothing controls (L1, freeze `5e80229a`).**
  `.ufo/waves/round-86/contract.md`, `count-c1.py`, `count-c2.py`, `count-c3.py` and
  `evidence/controls-r86.txt` froze the three predicates before any seat ran. Entering controls: C1
  `C1=unmet mutants=4 killed=0 survivors=4 total=4 arms=20 subject=arms` rc 1 (two anchors absent,
  the other four survivors); C2 `C2=unmet subject=stub
  missing=replay_match,replay_stale_mismatch,replay_none_requires_reason` rc 1; C3 has no reading at
  the entering revision (the counter file is absent — `git cat-file -e` rc 128) and the counter
  applied retroactively there reads `C3=met ... rev=fec2b328a4c8`, disclosed as a capability
  reading, not a before value. The C1 label-only stub control (six `PASS` labels,
  `C3_COUNTER_SELFTEST pass=26 fail=0`, no assertions, the six anchors as inert comments) reads
  `C1=unmet mutants=6 killed=0 survivors=6 total=6 arms=26` — labels alone are not the work.
- **C1 arms (seat `Mo86E01C1Arms`, completed by the L1).** `.ufo/waves/round-85/count-c3.py` at
  `87644619`: `stability(rcs, token_lines)`, `subject_ok(rc, fields)` and
  `met_verdict(...)` extracted, `observe_three`/`main` wired to them, six arms added; the six frozen
  anchors occur exactly once each and the live `main` path is unchanged (`C3=met observed=3 aa=stable
  own_tokens=64 subject_tokens=64 subject_deltas=0 unmatched=0 unnamed=0`, measured at `98d15d8f`).
  Each mutated copy's own selftest reads `pass=25 fail=1` rc 1 (`evidence/after-r86.txt`).
- **C2 replay (seat `Mo86E02C2Replay`, one-line fix by the L1).**
  `.ufo/waves/round-85/count-c2.py` at `87644619` parses `# replay: required|none` and
  `# no-replay:`, exports every repo-relative path its `# cmd:` names at the receipt's own `# rev:`,
  runs the command there with `GIT_CONFIG_GLOBAL=/dev/null`, and compares stdout to the body; the
  five-receipt population carries per-receipt expectations and the three r85 receipts stay
  `legacy` under a named limit; selftest 18 → 21 arms. The two receipts are written by
  `.ufo/waves/round-86/make-receipts-r86.sh <rev>` (`evidence/after-c1-r86.txt` and the stale-body
  `evidence/replay-defeat-r86.txt`). Replay at the measured revision prints `REPLAY
  after-c1-r86.txt rc=0` / `REPLAY replay-defeat-r86.txt rc=0` and the defeat receipt reads
  `problems=replay-mismatch` (`defeated=1`) while its headers, its `# rev:` and its
  `# counter-sha256:` (`1912e87d…`) all verify — the stale-body limit is the control the claim
  closes.
- **C3 value channel (L1 counter; seat `Mo86E03C3Value` controls).**
  `.ufo/waves/round-86/count-c3.py` runs the census twice through each surface, requires exact-order
  token stability and volatile-filtered atom stability, derives every stated class by the r83 name
  rule, and prints one `VALUE <token> <verdict>` line per bare-key `value-changed` row. The real run
  prints 14 `VALUE` lines; `-subject_commits` (`yes`) and `-window` (`launch..NOW`) read `equal`, so
  `contradicting=2`. `evidence/c3-value-controls.txt` drives every verdict
  (`equal`/`differs`/`masked`/`absent`) and both stability legs to their observed state with minimal
  fixtures, each run reading `C3=unmet` for the frozen floors and the reason named.
- **Sources and lesson (seats `Mo86S02Sources`, `Mo86S01Lesson`).** S602 (in-toto Specification
  v1.0.0) opened, pinned twice byte-identically and quoted; `corpus/knowledge/execution-evidence-r86.md`
  (K1–K3, `source: S602`) and the coverage-map row landed; the lesson mines the r85
  `predicate-underreach` class with a rebuilt one-byte-stale fixture and a Gate block recording the
  admit.
- **Recon and sibling scan (seats `Mo86Sc01Scout`, `Mo86K01Conn`).** The scout mapped every consumer
  of the three changed surfaces and named three landing risks (R1 helper-name coupling, R2 the
  subject's `--scratch`, R3 the `first` anchor) — R1/R2 became contract A1; R3 is the intended
  after-form anchor. The connector found no lane that replays a receipt's command, cited tsukuroi's
  five-class adjacency vocabulary as the fleet precedent for overlap classification, and recorded
  chousa's named limit ("a digest that re-derives proves the bytes are committed, not which command
  produced them") as the C2 rule's motivating gap.
- **Mutation probe (seat `Mo86M01Mut`; ended before its report).** Its last output, preserved at
  `.ufo/waves/round-86/evidence/mutation-r86.txt`, carries the 48-spec matrix (47 run, 1 refused by
  contract A1, 23 killed, 24 survived, 3 equivalent-by-coupling) and the confirmed end-to-end flips
  (M1-08 arms plumbing, M1-12 fail floor, M3-01 `value_rows`, M3-03 volatile drop, M3-06 name-agree,
  M3-10 malformed, M3-16/M3-19). Its finding 1 (a `SyntaxError` in `count-c2.py`) measured a
  mid-edit worktree snapshot, not committed bytes — no commit carries it and `98d15d8f` and later
  parse and run `pass=11`; finding 3 (the C3 counter's docstring said `value_rows=19` and its
  `TARGET` was never compared) was real and is fixed at `b0aa564c`, which is why the after receipt
  was re-measured there.

## Landed changes

Every change is a LOG.md Round-86 entry item and lands at the commit named beside it.

| change | commit |
|---|---|
| Round-86 contract, three counters, measured do-nothing controls (`contract.md`, `count-c1.py`, `count-c2.py`, `count-c3.py`, `evidence/controls-r86.txt`) | `5e80229a450fa007d73ad0fb8bc3147e4adf5438` |
| Wave w1 spec, validated dispatch (12 seats) and the ready handoff | `4eab48c0f721e5917f7611d51561894873a21ea4` |
| Routed-defect corrections from the r85 spot-check (LOG `<fill>`, control rc lines, r85 A4 errata) | `57104423a12a859cac7ac249c683b3a37d77fbe5` |
| Contract A1 (`--scratch`, label-only stub guard) and the C2 counter's stub guard | `98d15d8f784e55d979b84273aafb45225b8b8ccc` |
| Contract A2 (subject-line prefix, fleet-root limit) and the C2 counter's prefix check | `c2bfded0d25564d689282e3cbe462c8f043139bf` |
| Six C3 arms + the replay-enabled C2 subject + the receipt generator | `87644619078308ee523cd0c976c72bf079b0ff77` |
| The two replay receipts (`after-c1-r86.txt`, `replay-defeat-r86.txt`) and the generator's path guards | `50d80df0b02e57642a71091d29978da7f231c9dd` |
| After receipt (all three frozen targets) and the defeated-controls receipt | `8b4b4ad7f4b1b8a924b6b831fb9f8f3361847c8d` |
| SCORECARD round-86 section + capabilities + planned 87, LOG Round 86, QUALITY 177–180, PROVINCE round-86 notes, corpus/README row, SKILL registry row 20, S602 row, knowledge entry, lesson | `095bd1f6d90460267666a7642aa987a9a7d03c5f` |

No path was deleted. Line deletions occur only where code was replaced rather than added: the two
inline expressions in `.ufo/waves/round-85/count-c3.py` (`stable = (...)`, the `main` gate and the
met conjunction) become helper calls (6 lines), and `.ufo/waves/round-85/count-c2.py`'s
`parse_receipt`/`grade` are replaced by the replay-aware versions plus the stale `present` loop
(110 lines). The r85 contract (1 line) and `controls-r85-entering.txt` (2 lines) carry the routed
errata. Every other path in `git diff --numstat fec2b328 6e77fe0e6bd4e71156276fe46880c758df0fc000` is additions only.

## Before → after measurements

One per claim, each with the counting command and the revision measured.

| claim | counting command | before | after (at `b0aa564ca0dec352a9b42d5d74ecba9bdaab3d7f`) |
|---|---|---|---|
| C1 | `python3 -I .ufo/waves/round-86/count-c1.py <rev> --scratch <dir>` | at `fec2b328`: `C1=unmet mutants=4 killed=0 survivors=4 total=4 arms=20 subject=arms` rc 1 | `C1=met mutants=6 killed=6 survivors=0 total=6 arms=26` rc 0 |
| C2 | `python3 -I .ufo/waves/round-86/count-c2.py <rev> --scratch <dir>` | at `fec2b328`: `C2=unmet subject=stub missing=replay_match,replay_stale_mismatch,replay_none_requires_reason` rc 1 | `C2=met receipts=5 bindings=7 bound=7 revs=5 limits=5 cmd=5 summary=5 replay=2 matched=4 defeated=1 legacy=3 unexpected=0` rc 0 |
| C3 | `python3 -I .ufo/waves/round-86/count-c3.py <rev> --scratch <dir>` (`--fleet-root` off a `-shokunin` path) | counter file absent at `fec2b328` (`git cat-file -e` rc 128); retroactive reading `C3=met ... rev=fec2b328a4c8`, disclosed | `C3=met observations=2 aa=stable tokens=64 derived=64 name_agree=64 value_rows=14 contradicting=2` rc 0 |

The after receipt is `.ufo/waves/round-86/evidence/after-r86.txt` (three commands, three `rc=` lines,
`# counter-sha256:` bindings for the three counter bytes at the receipt's own revision). The three
counters' own selftests read `C1_COUNTER_SELFTEST pass=15 fail=0`, `C2_COUNTER_SELFTEST pass=11
fail=0`, `C3_COUNTER_SELFTEST pass=22 fail=0`; the two graded subjects read `C3_COUNTER_SELFTEST
pass=26 fail=0` and `C2_COUNTER_SELFTEST pass=21 fail=0`. C3 was stable across four independent
invocations at three different revisions (each `aa=stable`, `contradicting=2`).

## Sources & frontier

`corpus/SOURCES.md` rows **374 → 375** by
`grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md` (374 at the freeze
commit, 375 at the worktree after the append); one row added, tier A (`spec`), status `mined`,
`used-by corpus/knowledge/execution-evidence-r86.md`; no existing row's `status`/`recheck`/`used-by`
cell moved. Census before (`--root` at round start, pre-append) and after (at the worktree bytes):
`mori ok …/corpus/SOURCES.md`, rc **0** both times, 35 tolerated `W04` duplicate-URL warnings both
times, zero `E` codes. Rows added by tier: 1 × tier A. Rows touched old→new: none. Frontier rows
advanced: none — S602 grounds the r86 C2 rule but no `PROVINCE.md` frontier row moves (the coverage
map row cites it under calibration).

The row, opened and re-opened this round: **S602 — in-toto Specification v1.0.0**,
`https://raw.githubusercontent.com/in-toto/docs/v1.0/in-toto-spec.md`, HTTP 200, no redirect, two
fetches byte-identical, sha256 `17d3326e4cf58234619dbfe821cdc5187e55e2c89f7b63f03699c46588322097`,
87108 bytes, 2217 lines, pin `.ufo/waves/round-86/evidence/sources-r86/in-toto-spec-v1.0.md`;
accessed 2026-11-04; located quote at raw lines 1063-1064 (9 words): *"Byproducts are not verified
by in-toto’s default verification routine."* The gate records one admit (S602) and no reject; the
screening that excluded six candidates is the opener's measurement, cited as such.

`Assimilation: none` — no `merge/mori/` adoption this round; the package was not opened.

## Trend verdicts

- **expansion: improved.** One admitted knowledge entry on ground the coverage map did not hold
  (`corpus/knowledge/execution-evidence-r86.md`, execution evidence: recorded ≠ verified), its
  `source:` citing S602 — a row opened, pinned twice and quoted this round — plus the coverage-map
  row and the three capability rows. Registry 374 → 375, census rc 0, append-only.
- **quality: improved.** Six named mutants each killed behaviourally by an arm in the graded bytes
  (not by a label), a replay gate that executes a receipt's command and rejects a stale body with
  correct headers and digests, and a value channel that drives all four verdicts and both stability
  legs from minimal fixtures; the record and claim sweeps are green at the measured revision
  (`revisions=0`, `mismatches=0`), the pin check is unchanged at 4 stale pins (r19's, stale at
  entering), and the three counters gate their own detectors in the same invocation.
- **discernment: improved.** The round mines its own r85 `predicate-underreach` class with a
  measured fixture, closes the r85 spot-check's four record defects, and — the sharpest move — the
  C3 value channel contradicts two of the classification's own `value-changed` labels and names them
  instead of relabelling the frozen file. The counter's own named limits (legacy receipts, live
  value counts, `--fleet-root` off a `-shokunin` path) are stated in the contract and the report.

## SHONEN

One line per box of `SHONEN.md`; no `[x]` is written (promotion is operator-owned and no named
non-author verifier has judged these boxes this round).

- [~] SKILL.md decision tables, error patterns, checklists, cited sources — `SKILL.md` registry row
  20 (r86 counters, generator, targets and selftests at `b0aa564c`) appended after row 19; QUALITY
  177–180 (`corpus/QUALITY.md`, this round); the knowledge entry's K1–K3 and Gate block.
- [~] At least one end-to-end domain task executed and logged — `LOG.md` Round 86 (three claims with
  measured before→after, the arms, the replay receipts, the value channel, the dead seats);
  `evidence/after-r86.txt` carries the three target lines.
- [~] Instructions executable by an agent without oral context — `python3 -I
  .ufo/waves/round-86/count-c1.py --selftest` → `pass=15 fail=0`; `count-c2.py --selftest` →
  `pass=11 fail=0`; `count-c3.py --selftest` → `pass=22 fail=0`; the contract's P-C1/P-C2/P-C3
  sentences name their counters, revisions, targets and controls; the generator's usage line is in
  its header.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — `PROVINCE.md` round-86 notes (three core
  rule changes, no census surface, no threshold, no remediation); the connector's sibling scan found
  adjacent rules in kama/kengaku/chousa/tsukuroi and absorbed nothing; the lane's rea/dispatch and
  OS-state boundaries are unchanged.

## Round shape and hygiene

One v1 wave under `scripts/hyaku/ufo-wave-policy.json` (band 8–16): 12 seats
(`w1-dispatch.json` counts `{spawn: 12, resume: 0, total: 12}`), roles 4 executor / 2 scribe / 1
scout / 2 reviewer / 1 critic / 1 mutation-tester / 1 connector; attack share 4/12 = 33.3 %;
1 connector seat. No residual call. **Dead seats (8, provider usage limit):** `Mo86E01C1Arms`
(wrote two helpers; L1 completed the third, the wiring and the six arms from the seat's plan),
`Mo86E02C2Replay` (wake turn: `429 Usage limit reached for 5 hour`; wrote the full replay subject and
generator; L1 fixed one 4-tuple unpack and the generator's last-line guard and `LANE` depth),
`Mo86E03C3Value` (landed `evidence/c3-value-controls.txt`, no report), `Mo86E04Controls` (died before
its battery receipt), `Mo86R01ReviewC1`, `Mo86R02ReviewC2`, `Mo86C01Critic` and `Mo86M01Mut` (died mid-work; the probe's
last output is preserved but its report was never written — their attacks are not replaced by the
L1). **Landed seats (4):** `Mo86S01Lesson`,
`Mo86S02Sources`, `Mo86Sc01Scout`, `Mo86K01Conn`, `Mo86M01Mut`. No dead seat was replaced.

Scratch: every seat worked under `/fast/scratch/hyaku/mori-r86/<seat>/`; the L1's own trees
(`probe/`, `ref/`, `stub/`, `c2ref/`, `c2gate/`, `dryrun/`, `c1test/`, `census/`) are under the same
root and are removed after landing. No committed tool hardcodes `/tmp`; the counters honour
`--scratch`/`TMPDIR` and the generator honours `TMPDIR`.

Misroot sweep: `git -C /home/vgpnk/Projects/shokunin status --porcelain` shows no file written by
this lane's seats — only orchestrator `.scratch/*` run state, `.ufo/l0-questions.md` (another lane's
append) and the pre-existing `after` file. Nothing to move.

Stale-lane: respawn-per-round driver; no other mission of this lane is open.

Tool installs: none (no tool was installed or upgraded this round; nothing was needed).

## L0 questions

None opened by this round.
