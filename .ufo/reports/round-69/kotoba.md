# kotoba — round 69 (hyaku run 6, attempt 2)

Lane repo `/home/vgpnk/Projects/shokunin/kotoba-shokunin`, branch `master`.
Base `a5f7459f99bb27bf697e9438362e75ac5833eca8`; attempt-1 freeze commit `a238989a`;
landing commits `a02ba7e4` (content + repairs) and `54f4b6c` (baseline re-record, honest
receipts, counter hardening). Working tree clean at report time (2 untracked = this report's
sibling seat artifacts under `.ufo/waves/round-69/w1/`, committed in `a02ba7e`).

## Earlier attempt

Attempt 1 died 13m23s in on a provider error (`watchdog.log:1304` 06:46:36 launch,
`:1309` 06:59:59 `lane-dead-no-report kotoba round=69; … m_flash fallback chain reached
cursor/default`; attempt 2 launch `:1310` 07:00:36). Its uncommitted work was **inherited,
re-verified, and reused**: the frozen plan commit `a238989a` (three counters, base/junk
controls, freeze receipt) and the assimilation scratch under `.ufo/waves/round-69/assimilation/`.
Nothing else was carried. The plan's own line "the watchdog log shows no earlier attempt" was
stale at its committer time; the lesson discloses the inheritance instead.

## Claims (declared before any seat scored; three counters, base controls non-vacuous)

|claim|axis|instrument|at landing `54f4b6c`|at base `a5f7459`|
|---|---|---|---|---|
|C1 depth — a sourced map of what five clients document about two same-named skills|depth|`verifiers/check_skill_precedence.py`|`skill precedence backed 5 of 5` (exit 0)|`0 of 5`, entry missing (exit 1)|
|C2 consistency — the eight routed round-68 defects closed|consistency|`verifiers/check_r68_routed_repairs.py`|`r68 routed defects closed 8 of 8` (exit 0)|`0 of 8` (exit 1)|
|C3 coverage — the r67 authority and r68 trust-gate areas held in PROVINCE Core|coverage|`verifiers/check_province_core.py`|`province core rows 2 of 2` (exit 0)|`0 of 2` (exit 1)|

Self-tests at landing: C1 22 assertions, C2 25, C3 10, plus the repaired r67 counter 6 — all
0 failures. Base controls re-run at the pinned base in this session, not copied from the
freeze receipt.

## Gate

Theme assimilated from the read-only campaign package
`/home/vgpnk/Projects/shokuknow/merge/kotoba/` (nothing in it written, executed or committed).

**Admitted (5 source rows + 1 correction row + 1 knowledge entry).** Every source re-opened
this round with its own located quote (access date 2026-10-25), all tier A (official client docs):

- **S203 Roo Code** — "Project skills override global skills, mode-specific override generic" (8 words)
- **S204 Amp** — "Local skills mask repository skills with the same name." (9 words)
- **S205 Deep Code** — "only the highest-priority one is kept" (6 words)
- **S206 Junie** — "the project-level skill takes precedence and the user-level skill is ignored." (11 words)
- **S207 opencode (V1 route)** — "Ensure skill names are unique across all locations" (8 words)
- **S208 Microsoft Agent Framework** (correction row) — "All three skill tools require approval
  by default." (8 words), superseding S201's anchor.

Entry: `corpus/knowledge/skill-name-precedence-round69.md`, indexed in `corpus/README.md`.

**Delta against round 50, stated in the entry and the lesson.** `skill-selection-rules-round50.md`
already carries a same-name "which one wins" column including opencode's exact sentence; the new
ground is the four clients that column lacks plus the synthesis. The opencode row is re-carried,
and both row and entry scope themselves to the V1 route because `/v2/docs/skills/` (registry row
S064) carries a § Precedence ladder this round did not mine.

**Refused (1).** The r68 refusal of the staged S201 approval quote was corrected, not revived:
r68 judged the staged wording a *paraphrase*; the sentence is verbatim on the page twice, so the
true defect was the anchor. Row S208 supersedes the anchor; the r68 entry gains a `source: S208`
line and re-points its approval claim. The old refusal has no flip (superseded).

**Shaping (Q42).** S200's quote drops `<code>` around `.kilo/skills/`; S202's drops `**` around
"Standard Agent Skills path". Both disclosed in the lesson § Gate.

**Quarantine.** 13 register rows in this lane's slice (7 `payload-absent`, 6 `unreachable`);
S185 and S172 are this theme's rows, both re-opened under S203/S206. S172's register span
truncates mid-word and elides `<code>` parentheticals, so its `payload-absent` verdict names a
folded anchor copy, not a missing payload — the M111/Q62 class recurring on the campaign surface,
recorded in the lesson.

## Repairs routed by the round-68 closure (R68-1 … R68-8)

|#|defect|closure in this round|
|---|---|---|
|1|receipts not revision-pinned|nine receipts re-captured under `.ufo/waves/round-69/recapture/` with `measured-rev:`/`exit=`; two were re-taken in human mode so their `9/9 checks pass` line is the gate's own output, not a digest|
|2|r67 self-test receipt still red|re-captured `0 failure(s) over 6 assertions`, exit 0|
|3|r67 counter wrote the lane|sandbox moved to `reset --hard` inside a throwaway clone; no `checkout` token remains; a missing records file is a content verdict; an unknown revision stays exit 2|
|4|Q42 shaping notes|both notes land in the lesson § Gate|
|5|S201 supersede|S208 row + r68 entry `source: S208` + re-pointed citation (D5 now requires the source line)|
|6|mistake row + criterion|M111 names R68-6/S201 and the observed `verbatim` fact; QUALITY Q62 (a Q14 refinement) grounds refusals in observed facts|
|7|24 r68 wave paths uncommitted|all 24 land in `a02ba7e`; the 269 MB `c2falsify-clone/` is deleted and dispositioned; D7 also pins the landed diff at +6379/−251|
|8|index row + baseline|`lessons/round-68-verifier-spotcheck.md` and `lessons/round-69.md` both indexed; baseline re-recorded at 127 / 0 / 87 / 39 from the gate's own measurement|

Counter hardening done under seat attack (each defect reproduced before fixing): stub rule/client
cells, a five-word quote floor, coverage-map section scope, first-row-wins on a duplicate id, a
classified setup failure on partial states, bullet-block D6, diff-size D7, citation-requiring D5.

## Gate battery at the landing

- `verify_corpus_integrity.py` — **9/9 checks pass**, exit 0 (tracked 127, unindexed 0, report
  87, commit 39).
- `verify_corpus_independent.py` — exit 0.
- `check_gate_registry.py --rev HEAD` — 49 of 49 lane verifiers, phantom 0, exit 0.
- `verify_skill_checklist.py --json` — **10 pass / 1 fail, exit 1**. The red is
  `governance.citation_resolves`: `LOG.md:2676` and `:2678` cite `.ufo/waves/round-67/w1/controls/`
  paths that do not resolve, both past the frozen errata/corrections horizons. **Inherited from
  the r67 landing, not introduced or owned by any round-69 claim.** It is disclosed rather than
  excused: closing it needs two byte-pinned governance rows and its own self-test arms, which is
  a verifier change with no round-69 claim behind it. `SKILL.md` is 597 lines (budget 600).

## Mistakes

- **M111 — a refusal whose reason is false (R68-6, S201).** r68 refused the staged approval
  quote as a paraphrase; the sentence is verbatim on the page twice and the scout log had already
  located it. Captured by R68-6 in `round-68-verifier-spotcheck.md` and by M33 in `round-51.md`
  (Q23+Q14). Fix: S208 + the Q62 criterion; fails D5/D6 at `a5f7459` (0 of 8), passes at the
  landing commit.
- **M112 — uncommitted round-68 wave paths (R68-7).** 24 paths (10 modified, 14 untracked,
  one a 269 MB clone) were uncommitted while the r68 report said the evidence landed. Captured
  by R68-7. Fix: all 24 committed in `a02ba7e`, the clone removed and dispositioned, and D7 pins
  the diff size so a truncated landing fails.

## Learnings carried

- A counter's own self-test cannot see the defects a critic sees when both share the honest world;
  the round hardened five conjuncts only after seats reproduced each false accept.
- A metric named by a claim ("5 of 5") is only as strong as the version scope inside it: opencode
  splits V1/V2 across routes and one row cannot carry both.
- Inherited reds (the r67 governance citation) are cheaper to disclose with their cause than to
  excuse with a new pin under time pressure.
