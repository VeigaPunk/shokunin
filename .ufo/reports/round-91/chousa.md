# chousa — round 91 (hyaku, run 15)

Lane `chousa`, round `91`, attempt 1. Base `265b8633b7e5d1da49da6fb948df9707373fb15c` (round-90 landing + its
non-author spot-check). Claim freeze `F3 = 4d00d7519290569879f853d7122b82a927cda1f3`; receipts carrier
`C3 = 67954adc599bd605705d94a1ea7abb582491a907`. Two earlier freeze/carrier pairs (`160b658b`/`d02a950f`, then
`37831ce8`/`b8fc99a1`) were superseded before any scored run and before the wave (plan §§Pre-wave freeze repair 1–2;
lesson Mistakes 1–2 and 8).
Shape: one v1 wave, 12 seats, policy band 8–16. Three claims, three axes, no exploratory claim.

Stale-lane: respawn-per-round driver; no other mission of this lane is open. Final lane tip `406ac4741764ade04eefbee0f3127c453c03420a` (push verified by `ls-remote`).

## Work performed

Declared claims (frozen in `corpus/evidence/round91/claims.md`, machine form `.ufo/waves/round-91/claims.json`):

- **C1 operability (lowest scored non-retired axis, historical 3/10)** — the control-receipt driver's header keys are
  single-valued, `# expected_exit=` is enforced, every executed instrument and the expectations file is pinned in
  `instrument-pins.txt` and verified on disk and at `--rev`, `SELF_PIN` names both revisions, unscored receipts are
  refused, and `--root`/`--repo` are separate bases (QUALITY 202). Source: S070.
- **C2 calibration** — every `## Located quotes` row is counted or refused with its shape named, every cited source's
  `status`/`used-by` is read, the warrant share is guarded by a document-frequency test (`DF_MAX=3`, measured), and
  the unentailed double-count loop is replaced by one record per (row, term).
- **C3 freshness** — the `SKILL.md` case-range prose re-derives from the tool's own `ok-case` names: the
  `bash-pin-override` family is 282–283 (not the prose's 276–283) and the r39 `bashenv` family is 273–275.

Work items:

- `corpus/evidence/round91/control-driver-r91.py` (the C1 successor driver, 345 lines) — the C1 successor driver: `header_multi()` +
  `check_headers()` (one value per required header key), `pin_report()` (instrument + expectations pins on disk),
  `self_pin()` names `rev=` and `receipts_rev=`, `rel_for()` with an explicit base and a printed `BASES` line,
  `UNSCORED_RECEIPT` only for files that parse as receipts.
- `corpus/evidence/round91/control-forgeries-r91.py` — six-class battery; `FORGERY_REFUSED=6/6 PRIOR_ACCEPTED=6/6
  POSITIVE=pass` (`after/c1-forgeries.txt`).
- `corpus/evidence/round91/controls/expected.tsv` + `controls/receipts/` — six scored rows, emitted at F3, carried at C3; `c1-harm` now compares the tool at the frozen base `265b8633` with the landed tool (routed defect 3).
- `corpus/evidence/round91/curation-r91.py` — 13-leg successor counter (`QSHAPE`, `SOURCE`, `TFREQ`, fixed
  `UNENTAILED`); clean-tree line in `after/c2-counter.txt`.
- `corpus/evidence/round91/curation-r91-controls.py` — four tree forgeries + the double-count probe + the seven closed
  round-90 forgeries as regression (scored through a token-renaming alias, QUALITY 208).
- `corpus/evidence/round91/skill-tally-r91.py` + `skill-tally-r91-controls.py` — the case-range leg, the committed
  283-case selftest receipt, and the old-prose/stale-tally controls.
- `SKILL.md` one-clause repair: `r39 bash-pin cases 273–275 (pin-bashenv, drift-bashenv) and r82 pin-override cases
  276–283, of which bash-pin-override cases 282–283` (was `… bash-pin-override cases 276–283`).
- Source work: S070 re-opened (installed `sha256sum(1)`, unchanged sha), S001 re-opened with a rev-form Gate record
  (`tools/research-gate.sh:9010`), S221 attempted and refused (`curl rc 28`, no bytes).
- Wave evidence under `.ufo/waves/round-91/`: `w1-spec.json`, `w1-dispatch.json`, `w1/swarm-registry.json`,
  `w1.ready`, the 12 seat reports, `w1-results.json`, `claim-falsification.tsv`.

### Wave settlement (12 seats, 0 dead)

One v1 wave, policy band 8–16: 3 executor, 3 reviewer, 1 critic, 1 mutation-tester, 1 sentinel, 1 connector, 1 scout,
1 revenger — attack share 8/12 = 67 %, one connector seat, 0 dead. The wave fired on all three claims; 24 amendments
(`plans/round-91.md`) narrow each sentence to the instrument's measured behaviour and every one names its artifact.
The load-bearing findings: the frozen C1 command omits `--work` (exit 2 verbatim); a stub at the instrument's path
prints the predicate and the pins file is not self-pinned; the per-row read order is not the cross-row protection (a
receipt can go unread without `--repo`); the pin rule is lexical (a data operand first bypasses the executed script);
the dual-base form is asymmetric; C2's row filter drops a first-cell-empty/`:`/`Situation` row before QSHAPE, a 5-cell
decision row carrying both defect terms passes, `used-by` is a substring test and `df(source)` is 5 not 7; C3's
prefix-preserving rename is invisible, the clause regex is document-wide and the shipped r82 block range is unbound.
The connector's read-only scan maps last-wins parsers in seven sibling lanes and the absence of any term-frequency
guard in all twenty; `read_pins()` carries the same last-wins class in this lane (routed). The scout finds no
registry/capture/count drift and corrects the S070 quote to its rendered roff form.

## Landed changes

| commit | change | LOG entry |
|---|---|---|
| `7b19dd0b` | round-91 egress table, committed before the first fetch | Round 91 |
| `4d00d751` (F3) | freeze: claims, plan, six instruments, expectations, pins, before receipts, selftest receipt | Round 91 |
| `67954adc` (C3) | carrier: six control receipts emitted at F3 | Round 91 |
| `0c85c9ac` | wave-1 spec/dispatch/registry re-rendered at F3/C3 | Round 91 |
| `f4f1a116` | landing: SKILL.md clause, after receipts and procedure, lesson, QUALITY 203–210, SCORECARD, LOG, census, wave evidence | Round 91 |
| `406ac474` | LOG amendment-count correction (final lane tip) | Round 91 |

## Before → after measurements

Counting commands are run from the lane root; `F3`/`C3` are the hashes above.

| claim | before (measured) | after (measured) | command | measured at |
|---|---|---|---|---|
| C1 | `PRIOR_ACCEPTED=6/6` — the r90 driver accepts all six classes; its `header_fields()` keeps the last header value and it never reads a pin (`controls/receipts/c1-before.txt`) | `COMMITTED_OK=6/6 EXACT_OK=6/6 PIN_OK=6/6 FRESH_OK=6/6 PINNED_FILES=6 CONTROL_DRIVER_R91=PASS`; `SELF_PIN OK rev=F3 receipts_rev=C3`; `FORGERY_REFUSED=6/6` (`after/c1-verify.txt`, `after/c1-forgeries.txt`) | `git diff --quiet F3 -- <the six instruments, controls, selftest receipt, instrument-pins.txt, controls/expected.tsv, round90/control-driver-r90.py>` and `git diff --quiet C3 -- controls/receipts` (Amendment 10), then `python3 -B corpus/evidence/round91/control-driver-r91.py verify --root . --repo . --work <scratch> --rev F3 --receipts-rev C3` and `python3 -B corpus/evidence/round91/control-forgeries-r91.py --work <scratch>` (Amendment 7) | `f4f1a116` |
| C2 | r90 prints `CURATION_R90=PASS` on all four forged trees, `PRIOR_ACCEPTED=4/4`, and `UNENTAILED_TERM=2` for one row (`controls/receipts/c2-before.txt`) | `CURATION_R91=PASS`, `LEGS_MEASURED=13/13 Q_ROWS=20 Q_SHAPE_FAIL=0 SOURCE_STATUS_OK=20/20 USED_BY_OK=20/20 TFREQ_OK=17/17 TFREQ_MAX_DF=3 UNENTAILED_TERM=0 WARRANT_OK=17/17`; `CONTROLS=PASS FORGERY_REFUSED=4/4 PRIOR_ACCEPTED=4/4 DUPCOUNT_R90=2 DUPCOUNT_R91=1 PRIOR_REGRESSION=7/7` (`after/c2-counter.txt`, `after/c2-controls.txt`) | `python3 -B corpus/evidence/round91/curation-r91.py --root .`; `python3 -B corpus/evidence/round91/curation-r91-controls.py --root . --work <scratch>` | `f4f1a116` |
| C3 | r90 prints `SKILL_TALLY_R90=PASS` on the base `SKILL.md`; r91 on the same bytes prints `CASE_RANGE_OK=1/2 MISLABELED=6` (`controls/receipts/c3-before.txt`) | `SKILL_TALLY_R91=PASS`, `TALLY_ROWS=9 STALE_TALLIES=0/9 EXPECTED_CASES=283 EXPECTED_SKIPPED=0 OTHER_OCCURRENCES=3 CASE_RANGE_BASHENV=273-275 CASE_RANGE_BASH_PIN=282-283 CASE_RANGE_OK=2/2 MISLABELED=0 LEGS=2/2`; `CONTROLS=PASS OLDPROSE_REFUSED=1/1 PRIOR_ACCEPTED=1/1 STALE_REFUSED_BOTH=1/1` (`after/c3-counter.txt`, `after/c3-controls.txt`) | `python3 -B corpus/evidence/round91/skill-tally-r91.py --root . --selftest corpus/evidence/round91/controls/selftest-r91.txt`; `python3 -B corpus/evidence/round91/skill-tally-r91-controls.py --root . --work <scratch>` | `f4f1a116` |

A do-nothing control cannot reach any after-state: the r90 driver/counter on the same trees prints
`PRIOR_ACCEPTED=6/6`, `PRIOR_ACCEPTED=4/4` and `SKILL_TALLY_R90=PASS` (before receipts above), i.e. no claimed value is
reached without this round's bytes.

## Sources & frontier

- Census command, start and end:
  `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin chousa`
  → **exit 0** both times; `chousa ok …/corpus/SOURCES.md`; same five pre-existing `W04` duplicate-URL warnings
  (`S051`, `S053`, `S073`, `S074`, `S075`). Receipts `corpus/evidence/round91/census-start.txt`,
  `census-end.txt`.
- Rows: **219 → 219** (`grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}' corpus/SOURCES.md`). Rows added by tier: none.
  Rows touched old→new: none (no `status`/`recheck`/`used-by` change). Frontier rows advanced: none — this round's
  gain is instrument and prose binding, not corpus ground.
- Re-opened this round: **S070** (installed `sha256sum(1)`, `93c17dff…` unchanged; quote "Print or check SHA256
  (256-bit) checksums.", 7 words) and **S001** (rev-form Gate record at `tools/research-gate.sh:9010`, 4 words).
  Attempted and refused: **S221** (IR textbook document-frequency page, `curl rc 28`, no bytes; no row written).
- `Assimilation: none` — no `merge/chousa/` package was adopted this round; the run-15 wave-4 quarantine list was
  completed in an earlier round and no package bytes were re-opened.
- `considerthese/2026-11-07.md` proposal 1 (the duplicate-wins watch) is applied to the receipt header surface (C1)
  and the quote-row shape (C2); no other proposal acted on.

## Trend verdicts

- **expansion: unchanged** — registry 219 → 219 rows; no new knowledge entry; the source work is a re-open and a
  refused fetch, not new ground.
- **quality: improved** — C1/C2/C3 each verified with a red-before witness re-derived from committed bytes (six
  forgery classes, four tree forgeries + the double count, the mislabelled case range), and the round's own wave
  findings became QUALITY 203–210.
- **discernment: improved** — the freeze was re-cut once before the wave after its own emit/verify found two defects;
  the wave's attacks and the ledger are recorded below; no claim is filed wider than its instrument.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — `SKILL.md` Gates table;
  nine tallies and the case-range clause re-derived this round (`after/c3-counter.txt`); no non-author verifier for
  the skill as a whole.
- [~] At least one end-to-end domain task executed and logged in LOG.md — round-91 LOG entry; the three counters run
  end to end from a clean clone (`after/c1-verify.txt`, `after/c2-counter.txt`, `after/c3-counter.txt`).
- [~] Instructions executable by an agent without oral context — `corpus/evidence/round91/claims.md` carries every
  command and expected line; five wave seats re-ran them from clean clones and two found the frozen C1 command's
  missing `--work` (Amendment 7), which is the honest limit of this box.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — `PROVINCE.md` untouched; the connector seat's sibling scan
  is read-only and absorbs nothing.

## Prefile falsification

`python3 /home/vgpnk/Projects/shokunin/scripts/hyaku/prefile-falsification.py --lane chousa --round 91` →
`PREFILE-FALSIFICATION: pass claims=3 rows=34 attack_seats=8 findings=0`, exit **0**. The ledger
`.ufo/waves/round-91/claim-falsification.tsv` carries 34 rows over C1/C2/C3 and names all eight attack seats
(`R91ReviewerC1/C2/C3`, `R91CriticClaims`, `R91ExecMutations`, `R91SentinelScope`, `R91ConnectorSiblings`,
`R91RevPrior`); every artifact resolves under `.ufo/waves/round-91/`; each `falsifies-wording` row names its
Amendment in `plans/round-91.md`; no row is unreconciled.

## Process notes

- Selftest: `bash tools/research-gate.sh --selftest` → `RESEARCH_GATE_SELFTEST: PASS (283 cases, 0 skipped)`
  (6m04s, receipt `controls/selftest-r91.txt`); `tools/research-gate.sh` and `tools/gate-records.py` are unchanged
  this round.
- `python3 -B tools/gate-records.py verify --root . --repo . corpus/lessons/round-91.md` → `GATE_RECORDS files=1
  records=1 ok=1 fail=0`, exit 0 (the S001 rev record; the first draft said `words=5`, the gate printed
  `FAIL WORDS`, corrected to 4 before the lesson was committed).
- Tool installs: none.
