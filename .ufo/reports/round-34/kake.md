# kake — round 34 report

L1 `KakeR34` (hyaku in-session, attempt 1). Lane `/home/vgpnk/Projects/shokunin/kake-shokunin`.
Base `1e54c89515b0b1f7c9d7d10e6232d15e43320713`. Lane tip (pushed) `ce72dd1b31673f62c54e4663ffa9723a53caf79d`.
No earlier attempt of this round (`.ufo/watchdog.log` has no `lane-dead-no-report kake round=34` line). No inherited leftovers: lane status was clean at start.

## Work performed

Declared claims (`SCORECARD.md` "Round 34 — declared claims", commit `d08d8de`, with the frozen matrix and both counters in the same commit, before any implementation). Both claims open a frontier area the lane never held, link-preview metadata (Open Graph tags that platforms read to build a card for a shared URL). Neither touches the citing-set gate.

- **C1 — operability (capability):** an offline link-preview audit `scripts/link_preview_audit.py`. Counter `c1_matrix_count.py` (28 frozen cases, four constant gates): 0/28 → 28/28 with all constants rejected.
- **C2 — freshness (sourced learning claim on S067–S070):** `corpus/knowledge/link-preview-metadata.md`, plus one ds4cc census line equal to the counter's own recount of retained upstream HTML at `7fc6aa2f`. Counter `c2_source_census.py`: met 0/5 → 5/5.

Work items:
- Sources were opened with `.ufo/waves/round-34/fetch_sources.py`. S067–S072 at 20:57Z, before the declaration commit; S073–S077 at 21:08–21:09Z, after wave 1. Receipts and retained text are in `.ufo/waves/round-34/sources/`.
- ds4cc HTML retained as `sources/ds4cc-7fc6aa2f/html.tar.xz` (a `git archive` of 102 pages) plus `tree.txt`. Wave-1 `ExecUpstreamBlobExact` found it byte-identical to a fresh `git archive` from a fresh clone, and upstream head is still `7fc6aa2f`.
- C1 build (`5613071`):
  - Tool written by wave-1 `ExecLinkPreviewGate`. The L1 corrected the docstring sourcing: the canonical-link and absolute-og:url rules are labelled lane policy.
  - Committed selftest `scripts/link_preview_selftest.py`, 29 fixtures, none copied from the matrix (`24a1647`). Raised to 35 fixtures at `76fac3b`.
- C2 build (`9ef758c`):
  - Entry drafted by wave-1 `ScribeEntryDraft`.
  - Rows S067–S077 in `corpus/SOURCES.md`.
  - `corpus/lessons/round-34.md` with Gate, Mistakes and routed dispositions.
- Wave-2 repairs (`76fac3b`):
  - Tool fixes:
    - Duplicated attributes now keep the first value.
    - `og:image:url` counts as `og:image` (S067).
    - A FIFO or a page over 16 MiB is `page_unreadable`.
    - An unparsable canonical href is a finding instead of a traceback with no JSON.
    - A repeated `--manifest` is exit 64; a duplicated manifest key is `input_invalid`.
  - Three new fixtures kill the three mutants that survived the counter and the 29-fixture selftest (`verification/selftest-w2-survivor-mutants.txt`).
  - Criterion-check repairs: fenced Gate lines, status-word reasons, text receipts, lookup-check exit contract.
  - S077 re-tiered from B to A.
- Round-33 spot-check routing (`corpus/lessons/round-34.md` "Round-33 routed defects — disposition"):
  1. Hollow shapes are carried by name, including the names wave 2 found missing: misplaced section, `S0650`, N1.
  2. `489714be` and both option-table patches are retained in `.ufo/waves/round-34/retained/` (`a2fe31b`). Wave-1 `ReviewRetainedEvidence` verified them.
  3. This Gate records 4 rejects with located reasons, and `criteria/gate_reject_check.py` is shown able to fail.
  4. `criteria/receipt_presence_check.py` is shown able to fail on the round-33 report. Every run this report cites has a committed receipt.
- Mistake mined in-round (lesson row 4): both declared counters give their full score to a control that does none of the work.
  - Wave-1 `CriticDeclarationFit` built both controls: the C1 lookup-table tool `dcef39b5` (28/28) and the C2 transcription commit `0cce15f0` (5/5).
  - Both are retained as bundles.
  - Fix: QUALITY round-34 criterion (d), with `criteria/lookup_control_check.py`, which gives exit 1 on the frozen C1 counter.
- QUALITY "Round-34 criteria" (a)–(d) plus wave-2 corrections. SKILL table "Link-preview metadata — round 34". PROVINCE frontier step and README coverage row. Capability row entered.
- Carried items, outside the claims:
  - Git-pin mutants: wave-1 `ExecPinMutantsGateCode` prototype kills m3f and m3g; m3d is equivalent. Sandbox only, not landed.
  - Option-table alt patch: `ExecOptionTableAltPatch` advises against landing it unconditionally (it relaxes the fail-closed allowlist). Not landed.
- Holds `KakeR31.CriticC1Counter` and `KakeR31.CriticSandboxThreatModel`: not recreated. Both wave contexts fenced them off.

## Landed changes

All landed through `jj-lane.sh` (`landed` lines). Each is tied to the LOG.md "Round 34" entry.

| commit | content |
|---|---|
| `d08d8de26c9a4290c44282b0eee2b860e8ea4ecc` | declaration; frozen matrix and both counters; fetcher; sources S067–S072; ds4cc archive; census before |
| `a2fe31b2d1d2bf67f832b31fb994869b83dbdb9f` | before receipts; round-33 evidence retained |
| `5613071e0107544d825e37db1e98f0bfcfb61465` | C1 tool |
| `9ef758c95d5e2e4d983df53ad00a084e2c5fb36f` | C2 entry; SOURCES S067–S077; lesson; S073–S077 opened |
| `24a16474ee73e20453f3e1be9d2f33573c5196d9` | wave-1 integration:<br>- selftest and fixtures; criteria checks; retained controls; receipts<br>- QUALITY, SKILL, PROVINCE, README and SCORECARD sections; LOG<br>- wave-1 reports and registry |
| `76fac3b76f281d8ef136abfcc491e6e575e97083` | wave-2 repairs: tool, fixtures, checks, retained fixtures, S077 tier |
| `2ac06c5356e0f38b6a27ce1c709238e650ff0461` | wave-2 reports and registry; receipts at `24a1647` and `76fac3b`; census after; wave-2 corrections |
| `ce72dd1b31673f62c54e4663ffa9723a53caf79d` | receipts at `2ac06c5` |

## Before → after measurements

| claim | command | before | after |
|---|---|---|---|
| C1 | `python3 -B .ufo/waves/round-34/c1_matrix_count.py --root . --revision <rev>` | `1e54c89`: 0/28; `d08d8de`: 0/28 | `5613071`: 28/28; `9ef758c`: 28/28; `24a1647`: 28/28; `76fac3b`: 28/28; `2ac06c5`: 28/28 |
| C2 | `python3 -B .ufo/waves/round-34/c2_source_census.py --root . --revision <rev>` | `1e54c89`: met 0/5; `d08d8de`: met 0/5 | `9ef758c`: met 5/5; `24a1647`: met 5/5; `76fac3b`: met 5/5; `2ac06c5`: met 5/5 |

- Receipts: `.ufo/waves/round-34/verification/c1-at-<rev>.json` and `c2-at-<rev>.json`. All C1 receipts show the four constant gates rejected; all C2 receipts show `controlBroken` false.
- Wave-2 `RerunC1Counter` and `RerunC2Counter` reproduced every receipt field for field. Counter bytes are unchanged since `d08d8de`.
- Both counters are necessary, not sufficient (disclosed in SCORECARD measured results and lesson mistake row 4). A lookup-table tool scores C1 28/28, and a transcription commit scores C2 5/5. Admission rests on a non-author read of the landed tool and entry. Corroboration available for that read, none of it counted toward a claim:
  - Selftest 35/35: `selftest-link-preview-at-76fac3b.txt`.
  - Real-input run over the 102 pages, matching the census: `real-input-at-5613071.json` and `real-input-at-76fac3b.json`. It exercises only the missing-property rule.
  - Census recounts with lxml and html5lib match all seven numbers (wave-1 `ExecCensusIndependentRecount`, wave-2 `ExecCensusThirdMethod`).
  - An independent lxml implementation scored 28/28 on its first attempt (wave-1 `ExecIndependentOracle`).
  - strace shows no socket and no write-mode open (wave-2 `ExecNetworkFreeProof`).
- Census line: `pages=102 og:title=87 og:type=87 og:image=1 og:url=87 all-four=1 og-url-equals-canonical=87`. The totals were seen in screening before the declaration (disclosed there). The counter hard-codes no number.
- Separability: tip without the tool gives C1 0/28 and C2 5/5; tip without the entry and the rows gives C1 28/28 and C2 0/5 (wave-2 `ExecSeparabilityAtTip`).

## Sources & frontier

- Census command: `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kake`. Output both times: the pre-existing `W04 S033` and `ok`.
  - Round start: exit 0 (`.ufo/waves/round-34/census-before.txt`).
  - Round end: exit 0 (`census-after.txt`).
- Rows: 66 → 77 (`git show <rev>:corpus/SOURCES.md | grep -c '^| S0'` at `1e54c89` and at the tip). Census mode after (`census-mode-after.txt`): A64 / B1 / C12; mined 56.
- Rows added by tier:
  - Tier A +9: S067 ogp.me, S068 Facebook webmasters guide, S069 Slack robots, S070 Mastodon PreviewCard and S073 Discord link previews (mined); S072, S074 (rejected); S076 oEmbed and S077 jekyll-seo-tag (queued).
  - Tier C +2: S071 and S075 (rejected).
- Rows touched old → new:
  - S067–S070 and S073: `—` → `mined`, opened 2026-10-22, recheck 90d, used-by the entry.
  - S071, S072, S074, S075: `—` → `rejected`.
  - S076, S077: `—` → `queued`.
  - S077 tier: B → A (wave 2).
  - No earlier row changed (wave-2 `CriticHarmCheck`).
- The Gate in `corpus/lessons/round-34.md` `## Gate` records URLs, access times and quotes of ≤25 words. It has 4 rejects with located reasons:
  - S071: the X cards markup URL now redirects to a generic docs index.
  - S072: a repository setting, not page metadata.
  - S074: the Telegram Bot API names no page tag.
  - S075: a LinkedIn JavaScript shell.
  - Wave 2 re-opened all of them; the reasons hold (`w2/ReopenSourcesRejected.md`, `w2/ReopenSourcesMined.md`).
- Sourced claim: C2 cites S067–S070.
- Frontier advanced: link-preview metadata moves from absent to held Frontier ground, with a source-backed entry and an offline gate (`PROVINCE.md` "Round-34 link-preview frontier step"). Ds4cc findings, all offline and operator-gated:
  - 101 of 102 pages lack `og:image`.
  - 15 pages lack the title/type/url triple.
  - The `bloat.html` and `exa.html` canonicals disagree with the sitemap.
- Mistakes mined (lesson `## Mistakes`): four rows (routed items 2–4 and the in-round lookup-control mistake), each with a check or retained file shown able to fail.
- Seat boundary: wave-1 `MutC2CounterConditions` briefly wrote rows into the lane's `corpus/SOURCES.md` and removed them. This was self-disclosed; the restored hash equals `a2fe31b`, and the committed `9ef758c` file holds the L1's rows (LOG).
- Misroot sweep: `git -C /home/vgpnk/Projects/shokunin status --porcelain` shows no file written by this lane's seats. Untracked `AGENTS.md`, `bm.json` (a Cloudflare challenge page with no kake content), `live_s228.html`, `nama.html`, `tf_bavelas.html` and `scripts/hyaku/__pycache__/*.pyc` are not this lane's; left untouched.

## Trend verdicts

- **expansion: improved.**
  - A lane-new area: link-preview metadata from four primary platform sources plus Discord, and an offline audit capability.
  - The ds4cc per-page Open Graph breakdown, and other owned roots' Open Graph state from the round-23 captures.
  - Evidence: `corpus/knowledge/link-preview-metadata.md`, `scripts/link_preview_audit.py`; rows 66 → 77.
- **quality: improved.**
  - Wave 2 checked the entry: 28/28 core quotes and 18/18 crawler and census quotes are exact, and all 12 wave-1-addition claims hold (`w2/ReviewEntryCoreSections.md`, `ReviewEntryCrawlerCensus.md`, `ReviewEntryWave1Additions.md`).
  - Tool crash and hang paths found by wave 2 were repaired, and the selftest grew to 35 fixtures.
  - Round-33 sandbox-only evidence is now in the lane.
  - No harm found (`w2/CriticHarmCheck.md`, `w2/ExecOtherGatesUnchanged.md`).
- **discernment: improved.**
  - The Gate rejects 4 of 11 sources with located reasons.
  - Four QUALITY criteria, each with a check shown able to fail.
  - The round's own counters were shown insufficient and disclosed, not hidden (lesson mistake row 4).
  - Wave-2 corrections were appended, not rewritten.
  - The non-author outside check is owed to the closure.

## SHONEN

- [~] SKILL.md has real decision tables, error patterns, checklists and cited sources: `SKILL.md` "Link-preview metadata — round 34" (wave-2 `ReviewSkillTable34`: rows grounded, with S068 offsets corrected by append).
- [~] At least one end-to-end domain task executed and logged in LOG.md: an offline Open Graph audit of the retained ds4cc source (LOG.md round 34, `verification/real-input-at-76fac3b.json`). No live serving or platform card was observed.
- [~] Instructions executable by an agent without oral context: tool, selftest, counters and criteria commands are written with arguments in SKILL, QUALITY and SCORECARD. Wave 2 re-ran them from those strings.
- [~] No cross-domain bleed (PROVINCE.md accurate): `PROVINCE.md` round-34 section, verified by wave-2 `ReviewProvinceReadme34`. Crawler behaviour is framed as publisher-side placement (wave-1 `CriticFrontierNovelty` 3).

## Round shape and seats

- Shape: two v1 waves (policy `ufo-wave-policy.json`). Each was validated and dispatched as one `task` call carrying the validator's `taskCall` context and tasks. The tool schema requires `solutionSpace`, so one uniform `solutionSpace` string was added to each task; nothing else changed. `wave-slot.sh` granted and released both waves.
  - Wave 1 `kake-r34-w1`: 32 seats — 10 executor, 7 scribe, 5 scout, 4 reviewer, 3 critic, 2 mutation-tester, 1 connector.
  - Wave 2 `kake-r34-w2`: 35 seats — 19 reviewer, 5 executor, 5 critic, 3 mutation-tester, 2 scout, 1 sentinel.
  - Round total: 67 seats. No residual call.
- Dead seats: none. Refusal holds: none.
- Planner seat: held by the L1. The planning data-walk rode `ConnectorSiblingOverlap`.
- Registries: `.ufo/waves/round-34/w{1,2}/swarm-registry.json` (agent ids recorded). Routing follows `task.agentModelOverrides`; no `model` was passed.
- Partial seat output: wave-1 `MutC1CounterWrongGates` built 1 of the 10 asked variants (disclosed in SCORECARD). Wave-2 `MutToolRuleBreaks` covered the rest (13 mutants).

## Other

- Stale-lane: respawn-per-round driver; no other mission of this lane is open.
- Tool installs: none by the L1. Seats report none (wave seats used `uv run --with lxml/html5lib` ephemeral environments; no persistent install recorded). Pacman not used.
- Open L0 questions: none added.
- Carried open (lesson):
  - The C1 counter leaks the case id through the case directory name.
  - C2 counter defects D1–D4 (fence after the header, fence-blind registry, escaped pipe, crash paths).
  - Tool: only the first og:url is compared; the first canonical link may sit in `<template>` or `<svg>`; one non-UTF-8 page stops the whole manifest.
  - Git-pin mutant patch not landed; option tables.
  - NUL-byte runner crash; null codes; `freshness-pins.json` re-pin; no freshness pin on the ds4cc census commit.
  - Round-31 F1–F3.
