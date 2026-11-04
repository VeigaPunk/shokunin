# mori round 85 — report

lane: mori-shokunin · round 85 (attempt 1) · date 2026-11-04 · L1 `MoriR85`
entering revision: `2cc4b1ae35a83e4fd3fc48bae842bdf38df2e80e` (branch `master`, pushed, clean)
freeze commit: `ab2608655ea52ba6d151b3a31d69a3b18cd2b41e` · pre-data amendments A1 `79bb4ed8`,
A2 `4ffd5a2d`, A3 `89f82eac`, A4 `91f657f6` · post-data text fix A5 (in `42865833`)
code/landing commit: `25a74d4c34e8430e4fbb18d4038ef5db872fb0ee` · receipt/prose commit
`42865833c9b9f9bdd33b6c3d13641bebfc66efd2` · final lane tip
`1b733457220ee9ed698f9c537ce46a380cbe5375` (pushed; `ls-remote origin refs/heads/master` prints it)

## Work performed

Declared claims (frozen in `.ufo/waves/round-85/contract.md` before any seat ran; five amendments,
each disclosed in the contract and the round lesson):

- **C1 — operability (7):** the two surviving counter mutants the r84 C1 reviewer measured
  (`.ufo/waves/round-84/w1/Mo84R01C1.md` §5, X1/X2) get the failing arm each needs
  (`killed_mutant_with_coupling_not_equivalent`, `duplicate_coupling_not_equivalent`), taking the
  r84 counter's selftest 15 → 17 arms. Target `C1=met mutants=2 killed=2 survivors=0 total=2
  arms=17 r84=met`.
- **C2 — calibration (5, tied lowest):** every after receipt binds its command, its graded revision
  and the sha256 of each subject's bytes at that revision; the three frozen receipts and the
  `make-receipts.sh` generator are graded by `count-c2.py`. Target `C2=met receipts=3 bindings=5
  bound=5 revs=3 limits=3 cmd=3 summary=3 mismatch=0`.
- **C3 — depth (5, tied lowest; capability acquisition):** `count-c3.py` observes the census itself
  three times from R's own bytes and reconciles the r83 subject's live reading with its own
  observation. Target `C3=met observed=3 aa=stable own_tokens=N subject_tokens=N unmatched=0
  unnamed=0`.

Work items and evidence:

- **Contract, three counters, population controls (L1, freeze `ab260865`).**
  `.ufo/waves/round-85/contract.md`, `count-c1.py`, `count-c2.py`, `count-c3.py` and
  `evidence/controls-r85.txt` froze the three predicates before any seat ran. Entering controls: C1
  `C1=unmet mutants=2 killed=0 survivors=2 total=2 arms=15 harness=stub missing=killed_mutant_with_coupling_not_equivalent,duplicate_coupling_not_equivalent rev=2cc4b1ae35a8`
  rc 1; C2 `C2=unmet receipts=0 harness=absent rev=2cc4b1ae35a8` rc 1; C3 has no reading at the
  entering revision (the counter file is absent — `git cat-file -e` rc 128), and the counter
  applied retroactively there reads `C3=met ... rev=2cc4b1ae35a8`, disclosed as a reading, not the
  before value.
- **Pre-data amendments A1–A4 (L1).** A1 `79bb4ed8`: C2 verified a receipt's digest at the graded
  tip instead of at the receipt's own `# rev:` — fixed before any after value. A2 `4ffd5a2d`: the
  connector's clause sweep (`w1/Mo85K01Conn.md` §2) drove five clarifications — the header block is
  everything before the single `# ---` (a header-shaped body line is body text), header lines
  match loosely so a second malformed `# rev:` cannot vanish, a malformed `# counter-sha256:` is a
  `malformed-binding` problem and still counts as a binding, `# limits:` must carry the word `limit`
  and at least three words, and the C3 tail/entering-control text names the exact fields. A3
  `89f82eac`: C3 requires the subject's `C2=met` verdict, not merely rc 0. A4 `91f657f6`: the
  contract's C3 entering control states the counter file's absence instead of a line the counter
  cannot print. No predicate, target value, receipt, class or kill rule changed after data.
- **C1 arms (seat `Mo85E01C1Arms`; the L1 stood in from a validated scratch prototype while the
  seat's registration was stale, and the seat's own append then duplicated the two arms — the
  collision, its restore and the seat's independent verification of the restored bytes are in
  `w1/Mo85E01C1Arms.md` §0–§2).** `.ufo/waves/round-84/count-c1.py` `selfcheck()` gains the two
  arms (`killed_mutant_with_coupling_not_equivalent`, `duplicate_coupling_not_equivalent`), 15 → 17
  arms, +29 lines, `grade()`/`green()`/`killed()` untouched. The prototype was measured in
  scratch: pristine `C1_COUNTER_SELFTEST pass=17 fail=0`; X1 mutant `FAIL
  killed_mutant_with_coupling_not_equivalent ... C1_COUNTER_SELFTEST pass=16 fail=1` rc 1; X2
  mutant `FAIL duplicate_coupling_not_equivalent ... pass=16 fail=1` rc 1; the armed counter at
  that scratch revision printed `C1=met ... arms=17 r84=met` while the r84 counter still printed
  `C1=met mutants=4 killed=2 equivalent=2 survivors=0 total=4 pristine=green detector=green`.
  Named limit (A2, the met path as written): the two arm labels are bound in the subject's BYTES
  plus a green pristine selftest with exactly 17 passing arms — an arm whose name is present but
  whose assertion is vacuous is the mutation probe's finding, not a met-path clause. Provenance of
  the population (A5): the r84 reviewer's §5 table records X2 against the r83 spelling
  (`coupled = base.count(coupling) == 1`, r83 `count-c1.py:177-178`); the r85 counter re-pinned the
  same survival semantics to the refactored r84 line (`coupled = all(base.count(marker) == 1 for
  marker in coupling)`) and both mutants were re-measured surviving at the entering revision
  (`w1/Mo85R01C1.md` §1, `w1/Mo85C01Critic.md` §5.4).
- **Receipt generator and grammar (seat `Mo85E02Receipts`).**
  `.ufo/waves/round-85/make-receipts.sh` (sha256 `7fd5e043…`, 7681 bytes) writes the three frozen
  receipts with the `# receipt/# cmd/# rev/# counter-sha256/# limits/# ---` header block and one
  `rc=<n>` line per body; the seat re-proved the met direction (`C2=met ... bound=5 ... mismatch=0`
  rc 0 at a committed receipt set), the stale-digest control (`C2=unmet ... bound=4 mismatch=1` rc
  1), a headerless receipt (`C2=unmet ... mismatch=7` rc 1) and `parse_receipt` problems `[]` on all
  three generated receipts (`w1/Mo85E02Receipts.md`). The after receipt's `# counter-sha256:` lines
  pin the post-A3 counter bytes at `25a74d4c` — the bytes that produced the after values (A1–A3
  predate the landing; A5 records it). The `# cmd:`/`# rev:`/`# limits:`/summary checks are
  receipt-SHAPE checks; the acceptance reading of `C1=met` in `after-r85.txt` is corroborated by
  the live counter runs quoted below, never by the receipt alone. The frozen shorthand
  `C2=unmet headers=<receipt>` is superseded by the measured A2 form `C2=unmet ... mismatch>=1`
  (A5).
- **C3 observation controls (seat `Mo85E03C3Fixture`).** `evidence/c3-controls.txt`: the
  census-stub fixture (`786aab60`) reads `C3=unmet observed=3 aa=unstable own_tokens=0 rcs=1,1,1`;
  the stale-subject fixture (`409de5e8`) reads `C3=unmet ... own_tokens=64 subject_tokens=63
  unmatched=0 unnamed=0`; the pristine anchor (`f2efbfcb`) reads the met line — a single-difference
  proof that the token-count reconciliation is load-bearing.
- **Defeat controls and the battery header (seat `Mo85E04Controls`).**
  `evidence/controls-r85-defeated.txt`: the pre-arm C1 reads unmet (arms=15), the armed copy reads
  `C1=met ... arms=17 r84=met`; the stale-digest receipt reads `C2=unmet ... bound=4 mismatch=1`
  rc 1 and a headerless receipt `C2=unmet ... mismatch=7` rc 1; the fresh census-stub fixture reads
  `C3=unmet observed=3 aa=unstable own_tokens=0 rcs=1,1,1` rc 1.
  `evidence/battery-r85.txt` carries the D84-5 header (`# battery run at rev=4ffd5a2d date=…`) and
  the r84 command list verbatim: `BATTERY pass=57 setup=4 fail=0`, `BATTERY 57/61`.
- **Source pin and screening (seat `Mo85Sc01Source`).** Three byte-identical pins of
  `https://reproducible-builds.org/docs/definition/`
  (`corpus/evidence/sources-r85/rb-definition-{1,2,3}.html`, sha256 `a558c89f…`, 37681 bytes, 3662
  lines); the definition span at raw lines 175-177 (21-word located quote) and the verification
  sentence at 196-197; two screened exclusions with reasons; the r84-refused arXiv:2404.09241
  re-opened byte-identically and read `no flip`.
- **Registry rows, knowledge entry and lesson (seat `Mo85S01Lesson`).**
  `corpus/SOURCES.md` +2 rows — S600 (`docs`, tier A, `mined`) and S601 (`paper`, tier A,
  `rejected`; D84-3 discharged) — rows 372 → 374; `corpus/knowledge/receipt-provenance-r85.md`
  (K1–K3, cites S600); `corpus/lessons/round-85.md` with the mined `number-drift` +
  `reference-drift` mistake (the r84 D84-2 stale tally and the moved `:296-300` pointer), the Gate
  (one admit, one reject, each with URL, access date and a ≤25-word located quote), the census
  before→after (372 → 374, rc 0 both, 35 tolerated W04 warnings) and the `considerthese` line
  (`considerthese/2026-10-26.md` suggestion 3 → the receipt rule).
- **QUALITY and the gate registry (seat `Mo85S02Quality`, L1 row 176).** `corpus/QUALITY.md` 173
  (a quoted tally is re-run at the bytes its pointers name; supersedes 172's stale tally and moved
  pointer — D84-2), 174 (an arm is run against the unarmed subject first), 175 (a receipt states
  its own limit) and 176 (a tally moved by a later landing is re-pinned in that landing round — the
  r85 counter's 17 arms are the current reading, so D84-2 is not re-committed by this landing);
  `SKILL.md` registry row 19 names the three r85 counters, the generator and their selftests.
- **Connector (seat `Mo85K01Conn`).** Sibling-overlap: no sibling claims mori's counters, receipts
  or census reconciliation; the nearest is kama's live-reconcile shape — verdict `report`, nothing
  absorbed. Clause sweep: 13 divergences (7 graded-defects, 3 target/control mismatches, 3
  harmless-wording rows); A2/A4 discharge the code-side ones and A5 the control-text ones, with the
  remaining C1 label-binding nuance stated as a named limit.
- **First falsifiers** — `w1/Mo85R01C1.md`: all five C1 attack items accept; three named laxities
  (label binding byte-level, stub-class harness markers, target suffix), no fake kill found.
  `w1/Mo85C01Critic.md`: C1/C2 are not reachable by a do-nothing control; C3 is reachable by the
  freeze alone and is ruled a **capability acquisition, not an empty claim**, under the disclosed
  limits; C3's field-order divergence is named (documented in A2/A5). `w1/Mo85M01Mut.md`:
  `MUTANTS total=48 killed=18 survivors=30` on the freeze bytes (C1 17/9/8, C2 14/4/10, C3 17/5/12),
  with the A1/A3 closure mapping in the seat's addendum — the round-86 arm population.
  `w1/Mo85R02C2.md` = `**no report on disk — the seat is dead in this wave's evidence.** The C2 attack it owned is covered by `w1/Mo85C01Critic.md` §5.2 (C2 same-sentence divergences and the stale-body limit), by `w1/Mo85E02Receipts.md` §0 (the stale-digest and headerless-receipt controls) and by `w1/Mo85K01Conn.md` §2.2 (rows C2-D1–D6).`.

## Landed changes

| change | LOG entry | commit |
|---|---|---|
| frozen contract, three counters, population controls | `LOG.md` Round 85 | `ab260865` |
| pre-data amendments A1–A4 | `LOG.md` Round 85 | `79bb4ed8`, `4ffd5a2d`, `89f82eac`, `91f657f6` |
| C1 arms, `make-receipts.sh`, QUALITY 173–175, SKILL registry row 19, SOURCES S600/S601, knowledge entry, lesson, README coverage row, PROVINCE note, evidence (battery, controls, source pins), wave artifacts | `LOG.md` Round 85 | `25a74d4c` |
| receipts regenerated at the final generator, SCORECARD round section + capabilities, LOG entry, QUALITY 176, contract A5, seat evidence | `LOG.md` Round 85 | `42865833` |
| tip measurement and the receipt-commit correction | `LOG.md` Round 85 | `0649e5ca` |

## Before → after measurements

| claim | counting command | at entering `2cc4b1ae` | after, measured at `25a74d4c` |
|---|---|---|---|
| C1 operability | `python3 -I .ufo/waves/round-85/count-c1.py <rev>` | `C1=unmet mutants=2 killed=0 survivors=2 total=2 arms=15 harness=stub missing=killed_mutant_with_coupling_not_equivalent,duplicate_coupling_not_equivalent rev=2cc4b1ae35a8`, rc 1 | `C1=met mutants=2 killed=2 survivors=0 total=2 arms=17 r84=met rev=25a74d4c34e8`, rc 0 |
| C2 calibration | `python3 -I .ufo/waves/round-85/count-c2.py <rev>` | `C2=unmet receipts=0 harness=absent rev=2cc4b1ae35a8`, rc 1 | `C2=met receipts=3 bindings=5 bound=5 revs=3 limits=3 cmd=3 summary=3 mismatch=0 detector=green`, rc 0 (measured at the receipt commit `42865833`) |
| C3 depth (capability) | `python3 -I .ufo/waves/round-85/count-c3.py <rev>` | counter file absent (`git cat-file -e` rc 128); the retroactive reading `C3=met ... rev=2cc4b1ae35a8` is disclosed, not the before value | `C3=met observed=3 aa=stable own_tokens=64 subject_tokens=64 subject_deltas=0 unmatched=0 unnamed=0 detector=green rev=25a74d4c34e8`, rc 0 |

All three were re-measured at `3dc05084` (the measured tip) and read the same lines with
`rev=3dc050847430` (`evidence/tip-r85.txt`, committed at `1b733457`); the claims' counting commands are reproducible at any
revision from that revision's bytes.

## Sources & frontier

- `SOURCES.md` rows before → after: **372 → 374** by
  `grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`; the source census
  `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin mori` exits **0 before
  and 0 after**, with **35 tolerated `W04` warnings** both times and zero `E` codes.
- Rows added by tier: **S600** (`docs`, tier A, `mined`) and **S601** (`paper`, tier A,
  `rejected` — the row D84-3 owed); rows touched old→new: **none** (append-only; no `status`,
  `recheck` or `used-by` cell of an existing row changed).
- Frontier rows advanced: none retired; the round opens a new coverage-map line (receipt
  provenance) rather than moving an FR row. `corpus/knowledge/receipt-provenance-r85.md` (K1–K3,
  cites S600) plus the `corpus/README.md` Round-85 row are the new ground.
- `Assimilation: none` — no `merge/mori/` adoption this round.
- `considerthese/2026-10-26.md` suggestion 3 ("re-execute what closures only evidence-verified")
  is mined into the receipt rule (`corpus/lessons/round-85.md` Gate; QUALITY 173/175).

## Trend verdicts

- **expansion: improved** — one admitted knowledge entry on ground the coverage map did not hold
  (receipt provenance), whose `source:` cites S600 opened, pinned three times byte-identically and
  quoted this round; two registry rows (one admit, one reject) take the lane 372 → 374; census
  rc 0; append-only.
- **quality: improved** — the three round counters carry 18/18/20 graded detector arms and three
  behavioural kill sets measured from committed bytes; QUALITY 173–176 land the round's rules; the
  standing battery is unchanged at `BATTERY pass=57 setup=4 fail=0`; the record and claim sweeps
  are green at the measured revision (`RECORD_SWEEP ... revisions=0`; the receipt at `42865833`
  records `CLAIM_SWEEP ... pointers=274` rc 0, and the earlier `729b794a` receipt recorded 266
  before the round's own SCORECARD/LOG pointers landed; the tip re-run also reads 274, rc 0). Counterweights, not
  hidden: the C2 predicate's stale-body limit is named, the C1 label binding is byte-level (named
  limit), the mutation probe reports 30 survivors for round 86.
- **discernment: improved** — the round mines its own mistake class (`number-drift` +
  `reference-drift`, the r84 D84-2 stale tally and moved pointer) into a lesson and a superseding
  QUALITY row; the connector's 13 clause divergences are triaged (10 discharged by A1–A5, 3
  harmless); four attack seats (two reviewers, critic, mutation-tester) report verdicts; D84-2/3/4/5
  are discharged and D84-1 is recorded as an attribution note (the prompt commit is not
  re-attributed this round). The critic's required-before-report items are answered in A5 and above.

## SHONEN

`SHONEN.md` boxes, one line each (`[x]` only with a named non-author verifier; none is written
here):

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources —
  `SKILL.md:1371` (r85 gate-registry row 19); `corpus/QUALITY.md` 173–176 (added round 85);
  `corpus/knowledge/receipt-provenance-r85.md` (K1–K3, sourced S600).
- [~] At least one end-to-end domain task executed and logged in LOG.md — `LOG.md` Round 85 (C1/C2/C3
  with their measured values, receipts, the dead-seat/collision record and the battery reading).
- [~] Instructions executable by an agent without oral context — `python3 -I
  .ufo/waves/round-85/count-c1.py --selftest` → `C1_COUNTER_SELFTEST pass=18 fail=0`;
  `count-c2.py --selftest` → `pass=18 fail=0`; `count-c3.py --selftest` → `pass=20 fail=0`;
  `.ufo/waves/round-85/make-receipts.sh <rev>`; the three predicate sentences in
  `.ufo/waves/round-85/contract.md`.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — `PROVINCE.md` Round-85 note (core rules
  and evidence-only instruments; no new census surface); the connector's sibling scan names kama's
  live-reconcile shape adjacent and absorbs nothing; mori reads and reports, it never remediates.

## Round shape and hygiene

- **Settlement:** the wave's dispatcher never emitted `WAVE-DONE`: 11 of 12 seats wrote a report
  (`w1/`), `Mo85R02C2` is dead with no output, and `Mo85M01Mut` was asked to stop after its report
  was on disk; the wave is settled by observation and no seat is taken as live in this report. All
  landed seat work is committed (`25a74d4c`, `42865833`, `3dc05084`, `1b733457`).
- **Shape:** ONE v1 wave, 12 seats, validated under
  `scripts/hyaku/ufo-wave-policy.json` (band 8–16); dispatch `w1-dispatch.json` (`spawn=12`,
  `resume=0`). Roles: 4 executor / 2 scribe / 1 scout / 2 reviewer / 1 critic / 1
  mutation-tester / 1 connector; attack seats 4/12 = 33.3 %; connector seats 1; residual calls
  none; the planner seat is the L1 (the validator rejects `planner`). Round total: 12 seats.
- **Dead seats / stand-ins:** ``Mo85R02C2` — no output and no live process after the wave; never replaced, and its attack is covered as stated above. `Mo85E01C1Arms` was stood in by the L1 while its registration was stale; it later verified the restored bytes and reported the duplicate-arm collision its own append caused (`w1/Mo85E01C1Arms.md` §0). `Mo85M01Mut` ran long; its report was on disk before the round closed (freeze-byte population; the tip-byte mapping is named in the report as missing).`.
- **Routed defects:** D84-1 (the r84 prompt was committed by the lane identity) recorded, not
  re-attributed; D84-2 discharged by QUALITY 173 + 176; D84-3 by the `rejected` S601 row; D84-4 by
  the three committed receipts graded by C2; D84-5 by `battery-r85.txt`'s `rev=`/`date=` header.
- **Tool installs:** none — no pacman transaction, no tool installed or upgraded.
- **Stale-lane:** respawn-per-round driver; no other mission of this lane is open.
- **Misroot sweep:** `git -C /home/vgpnk/Projects/shokunin status --porcelain` shows no file
  written by this lane's round (the untracked `.scratch/*` and other lanes' reports belong to run
  state/other lanes); no seat wrote into the fleet root, so nothing was copied or deleted.
- **L0:** no question appended; no operator decision was needed this round.
