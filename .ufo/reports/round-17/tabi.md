# tabi — round 17 (hyaku phase 2, attempt 1)

Lane `tabi-shokunin`, branch `master`. Baseline `5859243183c4d7ac5429dfdb8a73ce0d9a43d583`
(clean). Measured revision `93bfead1f5f25f584353df3152a60209bbd89a2e`. Records landed at
`f97e7f7fcd391d62d841c29e92949fcb6402296b`; the delivered-tip binding receipt lands in the final
lane commit cited under Landed changes. Round prompt `.ufo/prompts/tabi-round-17.md`; lane plan
`tabi-shokunin/.ufo/waves/round-17/PLAN.md` (with its "L1 amendments after wave 1").

## Work performed

Declared claims (3, causally separable; no exploratory claim):
- **C1 — operability 8 (lowest tie):** jj lane-tip anchoring of the round gates. Count
  `c1_anchor_safe` 0 → 4.
- **C2 — coverage 9 + capability `webmcp-cdp-invocation` (sourced, S041–S048 opened this round):**
  WebMCP tool invocation over CDP as committed evidence. Count `c2_invocation_held` 0 → 1.
- **C3 — adjacency 8 (lowest tie):** checked sibling-overlap map recording the round-16 integrator
  CDP ruling and open contested scope. Count `c3_adjacency_verified` 0 → 10.

Work items:
- Lane-tip `laneTip` (symbolic-ref `--no-recurse`, branch else `refs/heads/master`, constructed git
  env) threaded through every live HEAD read in `scripts/check-round-contract.mjs` (`:114`),
  `scripts/check-user-round-contract.mjs` (`:160`, identity pair rotated `8a573b4e…`→archived,
  current `1579a794…`), `scripts/check-measurement-binding.mjs` (`:267`, default `--at`; selftest
  59→76). Red at baseline bytes, green after: `tabi-shokunin/.ufo/waves/round-17/w1/GateRoundAnchor.md`,
  `GateUserAnchor.md`, `GateBindAnchor.md`; real jj at M: `w2/JjRealAfter.md`.
- JjAudit routed items: 12 live R1 reads and 4 R2 `code_revision` diagnostics fixed (inventory
  `.ufo/waves/round-17/c1-sites.json`, residue 20/31/1 → 0/0/0); `check-freshness --witness HEAD`
  **not fixed in code**: the file is byte-frozen by `protectedPath` in both round gates and the pstack
  census (`w1/RevF6Repro.md`, sandbox `history_rewritten`); SKILL round 17 carries the invocation rule
  `--witness "$(git rev-parse --verify refs/heads/master)"` (unenforced).
- C2 harness `scripts/webmcp-invoke-round17.mjs`, receipt
  `corpus/evidence/round-17/webmcp-invoke/receipt.json` (11/11 + 4 controls incl. `cancelInvocation`
  → `Canceled`; producer `de62820d…`; reproduced 7× in `w2/ReRunHarness.md`), note
  `corpus/knowledge/webmcp-invocation-round-17.md`, sources S041–S048 + corrections S054–S057.
- C3 `corpus/adjacency.tsv` (10 rows, 7 siblings) + `scripts/check-adjacency.mjs` (self-test 57);
  fleet L0 questions filed: `ebeb396` (line 62, the-musketeer CDP lease kagi/kake) and `b6b3b5e`
  (line 65, ruling reach to revenger and kama).
- Round-16 spot-check routed defects 1–5: liar probe rooted (`corpus/evidence/round-17/routed/liar/`,
  identity-exact rebuild, `w2/ReRunLiar.md`); hardened-gate and `1205d26` receipts
  (`routed/binding-hardened/`); census U3 and r16 note `:135` README index rows (in-file pointer
  impossible: sha-pinned); ruling recorded in the map (PROVINCE is census-frozen). "Unforgeable"
  turned into QUALITY 27; all five turned into QUALITY 26–32 (lesson-backed).
- Planner seat: the L1 held it; bounded planning data-walks rode scout/connector/revenger items.

## Landed changes

| Commit | Content | LOG |
|---|---|---|
| `6c97851034e9d8f58b135d28ff969f1f28fa2f7d` | C1 gates, C2 harness/receipt/note/sources, C3 checker/map, routed evidence, wave-1 evidence | LOG round 17 |
| `93bfead1f5f25f584353df3152a60209bbd89a2e` | wave-2 repairs: checker/map, counters, note/source corrections, lifecycle probe | LOG round 17 |
| `f97e7f7fcd391d62d841c29e92949fcb6402296b` | measurements, binding manifest, lesson, LOG/SCORECARD/SKILL/QUALITY | LOG round 17 |
| final lane commit (cited in the closing line below) | delivered-tip binding receipts `corpus/evidence/round-17/binding/`, late wave-2 reports | LOG round 17 |

Fleet commits: `ebeb396`, `b6b3b5e` (tabi L0 lines).

## Before → after measurements

| Claim | Command | B 5859243 | M 93bfead | Counter sha256 at M |
|---|---|---|---|---|
| C1 | `node .ufo/waves/round-17/measure-c1.mjs REV` | 0 | 4 (4 label-only witness entries not credited; 8 total) | `1bb9804a…` |
| C2 | `node .ufo/waves/round-17/measure-c2.mjs REV` | 0 | 1 (15 bound cases+controls, 17 forgery probes 0) | `079dcc39…` |
| C3 | `node .ufo/waves/round-17/measure-c3.mjs REV` | 0 | 10 (ruled 1 integrator, contested-open 4 tabi-filed, split 2, refused 3) | `372c9658…` |

- Outputs: `tabi-shokunin/corpus/evidence/round-17/measurements.json`; manifest
  `corpus/evidence/round-17/measurement-binding.json`.
- Binding at the records tip `f97e7f7`: `--check … --at f97e7f7… --reproduce` → exit 0
  `MEASUREMENT_BINDING verdict=clean claims=3 bound=3` (receipt `corpus/evidence/round-17/binding/check-at-tip.json`).
  Selftest at the round-17 gate: exit 0 (76 cases) `binding/selftest.json`. The round-16 manifest is
  red at the round-17 tip by design (`counted_input_changed`; `binding/r16-check-at-tip.json`); its
  valid receipt is `routed/binding-hardened/check-at-1205d26.json`.
- No-harm: all 20 harm-baseline entries keep their exits (`w2/HarmAfter.md`); ROUND_CONTRACT clean 10;
  USER `round_count` 6/10 red as at baseline; freshness clean 34; SOURCES gate clean 57.
- No scalar moves (`w2/CriticScalars.md`).

## Sources & frontier

- Census command: `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin tabi`.
  Start: exit 0, rows 40 (A31/B4/C5; mined33/queued2/rejected5). End: exit 0, rows 57
  (A46/B4/C7; mined42/queued8/rejected7).
- Rows added by tier: A 15 (S041–S052, S054–S056), C 2 (S053, S057 rejected). Touched old→new: none in
  place (S032 re-opened, held). S049–S052, S055, S056 stay `queued` (the lesson that cites them
  lands after the measured revision).
- Frontier advanced: README frontier "tool invocation as committed evidence" held for Chromium 154
  loopback with flags; real-site, agent-side, Chromium 152 and default-profile stay open.
- Mined mistake: `tabi-shokunin/corpus/lessons/round-17.md` `## Mistakes` (9 rows). Sourced claim: C2
  (note `source:` S041–S048, S054).

## Trend verdicts

- **expansion: improved** — note `webmcp-invocation-round-17.md` on map-uncovered ground
  (`corpus/README.md:303` frontier), every `source:` row mined A opened this round; capability row
  entered with an in-round demonstration. Four of its cases repeat round-16 probe observations
  (quality, not expansion); C3 and source rows are not counted as expansion.
- **quality: improved** — routed defects 1–4 fixed with committed receipts; probe → receipt
  supersession; counters hardened against 23 C2 forgeries and the C3/C1 survivors; no harm.
- **discernment: unchanged** — author-side only: wave-2 non-author seats overturned the kasegi row and
  four source rows (corrected), and QUALITY 26–32 are lesson-backed, but no outside agreement exists
  yet.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — `SKILL.md` round-17 registry and WebMCP decision rows
- [~] At least one end-to-end domain task executed and logged in LOG.md — `corpus/evidence/round-17/webmcp-invoke/receipt.json`; LOG round 17
- [~] Instructions executable by an agent without oral context — `corpus/knowledge/webmcp-invocation-round-17.md` §Recheck procedure
- [~] No cross-domain bleed (PROVINCE.md still accurate) — `corpus/adjacency.tsv`; `PROVINCE.md` byte-unchanged

## Round mechanics and extras

- Waves: wave 1 86 seats (scout 22, executor 19, reviewer 12, scribe 9, connector 8, critic 6,
  revenger 4, sentinel 2, mutation-tester 2, simplifier 2), all 86 reported; dispatch refused once by
  the 100-job cap, spawned on retry 2. Wave 2 78 seats (scout 24, reviewer 23, executor 8, critic 7,
  scribe 5, mutation-tester 4, sentinel 3, connector 3, revenger 1). Round total 164. Specs, validation,
  registries, assignments under `tabi-shokunin/.ufo/waves/round-17/w{1,2}/`.
- Dead seats (never respawned): wave 2 — 17 m_zfl seats on `zai/glm-5.3-flash` 429 retry exhaustion
  (RevDiffUser, RevDiffBind, RevIdentityChain, RevAttachedIdentity, RevSitesInventory,
  RevFreshnessWhyNot, RevOtherScriptsHead, ConnJjSiblingsAfter, RevReceiptErrors, RevReceiptDecl,
  RevReceiptConc, ConnReadmeC2, RevC3Counter, ConnUnmappedOverlaps, RevRoutedHardenedAfter,
  RevRouted4, RevLessonDraft) and SentinelC3After (provider cyber-policy refusal); further seats
  still unreported at report time are listed in the closing line. Residual checks covered by other
  seats or the L1: identity chain and harm (L1 sandbox runs + `w2/HarmAfter.md`), receipt chains
  (`w2/CriticPredicates.md`, `w2/CriticC2Final.md`, `w2/RevNoteVsReceipt.md`), freshness why-not
  (`w1/RevF6Repro.md`), C3 counter (`w2/ForgeC3Checker.md`, `w2/CriticC3Final.md`).
- The L1 session exited once on an Anthropic 429 and was resumed under the same identity; three
  wave-1 seats (C2Harness, C3Checker, C3Counter) were revived by message, not respawned.
- Misroot sweep: `git -C /home/vgpnk/Projects/shokunin status --porcelain` shows no tabi seat file at
  the fleet root (only `.ufo/state/*.report-baseline` driver files); none moved.
- Inherited state: none (lane clean at dispatch; no earlier attempt).
- Open L0 questions: `.ufo/l0-questions.md:62` (musketeer lease), `:65` (ruling reach to revenger, kama).
- Tool installs: none by the L1; wave-2 seat RevNoteVsReceipt installed acorn 8.19.0 via npm into
  its /tmp sandbox only. No pacman transaction.
- Stale-lane: respawn-per-round driver; no other mission of this lane is open.
- Open debt: harness hardening (DevTools port, SIGTERM, downloads, merged feature switches), self-test
  cases for mutation survivors in the three gates, kaidoku's half of the ruling, frozen closure-checker
  certification (protocol/operator).

Closing: delivered lane tip `1b0bc7bbfec0305e0332a5e3b382d78f22248551` (helper `landed`; `state
local=remote=1b0bc7b… ahead=0 behind=0`) carries the `binding/` receipts; between `f97e7f7` and it only
`corpus/evidence/round-17/binding/` and wave-2 reports changed, so the bound counted inputs hold by
drift diff (`git diff --name-only f97e7f7 1b0bc7b`). End census exit 0. Wave-2 seats unreported at
report time: RevLabelOnly (dead, zai 429); RevDiffRound, RevBindSelftestCases, RevC1Fallback,
RevLocalVsPushed, RevNoteVsSources, RevSearchLog, RevSkillDraft (still running, results not used).
