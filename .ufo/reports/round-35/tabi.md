# tabi — round 35 report (hyaku run 9, attempt 1; L1 TabiR35)

Lane HEAD `1c432f2aaa10d15a7793b967f596871ee5d14280` (`git ls-remote origin refs/heads/master` prints it). Baseline
`2d2c8a77428f9c95c3cd0eb4a3bbf0c6fb4ab684`. Freeze `a4bfef0f75027c915e715649950b1d46dcb33d83`. Measured revision
`8de96c2986979112d4161b1961949db3258c26e8`.

## Work performed

The round declared two claims, frozen with counters and 13 control receipts before any data in `a4bfef0f`
(`.ufo/waves/round-35/claims.json`):
- **C1: adjacency** (lowest non-retired axis, 8; stagnation nudge inactive at window position 3 because the window
  rounds 32–34 holds the round-32 capability). The sibling-overlap map must answer the 383 sibling `SKILL.md` /
  `corpus/knowledge` lines on browser ground that do not name tabi and were not round-34 candidates. Target:
  unaccounted 0 and newMapped ≥ 2. New rows must pass the side-statement floor (QUALITY 97).
- **C2: coverage + capability acquisition, sourced.** WebDriver BiDi runtime evidence on a second engine, Firefox
  158.0.1 through geckodriver 0.37.1. Target: admitted 16 (every matrix §2 row with a BiDi command), failing 0,
  binding null, judged by the unchanged gate predicates over two committed runs and the counter's own live session.

Work items:
- **Tool installs and freeze.**
  - Firefox and geckodriver were installed from Mozilla's official releases (details under Tool installs below).
  - Counters: `.ufo/waves/round-35/counters/c1-adjacency-sweep-v3.mjs` and `c2-firefox-bidi.mjs`.
  - `measure.sh` and the control driver `baseline/controls.mjs`.
  - Controls (`baseline/controls-summary.json`):
    - C1 J1–J7 exit 1.
    - **C1 J8**, a lexical forgery, reaches the predicate. This is disclosed as the counter's residual in
      `claims.json` C1 `feasibilityDisclosed`.
    - C2 J1–J5 exit 1.
  - C2 instrument check before the freeze: 16/16 predicates and identical first screenshots
    (`baseline/c2-instrument-check.json`).
  - w1 RevControls reproduced all 13 receipts byte-identically.
- **C1 build and attack.**
  - 27 chunk scribes dispositioned all 383 lines into the new `corpus/adjacency-screen-browser.tsv` and drafted one map
    row (kagi `SKILL.md:40`).
  - w1 ConnBoundaries scanned the same lines independently and found no row it would defend.
  - w2 withdrew the kagi row. CritRowKagiA argued withdraw and CritRowKagiB argued hold; the integrator sided with
    withdrawal on kagi's bytes and recorded the reversal (lesson round-35 §C1 wave 2, `SKILL.md` §Round 35 note).
  - Eight screen-attack seats found 0 should-map among the 382 screens, and w2 ConnMissedBoundaries found none either.
- **C2 build and attack.**
  - Driver `scripts/bidi-firefox-loopback-round35.mjs` from w1 ExecFirefoxDriver. After w1 SentinelFirefoxEgress
    measured three outbound TLS sockets per launch, the L1 added DNS-off prefs.
  - The two runs were re-recorded (`corpus/evidence/round-35/bidi-firefox/`).
  - Entry `corpus/knowledge/webdriver-bidi-firefox-runtime-round-35.md`, with engine differences D1–D11 from w1
    ExecFirefoxDelta.
  - w1 ExecFirefoxDeterminism: one first-screenshot digest across 27 sessions.
  - Wave 2 held on the reruns (RerunC2, twice), the receipt, the driver code, egress (0 non-loopback sockets) and the
    entry claims. The entry's precision fixes came from w2 CritEntryDifferences and CritEntryClaims.
- **Frontier step.**
  - SOURCES S134–S141 were added; cell fixes from w2 Reopen*.
  - Lesson `corpus/lessons/round-35.md` covers Gate, C1/C2 decisions for both waves, Mistakes M1–M5, errata intake 1–8,
    the census delta and the adjacency planning input.
  - QUALITY criteria 98–101.
- **Round-34 routed defects.** Each has a disposition in lesson round-35 §Errata intake:
  - README `:794`/`:799` correction landed.
  - Lesson round-34 precision corrections landed (S131 span, the kake:411 note cell, the RFC 4122 refusal basis).
  - U01–U28 dispositions: `.ufo/waves/round-35/w1/ScribeUDispositions{A,B}/dispositions.md`. w2 RevUDispositions
    agreed 8/8.
  - S125 cadence routed again, with its reason: the cell alone turns `check-release-pins` red.
- **No-harm repair.** The w1 census append to `corpus/knowledge/browser-surface-census.md` turned
  `check-freshness --worktree` red. It was found by w2 RevCorrections D1 and withdrawn at the w2 integration (lesson
  M5, QUALITY 101).
- **Waves** (shape: two v1 waves):
  - w1 build + first falsifiers: 51 seats — 35 scribe, 4 executor, 3 connector, 2 critic, 2 mutation-tester, 2 scout,
    2 reviewer, 1 sentinel.
  - w2 falsify: 34 seats — 16 critic, 7 reviewer, 6 scout, 2 connector, 2 mutation-tester, 1 sentinel.
  - Round total 85. No residual call. Dead seats 0 (`w1-results.json` 51/51 and `w2-results.json` 34/34 non-empty).
  - The L1 held the canonical planner seat; the planning data-walk rode w1 ConnRound.

## Landed changes

| Commit | Content | LOG.md entry |
|---|---|---|
| `a4bfef0f` | freeze: claims.json, both counters, controls + 13 receipts, measure.sh, pins, candidate list, C2 instrument check, census-start | LOG "Round 35 — freeze" |
| `083c5c64` | w1 integration: screen ledger (382) + kagi map row + tabi declaration, Firefox driver/receipt/runs, entry, S134–S141, lesson round-35, QUALITY 98–100, README + lesson-34 corrections, census append (later withdrawn), w1 wave evidence | LOG "Round 35 wave-1 integration" |
| `8de96c29` | w2 integration: kagi row withdrawn → screen, census append withdrawn, entry/SOURCES precision fixes, lesson M5 + w2 sections, QUALITY 101, README correction, w2 wave evidence | LOG "Round 35 wave-2 integration" |
| `1c432f2a` | measurement at `8de96c2`, SCORECARD disposition, capability row `webdriver-bidi-runtime-firefox`, planned row | LOG "Round 35 disposition" |

## Before → after measurements

Measured at `8de96c2` in a clean clone, with counter bytes from the freeze. `measure/provenance-8de96c2.txt` records:
porcelain 0; digests equal frozenDigests; the gate pins unchanged; Firefox `firefox-bin` sha256 `46e2c204…` and
geckodriver `f831b7e6…`.

- **C1.** Command: `node .ufo/waves/round-35/counters/c1-adjacency-sweep-v3.mjs --rev <REV> --repo <clone> --fleet /home/vgpnk/Projects/shokunin --json`.
  - Before (`baseline/c1-J1-do-nothing.json`): candidates 383, mapped 0, screened 0, unaccounted 383, newMapped 0.
  - After (`measure/c1-at-8de96c2.json`): mapped 0, screened 383, unaccounted 0, newMapped 0, adjacency clean 16/16,
    screenFindings 0, predicate false.
  - **Not met: honest stop.** Wave 1 drafted one row; wave 2 withdrew it. No second defensible boundary exists in the
    pool (w1 ConnBoundaries, w2 ConnMissedBoundaries).
- **C2.** Command: `node .ufo/waves/round-35/counters/c2-firefox-bidi.mjs --rev <REV> --repo <clone> --json`.
  - Before (`baseline/c2-J1-do-nothing.json`): population 0, admitted 0, `e1-entry-absent`.
  - After (`measure/c2-at-8de96c2.json`): population 17, admitted 16, failing 0, unmeasured 1 (R16), binding null;
    the live session is Firefox 158.0.1 with first shot `7a3ae6a9…`; sourceWitness S134; predicate true.
  - **Met** under the declared sentence `admitted >= 16`. The counter's frozen threshold is 14 (lesson M1); admitted 16
    meets both.
  - Recorded limits:
    - A byte-cloned run2 with rewritten ids passes (w2 MutDriverReceipt).
    - Caller-named fake binaries pass (w1 CritC2Counter; this reading's binary digests are pinned in provenance).
    - The counter's live leg is not loopback-only (M3).
- **No-harm.**
  - `measure/noharm-at-8de96c2.txt`: 28 of 28 exit 0.
  - `measure/freshness-worktree-at-8de96c2.txt`: `check-freshness --worktree` clean 34/34.
  - Round-33 and round-34 C1 counters: unaccounted 0 with screenFindings [].
  - Round-34 C2 counter: killed 20.
  - `check-selfassessment` mismatches 0, both at `8de96c2` and at the candidate `1c432f2a` on a clean tree. Before the
    disposition commit it read m3 `unlanded-paths`, which the commit cleared (QUALITY 92).
  - `measure/numstat-at-8de96c2.txt`: 0 deleted lines in the append-only files.

## Sources & frontier

- **Rows 133 → 141.** Counting command: `grep -cE '^\| *S[0-9]{3,} *\|' corpus/SOURCES.md`. Census
  `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin tabi`:
  - Start: `tabi ok`, exit 0 (`.ufo/waves/round-35/baseline/census-start.txt`).
  - End: `tabi ok`, exit 0, 20 W04, all pre-existing (`.ufo/waves/round-35/measure/census-end.txt`).
- **Added: tier A 7, tier B 1.**

  | Row | Source | Tier |
  |---|---|---|
  | S134 | geckodriver Flags.html (`--websocket-port` "Defaults to 9222") | A |
  | S135 | Capabilities.html | A |
  | S136 | v0.37.1 `capabilities.rs` (`webSocketUrl` read) | A |
  | S137 | v0.37.1 `marionette.rs` (`moz:geckodriverVersion` insert) | A |
  | S138 | Firefox remote Prefs.html (BiDi is the only protocol) | A |
  | S139 | MDN `browsingContext.locateNodes` | B |
  | S140 | ftp release dir, with a SHA256SUMS signature Good | A |
  | S141 | geckodriver v0.37.1 release assets and digests | A |

- **Rejected:** the Firefox release notes, recorded with reason and flip condition in lesson §Gate.
- **Rows touched old→new:**
  - S135, S136, S139 and S141 had cells corrected at w2 (rows added this round).
  - S125 recheck stays `90d` → `90d`; the reason is in lesson §Gate.
- **Re-opens:** w2 Reopen* re-fetched all eight rows byte-identically.
- **Sourced claim:** C2. Its entry's `source:` line cites S134–S141, and the counter's s1 witness is S134 →
  `corpus/lessons/round-35.md:15`.
- **Frontier advanced:**
  - BiDi runtime evidence now spans two engines.
  - Sibling browser ground that does not name tabi is now bounded: 383/383 accounted.
- **Mistakes mined:**
  - M1 freeze-consistency: counter threshold 14 vs declared 16. Red state `measure/c2-M1-boundary-15.json`, reproduced
    by w2 CritC2Boundary.
  - M2 instrument: a short-line screen rule.
  - M3 overclaim: the "loopback" label.
  - M4 instrument trust: caller-named binaries.
  - M5 no-harm blind spot: the check-freshness pin.
- **Assimilation:** none. w1 ScoutAssimilation found no `merge/tabi/` theme on these surfaces. The id-collision check
  still ran (`.ufo/waves/round-35/assimilation/`): registry 133, staged 148, collisions 32. Nothing was appended, so
  nothing was renumbered.
- **considerthese:** this lane has no `considerthese/` dir.

## Trend verdicts

- **expansion: improved.**
  - A new capability: Firefox through geckodriver drives the BiDi runtime evidence on a second engine, which was absent
    from the host before.
  - One knowledge entry on ground the coverage map did not hold, citing 8 rows opened this round.
  - A 383-row screen ledger bounds sibling browser ground.
  - No new adjacency boundary.
- **quality: improved.**
  - Four QUALITY criteria (98–101), each with a red state.
  - Round-34 errata landed append-only.
  - Wave 2's entry and SOURCES precision defects were fixed before measurement.
  - A no-harm regression was caught and repaired within the round.
- **discernment: improved, pending the outside check.**
  - Wave 2 overturned the only integrator-admitted map row, and the round reports the miss rather than keeping it.
  - Admits on record: S134–S141 and the C2 rows.
  - Rejects on record: the kagi row, the release-notes source, and three unregistered pages.

Axis verdicts:
- adjacency: unchanged at 8; C1 not met.
- coverage: improved; C2 met, score held at 9.
- depth, operability, freshness, calibration: unchanged; no harm measured.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — `corpus/knowledge/webdriver-bidi-firefox-runtime-round-35.md` §4 engine-choice table and §2 launch discipline; `SKILL.md` §Round 35. Non-author verifier not on record.
- [~] At least one end-to-end domain task executed and logged in LOG.md — the Firefox BiDi driver's two cold runs plus the frozen counter's live session, `measure/c2-at-8de96c2.json`, LOG "Round 35 disposition".
- [~] Instructions executable by an agent without oral context — w2 RerunC1, RerunC2 and SentinelDriverEgress reproduced the readings from lane text. They are lane-dispatched seats, not non-authors.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — `PROVINCE.md` unchanged. 383 sibling browser lines were screened rather than absorbed, and the one overreaching row was withdrawn.

Stale-lane: respawn-per-round driver; no other mission of this lane is open.

Tool installs:
- Firefox 158.0.1: official release binary from `ftp.mozilla.org` into `~/.local/opt/firefox-158.0.1`, symlinked at
  `~/.local/bin/firefox`. The tarball's sha256 `dce45470…` equals the signed SHA256SUMS; the signature is Good under
  Mozilla key `14F26682…D98F0353`. Reason: C2's second engine.
- geckodriver 0.37.1: GitHub `mozilla/geckodriver` release into `~/.local/bin`, sha256 `e815130e…`. Its `.asc` is
  signed by a subkey that Mozilla marks revoked; this is recorded in lesson §Gate. Reason: the same.
- No pacman.

Misroot sweep: `git -C /home/vgpnk/Projects/shokunin status --porcelain` is empty, so there is no fleet-root misroot.
w2 ScoutMisrootSweep found no stray wave dirs. Scratch `/fast/scratch/hyaku/tabi-r35` was removed after landing; it
held the L1's own scratch and a leftover from w2 RevDriverCode, which is that seat's defect.

Open L0 questions: none filed this round.
