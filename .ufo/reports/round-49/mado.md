# mado — round 49 report (hyaku run 9, attempt 1)

Lane repo `/home/vgpnk/Projects/shokunin/mado-shokunin`, branch `master`, final lane hash **`8a370cd481c6044b2f5c09fd66acde8fc54d173c`** (`git ls-remote origin refs/heads/master` prints it). Base `03e4ae76aff7a4be59cb69970dd553baa319695a`. Round shape: two v1 waves planned. Only `w1` (build, 45 seats) was dispatched. Wave `w2` (38 attack items drafted in `.ufo/waves/round-49/w2-items.json`) was **never dispatched**: the L1's request budget ran out. **Round total 45 seats**, below the 64 floor; this is a conformance defect (M49-4). WAVE-DONE for w1 had not arrived when the report was filed: 38 of 45 seat reports had landed, and 7 seats were still running (ExecControlsC1, ExecSessionTriage, ScoutHyprBinds, CritPremiseC1, CritPremiseC2, CritRoutedItems, SentPrivacy). The budget notice forced the report before that message arrived, which is disclosed here as a defect.

## Work performed

Declared claims (`.ufo/waves/round-49/claims.md`, commit `5f37c1b8`):
- **C1** — operability, capability acquisition: `tools/mado-keysym.py` reproduces `xkbcli how-to-type --keymap=FILE --disable-compose --keysym ARG` (libxkbcommon 1.13.2).
- **C2** — coverage, sourced: `corpus/knowledge/hyprland-bind-key-match-r49.md` (how Hyprland 0.56.2 matches a bind's key field).

Lowest-axis rule: every published axis tied at its maximum at base (`checked=3 mismatched=0`), and the round-48 closure ruled all three trends `improved`. Paths below are under `mado-shokunin/.ufo/waves/round-49/` unless rooted.

- **w1 build (45 seats).**
  - Two independent C1 references:
    - `w1/ExecRefKeysymA` is the landed tool, selftest 38/38.
    - `w1/ExecRefKeysymB` is the independent check. The L1 ran it against the judge: 0 mismatches in 57,865 random (keymap, keysym) pairs over 400 random RMLVO keymaps.
  - Keysym names: `w1/ExecKeysymNames` (10,613 argument forms, 0 differences).
  - Counters: `w1/ExecCounterC1` (633 fixtures from `w1/ExecFixtures`), `w1/ExecCounterC2`, mutation-tested by `w1/MutCounterC1Draft` (all five clauses killed).
  - C2 source trace and live capture: `w1/ExecHyprSrc` (78/78 quotes verified), `w1/ScrEntry`, `w1/ScrRows`, `w1/ExecBindsLive`.
  - Host safety: `w1/SentHost` H1–H10.
  - Routed items: `w1/ExecSessionShapes` (gate v3 draft, selftest 94/94), `w1/ExecMutantSandbox` (host guard shown to fail on a fake home), `w1/ExecN4Matrix`, `w1/ExecCloneRecipe`, `w1/ScrCorrections`, `w1/CritSidecars`.
- **Freeze `dd2e827e`** (`registration.md`). The w1 counter drafts plus these L1 edits:
  - C1 compiles with `--include=/usr/share/xkeyboard-config-2` and requires a byte-equal compile on the default search path (SentHost H2/H3).
  - The judge reads stdin from `/dev/null`, and a Compose section in its output is a setup error.
  - The generator went from 60 to 150 cases: it draws from every header name and `U` names, and combines up to 3 layouts. 28,780 distinct generated RMLVOs all compiled.
  - TMPDIR under `/tmp`, `/var/tmp` or `/dev/shm` is refused.
  - C2 gains clause j (7 source-derived topics), and clause f now ignores counts inside code spans.
- **C1 data `430d2569`**: `tools/mado-keysym.py`.
- **C2**: the integrated candidate (`candidate/hyprland-bind-key-match-r49.md`, `candidate/rows.md`) still fails `PRED-C2-r49` (row-pin binding and quote attachment). No data commit was made: honest stop.
  - The L1 removed a w1 claim that 8 Shift binds are dead (M49-1). It contradicts the source trace: `KeybindManager.cpp:369` reads a translation state that never receives modifiers.
- **Routed round-48 items:**
  - The 47 sidecars were committed in the freeze. Gate findings at the tip go 159 → 110 (measured by `w1/CritSidecars`).
  - N1–N5 corrections are in `corpus/lessons/round-49.md` `## Round-48 closure items`.
  - M48-8 gate v3 and the M48-10 guard are drafted, not installed.
  - SentScratch refusals are in the new counters.

## Landed changes

| Commit | Change | LOG.md Round 49 bullet |
|---|---|---|
| `5f37c1b87b3ce5e438d19284e32b2e46fd548a92` | claims, w1 spec + dispatch, census before, operator-owned digest before | 1 |
| `dd2e827eeb30efe5b6bd3a918f41b74dc467b646` | freeze: registration, both counters, 633 fixtures, w1 evidence, pins, candidates, 47 sidecars | 2 |
| `430d2569c15309ac49ba694c1a1a5b21db1b325d` | C1 data: `tools/mado-keysym.py` | 3 |
| `602e39e3718a507a70eb9e7b4f4975ea48f09149` | lesson round-49, SCORECARD/LOG round 49, receipts (C1/C2 at data, census after, operator state after) | 4–6 |
| `8a370cd481c6044b2f5c09fd66acde8fc54d173c` | `receipts/axis-tip.txt` | 5 |

Inherited state: the 47 untracked `*.synthetic` sidecars. N1: the count was 47, not 52 (`git status --porcelain -uall | wc -l` → 47 at base). They were committed with the reason in `w1/CritSidecars.md`. Nothing is untracked at the tip.

## Before → after measurements

**C1** — counting command:

```
cd /home/vgpnk/Projects/shokunin/mado-shokunin && TMPDIR=<scratch> python3 -I quality/counters/c1-r49-keysym.py --repo . --rev <rev> --work <scratch> --nonce <n>
```

| Revision | Result | Exit | Receipt |
|---|---|---|---|
| base `03e4ae76` | `fixtures=0/633 generated=0/150 selftest=fail readonly=fail tool=absent verdict=TARGET_MISSED` | 1 | `receipts/c1-base.txt` |
| `430d2569`, nonce 4949 | `fixtures=633/633 generated=150/150 selftest=ok readonly=ok tool=present verdict=TARGET_MET` | 0 | `receipts/c1-after-data.txt` |
| `430d2569`, nonce 31337 | `fixtures=633/633 generated=150/150 selftest=ok readonly=ok tool=present verdict=TARGET_MET` | 0 | `receipts/c1-after-data-nonce2.txt` |

Do-nothing control (w1): an exit-2 stub scores `fixtures=52/633 … TARGET_MISSED` (`w1/ExecCounterC1/receipts-stub-always2.txt`). Self-verdict: **TARGET_MET, but unattacked**, because no w2 ran.

**C2** — counting command:

```
cd /home/vgpnk/Projects/shokunin/mado-shokunin && TMPDIR=<scratch> python3 -I quality/counters/c2-r49-bind-entry.py --repo . --rev <rev>
```

At `430d2569`: `clause=a entry_absent admitted=0/1 verdict=TARGET_MISSED`, exit 1 (`receipts/c2-at-data.txt`). **Honest stop.**

**Harm watch** at `602e39e3`: `MADO_AXIS: checked=3 mismatched=0` (navigation 65/65, calibration 86/86, operability 12/12; `receipts/axis-tip.txt`). The operator cache `~/.cache/xdg-terminal-exec` digest `ddd94f6b…` and mtime are unchanged before and after the round (`receipts/operator-state-before.txt`, `operator-state-after.txt`).

## Sources & frontier

Census command: `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin mado`. Before (`receipts/census-before.txt`) and after (`receipts/census-after.txt`) are identical: W04 ×17, W01 ×1, `mado ok`, exit 0 at both ends.

- **Rows:** 288 → 288 (`grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`).
- **Added by tier:** none. S352–S363 (tier A, opened 2026-10-27, pinned in `fetch/`) are drafted in `candidate/rows.md` but not appended, because no admitted entry cites them (CORPUS.md rule 4).
- **Touched rows:** none.
- **Gate:** the Gate in `corpus/lessons/round-49.md` names 2 located drafted admits and 4 rejects. The full admit lines are in `w1/ScrRows/gate.md`.
- **Frontier advanced:** keysym-to-key resolution (C1 tool). The README Frontier was not edited this round.
- **Sourced claim:** C2, not landed. The round's landed claim, C1, rests on the pinned judge, not on a new row. This conformance item is unmet.
- **Assimilation: none.** `w1/ScoutShokuknow` found no bind/keymap theme in `merge/mado/`.
- **considerthese:** proposal 2 (live-state tool ledger) is drafted at `w1/ScrToolLedger` and not landed.
- **Mistakes mined:** M49-1..4.

## Trend verdicts

- **expansion: improved.** One capability row (keysym-to-key parity), demonstrated by the count-time judge at `430d2569`. No new knowledge entry.
- **quality: unprovable-but-better.**
  - Round-48 routed items N1–N5, the sidecars and the SentScratch refusals were worked with receipts. The freeze closed the isolation holes w1 found.
  - Limits: no w2 attacked the freeze, gate v3 and the host guard were not installed, and the session-material gate is still red (110 findings).
- **discernment: unchanged.** The L1 caught and removed a false w1 claim (M49-1). No outside spot-check has run yet. No QUALITY criterion was added this round.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources. Untouched this round; the `w1/ScrSkill` draft was not landed. No non-author verifier.
- [~] At least one end-to-end domain task executed and logged in LOG.md. LOG Round 49: C1 judged against the pinned how-to-type on 783 cases (`receipts/c1-after-data.txt`). No non-author verifier.
- [~] Instructions executable by an agent without oral context. The `tools/mado-keysym.py` docstring and `--selftest` (38/38) are untested by an outside agent.
- [~] No cross-domain bleed (PROVINCE.md still accurate). `w1/ConnSiblings.md`: no sibling claims the keysym/bind ground. No non-author verifier.

Stale-lane: respawn-per-round driver; no other mission of this lane is open.

Tool installs: none. pacman untouched.

Seats: w1 45, by role:

| Role | Seats |
|---|---|
| executor | 20 |
| scribe | 7 |
| critic | 5 |
| scout | 4 |
| connector | 2 |
| sentinel | 2 |
| reviewer | 2 |
| mutation-tester | 2 |
| revenger | 1 |

The planner seat was held by the L1. Dead seats are not known; WAVE-DONE had not arrived and the 7 seats above were unsettled at filing.

Misroot sweep: `git -C /home/vgpnk/Projects/shokunin status --porcelain` was empty before this report, so no seat file landed at the fleet root.

Scratch: the L1 scratch dirs were removed. Seat scratch is owned by the seats and by `inline.sh advance`.

Open L0 questions: none.
