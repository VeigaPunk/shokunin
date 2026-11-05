# mori — round 99 report (L1 MoriR99, attempt 1)

Lane repo `mori-shokunin`, branch `master`. Entering `73308ff6e5c933f53498e9501ef95917b0ef7171` → final
`d51a6ab6d27cfb8ca049c6a56f239c0f41b0a726` (`git ls-remote origin refs/heads/master` → `d51a6ab6…`). Fresh-start
round (prompt Amendment 35): the last three rejected closures (r94, r95, r96) were read before any claim was declared,
and every claim was frozen with do-nothing, forgery, single-fix-removed and positive controls executed and committed
first (`.ufo/waves/round-99/evidence/controls-r99.txt`, `CONTROLS_DONE unexpected=0`). No earlier attempt of this
round (`.ufo/watchdog.log` holds only `launch mori round=99 … attempt=1`); nothing inherited.

## Work performed

Declared claims (2): **C1 operability** (score 7): the journal write-scan of the registered probe
`tools/mori-userns-runway.py` reads sudo's real log grammar and a `sh -c` script as a shell does (sourced: S633–S636,
opened this round). **C2 calibration** (score 5, the lowest non-retired tier with depth and freshness): SCORECARD
`## Axes` Evidence and Last-change cells match the admitted closure record.

- Protocol load and fresh-start reads: `corpus/lessons/round-9{4,5,6}-verifier-spotcheck.md` and the r98 spot-check
  (routed D1–D4). Contract `.ufo/waves/round-99/contract.md` (freeze `462cef1c`) names each.
- Capture study (motivating evidence): the r98 incident capture is exactly the `COMMAND=`-filtered view of the same
  journal window and lost one `(command continued)` line; the entering reader silently fell back to whitespace
  splitting on 24 of 276 `COMMAND=` values (`corpus/lessons/round-99.md` Mistakes 1, 2, 4). The full capture of
  every `sudo[` line is pinned at `.ufo/waves/round-99/evidence/journal-incident-r99.txt` (sha256 `7ec650c9…090d`).
- Sources opened and pinned (`corpus/evidence/sources-r99/`): sudo v1.9.17p2 `eventlog.c` (S635) and `lbuf.c` (S636),
  the host's sudo version; sysctl(8) (S633); POSIX XCU ch. 2 (S634); journalctl(1) re-opened (S014).
- C1 tool (`tools/mori-userns-runway.py`, landing `5013f0be`): `split_cmd` inverts sudo's `COMMAND=` rendering
  (quotes only around arguments with a space, `\'`/`\\`, `#0nn`, exit suffix); `scan_journal` joins
  `(command continued)` parts by pid and fails closed (`SYSCTL_WRITES_SETUP unparsed=U`, exit 2) on unreadable sudo
  lines; `shell_tokens`/`script_writes` read words, quotes, comments and operators, and report redirections to
  `/proc/sys`, `tee`, nested `sysctl` and shell `-c`; `sysctl -r/--pattern` and exit events are not writes; `-o short`
  timestamps parse. Self-test 11 → 19 at landing.
- C1 counter `.ufo/waves/round-99/count-c1.py`: battery generated at measurement time from a printed seed (QUALITY
  209, r98 D1), m03 runway clamp fixtures (r98 D2), live `used_lb` cross-check (r98 D1).
- C2: `SCORECARD.md` Axes cells via `.ufo/waves/round-99/candidate/apply-c2.py` (r98 D3); counter `count-c2.py`
  pins the fleet MANIFEST at `4ad377ea`.
- Knowledge entry `corpus/knowledge/sudo-log-grammar-r99.md` (10 sourced claims, limits, boundaries); registry row
  edited in place at `SKILL.md` (one row per tool; auditor `REGISTRY=met`); QUALITY 210, 211, 212.
- Wave w1 (12 seats, 0 dead), evidence `.ufo/waves/round-99/w1/`: real-sudo end-to-end probe (`Mo99ExecSudo.md`,
  3550-char argv split over three continuation lines recovered exactly); live journal trial over three days
  (`Mo99ExecTrial.md`: on `journalctl -o short` the entering tool reads the six incident writes as none, the landed
  tool reads all six); replays (`Mo99ExecReplay.md`); review (`Mo99RevC1.md` F1–F8); counter forgery
  (`Mo99CritC1.md`); 37-mutant battery (`Mo99MutC1.md`); source re-opening (`Mo99ScoutSrc.md`); C2 re-derivations
  (`Mo99ExecCalib.md`, `Mo99RevC2.md`, `Mo99CritC2.md`); sibling scan (`Mo99ConnSibling.md`); lesson draft
  (`Mo99ScribeLesson.md`).
- Post-landing fixes from the wave, outside the frozen measurement (commit `88c5c70c`): non-sudo lines mentioning
  `sudo[N]` ignored (ExecReplay found the r98 counter's J2 decoy read as unparsed); `>|`, `&>`, `>&`,
  backslash-newline, here-document bodies, `#040`, quoted ` ; EXIT=` (RevC1 F1–F6). Self-test 22 cases.
- Planner seat: held by the L1 (the validator refuses `planner`); the planning data-walk was done by the L1 before
  the freeze. `labrat` is not a swarm role under the validator; the bounded sudo probe rode an executor seat.

## Landed changes

| commit (`jj-lane.sh` `landed`) | content | LOG.md entry |
|---|---|---|
| `462cef1cc637de4c6e993aefd00ed9df32895984` | freeze: contract, counters, controls runner + receipts (draft and frozen), candidate tool and C2 transform, befores, census-before, full incident capture, pinned sources | Round 99 |
| `5013f0be8ac9e7fce3c08b680e43cf9cbd49620d` | landing: `tools/mori-userns-runway.py`, `SKILL.md` registry row, `corpus/SOURCES.md` S633–S636 + S014 used-by, `corpus/knowledge/sudo-log-grammar-r99.md`, `SCORECARD.md` Axes cells | Round 99 |
| `88c5c70c896671436524d0375da3dd14e1e143c6` | integration: post-landing tool fixes, knowledge limits, QUALITY 210–212, lesson, LOG, SCORECARD verdict + Planned r100, wave w1 evidence (spec, validator, dispatch, `.ready`, `.ready.dispatched`, results, 12 reports), landing receipts | Round 99 |
| `d51a6ab6d27cfb8ca049c6a56f239c0f41b0a726` | final receipts (`final-c1/c2`, `r98-counter-final`, `census-after`), lesson Mistake 7 + census close | Round 99 |

## Before → after measurements

| claim | command | before (`73308ff6`) | after (landing `5013f0be`) | final (`88c5c70c`) |
|---|---|---|---|---|
| C1 | `git -C mori-shokunin archive <rev> \| tar -x -C DIR` → `python3 .ufo/waves/round-99/count-c1.py --root DIR` | `C1=unmet cases_ok=24/60 … checks_failed=battery,sourced` exit 1 (`evidence/before-c1.txt`) | `C1=met cases_ok=60/60 … incident=ok registry=met sourced=met(S633,S634,S635,S636) checks_failed=-` exit 0 (`evidence/landing-c1.txt`) | same, exit 0 (`evidence/final-c1.txt`) |
| C2 | `python3 .ufo/waves/round-99/count-c2.py <rev>` | `C2=unmet mismatches=5 cells_unchanged=yes gate=rc1 mismatched_axes=coverage,operability,depth,freshness,calibration` exit 1 (`evidence/before-c2.txt`) | `C2=met mismatches=0 cells_unchanged=yes gate=ok mismatched_axes=-` exit 0 (`evidence/landing-c2.txt`) | same, exit 0 (`evidence/final-c2.txt`) |

Verdicts as the lane reads them (closure rules): **C1 met as frozen.** Counter defect: a zero-grammar template
forgery also scores `60/60` on four seeds (`w1/Mo99CritC1.md`, VERDICT needs-amend); the landed tool is right on
10/10 hand-written held-out lines where the forgery covers 3/10, real sudo probes are recovered exactly
(`w1/Mo99ExecSudo.md`), and the do-nothing control stays `24/60` on six seeds. Reviewer `Mo99RevC1` also returned
needs-amend on the claim sentence (F1/F2 `>|`, backslash-newline); both were fixed after landing and do not change
the frozen measurement. **C2 met** (holds per ExecCalib, RevC2, CritC2, ExecReplay). Disclosed behaviour change:
the r98 frozen counter at the final tip differs only on its J1 case (the truncated r98 capture now exits 2,
`evidence/r98-counter-final.txt`). The registered calibration gate with its default base `66c5518e` now prints
`columns_unchanged=no` — the designed detection firing on the sanctioned Evidence move (`w1/Mo99RevC2.md` §8).

## Sources & frontier

- Census: `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin mori` — start `mori ok`, exit 0,
  43 W04 (`evidence/census-before.txt`); end `mori ok`, exit 0, 44 W04 (`evidence/census-after.txt`; the added W04 is
  S634 sharing the XCU ch. 2 URL with S611–S614, lesson Mistake 7).
- Rows: 404 → 408 (`git show <rev>:corpus/SOURCES.md | grep -cE '^ {0,3}\| *S[0-9]{3,}'` at `73308ff6` / `88c5c70c`).
  Added by tier: A ×4 (S633 docs, S634 spec, S635 code, S636 code), all `mined`, opened 2026-11-05, used-by
  `corpus/knowledge/sudo-log-grammar-r99.md`.
- Rows touched old→new: S014 `used-by` gains `corpus/knowledge/sudo-log-grammar-r99.md` (status, recheck unchanged).
- Frontier advanced: the write-scan's input grammar (sudo log rendering, continuation lines, shell `-c` scripts) moved
  from unread to sourced and run on real host bytes.
- Sourced claim: C1 rests on S633–S636 (counter conjunct `sourced=met(S633,S634,S635,S636)`).
- Mined mistakes: 7 (`corpus/lessons/round-99.md` `## Mistakes`), each with how its fix is shown able to fail.
- Gate: admits S633–S636; rejects sudo `main` as the grammar ground (host runs 1.9.17p2) and a new row for the
  journalctl URL (already S014). Correction of record: S634 quote is 18 words, not 17.
- Assimilation: none (no `merge/mori/` theme fits C1 or C2). considerthese: `considerthese/2026-11-05.md` proposals
  1–5 read, none taken.
- r98 spot-check routed defects: D1 (lookup stub) → C1 counter generated battery and QUALITY 212; D2 (m03, F1–F3) →
  C1 (m03 killed, F1 short-format, F2 `-r`, F3 quotes/comments); D3 → C2; D4 carried (lesson Routed).

## Trend verdicts

- **expansion: improved** — one new knowledge entry on ground the lane did not hold (`git grep -c "command continued"
  73308ff6 -- corpus/knowledge PROVINCE.md SKILL.md` → no hit; at `d51a6ab6` the entry carries it), every `source:`
  a `mined` row opened this round.
- **quality: improved** — a registered instrument's stated outcome now holds on real input classes it failed at
  entering (`before-c1.txt` 24/60 → 60/60; `-o short` incident window 0 → 6 writes in `w1/Mo99ExecTrial.md`);
  QUALITY 210–212 grounded and shown able to fail. Counter weakness disclosed (QUALITY 212).
- **discernment: improved** — C2 calibration (`mismatches` 5 → 0); the lane's own critic's forgery of its counter is
  published beside the met verdict and became QUALITY 212; seven mistakes mined, two found by the wave after landing.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — `SKILL.md` registry row for `tools/mori-userns-runway.py` (round-99 grammar, verdict map, 22-case self-test); `corpus/QUALITY.md` 210–212
- [~] At least one end-to-end domain task executed and logged in LOG.md — `LOG.md` Round 99 (real `sudo -n /usr/bin/true` probes recovered exactly, `w1/Mo99ExecSudo.md`; three-day journal trial, `w1/Mo99ExecTrial.md`)
- [~] Instructions executable by an agent without oral context — `python3 tools/mori-userns-runway.py --selftest` → `PASS (22 cases)`; `python3 .ufo/waves/round-99/count-c1.py --root DIR` reproduced on 4+ seeds by `w1/Mo99ExecReplay.md`
- [~] No cross-domain bleed (PROVINCE.md still accurate) — `corpus/knowledge/sudo-log-grammar-r99.md` Boundaries; tsukuroi's capture defect reported, not edited (`w1/Mo99ConnSibling.md`)

## Round shape and seats

One v1 wave `w1` under `ufo-wave-policy.json` (band 8–16): 12 seats — scout ×1, connector ×1, executor ×4 (one a
bounded sudo probe), scribe ×1, reviewer ×2, critic ×2, mutation-tester ×1; attack seats 5/12 (42 %). No residual
call. Round total 12. Dead seats: 0 (all 12 `w1-results.json` outputs present). Seat disclosure: `Mo99ExecSudo` ran
`sudo -n -l` once outside its authorized `sudo -n /usr/bin/true` form (non-mutating; in its report). No seat mutated
a sysctl. Misroot sweep: 12 untracked fleet-root files, none written by a mori seat; none moved.

Open L0 questions: none new (carried: mori | round-94, round-95, round-96). Tool installs: none (L1 and every seat
report none). Stale-lane: respawn-per-round driver; no other mission of this lane is open.
