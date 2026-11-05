# mori — round 90 (L1 MoriR90, resumed attempt)

Lane repo `/home/vgpnk/Projects/shokunin/mori-shokunin`, branch `master`. Entering revision
`d1c8488986512a6a0475af88cc52779ce4703e00` (the commit that preserved attempt 1's in-flight
round-90 files after its L1 died on a provider failure; it adds only `.ufo/waves/round-90/`, and
every graded subject is byte-identical to the contract's entering `037c02ca`). Lane tip after this
round: `0a1f019b16d8a3e4952a34962c45e55e1a1dd7f7` (pushed; `git ls-remote origin
refs/heads/master` agrees). Resumed-attempt note: the contract, counters and controls were
re-verified before reuse; the inherited spec is kept as `.ufo/waves/round-90/w1-spec.inherited.json`
and the working copy differs from it only in the entering revision, the L1 id and the role encoding.

## Work performed

Declared claims (frozen in `.ufo/waves/round-90/contract.md` before any after-value; two claims,
two axes, causally separable — neither counter reads the other's subject):

- **C1 · operability** — the round-87 receipt gate refuses the non-executing-branch class with
  `harm=0` on the 78-case population and `branch_open=0` on the round-90 held-out battery.
- **C2 · calibration** — the three round-89 neighbouring survivors are killed with attributed and
  isolated FAIL sets (B1 `own_ok_arm_count`, B4 `met_line_call_site`, B6 `clone_root_negative`).

Calibration is the lowest-scoring non-retired axis (5, tied with depth and freshness), so the
stagnation nudge does not waive it; C1 moves operability (7). No score move is claimed.

Work items, each with its evidence pointer:

- **Reachability rule in the gate.** `.ufo/waves/round-87/count-c2.py:invocations_visited` (landed
  at `11197820`, sha256 `3fc9cc44…`): AND-OR short circuit from a literal status, sequencing after a
  literal `exit`/`return`, unselected `if`/`elif`/`else` bodies, subshell status, `!` negation,
  loops that cannot iterate, statements after `break`/`continue`, unmatched literal `case` arms,
  and glued control tokens (`);`, `)||`, `)&`) split so a subshell's terminator never ends its
  parent. Evidence: `C1=met …` and the battery line in `.ufo/waves/round-90/evidence/after-r90.txt`.
- **Held-out battery.** `.ufo/waves/round-90/battery/branch-heldout.json` (18 cases: 14 branch
  rejects of shapes the eight frozen ids do not use, 4 provenance `met` cases that must still
  bind), written by seat `Mo90E04Battery` before it saw the rule
  (`.ufo/waves/round-90/w1/Mo90E04Battery.md`).
- **B1/B4/B6 arms.** `.ufo/waves/round-88/count-c1.py` 28 → 29 arms and `count-c2.py` 26 → 27; the
  two count-c2 arms are structural pins by necessity
  (`.ufo/waves/round-90/w1/Mo90E03ArmsB46.md`, `.ufo/waves/round-90/w1/Mo90C01Critic.md` §2).
- **C1 attack (non-author).** Seat `Mo90R01C1` measured five glued-paren harms on the first
  integrated candidate (`.ufo/waves/round-90/w1/Mo90R01C1.md`, "Re-attack on the integrated
  candidate 79350315…"); all five bind after the landed fix, and its 78-case + 18-case re-run reads
  `branch_open=0 harm=0 newopen=0`.
- **C2 attack (non-author).** Seat `Mo90R02C2` falsified the isolation rule's canary/blanket/label-
  only forgeries (`.ufo/waves/round-90/w1/Mo90R02C2.md`); seat `Mo90C01Critic` judged the claim
  design and found the frozen arm-count arithmetic and the lookup-table reachability
  (`.ufo/waves/round-90/w1/Mo90C01Critic.md` §1–§4).
- **Mutation probe.** Seat `Mo90M01Mut` mutated the landed gate: 17 of 24 single-point rule mutants
  killed, 14 of 21 on the earlier snapshot, and none of the fifteen declared C2 mutants survives
  (`.ufo/waves/round-90/w1/Mo90M01Mut.md`).
- **Scope/boundary checks.** `Mo90Sc01Scope` classified the provenance class and
  `Mo90Se01Boundary` checked the counters' write scope, git reads and predicate-string identity
  (`.ufo/waves/round-90/w1/Mo90Se01Boundary.md`); `Mo90K01Conn` mapped every cross-round pin the
  landing moves (`.ufo/waves/round-90/w1/Mo90K01Conn.md`).
- **Frontier.** S612–S616 opened this round (seat `Mo90S01Sources`, quotes re-checked by the L1
  against the pinned copies), knowledge entry
  `corpus/knowledge/branch-reachability-r90.md`, lesson `corpus/lessons/round-90.md`, QUALITY
  190–192.

## Landed changes

- `11197820` **round-90.1** — `.ufo/waves/round-87/count-c2.py` (reachability pre-pass; 26 selftest
  arms unchanged), `.ufo/waves/round-88/count-c1.py` (29 arms), `.ufo/waves/round-88/count-c2.py`
  (27 arms), `.ufo/waves/round-90/battery/branch-heldout.json`, and the whole round-90 wave tree
  (spec, dispatch, ready markers, candidates, 13 seat reports, registry). LOG entry: `## Round 90`.
- `9441ef30` **round-90.2** — `.ufo/waves/round-90/evidence/after-r90.txt` (both counters, before
  and after, one clone), `corpus/SOURCES.md` (S612–S616), `corpus/knowledge/branch-reachability-r90.md`,
  `corpus/lessons/round-90.md`, `corpus/QUALITY.md` (190–192), `SCORECARD.md` (round-90 section and
  the round-91 plan), `LOG.md`.
- `0a1f019b` **round-90.3** — `SKILL.md` (round-90 registry pointer; supersedes the r89 receipt
  pointer and names the r89 `28/26` arm pins superseded), `LOG.md` (append-only corrections of
  record D1/D2/D3/D5/D6/D7 from the round-89 verifier spotcheck).
- Report commit: this file, via `fleet-commit.sh --as mori`.

## Before → after measurements

Counting command for both claims (each run against a `git clone --shared` of the lane so the
revision is replayed, never the working tree):

```
python3 -I .ufo/waves/round-90/count-c1.py <rev> --repo <clone> --scratch <scratch>
python3 -I .ufo/waves/round-90/count-c2.py <rev> --repo <clone> --scratch <scratch>
```

| Claim | Before (subject at `037c02ca`, do-nothing) | After (measured at `11197820`) | Axis |
|---|---|---|---|
| C1 | `C1=unmet branch_open=8 harm=0 newopen=0 open=30 cases=78` rc 1; `BATTERY cases=0` (no battery at that rev) | `C1=met branch_open=0 harm=0 newopen=0 open=22 cases=78` rc 0; `BATTERY cases=18 branch_cases=14 branch_open=0 harm=0 newopen=0` | operability (7) |
| C2 | `C2=unmet mutants=15 killed=12 survivors=3 unattributed=0 unanchored=0 isolated=0 literal_anchors=0 arms=28,26` rc 1 | `C2=met mutants=15 killed=15 survivors=0 unattributed=0 unanchored=0 isolated=0 literal_anchors=0 arms=29,27` rc 0 | calibration (5) |

Controls (committed before data, `.ufo/waves/round-90/evidence/controls-r90.txt`): do-nothing reads
both unmet; a gate that refuses every command reads `harm=37` (refusal-all is not a gain); the
three C2 labels without their arms read `survivors=3`; both counters' own selftests are green
(`pass=12`/`pass=21`). The landed subjects are byte-identical at `11197820` and at the tip
(`git diff --stat 11197820 HEAD -- .ufo/waves/round-87/count-c2.py .ufo/waves/round-88/` is empty).

Frozen-constant defect, disclosed: P-C2 froze `arms=29,27`, but B4 and B6 are both subjects of
`.ufo/waves/round-88/count-c2.py` and each declared mutant needs its own FAIL label, so a correct
landing there is 28 (`pristine-arms … arms=28 want=27`). The landing merges the only two
mutation-free constant pins (`arms_pinned`: `SUBJECT_ARMS == 26`; `marker_literal`: the
`missing-replay` label) into one `frozen_constants` arm that keeps **both** assertions —
26 + 2 − 1 = 27, no declared mutant touches either constant, no assertion lost. The critic
measured the weaker alternative (deleting `marker_literal`) also reaches 27; the merge is strictly
stronger and is recorded as QUALITY 190 and lesson mistake 1.

## Sources & frontier

Registry census command (same command at round start and round end):

```
/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin mori
```

- Round start (`d1c84889`): exit 0, warnings only (W04), 384 rows — `exit 0` was already true, so
  exit 2 (missing registry) did not apply.
- Round end (`0a1f019b`): exit 0, warnings only (W04 on S612–S615 for a shared URL across scopes),
  389 rows.

Rows added: 5, all tier A, all `status mined`, `recheck 90d`, `used-by corpus/knowledge/branch-reachability-r90.md`:

| Row | Source | Why admitted |
|---|---|---|
| S612 | POSIX.1-2024 §2.9.3 Lists | grounds the AND-OR short-circuit clause |
| S613 | POSIX.1-2024 §2.9.4.4 The if Conditional Construct | grounds the unselected if body |
| S614 | POSIX.1-2024 §2.15 `exit [n]` | grounds sequencing after `exit` |
| S615 | Python 3.15.2 `ast` | grounds walk-order-independent call-site pins |
| S616 | Python 3.15.2 `tokenize` | grounds reading the token stream for comments |

Rows touched old→new: 0 (no existing `status`/`recheck`/`used-by` change). Rejected this round:
`https://pubs.opengroup.org/onlinepubs/9799919799/utilities/exit.html` — HTTP 200 script-redirect
page with no specification text, so no quote could be located; flip condition recorded in the
lesson's `## Gate` block. Frontier rows advanced: the execution-binding family moves from
"token-level positions" (S611, round 89) to "control-flow positions" (S612–S614), and the
structural-pin family enters with S615/S616. The knowledge entry marks items 5–8 (`!`, loop
bodies, `break`, `case`) `[INFERENCE]`: no opened source states them and the held-out battery is
their only ground.

Tier counts after: A 349, B 19, C 21 (total 389).

Assimilation: none. `merge/mori/` was not taken (the claims are instrument repairs under the frozen
contract) and `considerthese/2026-10-26.md` proposal 1 was read but does not fit either claim.

## Trend verdicts

- **expansion — improved.** A new capability class (branch reachability over recorded command
  text) is in the gate with a held-out battery that grades it: `branch_open 8 → 0` on the frozen
  class, 0 of 14 held-out branch shapes still bound, and 22 provenance counterfeits reported as the
  measured limit. The frontier gained five sourced rows and one knowledge entry.
- **quality — improved.** `harm=0` and `newopen=0` on the 78-case population, on the 34-case r89
  no-harm battery and on the 18-case held-out battery; the gate's own 26-arm selftest stays green;
  the five glued-paren harms the reviewer measured were found and fixed before landing. C2's three
  kills are attributed and isolated (`killed=15 isolated=0 unattributed=0`), and the mutation probe
  reports 17 of 24 rule mutants killed on the landed bytes.
- **discernment — improved.** Two falsifications of the round's own assurance were taken into the
  record instead of being smoothed: the frozen `arms=29,27` was shown unreachable by a correct
  landing and the merge that reaches 27 is disclosed with its arithmetic (QUALITY 190); and the
  critic showed a 21-string lookup table reaches P-C1's frozen line, so the predicate grades
  verdicts, not rule shape (QUALITY 191, routed to r91 as a counter-synthesized guard). The
  structural nature of the B4/B6 pins and what they leave open is stated in the entry and the
  lesson (QUALITY 192).

## SHONEN

- `[~]` SKILL.md carries real decision tables and cited sources — `SKILL.md` round-90 registry
  pointer (landed `0a1f019b`), `corpus/QUALITY.md` 190–192, `corpus/knowledge/branch-reachability-r90.md`.
- `[~]` At least one end-to-end domain task executed and logged — `LOG.md` `## Round 90` (two
  counters, both met at `11197820`), receipts `.ufo/waves/round-90/evidence/{controls-r90,after-r90}.txt`.
- `[~]` Instructions executable by an agent without oral context — `python3 -I
  .ufo/waves/round-90/count-c1.py <rev> --repo <clone>` and `…count-c2.py <rev> --repo <clone>`;
  both replay a clone, honour `--scratch`/`HYAKU_SCRATCH`, and are cited with their exit codes.
- `[~]` No cross-domain bleed — `PROVINCE.md` unchanged; the knowledge entry's Limits section names
  what the rule cannot decide (provenance class, execution proof) and the round touched no
  dispatch, OS, or harness surface.

## Wave, seats and round shape

One v1 wave of **13 seats** under `ufo-wave-policy.json` (band 8–16), dispatched as one
`taskCall` from `.ufo/waves/round-90/w1-dispatch.json` via `.ufo/waves/round-90/w1.ready`;
attack seats 4/13 (2 reviewer, 1 critic, 1 mutation-tester = 31 %), connectors 1, no residual call.
Roles from `.ufo/waves/round-90/w1-results.json`: 4 executor (`Mo90E01Gate`, `Mo90E02ArmB1`,
`Mo90E03ArmsB46`, `Mo90E04Battery`), 1 scout (`Mo90Sc01Scope`), 2 scribe (`Mo90S01Sources`,
`Mo90S02Lesson`), 2 reviewer (`Mo90R01C1`, `Mo90R02C2`), 1 critic (`Mo90C01Critic`), 1
mutation-tester (`Mo90M01Mut`), 1 connector (`Mo90K01Conn`), 1 sentinel (`Mo90Se01Boundary`).
The L1 holds the canonical planner seat; the bounded planning data-walk rode `Mo90K01Conn`.
Round total: 13 seats, 0 dead.

Adopted vs re-verified from the dead attempt: adopted after re-verification — the contract, both
frozen counters, the controls script and its receipt, and the wave spec (three roles re-encoded
from JSON arrays, entering revision updated, L1 id changed); discarded — nothing (the inherited
byte set is unchanged in the landing except the spec, which is committed as both
`w1-spec.inherited.json` and `w1-spec.json`).

## Other required lines

- **Stale-lane:** respawn-per-round driver; no other mission of this lane is open.
- **Tool installs:** none this round (no `pacman` transaction; the pacman pause was honoured).
- **L0 questions:** none raised; nothing blocked on an operator decision.
- **Provider failures:** attempt 1 and attempt 2 of this lane-round died on provider errors before
  any report (the driver's markers moved this round here); no seat of this wave died.
