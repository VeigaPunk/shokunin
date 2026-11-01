# kotoba — round 84 report (attempt 1, Windows host)

Lane: kotoba-shokunin. Base `ae09f71fc8262b003d69f9e35d998e74d48b6c40`
(master), round head `462d240c02e31f90a87c88036e22b5011889b15b` (branch
`master`, pushed). FRESH-START continuity: the r79/r80/r81 rejected
closures were spot-checked in round 83; the ruled-out list is re-affirmed
and extended this round (lesson `corpus/lessons/round-84.md` § Ruled out;
report § Work performed, last bullet). Lesson: `corpus/lessons/round-84.md`.

## Work performed

Claims declared: **2** (both counted, causally separable, distinct axes).
Lowest-axis obligation: satisfied under the all-axes reading the r82/r83
non-author closures used — freshness 8 / adjacency 8.0 tie lowest; C2
targets freshness. The owned-axes two-readings L0 question stays open and
is routed around, not assumed.

- **Carry-in first (R83-V1, non-author spot-check defect 1) — the r83
  counter-base receipt regenerated; the filed capture stays as filed.**
  The committed `.ufo/waves/round-83/receipts/r83-counter-base.txt` reads
  `2 of 6` with `FAIL d2-anchor-consistency`, contradicting its own
  header ("must score exactly 3 of 6"), the r83 report/lesson, and the
  spot-check's re-run — a stale development-era capture, never
  regenerated when the predicate was finalized. Regenerated 2026-11-01
  from the frozen tip counter (blob
  `b299c265aec14d705b4eb3391a70af27234dcd53`, working-tree copy == HEAD
  blob at `ae09f71`, `git hash-object` verified) at the pinned base
  `4c95c456778baa4d61fc58a2642850c4a8b06b81`: `r82 routed defects closed
  3 of 6`, only the three D1 correction checks failing, exit 1 — receipt
  `.ufo/waves/round-84/receipts/r84-counter-base-regenerated.txt`
  (self-test at the same blob `0 failure(s) over 20 assertions`, exit 0).
  Header, bytes and claim now agree. Correction block appended to
  `corpus/lessons/round-83.md`; the filed receipt is not edited.
- **C1 — coverage (advisory, score held 8.5): the second host skills root
  governed.** The host presents a second skills root,
  `C:/Users/jpvei/.agents/skills` — the spec-tutorial `.agents/skills/`
  shape recorded as documentary evidence in round 74, live here with 15
  installed `*/SKILL.md` instruction surfaces, never enumerated by any
  committed artifact: `git grep -l 'jpvei/\.agents' ae09f71` prints
  nothing over the whole tree at the round base (before-receipt
  `.ufo/waves/round-84/receipts/before-c1-c2.txt`). The r82 census
  instrument runs against it unchanged — `host skill surfaces measured
  15: identical 0, drifted 0, lane-absent 15`, exit 0
  (`.ufo/waves/round-84/receipts/r84-agents-root-census.txt`) — and the
  PROVINCE § Core second-root row landed. Bounds: classification only, no
  installed copy edited, no instrument amendment (the capability
  generalized over roots by design, so this is a coverage move, not
  operability).
- **C2 — freshness (advisory, tied-lowest axis 8 under the all-axes
  reading): the round-72 A1 name-uniqueness rule re-verified against the
  live installed surfaces.** The A1 checklist rule ("`name` is unique
  among the skills likely installed alongside it") had never been
  measured on this host. Frontmatter `name:` extracted over both roots
  (24 installed surfaces): **2 duplicate-name pairs**, both inside the
  `.agents` root — `godspeed` and `ufo`, each a live directory plus a
  dated `.pre-adapt-backup-20260927` copy carrying the same `name:` value;
  cross-root collisions 0 (ledger
  `.ufo/waves/round-84/receipts/r84-name-collisions.txt`). Grounded in
  **S254**, opened this round: the harness documents the collision class
  (same-name precedence table; "`name` sets the command ... unless
  another command already uses that name"), making the pairs a grounded
  live violation of the lane's own rule. Bounds: the colliding surfaces
  are flagged read-only, never repaired from this lane; the A1 box text
  untouched (frozen tokens of `check_author_rules.py`); SKILL.md
  unchanged; no behavioral claim about which copy this host's loader
  favors (S254 documents Claude Code's rule; this host's loader is not
  measured here).
- **Frontier (2b):** SOURCES row S254 opened this round with the full
  Gate record (fetch receipt, located 19-word quote at line 207, companion
  sentence at line 439); round-start and round-end census both `kotoba ok`
  exit 0; one mistake mined (below). The lane file itself additionally
  validated directly (`--file`, exit 0) so the new row's parseability is
  proven without waiting for the orchestrator wrap-up sync.
- **Mistake mined (2b.3):** the stale-receipt class — a claim-cited
  receipt captured during development and committed without regeneration
  after the instrument's predicate was finalized (`r83-counter-base.txt`;
  R83-V1). Fix landed this round: the regenerated receipt, the r83-lesson
  correction block, and the going-forward rule (a claim-cited receipt is
  re-captured from the frozen instrument at the frozen rev whenever the
  predicate changed after the capture; the re-capture lands in the same
  round as the predicate freeze) — `corpus/lessons/round-84.md` ## Mistakes.
- **Ruled out (fresh-start bar):** the floors-gate Windows-degraded set
  (10 FAIL instruments at the r83 tip) — a fix would either touch the
  phantom-index L0 subject (line 177: `compare_harness_independent`
  missing / 0-vs-330) or sprawl across ten instruments in one round;
  named debt, unchanged. The tip-battery 6-of-6 lineage (r83 ruling
  stands). Repairing the 6 drifted installed copies or the 2 colliding
  backup dirs (read-only bound, r82). Substrate re-pin (omp absent on
  this host, r82). All with reasons in the lesson.
- **Dispatch/L0:** the ≥8-L2 floor — the batched subagent surface is not
  reachable from a headless round session (fleet `.ufo/l0-questions.md`
  line 249, open since r82); the phantom-index question (line 177) also
  stays open. Both routed around, never treated as answered. No wave was
  dispatched and none was padded.

## Landed changes

All in one plumbing-helper commit `462d240c02e31f90a87c88036e22b5011889b15b`
(push: `ls-remote origin refs/heads/master` == local HEAD == `462d240…`;
identity `kotoba-shokunin <kotoba@shokunin.local>`; verified
`git diff ae09f71..462d240 --stat`, 14 files, 1693 insertions, 2 deletions
— the two SCORECARD row lines rewritten by evidence-cell prepends; LOG.md
append-only held at +63/-0):

- R83-V1 carry-in: `.ufo/waves/round-84/receipts/r84-counter-base-regenerated.txt`
  (new), `corpus/lessons/round-83.md` (## Correction appended), LOG.md
  carry-in entry. The filed `r83-counter-base.txt` is absent from the
  diff — byte-untouched, as filed.
- C1 coverage: `.ufo/waves/round-84/receipts/r84-agents-root-census.txt`
  and `before-c1-c2.txt` (new), PROVINCE.md (one second-root § Core row
  appended), LOG.md C1 entry, SCORECARD.md coverage row evidence prepend
  + planned Round-84 block.
- C2 freshness: `.ufo/waves/round-84/receipts/r84-name-collisions.txt`
  and `code-claude-com-skills.fetch.md` (new), `corpus/SOURCES.md` (S254
  row appended, 179 → 180), LOG.md C2 + intake entries, SCORECARD.md
  freshness row evidence prepend.
- Round bookkeeping: `corpus/lessons/round-84.md` (new), census receipts
  `census-round-start.txt`, `census-round-end.txt`, `census-lane-file.txt`.
- SKILL.md: unchanged this round (no verifier added or amended; gate
  registry re-run at the new rev: 66 of 66, phantom 0).

## Before → after measurements

- **C1 (coverage):** before — `git grep -l 'jpvei/\.agents' ae09f71 | wc -l`
  → 0 (whole tree at the round base; PROVINCE named one host root);
  after — `python -B verifiers/check_host_skill_surfaces.py --skills-root
  C:/Users/jpvei/.agents/skills --fleet-root <fleet root>` → `host skill
  surfaces measured 15: identical 0, drifted 0, lane-absent 15`, exit 0,
  and `grep -c '^LANE-ABSENT'
  .ufo/waves/round-84/receipts/r84-agents-root-census.txt` → 15.
  Measured at commit `462d240` (receipt committed there).
- **C2 (freshness):** before — `git grep -c 'NAME-COLLISION' ae09f71` →
  no match (the class was never measured on this host); after — `for r
  in C:/Users/jpvei/.agents/skills C:/Users/jpvei/.zcode/skills; do for
  f in "$r"/*/SKILL.md; do n=$(sed -n '1,12{s/^name:[[:space:]]*//p}'
  "$f"); echo "$n"; done; done | sort | uniq -c | awk '$1>1' | wc -l` → 2
  (`2 godspeed`, `2 ufo` in the raw pipeline output), and `grep -c
  'NAME-COLLISION'
  .ufo/waves/round-84/receipts/r84-name-collisions.txt` → 2. Measured at
  commit `462d240`.
- **R83-V1 (carry-in, protocol work):** the stale receipt read `2 of 6`
  with `FAIL d2-anchor-consistency`; the regenerated receipt at the same
  pinned base from the same frozen blob reads `r82 routed defects closed
  3 of 6` + `FAIL d1-lesson-correction` / `FAIL d1-log-correction` /
  `FAIL d1-plan-correction`, exit 1; self-test `0 failure(s) over 20
  assertions`, exit 0. Header, bytes and claim agree. Measured at commit
  `462d240`.

## Sources & frontier

- SOURCES rows: 179 → 180. Counting command: `grep -cE '^ {0,3}\| S[0-9]{3}'
  corpus/SOURCES.md` → 179 before (`ae09f71`), 180 after (`462d240`).
  Row added: S254 (Claude Code Docs — Extend Claude with skills,
  same-name resolution; tier A, mined; fetch HTTP 200, 118879 B, sha256
  `d2a5d07c…`; located quote line 207, 19 words; known W04 duplicate-URL
  class shared with S053/S065, which hold other aspects of the page —
  disclosed in the row). Rows touched: none. Frontier rows advanced: 0.
- Census before→after: round start `kotoba ok`, exit 0, 179 rows,
  32 W04 warnings (`.ufo/waves/round-84/receipts/census-round-start.txt`);
  round end `kotoba ok`, exit 0, S254's W04 joins the known class
  (`.ufo/waves/round-84/receipts/census-round-end.txt`); lane-file
  validate `--file` → `ok`, exit 0
  (`.ufo/waves/round-84/receipts/census-lane-file.txt`).
- Mistake mining: one class mined with evidence pointer, captured-by and
  fix (see Work performed); lesson `corpus/lessons/round-84.md`.
- Sourced-claim rule (2b.4): C2 rests on S254, opened this round.

## Trend verdicts

- **expansion: improved** — a new real surface entered the governed set:
  the host's second skills root (15 installed instruction surfaces) went
  from zero committed references (whole tree at `ae09f71`) to a PROVINCE
  § Core row plus a committed enumeration receipt; SOURCES 179 → 180. No
  capability row (the r82 capability is unchanged), no knowledge/ file —
  the expansion is the governed-ground row, stated at exactly that size.
- **quality: improved** — freshness moved on its own rubric line ("each
  round LOG entry includes a re-verification result"): a drift class that
  had never been measured on this host (duplicate installed skill names)
  is now measured, dated, sha-pinned and grounded in a tier-A source
  opened this round; and the r83 receipt defect was closed executably
  (re-capture from the frozen instrument) with the correction recorded
  append-only. No trade: LOG append-only held (+63/-0), SKILL.md
  untouched (registry 66 of 66 at the new rev), census exit 0 both ends,
  no instrument predicate changed, floors untouched.
- **discernment: unchanged** — no exploratory claim declared; both claims
  are counted and bounded (read-only bounds named in every receipt); the
  floors-gate candidate was ruled out on evidence before any attempt
  (L0-routed subject named); the stale-receipt mistake was mined with a
  going-forward rule rather than papered over; the round sized C1 to a
  coverage move and explicitly refused the operability framing (no
  instrument amendment was made).

Per-axis verdicts: depth unchanged · consistency unchanged · coverage
improved · operability unchanged · freshness improved · calibration
unchanged · adjacency unchanged. No axis harmed.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists,
  cited sources — evidence: `SHONEN.md` box 1 pointers unchanged at
  `462d240` (SKILL.md untouched this round); current-state re-count:
  `awk '/^## Sources/{p=1;next} /^## /{p=0} p && /^- /' SKILL.md | wc -l`
  → 18, and `python -B verifiers/check_gate_registry.py --rev 462d240` →
  `gate registry rows conformant 66 of 66 lane verifiers; phantom 0`,
  exit 0.
- [~] At least one end-to-end domain task executed and logged in LOG.md —
  evidence: unchanged `SHONEN.md` box 2 record (LOG end-to-end entries
  with committed receipts); this round's LOG appends carry two new
  measured domain findings (C1, C2) with committed receipts at `462d240`.
- [~] Instructions executable by an agent without oral context —
  evidence: unchanged `SHONEN.md` box 3 record (the cold-run gap stands
  as recorded); this round's receipts are command-complete (each names
  its instrument, arguments and expected output), e.g.
  `r84-counter-base-regenerated.txt` reproduces from its own header.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — evidence:
  PROVINCE.md changed only by the round-84 second-root § Core row
  (kotoba-domain: installed skill instruction surfaces); `grep -n
  '^## Adjacent' PROVINCE.md` position unchanged, § Adjacent untouched;
  installed copies audited read-only, never edited; the 15 `.agents`
  surfaces are reported as lane-absent findings, not absorbed.

Assimilation: `considerthese/` inspected (newest digest 2026-10-26;
nothing new since the r83 check); both claims are grounded in this
round's own intake findings (the unenumerated second root; the S254
collision class); no proposal adopted. Assimilation: none — shokuknow
unreachable.
