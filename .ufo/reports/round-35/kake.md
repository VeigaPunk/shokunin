# kake — round 35 report

L1 `KakeR35` (hyaku in-session, attempt 1). Lane `/home/vgpnk/Projects/shokunin/kake-shokunin`.
Base `16a6b8b8144f4d6e6187e9ecbb4fb5f4528b911a`. Lane tip (pushed) `133a3a1f35d75416bdbb1544bf1051a9f9aff346`.
No earlier attempt: `.ufo/watchdog.log` has no `lane-dead-no-report kake round=35` line. No inherited leftovers: lane status was clean at start. Files not authored by the lane were not edited (`corpus/lessons/round-34-verifier-spotcheck.md`, the `round-*-aggregator-*` files).

## Work performed

Declared claims are in `SCORECARD.md` "Round 35 — declared claims" (commit `81d9fd74`), before any build. This is a repair-first round after the round-34 honest stop.
- The L1 wrote the C1 cases and the C2 probes before the declaration. They stayed outside the lane until the reveal commit `4c6be2bd` and are pinned by sha256 in `.ufo/waves/round-35/sealed_count.py`.
- The counter refuses (exit 2) any revision that already holds a key.

Claims:
- **C1 — operability (capability repair).** `scripts/link_preview_audit.py` meets the public round-35 contract: (a) `og_url_multiple`; (b) metadata inside `<template>`/`<svg>`/`<math>` is ignored; (c) an unreadable page no longer stops the other pages. Counter: 24 sealed cases. Target: passed ≥ 22.
- **C2 — freshness (sourced learning claim, new ground).** `corpus/knowledge/security-txt-publishing.md`: how a publisher serves a valid RFC 9116 security.txt from GitHub Pages. It rests on rows S078–S086 opened this round. Counter: 12 sealed probes plus size, copied, cites and entry conditions. Target: met true.

Work items:
- Sources: opened with `.ufo/waves/round-35/fetch_sources.py`. S078–S085 and the S006 re-open at 22:00:48–22:02:20Z, before the declaration. S086 and S087 at 22:27:54–55Z, after wave 1. Retained under `.ufo/waves/round-35/sources/`.
- Do-nothing controls were scored with the frozen counter and committed before any build (`318561ef`; table in SCORECARD "controls scored before any build"):
  - C1: base 14/24, `dcef39b5` lookup 7, constant clean 7.
  - C2: junk 0 probes, keyword 3, transcription 8 (copied fails).
- Counter version 2 (`bd14096a`), landed before any build was measured. Wave-1 `CriticC2Conditions` showed hidden bytes (an HTML-comment padding and zero-width splits) passing version 1. Version 2 cleans comments and format characters, counts size in overlap words (cap 2200), reads only the first Registry section, and checks the receipt URL.
  - Every control was rescored (`verification/control-v2-*.json`).
  - New reworded-transcription control: 6 probes.
  - Probes, pins and targets are unchanged.
- C1 build `b1cbbc39`: wave-1 `ExecToolRepair`, patch applied byte for byte. It adds 10 fixtures; selftest 45/45, round-34 matrix 28/28 (`verification/selftest-link-preview-at-b1cbbc39.txt`, `c1r34-matrix-at-b1cbbc39.json`).
- C2 build `95abec21`: entry drafted by wave-1 `ScribeEntryDraft`, landed unedited; rows S078–S087; S006 used-by.
- Round-34 spot-check routing (`corpus/lessons/round-35.md` "Round-34 routed defects — disposition"):
  1. Sealed targets and controls before the build.
  2. The `dcef39b5` description is corrected by append. It hashes the arguments plus every path and file content, not the case directory name. `criteria/control_description_check.py` is shown able to fail.
  3. `SKILL.md` "Link-preview audit gate registry — round 35" (`fd0d53b2`), with `criteria/registry_row_check.py` (exit 1 at `318561ef`, exit 0 at `fd0d53b2`).
  4. No census target in any pre-build receipt: the keys were sealed. `criteria/prebuild_leak_check.py` gives exit 1 on the round-34 receipt.
  5. S074 correction note appended to `SOURCES.md`: the page head has 3 `og:` metas; the reject stands.
- QUALITY "Round-35 criteria" (a)–(e). (e) was added after wave 2 with `criteria/knowledge_control_check.py`. PROVINCE and README round-35 sections. LOG round 35. Capability row "Link-preview audit, round-35 contract".
- Wave-2 corrections:
  - Appended: entry, lesson (with mistake row 5), QUALITY, SCORECARD, LOG.
  - S001 and S002 used-by cells now include the entry.
  - Edited in place because they entered this round: the SKILL exit-64 label and the S074 note wording.
  - New fixture `og_url_multiple_first_value_checked` kills mutant M09 (selftest 46/46).
  - Linear-time end-tag fix after `SentinelToolInputs` found a quadratic stack (499 s on a hostile page, now 0.33 s). Re-measured in a sandbox at `e068bc4b`: 24/24, 46/46, 28/28. It counts toward no claim.
- Holds:
  - `KakeR31.CriticC1Counter` and `KakeR31.CriticSandboxThreatModel` were not recreated.
  - New hold: wave-1 `KakeR35.CriticSealedDesign` ended in an automatic model switch after a safety filter. Its findings are not evidence, its bundles were not scored, and it was not retried.

## Landed changes

All landed through `jj-lane.sh` (`landed` lines), tied to LOG.md "Round 35".

| commit | content |
|---|---|
| `81d9fd74f1460ba8cff007fc42f8fb8265aa2d4d` | declaration; sealed counter v1 with key pins; fetcher; sources S078–S085, S006 re-open; census before |
| `318561efa67206699fdaf259ffb86e39f2d916a8` | control receipts and bundles, scored before build |
| `bd14096aa36e0a0e0e97552a38738be5904fbb10` | C2 counter version 2, before any build measured; controls rescored; reworded control |
| `b1cbbc39a12962cb6cae054b07e4ffc87d29f5ea` | C1 tool repair and 10 fixtures |
| `95abec210c35eb17abffc16f8d39dbc6c6825fc5` | C2 entry, SOURCES S078–S087, S006 used-by, S074 note, search log; S086–S087 |
| `4c6be2bdec5630166c4013e53c226b1119ec63cc` | reveal of both keys and the L1's private reachability patch (not landed as tool) |
| `61288738a763d800e80d650130dcd1da9a8002ed` | before and after receipts |
| `fd0d53b206dc35bff7b2d481863cba46c025ceab` | SKILL registry row and exit-2 correction; three criteria checks |
| `bc0304decdcc434d4e104eb6e404dcb402b1cca5` | lesson, QUALITY, PROVINCE, README, SCORECARD results, capability row, LOG; wave-1 reports and evidence |
| `7deacc4629c1d05a34fb919d8095e99efc7b712f` | criteria receipts; wave-1 ReviewCounterCode report |
| `0d52173cb6766a63e024a8bc85bdce98f90ce7e4` | wave-1 SentinelKeyExposure report; wave-2 spec |
| `662578e8e19b84ba77c8fbfe9da27a7851efb561` | wave-2 reports and all wave-2 corrections; end-tag fix and fixture; knowledge-control check |
| `133a3a1f35d75416bdbb1544bf1051a9f9aff346` | census after |

## Before → after measurements

Key revision `4c6be2bd`. Receipts: `.ufo/waves/round-35/verification/<claim>-at-<rev>.json` plus `.exit`.

| claim | command | before | after | target |
|---|---|---|---|---|
| C1 | `python3 -B .ufo/waves/round-35/sealed_count.py c1 --root . --revision <rev> --key-revision 4c6be2bd` | `16a6b8b8`: 14/24; `bd14096a`: 14/24 | `b1cbbc39`: 24/24; `95abec21`: 24/24 | ≥ 22: met |
| C2 | `python3 -B .ufo/waves/round-35/sealed_count.py c2 --root . --revision <rev> --key-revision 4c6be2bd` | `16a6b8b8`, `bd14096a`, `b1cbbc39`: met false, 0/12 | `95abec21`: met true; 12/12 probes, 1388 words, copiedShare 0.0, 8 good cites | met true: met |

- Counter v1 at `95abec21` also gives met true (`c2-v1-at-95abec21.json`). Measuring the reveal commit is refused with exit 2.
- Wave-2 `RerunC1Sealed`, `RerunC2Sealed` and `ReviewScorecardLog35` reproduced every receipt field for field.
- Separability (`w2/ExecSeparabilityAtTip.md`):
  - tip with the base tool gives C1 14/24 and C2 met;
  - tip without the entry and rows gives C1 24/24 and C2 not met.
- Each target is out of reach of every do-nothing control.
- Wave 2 showed what the targets do not show:
  - **C1:** 22 is reachable with bullet (c) skipped, since (c) moves only 2 cases. The sealed set holds no nested container. 11 of 14 single-rule mutants still reach 22 (`ExecPartialRepairs`, `CriticC1Sufficiency`, `MutToolRepair`).
  - **C2:** an all-false entry written with the revealed probes meets it (`dc8e1adf`, 12/12). So does an entry written from the public topic list with three landed row ids, by a seat that had read S079, S081 and the row summaries but no primary text (`0b7779dc`, 11/12). So the C2 counter does not show that the entry came from this round's sources or that it is true.
  - Both C2 controls are retained (`retained/r35-w2-*.bundle`). The disclosed limit "probes test that stated facts are present" overstated the counter.
  - Entry truth was read by wave 2: RFC facts 27/27, live examples 11/11, Pages facts 6/8 (2 corrected by append), probe spans 10 true and 2 partly true.
  - Author's expectation: the non-author closure may judge C2 not verified as declared on this sufficiency ground. That ruling is the operator's.

## Sources & frontier

- Census command: `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kake`. Both runs print the pre-existing `W04 S033` and `ok`.
  - Round start: exit 0 (`.ufo/waves/round-35/census-before.txt`).
  - Round end: exit 0 (`census-after.txt`).
- Rows: 77 → 87 (`git show <rev>:corpus/SOURCES.md | grep -c '^| S0'` at `16a6b8b8` and at the tip).
- Rows added by tier:
  - Tier A +8: S078 RFC 9116, S079 securitytxt.org, S080 Jekyll options, S082 RFC 8615, S083 IANA registry, S084 and S085 (live files), S086 GitHub Docs Creating a Pages site. All are mined.
  - Tier C +2: S081 Wikipedia and S087, the former `.nojekyll` URL, now a 404. Both are rejected.
- Rows touched old → new:
  - S078–S080 and S082–S086: `—` → mined, opened 2026-10-22, recheck 90d, used-by the entry.
  - S081 and S087: `—` → rejected.
  - S006, S001, S002: used-by gains the entry (lists logged in the lesson).
  - S074: no cell changed; a note was appended.
- Gate: `corpus/lessons/round-35.md` `## Gate` records 11 lines with URL, access time and quotes of ≤25 words. Real rejects with reasons:
  - S081: a secondary restatement that grounds no publisher step.
  - S087: an HTTP 404 page with no redirect.
  - Wave 2 re-opened S086 and S087 live, and S078–S085 against their retained copies: all hold. The S087 word count was corrected from 11 to 12.
- Sourced claim: C2 cites S078–S080 and S082–S086. As noted above, its counter cannot prove the provenance.
- Frontier advanced: security.txt publishing on GitHub Pages is now held ground (`PROVINCE.md` "Round-35 security.txt publishing frontier step"). Wave-1 findings:
  - ds4cc at `7fc6aa2f` has no `.well-known/` and pins `upload-pages-artifact@v3`.
  - GitHub mints `Expires` at 30 days after each response.
  - 3 of 8 large hosts set Expires more than a year ahead.
- Mistakes mined: 5 rows in the lesson. Rows 1–3 come from round-34 routed defects 2–4; each fix is a check shown able to fail. Row 4 is the v1 hidden-byte counter weakness, fixed by v2. Row 5 is the C2 probe sufficiency defect, with `knowledge_control_check.py` exiting 1 on the wave-2 controls and 0 on the pre-build controls.
- Misroot sweep: `git -C /home/vgpnk/Projects/shokunin status --porcelain` shows no file from this lane's seats. The untracked `AGENTS.md`, `bm.json`, `live_s228.html`, `nama.html`, `s395.txt`, `tf_bavelas.html`, `wb2.html` and the staged `write` carry no kake content; left untouched.

## Trend verdicts

- **expansion: improved.** New held ground: security.txt publishing on GitHub Pages, with 10 new rows and an entry checked sentence by sentence by wave 2. The link-preview capability gained three rules and 11 fixtures. Evidence: the entry, `scripts/link_preview_audit.py`, and rows 77 → 87. Admission of C2 is the closure's call.
- **quality: improved.**
  - The round-34 tool defects carried open are closed: first og:url only, canonical inside template/svg, and one non-UTF-8 page stopping the audit.
  - A quadratic regression found by wave 2 was fixed.
  - S001/S002 used-by drift was repaired, and the S074 overclaim was corrected.
  - No harm in any earlier selftest or counter (`w2/CriticHarmCheck.md`). The citing-set candidate gate's findings went from 4 to 7, which is recorded.
- **discernment: improved.**
  - Targets were sealed, and do-nothing controls were scored before the build.
  - Two rejects with located reasons.
  - Five criteria checks are shown able to fail.
  - Wave 2 refuted both claims' sufficiency, and the refutation is reported, not hidden (mistake row 5, QUALITY (e)).
  - The non-author outside check is owed to the closure.

## SHONEN

- [~] SKILL.md has real decision tables, error patterns, checklists and cited sources: the `SKILL.md` gate registry row for the link-preview audit and its exit-2 correction (wave-2 `ReviewSkillRegistryRow35`: conforms field by field).
- [~] At least one end-to-end domain task executed and logged in LOG.md: the link-preview audit repair, measured on 24 sealed cases and on 102 real ds4cc pages (no regression, `w2/ExecRealInputRegression.md`). No live serving was observed.
- [~] Instructions executable by an agent without oral context: the counter, criteria and selftest commands are written with arguments in SCORECARD, QUALITY and SKILL. Wave 2 re-ran them from those strings; one receipt's elided command was rewritten in full.
- [~] No cross-domain bleed (PROVINCE.md accurate): the `PROVINCE.md` round-35 section keeps vulnerability handling and owned-site actions out of province (wave-2 `ReviewQualityProvinceReadme`).

## Round shape and seats

- Shape: two v1 waves (policy `ufo-wave-policy.json`). Each was validated and dispatched as one `task` call carrying the validator's `taskCall`, issued through the eval kernel's `tool.task`. A uniform `solutionSpace` string was added to each task; nothing else changed. `wave-slot.sh` granted and released both waves.
  - Wave 1 `kake-r35-w1`: 36 seats — 8 scribe, 8 reviewer, 6 executor, 6 scout, 4 critic, 1 revenger, 1 mutation-tester, 1 sentinel, 1 connector.
  - Wave 2 `kake-r35-w2`: 35 seats — 22 reviewer, 5 critic, 4 executor, 3 mutation-tester, 1 sentinel.
  - Round total: 71 seats. No residual call.
- Dead seats: none. Hold: wave-1 `CriticSealedDesign`, which hit an automatic model switch after a safety filter.
- Planner seat: held by the L1. The planning data walk rode `ConnectorSiblingOverlap`.
- Registries: `.ufo/waves/round-35/w{1,2}/swarm-registry.json`, with agent ids recorded. No `model` was passed; routing follows `task.agentModelOverrides`.
- Seat disclosures:
  - `ScribeEntryDraft` ran one `test -e` on the sealed directory path and read nothing.
  - The probe topics were public in the declaration, and the L1 named them in the drafter's item.
  - The L1 relayed two wave-1 findings to the builders: ds4cc facts and the S086 pointer to the drafter, and the `CriticHarmPlan` fixture list to the tool builder. Neither relay carried key content.

## Other

- Stale-lane: respawn-per-round driver; no other mission of this lane is open.
- Tool installs: none by the L1. Seats report only ephemeral `uv run --with`/`uvx` environments (lxml 6.1.3, html5lib 1.1, cmarkgfm 2024.11.20) and the host `cmark` 0.31.2; no persistent install. Pacman not used.
- Open L0 questions: none added.
- Carried open (lesson "Carried open" and "Wave-2 corrections"):
  - C2 counter v2 evasions found with the revealed key: fullwidth or zero-width comment closers, link reference definitions, fence length, substring URL and used-by checks, S086/S087 not pinned.
  - Counter crash paths (exit 1 instead of 2).
  - `<template/>` semantics, and the stale comment at `link_preview_audit.py:71-72`.
  - Criteria-check false passes (18 of 32 mutants survive the receipts).
  - Git-pin mutants, option tables, NUL-byte crash, freshness-pins re-pin, round-31 F1–F3.
