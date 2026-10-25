# kake — round 36 report

Lane `kake-shokunin`, base `b720d799ae99c19a7c97f2b1391d4fe928be0e11`, lane tip
`1a16b8e3faebcd24718c2cde6bf0c04b4c09cc59` (pushed; `jj-lane.sh state`: `local=remote=1a16b8e3…
ahead=0 behind=0 tracked=0 untracked=0`). Hyaku in-session L1 `KakeR36`, attempt 1.

## Work performed

Declared claim (one): **C1 — freshness (capability): offline source re-check audit
`scripts/source_recheck.py`.** The surface it changes is new: a tool that re-checks a
`SOURCES.md` row's quote against a recorded fetch of its source (until now the lane had only a
shape census). Frozen predicate, the same sentence in the plan, in the counter and in each
receipt: `met: passed >= 25 of 28 sealed cases`. No knowledge-entry claim this round (the
blocker of rounds 34 and 35).

- Repair first. Round-35 closure routed defects 1–5 each got a disposition
  (`corpus/lessons/round-36.md` "Round-35 routed defects — disposition"): QUALITY round-36
  (a)–(f) (`corpus/QUALITY.md`), four criteria checks shown able to fail
  (`.ufo/waves/round-36/criteria/`, receipts `verification/criterion-*.txt`), and the S084 and
  Preferred-Languages corrections appended (`corpus/lessons/round-35.md` end,
  `corpus/knowledge/security-txt-publishing.md` end).
- Sources opened before the declaration (01:08:56Z–01:09:01Z, `.ufo/waves/round-36/fetch_sources.py`,
  `sources/receipts.json`); each re-opened live by an independent wave-1 scout, byte-identical.
- Declaration with sealed key and frozen counter: `3555f63f`. Counter v2 (tool run in a
  bubblewrap jail; the L1's own review found the /proc command-line key leak): `9d81c75c`.
- Pre-freeze control wave `kake-r36-ctl` (7 seats): constant clean 0, all-false 0, no-reader 8,
  naive reader 12 and shortcut 17 of 28 under key v1. The shortcut passed every (e) and (f)
  case without opening a body, so key v2 (both answer polarities, rotated contentTypes) and
  counter v3 (pin only) landed before any build: `cd321279`. Rescored: 0, 0, 8, 12, 9; 36
  ablations of the L1's private reference 13–24; reference 28. Receipts
  `.ufo/waves/round-36/verification/control-*.json`, `ablations/`; bundles `retained/`.
- Wave 1 `kake-r36-w1` (36 seats): build `4d5b3d55` (tool by `ExecToolBuild`, landed unedited,
  sha256 `577b2d7d…0d48`), selftest 101/101 (`ExecSelftest`), live recorder
  `scripts/source_snapshot.py`, rows S088–S094, criteria checks, probes of the cited sources
  (cp1252, urljoin, html.unescape, quote matching), first falsifiers. Reveal `fd1fb723`.
- Measured: 0 → 28 of 28 (`verification/c1-keyrev-at-4d5b3d55.json`). An independent blind
  implementation also scores 28 (`verification/independent-selftest-reference.json`). The build
  also meets under counters v1 and v2 with key v1 (`c1-counter-v1-keyv1-at-4d5b3d55.json`,
  `c1-counter-v2-keyv1-…`).
- Real-input run (freshness evidence, not a claim): 90 Gate quotes recorded live and audited
  (`realrun/audit.json`, 14 findings); every flagged row re-opened by hand in wave 2; run 2
  (`realrun/audit-run2.json`) 8 findings, each explained; notes appended to `corpus/SOURCES.md`.
- Wave 2 `kake-r36-w2` (34 seats) attacked everything; all receipts reproduced. Found and
  recorded: the declaration's "skipping any one rule fails four cases" is overstated (9 of 32
  tool mutants and 5 of 6 new reference mutants still meet 25); tool defects outside the sealed
  set (attribute-embedded `<script`, symlink escape, FIFO and huge manifests); recorder defects.
  Post-measurement repairs (count toward no claim): symlink containment (sandbox re-measure 28 of
  28 at `bf9b2089`, `retained/r36-l1-postfix-remeasure.bundle`), recorder Accept-Language and
  redirect-scheme guard (`verification/postfix-snapshot-redirect-test.txt`).

## Landed changes

| Commit | What | LOG |
|---|---|---|
| `3555f63fbf58f19445823eb88bc3161b7b1faad4` | declaration, counter v1, sources opened, census before | LOG.md round 36 |
| `9d81c75c963cd9399c788e51bbd7f376fbe42cec` | counter v2 (jail), base and ablation receipts | LOG.md round 36 |
| `cd3212796cab7a2afa03b638dbfafe7194df9629` | control-wave receipts and bundles, key v2, counter v3 | LOG.md round 36 |
| `4d5b3d550748e5b52af31646b74c1aa435942bde` | C1 build: tool, selftest, recorder, rows S088–S094 | LOG.md round 36 |
| `fd1fb723624b742a00a6e8e908f3b42901d627f8` | reveal of key v2/v1, private reference, generator | LOG.md round 36 |
| `e5a293b6782f09bf4d5d2105aafda76350c21409` | wave-1 reports, criteria checks, real-input run, QUALITY, SKILL registry rows, round-35 corrections | LOG.md round 36 |
| `f3a38bf8e68f6cee386125d34b5e95ac9b2df66e` | measured results, capability row, lesson, LOG | LOG.md round 36 |
| `25f84872c9d6808d4e4e877da6bee09254ade18d` | wave-2 reports and corrections, real-run 2, symlink repair, SOURCES re-check notes | lesson "Wave-2 corrections" |
| `1a16b8e3faebcd24718c2cde6bf0c04b4c09cc59` | late wave-2 reports, recorder redirect guard, census after | lesson "Late wave-2 results" |

Inherited state: none (clean tree at base; no `lane-dead-no-report kake round=36` attempt).
Files not authored and not edited: `corpus/lessons/round-35-verifier-spotcheck.md`.

## Before → after measurements

| Claim | Before | After | Counting command | Measured revision |
|---|---|---|---|---|
| C1 | passed 0 of 28, met false, exit 1 (`b720d799`, `3555f63f`, `9d81c75c`, `cd321279`) | passed 28 of 28, met true, exit 0 | `python3 -B .ufo/waves/round-36/sealed_count.py --root . --revision <rev> --key-revision fd1fb723624b742a00a6e8e908f3b42901d627f8` | `4d5b3d550748e5b52af31646b74c1aa435942bde` |

The reveal commit itself is refused (exit 2, `c1-keyrev-at-fd1fb723.json`). No control or
ablation met the predicate under any counter version.

## Sources & frontier

- Rows before → after: 87 → 94 (`git show <rev>:corpus/SOURCES.md | grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|'`
  at `b720d799` and `1a16b8e3`).
- Added by tier: A 5 (S088 RFC 9110 redirects and status, S089 RFC 3986 resolution, S090 WHATWG
  Encoding, S091 UAX #15, S092 WHATWG HTML syntax; all mined, used-by `scripts/source_recheck.py`);
  B 1 rejected (S094 MDN); C 1 rejected (S093 Wikipedia). URLs, access times and quotes:
  `corpus/lessons/round-36.md` `## Gate`.
- Rows touched old→new: none (no status, recheck or used-by cell changed). Re-check notes for
  S040, S068, S004–S008, S016, S017, S025, S065, S066, S087 appended below the registry.
- Census: start `kake W04 S033 …` / `kake ok`, exit 0 (`.ufo/waves/round-36/census-before.txt`);
  end three W04 same-URL-across-scopes warnings (S033, S088, S092) and `kake ok`, exit 0
  (`census-after.txt`).
- Frontier advanced: source re-check moved from absent to a working instrument with a first live
  re-verification of 90 rows. Sourced claim: C1's contract rests on S088–S092.
- Mined mistakes: `corpus/lessons/round-36.md` `## Mistakes` (5 rows; base-hash typo, key-v1
  polarity, seats writing into the lane, selftest fixture contradiction, overstated coverage
  sentence), each fix shown able to fail where a check exists.

## Trend verdicts

- **expansion: `improved`** (author-side). A new capability row "Offline source re-check audit"
  (`SCORECARD.md` `## Capabilities`) with its demonstration (28 of 28; real-input run) and 5 newly
  mined rows on ground the lane never held (HTTP redirect semantics, URI resolution, encoding,
  normalization). Non-author admission pending.
- **quality: `improved`.** The first quote-level re-verification of the registry: 90 rows re-opened
  by recording, 13 findings re-opened by hand; 2 real moves (S040, S068), 5 Gate quotes with
  markdown backticks, 1 transcription, all noted; round-35 corrections appended.
- **discernment: `improved`.** 2 real rejects with located reasons (S093, S094, the latter
  against the scribe's draft); the pre-freeze control wave caught a key flaw before any build;
  QUALITY round-36 (e)–(f) from this round's own mistakes with checks shown able to fail.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources: `SKILL.md` "Source re-check audit gate registry — round 36" (verdict map, procedure; wave-2 `ReviewQualityAndSkill` ran each command).
- [~] At least one end-to-end domain task executed and logged in LOG.md: live re-check of 90 Gate quotes, LOG.md round 36 and `realrun/audit.json`, `audit-run2.json`.
- [~] Instructions executable by an agent without oral context: counter, selftest, recorder and criteria commands written with arguments; wave 2 re-ran them from those strings (`w2/RerunC1Sealed.md`, `w2/ReviewCriteriaChecks.md`).
- [ ] No cross-domain bleed (PROVINCE.md still accurate): PROVINCE.md untouched this round.

## Round shape and seats

- Shape: default two v1 waves plus a pre-freeze control call. Each v1 wave validated under
  `scripts/hyaku/ufo-wave-policy.json` and dispatched as one `task` call carrying the validator's
  `taskCall` unchanged (through `tool.task`); `wave-slot.sh` granted and released each.
  - Control call `kake-r36-ctl`: 7 seats — 5 critic, 2 mutation-tester (ordinary `task` call, ≤8).
  - Wave 1 `kake-r36-w1`: 36 seats — 11 executor, 9 scout, 6 scribe, 4 reviewer, 3 critic,
    1 connector, 1 mutation-tester, 1 revenger.
  - Wave 2 `kake-r36-w2`: 34 seats — 13 reviewer, 13 scout, 4 critic, 2 mutation-tester,
    1 sentinel, 1 executor.
- Round total: 77 seats. Planner seat: held by the L1 (validator rejects `planner`).
- Dead seats (holds, not retried): `CtlJunk`, `CtlCounterExploit`, `CriticClaimSufficiency`, each
  `[openai-codex/gpt-6.1-sol] … flagged for possible cybersecurity risk … (code=cyber_policy)`.
  The declared junk control therefore has no receipt.
- Containment: two wave-1 executors wrote their check scripts into the lane (verified by sha256,
  committed as evidence, mistake row 3). Misroot sweep (`git -C /home/vgpnk/Projects/shokunin status
  --porcelain`): no fleet-root file carries this lane or round.

## Gate

Real rejects: S093 (tertiary; cites RFC 2616, omits 308) and S094 (restates S088 and contradicts
it on Location for 300/304). Not admitted to the claim: post-measurement repairs.

## Other

- Stale-lane: respawn-per-round driver; no other mission of this lane is open.
- Tool installs (by seats, seat-local, no pacman): `rfc3986` 2.0.0 and `html5lib` 1.1 into
  seat-local uv venvs (`w1/ExecProbeUrljoin.md`, `w1/ExecProbeUnescape.md`). The L1 installed nothing.
- Open L0 questions: none.
- Carried to round 37: attribute-embedded `<script` truncation, FIFO and huge-manifest handling,
  check-then-open race in `body_path`, recorder duplicate-id and write-scope items, the 18
  undecided contract points, criteria-check false passes.
