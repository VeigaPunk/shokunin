# mori — round 100 report (L1 MoriR100, attempt 1)

Lane repo `mori-shokunin`, branch `master`. Entering `d1bd1b339b894de0249b0f60702dff9962da88d9` → final
`79c673bfc794c86a4c0b3da81c82f9e904d8413f` (`git ls-remote origin refs/heads/master` → `79c673bf…`). Not a fresh-start
round (r97, r98, r99 admitted); the r99 spot-check routed defects D1–D4 were read first. No earlier attempt
(`.ufo/watchdog.log`: only `launch mori round=100 … attempt=1`); nothing inherited. Every claim was frozen with its
controls executed and committed first (`.ufo/waves/round-100/evidence/controls-r100.txt`, `CONTROLS_DONE unexpected=0`).
**Outcome: both claims miss as frozen.** C1's kill rule fires on unlucky seeds (a counter defect); C2 was met at
landing and then withdrawn because its fix broke CORPUS rule 2. The C1 capability landed and was verified on live data.

## Work performed

Declared claims (2): **C1 coverage** (score 6): the seat terminal census `tools/mori-seat-terminal.py` names
credential and entitlement deaths `dead_auth` (HTTP 401/403 or an auth spelling, read after Z.AI codes, quota and rate
evidence). Sourced: S637, S638, opened this round. **C2 calibration** (score 5, lowest tier): stated quote word counts
in `corpus/SOURCES.md` match their quotes.

- Motivating data walk (counts only, no message text): in the two days before the round, 187 of the 190 terminal
  errors that the round-99 rules file as `dead_error_other` carry 401/403 or an auth spelling
  (`.ufo/waves/round-100/evidence/live-errors-prefreeze.txt`, probe `probe-live-errors.py`).
- Sources opened and pinned (`corpus/evidence/sources-r100/`): Connect protocol (S637), gRPC status codes (S638),
  RFC 9110 text for §15.5 (S639).
- Freeze `9579cff6`: contract, counters `count-c1.py` / `count-c2.py`, controls runner, candidate tool, round-17 gate,
  knowledge entry, transforms. C1 controls K0–K8 included a template-lookup forgery (K5), per QUALITY 212. C2 controls
  were K0c–K5c. Every control behaved as expected on the first run.
- Landing `5e2bcf2c`: `tools/mori-seat-terminal.py` (`dead_auth`, 4 `auth-*` self-test arms, 53 arms in total),
  `tools/mori-round17-seat-regressions.py` (the class is added to its key set),
  `corpus/knowledge/seat-auth-deaths-r100.md`, S637/S638, the SKILL.md registry rows, and the C2 corrections appended
  inside rows.
- Wave w1 (12 seats, 0 dead, `.ufo/waves/round-100/w1/`):
  - live trial on 4741 real transcripts: the only transition is `dead_error_other` → `dead_auth`, on 22 seats (`Mo100ExecTrial.md`);
  - replays on seeds 1, 7, 10, 11, 17, 42, 51, 52, 100, 2026 and unseeded (`Mo100ExecReplay.md`);
  - review: info-level findings only (`Mo100RevC1.md`);
  - held-out records: 22/26 right at landing, 14/26 at entering (`Mo100CritC1.md`);
  - 32 mutants: 26 killed, 1 equivalent, gaps G1–G5 (`Mo100MutC1.md`);
  - harm sweep across 10 registered self-tests and gates (`Mo100RevHarm.md`);
  - C2 re-derivation and attacks (`Mo100RevC2.md`, `Mo100ExecCalib.md`, `Mo100CritC2.md`);
  - consumer scan (`Mo100ConnSibling.md`), sources (`Mo100ScoutSrc.md`), lesson draft (`Mo100ScribeLesson.md`).
- Post-landing repairs, outside the frozen measurement:
  - `878708b3`: C2 in-row edits reverted (rule 2); S639 replaces the S221 `used-by` re-point (S221 is scoped to
    §15.4); S640 supersedes S634 (17→18); QUALITY 213 and 214.
  - `a7951675`: S641–S644 supersede S581–S584, which clears the append-only gate's `stale_supersede`.
  - `6a1fc283`: capitalised `Quota`/`QUOTA` now win over a 403 (held-out H03/H04); self-test 53 → 54.
- Planner seat: held by the L1, because the validator refuses `planner`. The planning data-walk (the live probe and the
  word-count probe) was done by the L1 before the freeze.

## Landed changes

| commit (`jj-lane.sh` `landed`) | content | LOG.md entry |
|---|---|---|
| `9579cff6cfab2f06b1918e54aec4a5553b705a9c` | freeze: contract, counters, controls + receipt, candidate, befores, census-before, live probe, pinned S637/S638/RFC 9110 | Round 100 |
| `5e2bcf2c487e377b51287c587144bdde5b233f8f` | landing: seat terminal `dead_auth`, round-17 gate, knowledge entry, S637/S638, SKILL rows, C2 in-row corrections (later reverted) | Round 100 |
| `878708b3e50347fd1168c7b7c2dd0972fb216581` | C2 revert; S639, S640; knowledge re-point; QUALITY 213–214 | Round 100 (post-landing fixes) |
| `a79516754f52232e12ebab5bdf9af5d88e143a03` | S641–S644 correction rows + pins | Round 100 (post-landing fixes) |
| `6a1fc283f632e6ef37d8b158ac255e9a2567e66d` | capitalised quota spellings, 54-arm self-test, SKILL row, knowledge limits | Round 100 (post-landing fixes) |
| `dc9c9fedd2ea6cc66fc20f8f28c5dc3ecf441d15` | lesson, LOG, SCORECARD verdict + Planned r101, wave evidence (spec, validator, dispatch, `.ready`, `.ready.dispatched`, results, 12 reports), receipts | Round 100 |
| `79c673bfc794c86a4c0b3da81c82f9e904d8413f` | final receipts (census-after, final-c2, append-only gate), lesson census close | Round 100 |

## Before → after measurements

| claim | command | before (`d1bd1b33`) | landing (`5e2bcf2c`) | final (`dc9c9fed`) | verdict |
|---|---|---|---|---|---|
| C1 | `git -C mori-shokunin archive <rev> \| tar -x -C DIR` → `python3 .ufo/waves/round-100/count-c1.py --root DIR --seed N --work S` | `C1=unmet cases_ok=23/50 … checks_failed=battery,registry,sourced` (`evidence/before-c1.txt`) | seeds 100, 7: `C1=met cases_ok=50/50 … checks_failed=-` (`evidence/landing-c1.txt`); seeds 10, 11, 42: `C1=unmet cases_ok=49/50` (`evidence/landing-c1-killrule.txt`) | same pattern (`evidence/final-c1.txt`) | **unmet**: frozen kill rule "any family failing on any seed" |
| C2 | `python3 .ufo/waves/round-100/count-c2.py --root DIR` | `C2=unmet stated=58 mismatches=7 uncorrected=7` (`evidence/before-c2.txt`) | `C2=met stated=60 … uncorrected=0 spurious=0 altered=0 census=ok` (`evidence/landing-c2.txt`) | `C2=unmet stated=66 mismatches=7 uncorrected=7 … census=ok` (`evidence/final-c2.txt`) | **met as frozen, withdrawn** |

**C1.** Every C1 miss has the same cause: an auth case whose random counter tail (`request id r-18429`,
`[trace 34291]`) holds `429`. The round-17 rule reads that substring as rate evidence, and the tool applies its
documented precedence. So the planted label is wrong, not the tool. The frozen rule still binds, and I report C1 as
unmet. The pre-freeze controls had run one clean seed (lesson Mistake 7).

The capability itself is verified:
- live: 22 seats moved, no other transition (`w1/Mo100ExecTrial.md`);
- the 66 round-17 fixtures pass on both the landed tool and gate;
- self-test 54/54.

The substring hazard predates this round; it is routed to round 101.

**C2.** The correction was appended inside immutable anchor cells. CORPUS rule 2 says "A correction is a new row whose
`teaches` opens `supersedes S0NN —`". Six of the seven mismatches were already superseded in round 72, by S586, S587
and S585. The landing tripped `tools/mori-sources-appendonly.py --round-base`:
`round_changed=[S581,S582,S583,S584,S634]`, `stale_supersede=[S581,S582,S583,S584]` (`w1/Mo100RevHarm.md`).

The repair reverted the edits and corrected the rows the rule-2 way (S640–S644). At the final tip the plain gate reads
`appendonly_violations=50 round_changed=[] stale_supersede=[]`, the same as at entering
(`evidence/appendonly-final.txt`). Disclosed residual: the `--round-base d1bd1b33` form keeps listing the five ids,
because they are in the edit history.

## Sources & frontier

- Census: `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin mori`.
  - Start: `mori ok`, exit 0, 44 W04 (`evidence/census-before.txt`).
  - End: `mori ok`, exit 0, 50 W04 (`evidence/census-after.txt`). The six new W04 are S639–S644, which reuse URLs under
    a different scope (correction rows, the S585–S587 practice).
  - Intermediate commits `878708b3`–`6a1fc283` carry census E11, because the lesson they cite in `used-by` landed only
    at `dc9c9fed`.
- Rows: 408 → 416 (`git show <rev>:corpus/SOURCES.md | grep -cE '^ {0,3}\| *S[0-9]{3,}'` at `d1bd1b33` / `dc9c9fed`).
- Rows added by tier: A ×8.
  - S637, S638, S639 (spec): `mined`, used by `corpus/knowledge/seat-auth-deaths-r100.md`.
  - S640 (spec) and S641–S644 (docs): correction rows superseding S634 and S581–S584, used by the lesson.
  - All were opened 2026-11-05 by the L1; their quotes were counted by command.
- Rows touched old→new at the final tip: none. Every row's bytes are unchanged except the eight appended ones
  (`git diff d1bd1b33 79c673bf -- corpus/SOURCES.md` adds rows only). The landing's transient S221 `used-by` change and
  the five anchor-cell edits are logged in the lesson's Gate block.
- Frontier advanced: the death-cause surface of the seat census now separates credential/entitlement refusals from
  unknown errors. The new ground is grounded in RFC 9110 §15.5, the Connect code-choice rule and the gRPC status table.
- Sourced claim: C1 rests on S637/S638 (counter conjunct `sourced=met(S637,S638)`).
- Mined mistakes: 7 (`corpus/lessons/round-100.md` `## Mistakes`), each with how its fix is shown able to fail.
- Gate admits: S637–S644. Gate rejects:
  - re-pointing S221 by `used-by` alone;
  - Connect's 429 → `unavailable` mapping as the rate rule;
  - the in-row correction form.
- Assimilation: none (no `merge/mori/` theme fits). considerthese: `considerthese/2026-11-05.md` proposals 1–5 read,
  none taken.
- r99 routed defects:
  - D1 → S640, the rule-2 form. The spot-check's in-place advice was the cause of lesson Mistake 5.
  - D2 → this round's counter design (composed families, control K5).
  - D3 and D4 carried.

## Trend verdicts

- **expansion: improved** — one new knowledge entry on ground the lane did not hold
  (`git grep -c dead_auth d1bd1b33 -- corpus/knowledge SKILL.md PROVINCE.md` → no hit; `corpus/knowledge/seat-auth-deaths-r100.md`
  at the tip). Every `source:` line cites a `mined` row opened this round (S637, S638, S639).
- **quality: improved** — a registered probe now names the dominant real death cause of 2026-11-04/05:
  - live, 22 seats moved `dead_error_other` → `dead_auth` with no other transition (`w1/Mo100ExecTrial.md`);
  - held-out records right 22/26 at landing vs 14/26 at entering (`w1/Mo100CritC1.md`);
  - registered self-tests equal or additive (`w1/Mo100RevHarm.md`).

  Tempered: the C1 counter is defective (Mistake 7), and the C2 landing broke a CORPUS rule before it was repaired.
- **discernment: improved** — the round published its own counter defect and its own rule-2 breach, repaired the
  breach the CORPUS way, withdrew a met-as-frozen claim instead of keeping it, and mined seven mistakes. Four of them
  were found by the wave after landing.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — `SKILL.md` seat-terminal registry row (round-100 dead classes and precedence, 54-arm self-test) and r17 gate row; `corpus/knowledge/seat-auth-deaths-r100.md` Rule table; `corpus/QUALITY.md` 213–214
- [~] At least one end-to-end domain task executed and logged in LOG.md — `LOG.md` Round 100 (live trial over 4741 real transcripts, `w1/Mo100ExecTrial.md`)
- [~] Instructions executable by an agent without oral context — `python3 tools/mori-seat-terminal.py --selftest` → `arms 54 passed 54`; `python3 .ufo/waves/round-100/count-c1.py --root DIR --seed N` reproduced on seeds 1, 7, 10, 11, 17, 42, 51, 52, 100, 2026 by `w1/Mo100ExecReplay.md`
- [~] No cross-domain bleed (PROVINCE.md still accurate) — `corpus/knowledge/seat-auth-deaths-r100.md` Boundaries (re-login, key rotation and routing are the operator's); `w1/Mo100ConnSibling.md` (no sibling reader edited)

## Round shape and seats

- Shape: one v1 wave `w1` under `ufo-wave-policy.json` (band 8–16), 12 seats.
- Role mix: scout ×1, connector ×1, executor ×3, scribe ×1, reviewer ×3, critic ×2, mutation-tester ×1. Attack seats:
  6/12 (50 %).
- Round total: 12; no residual call. Dead seats: 0 (all 12 reports present; `w1-results.json` `seats: 12`).
- Misroot sweep: one untracked fleet-root file (`w4lines.txt`), not written by a mori seat; none moved.
- Conduct: no seat ran sudo or mutated a sysctl. Transcripts were read through the tool or as counts only.
- Open L0 questions: none new (carried: mori | round-94, round-95, round-96).
- Tool installs: none (the L1 and every seat report none).
- Stale-lane: respawn-per-round driver; no other mission of this lane is open.
