# mado — round 46 report (hyaku run 9, attempt 1)

Lane repo `/home/vgpnk/Projects/shokunin/mado-shokunin`, branch `master`, final lane hash **`edc147898e9de3c4e40f003277f20dbf67f18956`** (`git ls-remote origin refs/heads/master` prints it). Base `b22ea56bff2faec39ce9ff75d2107eaf4612ecbe`. Round shape: **one v2 wave** `w1` of **66 seats** (policy v2, band 64-128), build and attack items together: executor 18, critic 15, scribe 9, reviewer 6, connector 5, mutation-tester 4, scout 4, sentinel 3, simplifier 1, revenger 1. Attack roles (critic, reviewer, mutation-tester) 25/66 = 38 %; m_flash roles (executor, critic, scribe, sentinel, simplifier, revenger) 47/66 = 71 %. `labrat` is not a swarm role in the validator, so the four planned falsification probes ran as critics. Dead seats **0**: all 66 wrote reports (`.ufo/waves/round-46/w1/*.md`), and `w1-results.json` holds 66 outputs. No residual call. **Round total 66.** The L1 held the planner seat; no data-walk rode on another seat.

## Work performed

Declared claims (`.ufo/waves/round-46/registration.md`, freeze `8c5434c6`; re-registered before any data as `registration-v2.md`, freeze `2bcc335f`, and C1 again as `registration-v3.md`, freeze `7f793280`):
- **C1 — operability (capability acquisition): `tools/mado-devices.py`.** It is a read-only join of the `input` and `device` config with `hyprctl devices -j`. Judged by `PRED-C1-r46-v3`.
- **C2 — coverage (sourced): `corpus/knowledge/hyprland-input-devices-r46.md`.** It traces the chain from `input { kb_* }` and `device { name = X }` to what the dump prints, on Hyprland 0.56.2 with hyprlang 0.6.8. Judged by `PRED-C2-r46-v2`.

Lowest-axis rule: at base every published axis sat tied at its maximum (`receipts/axis-base.txt`, `checked=3 mismatched=0`). Paths below are under `mado-shokunin/.ufo/waves/round-46/`.

- **Pins.** Ten pins were fetched and opened on 2026-10-26 (`fetch/`, `receipts/fetch-sha256.txt`). `w1/ScoutRecheck.md` re-fetched all ten the same day and found them byte-identical.
- **v1 freeze with controls.** C1 controls: 0 of 23 met (`receipts/ctl-c1.txt`). A pre-freeze run had met V03, so I added the fixture `case-exact-dump-name` before the freeze. C2 controls: P admitted, 14 rejected (`receipts/ctl-c2.txt`). The C2 harness first stopped on its own URL assertion before scoring anything; that is M46-2.
- **w1 broke C1 v1:**
  - a 12-line delegator met it (`w1/CritClaimSizing.md` F2);
  - three cheat tools met it (`w1/CritC1Cheat.md` A-C);
  - clause r was bypassed (`w1/SentTool/findings.md` F1/F2).
- **w1 found the v1 contract wrong against Hyprland and hyprlang:**
  - strtof single rounding, hex, `inf` and out-of-range values (`w1/ExecStofOracle.md` D1-D7);
  - a final continuation line, checked against the host's real hyprlang library (`w1/ExecHyprlangOracleB.md`);
  - the directive trigger, `source =` inside a block, and the VT/FF strip (`w1/CritToolSemantics.md` F1/F2).
- **w1 broke C2 v1:** six forgeries were admitted outside the declared residuals (`w1/CritC2Forgery.md` F4-F10), and the T4 token list was missing `OK` (`w1/RevC2Counter.md`).
- **Entry prose defects were fixed in the v2 draft:** `w1/ExecC2Census.md` D1-D5 and `w1/CritEntryContent.md` H1-H8.
- **v2 freeze** `2bcc335f`:
  - C1 got an allowlist bubblewrap root (only /usr and /etc), 110 fixtures, and the v2 reference with selftest 59/59.
  - C2 got clause k (A-G) and the `OK` token. C2 controls passed: `CTL_C2v2 VERDICT: PASS (wrong=0 of 22; positive admitted=1)` (`receipts/ctl-c2-v2.txt`).
  - C1 failed its own controls: `CTL_C1v2 VERDICT: FAIL (controls scoring TARGET_MET: 2 of 40 ...)` (`receipts/ctl-c1-v2.txt`). The tripwire was an inherited pipe, and the tool's own subprocess closes inherited fds.
- **v3 freeze** `7f793280` (C1 only): the tripwire moved to a unix socket. Result: `CTL_C1v3 VERDICT: PASS (controls scoring TARGET_MET: 0 of 40; reference met: 1)` (`receipts/ctl-c1-v3.txt`, commit `fb6a1fee`).
- **Separability, both ways:** a tool-only tree meets C1 and misses C2; a data-only tree misses C1 and meets C2 (`w1/ExecC1Separability.md`).
- **Two independent rebuilds** met C1 v1 from the contract text alone (`w1/ExecIndepA.md`, `w1/ExecIndepB.md`).
- **Round-45 closure items:**
  - D1: 11 w2 seats attacked the round-45 data (`w1/ExecW2Monitors.md`: 5 nonces `81/81 + 150/150`, 22/22 adversarial configs; `w1/CritW2Entry.md`, `w1/CritW2Gate.md`, `w1/RevW2Rows.md`, `w1/MutW2Tool.md`, `w1/SentW2Privacy.md`).
  - D2: corrected in M46-10.
  - D3: registry row landed; triage of 97 findings: 15 real, 82 synthetic.
  - D4: digest committed.
  - D5: noted in the lesson.
  - D6: open.

## Landed changes

| Commit | Change | LOG.md Round 46 bullet |
|---|---|---|
| `8c5434c60e03f147ee1f75ab195e8bc3f0db4dec` | v1 freeze: registration, reference, counters, fixtures, pins, before receipts | 2 |
| `e0be61e4f6e34896f8b1c329f9c6d129e5af81f7` | v1 controls at freeze, C2 harness fix, w1 spec and dispatch (66 seats) | 2-3 |
| `2bcc335f236c950fded185a6e7d00c0cda5d80c7` | v2 freeze before data (C1 v2 counter, 110 fixtures, v2 reference; C2 v2 counter; v2 entry draft) | 4 |
| `7f7932807135f18722072210412a343d8824e789` | v2 control receipts, C1 v3 freeze, w1 evidence (66 reports, results), round-45 D4 digest | 4 |
| `fb6a1feec98afbf9319b99aff88a83af47e20b69` | C1 v3 control receipt (PASS) | 4 |
| `1001bda0472f1fdc0679fb88ced5d159f5d32c62` | **data**: tool, entry, rows S316-S325, lesson, README row + Frontier, SKILL section + `mado-session-material` registry row, PROVINCE refinement, QUALITY 87-90, live receipt | 5 |
| `9879964fee960f162dd334897b03fa7d352bb693` | SCORECARD/LOG Round 46, after-data receipts | 5 |
| `edc147898e9de3c4e40f003277f20dbf67f18956` | tip receipts (axis, C1, C2) | 5 |

Inherited state: one untracked round-45 leftover. `.ufo/waves/round-45/w1/MutC1Counter/results.json` (4 MB) was removed and its digest committed (D4). The worktree held no other leftovers.

Left untracked: `.ufo/waves/round-46/w1/ExecStofOracle/receipts/out.json.rows.tsv` (3.3 MB). The helper skips new files over 1 MiB inside a named directory. The seat's `report.md` and `out.json` summary are committed.

## Before → after measurements

- **C1:** `cd /home/vgpnk/Projects/shokunin/mado-shokunin && python3 -I quality/counters/c1-r46-devices-v3.py --repo . --rev <rev> --work <scratch>`
  - Base `b22ea56`: `fixtures=0/110 generated=0/150 selftest=fail readonly=fail tool=absent verdict=TARGET_MISSED`, exit 1 (`receipts/c1-v3-before-base.txt`).
  - Data `1001bda`: `fixtures=110/110 generated=150/150 selftest=ok readonly=ok tool=present verdict=TARGET_MET`, exit 0 (`receipts/c1-after-data.txt`).
  - Tip `9879964`: the same MET under a fresh nonce (`receipts/c1-tip.txt`).
  - Self-verdict **TARGET_MET**.
- **C2:** `cd /home/vgpnk/Projects/shokunin/mado-shokunin && python3 -I quality/counters/c2-r46-input-device-entry-v2.py --repo . --rev <rev>`
  - Base: `admitted=0/1 verdict=TARGET_MISSED`, exit 1 (`receipts/c2-v2-before-base.txt`).
  - Data `1001bda`: `admitted=1/1 verdict=TARGET_MET`, exit 0 (`receipts/c2-after-data.txt`); the same at the tip (`receipts/c2-tip.txt`).
  - Self-verdict **TARGET_MET**.
- **Harm watch:** `python3 -I quality/check-axis-scores.py --rev 9879964… --repo .` gives `MADO_AXIS: checked=3 mismatched=0` (navigation 63/63, calibration 77/77, operability 12/12; `receipts/axis-tip.txt`). The data commit reads STALE in the declared two-phase window (`receipts/axis-data.txt`).
- **Live host run** of the landed tool: `receipts/live-devices-host-r46.txt`, `keyboards=10 agree=9 ... virtual=1 mice=4 ... verdict=OK`, exit 0, selftest 59/59.

## Sources & frontier

Census `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin mado`:
- Round start (`receipts/census-before.txt`): W04 and W01 warnings, `mado ok`, exit 0.
- Round end (`receipts/census-after.txt`): the same plus five new W04 lines (S317, S318, S320, S321, S324 reuse held URLs under new scopes), `mado ok`, exit 0.

Changes:
- **Rows:** 252 → **262**, counted with `grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`.
- **Added by tier:** A ×10 (S316-S325: 9 code, 1 docs), all `mined`, opened 2026-10-26. Gate lines are in `corpus/lessons/round-46.md` `## Gate`.
- **Rows touched old→new:** none (held rows S018, S158, S162, S173, S182, S215, S303, S307 unchanged).
- **Frontier advanced:** `corpus/README.md` Frontier has a new bullet, "Round 46 moves the input-device plane onto sourced ground". Knowledge entries 62 → 63.
- **Sourced claim:** C2 rests on S316-S325, opened this round.
- **Assimilation: none.** No `merge/mado/` theme touches the plane (`w1/ScoutShokuknow.md`, `w1/ExecIdGuard.md`: 42 themes, 0 admit). The staged id block S203-S349 collides with 60 registry ids, so any later adoption must renumber by document first.
- **Mistakes mined:** M46-1..16 (`corpus/lessons/round-46.md` `## Mistakes`). They land as QUALITY 87-90.
- **considerthese:** `considerthese/2026-10-26.md` proposal 3 (age count per routed defect) became QUALITY 90 and `w1/ScrRoutedAges/ages.md` (15 open items, oldest 8 rounds).

## Trend verdicts

- **expansion: improved.** One capability: input-device config versus running devices, with SCORECARD Round 46 capabilities and the live run. One entry on ground absent at base (resolution-chain grep exit 1, `receipts/c2-ground-base.txt`). Rows 252 → 262.
- **quality: improved.**
  - The round-45 data finally got its falsification wave: 11 seats, round-45 D1.
  - Both round-46 instruments were broken by w1 and re-registered before data.
  - The C1 v2 counter was caught by its own controls before data.
  - The landed contract is checked against the host's real hyprlang library and a strtof oracle.
  - Limit: the round-45 entry's six non-supported sentence units are only recorded, not yet corrected (planned round 47).
- **discernment: improved (self-assessed, pending the non-author closure).**
  - Withdrawn on evidence: the lane's own v1 predicates, then its v2 C1 predicate (M46-15).
  - Corrected in the registration erratum: the registration's own count (two W04 repeats became five, M46-1).
  - Recorded as refusals: 19 rejected source candidates (lesson Gate).
  - Reported as mistakes, not hidden: the slipped S290-S297 supersession (M46-16), and the 18 synthetic session-material findings in this round's seat files.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources. New section "Input-device rules versus running devices (round 46)" with a verdict table and the `mado-session-material` registry row (`SKILL.md` tail, commit `1001bda`). No non-author verifier.
- [~] At least one end-to-end domain task executed and logged. Live read-only host run of the landed tool: `.ufo/waves/round-46/receipts/live-devices-host-r46.txt` (9 AGREE, 1 VIRTUAL, OK, exit 0); LOG.md Round 46. No non-author verifier.
- [~] Instructions executable by an agent without oral context. Two seats rebuilt passing tools from the contract text alone (`w1/ExecIndepA.md`, `w1/ExecIndepB.md`). Dispatched seats are not outside-lane verifiers.
- [~] No cross-domain bleed (PROVINCE.md still accurate). PROVINCE round-46 refinement; `w1/ConnSiblings.md` for sibling overlap. No non-author verifier.

Stale-lane: respawn-per-round driver; no other mission of this lane is open.

Tool installs: none. python3, git, curl, g++, bwrap and libhyprlang 0.6.8 headers were already present. Seats report none.

Misroot sweep: `git -C /home/vgpnk/Projects/shokunin status --porcelain` printed nothing. No seat file landed in the fleet root.

Session material: `quality/check-session-material.py` at `1001bda` reads `findings=115`, exit 1 (`receipts/session-material-data.txt`).
- 18 findings sit in round-46 seat files; all are synthetic gate fixtures.
- A grep for the host monitor serial over the whole wave dir finds 0 files.
- The marker layer that would waive synthetic fixtures is drafted but not installed (planned round 47).

Open L0 questions: none filed. Carried note for the operator: the host monitor serial is in three held entries and 21 wave files from rounds 32/37 (M46-10). Removing it from pushed history is the operator's decision.
