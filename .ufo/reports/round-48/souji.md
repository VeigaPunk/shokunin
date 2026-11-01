# souji — round 48 (Windows host; the r47 carry-in items landed as claims)

## Work performed

Two declared claims, two distinct axes; C1 works the lowest non-retired axis
(calibration 7). Preregistration frozen at `21ec2736`
(21ec27361c1ded8d93842b2e89239e874e30f875) before any claim receipt existed;
Amendment 1 landed at `5ca5001b` (5ca5001b358eca55b70f1da63f8c0c5c3b27b945),
also before any claim receipt; the preregistration blob is byte-unchanged, so
`tools/souji-freeze-check.py` reads `SUMMARY claims=2 findings=0` (exit 0) at
the freeze, at the amendment, and at the final tip `7f8433bf`
(7f8433bfb359f553babac7890070a6f6c744642a). Both do-nothing controls are
committed in the freeze commit (control-first). No wave was dispatched: this
host has no seat dispatch surface (standing L0 question; dispatched=0,
completed=0, dead=0; no WAVE-DONE claimed; nothing assumed answered).

- **C1 (calibration 7, capability acquisition)** — carry-in item 2: the
  integrator-landing index-drift class (r47 lesson mistake 1) recurred
  exactly as predicted — the r47 spot-check landing `8e17a4b1` left
  `corpus/lessons/round-47-verifier-spotcheck.md` outside the host index and
  the frozen r46 counter exited 2 at the round base (the do-nothing control
  receipt, taken pre-freeze). The committed fail-closed tool
  `tools/souji-idx-repair.py` performed EVERY host-index restoration this
  round (no manual `update-index` anywhere): base drift
  `census/round-48/records/idx-repair-base.txt` (BEFORE 38 rows, tolerated=6,
  repairable-paths=16 → AFTER rows=6 unexpected=0), this round's own landings
  (`-content.txt`: 23→6; `-end.txt`: 16→6; the terminal landing's repair
  receipt is a scratch receipt quoted below), each repair sha256-proven per
  path and executed with the rev's own mode+blob (`update-index --add
  --cacheinfo`, grounded on S271). The frozen r46 counter — byte-unchanged,
  digest-pinned — then reads green at the base
  (`census/round-48/records/c1-base-green.txt`, assertions=538 unfiled=0)
  and at the content tip (`records/c1-tip-48.txt`, assertions=545 unfiled=0;
  SCORECARD bytes byte-identical content→final tip, so the same SUMMARY
  re-derives at the final tip — corroborated at the tip, see Scratch
  receipts). The frozen Amendment-1 six-path set was re-derived at base and
  tip and NOT widened (`records/ntfs-exclusion-check-base.txt`, `-tip.txt`,
  count=6 both).
- **C2 (operability 8)** — carry-in item 1: the contract's census conf-name
  form reads rc 2 `souji missing` on this host. The committed adapter
  `tools/souji-census-run.sh` runs the conf form FIRST and records its raw
  rc-2 verdict — disclosed, never masked — beside the documented
  explicit-lane-directory form's rc-0 `shokunin-repo-hygiene ok` verdict,
  exits with the latter's code, and prints the fleet script's sha256 (the
  fleet instrument is read-only to this lane and is untouched). Claim
  receipt `census/round-48/records/census-runner-output.txt`
  (CENSUS-RUN lane=souji conf_rc=2 dir_rc=0); the frozen r48 counter at the
  tip reads `CENSUS-RUN forms=2 findings=0` (exit 0); selftest cases=3
  pass=3 fail=0 (`records/census-runner-selftest.txt`; arm A1 reproduces the
  host condition synthetically with the real fleet script copied into the
  fixture). PROVINCE's host correction now names the adapter as the runnable
  form; the contract-vs-host mismatch is routed to the operator (L0
  round-48, appended this round — the operator owns the fleet-side
  instrument; routed around, nothing assumed answered).
- **Enabling host work (disclosed, not claimed):** Amendment 1
  (`census/round-48/amendment-1.txt`) — the frozen C1 tool bytes refused the
  freeze landing's own drift because plain porcelain collapses a
  wholly-untracked directory into one `?? census/round-48/` row (first
  execution refused fail-closed, receipt preserved:
  `records/idx-repair-base-refused-plain-porcelain.txt`, EXIT=1). The
  amendment (authorized by the carry-in's own "widen the freeze amendment
  properly if needed"; r46 Amendment-1 precedent) keeps the prereg blob
  byte-identical, enumerates porcelain with `-uall`, keeps the after-check
  on the plain form for counter parity, adds a collapse selftest arm
  (SELFTEST cases=5 pass=5 fail=0), and supersedes the C1 tool pin
  3c6803da… → fd66d4f1… — committed before any after-data. Mined as lesson
  mistake 2. Also mined (mistake 3): the plumbing helper commits DISK bytes;
  the first end-receipts commit `5fd125bd`
  (5fd125bdae678b94c24f01fd6bcac66afdc60f74) landed EMPTY because its five
  receipt paths were still staged in scratch (`git diff-tree -r 5fd125bd` is
  empty) — the receipts re-landed on top as `6231642c`
  (6231642c94dc91bf1381cc59564ed3f4479cbc34, diff-tree = exactly the five
  files); the empty commit stays as history, never rewritten. Receipt-staging
  discipline (stage receipts outside the repo until they land) recorded in
  SKILL.md and the lesson.

### Fresh-start rulings (round prompt §7) — what was ruled out and why

| prior rejected shape | ruling |
|---|---|
| r43 — preregistration landed after ready handoff; instruments that cannot bind their tokens | ruled out by freezing at 21ec2736 with digest-pinned counters, populations and red do-nothing controls committed in the freeze commit; the round's one amendment also landed BEFORE any after-receipt (the r43 defect was the reverse ordering); every receipt binds its rev |
| r44 — a frozen predicate honest work cannot meet (registered=0 exit 1) | ruled out by deriving both targets from states that already hold at the base (the counter's own Amendment-1 precondition, red-controlled; the census forms' documented rcs, red-controlled) or that an installed tool produces directly — targets reachable without dispatch or operator action |
| r45 — the different-instrument limit (0-to-green by swapping instruments; axis-fit unprovable) | ruled out by re-using the r46 counter byte-unchanged (sha-pinned 5455fb46…) for C1: the green is restored by repairing the HOST to the documented frozen precondition, not by swapping instruments; C2's axis (operability: commands that exist, scripts that run) is the direct fit, with the counter that verifies it committed in the freeze |
| r43/r44/r45 — L2-floor wave shapes (lane-dead attempts, undispatched plans) | ruled out: no dispatch surface exists on this host; the round declares no wave-dependent claim (dispatched=0 disclosed; standing L0 question routed around) |

## Landed changes

| change | commit | LOG evidence |
|---|---|---|
| freeze: preregistration, populations, counter, do-nothing controls (counter rc-2 at base; conf-form rc-2 + runner-absent), pre-flight receipts (census-before 58 W04 rows 194, porcelain, NTFS base 6 paths), S271 capture, both tools | `21ec27361c1ded8d93842b2e89239e874e30f875` | LOG.md round-48 bullet 1 |
| Amendment 1 (append-only, prereg blob unchanged) + the refused first attempt preserved as evidence + amended tool bytes | `5ca5001b358eca55b70f1da63f8c0c5c3b27b945` | LOG.md round-48 bullet 1; lesson round-48 ## Mistakes row 2 |
| content: C1/C2 claim receipts (idx-repair-base, selftest, counter-green-at-base, runner output, runner selftest); S271 row + provenance; lesson (2 mistakes); PROVINCE host-correction extension; SKILL registry rows + r48 contracts section; LOG entry; SCORECARD r48 section + capability rows + planned r49 | `462f25eb0b51706f40fa1691fa791587c57bb455` | LOG.md round-48 bullets 2–5 |
| end receipts (re-landing of the empty `5fd125bd`): idx-repair-content, counter at content tip, C2 counter at tip, census-after (rc 0, rows 195, 58 W04), NTFS tip re-check | `6231642c94dc91bf1381cc59564ed3f4479cbc34` | LOG.md round-48 bullet 5 + landing addendum |
| final: idx-repair-end receipt + lesson mistake 3 (the empty landing) + LOG addendum | `7f8433bfb359f553babac7890070a6f6c744642a` | LOG.md round-48 landing addendum |

All six commits authored `souji-shokunin <souji@shokunin.local>` through the
index-free plumbing helper, named paths only, pushed to origin master; after
every landing the C1 tool restored the host index (receipted), and the final
tip's porcelain is exactly the six tolerated Amendment-1 rows. The report
file is fleet-side (not committed by the lane).

## Before → after measurements

| claim | before → after (counting command) | measured commit |
|---|---|---|
| C1 standing suite receipt | `python -B census/round-46/c1-counter.py --root . --rev 8e17a4b1a8f8bd81dd5a978e698e447bd4253b3e --work <scratch>`: exit 2 `COULD-NOT-EVALUATE dirty worktree at run time: 2 unexpected rows` at the base before any repair (control, pre-freeze) → exit 0 `SUMMARY assertions=538 mismatches=70 registered=70 corrected=0 exempted=0 unfiled=0` at the base after the receipted repair, and the same exit 0 at the content tip (assertions=545, `records/c1-tip-48.txt`) and at the final tip (scratch corroboration below) | `7f8433bfb359f553babac7890070a6f6c744642a` |
| C1 repair receipts | `python -B tools/souji-idx-repair.py --root . --rev <full40> --receipt <path outside the repo>`: BEFORE 38 rows tolerated=6 repairable-paths=16 → AFTER rows=6 unexpected=0 (base), 23→6 (content landing), 16→6 (end landing), 10→6 (terminal landing, scratch receipt) | `7f8433bfb359f553babac7890070a6f6c744642a` |
| C2 census conf-name form | `bash tools/souji-census-run.sh --fleet-root <fleet> --lane souji`: at base the adapter is absent (`git cat-file -e` rc 128, control) and the raw conf-name form exits rc 2 `souji missing` (pre-freeze receipt) → adapter exit 0, `CENSUS-RUN lane=souji conf_rc=2 dir_rc=0`; `python -B census/round-48/c2-counter.py --root . --rev 7f8433bfb359f553babac7890070a6f6c744642a` → `CENSUS-RUN forms=2 findings=0` exit 0 | `7f8433bfb359f553babac7890070a6f6c744642a` |

Scratch receipts (re-derivable from the committed state; quoted here because
the round's last landing's repair cannot commit itself): terminal repair
BEFORE 10 rows → AFTER rows=6 unexpected=0 (exit 0); frozen counter at the
final tip `SUMMARY assertions=545 mismatches=70 registered=70 corrected=0
exempted=0 unfiled=0` exit 0; freeze-check at the final tip `claims=2
findings=0` exit 0; `git diff-tree 462f25eb 7f8433bf -- SCORECARD.md` = 0
lines (SCORECARD byte-identical content→final tip); `git rev-parse HEAD
origin/master` and `git ls-remote origin refs/heads/master` all print
7f8433bfb359f553babac7890070a6f6c744642a; NTFS control-char set count=6.

## Sources & frontier

Census before→after (the contract's conf-name form stays rc 2 on this host —
PROVINCE correction, adapter shipped, L0 filed): before
`census/round-48/records/census-before.txt` rc 0, `shokunin-repo-hygiene ok`,
58 W04, rows 194; after `census/round-48/records/census-after.txt` rc 0,
58 W04, rows 195. Command:
`bash <fleet>/scripts/sources-census.sh validate --root <fleet-root> <lane-dir>`
(exit 0 required at round end: held; the conf-name form's raw rc-2 receipt
`census-confname-before.txt` travels beside it, and the adapter now produces
the working verdict from the contract's lane name — C2). The +1 row is S271
itself; no W04 change (git-update-index is new across scopes). S271 opened
live 2026-11-01 (curl HTTP 200, 84442 bytes; capture
`census/round-48/sources/s271-git-update-index-located-quote.txt`); located
quote (17 words): "cacheinfo is useful when the object is in the database
but the file isn't available locally" (section USING --CACHEINFO, after the
`--add --cacheinfo <mode>,<sha1>,<path>` example). Sourced claim: C1 (the
repair plumbing). Limits: documents the plumbing operation only — not the
drift classification, not the six-path tolerance, not porcelain collapse.
No existing row's status, recheck or used-by cell changed. Mistakes mined:
`corpus/lessons/round-48.md` `## Mistakes` (3 rows, each with receipts and a
fix executed this round: the predicted drift recurrence; the porcelain
collapse class closed by the pre-data amendment; the empty helper landing).

Assimilation: none — the lane repo holds no `considerthese/` directory
(named-path check 2026-11-01) and shokuknow is unreachable from this host.

## Trend verdicts

- **expansion: unchanged** — no knowledge entry, no Core promotion, no new
  PROVINCE surface (the host-correction section is extended in place; the
  Owns/Work-surfaces lists are untouched). SOURCES 194 → 195 (S271 on
  existing plumbing ground). The two capability rows are operational tooling
  over surfaces the lane already owns (receipts, census), recorded in the
  repertoire table with first-working round 48.
- **quality: improved** — before this round the contract census command had
  no runnable path on this host and every landing re-broke the standing
  suite receipt until a hand fix; after it, both moves are committed,
  selftested, registry-registered contracts with fail-closed verdict maps
  (`tools/souji-idx-repair.py` gate row; `tools/souji-census-run.sh` probe
  row; SKILL.md "Round 48 host-index and census-runner contracts"), and the
  standing receipt re-derives green at base and tip through the round's own
  landings. The observable "a checklist item can be run and produces the
  stated outcome" gained two items that run (receipts above). Numeric axis
  scores honestly unchanged (calibration 7, operability 8, coverage 8).
- **discernment: improved** — three real mistakes mined with receipts and
  executed same-round fixes (the predicted drift recurrence, now automated;
  the porcelain collapse class, closed by a pre-data amendment instead of a
  post-hoc edit; the empty helper landing, caught by post-landing diff-tree
  verification); control-first freeze with red controls; the amendment
  landed before any after-data; fresh-start rulings derived from the three
  rejected closures; receipt-staging discipline discovered and recorded.

## Stale-lane

This respawn-per-round assignment is the sole souji mission; no abandoned
concurrent lane mission.

## SHONEN

- [~] Decision tables/error patterns/checklists: `SKILL.md` (two new Gate
  registry rows naming failing arms + the r48 contracts section),
  `corpus/SOURCES.md` (S271 added), `corpus/lessons/round-48.md` (Gate +
  3 mistakes); no named outside promotion verifier.
- [~] End-to-end domain task executed and logged: LOG.md round-48 entry;
  the real drift repairs (`census/round-48/records/idx-repair-base.txt`,
  `-content.txt`, `-end.txt`) and the adapter receipt
  (`records/census-runner-output.txt`) — dry-run discipline preserved:
  nothing moved, nothing deleted, no removal proposed (certification OFF,
  K5 HELD).
- [~] Instructions executable without oral context: the frozen
  preregistration + amendment + counters + controls re-derive everything
  (`tools/souji-freeze-check.py` findings=0 at the tip; commands pasted
  above; the SKILL r48 section states the standing practice).
- [~] No cross-domain bleed: PROVINCE.md extended only inside the lane's
  host-correction section; the fleet census script untouched (read-only,
  sha256 recorded per run); secret-shaped findings remain routed, never
  read; no deletion authority acquired.

Open L0 carried (operator-owned, routed around, nothing assumed answered):
souji round-44 symlink-contract disposition; souji round-46 L2-floor
disposition (dispatched=0 again this round); souji round-46 staged-package
disposition; souji round-48 census conf-name contract-vs-host routing (new
this round). Holds unchanged: certification OFF, K5 HELD, NAMESPACE/reap
holds, execution-bound audit attribution open.
