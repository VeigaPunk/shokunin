# tabi — round 100

L1 `TabiR100`. Base `9a478a2e`. ONE claim: C1 coverage, the new capability generation
`client-oopif-uploadsets-linux` (duplicate names kept, a 0-byte payload lands as a real file, one path +
one payload refused client-side, both client-launched browsers land two paths trusted, a directory walks
recursively on a `webkitdirectory` input). Freeze `468c2b94` (frozenAt 2026-11-09T03:14:58-03:00),
scored `88b488db` (clean, 216 checks, 18 legs, nonce `tabi-r100-live-6e6168fce8a4`), records `ce29c653`,
wave evidence `9979f3df`, wave reports `2ac50293`.

## Work performed

- Declared claim C1 (coverage, capability `client-oopif-uploadsets-linux`, predicate
  `C1-CLIENT-OOPIF-UPLOADSETS-R100`) with its falsifiable before→after; least-axis rule: all six axes
  sit at 9, so C1 works coverage (a lowest tie at 9) and is a capability acquisition — `plans/round-100.md:1`.
- Opened S248-S250 this round (fetched, byte-counted, sha256-pinned; staged
  `.ufo/waves/round-100/sources/`, fetch log updated post-wave) and re-opened S237/S238/S240/S216
  byte-identical — `corpus/SOURCES.md:263-265`, `corpus/lessons/round-100.md:8-30`.
- Pre-freeze probe: 6 arms × 2 reps all as the predicate states; counter `--reps 1` clean 80 checks
  `.ufo/waves/round-100/probes/probe-a-log.txt`, `probe-a-score.json`.
- Froze and committed the instrument bytes + controls: driver `97947b0b1a45…`, counter
  `5c3d56d83377…`, battery `39c2b7284512…` (121/121), live killers `daf1282a7904…` (6/6)
  `468c2b94` + `claims.json` (frozenAt 03:14:58).
- Scored run: `node scripts/check-client-oopif-uploadsets-round100.mjs --live` → rc 0, clean, 216
  checks, 0 findings over 18 legs `.ufo/waves/round-100/scored/c1-live.json` @ `88b488db`.
- Ran one batched 12-seat wave (3 executor, 2 critic, 1 mutation-tester, 1 revenger, 1 reviewer,
  1 sentinel, 1 scout, 1 scribe, 1 connector; attack share 4/12 = 33 %; L1 holds the planner seat)
  `.ufo/waves/round-100/w1-results.json`; 10 neutral, 2 falsifies-wording (R100Critic1 W2, R100Critic2
  citations), both narrowed by post-wave amendments; reproductions R100Exec1 ×2 clean 216 and
  R100Exec2 reps-10 clean 678; live killers 6/6; battery 121/121; mutation sweep 112 mutants / 56
  killed / 11 survivors (all equivalent, live-only or cosmetic) `.ufo/waves/round-100/w1/`.
- Landed records: knowledge note `corpus/knowledge/client-oopif-uploadsets-round-100.md`,
  lesson with Gate + 4 mistakes `corpus/lessons/round-100.md`, `SKILL.md` `## Round 100 gate registry`,
  `corpus/README.md` `## Round 100 coverage`, SCORECARD round-100 section + capability row, LOG entry,
  falsification ledger `.ufo/waves/round-100/claim-falsification.tsv` — all committed below.

## Landed changes

| Change | LOG entry | Commit |
|---|---|---|
| S248-S250 rows + search-log line; staged sources + fetch log (incl. post-wave `elementHandle.ts` line) | `LOG.md` Round 100 | `ce29c653` |
| Knowledge note `client-oopif-uploadsets-round-100.md` (source/verified-at/recheck trio, S248-S250) | `LOG.md` Round 100 | `ce29c653` |
| Lesson `round-100.md` (Gate, 4 mistakes, wave, leads) | `LOG.md` Round 100 | `ce29c653` |
| `SKILL.md` `## Round 100 gate registry` (4 gates) | `LOG.md` Round 100 | `9979f3df` |
| `corpus/README.md` `## Round 100 coverage` + frontier | `LOG.md` Round 100 | `9979f3df` |
| SCORECARD round-100 section + capability row; LOG round-100 entry | `LOG.md` Round 100 | `9979f3df` |
| Amendment A2 (narrowing, R100Critic2) in `plans/round-100.md` | `LOG.md` Round 100 | `9979f3df` |
| Wave evidence + falsification ledger (12 rows) + census-end | `LOG.md` Round 100 | `9979f3df` |
| Wave seat reports + `w1-results.json` + dispatched markers | `LOG.md` Round 100 | `2ac50293` |
| Freeze (plan, claims, 4 instruments, controls, probe, staged sources, census-start) | `LOG.md` Round 100 | `468c2b94` |
| Scored run + committed receipt | `LOG.md` Round 100 | `88b488db` |

## Before → after measurements

- Claim C1 (coverage, capability `client-oopif-uploadsets-linux` generation r100).
  - Counted by: `node scripts/check-client-oopif-uploadsets-round100.mjs --lane /home/vgpnk/Projects/shokunin/tabi-shokunin --expect-driver-sha256 97947b0b1a4522a48cf08c3681bc13368534608841094a755dd4cf938b306b90 --live --deps <ABS npm install of puppeteer-core@25.16.0 playwright-core@1.65.0> --scratch <ABS scratch> --ports <http,child,cdp> --json` (predicate `C1-CLIENT-OOPIF-UPLOADSETS-R100`).
  - Before (base `9a478a2e`): `git cat-file -e 9a478a2e:scripts/check-client-oopif-uploadsets-round100.mjs` → rc 128; the r99 receipt under the frozen counter → rc 1 (`counter-donothing-r99.json`).
  - After: `--live` → rc 0, verdict `clean`, 0 findings, checkCount 216 over 18 legs (6 arms × 3 reps); measured commit `88b488db`, measured revision `9a478a2e`, nonce `tabi-r100-live-6e6168fce8a4`; receipt `corpus/evidence/round100/client-oopif-uploadsets/receipt.json` (sha256 `dac0998fce3b…`).
  - Kill rule: scoped run exits 0 with 0 findings; every frozen control (`rc.txt`) gives its expected verdict; no wave artifact shows a leg-level statement of the predicate false on a `--live` run of the pinned driver with the pinned libraries (R100Exec1 ×2 and R100Exec2 reps-10/default reproduce, R100Sentinel strace clean). Narrowings (A1 as frozen + A2 post-wave) do not touch the predicate, counter, kill rule or target.

## Sources & frontier

- Registry 247 → 250 rows (S248, S249, S250 new, all tier A, `mined`, `90d`, used-by
  `corpus/knowledge/client-oopif-uploadsets-round-100.md`).
- Counting command (run at round start and end from the lane root):
  ```sh
  /home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin tabi
  ```
  Start (`.ufo/waves/round-100/census-start.txt`): exit 1 with `tabi E11` on S248-S250 (the note naming
  them did not exist yet) — expected at round start.
  End (`.ufo/waves/round-100/census-end.txt`): exit 0, `tabi ok` (W04 duplicate-url warnings on older
  rows and on the new S249/S250 URLs, which share a URL with earlier rows by design).
- Rows added by tier: A ×3 (S248-S250). Rows touched old→new: none (re-opens of S216/S237/S238/S240 are
  byte-identical; no `status`/`recheck`/`used-by` cell changed).
- Frontier rows advanced: the r99-noted frontier items consumed here are duplicate names, empty
  *payload* files, directories (`webkitdirectory`), mixed path+payload calls, and the launch legs with
  two paths (all now counted legs); residual frontier is in `plans/round-100.md` Planned (r101).
- Frontier step (`corpus/SOURCES.md` contract v1): one sourced claim this round (C1 cites S248-S250);
  one mined mistake with evidence pointer and shown-able-to-fail — `corpus/lessons/round-100.md`
  `## Mistakes` (attribution, off-by-one, amendment ordering, narrow history sentence).

## Trend verdicts

- **expansion: improved** — Knowledge 112 → 113 notes on uncovered ground (three payloads, duplicate
  names, a deliberate 0-byte named payload, the mixed refusal, the client-launched two-path arms, the
  `webkitdirectory` walk) with a new capability row in SCORECARD; three new SOURCES rows (S248-S250)
  all tier A and `mined`, each cited by the r100 note. Evidence: `corpus/knowledge/client-oopif-uploadsets-round-100.md`,
  `corpus/SOURCES.md` S248-S250, receipt `corpus/evidence/round100/client-oopif-uploadsets/receipt.json`.
- **quality: improved** — r99 spot-check E1-E3 answered in-round: E1's whole-`scripts/` grep is the rule
  now; E2's R99Mut receipt-mode survivors (`missing-exists-zero`, `iframe-targetid-empty`,
  `resolved-errmessage-only`, `resolved-errname-only`, `files-d-key-dropped`) are battery cases and
  confirmed killed by the 121-case battery and the R100Mut sweep; E3 the provenance trio on the new note.
  No admitted entry failed its re-check (the scored receipt re-derives clean; R100Scribe's 37 jq
  cross-checks match). Evidence: `.ufo/waves/round-100/controls/battery.json`,
  `.ufo/waves/round-100/w1/R100Scribe-facts.json`, `corpus/lessons/round-100.md` §Gate.
- **discernment: unprovable-but-better** — the wave's adversarial seats caught a S250 attribution to
  the wrong document (the `webkitRelativePath` definition is not in WHATWG `input.html`), a
  `fileUploadUtils.ts` line off by one (44 vs 43), a missing fetch-log line, and the limit-8 first
  clause — and the lane narrowed all of them post-wave (plan §Amendment A2; the r100 note's append-only
  correction) instead of filing the wider wording. The ledger's two `falsifies-wording` rows are
  resolved. As the lane self-scores this `unprovable-but-better`: the narrowing is genuine evidence of
  externally-checked taste, but an L1 self-narrowing of its own overclaims is not the same epistemic
  achievement as a gate deciding — that judgment belongs to the non-author closure reviewer.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources
  `SKILL.md` `## Round 100 gate registry` (4 gates with verdict maps and pinned shas); the round-100
  knowledge note carries the decision table
  `corpus/knowledge/client-oopif-uploadsets-round-100.md`.
- [~] At least one end-to-end domain task executed and logged in LOG.md
  `LOG.md` Round 100 entry (scored run `88b488db`, clean 216 checks, nonce
  `tabi-r100-live-6e6168fce8a4`); also R100Exec1's two cold reproductions and R100Exec2's reps-10
  run, all filed under `.ufo/waves/round-100/w1/`.
- [~] Instructions executable by an agent without oral context
  `plans/round-100.md` §Counting command + `.ufo/waves/round-100/probes/probe-a-log.txt`
  (the driver bytes as frozen reproduce every leg); the wave's executors reproduced C1 cold from the
  plan text (R100Exec1/R100Exec2).
- [~] No cross-domain bleed (PROVINCE.md still accurate)
  `PROVINCE.md` unchanged this round; R100Connector found no sibling overlap (zero matches for
  upload/Puppeteer/Playwright/MIME over 20 sibling lanes' corpora).
