# kaidoku — round 72 report

Lane `kaidoku-shokunin`, round 72, attempt 1. Base `56241b1c8baff95862730c008f1ae5132b03388e`;
declaration `6316c1053f927a1a1cdc3e0960b70acab5f56381` (six round-72 instruments, the plan, the
nonce commitment, the census start) with four pre-freeze declaration fixes
(`17d8b5f7`, `306cbb3f`, `25ecc711`, `1563ea35`); operative freeze
`34fe7aa70b627d92e2d27dbce308d9f5bebda63d` (the round-29 freeze gate audits it CLEAN, findings
[], `l1/scores/gate-at-freeze.json`); record gate at `722edc98` CLEAN, disclosures exact, missing
[] stray [] (`l1/scores/gate-at-record.json`). Lane tip and pushed branch:
`05bf065684e52d72ea25aad95f7acb71fcd7874c` (`git ls-remote origin refs/heads/main`).

## Work performed

Three declared claims on three distinct axes, all capability acquisitions; the stagnation nudge
applies (every owned axis 10.0, saturation 10.0, window 10) so the lowest-axis obligation is
waived. The round picks up the round-71 report's own queue (a)–(c) and closes five wave findings
in-round under disclosed supersessions.

- **R72-C1 (coverage; checker-mode child environments, Frontier → Core).** `--check-receipt`'s
  `git` (tool blob) and `readelf` (carrier format) children now run under `build_child_env()` and
  are recorded into `--child-env-log`; the checker JSON carries `checker_child_env` and a
  re-derivable `clauses` block. The probe's new A11 reads the checker's log bytes itself and
  cross-checks independent perl shims. Evidence: `l1/scores/c1-at-landing.json` (11/11,
  `A11_checker_env` true, log-derived `{git: 1, readelf: 4}`, containment under the checker's
  `run_root`); base `l1/scores/c1-at-base-final.json` (9/11, shim canary present); independent
  re-derivations `.ufo/waves/round-72/w1/ExecC1.md`, `ExecC1Base.md` (five 275-key inherited
  records at base).
- **R72-C2 (calibration; the checker-emitted binding verdict).** A10 no longer re-derives a
  binding boolean from receipt fields: `binding_verdict()` reads the checker's
  `clauses.run_nonce`/`clauses.run_binding`, `checker_met()` requires the checker's `met` and
  `clauses.met` to agree, and the frozen `A10_binding_force_true` self-mutant — MutReaders
  survivor i in round 71 — is killed by the named case `a10-binding-from-checker`. Evidence:
  `l1/scores/c2-at-landing.json` (killed, `failed ["a10-binding-from-checker"]`, pristine 13
  cases green); base `l1/pre/c2-at-base.json` (survivor 1). Independent re-derivation
  `.ufo/waves/round-72/w1/ExecC2.md` (scratch mutant applied and restored by the seat).
- **R72-C3 (operability; raw-witness capsule audit).** `capsule-audit.py`/`capsule_audit.py`
  re-derive seven clauses from the capsule bytes; the checker audits an explicit `--capsule` or a
  resolvable filed capsule, fails closed on a named-but-absent lane-relative capsule, and never
  reads a receipt-named path outside the lane. Evidence: `l1/scores/c3-at-landing.json` (genuine
  46-record capsule accepted; 7/7 shapes rejected with named clauses), `c3-genuine-filed.json`
  (`receipt_capsule true`), `c3-lying-check.json` (`receipt_capsule: canary`, clause false); base
  `l1/pre/c3-at-base.json` (the round-71 checker accepts the lying receipt, `met true`, no
  clauses). Independent re-derivation `.ufo/waves/round-72/w1/ExecC3.md`.
- **Wave.** One v1 wave `r72-w1`, 16 seats: 5 executor, 3 scribe, 2 reviewer, 2 mutation-tester,
  1 critic, 1 sentinel, 1 scout, 1 connector; attack roles (reviewer/critic/mutation-tester) 5/16
  = 31%; one connector; the L1 held the planner seat. All 16 settled, none dead
  (`r72-w1-results.json`). Seats reproduced the claims independently (`ExecC1`, `ExecC1Base`,
  `ExecC2`, `ExecC3`), ran the standing duties (`ExecSweep`), attacked the instruments
  (`ReviewerGates`, `CriticClaims`, `MutProbe`, `MutReaders`, `SentinelScope`), opened the source
  (`ScoutSource`), scanned siblings (`ConnectorCross`) and drafted the record (`ScribeKnowledge`,
  `ScribeLesson`, `ScribeRecord`).
- **Controls.** `l1/scores/controls-at-landing.json` 5/5: base world 9/11, constant probe
  rejected, r71 mutant survivor 1, constant mutation receipt rejected, and the round-71 checker
  accepting the lying receipt while the audit rejects it (the strict `met_control` gates the
  aggregate).
- **Record.** `LOG.md` round-72 landing entry; `SCORECARD.md` three capability rows and the round
  section; `PROVINCE.md` `## Round-72 additions to Core` + frontier note; `corpus/README.md` index
  row and frontier note; `corpus/QUALITY.md` rows 123–128; `corpus/knowledge/2026-11-04-r72-checker-env-capsule.md`;
  `corpus/lessons/round-72.md`; `SKILL.md` registry rows for the six instruments.
- **Security incident (reported).** The `ExecC1` seat's raw `caller-env.txt` carried live
  credential values (1Password service-account token, OpenAI Codex token). GitHub push protection
  blocked the record commit; the file is replaced by a key-name census
  (`w1/ExecC1/caller-env.redacted.txt`), the unpushed commit was rewritten to drop the raw dump,
  and the pushed range was re-scanned for token shapes and is clean. No secret was pushed;
  QUALITY row 128 binds the lane rule; the L0 line is filed.

## Landed changes

| change | LOG entry | commit |
|---|---|---|
| six round-72 instruments + plan + nonce commitment + census start | round-72 land | `6316c10` (fixes `17d8b5f`, `306cbb3`, `25ecc71`, `1563ea3`) |
| pre receipts (both route worlds, base probe/mutation/capsule, controls) | round-72 land | `f6f4f67`, `8ce89ea`, `1563ea3` |
| claims container (three predicates, six instrument pins, five loaded-by-counter pins) | round-72 land | `34fe7aa` |
| wave spec, dispatch and validated ready file | round-72 land | `a08dba7` |
| supersession 1 — probe scratch copy carries `capsule_audit.py` | round-72 land | `6375afe` |
| supersession 2 — perl A11 shim; battery scratch sibling module | round-72 land | `6284abe` |
| supersession 3 — A11 log-derived census, capability fail-closed, strict control aggregate, `--receipt-rev` | round-72 land | `4913b5e` |
| supersession 4 — pure `a11_verdict` per conjunct; checker `met` agreement | round-72 land | `d8297e8` |
| supersession 5 — capsule read containment + `/usr/bin` preference (SentinelScope) | round-72 land | `e67f3a1` |
| supersessions 6–7 — control receipt revision | round-72 land | `72eeeca`, `2b5e894` |
| the record (sources, knowledge, lesson, QUALITY, PROVINCE, README, SCORECARD, SKILL, wave evidence) | round-72 land | `750a2b0` |
| redacted `caller-env.redacted.txt` (secret removed before any push) | round-72 land | `8f0ce04` |
| LOG landing entry, QUALITY 128, lesson incident + L0 text | round-72 land | `b9ae323` |
| record correction: `e67f3a1` disclosed for packed-elf/seam-probe with final replacement sha256; registry census receipt | round-72 land | `722edc9` |
| CLEAN record gate receipt | round-72 close | `05bf065` |

## Before → after measurements

Each claim's counting command, verbatim, and the commit it was measured against.

1. **R72-C1** — `python3 -I -B tools/round-72/seam-probe.py --root . --rev e67f3a1b1f79bcd5ce56dd4f64edb4ed18f903ff --receipt-rev <route receipt rev> --tool <round-72|round-71>/packed-elf.py --battery <round-72|round-70>/mutation-check.py --pkg <REA 6.5.0 root> --work <scratch> --receipt <route receipt> --expect-upx <pinned copy> --nonce-commitment 2532bd5b… --json-out <receipt>`.
   Before: 9 of 11, failed `[A10_run_binding, A11_checker_env]`, shim keys
   HOME/LANG/PATH/PWD/SHLVL/TMPDIR/_ with `KAIDOKU_ENV_CANARY` present
   (`l1/scores/c1-at-base-final.json`, round-71 route at `6284abe`). After: 11 of 11, failed [],
   A11 true with both shims exactly HOME/LANG/PATH/TMPDIR, canary absent, HOME/TMPDIR under the
   checker's run root, log census `{git: 1, readelf: 4}` (`l1/scores/c1-at-landing.json`, round-72
   route at `e67f3a1`). Exit 0 met.
2. **R72-C2** — `python3 -I -B tools/round-72/mutation-check.py --root . --rev e67f3a1b1f79bcd5ce56dd4f64edb4ed18f903ff --tool tools/round-72/seam-probe.py --patch-set r72 --work <scratch> --json-out <receipt>`.
   Before: patch set `r71` on the round-71 probe at its freeze `b827a8b5` reports
   `survivor_count 1`, survivors `["A10_binding_force_true"]` (`l1/pre/c2-at-base.json`). After:
   the same mutant is `killed`, `failed ["a10-binding-from-checker"]`, pristine 13 cases green,
   target sha `39a2193e…` (`l1/scores/c2-at-landing.json`). A10's landing observation: genuine
   `{present true, nonce_ok true, binding_ok true}`, `genuine_met true`, wrong-nonce
   `nonce_ok false`, broken-binding `binding_ok false`. Exit 0 met.
3. **R72-C3** — `python3 -I -B tools/round-72/capsule-audit.py --tamper-battery --capsule .ufo/waves/round-71/l1/scores/c1-env-at-landing.jsonl --audit .ufo/waves/round-71/l1/scores/c1-env-audit.json --work <scratch> --json-out <receipt>`.
   Before: the round-71 checker on the lying receipt exits 0, `met true`, `failing []`, no clause
   object (`l1/pre/c3-at-base.json`). After: the battery exits 0 with the genuine 46-record
   capsule accepted and 7/7 shapes rejected naming their clauses (`l1/scores/c3-at-landing.json`);
   the round-72 checker accepts the filed genuine receipt with `receipt_capsule true`
   (`c3-genuine-filed.json`) and rejects the lying receipt with `receipt_capsule: canary` and
   `clauses.receipt_capsule false` (`c3-lying-check.json`). Exit 0 met.

Measurement note: the first base-probe attempt at `e67f3a1` recorded A8 rc 2 (one-carrier route
unevaluable) while the control's identical arm was green; the re-run at the same revision is the
receipt of record (`c1-at-base-final.json`) and reports A8 true.

## Sources & frontier

`corpus/SOURCES.md` 181 → 183 rows; census start `l1/census-start.txt` exit 0, end
`l1/census-end.txt` exit 0 (24 W04 duplicate-URL warnings, all pre-existing or the S276
restatement). Counting command:
`/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kaidoku`.

- **Rows added**: S275 (the man-pages 6.19 `proc_pid_environ(5)` page, tier A `docs`, opened
  2026-11-04, snapshot 7 747 B sha256 `93394d9e…`, 18-word located quote; the served `proc.5.html`
  is a 31 125-byte stub with only a SEE ALSO link — the assignment's premise corrected by the
  live fetch); S276 (the S274 column repair: reason and flip in `teaches`, scope clean,
  supersedes S274's cell contract only; rejected).
- **Rows touched**: S275 status `mined`, `used-by` the knowledge entry and `ScoutSource.md`;
  S276 `rejected`, `used-by` the round lesson. S274 is never rewritten.
- **Search log**: the round-72 entry records the question, the two fetches, the 2 screened /
  1 included / 1 restatement split, and the stop rule.
- **Frontier**: `corpus/README.md` and `PROVINCE.md` record checker-mode child environments and
  the receipt-bound capsule audit moving Frontier → Core for the measured instruments, and name
  what stays Frontier (complete GFM parser, signed receipts, REA-internal/packer-internal
  children, a producer-independent child census, other packers/carriers, anti-UPX stubs, packed
  PE/Mach-O, semantic inventory equality).
- **Assimilation**: none — `merge/kaidoku/` does not serve these claims. `considerthese/` does not
  exist in this lane.
- **Mistake mined**: `corpus/lessons/round-72.md ## Mistakes` — the capture claim stopped at the
  mode; the round-71 mutation survivor was never bound to a failing case; a shell shim measured
  the shell; a control aggregate read the loose verdict. Each has a fix that can fail (a named
  case, a named clause, a sanitised fixture).

## Trend verdicts

- **expansion: improved.** One admitted knowledge entry on ground the coverage map held only as
  Frontier (checker-mode child environments) plus the new capsule-audit surface; registry 181 →
  183 rows; three capability rows enter the table beside the measured receipts. The frontier note
  names exactly what moved and what did not.
- **quality: improved.** The round-71 blind spot is closed at its surface, and five wave findings
  are fixed in-round under disclosed supersessions with replacement sha256 per entry (the
  round-71 container's missing-sha defect): summary trust, absent-capsule skip, strict control
  aggregate, contradictory-checker acceptance, and outside-lane capsule reads. The route receipts
  were re-taken after each packed-elf edit; the record gate is CLEAN. Four selftest-survivor
  classes are named debt, not smoothed.
- **discernment: improved.** The wave's critic/reviewer/sentinel falsified the first cut and every
  fix names its finding; the source seat reversed the assignment's premise with a live fetch and
  proved the id guard on an indented fixture; the lane reported the credential-capture incident
  and redacted before any push rather than rewording the record.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — evidence:
  `SKILL.md` registry rows for `tools/round-72/*`; `corpus/knowledge/2026-11-04-r72-checker-env-capsule.md`
  (decision table + witness table); `corpus/QUALITY.md` 123–128.
- [~] At least one end-to-end domain task executed and logged in LOG.md — evidence: the full
  4-carrier packed-ELF route at `e67f3a1` (46 observed children, receipt
  `l1/pre/route-at-declaration.json`) and its `LOG.md` round-72 entry.
- [~] Instructions executable by an agent without oral context — evidence:
  `plans/round-72-claims.md` counting commands; `tools/round-72/*.py --selftest` (35/13/13 cases);
  `.ufo/waves/round-72/w1/*.md` seat commands.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — evidence: `PROVINCE.md`
  `## Round-72 additions to Core` + frontier note; `ConnectorCross.md` finds no sibling owner for
  the checker-mode/capsule surfaces.

Named non-author verifier for these boxes: none this round (a dispatched seat does not count); the
non-author closure is the outside check.

## Extras

- **Stale-lane**: none — respawn-per-round driver; no other mission of this lane is open.
- **Tool installs/upgrades**: none; no pacman transaction (paused per the addendum guard).
- **Open L0**: the credential-capture question appended to `.ufo/l0-questions.md` (routed around:
  redaction and push-protection compliance, no secret pushed).
- **Routed defects for round 73**: (1) selftest coverage for the route's `env=` threading and the
  implicit-capsule path (MutReaders survivors a/b/c) and the remaining A11 auxiliary conjuncts
  (MutProbe); (2) `seam-probe`/`forged-receipts` scratch cleanup on failure (round-71 Sentinel
  SS-4); (3) a producer-independent census for a hostile-wrapper class (CriticClaims) or an
  explicit scope retirement; (4) the r63 record-section sweep; (5) the r58/r60 bare-name findings
  and the r64 placeholder-token disposition.
