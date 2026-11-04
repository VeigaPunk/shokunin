# kake — round 81 report (hyaku run 15, attempt 1)

Lane: kake (web properties & publishing) · repo `kake-shokunin` · base `2e11925500dd5a739376c9108c94616243af0cd4`
· lane tip at filing `ddd38022f888e4199e198195be173797ff416381` (pushed; `ls-remote` agrees) · date 2026-11-04.

## Work performed

The round declares **two claims**, each on a distinct axis:

- **C1 — calibration** (lowest non-retired axis, score 2): the six defects the non-author round-80
  closure routed (`corpus/lessons/round-80-verifier-spotcheck.md` §6, R80-1 … R80-6) each evaluate
  closed from bytes at a named revision. Frozen predicate `met <=> open == 0`.
- **C2 — operability** (score 10, held): a fresh GET-only capture of three declared `ds4cc.com`
  surfaces feeds the offline header audit, and the whole chain — receipt digests, byte counts,
  integer status, instant fetch-time floor, URL identity, declared-surface equality and the audit's
  own output — re-derives from committed bytes at a pinned revision. Capability acquisition.

Work items, each with its evidence pointer:

- **Froze the contract before any seat ran** — `.ufo/waves/round-81/contract.md`, both counters, the
  junk-tree builder and spec, the C2 expectations file, base/junk/tampered controls and
  `scripts/wave_seat_record.py` at `a77b8a19c2b65a07dfbe40aaf7ec86aaeee2f9cb`.
- **C1 counter** `c81_defect_queue.py` with a per-item byte condition, `--revision` mode, a 15-case
  `--selftest` (one green plus at least one mutant per item) and two controls
  (`controls/base-c81-defect-queue.txt` `open=6 met=false`, `controls/ctl-c81-junk-queue.txt`
  `open=6 met=false`, `controls/c81-selftest-c1.txt` `15/15 passed`).
- **C2 counter** `c81_capture_audit.py`, offline at measurement time, with a 22-case `--selftest`, a
  base control (`declared=0 surfaces=0 met=false`) and a tampered control built from the real capture
  (`controls/ctl-c81-tampered-capture.txt`: one body byte flipped → digest mismatch, `met=false`).
- **Three amendments, each written before the after-state it governs** — amendment 1 (`0a27045e`)
  fixed the C1 settled population and the S454 anchor (§15.5.4 is 403 Forbidden; the row cites
  §15.5.5 + §15.5.11); amendment 2 (`eccd0f9c`) made C2 measure the frozen expectations file, added
  `--revision`, byte-exact audit equality and URL identity; amendment 3 (`a704ffa6`) replaced the
  lexical fetch-time compare with an RFC 3339 instant compare after a positive UTC offset let a
  pre-round timestamp through. Predicates, item conditions and kill rules never moved.
- **C1 corrections landed by append in `corpus/lessons/round-81.md`** — R80-1 names
  `corpus/SOURCES.md:200` (re-derived by the counter, so a moved row re-opens the item), R80-2 carries
  `constants_failed=4/4`, `47/48` and `const_echo 11/12` re-summed from the round-80 receipt, R80-3
  carries `rfc9110.txt rows=4` / `rfc9110.html rows=3` with the base count stated.
- **R80-5 re-runnability** — `junk_tree_build.py` + `junk-tree.json` rebuild round-80's junk tree
  deterministically (two runs, identical digests) and round-80's own counter over it reads
  `open=5 closed=1 met=false`, exit 1 (`controls/after-r80-5-junk-rerun.txt`).
- **R80-6 seat record** — `scripts/wave_seat_record.py` re-derives `seat-failures.json` canonically
  from the wave results and spec; 15 seats, one empty (`ReviewRegression`), and the record names the
  results schema's silence about an error text instead of inventing one.
- **R80-4 wave accounting** — `make_accounting.py` → `w1-accounting.json`:
  requested `6/15 = 40.0 %`, settled `5/14 = 35.7 %` over {reviewer, critic, mutation-tester, labrat};
  sentinel is not an attack role (round-80 closure R80-4), matching the run-71/72 open L0 framing.
- **C2 live half** — one capture (`w1/ExecCapture/capture-run.txt`), three surfaces, one GET each,
  no cookies, no credentials: `ds4cc.com/` 200, 78,897 B; `/robots.txt` 200, 62 B (`Allow: /` +
  sitemap pointer); `/sitemap.xml` 200, 7,810 B, 100 `<loc>` entries — all at
  `2026-11-04T12:05:06Z`, bodies and receipts committed under `.ufo/waves/round-81/capture/`.
- **Offline audit** — `header_audit.py` over the mechanical manifest prints
  `checks=3 findings=4` (`hsts_present` missing on all three, `csp_present` missing on the primary),
  committed byte-exactly at `controls/after-c2-audit.txt`.
- **Sources** — S454 admitted (RFC 9110 §15.5.5/§15.5.11, tier A) with a raw-substring Gate quote and
  three collapsed-only located spans; S433 re-opened (bytes identical to the round-61 retained copy);
  `recheck`/`used-by` changes logged old→new.
- **Corpus maintenance by append** — absent-resource section in
  `corpus/knowledge/response-header-expectations.md` (S454), an append-only locator correction
  (§5.2 → §5.3) found by the sources seat, a `[r81-observation]` in
  `corpus/knowledge/publish-queue.md` recording that the captured instant serves `/robots.txt` and
  `/sitemap.xml` with 200 (the "still 404" lines stay as filed), and new rows in `corpus/README.md`,
  `PROVINCE.md` and `corpus/QUALITY.md`.
- **Wave** — one v1 wave, 15 seats (band 8–16), no residual call: scout 2, executor 4, scribe 2,
  reviewer 4, critic 1, mutation-tester 1, connector 1. Requested attack share 6/15 = 40.0 %, settled
  5/14 = 35.7 % by the frozen rule (a results row with non-empty output). **Two seats died and were not
  replaced:** `ReviewRegression` (reviewer) returned empty output and wrote no report, and `MutC`
  (mutation-tester) died on a provider 429 after emitting a 3,771-byte progress log — a transcript, not
  a deliverable, so the substantive attack share is **4/13 = 30.8 %** (three reviewers plus the
  critic). Both readings clear the 0.25 floor; the frozen record is left as the instrument computed it
  and the disclosure is in `corpus/lessons/round-81.md` §Dead seat. The L1 held the planner seat (the
  validator refuses `planner` as a swarm role); the bounded planning data-walk rode `ScoutRecon`.
  Round total: 15 seats, 13 reports (12 seat reports plus the renamed do-nothing reviewer's two-name
  pair), 2 dead.
- **Misroot sweep** — `git -C /home/vgpnk/Projects/shokunin status --porcelain` shows no kake/round-81
  file at the fleet root; the only untracked entries are orchestrator scratch (`.scratch/`) and other
  lanes' reports. Nothing to relocate.

## Landed changes

| Change | LOG entry | Commit |
|---|---|---|
| Frozen contract, both counters, junk builder/spec, expectations, base/junk controls, seat recorder | Round 81 §Frozen contract | `a77b8a19c2b65a07dfbe40aaf7ec86aaeee2f9cb` |
| Amendment 1: C1 settled population; S454 anchor corrected (§15.5.4 → §15.5.5/§15.5.11) | §Three amendments | `0a27045e4b1b18ae521c9be508429262fdf993ca` |
| Disclosure of the amendment-1 selftest receipt rewrite | §Three amendments | `bec3ecf7a067f2ec403888b16294aa6ce490cfd7` |
| Amendment 2: C2 measures the declared expectations, `--revision`, byte equality, URL identity | §Three amendments | `eccd0f9cb0beae2d9f029b1ec9d20d04583ecb4d` |
| Disclosure of the two amendment-2 receipt rewrites | §Three amendments | `e93d26b78bae28830a6423c775186b9bdfa755f0` |
| Amendment 3: RFC 3339 instant comparison for the fetch-time floor | §Three amendments | `a704ffa61708100dcd15856818ded70484d88f44` |
| Disclosure of the amendment-3 receipt rewrite | §Three amendments | `5ae1f32b39722310215779eabcc548c4d1ae41e4` |
| Corrections, S454 row, C2 capture chain, wave evidence | §C1 landed, §C2 landed, §Frontier | `395f123cd7ac7251e07890540b4f2e9a11353c84` |
| C2 carrier receipt at `395f123c` | §C2 landed | `dc8e5b082c54bcdd3552af4b446f77920f9b62e5` |
| C1 carrier receipt at `e84c354e`, wave results, accounting, seat record, settlement lesson | §C1 landed, §Wave `w1` | `e84c354ecf43bac6dce46377ea22cb425158a36f` → `31f502cb0cbc6e738535c69eedad49577cf17be5` |
| SCORECARD round-81 block, LOG round-81 entry, census after | §C1 landed, §C2 landed, §Frontier | `498a0969499f70830b7c992eb36ea364672f1a1b` |
| Final carrier receipts for both claims | §C1 landed, §C2 landed | `2b46f5c4db418c9a79e1990940da1a5029ff7e5b` |
| Dead-seat disclosure (`MutC` 429 after a progress log; substantive attack share 4/13 = 30.8 %) | §Mined mistakes, §Dead seat | `ddd38022f888e4199e198195be173797ff416381` |

Gateway suite (C1) untouched; the standing round-79 receipt-disclosure ledger is green at the tip:
`C1v2 revision=5ae1f32b… events=40 undisclosed=0 phantom=0 malformed=0 wrong_kind=0 unpointed=0
symlinks=0 round_rewritten=0 met=true`, exit 0 — the three amendments' re-cut receipts are disclosed
in `.ufo/waves/round-58/receipt-rewrites.json`.

## Before → after measurements

| Claim | Counting command | Before | After | Measured commit |
|---|---|---|---|---|
| C1 calibration: the round-80 routed-defect queue closes (R80-4's settled share reads 5/14 = 35.7 % by the frozen non-empty rule and 4/13 = 30.8 % on deliverables only; both ≥ 0.25) | `python3 -B .ufo/waves/round-81/c81_defect_queue.py --root . --revision <rev>` | `C1v1 revision=2e11925500dd5a739376c9108c94616243af0cd4 items=6 open=6 closed=0 met=false`, exit 1 (`controls/base-c81-defect-queue.txt`) | `C1v1 revision=2b46f5c4db418c9a79e1990940da1a5029ff7e5b items=6 open=0 closed=6 met=true`, exit 0 (`controls/after-c1-final.txt`); first measured at `e84c354e` (`controls/after-c1.txt`) | `2b46f5c4…` (final), `e84c354e…` (first carrier) |
| C2 operability: fresh capture → offline audit, verdict re-derives from committed bytes | `python3 -B .ufo/waves/round-81/c81_capture_audit.py --root . --revision <rev>` | `capture: no manifest at the measured revision`; `C2v1 revision=2e119255… declared=0 surfaces=0 failures=1 audit_rc=- met=false`, exit 1 (`controls/base-c81-capture-audit.txt`) | `C2v1 revision=2b46f5c4… declared=3 surfaces=3 failures=0 audit_rc=1 met=true`, exit 0 (`controls/after-c2-final.txt`); first measured at `395f123c` (`controls/after-c2-carrier.txt`) | `2b46f5c4…` (final), `395f123c…` (capture carrier) |

Controls actually exercised, not merely named: C1 junk control `open=6 closed=0 met=false`, exit 1;
C2 tampered control (real capture, byte 0 of the primary body flipped `0x3c` → `0x3d`)
`body sha256 d1220935… != receipt f2c5d2b3…`, `met=false`, exit 1; base controls for both claims read
`met=false` at the base revision.

## Sources & frontier

`SOURCES.md` rows **191 → 192**; counting command
`/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kake`
→ exit 0 before and after (`controls/census-before.txt`, `controls/census-after.txt`), `W04`
duplicate-URL warnings 20 → 21 (`S454` is a fourth scope on RFC 9110's `.txt` URL).

- **Rows added by tier** — one tier-A row: **S454** (RFC 9110 §15.5.5 *404 Not Found* and §15.5.11
  *410 Gone*), `status=mined`, `opened 2026-11-04`, `recheck 365d`, `used-by
  corpus/knowledge/response-header-expectations.md, corpus/lessons/round-81.md`; inserted directly
  after S453 so no earlier registry line moved. No tier-B/C row added.
- **Rows touched old → new** — **S433**: `recheck 180d → 2027-05-03` (the same cadence re-anchored to
  this round's access date) and `used-by corpus/knowledge/response-header-expectations.md →
  corpus/knowledge/response-header-expectations.md, corpus/lessons/round-81.md`. No other row's
  `status`, `recheck` or `used-by` changed.
- **Gate** — one admit (S454, raw-substring quote at `:7593`, 9 words, plus three collapsed-only spans
  with both digests), one reject (§15.5.4 as an absent-resource anchor — it is 403 Forbidden), the
  `merge/kake` package re-refused (8 id collisions unchanged, 27 staged URLs already held), and one
  re-open (S433, bytes identical to the round-61 retained copy).
- **Frontier rows advanced** — the capture-once/audit-offline chain moves into Core as an instrument
  (`corpus/README.md` `## Coverage — round 81`, `PROVINCE.md` §Round 81); absent-resource status
  semantics enters as the boundary of any audit verdict (S454). Remaining on the frontier: an
  occurrence oracle (proving a capture came from the network rather than from bytes) and per-bot
  effective resolution.
- **Assimilation: none.** `/home/vgpnk/Projects/shokuknow/merge/kake` still collides on 8 ids
  (S312, S329, S367, S372, S373, S374, S390, S409); nothing in the round's scope made adoption safer.
- **considerthese** — one proposal mined into practice: read the lane's own instruments' committed
  receipts and report only a change or a red (`considerthese/2026-10-26.md` §Part 2, proposal 1).
  This round's C1 items R80-2/R80-5 are exactly that move — they re-derive from committed receipts
  instead of restating a report sentence.
- **Mistake mined** — `corpus/lessons/round-81.md` §Mistakes carries five rows: a selftest that cannot
  run is indistinguishable from a property that cannot pass; the instrument's population is not the
  predicate's population; a locator that names the section above its quote; an item premise inherited
  from a closure instead of re-derived; a dispatch that outlives its instrument. Each names the
  captured-by rule and shows the fix able to fail.

## Trend verdicts

- **expansion — unchanged (honest bounded move).** `corpus/knowledge/*.md` stays at 67 files: the round
  added a *section* to an existing entry (absent-resource status semantics, S454) and one mined row,
  but no new admitted entry file, which is what LEARNING.md's expansion observable counts. One
  coverage-map row and a Core instrument entered, and the capability table gained a row.
- **quality — improved.** Two weaker instruments are superseded by stronger ones with their frozen
  case sets unchanged (C1's settled population now equals the contract's sentence; C2 compares
  instants, binds the manifest to the frozen declaration, and compares the audit bytes); one stale
  standing claim is superseded by observation (`publish-queue.md`'s "still 404" lines vs the captured
  200s, appended as an observation with digests); one locator drift is corrected append-only (§5.2 →
  §5.3); five receipt rewrites are disclosed and the ledger gate is green (`events=40 undisclosed=0
  met=true`); no admitted entry was found false and left unmarked.
- **discernment — improved.** The previous round's outside spot-check routed six defects and all six
  are now decided from bytes by a committed counter (`open=6 → 0` with base and junk controls); this
  round's own attack seats found four defects in the round's instruments and terms *before* the states
  they governed (settled population, manifest self-assertion, lexical time compare, wrong RFC section
  anchors), each fixed by a dated amendment with the predicate unchanged. The honest counterweight is
  recorded, not hidden: C1's six items are record-closures and a records-only tree reaches `open=0`
  (`w1/ReviewC1.md` F2), and a well-formed fabricated capture passes C2 (`w1/ReviewC2.md` F1) — the
  non-author closure is what can catch either.

## SHONEN

- [~] **SKILL.md contains real decision tables, error patterns, checklists, cited sources** —
  `corpus/knowledge/shonen-ledger.json` row `box 1` (`status=evidenced`); not re-measured this round;
  this round added no `SKILL.md` row (the new instrument lives under `.ufo/waves/round-81/`, outside
  the gate-registry population), so the box's evidence is the round-77/78 ledger row, author-side.
- [ ] **At least one end-to-end domain task executed and logged in LOG.md** — this round *did*
  execute one (live capture → offline audit → four findings on `ds4cc.com`, logged at LOG.md §Round 81
  "C2 landed") but the ledger row's gap (one historical LOG-named receipt absent) is unchanged, so the
  lane does not flip the box; promotion stays operator-owned.
- [~] **Instructions executable by an agent without oral context** — ledger row `box 3`
  (`status=evidenced`, frozen script-path scope); every command in this report and in the lesson is
  absolute-path, `python3 -B`, and re-runnable; author-side.
- [~] **No cross-domain bleed (PROVINCE.md still accurate)** — re-measured this round: 67
  `corpus/knowledge/*.md` files, 0 citing a sibling lane repository path
  (`grep -lE '(kagi|tabi|chousa|kumitate|kotoba|kama|mori|souji|kaidoku|kasegi|kengaku|tameshi|tsukuroi|mado|revenger|audio|game-dev|lore)-shokunin/' corpus/knowledge/*.md | wc -l` → `0`); the
  S454 row's scope is narrowed against S088 in-lane, not absorbed from a sibling.

**Stale-lane** — none: this lane runs a respawn-per-round driver and no other mission of kake is open.

**Tooling** — no tool installed or upgraded this round; no pacman transaction (the host-wide pause was
respected).
