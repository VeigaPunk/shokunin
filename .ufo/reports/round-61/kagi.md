# kagi — round 61 (secrets & vault ops)

Lane: kagi (`kagi-shokunin`, branch `master`). Round 61, attempt 1, driver
`hyaku-inline`. Claim BASE `c940f51689d702f1786989d56ad4663833c1452e` (round-60 verifier
spot-check tip); predeclaration `8595018164f7421864254c6c5ca762b8f201e8be` (frozen plan
`plans/round-61.md`); candidate/landing `08f950daa61986b5dbf579791d7138102184fa66`.

Declared claims (frozen before data):

- **C1 — calibration** (`C1_ROUTED`): the seven round-60 spot-check routed record defects
  (D1–D7) are resolved and re-checkable. Predicate: `value` = unresolved items over
  `POP = 7` when `GUARD = 1`, else FAIL; target 0 (BASE 7).
- **C2 — operability, capability acquisition** (`C2_SEAL_TRIAL`): an executed OpenBao seal /
  unseal key-share custody trial with five mechanics, five falsifier shims, a no-bao leg and
  its own fixture-driven `--selftest`. Predicate: `value = 5` when both real runs are HOLDS
  5/5, each shim flips exactly its designated test, a no-bao PATH reads SETUP rc 2, and
  `--selftest` prints `SEAL_SELFTEST: PASS (cases=N)` with N ≥ 8; target 5 (BASE 0).

Both claims are sourced: C2's T5 rests on S126 (`operator rekey`), T1/T2 on S125 (seal
concepts), T4 on S127 (generate-root), each opened this round with a located quote in the
lesson `## Gate`.

## Work performed

- **C1 — the seven routed record defects became an audited item set.** Each item's compared
  number is derived by `plans/round-61-c1-check.py` from the measured tree or a named
  revision: I1 the `R60MutCounters` output byte length against
  `.ufo/waves/round-60/w1-results.json` (16 results / 3824 B); I2 a fixture-driven
  `--selftest` on `plans/round-60-c2.sh` (36 cases) plus its `SKILL.md` row; I3 the
  `## Amendment A7` withdrawal of `plans/round-60.md` §A3 item 2 plus the M60-2 second
  instance; I4 the quality-trend correction naming D1–D3; I5 the `LOG.md` in-place-rewrite
  correction (`insertions=1 deletions=1`); I6 the driver launch line plus four `%ci`
  committer stamps; I7 the attack-share fractions derived from the results role mix
  (3/16, 4/16). Evidence: `plans/round-61-c1.sh`, `plans/round-61-c1-check.py`,
  `.ufo/waves/round-61/build/R61ExecCounterC1/` (BASE reading, selftest 52 cases, challenge
  receipts), `.ufo/waves/round-61/build/R61ExecFixRecords/rederive.md` (every number
  re-derived), `.ufo/waves/round-61/controls/controls-prefreeze.txt`.
- **C2 — an executed seal / unseal key-share custody trial.** `corpus/openbao-seal-trial.sh`
  (1123 lines, sha256 `a3bc8825…`) runs T1 init share/threshold arithmetic and
  non-persistence, T2 the unseal threshold with the duplicate-share refusal, T3 seal and the
  503 sealed-state request, T4 generate-root with the OTP decode, T5 `operator rekey` refused
  under the default config on raft and inmem — on throwaway servers bound to 127.0.0.1 under
  `setpriv --pdeathsig KILL`, `bao` through PATH, no real vault/account/secret touched.
  Evidence: `.ufo/waves/round-61/build/R61ExecTrial/` (two byte-identical real runs, five
  shim receipts, no-bao leg, selftest 63 cases, mutant witness),
  `.ufo/waves/round-61/build/R61ExecCounterC2/` (candidate and BASE readings, stub controls).
- **The rekey root cause was reverse-engineered, not inferred.** `.ufo/waves/round-61/build/R61Revenger/rekey.md`
  measures that the 405 is a registration gate — `/v1/sys/rekey/{init,update,verify}` is
  mounted only when the listener sets `disable_unauthed_rekey_endpoints = false` explicitly;
  unmounted, the logical paths carry no callback and `sdk/framework/backend.go` turns the nil
  callback into `ErrUnsupportedOperation` → 405 — and that `rotate-keys` completes a full
  rotation (5/3 → 3/2, old shares refused, new shares unseal). The flag also exposes
  anonymous start/status/update/cancel, recorded as a custody hazard.
- **The knowledge entry and the registry rows.** `corpus/knowledge/openbao-seal-key-custody.md`
  (42nd entry) separates the documented rule (located quotes) from the measured mechanic
  (receipt lines), carries the docs-vs-binary table and the custody reading, and names its
  bounds and falsifiers. Rows S125–S127 with fetch-provenance rows.
- **Attack seats changed the instruments before the candidate reading.** The critic found the
  trial's T4 decode contract inverted and the C2 counter's secret scan false-positiving on
  comment separators; the reviewer found the trial's syntax break, the C2 counter's
  vacuity (a printer-stub trial read `value=5`) and five structural-item bypasses; the
  mutation-tester ran 22 mutants (20 killed, 1 survived, 1 inconclusive); the sentinel
  reviewed secret shapes, listener posture and scratch confinement; the connector swept 21
  lanes. Evidence: `.ufo/waves/round-61/build/R61{Critic,Reviewer,MutCounters,Sentinel,Connector}/`.
- **Controls battery.** `plans/round-61-controls.sh` ⇒ `CONTROLS: match=18 mismatch=0`
  (`.ufo/waves/round-61/controls/controls-prefreeze.txt`), including `C2-STUB`,
  `C2-HELPSTUB` and `C2-FIXTURE-TRUTH` (re-pointed after adjudication to the measured,
  stronger refusal `R61_BAO=<stub>` ⇒ `SETUP bao-pin-mismatch` rc 2).
- **Frontier step.** Three rows opened and admitted, one candidate rejected with reason and
  flip; one mistake class mined into eight lesson rows with fixes shown able to fail; the
  census before/after recorded below.
- **Wave.** ONE v1 wave, 16 seats (`kagi-r61-w1`), 0 dead, no residual call: 2 scout,
  6 executor, 2 scribe, 1 reviewer, 1 critic, 1 mutation-tester, 1 sentinel, 1 connector,
  1 revenger. Attack share 3/16 = 18.75 % on the addendum's literal list (no labrat seat
  exists), 4/16 = 25 % counting the sentinel. The L1 holds the canonical planner seat (the
  validator rejects `planner` as a swarm role). Round total: 16 seats.

## Landed changes

All changes land in `08f950daa61986b5dbf579791d7138102184fa66` (lane tip, pushed) and are
tied to the `LOG.md` round-61 entry (`LOG.md:1984`).

| change | LOG.md entry | commit |
|---|---|---|
| C1 checker + driver (`plans/round-61-c1-check.py`, `plans/round-61-c1.sh`) | Round 61, C1 bullet | `08f950da` |
| C2 counter (`plans/round-61-c2.sh`) and trial (`corpus/openbao-seal-trial.sh`) | Round 61, C2 bullet | `08f950da` |
| Control battery (`plans/round-61-controls.sh`) and receipt | Round 61, battery bullet | `08f950da` |
| Seven record corrections (`corpus/lessons/round-60.md:176-180`, `LOG.md:1982`, `plans/round-60.md` §A7, `plans/round-60-c2.sh` `--selftest`, `SKILL.md:855`) | Round 61, C1 bullet | `08f950da` |
| Entry `corpus/knowledge/openbao-seal-key-custody.md` + coverage rows (`corpus/README.md:94-95`) | Round 61, corpus bullet | `08f950da` |
| Registry rows S125–S127 (`corpus/SOURCES.md`, `corpus/source-fetches.tsv`) | Round 61, corpus bullet | `08f950da` |
| Lesson `corpus/lessons/round-61.md` (Gate, 8 mistakes, routed dispositions, corrections) | Round 61 entry | `08f950da` |
| `corpus/QUALITY.md` QM78–QM80; `SCORECARD.md` round-61 pre/post sections and the capability row; `corpus/claims-declared.tsv` rows 61/C1, 61/C2; `corpus/stamps.tsv` (149 rows) | Round 61 entry | `08f950da` |
| Wave evidence `.ufo/waves/round-61/` (spec, dispatch, ready, capture, build, controls, w1 reports, results) | Round 61, wave bullet | `08f950da` |
| Frozen predeclaration `plans/round-61.md` | Round 61 entry | `85950181` |

## Before → after measurements

**C1 — calibration.** Counting command and both readings (the same command, one revision
apart; `c1-driver` materialises each revision with `git archive`):

```
bash plans/round-61-c1.sh c940f51689d702f1786989d56ad4663833c1452e
  C1_ROUTED: value=FAIL population=7 i1=0 i2=0 i3=0 i4=0 i5=0 i6=0 i7=0 guard=0   rc 1
  c1-driver: measured=revision c940f51689d702f1786989d56ad4663833c1452e (git archive)
bash plans/round-61-c1.sh 08f950daa61986b5dbf579791d7138102184fa66
  C1_ROUTED: value=0 population=7 i1=1 i2=1 i3=1 i4=1 i5=1 i6=1 i7=1 guard=1      rc 0
  c1-driver: measured=revision 08f950daa61986b5dbf579791d7138102184fa66 (git archive)
```

7 → 0 over population 7, guard 1, measured against `08f950da`. Checker selftest
`C1_CHECK_SELFTEST: PASS (52 cases)`; the guard challenge fires (a `deletions=1→2` delta on
the evaluated I5 line reads value+1; a constant-0 printer stub fails the same challenge);
the pre-freeze battery's `C1-NOWORK` reads `value=7 population=7` and `C1-F1..F7` each read
exactly one unresolved item.

**C2 — operability (capability).** Counting command and both readings:

```
bash plans/round-61-c2.sh c940f51689d702f1786989d56ad4663833c1452e
  C2_SEAL_TRIAL: value=0 tests=5 pass=0 shims=0 vectors=0/5 selftest=0 guard=0 (absent)  rc 1
bash plans/round-61-c2.sh 08f950daa61986b5dbf579791d7138102184fa66
  C2_SEAL_TRIAL: value=5 tests=5 pass=5 shims=5 vectors=ok/5 selftest=1 guard=1
    (real=1 real2=1 none=1 ops=1 t2w=1 stubctl=1 secret=1
     sh1=BHHHH sh2=HBHHH sh3=HHBHH sh4=HHHBH sh5=HHHHB
     trial=a3bc882597ccaebca66d23d5a76cf6a6d4810822fe774f43ff2dace8cb60b535 cases=63)  rc 0
```

0 → 5, measured against `08f950da`. The trial's own `--selftest` ⇒
`SEAL_SELFTEST: PASS (cases=63)`; each shim reads `BROKEN holds=4 broken=1` with exactly its
own test moved; the no-bao leg reads `SETUP no bao on PATH` rc 2 with no HOLDS line.

## Sources & frontier

Census command (the frozen manual census is in `CORPUS.md`; this is the maintained parser):

```
/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kagi
```

- **Before (round start, at BASE `c940f51`):** `kagi ok` — rc 0, 124 rows, the standing
  `W04` duplicate-URL warnings.
- **After (candidate `08f950da`):** `kagi ok` — rc 0, 127 rows, the same `W04` warnings.

| measure | before | after | command |
|---|---:|---:|---|
| registry rows | 124 | 127 | `grep -cE '^\|\[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md` |
| rows added by tier | — | 3 × tier A | `awk -F'\|' '/^\| S[0-9]/{...}' corpus/SOURCES.md` (S125–S127) |
| rows touched old→new | — | 0 | `git diff --numstat c940f516 08f950da -- corpus/SOURCES.md corpus/source-fetches.tsv` ⇒ `3 0` / `3 0` (appends only) |
| frontier rows advanced | — | 0 | the frontier list (`corpus/README.md` §Frontier) is unchanged; S125–S127 are core additions, not frontier promotions |
| fetch-provenance rows | 167 | 170 | `wc -l corpus/source-fetches.tsv` |

Rows added: **S125** (seal concepts, tier A, `mined`, `180d`), **S126** (`operator rekey`,
tier A, `mined`, `180d`), **S127** (`operator generate-root`, tier A, `mined`, `180d`). Each
was opened this round (2026-11-07) with a captured decoded body, a sha256, and a located
≤25-word quote in the lesson `## Gate` (three admits, one reject:
`https://openbao.org/docs/configuration/seal/` refused as a duplicate of S125's `teaches`
with nothing measurable, flip condition recorded). No existing row's `status`, `recheck` or
`used-by` changed.

**Assimilation: none.** The shokuknow `merge/kagi/` package was read (read-only): 172 staged
rows `S052..S223` and 81 staged knowledge files, covering OIDC federation, secret scanning,
NIST/GB-T/ISO key-management standards and cloud KMS. None touches OpenBao seal/unseal,
Shamir, rekey or record-defect remediation, and the staged ids collide with this lane's
registry (`S124` at BASE). Evidence: `.ufo/waves/round-61/build/R61Connector/sweep.md` §2.

**considerthese:** the newest file (`considerthese/2026-10-26.md`) holds four proposals —
two already implemented (the `lane-status:` line, round 31), one stale (the
`release-clock.py` title-suffix defect resolved in round 45), and one (`BACKLOG.md`) that
does not fit this round's claims. None is mined this round; the connector recorded the
lane-bar evidence an implementation would need.

## Trend verdicts

- **expansion: improved** — three admitted tier-A rows (S125–S127) and one admitted entry on
  ground the coverage map did not hold (`git show c940f51:corpus/README.md | grep -ci 'seal'`
  ⇒ 0 at BASE; the tip adds the seal-key entry and the round-61 lesson rows), plus a
  capability row in `SCORECARD.md` with first-working round 61.
- **quality: improved** — seven routed record defects repaired append-only (the diff against
  BASE is additions only for `LOG.md`, `corpus/lessons/round-60.md`, `plans/round-60.md`),
  a gate that could not fail gained a real `--selftest` (36 cases), the new entry separates
  documented rule from measured mechanic and names its bounds and falsifiers, and the C2
  counter's vacuity class was closed in-round (QM80). The round also introduced defects it
  routed rather than hid: the trial's T4 decode inversion and the checker's I2 legs were
  found by seats and fixed before the candidate reading; the reviewer's five structural-item
  bypasses and the C2 guard/selftest debts stay open and are named as ceilings below.
- **discernment: improved** — the gate admitted three rows and refused one with a measured
  reason and a flip condition; the wave's attack seats changed the instruments before the
  candidate reading (critic: the T4 decode contract and the secret-scan false positive;
  reviewer: the trial syntax break, the C2 stub vacuity, five item bypasses; mutation-tester:
  22 mutants, 20 killed); and the disagreements became three grounded `QUALITY.md` criteria
  (QM78–QM80). The non-author closure spot-check of this round is the integrator's; this
  verdict is the lane's reading, and the round records that the reviewer and critic are lane
  seats, not outside reviewers.

## Ceilings and open debts (recorded, not smoothed)

- **C1 items are structural reads.** A tree that keeps every token but negates the statement
  (`not withdrawn`, `no three`, `not rewritten in place`) or swaps a pairing
  (`3/16 = 25 %`) reads the item satisfied — five such trees measured
  (`build/R61Reviewer/findings.md` §C1 I3–I7). QM79 is the next-round hardening; the round's
  own corrections are not negations.
- **I6's literal `-03:00` text is unsatisfiable against `%ci`'s `-0300`**; the checker
  compares instants after offset normalisation, which is the only reading under which the
  item can hold (lesson finding 1).
- **C2-4/C2-5 (open).** `guard` is near-constant (the mutation-tester's surviving mutant
  C2-M6) and the counter's `--selftest` does not execute the main aggregation (reviewer
  §C2-5: two mutations pass). Both are instrument debts for the next round; the round's own
  readings do not depend on them (`value=5` is driven by the five legs, not by `guard`).
- **Plan §Control plan drafting defect:** its forgery parenthetical lists eight descriptions
  for seven ids. The battery builds F1–F7; the displaced I7 description is covered by the
  reviewer's I7 attack, not by a control.
- **The plan's motivating grep overstates its negative:** no entry measures the *OpenBao*
  Shamir seal; `sops-age-key-rotation.md` does measure a Shamir threshold (SOPS key groups).
- **Write-scope slips recorded:** the scribe wrote three `.body.txt` locator files into the
  capture dir (removed; capture sha256s unchanged) and the controls seat left a `bash -x`
  trace under `/tmp` (3001 B, not evidence). Both are in the lesson `## Mistakes` (M61-4).

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — evidence: `SKILL.md` §Vault-ops decision table, §Failure table, §Credential-hygiene checklist; citation run `CITATION_GATE: CLEAN (cites=891 docs=53 unresolved=0 ephemeral=0 labeled=13)` (LOG.md:758); this round adds the seal-key entry's rows to the cited set.
- [~] At least one end-to-end domain task executed and logged in LOG.md — evidence: `LOG.md:1984` round-61 entry; `corpus/openbao-seal-trial.sh` executed twice against throwaway OpenBao 2.7.2 servers with receipts under `.ufo/waves/round-61/build/R61ExecTrial/`.
- [~] Instructions executable by an agent without oral context — evidence: the round's five instruments carry `--selftest` (52 / 36 / 63 / 11 / 18-control cases) and the trial runs from `plans/round-61.md` §C2 alone; `bash corpus/openbao-seal-trial.sh --selftest` runs with no `bao` and no network.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — evidence: `PROVINCE.md` §Surfaces and the round-61 connector sweep (21 lanes; no sibling holds seal/Shamir/rekey/generate-root ground); the contested CDP/musketeer surfaces stay reported, not absorbed; `ADJACENCY_SCOPE: DEFECT` unchanged and named.

## Stale-lane

Driver line `2026-11-07T16:45:05-03:00 launch kagi round=61 pgid=672160 driver=hyaku-inline
attempt=1`; lane commits `8595018` (16:49:16 −03) and `08f950d` (17:41:50 −03) are inside the
window, and the wave's 16 seats all settled — the mission is **progressing**, not stale.

## Tool installs

None. No tool was installed, upgraded or removed by the L1 or any seat; the round used
`bash`, `python3`, `curl`, `git` (read-only) and the already-present `bao` v2.7.2
(sha256 `9c5f3628…`). The pacman guard was respected (no package transactions).

## L0

No new operator decision is required this round. The rekey divergence is a measured
documentation gap, not a decision.
