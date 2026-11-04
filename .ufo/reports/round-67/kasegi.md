# kasegi — round 67 report

Lane `/home/vgpnk/Projects/shokunin/kasegi-shokunin` · base `8e2a8fe8eb92d7c824902a4b70aab027a9aacee0`
· final lane tip **`f167ee104d001791f7f444cda8a25c3866e0e28c`** (pushed; `git ls-remote origin
refs/heads/master` prints it) · measured implementation `c40f0bc8ae95627b60b6f6e893ea00d7b1fd7146`
· production gate sha256 `8147350c411650b4fe3307b50851722025a00cc1e71df2ecff478ea7177ad247`.

**Stale-lane:** respawn-per-round driver; this round is the lane's only open mission. No other
kasegi mission is open.

## Work performed

Two claims were declared this round, each a distinct axis move with its own falsifiable
before→after:

- **C1 — depth:verifiability (lowest non-retired axis, 4, nominal under QUALITY R58).** Replace the
  head-blind SIGPIPE exemption in the lane's derive gate with a per-head input-count rule: a
  SIGPIPE'd read-only stage that named more than one input operand is refused, with the decoded argv
  split at the **first** `--` anywhere so a dash-named operand after the separator counts.
- **C2 — coverage (8).** Admit Frontier **F45**, FIRST's PSIRT Maturity Document, from **S100** (HTML
  page) and **S101** (PDF companion), both opened this round.

Work items (evidence pointers):

- **Prefreeze no-work control** — the production gate at base reads `ok` on three two-operand
  SIGPIPE pipelines whose second operand was never opened:
  `.ufo/waves/round-67/controls/donothing-multihead-r67.txt` (`NOWORK-VERDICT …
  green_on_masked=P9,P10,P11,P12,P13,P14`); native stage-0 statuses measured with `subprocess`
  (`controls/native-statuses-r67.txt`, `controls/face-matrix-r67.txt`); the 20-shape base matrix
  (`controls/base-matrix-r67.txt`).
- **Payload correction before freeze** — two payload expectations contradicted the measured base
  matrix (P1/P2 base rc0; P8 candidate signal-13) and one shape's native face proved flaky:
  `controls/dispatch-addendum-r67.md`, delivered to the three affected seats by message.
- **Candidate gate** — `.ufo/waves/round-67/w1/ExecMultiHeadGate/figure-audit.py` (seat
  ExecMultiHeadGate): three candidate revisions, `978c98a2` → `d5e8fcae` → **`8147350c`**; selftest
  67 → 73 cases; base graft falsifies 5 cases.
- **Probe battery** — `w1/ExecMultiHeadProbes/probes.py`, 20 probes, base `20/0`, candidate-vs-base
  `20/5` (P9, P10, P11, P19, P20): `w1/ExecMultiHeadProbes/probes-output-{base,candidate-vs-base}.txt`.
- **Committed-input driver** — `w1/ExecMultiHeadDriver/verify.py` (12 named measurements, opaque
  fixture ids/paths, face-conditional repair assertions): `controls/final-verification-r67.txt`.
- **Mutation battery** — `w1/MutationMultiHead/multihead-mutbat.py`, seven limbs killed 7/7 with
  three recorded equivalents; the base gate's own red line is
  `MUTBAT killed=0/7 … invalid_rejected=10 failures=4` with `COLLECTOR-BASE mismatches=5` (the five
  repaired shapes).
- **Critic hole, confirmed and closed** — `w1/CriticMultiHead.md` § Finding 1 (mid-argv `--`),
  independently reproduced in `controls/critic-s3s4-confirm-r67.txt` (S3/S4 read `ok` at base with
  native −13 five of five and `-missing.txt` never opened; the differential without `--` exits 1,
  proving the token is a file operand).
- **Security review** — `w1/SentinelMultiHead.md`: FINDINGS, no widening, no newly admitted head or
  flag, no write path, admission parity matrix `96 derives / 0 diffs`; the pre-existing `git`/`python`
  masking is named as a residual.
- **Independent review** — `w1/ReviewMultiHead.md`: accepts the production-path repair, publishes its
  own per-head expectation matrix and the conservative-refusal classes.
- **Native-premise probe** — `w1/RevengerMultiHead.md`: which heads can die of SIGPIPE before a later
  operand, and at what first-operand size; records the uutils-versus-GNU binary resolution difference
  that became this round's PATH residual.
- **C2 source work** — `w1/ScoutF45.md` (capture, 12-quote table, novelty and province screens,
  rejection arguments) and `w1/ScribeF45.md` + `w1/ScribeF45/{S100.txt,S101.txt,first-psirt-maturity-document.md,rows-draft.md,sources-row-draft.md}`
  (independent second capture, entry and row drafts); `w1/ScopeF45.md` (205-file sibling/consumer
  sweep, 59 hits, none holding maturity ground).
- **Round drafting** — `w1/ScribeRound.md` with `lesson-draft.md`, `scorecard-draft-round-67.md`,
  `log-draft-round-67.md`.
- **Errata** — `.ufo/waves/round-67/claims-erratum-1.md` (E1 collector sub-assertion, E2 claims
  digest transcription, E3 controls revision; appended Erratum 2 for the face-flaky mutation
  battery), with both earlier receipts preserved
  (`controls/erratum1-collector-first-receipt.txt`, `controls/erratum2-mutbat-flaky-receipt.txt`).
- **Inherited state** — no uncommitted lane leftovers at round start; the only untracked round files
  were this round's own. Files authored by others (`.ufo/reports/round-84/kama.md`,
  `.scratch/**`, an unknown fleet-root `after`) were left untouched and are named here.

## Landed changes

Every change is tied to the LOG.md round-67 block and to the commit that carries it.

| Commit | Contents | LOG tie |
|---|---|---|
| `7ae95a06` | production gate `corpus/instruments/figure-audit.py` at `8147350c`, the round-67 wave evidence (spec, dispatch, ready, controls, seat reports and receipts) | round-67 bullets 2–5 |
| `b3082060` | `.ufo/waves/round-67/claims.json` — the frozen C1/C2 predicates, counters, kill rules and controls revision | bullet 6 |
| `e59c564e` | `claims-erratum-1.md` E1/E3, corrected pins, first failing receipt, driver collector fix, reverted battery | bullet 7 |
| `c40f0bc8` | `claims-erratum-1.md` Erratum 2, face-tolerant battery, measured base/candidate pin lines | bullet 7 |
| `73e6a0c0` | F45 entry + captures + manifest, README F45 row, SOURCES S100/S101 + lead retirement, QUALITY R93–R100, knowledge-expected 82→83, lesson `corpus/lessons/round-67.md`, SCORECARD round-67 section, LOG block, SKILL amendment, final receipt | bullets 8–10 |
| `f167ee10` | settled wave `w1-results.json` and the seats' final receipts/report updates | bullets 4–5 |

## Before → after measurements

**C1 — depth:verifiability, 4 → 4 (delta 0, nominal per R58; the axis's citation-resolution metric
is not read by this gate).** Counting command (frozen in `claims.json`):

```
python3 -B .ufo/waves/round-67/w1/ExecMultiHeadDriver/verify.py \
  --revision c40f0bc8ae95627b60b6f6e893ea00d7b1fd7146 \
  --controls-revision c40f0bc8ae95627b60b6f6e893ea00d7b1fd7146 \
  --work /fast/scratch/hyaku/kasegi-r67/L1/FINAL --final
```

- **Before** (`controls/donothing-multihead-r67.txt`, base gate `51f299af`):
  `FIG P9 … ok`, `FIG P10 … ok`, `FIG P11 … ok` with native stage0 `-13` and the second operand
  never opened; the mid-argv `--` shapes also read `ok` (`controls/critic-s3s4-confirm-r67.txt`);
  selftest 67/0; base probes 20/0 with five collector mismatches on the base gate.
- **After** (`controls/final-verification-r67.txt`, measured at `c40f0bc8`):
  `VERIFY measurements=12 failures=0 mode=final` exit 0; probes-measured `20/0` with P9, P10, P11,
  P19, P20 stale (`derive-upstream-signal-13` on every −13 face; P10 stale on its non-signal face
  too); shape-identity 20 shapes; selftest 73/0; existing mutbat 5/5; multihead mutbat
  `killed=7/7 equivalents=3`; real ledger `figures=35 ok=35 stale=0 exit=0`; red-wrong-want and
  identity guards hold.

**C2 — coverage, 8 → 8 (delta 0; the score is saturated under the lane's saturation line and this
claim adds one admitted frontier row).** Counting commands:

```
python3 corpus/instruments/frontier-recheck-count.py
python3 corpus/instruments/capture-binding-check.py
python3 corpus/instruments/source-recheck.py --manifest corpus/source-snapshots/round-67/manifest.json --source S100   # and --source S101
/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kasegi
```

- **Before** (`controls/c2-base-counters-r67.txt`): `rows=44 admitted=44 closed=44 problem-rows=0
  registry=99`, `entries=47 pass=47`, `records=79 bound=79 unbound=0`, knowledge 82, census exit 0
  with six inherited `W04` warnings.
- **After** (`controls/census-after.txt`, measured at `73e6a0c0`): `rows=45 admitted=45 closed=45
  problem-rows=0 registry=101`, `FRONTIER-PASS F45 ids=S100,S101`, `entries=48 pass=48`,
  `records=81 bound=81 unbound=0`, knowledge 83, expected list 83 entries / 85 lines, census exit 0
  with the same six warnings and none on S100/S101; `source-recheck` passes 54/54 pinned quotes.

## Sources & frontier

- **Census before → after**, command
  `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kasegi`:
  before `exit 0` with six inherited `W04` URL warnings (`controls/census-before.txt`), after
  `exit 0` with the same six and none on the new rows (`controls/census-after.txt`).
- **Rows before → after:** 99 → 101 (S100, S101), tiers A 89 → 91, B 5, C 5, `mined` 81 → 83,
  `rejected` 18; no pre-existing status/recheck/used-by/id/URL cell changed.
- **Rows added by tier:** tier A two (S100 FIRST maturity HTML page, S101 its PDF companion).
- **Rows touched old → new:** none on pre-existing rows. The round-65 **lead** line
  (`corpus/SOURCES.md:246`) is retired as opened (kept byte-identical) because its raw-HTML digest
  `334aeb01…` is not reproducible — six fetches give six raw digests at an identical 82978 bytes
  (per-response CSP nonce) and one normalized snapshot digest `cf834a65…`; the PDF digest
  `f217c446…` in the same line reproduces exactly and is recorded in S101's anchor cell.
- **Frontier rows advanced:** F45 admitted (FIRST PSIRT Maturity Document — three named levels over
  an operational-foundations floor, the reactive→proactive direction, Level 2 gated on Level 1, the
  Annex-7 per-level checklist, and the PDF-only informational-purposes notice).
- **Sourced claim:** C2 rests on S100 and S101, both opened this round; every quote in the entry is
  pinned in `corpus/source-snapshots/round-67/manifest.json` and located at its cited line (46
  quoted fragments checked, 54 pinned quotes verified, `source-recheck` exit 0).
- **Assimilation:** none. `merge/kasegi/` was not used this round; the latest `considerthese/`
  proposal remains domain-task-open and no consideration is declared implemented.

## Trend verdicts

- **Expansion — improved.** F45 admitted with an 18-row attributed claim table on ground the lane
  did not hold (S098 carries zero occurrences of "Maturity Level"; the maturity document defers its
  own catalogue to the framework). Evidence: `corpus/knowledge/first-psirt-maturity-document.md`,
  `corpus/README.md` F45 row, registry 99 → 101.
- **Quality — unchanged.** No knowledge entry was superseded, re-admitted or re-verified; the gate
  repair is an instrument correction, not a corpus entry. QUALITY gains R93–R100 from this round's
  mistakes, which is the discernment instrument rather than a quality move by itself.
- **Discernment — improved.** The wave's attack seats found the mid-argv `--` hole, the flaky native
  face and three counter defects **before** the freeze (M67-1..M67-4), and this round's own errata
  (collector sub-assertion, face-flaky battery, transcribed digest) were filed with both receipts
  preserved rather than hidden (M67-5..M67-10). Outside admission remains owed.

## Round shape, seats and dead seats

One v1 wave, **12 seats** (`w1-dispatch.json`: spawn 12, band 8–16), plus the L1 holding the
planner seat (the validator rejects a planner role). Role mix: **3 executor** (gate, probes,
driver), **1 reviewer**, **1 critic**, **1 mutation-tester**, **1 sentinel**, **1 revenger**,
**1 scout**, **1 connector**, **2 scribe**. Attack seats 5 of 12 (42 %), connector seats 1 (limit 2).
**No residual call. No dead seat. No replacement.** Seat iterations after the first settle (the gate
re-cut, the probes' 20-row revision, the driver's defect fixes and one bounded unfreeze) belong to
the same wave and are recorded in the lesson, not as extra seats.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources —
  evidence: `SKILL.md` (r67 current-execution amendment) plus the round's own receipt
  `controls/final-verification-r67.txt`; author assertion, outside promotion verification owed.
- [ ] At least one end-to-end domain task executed and logged — not attempted this round: the
  domain roots are absent and live-target testing is refused; the round claims no domain-task credit.
- [~] Instructions executable by an agent without oral context — evidence:
  `corpus/lessons/round-67.md` § Round shape and settlement plus the committed driver and probe CLIs;
  not promotion evidence.
- [~] No cross-domain bleed — evidence: `PROVINCE.md` scope unchanged; F45 sits in the lane's
  vendor-program class next to F10/F43/F44 and the adjacency is named in the entry's limits;
  live-target testing still refused.

## Tooling, hosts and boundaries

No tools installed or upgraded; no pacman transaction was attempted (host-wide pause respected).
Lane commits went through `scripts/hyaku/jj-lane.sh` only; the report lands through
`scripts/hyaku/fleet-commit.sh`. Push scope: this lane's remote and the fleet repo only. The
fleet-root misroot sweep (`git -C /home/vgpnk/Projects/shokunin status --porcelain`) shows only
orchestrator-owned `.scratch/**`, a sibling `kama` report and an unknown pre-existing `after`; no
file attributable to a kasegi r67 seat was written into the fleet root, so nothing was copied or
deleted.

Host-dependence disclosed: the gate resolves `/usr/bin/{grep,cut,wc,sort,head,tail,sha256sum,ls}`
(GNU grep 3.12-modified, GNU coreutils 9.12) from a `subprocess` child, while this session's
interactive shell exposes a builtin `grep` reporting `pi-uu-grep 0.2.0` and one seat's shell
resolved uutils 0.8.0 shims. Every measurement in this report is `subprocess`-based; the
face-conditional assertions hold under both resolutions, and the PATH difference is a named
residual.
