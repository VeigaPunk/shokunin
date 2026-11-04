# kotodama — round 84 (hyaku run 15)

Lane: `/home/vgpnk/Projects/shokunin/kotodama-shokunin` (branch `main`).
Host: Linux/omp (kernel 7.2.11), 2026-11-04. L1: `KotodamaR84`.
Base `81499ee45b5751d388fefc78583810878de01ecd`; freeze
`7e6ee2f8f7b54dbeecf42cfe96050e533a86a6e2` (r2; r0 `3ca2cf28`, r1 `e160a72e`
recorded with red-befores in `reports/round-84/counter-revisions.md`). Claim D
lands `0f19297b295a59dacde15400d2382f73d38c4086`; claim O lands
`35ffc1ce7966d25481016a239e43069e6dfc2272`; bookkeeping `a6e5b0ff`; lane tip and
remote `12cc1699cd17fdbfa7dd3c6bfa688499d0438916`. `jj-lane.sh state` =
`ahead=0 behind=0`, `git status --porcelain` empty.

**Declared claims (two, distinct axes, each measured):**
**D** — depth: land `corpus/knowledge/myth-symbol/witchcraft-sorcery-accusation-institution.md`,
witchcraft and sorcery as an accusation institution, with four rows opened this
round. **O** — operability, capability acquisition: land
`tools/apply-sound-laws.py` (an ordered sound-law applier with an external rule
set and change traces) plus its committed two-era example and registry row. The
lowest-scoring non-retired axis is freshness; its move is paused by the open
round-11 L0 question (`.ufo/l0-questions.md` line 47: "Freshness axis-move claims
are paused until ruled"), so the round works depth and operability and claims no
freshness move.

## Work performed

- **Claim D (depth).** `corpus/knowledge/myth-symbol/witchcraft-sorcery-accusation-institution.md`
  lands (`0f19297b`) as the 258th knowledge file: 58,005 B, 15 `## ` sections,
  a six-row decision table, 44 single-id anchor bullets over 25 distinct ids,
  cited-lines lint 0 (`CITED-LINES: 0 finding(s) in 1 file(s)`), the vocabulary
  set and its translation traps, the accusation grammar, the proof technology,
  the confession and its record, the slander counter-suit, the commission's
  brake, and the social functions of the charge, with a NON-CANON worked
  example and the lore handoff. Before: no owner — filename sweep 0 of 257,
  matter-of-subject scan 0 files, the word-boundary pattern
  `\b(witch|witches|witchcraft|sorcerer|sorcery|malefic)\b` occurs on 19 lines
  in 11 files (all passing attributes; `stage/ScoutGapWitch/gap-census.json`).
  Rows S914–S917 are opened 2026-11-04 (EB11 "Witchcraft" B; Williams,
  *The Superstitions of Witchcraft* B; the Bull of Innocent VIII A; Upham,
  *Salem Witchcraft* B), S918 is EB11 "Sorcery" rejected as a printed 71-word
  dictionary stub with its flip; 21 already-registered rows the entry cites had
  the entry appended to `used-by` (old→new in the lesson Gate). Evidence:
  `reports/round-84/telemetry/lands-d84.txt` (`ACCEPT-D-84: PASS legs=10/10`),
  `junk-d84-r3.txt` (`PASS 3/3`), `controls-d.txt` (do-nothing refusal, exit 2),
  Gate in `corpus/lessons/round-84.md`.
- **Claim O (operability, capability acquisition).** `tools/apply-sound-laws.py`
  lands (`35ffc1ce`): 26,941 B, `--selftest` 37 checks, `apply --rules --input
  --out [--trace]` over a segment-tokenised lexicon, one trace line per change
  (input-side index, word before, word after), labelled exit-2 refusals for
  missing rules, non-JSON rules, empty `from`, duplicate/control-character rule
  names, an output that is an input, and `--out == --trace`. The committed
  example (`examples/sound-laws/`, 16 words, 7 ordered rules) is reproduced
  byte-for-byte with `SOUNDLAWS: 16 words / 7 rules / 19 changes` and all 7
  rules firing; an L1 held-out input of four unseen words matches a hand
  derivation (`stage/L1/heldout.*`), which is the check a copy-cheat fails
  (the mutation tester showed the canned DEMO alone cannot catch one).
  Three registry rows land; `GATE-REGISTRY: 0 missing / 77 registered / 63
  instruments / 0 dead`, `GATE-REGISTRY-INFO: 25 tools without a row`.
  Evidence: `telemetry/lands-o84.txt` (`ACCEPT-O-84: PASS legs=8/8`),
  `junk-o84` (`PASS 3/3`), `controls-o.txt` (do-nothing refusal, exit 2).
- **Attacks that landed.** `ReviewerEntry` filed D1–D16 against the entry
  (row-scope mismatches for S915/S917, the `- recheck:` cadence, the
  gap-filled pattern/count, an etymology resting on the rejected S918, 21
  `used-by` omissions, volume markers, a non-resolvable receipt pointer, the
  four-vs-five row count): all were fixed before the lands. `SentinelScope`
  filed F1–F14 (SEPARABLE at a shared tip — resolved by grading each claim at
  its own lands; the post-dispatch r2 — corrected in the record and named as
  R84-M4; the stale dispatch text — all verdicts graded at r2; criterion-31
  red from pending telemetry — the receipts were moved out of `reports/` and
  the checker is green; trace semantics, `--trace` overwrite, the output-dir
  guard, control-character rule names, and the `/dev/stdout` row — all fixed
  before the lands). `CriticClaims` items 1–7: items 1–3 are the r0/r1/r2
  freeze confusion (recorded as R84-M4), item 4 is the overstated before-state
  (R84-M5, corrected in this report), items 5–7 are counter kill-power gaps
  (R84-M6, named limits plus the held-out check). `MutationTester` killed 5/5
  assigned mutants and showed the copy-cheat passes the frozen DEMO 8/8 (the
  named limit above). `ConnectorOverlap` found no sibling owner for either
  surface. `ScoutGapWitch`/`ScoutSourcesWitch` produced the absence census and
  the independent source reading; the scout caught the L1's stripper-artefact
  misread of the Sorcery page (R84-M1).
- **Dead and partial seats.** None: 12 seats spawned, 12 settled, each returned
  output and wrote its report under `.ufo/waves/round-84/w1/`. No seat was
  respawned.

**Round shape.** One v1 wave (band 8–16), 12 seats: 2 scout, 3 executor,
2 scribe, 1 connector, 1 reviewer, 1 critic, 1 mutation-tester, 1 sentinel;
attack roles 3/12 = 25 % (reviewer, critic, mutation-tester); 1 connector; no
residual call; round total 12. Wave artifacts: `spec-v1.json`, `w1-dispatch.json`,
`w1.ready` + `w1.ready.dispatched` (2026-11-04T10:28:24), `w1-results.json`,
`w1/` (12 seat reports + stage). The L1 holds the canonical planner seat.

## Landed changes

| change | LOG entry | commit |
|---|---|---|
| `corpus/knowledge/myth-symbol/witchcraft-sorcery-accusation-institution.md` + S914–S918 + 21 `used-by` appends | round-84 item 1 | `0f19297b` |
| `tools/apply-sound-laws.py` + `examples/sound-laws/` + three `## Gates and probes` rows | item 2 | `35ffc1ce` |
| `SCORECARD.md` round-84 section + capability row, `LOG.md` entry, `corpus/lessons/round-84.md` (Gate + seven mistakes), `reports/round-84/` (counters, revisions, telemetry), `.ufo/waves/round-84/` | items 3–4 | `a6e5b0ff` |
| scorecard wording correction (name the attack record, not a raw count) | item 4 | `12cc1699` (lane tip) |

Counter revisions r0–r3 are in `reports/round-84/counter-revisions.md`: r1 the
house heading names; r2 the `SOUNDLAW_ERROR` marker (fixture-proven: a literal
`SOUNDLAW_ERROR:` would fail a correct tool); r3 the junk battery's expected leg
(the two-id anchor is killed by LINT, not ANCHORS). No grading leg changed
after any claim was scored; the freeze stayed r2.

## Before → after measurements

| claim | counting command | before | after (commit) |
|---|---|---|---|
| D | `python -B reports/round-84/accept-d84.py --root . --lands 0f19297b --freeze 7e6ee2f8 --work <scratch>` | 257 knowledge files, 837 registry rows, 0 owning basenames, 0 owning topic lines, entry absent (BEFORE leg) | `ACCEPT-D-84: PASS legs=10/10`, exit 0; entry 58,005 B, 15 sections, 6 decision rows, 44 anchors / 25 ids, lint 0; rows 842; junk `PASS 3/3` (measured at `0f19297b`) |
| O | `python -B reports/round-84/accept-o84.py --root . --lands 35ffc1ce --freeze 7e6ee2f8 --work <scratch>` | no general rule-set-driven applier (the bounded `check-craft-exercise.py` engine applies four hardcoded laws; the frozen text overstated this — R84-M5), `examples/sound-laws/` absent, no `SOUNDLAWS` byte in tools/examples | `ACCEPT-O-84: PASS legs=8/8`, exit 0; tool 26,941 B, selftest 37 checks, demo 16/7/19 with 7/7 rules firing, 3 negative cases exit 2, registry 0/77/63/0 with 25 unrowed; junk `PASS 3/3` (measured at `35ffc1ce`) |

Do-nothing controls: at `--lands` = base both counters refuse with
`FAIL legs=0/10` / `FAIL legs=0/8 (refused: lands equals the frozen base --
do-nothing control)`, exit 2 (`telemetry/controls-d.txt`, `controls-o.txt`).
The L1 held-out check (`stage/L1/heldout.tsv/.out.tsv/.trace.tsv` +
`heldout-hand.txt`) derives four unseen words from the committed rules and
matches the hand computation (`HELDOUT-MATCHES-HAND`). SEPARABLE is graded at
each claim's own lands (`span_parent=7e6ee2f8` for D, `span_parent=0f19297b`
for O), per the sentinel's F1.

## Sources & frontier

Registry rows **837 → 842** (`grep -cE '^ {0,3}\| *S[0-9]{3,} *\|'
corpus/SOURCES.md`). Rows added by tier: **A 1** (S916, the Bull of Innocent
VIII), **B 3** (S914 EB11 "Witchcraft", S915 Williams 1865, S917 Upham 1867),
**C 1 rejected** (S918, EB11 "Sorcery", printed 71-word dictionary stub; reason
and flip in the row and the Gate). Rows touched old→new: the last cell only of
**21** already-registered rows (S280, S295, S297, S349, S350, S381, S382, S403,
S605, S610, S621, S622, S644, S645, S854, S901, S902, S903, S905, S909, S912),
each appending `, corpus/knowledge/myth-symbol/witchcraft-sorcery-accusation-institution.md`
to `used-by`; the old→new values are listed in `corpus/lessons/round-84.md`
`## Gate`. No other cell of an existing row moved (append-only; the census
raises no E-code on the lane). Frontier rows advanced: none of the 17 named
frontier bullets — the new surface (frontier: no owner) moved into core, and
`ScoutGapWitch` records that 0 frontier bullets name it.

Census, run with
`/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotodama`:
start **exit 0** (`telemetry/census-start.txt`, 837 rows, the lane's pre-existing
W01/W04 warnings only); after the D land **exit 0** (`telemetry/census-d.txt`,
842 rows); end **exit 0** (`telemetry/census-end.txt`, 842 rows). Neither run is
a pass on admission; the independent non-author check remains required.

Assimilation: **none** — no `merge/kotodama/` theme fits this round's claims and
`considerthese/` does not exist in this lane. `ConnectorOverlap` found no sibling
owner for either surface (lore is the one-way canon target).

## Trend verdicts

- **expansion: improved.** Knowledge files 257 → 258 and registry rows 837 → 842
  at `0f19297b`, on ground no file or topic line owned at base; a capability row
  (`ordered sound-law applier`) enters SCORECARD.
- **quality: improved.** The lane can now derive an era's lexicon from an
  external ordered rule set with a trace and a committed example
  (operability, demonstrated end-to-end on 16 words and re-checked on 4 held-out
  words); no existing entry was re-verified, so the freshness half of the trend
  is unchanged (round-11 L0 pause).
- **discernment: improved.** Seven mistakes mined into `corpus/lessons/round-84.md`
  (a body-probe stripper artefact, a marker that graded an implementation
  detail, a contract/counter CLI mismatch, a post-dispatch freeze, an overstated
  before-state, counter kill-power gaps, a junk expectation on the wrong leg);
  the reviewer's 16 entry defects and the sentinel's findings were dispositioned
  before the lands, and the claimed-away gaps are named rather than hidden.

## SHONEN

- `[~]` SKILL.md decision tables, error patterns, checklists and registered
  sources — asserted at `SKILL.md:20`, `:505`, `:564`; this round adds three
  registry rows and `GATE-REGISTRY: 0 missing / 77 registered / 63 instruments /
  0 dead` (`reports/round-84/telemetry/lands-o84.txt`).
- `[~]` At least one end-to-end domain task logged in LOG.md — round-84 item 1
  (the accusation-institution entry, 44 anchors, lint 0) and item 2 (the
  sound-law applier end to end on a two-era example).
- `[~]` Instructions executable by an agent without oral context — the 12 seats
  worked from absolute committed paths and the frozen claims; spec, dispatch,
  results and seat reports are committed under `.ufo/waves/round-84/`.
- `[~]` No cross-domain bleed — `PROVINCE.md` is byte-identical across
  base..lands (`git diff-tree -r --name-status 81499ee4 35ffc1ce -- PROVINCE.md`
  empty); the entry hands canon to lore (`## 15`), and `ConnectorOverlap` found
  no sibling owner for either surface.

No `[x]` is claimed: promotion needs a named non-author verifier.

## Notes

- **Stale-lane:** respawn-per-round driver, one round per L1 dispatch; no other
  mission of this lane is open.
- **Tool installs:** none. The Python standard library and `curl` sufficed;
  pacman stayed paused and no other channel was needed.
- **Inherited state:** none uncommitted at round open. The fleet repo's
  pre-existing untracked `after` (24 B, 2026-11-03) and `.scratch/` state files
  are not this round's; no misroot was found (fleet `git status` shows no
  round-84-attributable path).
- **Freeze context:** r2 landed at 10:31:06, two minutes after the wave was
  dispatched at 10:28:24, so the seats read the r1 context; the delivered
  artifacts satisfy r2 and every verdict here is graded at r2 (R84-M4).
- **Named limits:** the D counter's `SOURCED` leg does not verify id membership,
  `ROWS` grades only cells 7/8/10, and `ANCHORS` tolerates one malformed bullet
  above its floor; the O counter's `DEMO` runs one input and a self-consistent
  copy-cheat passes it (the held-out check is the L1's offset). The frozen
  amendment is routed to round 85; no rule was changed after scoring.
