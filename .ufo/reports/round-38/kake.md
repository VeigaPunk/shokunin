# kake — round 38 report

L1 `KakeR38` (hyaku in-session), attempt 1. Lane base `af43a50fa399881eead9381d835b78a015e277a6`,
lane tip `729878e3e74e18b55cd9a58d071a4f7b2419a8b7` (pushed; `jj-lane.sh state`: ahead=0 behind=0,
tracked=0 untracked=0).

## Work performed

Declared claims:
- **C1, operability (tool repair) — withdrawn before any build.** `scripts/robots_audit.py` was
  to gain rules (h) non-JSON number literals and integers of any length, (i) URL characters and
  (k) the implicit `/robots.txt` allow on the normalized path. Counter v2, predicate
  `met: passed >= 19 of 20 sealed cases`, declared at `b0ab7f60`.
- **C2, operability (tool repair; redesign of C1).** The same three rules under counter v3, key
  v3 and control classes named in advance. Predicate `met: passed >= 20 of 20 sealed cases`,
  declared at `2dab7f31`. Measured 8 → 20 of 20. Self-verdict: **measured met; admission
  contested** (see Gate).

Work items:
- Round-37 closure routed defect 1: SCORECARD "Round 37 — closure correction" (C1 not admitted).
  Both robots capability rows now end "not admitted" (`b0ab7f60`, `2dab7f31`).
- Routed defect 2: the round-37 shortcut (`CtlC1Shortcut-followup`, 28 of 28 under the round-37
  counter) scores 7 of 20 under v3, and a stdlib reader patched for (h), (i), (k) scores 13. The
  round-37 counter stays round 37's rule of record (`SCORECARD.md` "Round 38 — C2 declared";
  `verification/v3/`).
- Control call `kake-r38-ctl` (7 seats) ran before any build. Controls of C1's declared kinds met
  its predicate: 29 of 42 reference mutants and four full-rule wrappers. C1 was withdrawn per its
  own declared consequence, and C2 was declared with a stricter key and counter (MutCounterV2 F1/F2
  fixed, `checksEvaluated` compared). Receipts landed at 04:28:54Z, 58 s before wave 1 was
  dispatched (`2dab7f31`; `criteria/receipts/timeline-r38.txt`).
- Build: wave-1 `ExecRobotsTool`'s file, landed unedited (`3ed8e15c`, sha256 `f4d057c4…baace`).
  Keys, private reference, ablations and mutants revealed at `99357694`.
- Routed defect 3: QUALITY (j) check `.ufo/waves/round-38/criteria/control_consequence_check.py`.
  Round 37 exit 1, rounds 36 and 38 exit 0, selftest 10/10 (`145a6468`;
  `criteria/receipts/ccc-*.txt`).
- Routed defect 5: `pinned_selftest.py`. The round-37 postfix receipt is pinned at `944d2f51…d3e5`,
  137/137 (`verification/postfix/r37-postfix-selftest-pinned.json`). The round-38 harm receipts
  carry `toolSha256` (`verification/harm/`).
- Routed defect 4: QUALITY (k), rule only. No seat died this round.
- Carried round-37 items closed: the robots tool's `NaN`/long-integer/malformed-URL defects (C2).
  `source_recheck.py` body cap (16 MiB) and `MemoryError` handling: hardening 9/9, selftest
  106/106, round-36 counter 28 of 28 (`145a6468`, `verification/harm/`).
- Robots selftest 137 → 194 fixtures, written blind; the base fails exactly the 45 (h)/(i)/(k)
  fixtures (`145a6468`).
- Real-input run on 12 retained robots.txt files plus 36 new checks and six (h) manifests: the
  build matches 7 of 7 oracle runs, the base 1 of 7 (`.ufo/waves/round-38/realrun/build-3ed8e15c/`,
  `b7d821e3`).
- Sources S098–S101, knowledge-entry round-38 section, QUALITY round-38 (j)–(n), PROVINCE, README,
  SKILL amendments, lesson, LOG (`adab4c7e`). Wave-2 corrections (`729878e3`).

## Landed changes

| Commit | LOG.md round-38 entry | What |
|---|---|---|
| `b0ab7f606d1f61fb6b850785866ba71583f629cc` | bullet 1 | round-37 closure correction; C1 declaration, counter v2, before and separation receipts |
| `2dab7f3114f3e9dcf072b524c88816ab05fdfcf1` | bullet 2 | control-call receipts; C1 withdrawn; C2 declared, counter v3, v3 receipts |
| `3ed8e15c2707ac4cec88f48fc9be48b35be4f2b0` | bullet 3 | C2 build `scripts/robots_audit.py` |
| `99357694f68886d3175fc6c386979c350be789bc` | bullet 3 | reveal: keys v2 and v3, private reference, ablations, mutants |
| `145a6468de861470ae558e3a8ce9573680b81fb0` | bullet 4 | selftest 194, source_recheck caps, (j) and timeline checks, pinned runner |
| `adab4c7e9ec2178657395f49346f18800ff4796f` | bullet 4–5 | measured results, harm receipts, SOURCES, knowledge entry, QUALITY, PROVINCE/README/SKILL, lesson, LOG |
| `b7d821e3a79bd5d5fa7658b7cc82b2d385232a98` | bullet 3 (real run) | real-run evidence, late wave-1 reports, wave-2 spec |
| `729878e3e74e18b55cd9a58d071a4f7b2419a8b7` | lesson "Wave-2 corrections" | wave-2 reports and corrections, independent v3 receipt, v3 sweep, census after |

## Before → after measurements

| Claim | Counting command | Before (rev) | After (rev) | Verdict |
|---|---|---|---|---|
| C1 (withdrawn before any build) | `python3 -B .ufo/waves/round-38/sealed_count.py --root . --revision <rev> --key-revision 99357694` | 8 of 20 (`af43a50f`) | not measured (withdrawn at `2dab7f31`) | withdrawn; controls met (`verification/control-*.json`, `mutref/`) |
| C2 robots_audit (h), (i), (k) | `python3 -B .ufo/waves/round-38/sealed_count_v3.py --root . --revision <rev> --key-revision 99357694` | 8 of 20, exit 1 (`af43a50f`, `b0ab7f60`, `2dab7f31`) | 20 of 20, exit 0 (`3ed8e15c`) | measured met; admission contested |

Harm, not claims: round-37 counter on the build's tool 28 of 28; selftest 137/137 at `3ed8e15c` and
194/194 at `145a6468`; source_recheck 106/106, hardening 9/9, round-36 counter 28 of 28. Wave 2
`ReviewHarm` found no regression from base to tip.

## Sources & frontier

- Census `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kake`:
  round start exit 0 (three W04, `kake ok`; `.ufo/waves/round-38/census-before.txt`). Round end
  exit 0 (five W04 — the new S098 and S099 share URLs with S029 and S011 — `kake ok`;
  `census-after.txt`).
- Rows 97 → 101. Added by tier: A 4 — S098 RFC 3986 §§2.1–2.3 (spec, mined), S099 RFC 9309 §§1–5
  (spec, mined; supersedes S011's narrow scope), S100 Python json docs (docs, mined), S101 WHATWG
  URL Standard (spec, **rejected**: not the contract's source; flip if the lane adopts WHATWG
  parsing). Touched old → new: S034 `used-by` gains `corpus/knowledge/robots-txt-rules.md` and
  `corpus/lessons/round-38.md`. S034 and S011 were re-opened with the same bytes as before; their
  status and recheck are unchanged.
- Gate (`corpus/lessons/round-38.md` `## Gate`): URL, access time and a quote of at most 25 words
  for each row. Wave 2 re-opened all five; location fixes are in "Wave-2 corrections".
- Sourced claim: C2's rules rest on S034 §6, S098 §2 and S099 §2.2.2, all opened this round. The
  knowledge entry cites them; Google's divergence is recorded from S096 `robots.cc`.
- Frontier: PROVINCE "Round-38 robots audit repair step". This repairs ground already held; no new
  frontier area. Mined mistakes: five rows plus one wave-2 row in `## Mistakes`. Each has a check
  shown able to fail (control-consequence check, timeline check) or a receipt.

## Trend verdicts

- **expansion: unchanged.** The round repaired an existing tool and extended an existing knowledge
  entry (S098–S100 readings, Google's implicit-allow divergence). It opened no new ground.
- **quality: improved.** Routed defects 1, 3 and 5 were repaired, and each check has red and green
  receipts. Counter v3 closes 13 false passes that v2 allowed (mutants at 20: v2 13, v3 0). Robots
  selftest 137 → 194. The source_recheck caps landed, and wave 2 reproduced every receipt.
- **discernment: unchanged.** For: C1 was withdrawn under its own declared consequence before any
  build, which is the round-37 mistake not repeated. S101 was rejected with a flip. Ablations show
  the four full-rule tools do all three rules (`w2/AblateBuilds.md`). Against: C2's "build" class
  was written after those tools had scored 20 under v2 (`w2/CriticReclassification.md`). The
  claim's 20 of 20 left untested sentences (`w2/CriticKeyExpectations.md`, `w2/MutBuildTool.md`).

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources: `SKILL.md` "Robots.txt expectation audit — round-38 amendment to the gate registry row" (`adab4c7e`); wave-2 `ReviewQualityProvince` holds.
- [~] At least one end-to-end domain task executed and logged in LOG.md: real-input run on 12 retained robots.txt files plus (h)/(i)/(k) checks, LOG round 38, `.ufo/waves/round-38/realrun/build-3ed8e15c/summary.json`; re-run by wave-2 `ReviewRealRun`.
- [~] Instructions executable by an agent without oral context: counter, selftest, criteria and pinned-runner commands re-run from their written strings by wave 2 (`w2/RerunC2Receipts.md`, `w2/RerunControlsV3.md`, `w2/ReviewQualityProvince.md`).
- [~] No cross-domain bleed (PROVINCE.md still accurate): PROVINCE round-38 step; wave-2 `ReviewQualityProvince` holds; tabi boundary per `w1/ConnectorSiblings.md`.

## Round shape and seats

- Shape: default two v1 waves plus a pre-freeze control call (an ordinary `task` call of 7 seats,
  at most 8). Each wave was validated under `scripts/hyaku/ufo-wave-policy.json` and dispatched as
  one `task` call with the validator's `taskCall` (through `tool.task`; `solutionSpace` added per
  the tool schema). `wave-slot.sh` granted and released each.
  - Control call `kake-r38-ctl`: 7 seats — 5 critic, 2 mutation-tester.
  - Wave 1 `kake-r38-w1`: 32 seats — 8 scout, 9 executor, 5 scribe, 3 critic, 3 reviewer,
    1 connector, 1 sentinel, 1 revenger, 1 mutation-tester.
  - Wave 2 `kake-r38-w2`: 34 seats — 19 reviewer, 5 scout, 4 mutation-tester, 3 critic,
    2 sentinel, 1 revenger.
- Round total: 73 seats. The L1 held the planner seat (the validator rejects `planner`); the
  planning data-walk rode `ScoutPlanWalk`. The §3 floor was met inside wave 1.
- Dead seats: none (7/7, 32/32, 34/34 returned). Refusals: none.
- Containment: no seat wrote a lane file outside its report (`w2/ReviewContainment.md`). The
  misroot sweep (`git -C /home/vgpnk/Projects/shokunin status --porcelain`) found no kake round-38
  file at the fleet root. Three disclosed metadata probes touched sealed-tree paths without reading
  content: `CtlStdlibV2` ran `test ! -e`, `ProbeDigits` ran `test -d`, and `CriticControlReceipts`
  listed child names once.

## Gate

- **Real reject: C1** (declared `b0ab7f60`). Controls of its own listed kinds met its predicate: 29
  of 42 reference mutants and four wrappers that implement all three rules. Withdrawn before any
  build seat was dispatched; receipts `verification/control-*.json`, `mutref/`.
- Real reject: S101 WHATWG URL Standard (not the contract's source; flip named).
- **Contested, for the closure:** C2's control-class list. It names in advance that "a tool
  implementing all three rules is a build". That sentence was written after four such tools had
  scored 20 under v2. `CriticReclassification` judges that a strict reading of the round-37 ruling
  rejects it. `AblateBuilds` shows each of those tools drops to 16 when any one rule is removed.
- Not admitted to any claim: the source_recheck caps, selftest additions, criteria checks and
  pinned runner (non-claim repairs).

## Other

- Stale-lane: respawn-per-round driver; no other mission of this lane is open.
- Tool installs: none by the L1 or reported by seats. No pacman.
- Open L0 questions: none.
- Carried to round 39 (`SCORECARD.md` "Round 38 — wave-2 corrections"):
  - Untested (h)/(i)/(k) sentences: `/robots.txt?`, bare `%`, explicit `Disallow: /robots.txt`, and
    the 20 s bound.
  - Six build mutants that survive both instruments.
  - source_recheck `moved` + `check_invalid` on oversized bodies.
  - The (j) check's mutant survivors and its name-based classification.
  - Lone-surrogate URL reading.
  - Bracket hosts.
  - Knowledge entry still cites S011 outside its scope.
  - Symlinked manifest directory, U+FFFD per byte, duplicate JSON member names.
