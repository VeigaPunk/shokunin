# souji — round 89 report

Lane: `souji-shokunin` (lane repo `/home/vgpnk/Projects/shokunin/souji-shokunin`). Round 89, attempt 1.
Lane base `a2cef94a`. Instruments/controls P `c9329534`; preregistration alone F `d8bc7484`; harness fix
(post-F, disclosed A0.6) `a3c7cb1f`; wave evidence `4864129b`. Wave evidence dir `.ufo/waves/round-89/w1/`.

Round shape: one v1 wave of 12 seats under `scripts/hyaku/ufo-wave-policy.json` (band 8–16), **6 attack seats**
(critic, reviewer, mutation-tester, sentinel, simplifier, revenger-labrat), 2 executors, 1 scribe, 1 scout,
1 connector, 1 second reviewer (distiller role); **no residual call**; round total **12**, no dead seat. The L1
(`SoujiR89`) holds the canonical planner seat; no `planner` seat was dispatched.

## Work performed

Declared claims: **C1 (calibration 7, the lane's lowest owned non-retired axis)** — the four S88MutCounter F1–F4
survivors each get one binding row and one binding mutant: NF6h (the `_whole` before-byte half with a `/`
predecessor, fixture R12) kills `m18b`; LD1b (a duplicate with a DIFFERENT appended target) kills `m17b`; NF6i
(the `_whole` loop over every occurrence, R12's twice-token line) kills `m18d`; LD2 (a 2-column ledger append) was
to kill `m17c`. **C2 (operability 8)** — the FLAGFAIL branch decodes base64 with `surrogateescape` and bounds RAW
bytes first (head-100 / `…` / tail-99) before escaping, so the detail is injective on the bytes and the head
carries content.

- **C1 instruments (P).** `census/round-89/c1-false-rows.tsv` (57 rows = the r88 53 byte-for-byte, in order, plus
  NF6h/NF6i at fixture revision R12 and LD1b/LD2, sha `04570a64…`), `c1-mutants.json` (16 members, the r88 twelve
  plus `m18b`/`m17b`/`m17c`/`m18d`, sha `bc7e6bb1…`), `c1-false-row-harness.py` (R12 fixture + the LD1b/LD2
  ledger-append variants), `c1-clause-battery.py` (the r88 battery plus the r89 PINS entry). The counter under
  test is the **unchanged r87 counter** (`fd0a8e24…`); the item file is unchanged (`ce80195d…`).
- **C1 before/after.** `census/round-89/controls/c1-before.txt` is the do-nothing control (the same sixteen
  mutants on the r88 53-row population): twelve killed, `m18b`/`m17b`/`m17c`/`m18d` alive, `SUMMARY killed_r88=12`,
  EXIT 0. `census/round-89/records/c1-after.txt` is the frozen command's after arm: pristine 53/0 and 57/0,
  **fifteen killed on r89**, `m17c-no-malformed killed=no`, `SUMMARY killed_r88=12 killed_r89=15 killed_total=27`,
  battery **EXIT 1**. The L1's detached run was reaped at mutant 3, so the receipt is composed from three seats'
  independent full-matrix runs (`S89MutCounter` after-A..D.log, `S89Reviewer` c1-after.out, `S89Sentinel` §3.4,
  and `S89Simplifier`'s baseline), which agree cell for cell.
- **C2 repair.** `tools/souji-record-agreement.py` (`f6fce6d1…`): `_escape_text` gained the surrogate arm
  (`0xDC80..0xDCFF` → `\xNN` of the original byte), `_decode_record` uses `surrogateescape`, `_one_line_bytes`
  bounds the RAW bytes first, and the FLAGFAIL branch renders through `_one_line_bytes` instead of
  `backslashreplace` + `_one_line`.
- **C2 fixture.** `tests/fixtures/r89-k4-flagfail.py` (`a9b03141…`): the r88 seven cases plus KFF6 (invalid UTF-8
  byte), KFF7 (the literal escape spelling) and KFF8 (25 leading SOH bytes then `AttributeError`), with counting
  checkers (`chr(92)`-based, so the doubled and single spellings cannot be confused) and a pair check that the
  KFF6/KFF7 details differ on the tool under test.
- **C2 before/after.** `census/round-89/controls/c2-before.txt` on the r88 tool bytes (`4042218f…`, both arms):
  `SUMMARY cases=10 tool_pass=8 before_pass=8`, KFF6/KFF8 fail, EXIT 1. `records/c2-after.txt` on the filed tool
  (re-run after F because the first run predated the freeze; identical numbers): `SUMMARY cases=10 tool_pass=10
  before_pass=8`, EXIT 0. The r87 12-row K4 counter on the filed tool reads `rows=12 mismatches=0 errors=0`
  (`S89ExecC2` §2).
- **Sources.** S351 (Python `codecs` § Error Handlers, the `surrogateescape` entry) admitted `mined`, 13-word
  rendered quote, capture `census/round-89/srcs/codecs.html`; it is the source the C2 repair rests on and is cited
  by `corpus/knowledge/decode-escape-order.md`. S352 (Python `base64` `b64encode`/`validate`) is the round's
  **reject sample and was not filed** — S349 already holds that exact scope, quote, rejection and flip, so S352
  would add registry weight, not a decision (`plans/round-89.md` A3). Quality criterion **Q164** added.
- **Wave.** `.ufo/waves/round-89/w1/` — 12/12 seats settled (`w1-results.json`), no dead seat: executor ×2
  (`S89ExecC1` re-derived the C1 arms and per-row attribution; `S89ExecC2` re-derived both C2 arms, the r87
  regression and five attacks), mutation-tester (`S89MutCounter`: LD2 kills nothing; the whole-matrix measurement),
  revenger (`S89Labrat`: the `_whole` probe table, all pairs agree with the row expectations), critic (H1 + C1-a/b/d
  and C2-a/d narrowings), reviewer ×2 (`S89Reviewer`: after arm DISAGREE, both C2 ends AGREE, chronology;
  `S89Distiller`: dedup vs prior rounds and the unattacked-loci list), sentinel (F-1 the same measurement, F-2 the
  dispatch wording, F-3/F-4 the inherited carries, plus a 16-probe privilege table), simplifier (deletion audit,
  `_one_line` and battery-default patches queued for r90), connector (separability PROVEN, carry audit, sibling
  overlap zero, prior-art zero duplicates), scout (`S89ScoutSources`: live re-fetch of both pages, S351/S352
  verdicts, the version-drift note), scribe (`S89Scribe`: the S351 row, the knowledge entry, Q164 and the
  quote-verification receipt). Spec `w1-spec.json`, validated dispatch `w1-dispatch.json`, ready handoff `w1.ready`
  (`.dispatched` 09:46).
- **Wording narrowings before filing.** `plans/round-89.md` A1 (C1: three of four bindings verify; LD2 falsified;
  `LD2b` carried), A2 (C2: the 0x85/U+0085 collision and the 202-byte raw window), A3 (S352 redundancy and the
  3.15.2/3.14.8 version note), A0.6 (the harness pin superseded by `6165eade…`), A0.1–A0.5 (checker fix, number
  correction, bound restatement, the fleet misroot, the battery wall). `claim-falsification.tsv` reconciles every
  attack seat against `census/round-89/preregistration.txt`, not against the dispatch text.

## Landed changes

| change | LOG.md entry | commit |
|---|---|---|
| C1 population (57 rows), 16 mutants, harness (R12 + LD1b/LD2), battery, C2 fixture, tool repair, both before receipts, the two source captures | round-89 entry, bullets "Claims", "Sources" | `c9329534ccecb2e2ffe17214e4dbd4928df2d9b7` (P) |
| the preregistration, alone | round-89 entry, "Claims" | `d8bc7484df076b3846e1bba57af91371631fd685` (F) |
| wave-1 spec, validated dispatch, ready handoff, plan skeleton | round-89 entry, "Wave" | `4854c8d72ec874bef5d21b18909a615d061a6bae` |
| the NF6i fixture-line fix (R12 token twice) | round-89 entry, A0.6 | `a3c7cb1f1c5aa21a3da2248cbe0fb501058743aa` |
| the C1 after receipt, the post-freeze C2 after receipt, S351, Q164, the knowledge entry, the lesson, the plan amendments, the falsification ledger, the r89 build-spec wording | round-89 entry, "Measured"/"Docs" | `755a46cbdf0525d2bded60f211d4483c0903bdfe` |
| wave evidence (12 seat reports + receipts + results), SCORECARD r89 rows, LOG round-89 entry, census after | round-89 entry, all bullets | `4864129b34fabfbd86a0d78b16c336e86e23e11f` |
| the pre-file claims file | — | `c2ee31aea555eabb8a86d036bbb1d3fe4e5663bb` (final lane commit before the report) |

## Before → after measurements

### C1 — calibration 7

Counting command (one, both ends; run from the lane root, `WORK` an empty dir outside `/tmp`):

```
after:  python3 -B census/round-89/c1-clause-battery.py --counter census/round-87/c1-pointer-counter.py \
          --work WORK --only r88,r89 --expect-killed 28
before: the same battery/counter/mutants with --only r88 --expect-killed 12
```

| end | receipt | observed | exit |
|---|---|---|---|
| before (do-nothing: sixteen mutants on the r88 53 rows) | `census/round-89/controls/c1-before.txt` | `ARM pristine pop=r88 rows=53 mismatches=0 errors=0 exit=0`; twelve killed; `m18b-alnum-before`, `m17b-target-keyed`, `m17c-no-malformed`, `m18d-first-only` alive; `SUMMARY mutants=16 sets=r88 pristine_r88=ok killed_r88=12 killed_total=12` | 0 |
| after (57 rows) | `census/round-89/records/c1-after.txt` | `ARM pristine pop=r88 rows=53 mismatches=0 errors=0 exit=0`; `ARM pristine pop=r89 rows=57 mismatches=0 errors=0 exit=0`; `m17c-no-malformed pop=r89 killed=no`; `SUMMARY mutants=16 sets=r88,r89 pristine_r88=ok pristine_r89=ok killed_r88=12 killed_r89=15 killed_total=27` | **1** |

**Verdict: C1's frozen target (16/28/EXIT 0) is NOT MET — three of the four bindings verify and the fourth is
falsified by the round's own artifacts.** `LD2`'s appended `P02\tABSENT` is a 2-column row, but `P02` is already
`ABSENT\t-` in the frozen r77 ledger, so pristine refuses it on `len(r) < 3` and `m17c` (which drops only that
clause) refuses it on `r[0] in ledger` with the same `LEDGER-REFUSED id=P02` marker and exit 1; the harness row
stays green, so `m17c` survives and `LD2` binds the duplicate clause a second time. The clause IS reachable: a
2-column row under an absent id (`ZZ9\tABSENT`) makes pristine print `LEDGER-REFUSED id=ZZ9` and `m17c` raise
`IndexError` with no marker (`S89Sentinel` §6.1, `S89MutCounter` F1). The binding row `LD2b` is measured and
carried to r90; the narrowed sentence is `plans/round-89.md` A1. The four new mutants deliver three kills, not four.

### C2 — operability 8

Counting command (one, both ends):

```
after:  python3 -B tests/fixtures/r89-k4-flagfail.py --tool tools/souji-record-agreement.py \
          --before census/round-89/controls/c2-before-tool.py --work WORK
before: the same fixture with the r88 tool bytes as BOTH --tool and --before
```

| end | receipt | observed | exit |
|---|---|---|---|
| before (r88 tool `4042218f…`) | `census/round-89/controls/c2-before.txt` | `SUMMARY cases=10 tool_pass=8 before_pass=8`; KFF6/KFF8 fail | 1 |
| after (filed tool `f6fce6d1…`) | `census/round-89/records/c2-after.txt` | ten `CASE … tool=pass`; `SUMMARY cases=10 tool_pass=10 before_pass=8` | 0 |
| regression (r87 12-row K4 counter on the filed tool) | `S89ExecC2` §2 | `SUMMARY rows=12 mismatches=0 errors=0` | 0 |

**Verdict: the enumerated kill rule passes (10/10/8, EXIT 0); the headline "injective on the bytes" is narrowed.**
`S89ExecC2` §6 measured that a raw `0x85` byte and the UTF-8 NEL (`b'\xc2\x85'`) render identically on the r89
tool (they were distinct on r88), because `_escape_text` spells the surrogate `\udc85` and the real character
U+0085 with the same `o == 0x85` branch, and a 4000-byte update should note the window arithmetic: the truncated
raw window is `100 + 3 (U+2026) + 99 = 202` raw bytes, not 200, and the K4 cell adds a 59-character wrapper
(`S89Critic` C2-a, `S89Scribe` F1). Both narrowings are recorded in `plans/round-89.md` A2; the falsifying pair is
not in the frozen fixture, so the kill rule still passes. Fixes (spell U+0085 as `\u0085`, or a KFF9 row) are
carried.

| claim | counting command | measured commit |
|---|---|---|
| C1 | `python3 -B census/round-89/c1-clause-battery.py --counter census/round-87/c1-pointer-counter.py --work WORK --only r88,r89 --expect-killed 28` | `755a46cbdf0525d2bded60f211d4483c0903bdfe` (receipts), instruments at `c9329534` |
| C2 | `python3 -B tests/fixtures/r89-k4-flagfail.py --tool tools/souji-record-agreement.py --before census/round-89/controls/c2-before-tool.py --work WORK` | `755a46cbdf0525d2bded60f211d4483c0903bdfe` (receipt), tool at `c9329534` |

## Sources & frontier

`SOURCES.md` rows: before **273**, after **274** (`grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|'
corpus/SOURCES.md`). Rows added by tier: tier A `docs` **1** (S351 admitted `mined`, `surrogateescape`); **1
reject sample not filed** (S352, re-using the standing S349 reject — filing it would duplicate a held scope).
Rows touched old→new: S351 new `mined` (used-by `corpus/knowledge/decode-escape-order.md`); no existing row's
status/recheck/used-by cell changed. Frontier rows advanced: none — this round is instrument masonry (a
population/mutant extension and a tool repair), not a PROVINCE frontier promotion; F1–F5 keep their statuses.

Census commands and outputs: before `census/round-89/records/sources-census-before.txt` → `souji ok`, `EXIT=0`;
after `census/round-89/records/sources-census-after.txt` → `souji ok`, `EXIT=0`, with one new `W04` (S351
duplicate URL on the codecs page, the expected scope-narrowing warning). Full form:
`/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin souji`.

Assimilation: none this round (no `merge/souji/` theme admitted); `considerthese/` is absent in this lane.

Curation: the S351 row is a scope-narrowing row on a held URL — S253's own scope cell says "not the `ignore` or
`surrogateescape` handlers", so S351 occupies exactly the excluded scope (the S256-supersedes-S253 precedent).
Version note: the filed captures carry the 3.15.2 book while the host is 3.14.8; the scout's `/3.14/` fetches and
the filed `/3/` captures agree on both quoted sentences byte-for-byte, so the quotes and word counts hold
(`plans/round-89.md` A3).

r88 spot-check routed defects: **report attribution** — the r88 report's adding fleet commit was swept under
`kagi-shokunin`; this round's report is filed through `fleet-commit.sh --as souji` as the protocol requires (the
helper assigns the lane identity; any later sweep by another identity is again a fleet-side defect to record, not
a lane re-file). **S349 word-count self-correction** — verified, no action. **Launch-workdir convention** — the
r89 receipts name their `--work` roots under `/fast/scratch/hyaku/souji-r89/` and the composed C1 receipt states
the reaping, so the cosmetic gap is closed for this round's artifacts.

## Trend verdicts

- **expansion: improved.** One source opened and admitted (`S351`), one duplicate-scope candidate rejected by
  measurement rather than filed (`S352`), and one new knowledge entry
  (`corpus/knowledge/decode-escape-order.md`); registry 273 → 274. The C1 population gains four rows (57) and the
  mutant set four members (16).
- **quality: improved.** C2's FLAGFAIL detail is injective on the measured bad-byte/literal pair and its head
  survives 25 leading control bytes, measured through the public path (10/10 after, 8/10 before) with the r87
  12-row counter unchanged; Q164 records the raw-first/`surrogateescape` rule and its two measured limits.
- **discernment: mixed → improved by the honest stop.** Four seats independently measured C1's miss and the round
  files it as a failed target rather than re-scoring (A1); three seats measured the C2 headline's overreach and it
  is narrowed, not quietly kept (A2); the do-nothing control was committed before F and beats nothing
  (12 < 15 < 16); and a row the round itself designed was measured non-load-bearing and carried as a fix rather
  than defended.

## Stale-lane

Respawn-per-round driver; no other mission of this lane is open. The r89 round is the lane's only in-flight work.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — the Q164 rule and the
`corpus/knowledge/decode-escape-order.md` entry are grounded in S351 and the r89 receipts under `census/round-89/`.
- [~] At least one end-to-end domain task executed and logged in LOG.md — `LOG.md` round-89 entry with the two
frozen commands and their receipts; `.ufo/waves/round-89/w1/S89ExecC1.md`, `S89ExecC2.md`.
- [~] Instructions executable by an agent without oral context — `census/round-89/preregistration.txt` carries both
commands, both controls and the kill rules; the twelve seats re-derived them from the files alone.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — `S89Connector` §3 read kagi/mori/tsukuroi/tameshi
PROVINCE.md and found zero overlap; no credential, host-repair or orchestration work was absorbed.

## Extras

- **Pre-file falsification:** `python3 scripts/hyaku/prefile-falsification.py --lane souji --round 89` →
  `PREFILE-FALSIFICATION: pass claims=2 rows=12 attack_seats=6 findings=0`, EXIT 0 (`.ufo/waves/round-89/
  claim-falsification.tsv`); every attack seat (critic, mutation-tester, reviewer, sentinel, simplifier, connector)
  appears in the artifact column.
- **Inherited state:** the round directory was absent at start (attempt 1, no `lane-dead-no-report` line for r89);
  nothing was inherited. The only mid-round instrument change is the disclosed A0.6 NF6i fix.
- **Misroot sweep:** `git -C /home/vgpnk/Projects/shokunin status --porcelain` shows no untracked fleet file naming
  this lane or round. One L1 `write` misrooted the preregistration at `/home/vgpnk/Projects/shokunin/census/round-89/`
  earlier in the round; it was moved byte-exact (`cmp`) into the lane and the fleet directory removed (A0.4), and
  is recorded as mistake M4 in `corpus/lessons/round-89.md`.
- **Dead seats:** none — all 12 seats settled and wrote reports (`w1-results.json`); no substitute or duplicate
  seat was spawned.
- **Tool installs:** none. No pacman (paused host-wide), no uv/npx/binary fetch, no sysctl, sudo or kernel change.
- **L0 questions:** none opened this round.
