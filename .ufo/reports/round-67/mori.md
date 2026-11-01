# mori round 67 — the second vendor churn grammar (`asset-churn`) + the receipt-driven standing step (`--from-sweep`)

lane: mori-shokunin · branch master · entering `8470a025f94f7449e881c3d8a8c997ed89aa7a9a` (r66 verifier spotcheck tip) · landed `eed7272fc17d8beea75a275b13d03542ae275446` (helper-printed, pushed origin, ahead=0)

## Work performed

FRESH-START duty: the §7 rejections r59–r61 re-read and re-spot-checked with
own receipts (not cited from r66) — frozen r61 counter re-derived at the r61
data tip → `C2=unmet` rc 1 (same verdict as all prior re-derivations); r59/r60
cited evidence `git cat-file -e` PRESENT and ancestral
(`fleet/mori-shokunin/.ufo/waves/round-67/evidence/freshstart-spotchecks-r67.txt`).
Ruled out, and why: (1) the r59/r60 entry-claims instruments (met-flip
counterexamples stand on frozen bytes); (2) scalar score moves (no closure
states a new number); (3) old-Linux-host live surfaces (absent here); (4)
editing the frozen sweep or the r65 adjudicator (SKILL:905 tally pin + r65/r66
receipts bind those bytes — the r67 work extends only the lane-owned r66
re-check, which pins no SKILL tally); (5) a third grammar for the
instrument-UA bot-manager chrome (per-response serving variance, not a build
artifact); (6) re-declaring the admitted r64–r66 work.

- **C1 (depth): the second vendor churn grammar.** The r66 closure routed
  note 1 and the lane's own planned item: the stamp grammar was
  docs.python.org-scoped and S241 (learn.microsoft.com asset-build-id churn)
  stayed honest `content-drift` at the byte layer. Taught `asset-churn`
  (class `learn-microsoft-asset-build-id`, named on the output header beside
  `stamp-class=`), grounded in the vendor's own redeploy signature recorded
  at `.ufo/waves/round-65/evidence/disposition-diffs-r65.txt` (S241,
  changed_opcodes=2, both asset-reference lines) and in S578 (web.dev
  versioned URLs, opened this round); decided on the pinning-UA body when the
  instrument UA is served a different variant. Demonstrated live on S241 —
  evidence `.ufo/waves/round-67/evidence/s241-assetchurn-live-r67.txt`.
- **C2 (operability): `--from-sweep <receipt>`.** The r66 closure routed
  note 2: the standing step took a hand-copied `--only` id list. The mode
  reads the sweep receipt's own finding list (rows only — the `drifted=N`
  summary token is never counted as a row, the r65 M1 lesson made
  procedural), enforces rows-vs-summary agreement (rc 2 on disagreement),
  refuses non-sweep receipts (rc 2), errors on findings absent from the
  registry, and is mutually exclusive with `--only`. Demonstrated on the
  committed r66 sweep receipt — evidence
  `.ufo/waves/round-67/evidence/fromsweep-standing-r67.txt`.
- Honest run history receipted: the first edit execution died on a dropped
  `emit=` definition (NameError rc 1, fixed); the first green version still
  classified live S241 `content-drift` (10:21:36Z) because the second-UA arm
  never attempted the churn grammars — the live run caught the design gap the
  selftest's fixtures missed; fixed, receipted pre/post side by side, and the
  S914 fixture now replicates the S241 shape
  (`.ufo/waves/round-67/evidence/recheck-selftest-r67.txt` header + runs).
- Do-nothing controls: `asset-churn` = 0 and `from-sweep` = 0 in the entering
  tool bytes (rc 1 each), QUALITY `^159\.` = 0, S578 = 0 —
  `.ufo/waves/round-67/evidence/controls-r67.txt`.
- Carry-in 3 routed around: the r65 L0 (SKILL:905 `python3` naming) stays
  open for the operator; no frozen byte edited — the sweep, the r65
  adjudicator and SKILL.md are absent from the `8470a025..eed7272f` diff and
  the `PASS (6 cases)` pin counts 1 at the tip.

## Landed changes

One commit, `eed7272fc17d8beea75a275b13d03542ae275446` (helper-printed;
`8470a025..eed7272f` = 16 files, +6083/−44; `merge-base --is-ancestor` ok;
`refs/heads/master` = `ls-remote origin refs/heads/master` = `eed7272f`):

- `tools/mori-drift-recheck.py` — the `asset-churn` class + grammar
  (`learn-microsoft-asset-build-id`), pinning-UA-body resolution, `--from-sweep`
  mode with the integrity checks, selftest 7 → 10 cases (LOG.md Round67).
- `corpus/QUALITY.md` — criterion 159 (vendor-scoped churn grammars, named on
  the header) + append-only erratum on 158's not-covered clause.
- `corpus/SOURCES.md` + `corpus/evidence/sources-r67/S578.html` — S578 opened
  and pinned byte-identical (sha `5c02b661…`).
- `SCORECARD.md` Round67 section (claims table, capability-row r67 extension,
  rule-outs, controls), `LOG.md` Round67 entry, `SHONEN.md` boxes 2–3
  refreshed to the r67 evidence and tally.
- `corpus/lessons/round-67.md` — three mistakes mined (dropped-definition
  edit; green-selftest-over-design-gap; the r66 M4 truncation class recurring,
  now fixed by write-to-file-then-append instead of heredocs).
- `.ufo/waves/round-67/evidence/` — 8 receipts: census start/end,
  freshstart-spotchecks, controls, recheck-selftest (×3 runs),
  s241-assetchurn-live A/B, fromsweep-standing, selftests-battery.

## Before → after measurements

- **C1 (depth 5):** `git show 8470a025:tools/mori-drift-recheck.py | grep -c
  asset-churn` → `0` (rc 1, `controls-r67.txt`) → `git show eed7272f:tools/
  mori-drift-recheck.py | grep -c asset-churn` → `19` (rc 0). Selftest
  `python tools/mori-drift-recheck.py --selftest` → `MORI_DRIFT_RECHECK_SELFTEST:
  PASS (10 cases)` rc 0 ×3 at the final bytes (`recheck-selftest-r67.txt`).
  Live A/B: r66 standing receipt `recheck-standing-r66.txt:20` =
  `S241 content-drift as-of=2026-11-01T08:40:58Z` → post-fix live run =
  `S241 asset-churn as-of=2026-11-01T10:30:25Z` (reproduced 10:36:29Z), the
  pinning-UA delta being exactly the two asset-id lines (`0.4.03574.8308-9505b1c8`
  → `0.4.03589.8339-b0a05127`; 2 of 1499 lines; `grep -c "^[<>]"` = 4)
  (`s241-assetchurn-live-r67.txt`). QUALITY: `grep -c "^159\." corpus/QUALITY.md`
  0 → 1. **Self-verdict: verified met** (closure to re-derive).
- **C2 (operability 7):** `git show 8470a025:tools/mori-drift-recheck.py |
  grep -c from-sweep` → `0` (rc 1) → committed bytes → `17` (rc 0).
  Standing run `python tools/mori-drift-recheck.py --root . --from-sweep
  .ufo/waves/round-66/evidence/sweep-live-r66.txt` → header `findings=17`,
  `grep -cE "^S[0-9]{3} " .ufo/waves/round-67/evidence/fromsweep-standing-r67.txt`
  → `17` rows adjudicated rc 0 — 8 time-churn, 1 asset-churn (S241, the
  single intended flip), 5 receipt-open, 2 ua-serving, 1 gate, 0 content-drift
  — every r66 standing class reproduced except the disclosed flip, window
  10:38:29Z..10:38:33Z. No-harm: standing battery green — register 12/12,
  settlement 10/10, vote-bind 16/16, pin-check 125/125, adjudicate 5/5,
  recheck 10/10 (`selftests-battery-r67.txt`). **Self-verdict: verified met**
  (closure to re-derive).

No axis harmed: frozen instruments and SKILL.md byte-identical; census rc 0
both ends; standing selftests green.

## Sources & frontier

SOURCES rows 350 → 351, counted by `grep -c "^| S" corpus/SOURCES.md`
(census-start receipt states 350 at entering; committed tip counts 351).
S578 opened this round (tier-A vendor docs): duplicate sweeps before opening
`grep -c "web.dev"` = 0, `grep -c "http-cache"` = 0, `grep -c "cache.busting"`
= 0; fetched `curl -sS -m 60 -L`, pinned byte-identical
`corpus/evidence/sources-r67/S578.html` sha256 `5c02b661…`; quote
(`S578.html:4647`, 15 words): "Versioned URLs are a good practice because
they make it easier to invalidate cached responses."; heading `:4638`;
continuation `:4652`. No source rejections this round (the fresh-start
rule-outs are the round's reject-class decisions). Census (validator):
start receipt `.ufo/waves/round-67/evidence/census-start-r67.txt`
(2026-11-01, `mori ok`, 31 tolerated W04, `rc=0` line embedded) → end receipt
`.ufo/waves/round-67/evidence/census-end-r67.txt` (`mori ok`, 31 tolerated
W04, `rc=0`) — **exit 0 required at round end: met**. Mistake mining:
`corpus/lessons/round-67.md` `## Mistakes` — three mistakes, each with class,
evidence pointer, captured-by and fix; none found none.

## Trend verdicts

- **expansion: improved** — the capability row extends with a demonstrated
  r67 extension (grammar + mode; first-working stays 66), one tier-A source
  opened, pinned and mined (350 → 351), the instrument's repertoire grows
  without claiming new surfaces (PROVINCE unchanged and accurate).
- **quality: improved** — C1 and C2 verified with able-to-fail evidence (the
  pre-fix live run receipted beside the post-fix run; the from-sweep
  integrity checks can fail rc 2 and do in the selftest); QUALITY 159 + the
  append-only erratum keep the recorded facts aligned with the bytes; the
  standing battery is green, so no operational axis was traded for the
  extension.
- **discernment: improved** — three mistakes mined with captured-by and fix
  (including this round's honest disclosure that the first green selftest
  masked a design gap the live surface caught, and that the r66 truncation
  class recurred and was structurally fixed); the third-grammar temptation
  (bot-manager chrome) rejected as serving variance; the considerthese
  pin-check proposal routed to the operator's open L0 line instead of being
  adopted against a tally-cited instrument; the r65/r62 L0 lines left open
  and routed around, never treated as answered.

Per-axis: depth improved (C1), operability improved (C2), freshness
unchanged (held; r66's standing convention holds — no freshness-axis claim
declared), coverage unchanged (6), calibration unchanged (5; three mistakes
mined), adjacency unchanged (6; no sibling surface touched — write scope
confirmed by the diff file list).

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists,
  cited sources — unchanged this round (`SKILL.md:1211`, `SKILL.md:1178`,
  QUALITY 148-151/154, now also QUALITY 158–159); resolvable by a non-author
  verifier from committed bytes.
- [~] At least one end-to-end domain task executed and logged in LOG.md —
  `LOG.md` Round67 (C1 the S241 asset-churn live A/B; C2 the from-sweep
  standing run, 17/17) with `.ufo/waves/round-67/evidence/` receipts; box
  text refreshed at `eed7272f`.
- [~] Instructions executable by an agent without oral context — register
  12/12, settlement 10/10, vote-bind 16/16, pin-check 125/125, adjudicate
  5/5, recheck 10/10 (`.ufo/waves/round-67/evidence/selftests-battery-r67.txt`,
  loopback-transport condition carried per the standing r65 L0 disclosure);
  interpreter is `python` here (`python3` is a non-functional Store stub,
  rc 49 — the SKILL:905 naming line stays open for the operator).
- [~] No cross-domain bleed (PROVINCE.md still accurate) — no PROVINCE edit
  needed (it names no drift-tool modes); the round touched only lane files
  plus vendor docs within the lane's drift-instrument domain (S578, S241
  grammar); the r65 disposition writes and sibling boundaries stand.

## Assimilation

considerthese re-mined (2026-10-19…2026-10-26, all eight files; no newer file
exists — checked this round): the 2026-10-26 suggestion 1 (split pin-check
mismatches environmental vs stale) is the one still-unimplemented proposal;
not adopted — it changes a tally-cited instrument's reported behavior and
belongs behind the operator's open instrument-change ruling (mori |
round-65); suggestion 3 (re-execute what closures only evidence-verify) was
executed again in the fresh-start receipt. Assimilation: none — shokuknow
unreachable.
