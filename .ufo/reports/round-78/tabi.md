# tabi — round 78

Lane `tabi-shokunin`, round 78, attempt 1. Base `ae2dc25fe8b4db70d2ef8a83804bc5545fbc35ff` (lane clean,
`local=remote`, `ahead=0 behind=0`). Round 77 was **not admitted** (`corpus/lessons/round-77-verifier-spotcheck.md`:
C1 NOT VERIFIED, quality harmed); its eight routed defects are this round's spine.

## Work performed

Two claims:

- **C1 — coverage (9), capability `chromium-file-chooser-linux`, generation r78** (re-claim with the
  round-77 routed defects closed). Predicate `C1-FILECHOOSER-R78`, frozen in
  `.ufo/waves/round-78/claims.json`; final digests commit **D `bf94adaa`**.
- **C2 — calibration (9), capability-row status**: every capability row names a round whose claim-table
  verdict holds, or carries `provisional` naming the failed round; the named round must itself list the
  capability; counted by `scripts/check-capability-status.mjs`.

Work items (evidence pointers):

- **C1 instruments.** `scripts/chrome-cdp-filechooser-round78.mjs` (driver; records `frameTree` from
  `Page.getFrameTree` and `fixtureInputs` — the page's own tag/type/attributes/rect; its LEG_SHAPE and
  predicate compare chooser modes, not the assigned id), `scripts/check-filechooser-r78.mjs` (counter,
  186 checks; mode-only per-leg binding, `nodeReport`/`node-binding-law`, `fixture-descriptors`,
  `frame-tree`, full-argv equality, `receipt-fields` incl. `sweeps`, parse-every-file walk with a
  path-only exemption, `--tree-exempt` recorded, unreadable directories refused),
  `scripts/negatives-filechooser-r78.mjs` (battery, 400 cases incl. 32 carried R77Mut1 witnesses, the
  TOL 0.06 witness, count-aware gap cases and the MIN_OWN_GAPS accepting side),
  `.ufo/waves/round-78/controls/c1/kill-power-r78.mjs` (186 force-true + 76 semantic mutants),
  `scripts/selftest-r78-gates.mjs` (15 cases). Pins: `.ufo/waves/round-78/freeze.txt` (14 files, all
  matching at D).
- **Pre-freeze gates on final bytes** (executed, committed): counter 7/7 clean, battery 7/7 `allOk`
  (400/400 each), kill power holds on p1, s1, s2, s3 —
  `.ufo/waves/round-78/controls/c1/pf/out/prefreeze-summary.json` (`allOk: true`).
- **Controls.** No-work: the r77 scored receipt under the r78 counter exits 1 with 9 findings
  (`lesson-proof/c1-nowork.json`). C2: base exits 1 (r77 row on a NOT VERIFIED verdict); a relabel of
  the verified row to round 75 exits 1 (that round does not list the capability); `provisional` without
  a round exits 1; the current tree exits 0 with `provisional 1` (`lesson-proof/c2-controls.json`).
  Walk escapes: escaped schema, contradictory nonce, unreadable directory, decoy argv, frame-tree
  mismatch, receipt-field extra, sweeps shape — refused (`scored/c1-negatives-a.json`).
- **Scored run (post-D).** `corpus/evidence/round78/chromium-file-chooser/receipt.json`, nonce
  `tabi-r78-l1-bf94adaab578`: counter exit 0 clean, 186 checks, 11 priors (`scored/c1-counter-a.json`);
  battery 400/400 `allOk` (`scored/c1-negatives-a.json`); kill power holds, force-true 186/186, semantic
  76/76, no survivors (`scored/c1-killpower-a.json`); selftest 15/15 exit 0
  (`.ufo/waves/round-78-seats/L1-selftest/selftest-r78-gates.out`).
- **Cold-run acceptance (leg b).** `scored/cold-runs.txt` lists five committed cold runs (cold1,
  R78Exec1, R78Exec2 d1–d3), each counter exit 0 clean 186 — zero honest refusals (round 77 refused 2 of
  25). The scored receipt's `nodeReport` carries a drifted id (pick-multiple 10) and is accepted by design.
- **C2 repair.** `SCORECARD.md` capability rows: the historical r77 row reads `provisional r77`, the r78
  row reads `round 78`; `scored/c2-after.json` exits 0, rows 11 / claimed 10 / provisional 1 /
  mismatches 0.
- **Corpus.** `corpus/knowledge/chromium-file-chooser-runtime-round-78.md` (S208–S215 + wave
  corrections), `corpus/SOURCES.md` S214/S215, `corpus/QUALITY.md` 151–154, `corpus/README.md` round-78
  coverage, `corpus/lessons/round-78.md` (Gate, 9 Mistakes rows with red states, Corrections),
  `SKILL.md` `## Round 78 gate registry`, `LOG.md` round-78 entry.
- **Misroot sweep.** `git -C /home/vgpnk/Projects/shokunin status --porcelain` shows four untracked
  fleet-root files (`dropped-volatile.txt`, `f.txt`, `host-list-final.txt`, `trail-ids.txt`) and
  `.scratch/*` state; none names this lane or round, so none is copied or deleted.
- **Inherited state.** No uncommitted lane-authored leftovers at base. The round's own re-freeze history
  is disclosed in `SCORECARD.md` Correction 6 and `lesson-proof/`.

## Landed changes

| Change | LOG entry | Commit |
|---|---|---|
| r78 instruments, pre-freeze receipts/controls, claims, S214–S215, note, QUALITY 151–154, README, lesson | round 78 bullet 1 | `e866ca7c` |
| pre-freeze repair: driver LEG_SHAPE binds modes, not the assigned id; receipts re-produced | round 78 bullet 1 | `3289c1d0` |
| battery brackets state their decisive property; pre-freeze batteries re-run | round 78 bullet 1 | `3a9caf6a` |
| battery bytes of the first D and final pre-freeze outputs | round 78 bullet 1 | `8384256d` |
| re-freeze: battery deduped/TOL witness, kill-power mutant corrected, capability-status structural rules, selftest output moved out of the walked trees | round 78 bullet 1 | `d986c273` |
| re-freeze: counter refuses unreadable walked directories, reads `sweeps`, records `treeExempt`; battery count-aware gap cases | round 78 bullet 1 | `a4d628c8` |
| re-freeze: MIN_OWN_GAPS accepting side; kill-power cleanup tolerates the locked-dir case | round 78 bullet 1 | `4920e079` |
| **final D `bf94adaa`**: battery `forceRm` mirror cleanup, 400 cases; pre-freeze pass on final bytes | round 78 bullet 1 | `bf94adaa` |
| scored evidence under D, cold-runs ledger, wave seat evidence/reports, corrections | round 78 bullets 2–4 | `e98b588b` |
| late seat evidence (connector scan digest, review sweep) | round 78 bullet 4 | `a74da97f` |

## Before → after measurements

| Claim | Counting command | Before | After | Measured against |
|---|---|---|---|---|
| C1 | `node scripts/check-filechooser-r78.mjs --lane <lane> --receipt corpus/evidence/round78/chromium-file-chooser/receipt.json --expect-driver-sha256 0ae89d92…523f --expect-nonce tabi-r78-l1-bf94adaab578 --prior-set .ufo/waves/round-78/controls/c1/prior-set.txt --json` | r77 scored receipt under the r78 counter: exit 1, 9 findings (`lesson-proof/c1-nowork.json`); no r78 receipt at base | exit 0, `clean`, 186 checks, 11 priors; battery 400/400; kill power holds; selftest 15/15 | D `bf94adaa`; scored run `e98b588b` |
| C1 leg (b) | same counter on each committed cold run (`scored/cold-runs.txt`) | round 77: 2 of 25 honest runs refused on the pinned id | 0 refusals in 5 cold runs | D `bf94adaa` |
| C2 | `node scripts/check-capability-status.mjs --json` | exit 1, `mismatches 1` (`lesson-proof/c2-before.json`) | exit 0, `mismatches 0`, rows 11, claimed 10, provisional 1 (`scored/c2-after.json`) | base `ae2dc25f` vs `bf94adaa` |

## Sources & frontier

Counting command (frozen): `grep -cE '^\| S[0-9]{3,}' corpus/SOURCES.md` → **213 → 215**; census
`scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin tabi` **exit 0 at start**
(`census/start.txt`, 213 rows at base) and **exit 0 at end** (`census/end.txt`, 215 rows; W04 warnings
only, all pre-existing second scopes).

- Rows added: **S214** (Playwright `class FileChooser`, `docs`, tier A for Playwright's own contract,
  `mined`) and **S215** (Puppeteer `Page.waitForFileChooser()`, `docs`, tier A, `mined`), opened this
  round (http 200, bytes/sha256 in `sources/FETCH.txt`, raw HTML staged). Gate records with located
  quotes are in `corpus/lessons/round-78.md` `## Gate`.
- Rows touched old→new: none.
- Frontier rows advanced: the file-chooser surface moved from a capability entered on an unverified claim
  to a verified generation bound to page-measured elements; the frontier list now names
  `HTMLInputElement.showPicker()` under interception (R78Exec3) and a sha256-bound `--tree-exempt` (r79).
- Assimilation: none — `merge/tabi/` adoption stays closed pending the open L0 `tabi | round-57`;
  `considerthese/` does not exist in this lane.

## Trend verdicts

- **expansion — improved.** Knowledge 90 → 91 on ground the coverage map did not hold (page-side element
  binding, frame-tree anchor, path-only walk exemption), citing S208–S215; registry 213 → 215 with both
  new rows `mined`; the capability row moved to a verified round.
- **quality — improved.** The r77 red gate generation (selftest 11/13) is replaced by a green one
  (15/15) whose per-prior needs are derived; the battery grew 336 → 400 cases with the carried
  witnesses and count-aware brackets; kill power kills 262/262 mutants with no survivors; the counter
  no longer pins a browser-assigned id, and the producer's own check was repaired the same way.
- **discernment — improved.** The round's cold-run leg caught a defect in its own producer layer before
  any scored verdict; the wave's 12 seats falsified the claim twice (stale-state leg (c), then the limit
  sentence), both are on the record as corrections, and R78Critic's final verdict on the frozen bytes is
  HOLDS with no leg false. C2 turns self-assessment into a counted instrument with red/green controls.

## Round shape

- One v1 wave `w1`, **12 seats** (spec `w1-spec.json`, dispatch `w1-dispatch.json`, ready `w1.ready`):
  4 executor, 3 reviewer, 1 critic, 1 mutation-tester, 1 scout, 1 connector, 1 scribe. Attack share
  5/12 = 41.7 % (≥25 %). The L1 holds the planner seat (the validator rejects `planner`). No residual
  call.
- All 12 seats settled (`w1-results.json`), none dead. Verdicts (reports under
  `.ufo/waves/round-78/w1/<seat>/report.md`): R78Exec1 HOLDS, R78Exec4 HOLDS, R78Critic **HOLDS**
  (final, on D `bf94adaa`, no leg false); R78Exec2, R78Exec3, R78Review1, R78Review2, R78Review3,
  R78Scout, R78Connector, R78Scribe, R78Mut1 FINDINGS.
- R78Mut1: 95 single-edit semantic mutants beyond the frozen 76, on the frozen counter bytes
  (`4ae29412`): 46 killed by a named case, 28 killed-positive (false refusals), **21 survived**, 0
  crashed; the survivor set is identical on the D-era bytes. The survivors are routed to r79 as battery
  cases and are not claimed closed; leg (c)'s kill power (the frozen 262-mutant set) holds independently.
- Route map: `task.agentModelOverrides` in `~/.omp/agent/config.yml` (read, never changed); no `model`
  passed. Scratch: `/fast/scratch/hyaku/tabi-r78/…`, removed after use; no `/tmp` evidence.

## Corrections the wave forced (all on the record, none a leg)

1. **Limit sentence (R78Critic F3).** The escape minimum is `N_p - absNeed + 1` events AND
   `G_p - gapNeed + 1` gaps (40 and 3 for the 79/11 priors), not `absNeed`/`gapNeed`; F3 scores clean
   186 and is outside the frozen sentence. Disclosed in `SCORECARD.md` Correction 5 and
   `corpus/lessons/round-78.md` Corrections 1; r79 prints the escape minimum beside the threshold.
2. **Counter defects found by R78Review1** (locked-dir refusal, `sweeps` read, `treeExempt` emitted) are
   fixed in D; the ENOENT-vs-EACCES distinction, `sweeps` value validation, the frame-tree raw capture
   and F2/F3/F6/F7/F9/F10 are routed to r79, not claimed closed.
3. **Note locators** corrected in the note's `## Corrections` section (S210:203, 24/25 runs, the
   frame-tree anchor's limit, `--tree-exempt` scope, the unparsable-file rule, consistent swaps).
4. **C2 limit**: the counting command alone is satisfiable by labelling every row `provisional`; leg (c)
   fixes the count at 1 and the round at 78 (`SCORECARD.md` Correction 7).
5. **Re-freeze history** (D `d59ca027` → `d986c273` → `a4d628c8` → `4920e079` → **`bf94adaa`**) with the
   reason for each step is in `SCORECARD.md` Correction 6; superseded scored receipts are never edited.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — `SKILL.md`
  `## Round 78 gate registry` (entry command, verdict map, self-test, pinned path); author-attested.
- [~] At least one end-to-end domain task executed and logged — the scored file-chooser run and its
  gates (`scored/`), LOG round-78 entry; author-attested.
- [~] Instructions executable by an agent without oral context — `corpus/knowledge/chromium-file-chooser-runtime-round-78.md`
  §1–§6 plus `run-scored.sh`/`run-scored-gates.sh`; author-attested.
- [~] No cross-domain bleed — `PROVINCE.md:3-19` unchanged; R78Connector's sibling scan in
  `w1/R78Connector/report.md`.

## Lane state

Final lane tip `f1697b6fcfa774297989c9dcde5075a9a2e04b84` (`master`, `ls-remote` verified), clean,
`ahead=0 behind=0`; digests commit D `bf94adaa`; report commit cited in the closure.

## Stale-lane

Respawn-per-round driver; no other mission of this lane is open. One L1 (`TabiR78`), no respawn.

## Tooling

No tool installed or upgraded this round (no pacman transaction; nothing added to `~/.local/bin`).

## Open L0

`tabi | round-57` (assimilation adoption) remains open and is routed around: `merge/tabi/` adoption
stays closed. No new L0 question this round.
