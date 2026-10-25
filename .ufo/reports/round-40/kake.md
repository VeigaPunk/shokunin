# kake — round 40 report (attempt 1, L1 `KakeR40`, hyaku in-session)

Lane `/home/vgpnk/Projects/shokunin/kake-shokunin`, base `f171c58b`, lane tip `0c732d5a` (pushed; `jj-lane.sh state` local = remote).

## Work performed

Declared claims: **one** — **C1, operability: repair of the held tool `scripts/sitemap_audit.py` on three routed input classes** (E UTF-16 without BOM → `xml_malformed`; U a `loc`/`sitemapUrl` that `urlsplit` would alter → `loc_not_absolute`/`check_invalid`; R a repeat of an earlier invalid check's string id → `check_invalid`). It was declared measured, with a frozen kill rule. The control wave set off kill rule (1) before the build landed, so **C1 is exploratory**. No second claim was declared.

- Declaration, frozen counter, witnesses, kill rule and L1 controls: `f043c721` (`SCORECARD.md` "Round 40 — C1 declared"; counter `.ufo/waves/round-40/c1_count.py` sha256 `6d73b8f4…bee8d8`; predicate `met: passed >= 30 of 30 witnesses and the round-39 selftest passes 150 of 150`). Before: base 10/30 (E 4/9, U 3/13, R 3/8), selftest 150/150, not met (`verification/pre/base-f171c58b.json`). L1 controls: constant-clean 5, junk 0, all-false 8, no-reader 8, absent 0.
- Repair-first items from `corpus/lessons/round-39-verifier-spotcheck.md`:
  - Routed defect 1: superseding rows S112 (S106), S113 (S107), S114 (S109) (`corpus/SOURCES.md:120-122`).
  - Routed defect 2: D2, D4 and D5 repaired, each with fixtures that fail on the round-39 bytes and pass on the build (selftest 150 → 179 → 183). D1 was **rejected by source**: S110 §2.8 says a 1.x document is processed as 1.0. D3 was kept as the sentence-9 reading (lesson Gate).
  - Routed defect 3: the round-39 capability row is marked admitted `unprovable-but-better` (`SCORECARD.md` "Round 39 — closure correction").
  - Routed defect 4: violated by this round (lesson Mistake 1) and then turned into the amended QUALITY (o) with a check.
  - Routed defect 5: carried items re-verified open (`w1/ScoutCarriedItems.md`).
- Wave 1 (39 seats), the adversarial control wave (it built every frozen control class): 27 of 76 control receipts meet the predicate (`jq -s 'map(select(.met))|length' .ufo/waves/round-40/verification/w1/*.json` → 27). The meeting receipts cover these classes:
  - key-finder: witness id read from `/proc/1/cmdline` and `/proc/self/mountinfo` (`case-<id>` directory) (`w1/CtlKeyFinder.md`);
  - label replay (`w1/CtlLabelKeyed.md`);
  - position/id-length keying (`w1/CtlPositionKeyed.md`);
  - raw-byte proxy (`w1/CtlURawBytes.md`);
  - case-fold/NFKC lookups (`w1/CtlRCaseFold.md`);
  - partial repairs on unsampled sub-shapes (`MutFamilyE` M07–M11, `MutFamilyU` M09–M12, `MutFamilyR` m02–m06, the L1-built `CriticDeclaration` counterexample: LF in `sitemapUrl`).

  The kill record landed at `12211cc5`, before the build.
- Build `56d57ee4` (L1 reference bytes `03a8fba4…7b22b`, declared before data): 23 new fixtures red on the round-39 bytes (`PASS 156/179`, exit 1) and green on the build (`PASS 179/179`) (`verification/build/`). Counter 30/30 as information only.
- Residual call (8 seats) found three regressions in `56d57ee4` (`resid/CriticBetterClaim.md` F1–F3):
  - a NUL vs a non-UTF-8 declaration;
  - a NUL vs a DOCTYPE;
  - a TAB inside an ignored foreign element in `loc`.

  Revision `d8d5578e` (tool sha256 `4de35f8c…1460e`) fixes all three. Its four fixtures are red on `56d57ee4` (`PASS 179/183`, exit 1) and green on `d8d5578e` (`PASS 183/183`, exit 0) (`verification/build2/`). Real run on the six round-39 public sitemaps stays byte-equal (`jq -S . | sha256sum` → `fd985a41…`, `verification/harm/realrun-build2.json`). The counter scores `d8d5578e` 30/30 (information, `verification/c1-at-d8d5578e.json`).
- Frontier step: sources S110–S116; census exit 0 → exit 0. Mistakes 1–2, each with a fix shown able to fail. QUALITY (o) amended, plus new (q) and (r).
- Sibling overlap (`w1/ConnectorSiblingOverlap.md`): no sibling duplicates or contradicts S110 or S111. Siblings that call `urlsplit` without a whitespace or C0 guard inherit the S111 hazard: `kagi` `corpus/release-clock.py`, `kotoba` `verifiers/check_*.py`, `chousa` `tools/quote-reopen.py`. `kotodama`'s `r8_checks.py` guards against it. This is reported only; sibling repos are read-only.
- Independent-oracle probe (the frontier step the orchestrator named): `w1/ExecIndependentOracle.md`. libxml2/xmllint agrees with the contract on E only in part: it re-sniffs UTF-16 when a declaration is present. It has no leverage on U or R. An oracle-backed measured claim needs an RFC 3986 absolute-URI checker.

## Landed changes

| Commit | What | LOG.md |
|---|---|---|
| `f043c721` | C1 declaration, counter, L1 controls/receipts, S110–S114, round-39 closure correction, lesson Gate | "Round 40" bullet 1 |
| `12211cc5` | wave-1 control tools (`controls/w1/`), 76 receipts (`verification/w1/`), kill rule (1) record | bullet 2 |
| `56d57ee4` | build: `scripts/sitemap_audit.py` repairs E/U/R, selftest 150 → 179, SKILL amendment | bullet 3 |
| `6d5cd54a` | lesson (Gate updates, Mistakes, round-39 corrections), QUALITY (o) amended/(q)/(r), S115, LOG, criteria checks, harm receipts, wave-1 reports | bullet 4 |
| `d8d5578e` | build revised after the residual attack (F1–F3), selftest 183, S116, residual reports | lesson "Residual call", SCORECARD "build revised" |
| `83b48204` | connector report, dispatch/settle logs, census-after, LOG correction (8 refusals, not 7) | LOG "Round 40" correction line |
| `0c732d5a` | retained source bytes `xmlschema11-2.html` (S113; skipped by the directory commit as >1 MiB) | — |

## Before → after measurements

- **C1 counter** (frozen; exploratory by kill rule, so this is information, not admission): `python3 -B .ufo/waves/round-40/c1_count.py --root . --revision <rev> --seed 40001 --out <receipt>`. Base `f171c58b` scores 10/30, not met. Build `56d57ee4` scores 30/30, met; revision `d8d5578e` scores 30/30, met. 27 of 76 controls also meet, so the number does not decide C1.
- **Selftest red-then-green:** `python3 -B scripts/sitemap_audit_selftest.py --tool <tool>`. At tip the selftest has 183 fixtures. The round-39 bytes score `PASS 159/183` (exit 1), `56d57ee4` scores `PASS 179/183` (exit 1), and `d8d5578e` scores `PASS 183/183` (exit 0) (`verification/build2/selftest-*.txt`). Fault injection still rejects the silent and constant-clean tools.
- **Harm:**
  - `git diff --diff-filter=DR f171c58b <tip>` is empty. The only deleted lines are inside `scripts/sitemap_audit.py`.
  - Other `scripts/*.py` are byte-equal; the robots selftest passes 204/204 (`resid/ReviewHarm.md`).
  - Real run is byte-equal (`fd985a41…`).
  - The D1 check `python3 -B .ufo/waves/round-40/criteria/d1_check.py --tool <tool>` exits 0 on the base and on both builds, and exits 1 on the D1-"fixed" mutant.
- **Mistake checks:** `python3 -B .ufo/waves/round-40/criteria/preseal_order_check.py --root . --revision <rev> --counter .ufo/waves/round-40/c1_count.py --receipts .ufo/waves/round-40/verification` exits 1 at `f043c721` (0 non-author receipts), exits 1 at round 39's `ceecb1b1`, and exits 0 at `12211cc5` (`verification/criteria/preseal-*.txt`).

## Sources & frontier

- Census: `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kake`.
  - Round start (08:29:00Z): exit 0, 6 W04.
  - Round end (09:03:24Z): exit 0, 10 W04 (new: duplicate URLs S110, S111, S115, S116), `kake ok`.
  - Files: `.ufo/waves/round-40/census-{before,after}.txt`.
- Rows `grep -c '^| S[0-9]' corpus/SOURCES.md`: 109 → 116. Added by tier: A +7 (S110 XML 1.0 Char/VersionNum/BOM; S111 urllib.parse; S112, S113 and S114 supersede S106, S107 and S109; S115 supersedes S111; S116 supersedes S115).
- Rows touched old→new: none. No `status`/`recheck`/`used-by` change; corrections are superseding rows, append-only.
- Every new row was opened this round by the L1 (retained under `.ufo/waves/round-40/sources/`, `SHA256SUMS`) and has a Gate line with URL, access time and a quote of 25 words or fewer (`corpus/lessons/round-40.md` Gate tables).
- Sourced claim: C1 rests on S110 (E: U+0000 is not a Char) and S111/S115/S116 (U: what `urlsplit` strips).
- Frontier rows advanced: sitemap scope (PROVINCE Frontier) moves from "audit exists" to "audit repaired on three routed classes". The next step is an RFC 3986 absolute-URI oracle (`w1/ExecIndependentOracle.md`).

## Gate

- **Reject:** routed defect 2's "fix D1". Reason: S110 §2.8, "When an XML 1.0 processor encounters a document that specifies a 1.x version number other than '1.0', it will process it as a 1.0 document." `CriticD1Reject` holds the reject. A D1-"fixed" mutant meets the round's counter (`w1/ExecD1Check.md`), so the reject is enforced by `criteria/d1_check.py` and fixture `r40_d1_version_1_1_clean`.
- **Reject:** the frozen 30-witness counter as C1's admission instrument. Reason: 27 of 76 controls meet it (kill rule (1), `12211cc5`).
- **Reject:** `ReopenS114`'s "same-domain URLs only is overstated". Reason: the page says "Specify only page links of the domain where the file will be located." S114 stands.
- **Accepted correction:** `ReopenS111`'s "must reject is overstated" (→ S115) and `CriticSourcesDecisions`' S115 scope wording (→ S116).
- **Admit:** S110–S116, each with its Gate quote.

## Mistakes (lesson `corpus/lessons/round-40.md` § Mistakes)

1. **A counter was frozen on author-only controls, against round-39 routed defect 4.** Captured-by: QUALITY (o), which existed and was not applied. Fix: (o) amended plus `preseal_order_check.py`. It is shown able to fail: red at `f043c721` and `ceecb1b1`, green at `12211cc5`.
2. **A routed defect was nearly taken as a requirement without re-deriving it from its source (D1).** Captured-by: none. Fix: QUALITY (q) plus `d1_check.py`. It is shown able to fail: exit 1 on the mutant, exit 0 on the base and the build.

Also new: (r), a counter's sandbox may expose no witness identity. It is red on the round-40 counter: the `CtlKeyFinder` and `CtlLabelKeyed` tools score 30/30.

## Corrections to the round-39 report (appended here; that report is not edited)

1. "Surface unmoved": `git ls-tree -r --name-only 565ef4c9 scripts/ | grep -c sitemap_audit` gives **2** (tool and selftest), not 1. `grep -cx scripts/sitemap_audit.py` gives 1.
2. "Seven critic seats returned source or diffs": it was **six** (three source, three diffs). `CtlValuesOnly` and `CtlHandTokenizer` wrote their own files; `CtlStructureOnly` was refused.
3. "5 false accepts in 15 adversarial samples" should read **5 of 7 adversarial samples** (`w2a3/MutCriterionO.md`).

All three were re-derived from committed bytes (`w1/ScribeR39ReportCorrections.md`, `resid/KakeR40.ReviewRoutedDefects.md`).

## Trend verdicts

- **expansion: unchanged.** No new `corpus/knowledge/` entry. The new rows correct or ground existing sitemap ground; the oracle probe is a finding, not an admitted entry.
- **quality: unprovable-but-better.**
  - For: the held sitemap audit is repaired on three routed classes, red-then-green, with no harm on exercised surfaces.
  - For: three regressions were caught and fixed within the round.
  - For: S106, S107, S109 and S111 now have corrected superseding rows.
  - Against: no counter can certify the repair (27 of 76 controls met).
  - Against: `ReviewBuildRepairs` notes that interior C0 controls other than TAB/CR/LF still pass in `sitemapUrl` (outside the declared class; open).
- **discernment: improved.**
  - The round rejected a routed defect by source (D1).
  - It rejected a scout's over-reading (S114) and accepted two source corrections (S115, S116).
  - It applied its own frozen kill rule against itself before data.
  - QUALITY gains (o)-amended, (q) and (r), each grounded in a lesson mistake; the (o) and (q) checks are shown red, and (r) is red on this round's counter.

## C1 verdict

- **Self-verdict:** exploratory, `unprovable-but-better`.
- **Advisory lane seat:** `KakeR40.ExploratoryVerdictC1` (reviewer, not the build author) judged `unprovable-but-better` (`resid/KakeR40.ExploratoryVerdictC1.md`). A lane-dispatched seat is not the verdict of record (LEARNING.md).
- **Verdict of record:** owed to the non-author closure.
- **Why "better":**
  - the round-39 tool read BOM-less UTF-16 as clean;
  - it judged URLs after `urlsplit` silently removed characters;
  - it missed repeats of invalid checks' ids;
  - the build fixes all three, as the selftest red-then-green shows, with no observed harm.
- **Why "unprovable":** the frozen counter cannot separate the repair from 27 controls.
- **Axis scores:** unchanged (operability 10, freshness 10).

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — `SKILL.md` "Sitemap file audit — round-40 repairs" (S110, S111 cited; revision paragraph).
- [~] At least one end-to-end domain task executed and logged in LOG.md — `LOG.md` "Round 40" bullet 3 (real run on six public sitemaps, byte-equal; `verification/harm/realrun-build2.json`).
- [~] Instructions executable by an agent without oral context — `scripts/sitemap_audit_selftest.py` (183 fixtures) plus the SKILL procedure.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — `PROVINCE.md` unchanged (`git diff f171c58b <tip> -- PROVINCE.md` is empty); the work stays inside sitemap publishing checks.

## Round shape, seats, holds

- **Shape:** default two-wave shape, with wave 2 replaced by the residual call because there were fewer than 32 genuine attack items after the build.
  - Wave 1: 39 seats, validated under policy v1. Roles: 14 mutation-tester, 10 executor, 6 scout, 4 reviewer, 2 critic, 2 scribe, 1 connector.
  - Residual call: 8 seats (6 reviewer, 2 critic).
  - **Round total 47.**
- **Planner seat:** held by the L1; the planning data-walk rode `CriticDeclaration` and `ReviewWitnessContract`.
- **Gate log:** wave 1 granted at 08:37:35Z (live 60, cap 100); residual granted at 08:54:45Z (live 78).
- **Holds (provider refusals; each item ended, not retried, rerouted or rephrased):** **8**, all mutation-testers, "[openai-codex/gpt-6.1-sol] Codex error event: This content was flagged for possible cybersecurity risk … (code=cyber_policy)": `CtlENulSniff`, `CtlUSitemapUrlOnly`, `CtlUAnyWhitespace`, `CtlROneKind` (12–17 s), `CtlRAnyRepeat` (1m42s), `CtlEDeclOnly` (1m45s), `CtlULocOnly` (4m59s), `CtlEWrongCode` (6m34s); their sandbox leftovers were not scored (`w1-dispatch-log.txt`).
- **Dead seat:** 1, `CtlUTabOnly` ("SYSTEM WARNING: Subagent ended without a final message."). Its sandbox tools were scored as controls; one, `tool_tab_only_query`, meets.
- **Cancelled:** none (all 47 seats settled before the 09:22Z / 09:40Z deadlines; `ConnectorSiblingOverlap` returned last at 31m38s).
- **Misroot sweep:** `git -C /home/vgpnk/Projects/shokunin status --porcelain` at report time found no file written by this round's seats (the untracked fleet files predate the round or belong to other lanes).
- **Inherited state:** no earlier attempt of round 40 (`watchdog.log` has only the launch line); the lane was clean at `f171c58b`. Not edited (not authored here): `corpus/lessons/round-39-verifier-spotcheck.md`.

Stale-lane: respawn-per-round driver; no other mission of this lane is open.
Tool installs: none (no seat reported an install).
L0 questions: none.
