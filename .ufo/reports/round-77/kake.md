# kake — round 77 report (hyaku run 15, attempt 1)

Lane `kake`, repo `/home/vgpnk/Projects/shokunin/kake-shokunin`, branch `master`. Base
`a2cc5f51002433e11cc3d2f70e650a6c60ad5e68` (lane tip at round open, 2026-11-03). Frozen contract
`.ufo/waves/round-77/contract.md` (`bc2e5fb9`), frozen before any seat ran; Amendments 1 and 2
(terms-only, recorded before any after-state) land at `893b0f33`. Measured carrier
`3db64e09550c9f8309f6c1077f9f7df6243cb446`; final lane tip `bb2f8edac2e1d0bc102545a0ffa56871410e21b0`.

## Work performed

The round declares **two claims on two distinct axes**: **C1** — calibration, score 2, the lane's lowest
non-retired axis — every `SHONEN.md` box classified from committed bytes at one named revision, with the
recorded observation re-derived rather than trusted; **C2** — operability, score 10 HOLD — a capability
acquisition: `scripts/sitemap_audit.py` decides the gzip container, the plain-text sitemap and RSS 2.0 /
Atom 1.0 feeds, the three families the round-39 tool refused. Both claims are causally separable: C1 rests
only on the ledger counter and `corpus/knowledge/shonen-ledger.json`, C2 only on the audit tool and the
frozen matrix. Scores stay HOLD (operability 10, freshness 10, calibration 2); no scalar move is claimed.

- **C1 instrument + ledger.** `.ufo/waves/round-77/c77_shonen_ledger.py` (selftest 26/26 from the committed
  blob) re-derives every `observed` value through five frozen kinds (`exists`, `count_at_least`,
  `regex_count`, `all_ids_resolve`, `no_match`), refuses a `command` kind outright, and counts a `holds` flag
  that contradicts its own derivation as a finding. `corpus/knowledge/shonen-ledger.json` carries one row per
  box; `SHONEN.md` carries `[~] [~] [ ] [~]` with a pointer line each. Evidence:
  `.ufo/waves/round-77/controls/after-c1-ledger.txt`, `base-c1-ledger.txt`.
- **C1 controls.** A scratch repo with four `[~]` markers and four fabricated `evidenced` rows stays red:
  `C1 revision=0104075b470f6c7b12f4a0749de40feab04908b6 boxes=4 evidenced=0 gap=0 unexamined=0 mismatches=4 met=false`
  (`.ufo/waves/round-77/controls/ctl-c1-fake-ledger.txt`); the base tree with no ledger prints
  `unexamined=4`.
- **C2 tool.** `scripts/sitemap_audit.py` gains the gzip container (magic `1f 8b` whatever the file name,
  the 52,428,800-byte limit applied to **decompressed** bytes, a truncated stream as check error
  `gzip_invalid`), the plain-text sitemap (`text_line_not_url`, `text_url_not_absolute`, `text_empty`,
  `text_too_many_entries`, BOM tolerated as a lane convention), RSS 2.0 (`<link>`, optional `<pubDate>`) and
  Atom 1.0 (`<link href>`, optional `<updated>`), and `format_unsupported` as a check error; the delivered
  selftest is `PASS 271/271` from the committed blob (235/235 at base). Evidence:
  `.ufo/waves/round-77/controls/after-c2-matrix.txt`.
- **C2 instrument.** `.ufo/waves/round-77/c77_sitemap_matrix.py` (selftest 14/14) runs any same-CLI tool over
  the 20 frozen cases and four constants, comparing finding-id sets, error codes and exits.
  `.ufo/waves/round-77/cases/` is generated deterministically (`build_cases.py`); `consts/round39_xml_only.py`
  is byte-identical to the base tool (`sha256 914ebdee…`), so the before-state is the tool's own red.
- **Round-76 routed defect D1 repaired by evidence.** `ExecRevisionReceipts` re-ran the round-76 hreflang
  matrix at a full hash on the landed digest: `cases=71 decided=69 correct=69 wrong=0 undecided=2 constants_failed=4/4 met=true`
  with `revision=a2cc5f51…` and `tool_sha256=0762452f…` equal to the blob at that revision
  (`.ufo/waves/round-77/controls/r77-hreflang-matrix.txt`), plus the 8-page real-input rerun on the landed
  tool (`controls/r77-hreflang-realrun.txt`). D2/D3 became `corpus/QUALITY.md` criteria; D4/D5/D6 became
  append-only correction lines in `corpus/lessons/round-77.md` §Corrections.
- **Recon that changed the round before data.** Ten contract ambiguities (a spliced S012 quote, the
  `too_large`/`sitemap_too_large` collision, the namespace question on RSS/Atom roots, the missing exit-2
  error name) were frozen in Amendment 1; the reviewer's attack on a *reference* counter found the
  executable-check hole and the base-mismatch arithmetic, frozen in Amendment 2; ReviewC2 found the matrix
  could not separate a name-gated gzip dispatch and g01's payload was renamed to a non-`.gz` name
  (`.ufo/waves/round-77/w1/ReviewC2.md` F1, applied). Evidence: `w1/ScoutSurface.md`, `w1/ReviewC1.md`,
  `w1/ReviewC2.md`, `w1/ConnectorC.md`, `w1/CriticC.md`.
- **Mutation breadth.** 20 mutants across the tool, the matrix counter and the ledger counter: 19 killed by
  named cases/controls, one survivor (S8e, `except Exception: sys.exit(0)`) reachable only through an
  output-channel fault after the emit path, which neither frozen detector closes — recorded, not tidied
  (`.ufo/waves/round-77/w1/MutC.md` §5 F1).
- **Security review.** SentinelC found one live code-execution class (a ledger row's `argv` executed
  verbatim, closed before the carrier) and five open read/denial/integrity classes (lexical manifest
  containment, FIFO denial, unbounded manifest read, `--revision` label forgery, `--tool-revision` option
  injection) — routed in the lesson, not claimed closed (`.ufo/waves/round-77/w1/SentinelC.md`).
- **Frontier step.** `corpus/knowledge/sitemap-formats.md` (new entry, 63 → 64 knowledge `.md` files) cites
  S012 (re-opened), S447 and S448; `corpus/SOURCES.md` 184 → 186 rows. Gate: three admits with located
  quotes and four rejects with flip conditions (`corpus/lessons/round-77.md`).
- **Wave.** One v1 wave `w1`, 14 seats — scout 2, executor 4, scribe 2, reviewer 2, critic 1,
  mutation-tester 1, connector 1, sentinel 1; attack share 4/14 = 28.6 %; the L1 held the canonical planner
  seat. All 14 settled with non-empty output, no dead seats (`.ufo/waves/round-77/w1-results.json`). No
  residual `task` call was needed: the round's verification items rode the same 14 seats.

## Landed changes

| Change | LOG entry | Commit |
|---|---|---|
| Frozen contract | `## Round 77` bullet *Frozen contract* | `bc2e5fb9` |
| Instruments, fixtures, ledger, amendments 1–2, wave spec/dispatch, entry, `QUALITY.md` criteria | *Wave*, *C1 landed*, *C2 landed*, *Frontier and sources* | `893b0f33` |
| Carrier: final ledger counter (selftest 26/26), amended ledger rows, sitemap tool (selftest 271/271), t05 fixture, SOURCES S012/S447/S448 | *C1 landed and measured*, *C2 landed and measured*, *Frontier and sources* | `3db64e09` |
| Measured claims, SCORECARD/LOG/lesson, receipts, wave seat evidence | *C1 landed and measured*, *C2 landed and measured*, *Mistakes mined*, *Routed (not claimed)* | `b5a0053c` |
| Source and carrier-supersession receipts; QUALITY defect-span wording; lesson span made whole | *Self-check at the tip* | `444ee748`, `b946acf9` |
| LOG self-check bullet | *Self-check at the tip* | `3d9239ed` |
| C1 cheap-fake control receipt | *C1 landed and measured* | `c7f1fba3` |
| Wave `w1-results.json` and `MutC.md` | *Wave* | `bcbe4694` |
| `ExecShonenLedger.md` re-citing the carrier | *C1 landed and measured* | `bb2f8eda` |

## Before → after measurements

**C1 — calibration (2 HOLD).** Counting command
`python3 -B .ufo/waves/round-77/c77_shonen_ledger.py --root . --revision <rev> [--work <scratch>]`.

- Base `a2cc5f51` (`controls/base-c1-ledger.txt`, exit 1):
  `C1 revision=a2cc5f51002433e11cc3d2f70e650a6c60ad5e68 boxes=4 evidenced=0 gap=0 unexamined=4 mismatches=0 met=false`
- Carrier `3db64e09` (`controls/after-c1-ledger.txt`, exit 0):
  `C1 revision=3db64e09550c9f8309f6c1077f9f7df6243cb446 boxes=4 evidenced=3 gap=1 unexamined=0 mismatches=0 met=true`

The gap is box 2 and is honest: `LOG.md` names 98 wave-receipt paths and one,
`.ufo/waves/round-47/verification/offline-sweep-r46-verdict-time.txt`, does not exist at the revision. No box
is ticked `[x]`: no named non-author verifier has signed one.

**C2 — operability (10 HOLD, capability).** Counting command
`python3 -B .ufo/waves/round-77/c77_sitemap_matrix.py --root . --tool-revision <rev> --cases .ufo/waves/round-77/cases --consts .ufo/waves/round-77/consts --work <scratch>`.

- Base `a2cc5f51` (`controls/base-c2-matrix-v2.txt`, exit 1):
  `C2 revision=a2cc5f51002433e11cc3d2f70e650a6c60ad5e68 cases=20 decided=20 correct=2 wrong=18 constants_failed=4/4 met=false`
- Carrier `3db64e09` (`controls/after-c2-matrix.txt`, exit 0):
  `C2 revision=3db64e09550c9f8309f6c1077f9f7df6243cb446 cases=20 decided=20 correct=20 wrong=0 constants_failed=4/4 met=true`

Constants at the carrier each fail at least one case: `always_clean` 12, `empty_findings_real_exits` 10,
`report_every_id` 20, `round39_xml_only` 18. The base's wrong set is the three new families plus `d01`; it
decides only `g04` (plain XML under a `.gz` name) and `s01` (index with `.txt`/`.rss`/`.atom` locs).

**Round-level self-check.** `python3 -B scripts/doc_quote_truth.py --root . --revision b946acf9 --base a2cc5f51 --rounds 76,77`
prints `C1v2 revision=b946acf9 rows=38 receipt_files=8269 spans=58 exempted=0 corrections=2 findings=0 met=true`,
exit 0: every claim-bearing span in this round's rows is a whole committed receipt line.

## Sources & frontier

Counting command, both runs on this host:
`/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kake`.

- **Before** (round open, base `a2cc5f51`): `kake ok corpus/SOURCES.md`, exit 0, 184 rows, 17 `W04`
  duplicate-URL warnings (16 inherited + the round-76 S445 row).
- **After** (round end, tip): `kake ok`, exit 0, 186 rows, 17 `W04` — the two new rows add no duplicate URL.

Rows added by tier: two, both **tier A spec** — S447 (RFC 1952, gzip container) and S448 (RFC 4287, Atom
1.0), each opened 2026-11-03 with HTTP 200, byte size and sha256 recorded in
`.ufo/waves/round-77/controls/sources-r77.txt`. Rows touched old→new:
S012 `used-by` `corpus/knowledge/crawl-scope-per-host.md` → `corpus/knowledge/crawl-scope-per-host.md, corpus/knowledge/sitemap-formats.md, corpus/lessons/round-77.md`;
status `mined`, `recheck 365d` and `opened 2026-10-19` unchanged. The lesson's `## Gate` carries the URL,
access date and a ≤25-word located quote for each admit and a flip condition for each of the four rejects.

Frontier rows advanced: `PROVINCE.md`'s sitemap line ("Still open: gzip, live fetch, text/RSS sitemaps, robots
cross-submission, and a key that kills those 15 breaks") loses **gzip** and **text/RSS sitemaps** to held
ground with a working instrument; live fetch, robots cross-submission and the 15 single-sentence breaks stay
open and are named in the entry's Limits.

`Assimilation: none` — the `merge/kake` package's staged ids collide on 8 rows with different content and 121
staged ids are free; the 0–3-space collision parser was re-run and receipted under
`.ufo/waves/round-77/assimilation/` (`reg-ids`, `staged-ids`, `collisions`), and no renumber map was produced.
`considerthese/2026-10-26.md`: proposals 2, 3, 5 are implemented (r58 receipt watch, r66 gate-status ledger,
report practice); proposal 1 is unimplemented and proposal 4 exists only as an aggregate count in the r66
counter — the contract's "all five implemented" sentence was wrong and is corrected in the lesson
(`w1/ConnectorC.md` §3).

## Trend verdicts

- **expansion — improved.** One admitted knowledge entry on ground the coverage map did not hold
  (`corpus/knowledge/sitemap-formats.md`, knowledge `.md` files 63 → 64) citing two new tier-A rows opened
  this round and one re-opened row. The ground was declared open at base, not already held:
  `corpus/README.md:161` lists "Sitemap gzip, text/RSS sitemaps, robots `Sitemap:` cross-submission" as
  frontier, and `git grep -c sitemap-formats a2cc5f51 -- corpus/README.md PROVINCE.md` exits 1 (no hit).
  The PROVINCE sitemap frontier advances by two families (gzip, text/RSS), leaving live fetch, robots
  cross-submission and the 15 breaks open.
- **quality — improved.** Both claims move from a red base to green on re-derivable counters over committed
  bytes; the tool's delivered selftest grows 235 → 271; the round's own quote-truth counter is green at
  `b946acf9`; 20 mutants with 19 killed and the one survivor named with its reachable path.
- **discernment — improved (author-side).** Gate records three admits and four rejects with flip conditions
  and no quote longer than 25 words; ten contract ambiguities and two counter holes were found by dispatched
  seats and frozen as terms-only amendments *before* any after-state; the connector measured sibling overlap
  (audio's `count_checklist.py` and kasegi's `shonen-form.py` are the nearest, and neither re-derives an
  observation) instead of asserting it. The non-author spot-check is owed to the closure.

## SHONEN

- `[~]` box 1 — `SKILL.md` contains real decision tables, error patterns, checklists, cited sources:
  `corpus/knowledge/shonen-ledger.json` row `box 1` (`status=evidenced`), checks `b1-ids` (77/77 `S###` ids
  resolve), `b1-tables`, `b1-registry`, `b1-checklist`; pointer line in `SHONEN.md`.
- `[ ]` box 2 — at least one end-to-end domain task executed and logged: row `box 2` is a `gap`; `LOG.md`
  names `.ufo/waves/round-47/verification/offline-sweep-r46-verdict-time.txt`, which does not exist at the
  revision; the flip is carried on the row.
- `[~]` box 3 — instructions executable without oral context: row `box 3` (`status=evidenced`) within
  amendment 1 A11's frozen scope (`scripts/*.py|sh`, counter paths, `python3 -B` targets, 0 missing); the
  three `node ~/Projects/webzites/...` spans and `scripts/kimi-surface.mjs` stay an open defect in the
  lesson and are outside that scope.
- `[~]` box 4 — no cross-domain bleed, `PROVINCE.md` still accurate: row `box 4` (`status=evidenced`), 0 of
  63 `corpus/knowledge/*.md` entries cite a sibling lane repository path, the `freshness-*.json` exclusion
  written in the row's params.

## Notes

- **Stale-lane:** none. The lane is a respawn-per-round driver lane; no other mission of this lane is open.
- **Tool installs/upgrades:** none. Pacman untouched; network reads were three public documentation GETs
  (each HTTP 200, retained under the wave dir) and no operator-owned property was fetched.
- **Misroot sweep:** `git -C /home/vgpnk/Projects/shokunin status --porcelain` shows only `.scratch/*`
  (orchestrator-owned) and a 24-byte file `after` dated 20:05, before this round opened; no seat of this
  round wrote into the fleet root.
- **Inherited state:** the lane was clean at round open (`jj-lane.sh state` → `ahead=0 behind=0`,
  `tracked=0 untracked=0`); nothing inherited to resolve.
- **Open L0:** `kake | round-69` (the `~/projects` drift the freshness sweep reports) stays open and was
  routed around, not treated as answered.
