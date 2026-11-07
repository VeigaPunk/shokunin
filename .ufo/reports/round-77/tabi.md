# tabi — round 77 (attempt 2)

**Declared claim (1): C1 coverage — capability acquisition `chromium-file-chooser-linux`, generation r77.**
File choosers over raw CDP on Chromium 155.0.8059.84 Linux `--headless=new`
(`Page.setInterceptFileChooserDialog`, `Page.fileChooserOpened`, `DOM.setFileInputFiles`), driven by real
mouse clicks, sourced S208–S212 (new this round) plus S213 post-freeze (client side).

**Verdict: C1 NOT VERIFIED — leg (b) is false as frozen** (the independent cold run produced a receipt the
pinned counter refuses, because it pins a browser-assigned `backendNodeId`; §*Before → after*). Legs (a),
(c) and (d) hold. Reported as an honest stop; frozen instruments, predicate and kill rule unchanged.

Base `1320d428f0c0957b46d6969b59c122fd69199331`; pre-freeze `cf0804f4`; claims `b51afa7f`; digests commit
**D `dcdf582a`**; scored `ec89a40e`; wave spec/dispatch `eedaa802`; integration `24cd88f8`.
Counter 183 checks, battery 336 cases, kill power 183 force-true + 70 semantic mutants.

Attempt 1 (`TabiR77`, 05:48–10:50 the same day) ended `lane-dead-no-report tabi round=77` with its whole
output uncommitted. This attempt inherited it and re-verified it before the freeze: a fresh driver run →
counter clean 183; the battery 336/336 on that fresh run; `controls-c1.mjs` allOk rc 0; the full pre-freeze
gate pass re-run over the final bytes (13/13 counter+battery, 9/9 kill power,
`controls/c1/prefreeze-summary.json` allOk, honest pairs 156 refused 0, max abs 1/40, max gap 2/9). Two
inherited items were not reused as they stood: `claims.json.draft` (superseded by `claims.json`, deleted)
and one battery placement guard that an honest fresh receipt falsified (repair + QUALITY 149, below). One
wave-spec seat changed role: `labrat` is a frozen-topology seat the swarm validator rejects, so the probe
item runs as an executor (`R77Exec4`).

## Work performed

- **C1 leg (a)** — pinned driver once, own ports, nonce `tabi-r77-l1-dcdf582add58`, receipt
  `corpus/evidence/round77/chromium-file-chooser/receipt.json`; frozen counting command exit 0, clean 183,
  19-prior limit block (`scored/c1-counter-a.exit`, `scored/c1-counter-a.json`).
- **C1 leg (b)** — `R77Exec1` cold run with nonce `tabi-r77-exec1-dcdf582add58`: driver rc 1, receipt
  written, counter **exit 1 with 8 findings** (seven `leg-*-opened` on `#s`, `producer-verdict`);
  `R77Exec1/counter.json`. Cause reproduced by the L1: 4 diagnostic cold runs, one gave `#m` = 10 instead of
  7 with every other per-leg field identical (`L1-diag/r{1..4}.json`, `drv2.out` rc 1). The id is Blink's
  DOM-serialization value, not a fixture property → QUALITY 150, note corrected, r78 binds the event's node
  to the page-side leg record.
- **C1 leg (c)** — battery 336/336 allOk with the three laundered degenerates, kill power holds, 0 survivors,
  0 crashes on the scored receipt (`scored/c1-negatives-a.json`, `scored/c1-kill-power-a.json`); `R77Exec2`
  re-ran both on 3 fresh receipts (clean).
- **Pre-freeze gates** — counter 13/13, battery 13/13, kill power 9/9 over `p1–p4`/`smoke1–9`
  (`controls/c1/run-prefreeze-gates.out`, `prefreeze-summary.json`); controls allOk (`controls/c1/controls-summary.json`).
- **Repair (pre-freeze, QUALITY 149)** — `accept-prior-tol-out-0.051` demanded exactly 0 abs matches from a
  prior derived from the receipt under test; an honest fresh receipt whose events sat on adjacent 0.1 ms grid
  steps threw the guard (`lesson-proof/attempt2-battery-fresh-receipt-pass1.json`) while the counter's verdict
  on it was clean. Guard now asserts what it brackets; the same receipt is 336/336
  (`attempt2-battery-fresh-receipt-pass2.json`); the pass was re-run over all 13 receipts.
- **Sources & frontier** — S208–S212 fetched at the tag with located quotes (`.ufo/waves/round-77/sources/FETCH.txt`);
  `R77Scout` re-opened all five independently (`cmp` exit 0 each) and found six citation-precision defects,
  all corrected (S212 range → 1294-1304; verbatim cancel quote; `input.Multiple()` belongs to S210:203;
  `SetFiles(files) || force` at 469; `SetFilesFromPaths` at 535; S210 scope widened to 174-224 and 525-556).
  S213 (Puppeteer v25.16.0 `cdp/ElementHandle.ts` + `revisions.ts`, opened by the L1 at
  2026-11-07T12:07:51-03:00 **after** the freeze, client-side, not a claim source) added with my own quote
  and bytes staged.
- **Wave w1** — one v1 wave, 12 seats, 0 dead: 4 executor, 3 reviewer, 1 critic, 1 mutation-tester, 1 scout,
  1 connector, 1 scribe (attack share 5/12 = 42 %). Results `w1-results.json`; seat reports `w1/*.md`.
  `R77Review1` F1/F2 (walk gated on literal schema bytes so a JSON-escaped schema hides an in-tree receipt;
  the run-under-test exemption is the receipt's self-claimed nonce) and F3 (`host-argv` pins 6 of 17 slots,
  a decoy `--user-data-dir`/`--remote-debugging-port` passes while Chromium honours the decoy — measured);
  `R77Mut1` 69 mutants, 27 killed, 42 survive (34 witnessed, 6 equivalent, 2 unwitnessed); `R77Exec4` R10
  (the exemption is the file's own nonce claim); `R77Review3` F1 (the frozen claim cites an absent
  enumeration file — reproduced and recorded post-D); `R77Critic` (do-nothing reach declared; prior
  integrity unstated); `R77Connector` (20/20 sibling lanes, 0 contested ground); `R77Scribe` (13 corrections).
- **Selftest** — `scripts/selftest-r77-gates.mjs --selftest` **11/13, exit 1**: `exec1-clean` red for the
  node-id defect; `scored-clean` red because the harness demands `priorEvents 79 / priorGaps 11` of every
  prior while three of the 19 priors are degenerate producers (37 and 35 events). Both routed to r78.
- **Census** — start exit 0 (207 rows), end exit 0 (213 rows) (`census/start2.txt`, `census/end.txt`).
- **Misroot sweep** — `git -C /home/vgpnk/Projects/shokunin status --porcelain`: no file written by this
  round's seats into the fleet root; `f.txt`, `trail-ids.txt` and `.scratch/` predate it and are not mine.

## Landed changes

- Lane commits (pushed through `jj-lane.sh` as `tabi`): `cf0804f4` pre-freeze instruments, controls,
  16 receipts, sources, note, lesson, QUALITY/SOURCES; `b51afa7f` frozen `claims.json`; `dcdf582a` `freeze.txt`
  (D); `ec89a40e` scored run + status at dispatch; `eedaa802` wave spec + dispatch; `24cd88f8`
  wave evidence and reports, seat receipts, SCORECARD row + corrections, note/lesson/SOURCES corrections,
  SKILL.md gate registry, selftest output, census end, prior-set enumeration record; `b985aac4` the
  SCORECARD commit pointer. **Lane tip pushed and verified: `b985aac4` (`ls-remote origin refs/heads/master`).**
- `SCORECARD.md` — `## Round 77` section, the C1 row with the NOT-VERIFIED verdict, capability row
  `chromium-file-chooser-linux` (0 → 1), a ten-item correction, `Planned (r78)`.
- `corpus/SOURCES.md` — S208–S213 (207 → 213) with the round-77 log line and two scope corrections.
- `corpus/QUALITY.md` — 145 (limit denominators), 146 (walk + enforced seat-output rule), 147 (wide novelty
  grep), 148 (pipe-complete output), 149 (derived-prior bracket guards), 150 (never pin a browser-assigned id).
- `corpus/lessons/round-77.md` — attempt-2 header, Gate (admit + 4 rejects with flips), 7 Mistakes rows
  (two of them `captured-by: none`, grounded as QUALITY 148/150).
- `corpus/knowledge/chromium-file-chooser-runtime-round-77.md` — corrected in place (node-id instability,
  verbatim quotes, S213 scope, the measured directory frontier).
- `SKILL.md` — `## Round 77 gate registry`.

## Before → after measurements

| Claim | Counting command | Before | After (commit) |
|---|---|---|---|
| C1 (a)+(c) | `node scripts/check-filechooser-r77.mjs --lane /home/vgpnk/Projects/shokunin/tabi-shokunin --receipt corpus/evidence/round77/chromium-file-chooser/receipt.json --expect-driver-sha256 9954db0703e03aed157c4be9b13f678b1bc1a6240b4bf88491d0e1f5286558a6 --expect-nonce tabi-r77-l1-dcdf582add58 --prior-set .ufo/waves/round-77/controls/c1/prior-set.txt --json` | no r77 receipt → exit 2 `receipt-unreadable`; the r76 dialog receipt → exit 1 with 122 findings under the scored nonce (123 under a dummy nonce) incl. `schema, nonce-shape, driver-pin, fixture-hash` (`scored/before/`); no prior set → exit 2 usage | exit 0, clean 183, 19 priors, limit block 19 entries (absNeed 40 / gapNeed 9 per honest prior); battery 336/336; kill power holds (`ec89a40e`) |
| C1 (b) | same counter on `.ufo/waves/round-77-seats/R77Exec1/receipt.json` with nonce `tabi-r77-exec1-dcdf582add58` and `--prior` the scored receipt | — | **FALSE: exit 1, 8 findings** — the seven `#s` legs report `backendNodeId` 4 (the scored run and 22 other observed runs report 5); reproduced by the L1 (1 of 4 cold runs, `#m` = 10) (`24cd88f8`) |
| C1 (d) | `grep -c '^| \`chromium-file-chooser-linux\` |' SCORECARD.md`; `git grep -lE 'setFileInputFiles\|fileChooserOpened' -- corpus/knowledge | wc -l` | 0 / 0 | 1 / 1 (`24cd88f8`) |

## Sources & frontier

- Census (contract v1): start exit 0 (207 rows, `git show 1320d428:corpus/SOURCES.md | grep -cE '^ {0,3}\| S[0-9]{3,} '`),
  end exit 0 (213 rows) — `census/start2.txt`, `census/end.txt`.
- Rows added: 6 (S208–S212 before the freeze; S213 after, client-side, not a claim source), all tier A
  `code`, status `mined`, `recheck: on-release`. Rows touched old→new: S210 (scope widened to 174-224 and
  525-556; anchor gained 224, 483-508, 525-533), S212 (1294-1303 → 1294-1304). Frontier rows advanced:
  S212 second scope of S202's file (W04 by design); S213 is the lane's first Puppeteer source.
- Mined mistake: `corpus/lessons/round-77.md ## Mistakes`, 7 rows; the post-D row (browser-assigned id)
  is `captured-by: none` and grounds QUALITY 150.
- Assimilation: none — `merge/tabi/` adoption stays closed pending the register-correction L0
  `tabi | round-57`; `considerthese/` does not exist in this lane.

## Trend verdicts

- **expansion — improved**: a surface the lane never held (0 capability rows, 0 notes by the wide grep at
  base) now has a 100-line note with 15 measured legs, 5 + 1 sources opened, and a capability row; the
  directory frontier was measured by a seat (3 runs) and folded into the note.
- **quality — harmed**: the new gate generation refuses honest runs. The frozen counter pins a
  browser-assigned `backendNodeId` and refused 2 of 25 observed cold runs (leg (b) is false because of it);
  its walk is gated on literal schema bytes so a JSON-escaped schema hides an in-tree receipt, and the
  run-under-test exemption trusts the receipt's own nonce claim (`Review1` F1/F2, `Exec4` R10); `host-argv`
  constrains 6 of 17 slots; the selftest mis-asserts the prior shape (11/13). All are recorded and routed;
  none is repaired into the frozen claim.
- **discernment — improved**: the round's own falsifier caught its claim (leg (b)), and the wave's
  independent seats found the escape classes, 42 surviving mutants and six citation defects — every one
  verified against committed bytes or a located source line, and each is now a QUALITY criterion, a note
  correction or an r78 item rather than an unexamined green.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — `SKILL.md`
  §Round 77 gate registry (gate entry, verdict map, pins, write scope); prior evidence unchanged.
- [~] At least one end-to-end domain task executed and logged in LOG.md — this round: the 15-leg chooser
  fixture driven end to end, scored run + 4 seat runs; `LOG.md` round-77 entry.
- [~] Instructions executable by an agent without oral context — the driver/counter/battery contracts and
  the gate registry; executed by 4 executor seats from the spec alone (`w1/*.md`).
- [~] No cross-domain bleed (PROVINCE.md still accurate) — `R77Connector`: 20/20 sibling lanes scanned, 0
  contested ground; `PROVINCE.md:3-19` unchanged.

## Round shape

One v1 wave (policy v1, band 8–16) of 12 seats; no residual call; **round total 12**; dead seats 0. Roles:
4 executor, 3 reviewer, 1 critic, 1 mutation-tester, 1 scout, 1 connector, 1 scribe. L1 holds the planner
seat (the validator rejects `planner`; the bounded planning data-walk rode `R77Exec4`). Attack share 5/12
≥ 25 %; connector seats 1 ≤ 2. Routes are whatever `task.agentModelOverrides` held at spawn
(`~/.omp/agent/config.yml`): `task/main/planner/reviewer/security-reviewer/critic/revenger/labrat/mutation-tester/simplifier/sentinel/scribe/sonic/distiller/seance` →
`@m_flash`, `executor` → `@m_zfl`, `scout` → `@m_mim`, `connector` → `@m_antigravity`; no `model` was passed.

Stale-lane: none — this is the respawn-per-round driver's round; no other mission of this lane is open.
Tool installs: none (node v24.21.0 and /usr/bin/chromium 155.0.8059.84 already present; pacman untouched per
the addendum guard; `curl` used to open S213, no install).
