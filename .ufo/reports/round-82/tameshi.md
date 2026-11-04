# tameshi — round 82 report (hyaku run 15, attempt 1)

Lane: `tameshi-shokunin` (verification-fixture craft; axes depth + calibration).
Round 82, 2026-11-04. Base `4dfc3181310088c2f32d51e87a4d82c047d05231`
(= `origin/master`, the round-81 closure and its non-author spot-check tip).
Declaration `4005a48ac73a66c794ff8fd528e6926633fe2af3`; landing
`b6658e7a90472d9c8c783067f2e5d16a98fc02c7`; records
`c8d40f5d4ed8b2cb3b418eaefa66471a22b2b906`; wave commit
`cfd59557ca856a737914141646ca8328fd7fe7ab`; final lane tip
`d9b02d653e11a9ab4c2234a5b92a4487fcc36f55` (= `origin/master`, `ahead=0`).
Round shape: **one v1 wave, 13 seats** (4 executor · 2 scout · 1 scribe ·
2 reviewer · 1 critic · 1 mutation-tester · 1 sentinel · 1 connector; attack
seats 5 = 38.5 %), policy `scripts/hyaku/ufo-wave-policy.json` (band 8–16),
validated by `ufo-swarm-wave.mjs` (`counts.spawn=13`, `maxLanes=16`,
dispatch `.ufo/waves/round-82/w1-dispatch.json`). The §3 planner seat stays
with the L1 (the validator rejects `planner`); its data walk rode the two
scout items. Saturation: scored axes depth 10, calibration 8, freshness 9;
round 82 enters no new capability row (it binds existing ones), so the
stagnation nudge does not fire and C1 works **calibration, the lowest scored
axis**.

## Work performed

The round declares three claims on distinct axes, frozen before any data in
`plans/round-82.plan.md` (declaration `4005a48a`):

- **R82-C1 — calibration (the lowest scored axis).** The routed-defect register
  is content-bound: the six-row register measures `manifest=bound` at a
  declared revision, a manifest whose bytes differ is refused before any row
  effect, and a path row reads the object's type and mode.
- **R82-C2 — freshness.** The three round-81 capabilities become live
  self-state rows and move into the live repertoire table: the population goes
  23 → 26 with every pin settled at the tip.
- **R82-C3 — coverage.** The newest instrument's own assertion text is pinned
  (`A14_selftest_text_pin`), so the test-text mutant that survives at the base
  bytes dies.

Work items, each with its evidence pointer:

- **The instrument is content-bound.** `tools/defect-bind.py` gains
  `--manifest-rev REV` (the manifest's bytes must equal `REV:<manifest path>`;
  a mismatch is `manifest-rev-mismatch`, exit 2, before any row effect), a
  single read shared by the binding and the parse, `GIT_NO_REPLACE_OBJECTS=1`
  on every git call, and a type/mode gate in `blob_bytes` so all five row kinds
  refuse a directory or symlink (arms A12/A13; `SELFTEST_ARMS = 14`) —
  `tools/defect-bind.py:132-250`, `:400-500`, `:760-900`; commits `4005a48a`,
  `ea618593`, `43fb2446`, `97f0186f`, `b37860b7`.
- **A five-defect battery lands with it.** `tools/defect-bind-mutants.spec`
  (the text mutant plus the four new code paths): `defects=5 killed=5
  survived=0`, `CONTROL: GREEN`, `MUTATE_RESTORE: OK`, FAIL sets singleton
  (`.ufo/evidence/round-82/final/c3-battery.txt`).
- **Two wave survivors become arms.** The mutation-tester's `r2` (a dropped
  `resolve_rev`) and `r3` (the deleted empty-flag guard) are pinned by
  extending A13/A8 without changing the arm count; the re-run reads
  `defects=2 killed=2` (`.ufo/evidence/round-82/final/c3-survivors.txt`).
- **Three capability rows become live self-state rows.**
  `tools/selfstate-freshness.json` rows `closure-defect-bind`,
  `standing-pin-audit`, `selftest-text-pin`, each pinned at the instrument's
  last commit: `SELFSTATE: rows=26 match=24 stale=2 unexpected=0` and
  `SELFSTATE_PINS: rows=26 settled=26 stale=0`
  (`.ufo/evidence/round-82/final/c2-landed.txt`, `c2-pins.txt`).
- **The repertoire table carries them.** The three round-81 capabilities moved
  into `SCORECARD.md`'s live `## Capabilities` table with refreshed evidence
  (`SCORECARD.md:269-271`); the round-81 snapshot table is preserved
  (round-81 closure §6 item 6).
- **The round-81 closure's record defects are closed and registered.** The
  manifest-binding receipt is reissued at its measured commit
  (`.ufo/evidence/round-82/manifest-binding.txt`: blob `c8372447…` →
  `d92d6bea…`, the D2 span extension, rows unchanged); the append-only
  correction paragraph sits at `SCORECARD.md:5203-5234`;
  `.ufo/evidence/round-82/tip-rederivation.txt` re-runs the round-81 counters at
  the tip; `tools/defect-bind-r82.json` measures the four items as
  `DEFECT_BIND: rows=4 closed=4 open=0 unexpected=0 manifest=bound`
  (`.ufo/evidence/round-82/final/c-r82-register.txt`).
- **Registry and SKILL figures refreshed and re-measured.**
  `tools/registry.json` (`defect-bind-selftest` 11/11 → 14/14, the sweep row
  now carries `--manifest-rev HEAD` and the bound line, `selfstate-*` 23 → 26,
  source cells re-pointed) and an append-only `SKILL.md` registry section
  (`SKILL.md:2258-2271`); `REGISTRY_BIND: rows=7 match=7 stale=0 absent=0
  error=0 unexpected=0`, exit 0.
- **Sources curated.** S294 (`gitattributes`) re-opened as the sourced row;
  S289, S305 and S310 re-opened with committed fetch comparisons; the drafted
  S311 refused by the census as a within-scope duplicate (W04) and never
  committed; `git-ls-files` and `git-check-attr` refused. Registry rows
  170 → 170; census exit 0 (`.ufo/evidence/round-82/final/census-after.txt`).
- **Records.** `LOG.md` round-82 entry; `corpus/lessons/round-82.md`
  (`## Gate`, `## Mistakes` 1–6, `## Wave findings`, `## Corrections of
  record`); `corpus/QUALITY.md` criteria 80–83;
  `corpus/knowledge/counter-population-binding.md`.

### The five instrument repairs (each re-pinned and re-measured)

The wave attacked the declaration and found five real holes; each was fixed in
its own commit and every after-state re-measured afterwards:

| # | Finding (seat) | Repair | Commit |
|---|---|---|---|
| 1 | two surviving mutants: a non-commit `--manifest-rev` and the empty-flag guard (M1) | A13 exercises unresolvable/non-commit revisions, A8 drives `main()`; arm count unchanged | `72832c94` |
| 2 | three of five row kinds were mode-blind; a symlink doc read the link target (R1) | the type/mode gate moved into `blob_bytes`, one gate for every kind | `ea618593` |
| 3 | the bound bytes and the parsed bytes were two reads (SN1, C1) | `read_manifest_bytes` — one read for binding and parse; the path check runs first | `43fb2446` |
| 4 | `git replace` substitutes the bytes the binding reads (E1) | `GIT_NO_REPLACE_OBJECTS=1` on every git call | `97f0186f` |
| 5 | an absolute-path symlinked manifest bound as its target (C1) | no `realpath`; the manifest must be a regular blob at the declared revision; A13 probes it | `b37860b7` |

## Landed changes

Every change ties to the round-82 `LOG.md` entry and the commit that carries
it:

| Change | LOG pointer | Commit |
|---|---|---|
| declaration: frozen plan, declared instrument, mutant spec, base controls | LOG.md round-82 (base/declaration paragraph) | `4005a48a` |
| landing: live rows, repertoire move, registry figures, correction paragraph | LOG.md round-82 (R82-C1/C2 paragraphs) | `b6658e7a` |
| records: after-state receipts, S294 re-open, lesson, criteria, register | LOG.md round-82 (Records/Sources paragraphs) | `c8d40f5d` |
| survivor pins (repair 1) | LOG.md round-82 (repairs table) + lesson `## Wave findings` 11 | `72832c94` |
| shared type/mode gate (repair 2) | lesson `## Wave findings` 8 | `ea618593` |
| single-read sweep (repair 3) | lesson `## Wave findings` 10, 12; `## Mistakes` 6 | `43fb2446` |
| replace-ref immunity (repair 4) | lesson `## Wave findings` 1 | `97f0186f` |
| regular-file manifest (repair 5) | lesson `## Wave findings` 10; `## Mistakes` 5 | `b37860b7` |
| wave artifacts: 13 seat reports, results, spec, dispatch, ready | LOG.md round-82 (wave shape) | `cfd59557` |
| records at the final instrument: re-pins, receipts, SCORECARD/SKILL/registry/SOURCES | LOG.md round-82 (no-harm/sources) | `b95b61c1`, `9403eadf`, `d9b02d65` |

## Before → after measurements

| Claim | Before (base bytes) | After (measured) | Counting command | Commit measured against |
|---|---|---|---|---|
| R82-C1 | `--manifest-rev` unrecognized (exit 2); the narrowed register reads `rows=5 closed=5 open=0 unexpected=0` exit 0; a directory row reads `state=closed detail=paths-present` (`.ufo/evidence/round-82/controls/`, plus the one-row control `c1-before-directory-only.txt`) | `DEFECT_BIND: rows=6 closed=6 open=0 unexpected=0 manifest=bound` exit 0; the narrowed clone refused `manifest-rev-mismatch` exit 2 with no row effect; the directory row `state=open detail=not-regular-file:.ufo/evidence/round-81=040000`; `DEFECT_BIND_SELFTEST: 14/14 pass`; the round register `rows=4 closed=4 open=0 unexpected=0 manifest=bound` (`.ufo/evidence/round-82/final/c1-*.txt`, `c-r82-register.txt`, `final-tip.txt`) | `python3 -I -X utf8 tools/defect-bind.py --repo . --manifest tools/defect-bind.json --manifest-rev HEAD` (+ the narrowed clone, + `--selftest`) | `b37860b7bf95fe195359057ff24db7a4622d505c`; re-derived at the tip in `.ufo/evidence/round-82/final/final-tip.txt` |
| R82-C2 | `SELFSTATE: rows=23 match=21 stale=2 unexpected=0` exit 0; `SELFSTATE_PINS: rows=23 settled=23 stale=0` exit 0; no row for any of the three capabilities (`.ufo/evidence/round-82/controls/c2-before.txt`) | `SELFSTATE: rows=26 match=24 stale=2 unexpected=0` exit 0 (the two `stale` rows are the declared red arms); `SELFSTATE_PINS: rows=26 settled=26 stale=0` exit 0; the three named rows print `measured=match` with identical doc/measured figures (`.ufo/evidence/round-82/final/c2-landed.txt`, `c2-pins.txt`, `final-tip.txt`) | `python3 -I -X utf8 tools/selfstate-freshness.py --repo . --manifest tools/selfstate-freshness.json` and the same `--pin-audit --pin-rev HEAD` | `b37860b7`; re-derived at the tip in `.ufo/evidence/round-82/final/final-tip.txt` |
| R82-C3 | base tool bytes + the single test-text edit: suite `11/11 pass`, `defects=1 killed=0 survived=1` — SURVIVED (`.ufo/evidence/round-82/controls/c3-before-mutant.txt`) | `defects=5 killed=5 survived=0 inconclusive=0 kill-rate=100 %`, `CONTROL: GREEN`, byte-identical restore; `db-a1-assertion-weakened` FAIL set = `A14_selftest_text_pin` only; the wave's two custom survivors re-run `defects=2 killed=2` (`.ufo/evidence/round-82/final/c3-battery.txt`, `c3-survivors.txt`) | `bash tools/mutate-and-run.sh --target tools/defect-bind.py --defects tools/defect-bind-mutants.spec --suite 'python3 -I -X utf8 "$MUTANT" --selftest' --label defect-bind-arms-r82` | `b37860b7` (`.ufo/evidence/round-82/final/c3-battery.txt`) |

**Honest limits, named rather than smoothed:** the binding proves bytes at a
*caller-named* revision, not that the revision is the intended one (a committed
narrowed register still binds at its own revision — the population's identity
stays with the declaration commit and the record); `rows=26` alone is reachable
with fabricated rows, so C2 rests on the three *named* rows' measured lines; a
deleted row is not caught by the two C2 commands (routed to round 83 with
`--manifest-rev` on the selfstate manifest); the A14 digest covers the
`selftest` function only (module-level edits and a two-edit recompute stay
outside; a vacuous comment inside is over-kill, measured); and the S294
conversion-attribute limit (`text`/`eol` on the manifest path) is declared, with
no such attribute on this lane's paths.

## Sources & frontier

- Counting command (round start and end):
  `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin tameshi`
  → before: exit **0**, verdict `tameshi	ok	…/corpus/SOURCES.md`
  (`.ufo/evidence/round-82/controls/census-before.txt`, run against a lane copy
  at the base revision); after: exit **0**, verdict `tameshi	ok	…`
  (`.ufo/evidence/round-82/final/census-after.txt`).
- Rows before → after: **170 → 170**. Rows added by tier: none (`A` 152,
  `B` 14, `C` 4 unchanged). Status: `mined 137`, `queued 22`, `rejected 11`.
  Malformed rows 0.
- Rows touched old → new: **S294** `used-by` gains
  `corpus/knowledge/counter-population-binding.md, corpus/lessons/round-82.md`;
  **S289**, **S305** and **S310** each gain `corpus/lessons/round-82.md`; all
  re-opened 2026-11-04 with committed fetch comparisons (S289 byte-identical;
  S305 byte-identical; S294 and S310 same-quote, different furniture).
- Refusals (kept as evidence of taste): the drafted **S311** (Git
  gitattributes) — a within-scope duplicate of S294, caught by the census
  `W04 S311 duplicate url …/gitattributes` **before** any append landed and
  never committed; **git-ls-files** — index listing, not tree objects at a
  revision; **git-check-attr** — the instrument never consults attributes.
- Frontier rows advanced: **none**. F11 (trusted-executor binding by committed
  blob identity) stays partly held; this round's binding is the *counter's
  population*, not the executor-source gate, and no frontier row moves without
  its next move measured.
- `Assimilation: none` — no `merge/tameshi/` theme was taken; `considerthese/`
  (2026-10-28) proposes source-census presentation changes that do not match
  the frozen claims.
- `git-ls-files`/`git-check-attr` fetch receipts:
  `.ufo/evidence/round-82/sources/ls-files.html`, `ls-files.headers`.

## Trend verdicts

- **expansion — unchanged.** No admitted knowledge entry on ground the coverage
  map did not hold, no frontier row's next move measured, no new capability row
  (the one new entry, `counter-population-binding.md`, deepens PROVINCE Core's
  own counter craft and cites held rows; reported under quality).
- **quality — improved.** A counter that could certify a narrowed population
  now refuses it, reads its population once, ignores replacement refs, and
  reads every row's object type and mode; the newest suite's own text is
  pinned with its mutant killed and two wave survivors pinned; the three
  capabilities are measured live (rows 23 → 26, pins 23 → 26 settled); every
  standing sweep exits 0 and no admitted entry was found stale.
- **discernment — improved.** The wave's own probes falsified the binding twice
  (a symlinked manifest, the double read) and the claim's guarantee was
  repaired in-round rather than argued away; the census refused the round's own
  duplicate draft; the mutation battery's FAIL sets were re-checked for
  over-kill; and the quality criteria 80–83 cite the mistakes. The closure's
  items 1, 2, 3 and 6 are closed with receipts and measured by
  `tools/defect-bind-r82.json`.

## SHONEN

One line per `SHONEN.md` box; no `[x]` is claimed this round (a `[x]` needs a
named non-author verifier, and the round-82 closure is not yet written).

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — round-82 registry section appended (`SKILL.md:2258-2271`), figures re-measured by `REGISTRY_BIND: rows=7 match=7`.
- [~] At least one end-to-end domain task executed and logged in LOG.md — round-82 LOG entry with measured after-states and receipts.
- [~] Instructions executable by an agent without oral context — `DEFECT_BIND_SELFTEST: 14/14 pass` and the plan's counting commands run from the repo; the input-keyed monitor is unchanged from round 21.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — every surface this round read is the lane's own tools/corpus; sibling lanes were read only by the connector seat (findings only, nothing absorbed).

## Round shape, seats and dead seats

One v1 wave `w1`, 13 seats, policy band 8–16, attack 5/13 = 38.5 %; spec
`.ufo/waves/round-82/w1-spec.json`, dispatch `w1-dispatch.json`, ready handoff
`w1.ready` (taken at 10:18), results handoff `w1-results.json` (`seats=13`,
`results=13`). **Dead seats: none** — every seat returned a report and a
terminal summary; no seat was replaced. No residual `task` call was made; the
round total is the wave's 13 seats. Seat role mix: 4 executor · 2 scout ·
1 scribe · 2 reviewer · 1 critic · 1 mutation-tester · 1 sentinel ·
1 connector.

**Stale-lane:** the driver is respawn-per-round (this process launched
2026-11-04T10:06:55-03:00 for round 82 only); no other mission of this lane is
open; the mission is `progressing` (round work landed inside this process).

**Tool installs:** none. **L0 questions:** none added this round.

**Inherited state:** none — `.ufo/waves/round-82/` did not exist at start (the
watchdog log shows no earlier attempt of this round) and the lane was clean at
the base revision. **Misroot sweep:** `git -C /home/vgpnk/Projects/shokunin
status --porcelain` shows only other lanes' reports, `.scratch/` state and the
known unattributed `after` file — nothing this round's seats wrote; no misroot.
