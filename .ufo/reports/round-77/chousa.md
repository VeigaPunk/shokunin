# Chousa round 77 — the outer battery stops being passable by an invocation counter

## Work performed

Declared claims: **C1 operability** (lowest scored non-retired axis; the historical 3/10 is held, not
moved) — the lane's candidate-running battery is no longer passable by a matrix that counts its own
invocations; **C2 calibration** — the false sentence in the frozen round-76 claims file is superseded
append-only and one committed counter re-derives the supersession. Both predicates were frozen in
`corpus/evidence/round77/claims.md` at `a9530782578723de1364e0a3a47effcde8c85c23`, after the controls commit `e6fcdc4770c2fa73e5ccda99445c4311128d7e0d`.

- C1: `matrix-battery-v4.py` permutes the subject order per run from `secrets.randbits(64)`, requires
  every matrix run to print the twelve-line contract table with the battery's own independently stated
  expected cells, and scores three forged matrices as a control leg. `corpus/evidence/round77/matrix-battery-v4.py`;
  `corpus/evidence/round77/forgers/{forge-order-matrix,forge-order-matrix-table,forge-order-matrix-block}.py`;
  `controls/{before-oracle-v3,before-oracle-v3-committed-bytes,after-battery-v4}.txt`.
- C1 before/after on one command: the round-76 battery prints
  `BATTERY=PASS forgers_rejected=11/11 positive=2/2` (exit 0) for a call-count matrix
  (`controls/before-oracle-v3-committed-bytes.txt`); the successor prints
  `BATTERY=PASS forgers_rejected=11/11 positive=2/2 oracle=REJECTED` (exit 0)
  (`controls/after-battery-v4.txt`). Closure-removal twins: `--no-permute` → `BATTERY=FAIL … oracle=MISS`
  (`controls/twin-no-permute.txt`), `--no-content` → still `BATTERY=PASS` (`controls/twin-no-content.txt`).
- C2: the false clause is quoted and superseded in `corpus/evidence/round76/claims.md`
  (`## Correction — round-76 claims prose`), and `corpus/evidence/round77/c3-count.py` moves
  `C3=FAIL checks=1/5` (exit 1, `controls/before-c3.txt`) to `C3=PASS checks=5/5` (exit 0,
  `controls/after-c3.txt`).
- Wave falsification: `R77CriticA` reaches the frozen predicate line at exit 0 without scoring any subject through three
  channels — the appended salt suffix leaves a content hash that classifies every subject
  (`rcpt-a1.txt`), `/proc/<ppid>/cmdline` exposes the battery's `CONTRACT` cells (`rcpt-a2.txt`), and
  the printed `ORDER` digest is a digest of the permutation, recovered by enumerating 13! inside the
  battery's own 300 s cap (11.8 s and 59.1 s, `rcpt-a7.txt`); a detached helper appends 26 copies of
  the predicate line after a failing run (`rcpt-a5d.txt`). `R77SentinelA` measures the `--work`
  defects (a caller's directory is deleted by the battery's `finally`; an unwritable `--work` exits 1,
  not 2) and no lane-root guard in `c3-count.py`. `R77ScoutA` opens the installed `random.py`/
  `secrets.py`: "cryptographically strong" is written, "unpredictable" never is. `R77ScribeA` corrects
  a quote count from 12 to 11 words and finds a control receipt naming an oracle digest no committed
  object carries. `R77ConnectorA` reports that chousa QUALITY 139 is the only sibling-set criterion
  naming the outer-battery boundary, and absorbs nothing. Files:
  `.ufo/waves/round-77/w1/{R77CriticA,R77SentinelA,R77ScoutA,R77ScribeA,R77ConnectorA}.md`.

## Landed changes

Final lane commit: **`958a6023c376f4142dd5d995e88754d9e391c6f6`**. Before writing this report,
`git -C /home/vgpnk/Projects/shokunin/chousa-shokunin ls-remote origin refs/heads/master` printed that exact hash.

| landing | changes tied to LOG.md Round 77 |
|---|---|
| `e6fcdc4770c2fa73e5ccda99445c4311128d7e0d` | successor battery, three forged matrices, the C2 counter, the committed control receipts and the validated wave spec; the controls commit strictly precedes the claims freeze |
| `a9530782578723de1364e0a3a47effcde8c85c23` | the two frozen claims; predicate, counter and kill-rule bytes unchanged after any seat scored them |
| `9fcfb70ba6f202506dfd55f71917dc2d31b3f825` | validated dispatch, registry and ready handoff (12 seats, one v1 wave) |
| `9874f46d21139dcfa9ca496ad831c4b9300c3d8b` | the append-only correction of the r76 claims prose, the round lesson (Gate, Mistakes, limits), SOURCES S190–S192, QUALITY 141, the SKILL registry row, the SCORECARD planned section and the LOG entry |
| `958a6023c376f4142dd5d995e88754d9e391c6f6` | wave reports and results, QUALITY 142–143, the lesson's wave integration and self-evaluation, the SCORECARD verdict, the C2 after-receipt, the committed-bytes before-receipt and the final census |

Wave: one v1 wave under `ufo-wave-policy.json` (band 8–16), 12 seats — 3 executor, 1 scout, 1 scribe,
1 connector, 2 reviewer, 2 critic, 1 mutation-tester, 1 sentinel — so 5 attack seats (42%); L1 holds
the canonical planner seat; no residual call; no dead seat replaced. Five seat reports are retained.
`w1-results.json` carries 12 entries with empty `output` and a note that the orchestrator kernel
restarted mid-wave and seat outputs went to the orchestrator session, so seven seats settled without a
retained report: the r76 routed defect 5 recurs, committing the results file did not cure it, and this
report records it rather than calling the wave fully attested. `.ufo/waves/round-77/{w1-spec.json,
w1-dispatch.json,w1.ready,w1.ready.dispatched,w1-results.json,w1/}`.

Misroot sweep: `git -C /home/vgpnk/Projects/shokunin status --porcelain` showed only orchestrator-owned
`.scratch/` entries and a pre-existing untracked `after`; no file names chousa or round 77, so no
misroot was moved or deleted. Inherited lane state was clean at round start. No aggregator, operator or
sibling-lane file was edited. Tool installs: none (no package installed or upgraded; the pacman pause
was respected).

## Before → after measurements

| claim | counting command (lane cwd; DIR under `/fast/scratch/hyaku/chousa-r77/`) | observed before → after |
|---|---|---|
| C1 | `python3 -B corpus/evidence/round77/matrix-battery-v4.py --matrix corpus/evidence/round76/loader-matrix-v3.py --work DIR` | do-nothing state: the round-76 battery over the committed call-count matrix is `BATTERY=PASS forgers_rejected=11/11 positive=2/2`, rc 0 → successor `BATTERY=PASS forgers_rejected=11/11 positive=2/2 oracle=REJECTED`, rc 0; `--no-permute` twin `BATTERY=FAIL … oracle=MISS`, rc 1 |
| C2 | `python3 -B corpus/evidence/round77/c3-count.py --lane . --base a519fb0a80cf52c7988713c1f05b3ce8440fedda --rev REV` | `C3=FAIL checks=1/5`, rc 1 (`controls/before-c3.txt`) → `C3=PASS checks=5/5`, rc 0 at `9874f46d21139dcfa9ca496ad831c4b9300c3d8b` (`controls/after-c3.txt`) |

Both measured at the frozen instrument bytes (`matrix-battery-v4.py` `155fafb1…f106a3d`,
`c3-count.py` `32b76565…062335d`), unchanged from the controls commit through the landing.

## Sources & frontier

Registry 189 → 192; +2 tier B, +1 tier C; A123/B50/C16 → A123/B52/C17; mined 152 → 154, queued 19
unchanged, rejected 18 → 19. Counting command:
`grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`; histograms derive
columns 4 (tier) and 8 (status) after splitting table cells.

New rows only: S190/S191 `mined`, recheck `on-release`, used-by `corpus/lessons/round-77.md`; S192
`rejected`, used-by `—`. No held status/recheck/used-by cell changed. Both admits are the r76 verifier
file at **`6defa58dbdc40856f4e7dd24df98dc7ebd3459c0`**; the lesson Gate records the access date and the
located 10- and 11-word quotes (`R77ScribeA` corrected the first draft's 12-word count before landing).
No external live fetch.

Census command at both ends:
`/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin chousa`

Both outputs (`.ufo/waves/round-77/census-{start,end}.txt`), both **EXIT=0**:
```text
chousa	W04	S051 duplicate url www.w3.org/TR/2017/REC-html52-20171214/syntax.html across scopes
chousa	W04	S053 duplicate url docs.python.org/3/library/socket.html across scopes
chousa	W04	S073 duplicate url www.gnu.org/software/coreutils/manual/coreutils.html across scopes
chousa	W04	S074 duplicate url docs.python.org/3/library/hashlib.html across scopes
chousa	W04	S075 duplicate url www.gnu.org/software/coreutils/manual/coreutils.html across scopes
chousa	ok	/home/vgpnk/Projects/shokunin/chousa-shokunin/corpus/SOURCES.md
EXIT=0
```

Frontier ground advanced: none — this is existing-method instrument quality and curation, not new
province coverage. **Assimilation: none**; `considerthese/` was opened and no proposal was adopted at
the claim cap. Non-author admit/reject spot-check requested, not supplied by lane-dispatched seats.

## Trend verdicts

- **Expansion: unchanged** — no knowledge entry, capability row or province ground; three registry rows are curation.
- **Quality: improved narrowly** — the outer battery now refuses a call-count matrix that reached its exact target lines, the order leg is shown load-bearing by its twin, and two of the round's own instrument defects (a probe writing into the lane, a receipt naming an uncommitted digest) are mined with a guard shown able to fail. The content leg is not claimed as the discriminating closure, and the battery's `--work` defects are carried as QUALITY 142 rather than repaired after scoring.
- **Discernment: improved** — the wave's attack findings became recorded limits and two grounded criteria, the Scribe corrected a quote count and found a receipt-identity slip before landing, and the Sentinel's boundary audit is retained. Outside admit/reject agreement is pending, not self-granted.

Stale-lane: respawn-per-round; no other chousa mission open. This round progressed through landed
commits and retained seat evidence; no silent mission claimed.

## SHONEN

- [~] Real tables/error patterns/checklists with sources — `SKILL.md` Decision table/Error patterns/Checklist/Gates (the round-77 battery row); no named non-author promotion verifier.
- [~] End-to-end domain task logged — `LOG.md` Round 9; `corpus/fixtures/archives-r9/`.
- [~] Executable without oral context — `SKILL.md` Gates; `corpus/evidence/round73/controls/preflight-r73.txt`.
- [~] No cross-domain bleed — `PROVINCE.md`; round-77 lesson Boundaries; sibling precedents read only.
