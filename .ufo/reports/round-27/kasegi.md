# kasegi round 27 — freeze + honest stop (operator wrap-up; claims NOT VERIFIED)

Lane repo: kasegi-shokunin. Lane HEAD: `c2ab51de7a97820794ccde9db8c673bb993a434f` (round-27 freeze,
pushed; `git ls-remote origin refs/heads/master` prints it — pre-report gate satisfied). Round
base: `744a0d8`. Round shape: **zero waves** — the operator ended the run mid-round
(orchestrator wrap-up: "start no new waves… land NOW with what you have"); the §3 L2 floor and
the 32–64 wave band were not exercised, no seat ran, no dispatch refusal occurred. Claims are
recorded honestly as NOT VERIFIED; nothing was prettified.

## Work performed

Declared claims (frozen before any dispatch, `.ufo/waves/round-27/claims.json`):
- **C1 — depth:verifiability** (lowest non-retired axis, score 4): `anchorcheck.py` gate
  soundness — exit nonzero on unverifiable verdicts (MISSING-FILE, PAST-EOF, OUTSIDE-BASE,
  PIN-BROKEN, BASE-ABSENT, BOUNTIES-ABSENT); CITE gains a `~/Projects/bounties/` arm;
  `--selftest` with one isolating fixture per limb.
- **C2 — coverage** (score 7): F12 "Japanese state-coordinated disclosure workflow" admitted
  from the staged package entry `japanese-domestic-disclosure-workflow.md` (staged S042 → lane
  S042; staged S043 = lane S041 from round 26), re-grounded on round-27 captures.

Work items landed:
- Claims frozen pre-dispatch with predicates, counters, kill rules, do-nothing controls
  (R25-1 complied; no in-place edit after freeze) — `.ufo/waves/round-27/claims.json` @ `c2ab51de`.
- C1 control fixtures built AND executed pre-freeze: `c1-controls/bad-fixture.md`,
  `bounties-fixture.md`, `instrument-digest-before.txt` (anchorcheck sha256 before),
  `bad-fixture-before.txt`, `bounties-fixture-before.txt`, `selftest-before.txt`,
  `skill-before.txt` — commit `c2ab51de`.
- **M27-1 caught by that pre-freeze execution**: the fabricated-citation fixture reports
  `BASE-ABSENT`, not the assumed `MISSING-FILE`, on a host whose mirror root is absent since
  2026-10-12; the frozen claim was written against the observed verdict class. Evidence:
  `corpus/lessons/round-27.md` §Mistakes; `c1-controls/bad-fixture-before.txt`.
- C2 before-receipts: `c2-controls/before.txt` (frontier 11; entries citing S042: 0; harness
  `entries=14 pass=14 exit=0`; expected-list 41 lines) and `census-before.txt` (exit 0, 41 rows,
  W04 ×2 pre-existing S028/S029).
- Staged-package planning survey only (read-only, no campaign tool run): staged S042 free in the
  lane registry; staged S043 = lane S041; `vendor-third-party-finding-coordination` carries
  `ground: F20` naming no lane frontier row — recorded as the planned round-28 reject. Evidence:
  `corpus/lessons/round-27.md` §Gate.
- Round lesson (`corpus/lessons/round-27.md`: Gate, Mistakes M27-1/M27-2, frozen-claim status
  table, round-28 carry-forward), LOG.md round-27 entry, SCORECARD.md round-27 row — all @ `c2ab51de`.

## Landed changes

All in commit `c2ab51de7a97820794ccde9db8c673bb993a434f` (via jj-lane.sh; `landed` after remote
verification), each tied to the LOG.md round-27 entry:
- `.ufo/waves/round-27/claims.json` — frozen C1/C2 (new).
- `.ufo/waves/round-27/c1-controls/` — fixtures + before receipts (new; M27-1 evidence).
- `.ufo/waves/round-27/c2-controls/before.txt`, `.ufo/waves/round-27/census-before.txt` (new).
- `corpus/lessons/round-27.md` (new), `LOG.md` (round-27 entry appended), `SCORECARD.md`
  (round-27 honest-stop row appended).

No production byte changed: `corpus/instruments/anchorcheck.py` untouched (C1 after-state never
produced); no capture, no knowledge entry, no SOURCES.md row (C2 after-state never produced);
SKILL.md untouched (density axis undisturbed).

## Before → after measurements

C1 (commands frozen in claims.json; run from lane root):
- `python3 corpus/instruments/anchorcheck.py .ufo/waves/round-27/c1-controls/bad-fixture.md >/dev/null 2>&1; echo $?` — **before 0** (`BASE-ABSENT` printed, exit 0; `c1-controls/bad-fixture-before.txt`); after: not reached.
- `python3 corpus/instruments/anchorcheck.py .ufo/waves/round-27/c1-controls/bounties-fixture.md 2>/dev/null | grep -c BOUNTIES-ABSENT` — **before 0** (cite invisible to CITE); after: not reached.
- `grep -cE 'selftest cases=' .ufo/waves/round-27/c1-receipt-index.txt` — **before 0** (file absent; `--selftest` itself FileNotFoundError exit 1, `c1-controls/selftest-before.txt`); after: not reached.
- SKILL.md no-harm — **before exit 0, bad=0** (`c1-controls/skill-before.txt`); after: not reached (bytes unchanged, so still exit 0, bad=0).
- Do-nothing control: the committed before-receipts on unchanged bytes cannot reach any after value.

C2:
- `awk -F'|' '$2 ~ /^ *F[0-9]+ / && $4 ~ /^ *admitted *$/ {n++} END{print n+0}' corpus/README.md` — **before 11**; after: not reached (still 11).
- `grep -lE '^source: S042 ' corpus/knowledge/*.md | wc -l` — **before 0**; after: not reached (still 0).
- `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kasegi` — **before exit 0** (`census-before.txt`); after: unchanged bytes, same exit (registry untouched).
- `python3 corpus/instruments/frontier-recheck-count.py` — **before `entries=14 pass=14 exit=0`** (`c2-controls/before.txt`); after: not reached.

Verdicts: **C1 NOT VERIFIED, C2 NOT VERIFIED** — declared, frozen, before-measured; the
operator wrap-up stopped the round before any wave or edit; per the honesty rule no after-value
is claimed. SCORECARD rows carry the verdicts with this commit as evidence.

## Sources & frontier

`SOURCES.md` rows before → after: **41 → 41** (registry untouched). Counting command:
`grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md` → 41 both sides;
census `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kasegi` → **exit 0 both sides** (before: `census-before.txt`; after: same bytes, same exit, re-run at round-28 close). Rows added by tier: none. Rows touched: none (no status/recheck/used-by change; nothing to log old→new). Frontier rows advanced: none (F12 planned, not admitted). Assimilation: **none executed** — the package was surveyed at planning level only; the Gate in `corpus/lessons/round-27.md` records zero admits/zero rejects and the planned round-28 candidates. considerthese: not mined this round (wrap-up); proposal 1 (wave-evidence economy) remains the planned round-28 R14 item.

## Trend verdicts

- **expansion — unchanged**: no entry, row, or frontier advance; F12 exists only as a frozen claim.
- **quality — unchanged**: the one real quality event is M27-1 (a stale-premise fixture design caught
  pre-freeze by executing fixtures before freezing) — process learning, landed as a lesson; no
  instrument or entry quality moved.
- **discernment — unchanged**: the honest stop itself (claims recorded NOT VERIFIED rather than
  padded) is the discernment signal; evidence `corpus/lessons/round-27.md` §Frozen claims.

No owned axis harmed: lane diff `744a0d8..c2ab51de` touches only `.ufo/waves/round-27/` receipts,
the new lesson, LOG.md and SCORECARD.md appends.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — SKILL.md
  bytes untouched this round; the box rests on the round-25 receipts (`density.py` mean 154.0;
  `anchorcheck.py` bad=0) plus this round's committed before-receipt `c1-controls/skill-before.txt`
  (exit 0, bad=0, unchanged bytes).
- [ ] At least one end-to-end domain task executed and logged — not this round: no dispatch, no
  domain task; last executed end-to-end evidence remains LOG.md round-25/round-26 entries.
- [~] Instructions executable by an agent without oral context — re-verified in-round:
  `python3 corpus/instruments/frontier-recheck-count.py` → `entries=14 pass=14 exit=0`
  (`c2-controls/before.txt`); recheck-audit/expected-list instruments unchanged from the round-26
  green receipts (`c1-live.json` @ `a04cc6c`).
- [~] No cross-domain bleed — no corpus/knowledge or PROVINCE edit this round; the C2 plan's
  sibling-overlap scan (connector seat) was not run (no wave); the round-26 connector verdict
  (chousa cedes bounty-program scope; kake refuses disclosure timing) stands unchanged.

Stale-lane: respawn-per-round driver; no other mission of this lane is open.
Tooling: no tool installed or upgraded; no pacman transaction attempted (host-wide pacman pause in force).
L0 questions: none appended this round.
