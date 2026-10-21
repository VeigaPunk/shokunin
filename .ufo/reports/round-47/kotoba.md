# kotoba — round 47 report

Coordinator: MoriR22R (reused idle agent; Main spawn job-capped) — died with the host
session after dispatching wave 1; replacement coordinator KotobaR47-2 (same held claim
`kotoba=47` attempt 1, BASE `c61a973b2e02e1ded169703ddcb06466f4edd8bd`), which paused on an
Anthropic 429 hold (retry-after 6621 s, not_before 2026-10-21T19:50:56Z) and resumed as the
same author. Lane: `/home/vgpnk/Projects/shokunin/kotoba-shokunin`. Final lane tip
`f1c2a68eb6e32065231005d20cce57dac179d710`; integration `7ad7fad`, falsify corrections
`3f4345479278ec87e656afb230e2644f2d7db9ba`, custody correction `f1c2a68`.

## Work performed

Declared claims (plan `plans/round-47.md`, unchanged by the replacement):
**C1 freshness** (lowest non-retired axis under the all-axes reading, 8.0) — re-derive then
re-pin the instruction-surface substrate for omp 18.12.5 and opencode 1.19.3;
**C2 operability** (8.5) — a frontmatter XML-tag check, sourced on S003 (+ S012), and this
lane's own description loses `<skills>`; **C3 calibration** (8.5) — a pinned fail-closed
erratum for the governance citation gate's one recorded absence (`LOG.md:2111`) and the
round-46 spot-check file indexed. Frontier step: S012–S015, M20–M23, Q19.

- Inherited and re-verified: the predecessor's before-run (`.ufo/waves/round-47/before/SUMMARY.md`,
  re-checked against live substrate — omp `fdbc8136…`, opencode ELF `179ca421…` unchanged),
  the frozen snapshot `/fast/scratch/kotoba-r47/shared/` (`sha256sum -c` 4/4), the plan, the
  92-seat wave-1 spec/dispatch/refusals/registry, and its 72 seat reports; its L1 clone edits
  (SKILL.md token swap, README row) were re-done from the critic-reviewed patches.
  Discarded: the 20 dead wave-1 seats' partial artifacts (e.g. `C2CheckImpl.patch`,
  `CritNoHarm.planter.patch`) — never integrated; `ExecDescriptionCheckAlt.patch` (scans
  `description` only) and `RevPinsContract.patch` (changes the pin target to 4/4) not taken.
- C1: omp callees `lq|Xl|Fo` appended with an 18.12.5 fixture (`C1OmpCallShapes`); opencode
  1.19.3 recognised as the round-14 loader lineage and OC-1..OC-6 re-measured anchor by anchor
  on the frozen dump (OC-3b requires `.filter(`, OC-4 adds `ReadTool.execute`); 7 ids
  resurrected, 1 retained, `config/instructions` re-verdicted governed, 3 v2.0.26 ids retired —
  census § B′ + ledger (`corpus/knowledge/instruction-surface-census-round13.md`); fixtures
  rebuilt from dump substrings, v2.0.26 fixture kept as a must-fail generation probe; default
  opencode path moved in all three verifiers; `verifiers/baseline.json` re-pinned from the
  snapshot. Evidence: `.ufo/waves/round-47/after/SUMMARY.md`, `falsify/W2Matrix2x2.md`.
- C2: `trigger.no_xml_tag` (`verifiers/verify_skill_checklist.py`, reference design
  `build/C2CriticRule.md`), four fixtures, SKILL.md token removed. Evidence `falsify/W2XmlLive.md`.
- C3: `GOVERNANCE_ERRATA` (line-sha-pinned, horizon 2315, `build/C3CriticDesign.md`); README
  rows for the round-46 spot-check and round-47 lesson; corpus baseline 58→60; fault-harness
  planter scoped to `## Coverage map` (`build/ExecFaultBaseline.md`). Evidence `falsify/W2ErrataLaunder.md`,
  `falsify/W2CorpusBaselineFit.md`, `falsify/W2FaultHarness.md`.
- Floors ratcheted in step (surfaces 87→99, checklist 1597→1845).
- Planner seat: held by the L1 (validator rejects `planner`); planning data-walk rode
  ConnClaimSeparability (dead) and RevPlanCalibration (a reviewer; dead).
- Waves: W1 build 92 seats (scout 39, executor 17, reviewer 10, scribe 8, connector 6,
  critic 5, revenger 2, sentinel 2, mutation-tester 2, simplifier 1), spawned on gate try 9
  after 8 job-cap refusals; 72 reported, 20 dead (named in LOG.md round-47 entry).
  W2 falsify (post-crash, fresh identities, disclosed per the parent's ruling) 77 seats
  (reviewer 28, scout 19, critic 10, executor 10, mutation-tester 5, connector 3, sentinel 2),
  spawned on try 2 after 1 refusal; 73 reported, 4 dead (W2S015Rerun, W2PlanNote,
  W2JjHygiene, W2EvidenceBloat — 0-byte, stay dead/uncredited). Round total 169 seats,
  24 dead. Routing: host role map, no model parameters. Provider deaths: the 20 W1 deaths
  were the host SIGHUP; the 4 W2 deaths followed the coordinator's Anthropic 429
  (`rate_limit_error`, retry-after-ms 6621000); 22 W2 seats saw an in-transcript 429 and
  still finished (checkpoint `/fast/scratch/hyaku-resume-s3/checkpoint-kotoba-r47-provider.md`).
- Seat incident: W2DropOC2 wrote into production `verifiers/verify_surfaces.py` via a
  relative path for ~1 min and restored it byte-identical; lane verified clean at `7ad7fad`.
- Falsify outcome: every counting command reproduced; record defects corrected in
  `3f4345479278ec87e656afb230e2644f2d7db9ba` (LOG.md "evaluated 804" → 848, SKILL.md "10 checks" → 11, fixture-header and
  comment overclaims, README rows, census/round-14 errata); gate-strength defects carried
  (presence-only OC rules, tautological OC-1 gate, non-ASCII tag FN, escape FP, unpinned
  npx launcher, silently ignored compound pin keys) — LOG.md § Round 47 landing pin and
  falsify wave.

## Landed changes

- `7ad7fad` — LOG.md § Round 47 landing: C1/C2/C3 code, data, fixtures, census, SOURCES,
  QUALITY Q19, lesson round-47, README/PROVINCE/SCORECARD/plan, wave-1 evidence.
- `3f4345479278ec87e656afb230e2644f2d7db9ba` — LOG.md § Round 47 landing pin and falsify wave: falsify corrections
  (records/comments only, no gate logic), lesson M23, after/ and falsify/ evidence,
  after-falsify battery `.ufo/waves/round-47/after-falsify/SUMMARY.md`.
- `f1c2a68eb6e32065231005d20cce57dac179d710` — LOG.md final custody append:
  parent's historical-scope correction, cleanup incident and verified shared-snapshot restoration;
  `.ufo/waves/round-47/after-falsify/snapshot-restoration.txt`.
- Fleet: `c2e2913` (two L0 lines), this report.

## Before → after measurements

| claim | counting command | before (BASE `c61a973`) | after (`7ad7fad`; same at `3f43454`) |
|---|---|---|---|
| C1 | `python3 -B verifiers/verify_surfaces.py --json` | exit 2 (opencode binary not found) | exit 0, 7/7 |
| C1 | `python3 -B verifiers/check_substrate_pins.py` | exit 2, DRIFT 3/3 | exit 0, 3/3 |
| C1 | AFTER code × BASE baseline+census | — | exit 1 (discriminating cell) |
| C2 | `sed -n '/^---$/,/^---$/p' SKILL.md \| grep -c '<skills>'` | 1 | 0 (grep exit 1) |
| C2 | `python3 -B verifiers/verify_skill_checklist.py --json --check trigger.no_xml_tag` | check absent | PASS, evaluated 2 |
| C2/C3 | `python3 -B verifiers/verify_skill_checklist.py --self-test` | 1597 | 1845 (C2 1837 + C3 8), 0 failures |
| C3 | `python3 -B verifiers/verify_skill_checklist.py --json` | exit 1, 9 PASS / 1 FAIL (LOG.md:2111) | exit 0, 11/11 (governance evaluated 848 at `7ad7fad`, 871 at `3f43454`) |
| C3 | `python3 -B verifiers/verify_corpus_integrity.py --json` | exit 1, 2 DRIFT | exit 0, 9/9 |
| C3 | `python3 -B verifiers/verify_corpus_independent.py --json` | exit 1 | exit 0 |
| C3 | `bash verifiers/fault_injection_corpus.sh --repo $PWD` | exit 1 | exit 0, ALL PASS |
| no-harm | `python3 -B verifiers/verify_harness_claims.py` | exit 1, 21/28 | exit 1, 21/28, same 7 DRIFT ids |

## Sources & frontier

`/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotoba`
→ start `kotoba ok` exit 0 (`.ufo/waves/round-47/census-start.txt`); end `kotoba ok` exit 0
(`after/census.out`, `after-falsify/census.out`). Rows 11 → 15 (tier A +4: S012 code mined,
S013 docs queued, S014 docs queued, S015 own-work mined); rows touched old→new: none (S001
anchor defect, S003 teaches defect and S010 stale teaches recorded for superseding rows in
round 48). Sourced claim: C2 on S003 (re-opened) + S012; C1 on S015. Mined mistakes M20
(stale planned premise → Q19), M21 (unindexed closure landing), M22 (stale lesson pointers),
M23 (landing record quoting a count from another tree). Frontier: the XML-tag rule moved to
PROVINCE Core; Loader-rule freshness stays Frontier, narrowed.

Exact validation outputs (start/end, both exit 0):
```text
start: kotoba	ok	/home/vgpnk/Projects/shokunin/kotoba-shokunin/corpus/SOURCES.md
end:   kotoba	ok	/home/vgpnk/Projects/shokunin/kotoba-shokunin/corpus/SOURCES.md
```
Row-count command (BASE stdout versus final file):
`python3 -c 'import re,subprocess,pathlib; b=subprocess.check_output(["git","show","c61a973:corpus/SOURCES.md"],text=True); a=pathlib.Path("corpus/SOURCES.md").read_text(); print(*(sum(bool(re.match(r"^\| S\d{3} \|",l)) for l in s.splitlines()) for s in (b,a)))'`
→ `11 15`. No change to parent-owned source-census tooling or dispatch baselines.

## Trend verdicts

- expansion: **unchanged** — no `corpus/knowledge/` entry admitted (34 → 34; `falsify/W2TrendVerdicts.md`).
- quality: **improved** — the census re-derived for the live substrate with a class ledger,
  and the stale round-14/§ B/§ A statements the falsify wave found are now marked by
  append-only errata (the seat's `harmed` reading applied to the pre-errata tree).
- discernment: **unchanged** — no non-author spot-check this round; wave 2 is lane-dispatched.

Claim verdicts (lane view, for the non-author closure to rule): C1 improved (measured;
gate-strength limits carried); C2 improved (measured; Unicode-name FN and escape FP carried);
C3 **unprovable** for calibration/no-harm admission despite passing counting targets. Scores held (delta 0 on each claimed axis); no round admission asserted. **No-harm is contested:** moving `OC_BIN` to the live ELF makes the
producer's `oc.roots.names_plus_builtin` 10 → 11 against the independent instrument's
declared 0 built-ins, so the comparator's frozen-carrier join moves 21/24 → 20/24
(`falsify/W2DepthNoHarm.md`); its default live join exits 2 at BASE and landing alike.
Reported, not resolved.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — `.ufo/waves/round-47/build/ShonenEvidence.md`; `SKILL.md` 41 boxes, `--json` 11/11.
- [~] End-to-end domain task executed and logged — `LOG.md` § Round 47 landing (C1 re-derivation red→green on the live substrate).
- [~] Instructions executable without oral context — `corpus/lessons/round-8-aggregator-box3-coldrun.md` (no fresh non-author run this round).
- [~] No cross-domain bleed — `PROVINCE.md` Core/Frontier updated round 47; sibling substrate records reported, not absorbed (`falsify/W2SiblingOverlap.md`: kagi, kumitate, kaidoku still name `~/.opencode/bin` / omp 18.12.3).

## Other

- Stale-lane: respawn-per-round driver; no other mission of this lane is open.
- Tool installs/updates: none (coordinator and all reporting seats).
- L0: appended `kotoba | round-47 | …` lines (advisory-axis reading; LOG erratum mechanism) at fleet `c2e2913`; open.
- Cross-domain: siblings kagi/kumitate/kaidoku record removed opencode path / old omp version (report-only).
- Scratch cleanup incident: under the earlier deletion instruction, `/fast/scratch/kotoba-r47/`
  and 13 identified owned temp files were removed **after** all source edits/evidence landed
  at `3f43454`, just before the parent's stricter preservation correction arrived. No unmerged
  production edits lost. The shared snapshot was reconstructed from live pinned files plus
  regenerated strings and all four full SHA-256 values matched committed pre-deletion receipts.
  `/fast/scratch/kotoba-r47/shared/` is retained. Historical dump mtimes/inodes are not restored.
  Scratch-only experiment Git objects may be lost; their availability is not asserted.
  Post-incident `omp worktree list --json` and `omp worktree clear --dry-run` listed only an
  unrelated empty `ufo-elegance` directory (not removed); no clear command or further cleanup.

## Custody and admission qualifications

- W1/W2 reports are lane-authored evidence, never the required non-author closure.
  Parent clarified that the new sole-report/no-scratch rule does **not** retroactively
  rewrite W2's captured permissions. The provisional 58-report lexical hold in the
  first custody note is **withdrawn**: zero reports void solely for authorized scratch use.
  W2DropOC2's production-write incident remains separate; its candidate source was not
  integrated, while its in-scope findings remain lane evidence. No blanket-void count.
  Full chronology: `.ufo/waves/round-47/falsify/custody-note.txt`.
- L1 exercised positive authority: after-falsify source-tree battery (all target checks exit 0,
  harness claims exit 1, floors exit 0 with explicit 300-second timeout); checklist exit 0,
  governance evaluated 871, and fleet-root census exit 0 measured immediately before
  `3f43454` landed the byte-identical source (`after-falsify/final-checklist.json`,
  `final-census.out`). `f1c2a68` adds custody prose/evidence only; its new governance
  population was not re-counted and is not claimed as 871.
- Frozen-target honesty: full no-harm admission is not established. C3 remains **unprovable**;
  the reported join disagreement, hard-coded erratum design limits, S003/S010/S013 source
  defects, Q19's unlanded prototype limits, Unicode XML and escape boundaries, and
  source-snapshot cleanup are not converted into passes. Parent retains MANIFEST/admission.
- Fleet misroot sweep (unrestricted `git status --porcelain`) found only parent-owned
  driver/state modifications; no round-47 seat misroot to move. Those files were untouched.

## Final object-custody append (supersedes earlier tip/custody availability wording)

Final lane tip: `92aa937fb767ace51752fa4188e3382905042737`, landed through the helper
after `f1c2a68`; LOG.md final append and
`.ufo/waves/round-47/after-falsify/git-object-custody.json` carry the additional audit.
No code or claimed counting target changed in this custody-only commit.

The restored snapshot is **reconstructed**, not uninterrupted custody. All four byte
digests were compared against the **original committed expectations**, not refitted.
Restoring identical bytes did not recover past Git objects: explicit cited scratch commits
`b1b48d1`, `5d50621`, `371e901`, `51385ae`, `d68eae3`, `2e6e5c1`, and measured scratch tree
`a736f6407ba02a038a6c0256c40cc932727688fc` do not resolve in lane or fleet stores.
They were not synthesized. Production landing commits and their source bytes remain retained.

Audit population: 953 standalone hex candidates (deliberately overinclusive, many truncated
SHA-256s, **not 953 claimed Git commits**); 90 resolve to commits reachable from lane refs,
17 from fleet refs, 60 existing objects lack proved ref reachability, 786 candidates
do not resolve in either repository. Thus durable availability of **every** cited
experiment object is not established; that limitation remains **unprovable**. No further
cleanup, source reconstruction, routing change or round dispatch occurred.
