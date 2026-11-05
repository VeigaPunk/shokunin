# mori — round 95 report (attempt 2)

Lane `mori` · round 95 · L1 `MoriR95a2` (resumed the attempt-1 wave `w1`; attempt 1 ended without a report at 08:10:36).
Entering `754f4991198c16ddd1d4a3ea9206cfb7d74d6827` · freeze `2dc476d7fdb68bf916685a9f217a92047662baeb` · **landed
`155069fa86a44258e9231dbb89c514e73d2b7db8`** (`master`; `git ls-remote origin refs/heads/master` = `155069fa86a44258e9231dbb89c514e73d2b7db8`;
`merge-base --is-ancestor` verified). Lesson: `corpus/lessons/round-95.md`.

## Work performed

**Declared claims (2; frozen at `2dc476d7`, before any seat output):**

1. **C1 — calibration** (tied lowest non-retired axis; contract §C1). The round-94 admission battery kills the seven
   non-equivalent counter mutants m1, m1b, m2, m3, m4, m6, m7 with four added fixtures. Predicate: `C1=met survivors=0 killed=7/7`.
2. **C2 — operability, capability acquisition** (contract §C2). The counting surface runs with the account home absent
   (`unshare -rm`, tmpfs over home). Predicate `P-C2r95`: `HOSTINDEP hidden=1 before=C1=unmet(...) after=C1=met(rc=0) control_outside=C1=met(rc=0)`.

No exploratory claim. Frontier step: S626 mined, S627 rejected, one lesson with a `## Mistakes` table.

**Work items (evidence pointers):**

- Load order read: `skill://shokunin`, `PROTOCOL.md`, `MISSION.md`, `AXES.md`, `CORPUS.md`, `LEARNING.md`, lane `SKILL.md`,
  `PROVINCE.md`, `SCORECARD.md`, `corpus/lessons/round-94-verifier-spotcheck.md` §6 (routed items carried into the claims).
- Inherited wave `w1` re-verified, not re-dispatched: `.ufo/waves/round-95/w1.ready` (08:02), `w1.ready.dispatched` (08:03),
  `w1-dispatch.json`, `w1-spec.json`, `w1/swarm-registry.json`, `w1-results.json` (12 seats). Frozen pins re-checked:
  `count-c1.py` sha256 `6c288d70…aa450`, `count-c2.sh` sha256 `014980bc…44b9f`, pristine `count-c1v2.py` `6eb7fa4c…7b384`.
  Discarded: nothing. Reused: all wave outputs, as seat evidence.
- C1 before: `.ufo/waves/round-95/evidence/before-c1-r95.txt:1` (round-94 subset: `before_r94_survivors=4 r94_survivor_ids=m2,m3,m4,m6`).
- C1 after (landing re-run by the L1, not a seat): `.ufo/waves/round-95/evidence/landing-c1-r95.txt` →
  `C1=met survivors=0 killed=7/7 before_r94_survivors=4 … pristine=green equiv=m5(declared) crash_ids=-`, `exit=0`.
- C2 before: `before-c2-r95.txt:1` (`hidden=1 before=C1=unmet(rc=1) after=C1=met(rc=0) control_outside=C1=met(rc=0)`).
- C2 after (L1 re-run): `evidence/landing-c2-r95.txt` → same line, `exit=0`, `census_sha=3fb7261569f4 rev=2dc476d7fdb6`.
- Seat replays of the frozen bytes: `w1/Mo95E01Replay.md` (C1 and C2 identical, exit 0); `w1/Mo95R01Atk.md` (A1–A6, verdict HOLDS:
  one-change fixtures, revert-controls, forged counter rejected by the sha pin with exit 2, m5 equivalence over 20 pairs);
  `w1/Mo95R02Atk.md` (B1–B6, HOLDS: stub before rejected, stub after passes, mount-table leak check: none on host);
  `w1/Mo95K02Crit.md` (fresh C1 and C2 runs identical; six-axis harm check `NO-HARM`).
- Controls and discriminators: `w1/Mo95Lab01.md` (H1 supported; A0 positive control `C1=met`, A1 absent `rc127`, A3 failing stub
  `rc1`, A4 passing stub `C1=met`); `w1/Mo95E02Relo.md` (control A **survived** — a dormant literal fallback not on the invoked path;
  supplemental A2 forced-literal mutant exit 1; control B absent census `C2_SETUP` exit 2).
- Critic `w1/Mo95K01Crit.md`: K1 holds C1 is battery coverage, not a counted calibration mismatch (see §Trend verdicts);
  K3/K5 hold C2's do-nothing control is reached at entering. **The L1 agrees with both objections.**
- **Do-nothing defect (C2):** the entering repository already meets `P-C2r95` (K01 ran it at `754f4991`: `rc=0`; the L1 re-ran it at
  the freeze: `rc=0`). The round-93 before is pre-existing and unmet, and the round-94 after is pre-existing and met. The predicate
  does not discriminate round-95 work. This is a defect of the frozen claim, recorded and not amended after data.
- Sources (frontier step): scout `w1/Mo95S01Src.md` opened both pages; L1 re-opened both: `unshare.1.html` sha256
  `1df4f95f877112743581e8b0900ce1296dbc6155619f7b88232e076f27b7375e`; `user_namespaces.7.html` sha256
  `276480f2185f65ee9ca1402c233a53780dd558a77bcc30127bbb5bfafb1301b4`. Located quotes re-counted (count 1 each). The propagation
  sentence is absent from `user_namespaces(7)` (`mount operations` count 0).
- Assimilation: none (no `merge/mori/` theme taken; frozen predicates were the round's scope).
- Misroot sweep (see §Dead seats and sweep): nothing of round 95 at the fleet root.
- Scratch: all seat scratch deleted by seats; L1 scratch `/fast/scratch/hyaku/mori-r95/L1` removed after landing.

## Landed changes

| Change | Tied to | Commit |
|---|---|---|
| `corpus/lessons/round-95.md` (claims, Gate, Mistakes 1–5, routed items) | LOG.md Round 95 | `155069fa` |
| `corpus/QUALITY.md` criteria 205–208 (battery survivors; operability before; setup diagnostic; do-nothing control) | LOG.md Round 95 | `155069fa` |
| `corpus/SOURCES.md` rows S626 (`unshare(1)`, mined) and S627 (`user_namespaces(7)`, rejected) | LOG.md Round 95 | `155069fa` |
| `SCORECARD.md` round-95 section, claim table, capability row (`host-independent counting namespace`, harness-bounded, first-working 95), planned round 96 | LOG.md Round 95 | `155069fa` |
| `LOG.md` Round 95 entry | — | `155069fa` |
| `.ufo/waves/round-95/` (frozen contract, counters, before and landing receipts, spec, dispatch, registry, `w1-results.json`, `w1/` seat outputs) | the claims' evidence | `155069fa` |
| `.ufo/l0-questions.md` lines 342–344 (C1 ruling, C2 ruling, seat-death routing) | operator decisions | fleet commit (below) |

Lane commit: `155069fa86a44258e9231dbb89c514e73d2b7db8` (landed via `jj-lane.sh`; the diagnostic `rewritten aa27ee87…` is not cited).

## Before → after measurements

| Claim | Counting command | Before | After | Measured commit |
|---|---|---|---|---|
| C1 battery kills | `python3 -I .ufo/waves/round-95/count-c1.py 2dc476d7fdb68bf916685a9f217a92047662baeb --lane /home/vgpnk/Projects/shokunin/mori-shokunin --census /home/vgpnk/Projects/shokunin/scripts/sources-census.sh` | `before_r94_survivors=4` (m2,m3,m4,m6) — the do-nothing control, `evidence/before-c1-r95.txt:1` | `C1=met survivors=0 killed=7/7 pristine=green`, exit 0 — `evidence/landing-c1-r95.txt` | `2dc476d7` (frozen bytes unchanged in `155069fa`) |
| C2 home-hidden harness | `bash .ufo/waves/round-95/count-c2.sh 2dc476d7fdb68bf916685a9f217a92047662baeb /home/vgpnk/Projects/shokunin/mori-shokunin /home/vgpnk/Projects/shokunin` | round-93 counter in namespace `C1=unmet(rc=1)` — `evidence/before-c2-r95.txt:1` | `HOSTINDEP hidden=1 before=C1=unmet(rc=1) after=C1=met(rc=0) control_outside=C1=met(rc=0)`, exit 0 — `evidence/landing-c2-r95.txt` | `2dc476d7`; P-C2r95 also met at entering `754f4991` (K01, rc 0) |

## Sources & frontier

- SOURCES rows: **397 at entering** (`git show 754f4991:corpus/SOURCES.md | grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|'`) →
  **399 now** (same command on the working tree at landing).
- Census: `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin mori` **exit 0 at round start**
  (`.ufo/waves/round-95/evidence/census-before-r95.txt`) and **exit 0 at round end** (`mori ok`; W04 duplicate-URL warnings,
  pre-existing, no E-class finding after the lesson's `used-by` was written).
- Rows added by tier: S626 tier A (mined, cited by `corpus/lessons/round-95.md`); S627 tier A (rejected for the mount-propagation
  scope; flip condition on the row). Rows touched old→new: none.
- Frontier rows advanced: none (PROVINCE.md Frontier unchanged). Sourced claim: C2's mechanism cites S626 in the lesson.
- Considerthese: `considerthese/2026-10-26.md` carries four unimplemented proposals; none taken this round (one per round allowed; deferred).
- Assimilation: none.

## Trend verdicts

- **expansion: unchanged.** No admitted `knowledge/` entry this round. Two registry rows only (S626 mined, S627 rejected); CORPUS rule 4.
- **quality: improved.** QUALITY 205–208 added, each grounded and shown able to fail (lesson table). The frozen battery's named
  set moved 4→0 survivors. Residuals m8, m10, m11 and the kill-rule doc/code mismatch are named, not hidden (K02 H4; `count-c1.py:212`).
- **discernment: unchanged.** Non-author critic K01 disagrees with the C1 axis classification; that is an open operator ruling (L0 line 342),
  not resolved here. The C2 do-nothing defect was caught by a non-author critic (K01 K5), not by the L1.

## Dead seats and sweep

Wave `w1`, one v1 wave, 12 seats: executor 2 (`Mo95E01Replay`, `Mo95E02Relo`), scout 1 (`Mo95S01Src`), scribe 1 (`Mo95Sc01Lesson`),
reviewer 2 (`Mo95R01Atk`, `Mo95R02Atk`), critic 2 (`Mo95K01Crit`, `Mo95K02Crit`), mutation-tester 2 (`Mo95M01Mut`, `Mo95M02Mut`),
labrat slot 1 (`Mo95Lab01`, recorded as agent `revenger`), connector 1 (`Mo95Conn01`). Attack share planned 7/12 (58 %); delivered 5/12
(42 %), still ≥25 %. Connector 1. No residual call. Planner held by the L1 by disclosure (validator refuses `planner`; L0 D1 open with operator).
The `results.json` records no per-seat route beyond agent names; actual answering models were not recorded.

**Dead or incomplete seats (named, not replaced — protocol: never replace a dead seat):**

- `Mo95M01Mut` (mutation-tester): **dead, provider limit** (orchestrator notice). Last output ended mid-narration ("Two findings shape the sweep…"); no report file.
- `Mo95M02Mut` (mutation-tester): **dead, zai 429** (orchestrator notice). Last output ended mid-narration ("Pristine baseline: exit 0…"); no report file.
- `Mo95Sc01Lesson` (scribe): **dead, provider limit** (orchestrator notice). Its file is an incomplete draft with pending verdicts; the L1 wrote the lesson itself and used the draft only for the quoted criteria pointers.
- `Mo95K01Crit` (critic): report file `w1/Mo95K01Crit.md` complete (K1–K6, `SEAT Mo95K01Crit PASS`); **final yield empty**; used as evidence, disclosed as a yield-only failure.

The mutation-testers' sweep therefore did not land. Coverage of mutants is the frozen seven plus K02's residuals and E02's dormant-literal control.

**Misroot sweep:** `git -C /home/vgpnk/Projects/shokunin status --porcelain` before this report:
` M .scratch/run15-state.json` (orchestrator-owned), ` M .ufo/l0-questions.md` (other lanes' appends; this lane appended lines 342–344),
`?? .ufo/waves/round-68/` (another lane's round). **No round-95 seat file sits at the fleet root; nothing moved.**

**Host and tools:** no tool installed or upgraded; no pacman transaction; no sudo; no host sysctl changed.
`/proc/sys/user/max_user_namespaces` = 122865 (read-only here; the labrat and K02 read it). Namespace availability is host configuration.

**Stale-lane:** none (respawn-per-round driver; no other mission of this lane is open).

**Attempt note:** attempt 1 (`MoriR95`) dispatched `w1` and settled the wave, then ended without a report at 08:10:36 (`watchdog.log`
`lane-dead-no-report mori round=95`). Attempt 2 re-verified the frozen pins and the wave outputs, reused them, and landed the round.

**Open L0 questions this round** (appended to `.ufo/l0-questions.md`): C1 axis ruling; C2 do-nothing and capability-row ruling; seat-death routing.

## SHONEN

[~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — `SKILL.md` (decision table; error patterns);
`corpus/QUALITY.md` 205–208 (round 95) added on top of the round-94 criteria.
[~] At least one end-to-end domain task executed and logged in LOG.md — `LOG.md` Round 95 entry; the C1 and C2 landing re-runs
in `.ufo/waves/round-95/evidence/landing-*.txt`; the lesson `corpus/lessons/round-95.md`.
[~] Instructions executable by an agent without oral context — `python3 -I .ufo/waves/round-95/count-c1.py <rev> --lane <lane> --census <census>`
and `bash .ufo/waves/round-95/count-c2.sh <rev> <lane> <fleet>` (exact commands in this report and the lesson).
[~] No cross-domain bleed (PROVINCE.md still accurate) — `PROVINCE.md` Adjacent; the C2 harness reads only its own clone and the fleet
census copy; the sibling host-literal class is routed to the operator (L0), not edited.

## Final

Lane HEAD `155069fa86a44258e9231dbb89c514e73d2b7db8`. Report commit: fleet repo, `fleet-commit.sh --as mori`. Claims: C1 met as frozen,
calibration not admitted (non-author disagreement); C2 met as frozen, operability not admitted (do-nothing control reaches the predicate),
capability row entered with its harness bound. No axis harmed (critic K02, six-axis check).
