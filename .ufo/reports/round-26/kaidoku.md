# kaidoku — round 26 report (attempt 1)

Lane repo `/home/vgpnk/Projects/shokunin/kaidoku-shokunin`, branch `main`. Pushed lane tip at filing: `ae8bcd860e2ee0e187f66bd2f047cc40b905ede1` (every lane commit below came from `jj-lane.sh` printing `landed <hash>` after remote verification). Lane-round base `a0639d8e61e486e2a716ff94cddd89a73200a02c`. Dispatched 2026-10-22T11:54:44Z; claims frozen at 12:01Z; wave 1 dispatched 12:11Z, wave 2 at 12:58Z; report filed before the 2 h scope freeze. No earlier attempt of round 26 exists (`.ufo/watchdog.log` has no `lane-dead-no-report kaidoku round=26` line), so nothing was inherited. Stale-lane: respawn-per-round driver; no other mission of this lane is open.

## Work performed

Declared claims, frozen definitions-first at `c27f445e70cedbaf5300b2fd0a53e821d9b659a9` (`.ufo/waves/round-26/claims.json`; one pre-freeze shape probe disclosed there):

- **R26-C1, depth (learning claim, sourced claim).** An evidence-ID identity table for eight native reader verbs (`analyze`, `inspect`, `decompile`, `xrefs`, `read-bytes`, `function`, `instructions`, `inspect-binary-layout`) at `rea-agents@6.5.0` on `/usr/bin/jq`: base, same-path repeat and a byte-identical copy in another directory, each verdict re-derived from three committed envelopes, plus a knowledge entry citing the table and SOURCES rows opened 2026-10-22. Target: rows complete 0 → 8 of 8, entry_ok 0 → 1.
- **R26-C2, calibration.** Six fixed self-assessment items K1–K6 (SCORECARD `## Owned axes` depth, coverage and calibration rows; the SHONEN no-cross-domain-bleed line), taken from round-25 seat report `.ufo/waves/round-25/a3/w1/C1Cherrypick.md` (E1, E2, E3, E5) and routed defect 2. Target: mismatches → 0 of 6. Not a full audit.

Work items:

- C1 runs: 24 REA 6.5.0 CLI calls by four executor seats, all exit 0 and `ok: true`, subject sha256 equal to the carrier `e8156675…7806` (`corpus/evidence/round-26/c1/runs.tsv`, `envelopes/`, `table.tsv`; seat reports `.ufo/waves/round-26/w1/Run*.md`). Result: seven verbs content-keyed across directories, `inspect-binary-layout` path-sensitive.
- C1 mechanism: the 6.5.0 minting rule read from source (`dist/domain/evidence.js:156-182`, S079); offline recompute tool `tools/round-26/recompute-ids.py` reproduces 24 of 24 ids (`corpus/evidence/round-26/c1/recompute-ids.txt`); a prediction written from source matched all eight verdicts (`w1/PredictionCritic.md`); caches ruled out by source reading (`w1/CacheConfound.md`); 6.5.0 versus 6.7.0 id values differ (`w1/PinSourceDiff.md`).
- C1 entry `corpus/knowledge/2026-10-22-r26-native-reader-evidence-id-identity.md`; README coverage-map, knowledge and Known-gaps rows (`corpus/README.md:75`, `:166`, `:206`); SKILL.md decision table "Evidence-ID identity per verb at a named pin — round 26" (end of `SKILL.md`), grounded in the entry; QUALITY row 37 (supersedes 15).
- C1 instrument `tools/round-26/c1-id-identity.py` (sha256 `11c27422…18fa`, selftest 16 cases), committed `bd0c84bc`.
- C2 instrument `tools/round-26/c2-calibration.py` (sha256 `3b0f6507…7e8e`, selftest 18 cases, reads only rows inside `## Owned axes`, so the round-25 first-row false accept is closed), committed `81f63f36` before any repair edit. Repair `46ebfd2f`: depth row 17/17 with `SKILL.md:81-314`, coverage 109/109, calibration measured at `c265db9b`, history kept as clauses; SHONEN clause points at `PROVINCE.md:8-14` and `:24`.
- Routed round-25 defects (`corpus/lessons/round-25-verifier-spotcheck.md`, Routed defects): (1) SKILL.md superseding note for the round-25 custody section, `c3277726` (reviewed clause by clause, `w2/CustodyNoteReview.md`, 19 of 19 hold); (2) is R26-C2; (3) the round-25 instruments are not reused, new instruments ship red fixtures (their own false accepts are disclosed below); (4) correction section on the round-25 EVM entry: 138 responses are 2 per 69 carrier-selector rows, up to three carriers not four, 35 distinct 4byte bodies (`c3277726`, `0375717e`); (5) QUALITY row 35, then row 36 superseding it after the falsify wave found 35 could not fail; (6) this report counts Sources from the lane-round base and lists every lane-round commit; (7) new text uses spaced words (wave-2 scan `w2/PlainEnglishScan.md`; the one run-together token it found in new prose, "arc3", was rewritten).
- Mined mistakes: `corpus/lessons/round-26.md` `## Mistakes` M26-1 to M26-7 (counter frozen without a red case; round-25 falsify wave never ran; Sources counted from an attempt freeze; QUALITY row 35 could not fail; C1 counter accepts forged envelope sets; a craft rule generalized from same-path repeats; two misrooted seat files).
- Falsify wave (32 attack seats) re-ran both counters, mutation-tested both, replayed `read-bytes` and `inspect-binary-layout`, replayed a renamed copy, re-checked the 24 envelopes against the frozen argv and paths, recomputed all ids independently, decided the pin per verb, reopened S079 and S080, and reviewed every new text. Its corrections landed at `003de8cc`, `0375717e`, `16307c47`.

## Landed changes

| commit | what | LOG.md entry |
|---|---|---|
| `c27f445e70cedbaf5300b2fd0a53e821d9b659a9` | claims freeze, start census | `LOG.md` "2026-10-22 — round 26" |
| `81f63f36f95f271a1d4d9b297c662615ed9970ae` | C2 instrument and before receipt (5 of 6) | same |
| `ebe2cb4aff1aea6f45e8bb5583662717ea61c0bb` | C1 envelopes, runs, table, recompute tool, entry, S079–S080, lesson, README rows | same |
| `46ebfd2f0170266646d7cd525be4d46929e953fc` | C2 repair of SCORECARD owned-axes rows and SHONEN | same |
| `bd0c84bcb60724a16d33eb332e625ed9b767bea5` | C1 instrument, C1 before/after and C2 after receipts | same |
| `c327772653badd3b19b3954e1f8713973aa3f93e` | routed fixes: SKILL custody note, round-25 entry correction, QUALITY row 35 | same |
| `fe3eb4edf410244eff46151a148c8f754be1ce80` | SCORECARD round-26 section, LOG entry, claim-freezes row, wave-1 evidence, wave-2 spec | same |
| `003de8cc38a86a914c0348ded674091d47d71fc1` | falsify corrections 1: entry scope, SKILL table, QUALITY 36 and 37, pointers in r12-01, r4-16, r17 | same |
| `0375717e72dac9ba3e964a83cbc889dd94f3f55d` | falsify corrections 2: entry pin section, README wording, round-25 body counts, lesson rows | same |
| `16307c47fe7a966856b1ccd183149a80424ef886` | falsify corrections 3, wave-2 reports, misroot copies | same |
| `ae8bcd860e2ee0e187f66bd2f047cc40b905ede1` | final receipts at `16307c47`, end census, last seat reports | same |

No superseded attempt exists for this round, so every lane-round commit is listed.

## Before → after measurements

| claim | counting command | before (commit) | after (commit) |
|---|---|---|---|
| R26-C1 depth | `python3 -I -B tools/round-26/c1-id-identity.py --root /home/vgpnk/Projects/shokunin/kaidoku-shokunin --rev <REV>` | rows complete 0 of 8, entry_ok 0, exit 1 (`a0639d8e`; receipt `corpus/evidence/round-26/before/c1-at-a0639d8e.json`) | 8 of 8, entry_ok 1, exit 0 (`ebe2cb4a`; `after/c1-at-ebe2cb4a.json`), still 8 of 8 at `16307c47` (`after/c1-at-16307c47.json`) |
| R26-C2 calibration | `python3 -I -B tools/round-26/c2-calibration.py --root /home/vgpnk/Projects/shokunin/kaidoku-shokunin --rev <REV>` | 5 of 6 mismatches (K1, K2, K4, K5, K6), exit 1 (`a0639d8e`; `before/c2-at-a0639d8e.json`; matched by hand in `w1/C2BeforeManual.md`) | 0 of 6, exit 0 (`46ebfd2f`; `after/c2-at-46ebfd2f.json`), still 0 at `16307c47` (`after/c2-at-16307c47.json`) |

Re-run by wave-2 seats `RerunC1Counter.md` and `RerunC2Counter.md` at every named commit with the same results and pinned instrument digests.

What the counters do not carry (claim sizing, disclosed): the C1 counter accepts forged envelope sets (copy replaced by base, one run used three times, `analyze`/`inspect` swapped, probe reuse; `w2/MutC1Forgery.md`), never reads the SOURCES row status or `.meta.command`, and accepts an empty table digest cell. The landed envelopes were checked directly instead: 24 of 24 match the frozen argv, paths and call-record sha256 (`w2/ArgvAndPaths.md`), 24 of 24 ids recompute under an independent implementation (`w2/RecomputeIndependent.md`), and the 6.5.0 id rule fits 24 of 24 while the 6.7.0 rule fits 3 (`w2/PinEvidence.md`). The C2 rules check counts, revisions, a substring and the absence of "contested", not truth; K6 accepts a box flipped to `[x]` and a false pin (`w2/MutC2Shonen.md`); 11 further stale statements in SCORECARD (8 observed, 3 inferred) stay open (`w1/C2Cherrypick.md`). Both instruments were written in wave 1 after the definitions-first freeze, so `corpus/claim-freezes.tsv` records round 26 as FLAGGED INSTRUMENT_ABSENT.

Command A at `16307c47`: mapped 109 of 109, rule blocks 17 of 17; command B 9/9 (unchanged).

## Sources & frontier

SOURCES rows 78 → 80, counted from the lane-round base: `git show <REV>:corpus/SOURCES.md | grep -cE '^\| S[0-9]{3} \|'` at `a0639d8e` = 78 and at `16307c47` = 80. Census `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kaidoku`: start exit 0 (`corpus/evidence/round-26/before/census-start.txt`, five pre-existing W04 warnings S033, S047, S054, S062, S069, then `kaidoku ok`); end exit 0 with the same five warnings (`corpus/evidence/round-26/after/census-end.txt`).

- Rows added by tier: tier A 2 — S079 (code: the 6.5.0 package's evidence-id minting and projection source, read from the installed copy that is file-for-file identical to the registry tarball) and S080 (dataset: npm registry record for `rea-agents@6.5.0`, integrity, publish time, attestation). Both `mined`, opened 2026-10-22, Gate quotes in `corpus/lessons/round-26.md` `## Gate`.
- Rows touched old → new: none of the earlier rows. S079's own `source` and `used-by` cells were widened the same round after the falsify review (logged in the lesson).
- Reopened by the falsify wave: S079 (`w2/ReopenS079.md`: hashes and quotes hold), S080 (`w2/ReopenS080.md`: hashes reproduce, the registry attestation signature verifies; quotes rewritten to the compact JSON form served).
- Frontier advanced: per-verb evidence-id identity at the carrier pin moved from a family-wide statement backed by 6.4.0 controls to a measured 6.5.0 table (README Known gaps bullet and its new sub-bullet). The sourced claim is R26-C1 (entry `source:` cites S079 and S080).
- Sibling overlap: none found (`w1/SiblingOverlap.md`).

## Trend verdicts

- **expansion: improved.** One new admitted-candidate entry on ground the lane did not hold (five of the eight verbs had no two-path identity control at any pin; none at 6.5.0), knowledge 108 → 109, sourced by two rows opened this round.
- **quality: improved.** Held knowledge was corrected, not only added: the craft rule's two-class reading of ids now has a superseding SKILL section and QUALITY row 37 (the `inspect-binary-layout` id held "byte-exact" in r12-01 is path-sensitive); pointers appended to r12-01, r4-16 and r17; the round-25 EVM entry's per-selector wording, carrier maximum and body count corrected.
- **discernment: improved.** The six fixed self-assessment items moved 5 → 0 mismatches on a counter with red fixtures; the round-24 outside source disagreement became a criterion (row 35, then row 36 after the falsify wave showed 35 could not fail), and the 11 statements the counter does not cover are listed rather than claimed.

## SHONEN

- `[~]` SKILL.md contains real decision tables, error patterns, checklists, cited sources — `SKILL.md:81-314` craft section 17/17 at `16307c47` (command A); new per-verb identity table at the end of SKILL.md; no non-author promotion verifier.
- `[~]` At least one end-to-end domain task executed and logged in LOG.md — `corpus/lessons/2026-10-15-round-1.md` (historical); this round's 24 logged CLI calls are `corpus/evidence/round-26/c1/runs.tsv`; no promotion verifier.
- `[~]` Instructions executable by an agent without oral context — the entry's `recheck:` line now names the login-shell variables the calls need (`GHIDRA_INSTALL_DIR`, `REA_PWNTOOLS_PYTHON`); no promotion verifier.
- `[~]` No cross-domain bleed (PROVINCE.md still accurate) — `SHONEN.md:12` points at `PROVINCE.md:95-116`, `:8-14` and `:24`; no promotion verifier.

## Round shape, seats and conformance

- Shape: default, two v1 waves, validated under `/home/vgpnk/Projects/shokunin/scripts/hyaku/ufo-wave-policy.json`, each dispatched as one in-session `task` call after a `wave-slot.sh acquire` grant (wave 1 granted 12:11:26Z after a 7 min wait, wave 2 granted 12:58:01Z after 6 min). No refusals.
- Wave 1 (`kaidoku26-w1`, 33 seats; `.ufo/waves/round-26/w1-spec.json`, `w1/swarm-registry.json`, 33 reports): executor 7, scribe 7, reviewer 7, scout 5, critic 3, mutation-tester 2, connector 1, sentinel 1. Attack roles 12.
- Wave 2 (`kaidoku26-w2`, 32 seats; `w2-spec.json`, `w2/swarm-registry.json`, 32 reports): reviewer 20, mutation-tester 7, critic 5. Attack roles 32.
- Round total 65 seats; attack seats 44 (67.7%). Dead seats: none. 64 seats returned; `MutC2CoverageCalibration` (wave 2) had written its report (`w2/MutC2CoverageCalibration.md`, committed in the final lane commit; K4 and K5 mutants killed per its table) and was cancelled by the L1 at 13:51Z at the scope freeze before it sent its final message. No residual call.
- Planner mapping: the L1 held the planner seat (claims frozen from round-25 seat `PlannerWalk.md`, candidate C-C); the validator rejects `planner` as a swarm role. §3 floor met inside wave 1 (3+ executors, scribe, scout, reviewer, critic, connector).
- Misroot sweep: two round-26 seat files were found at the fleet root (`.ufo/waves/round-26/w2/CustodyNoteReview.md`, `kaidoku-r26/seats/EntryCorrection/final-report.md`); both copied byte-exact into the same relative paths in the lane (`cmp` equal) and the fleet copies deleted (lesson M26-7). The kotoba round-49 file at the fleet root was left untouched.
- Disclosures: one REA probe before the freeze (claims.json `pre_freeze_probe`); the sentinel seat advised redacting the scratch copy path from envelopes, declined because that path is hashed into the `inspect-binary-layout` copy id (redaction would break recompute) and is already public in claims.json; no secrets or user names were found (`w1/EnvelopePrivacy.md`). The fleet census script keys duplicate URLs with trailing Markdown punctuation (`w2/CensusEnd.md`, F1); fleet-owned, reported only.
- Tool installs: none by the L1. Seat `PlainEnglishScan` installed pyspellchecker 0.9.1 with `uv pip` into a scratch `uv venv` (reason: English word list for the run-together scan); no host package changed. No pacman transaction.
- Open L0 questions: none added.
