# souji — round 49 (Windows host; the r48 non-author closure's routed defects landed)

## Work performed

One declared claim, one axis; C1 works the lowest non-retired axis
(calibration 7). All three r48-closure routed defects are addressed: item 1 =
claim C1; item 2 (the S271 quote word-count label) and item 3 (the Gate's
reject sample stated explicitly) are lesson rows in
`corpus/lessons/round-49.md`. Round base `5a26fbfd`
(5a26fbfd5b0f94b0d8283908a0f4b876b2857bfc, the r48 non-author spot-check).
Preregistration frozen at `445321aa`
(445321aa61cfafb95b623a5fe1c0126c0a60186f) before any claim receipt existed;
freeze attempt 1 `ebebc44` (ebebc44c0ccd8941dd4cc1fc4dd71452ab9027fa) is
SUPERSEDED and preserved as evidence — its Control receipt ended
`COUNTER-EXIT=1`, the freeze-check itself read `FINDING C1 CONTROL-NOT-RED …
SUMMARY claims=1 findings=1` at the attempt-1 freeze (receipt
`census/round-49/records/freeze-check-at-freeze-attempt1.txt`), and the
supersede landed before any after-data (the r48 Amendment-1 ordering;
attempt-1 files keep their bytes forever). The attempt-2 freeze-check verdict
is `SUMMARY claims=1 findings=0`, exit 0
(`census/round-49/records/freeze-check-at-freeze-r2.txt`). The do-nothing
control is committed in the freeze commits (control-first). No wave was
dispatched: this host has no seat dispatch surface (standing L0 question;
dispatched=0, completed=0, dead=0; no WAVE-DONE claimed; nothing assumed
answered).

- **C1 (calibration 7, instrument repair — not a capability acquisition)** —
  r48 routed defect 1: the committed `tools/souji-freeze-check.py --selftest`
  failed 37/41 on this host from text-mode fixture writes. Before: raw
  selftest `SELFTEST cases=41 pass=4 fail=37`, EXIT=1
  (`census/round-49/controls/freeze-selftest-base-red.txt`); the digest-pinned
  r49 counter over the same committed bytes read `selftest=FAIL (41, 4, 37)
  patches=0/3 real=ok retro=red retro_clean=ok`, exit 1
  (`census/round-49/controls/c1-control-donothing-r2.txt`; tool_sha
  f7f54e8f0a71) — the r42 registry gate `r42-freeze-check-selftest` had no
  obtainable green here, i.e. the lane's standing self-assessment of its own
  freeze instrument did not match observed state. Repair: the selftest's
  fixture writer ported to binary mode (`open(fp, "wb")` + UTF-8 encode); the
  base→fixed diff receipt shows exactly the writer hunk plus its docstring
  line — verdict code byte-identical
  (`census/round-49/records/tool-diff-base-to-fix.txt`; tool sha
  f7f54e8f…9999 → d1ca06fd…a364). After: raw selftest on the fixed bytes
  `cases=41 pass=41 fail=0`, EXIT=0
  (`records/freeze-selftest-fixed-green.txt`), and the SAME counter at the
  content tip re-derives the gate green from committed bytes: `selftest=ok
  (41, 41, 0) patches=3/3 real=ok retro=red retro_clean=ok`, exit 0
  (`records/c1-tip-49.txt`; tool_sha d1ca06fd0fb2). `patches=3/3` proves the
  repaired selftest still discriminates (P1 reversed digests, P2 empty
  diff-filter, P3 failing merge-base each flip it non-zero), and the
  real/retro/retro_clean legs are identical at base and tip — the verdict
  path is unchanged. Grounded on S272 (text mode translates `\n` to
  os.linesep on writing; binary mode does not). The pre-freeze hazard sweep
  (`records/fixture-hazard-sweep.txt`) classifies the inventory: 49
  selftest-bearing instruments, 27 with text-mode open sites, exactly ONE
  digest-bound writer in the tools layer (repaired this round); the frozen
  census counters (r41 c3, r42 c2, r43 c2/c3) carry the class as named
  limits — frozen bytes, never edited (the r42 counter additionally cannot
  launch its child here: it invokes the `python3` name and this host has
  none).
- **Carry-in item 2 (S271 quote word-count erratum)** — the r48 lesson/report
  label the S271 located quote "17 words"; verbatim it is 16 (count command
  in `corpus/lessons/round-49.md` Gate → 16). The ≤25-word bound held either
  way; quote bytes never changed; the r48 lesson stays as filed. Lineage
  noted: r45's Gate carried the same class ("15 words" for a nine-word
  quote) — quotes are now command-counted against captured bytes.
- **Carry-in item 3 (the Gate's reject sample, stated explicitly)** — the
  round-49 Gate opens exactly ONE new source (S272, admitted; the only
  candidate fetched) and lands ZERO new reject rows, with the single-fetch
  sweep named; the reject-side sample is a standing-rejection re-open: S267
  re-opened against the live stdtypes page (HTTP 200, 814236 bytes; receipt
  `census/round-49/sources/s267-reopen-receipt.txt`) — the recorded rejection
  reason holds, S267 stays rejected, no row cell changed.
- **Standing practice executed** — the r48 verifier's landing re-created the
  index drift (third consecutive round, exactly as predicted); restored by
  the committed fail-closed tool only (`records/idx-repair-base-49.txt`:
  repairable-paths=1 → AFTER rows=6 unexpected=0); the mid-round repair
  REFUSED fail-closed on the in-progress tool edit as designed
  (`records/idx-repair-freeze2-49.txt`, EXIT=1, nothing repaired —
  disclosed); after the content and end landings the tool restored the
  tolerated state (`records/idx-repair-content-49.txt`; the terminal repair
  receipt is a scratch receipt, quoted below). Amendment-1 six-path set
  re-derived at base and tip, not widened
  (`records/ntfs-exclusion-check-base.txt`, `-tip.txt`, count=6 both). The
  r46 standing landing-suite counter re-derived green at the tip:
  `SUMMARY assertions=548 mismatches=70 registered=70 corrected=0 exempted=0
  unfiled=0`, exit 0 (`records/c1-suite-tip-49.txt`) — my SCORECARD
  additions registered cleanly. Terminal porcelain is exactly the six
  tolerated rows (scratch receipt `porcelain-at-end.txt`, quoted below).

### Fresh-start rulings (round prompt §7) — what was ruled out and why

The three rejected closures (r43, r44, r45 — lessons + reports) were re-read
and spot-checked before drafting (this is the second consecutive round under
the same three, so the r48 rulings were re-derived rather than copied):

| prior rejected shape | ruling this round |
|---|---|
| r43 — preregistration landed after ready handoff; instruments that cannot bind their tokens | ruled out: freeze attempt 2 landed before any claim receipt; the counter is digest-pinned in the prereg (194df28cf…, verified by the freeze-check at the freeze); the do-nothing control is committed in the freeze commit. The r43 class's own descendant (the "never actually writes CRLF" fixture critique) is the defect this round FIXES. |
| r44 — a frozen predicate honest work could not meet | ruled out: the target is derived from a state the base already exhibits honestly (the instrument's own verdict over committed bytes: red at base, green at tip — no new predicate invented, no operator action or dispatch needed) |
| r45 — the different-instrument limit (0-to-green by swapping instruments; axis-fit unprovable) | ruled out structurally: the SAME r49 counter measures both arms — its bytes are identical at base and tip (digest-pinned); only the world (the tool's fixture writer) moves, along the r48 non-author verifier's own routed fix. The axis fit is the AXES.md calibration signal verbatim: self-assessment (the registered gate) must match observed repo state — at base it could not, at tip it does |
| r43/r44/r45 — L2-floor wave shapes | ruled out: no wave-dependent claim; no dispatch surface exists on this host (dispatched=0 disclosed; standing L0 question routed around) |

## Landed changes

| change | commit | LOG evidence |
|---|---|---|
| freeze attempt 1 (SUPERSEDED, preserved as evidence): preregistration, counter, population, red do-nothing controls, pre-flight receipts (census-before with the conf rc-2 verdict inside, porcelain-at-base, idx-repair-base-49, NTFS base 6 paths), S272 capture, fixture-hazard sweep | `ebebc44c0ccd8941dd4cc1fc4dd71452ab9027fa` | LOG.md round-49 bullet 1; lesson round-49 ## Mistakes row 2 |
| freeze attempt 2 (operative): preregistration-r2 + the Control receipt re-taken to the freeze-check grammar | `445321aa61cfafb95b623a5fe1c0126c0a60186f` | LOG.md round-49 preamble; lesson round-49 ## Mistakes row 2 |
| content: C1 (binary fixture writer + diff receipt + raw green receipt), S272 row + provenance + S267 re-open receipt, lesson round-49 (Gate + 3 mistakes), LOG entry, SCORECARD r49 section + planned r50, SKILL r49 contract + gate row, freeze-check attempt-1/r2 receipts, mid-round repair-refusal receipt | `f86a51039e729bc0d56d6e3cbff7f31a2c8328ff` | LOG.md round-49 bullets 1–5 |
| end receipts: r49 counter green at the tip, r46 standing suite green at the tip, census-after (rc 0, rows 196, 59 W04, the +1 disclosed), NTFS tip re-check, freeze-check claims=1 findings=0 at the final tip, idx-repair-content receipt | `7836df3e50538598f245ce3823d979de2992eb73` | LOG.md round-49 bullet 3 (end receipts owed) |

All four commits authored `souji-shokunin <souji@shokunin.local>` through the
index-free plumbing helper, named paths only, pushed to origin master; after
every landing the named paths were verified with `git diff-tree -r
--name-only <new>` (the r48 lesson's standing rule), and every landing's
index drift was repaired by the committed tool.

## Before → after measurements

- **C1 (calibration 7):** counting commands and values —
  - `python -B tools/souji-freeze-check.py --selftest`: before
    `SELFTEST cases=41 pass=4 fail=37`, EXIT=1
    (`controls/freeze-selftest-base-red.txt`, bytes = base commit
    5a26fbfd…); after `SELFTEST cases=41 pass=41 fail=0`, EXIT=0
    (`records/freeze-selftest-fixed-green.txt`, bytes = content tip
    f86a5103…).
  - `python -B census/round-49/c1-counter.py --root . --rev <full40>
    --scratch DIR`: before (rev = base) `SUMMARY selftest=FAIL patches=0/3
    real=ok retro=red retro_clean=ok`, exit 1
    (`controls/c1-control-donothing-r2.txt`); after (rev = content tip)
    `SUMMARY selftest=ok patches=3/3 real=ok retro=red retro_clean=ok
    tool_sha=d1ca06fd0fb2`, exit 0 (`records/c1-tip-49.txt`). Same counter
    bytes both ends (sha256 194df28cf…, pinned in
    `census/round-49/preregistration-r2.txt`). Measured commit: content tip
    f86a5103…; SCORECARD bytes unchanged after the content commit, and the
    freeze-check at the final tip 7836df3e… re-reads `claims=1 findings=0`
    (`records/freeze-check-at-tip.txt`).
  - No axis harmed: calibration improved (the registered gate re-derivable
    green); operability unchanged (no command surface added or removed — the
    sweep's named limits are documented, not edited); coverage unchanged (no
    PROVINCE surface change). Numeric scores honestly unchanged (7/8/8).

## Sources & frontier

- SOURCES rows 195 → 196 (S272). Counting command:
  `git show <rev>:corpus/SOURCES.md | grep -cE '^\|\s*S[0-9]{3,}\s*\|'` →
  195 at base 5a26fbfd…, 196 at tip 7836df3e…. W04 duplicate-url warnings
  58 → 59: the +1 is `S272 duplicate url
  docs.python.org/3/library/functions.html across scopes` — S272 shares the
  functions.html host page with an earlier row's anchor under a different
  scope (the located quote and scope differ); the census reports this as a
  W04 warning, not a finding; disclosed, not masked. S272 opened live
  2026-11-01 (curl -sSL HTTP 200, 330862 bytes, sha256 ece1c4b3…e00701a;
  served at /3/builtins/functions.html after one 301; capture
  `census/round-49/sources/s272-python-open-located-quote.txt`); located
  quote (23 words, counted by command against the captured bytes): "When
  writing output to the stream, if newline is None, any '\n' characters
  written are translated to the system default line separator, os.linesep."
  Sourced claim: C1. Limits: the page grounds interpreter behavior only.
  No existing row's status, recheck or used-by cell changed; standing reject
  S267 re-opened and holding (receipt
  `census/round-49/sources/s267-reopen-receipt.txt`).
- Census before→after (contract §2b): before
  `census/round-49/records/census-before.txt` — the r48 adapter form, rc 0,
  58 W04, rows 195, `shokunin-repo-hygiene ok`, with the conf form's raw
  rc-2 `souji missing` verdict recorded inside (the documented host state,
  PROVINCE host correction; routed to the operator at L0 round-48). After
  `records/census-after.txt` — rc 0, `CENSUS-RUN lane=souji conf_rc=2
  dir_rc=0`, 59 W04, rows 196. Exit 0 at round end: held (adapter exit; the
  conf-name form's rc 2 is the known, disclosed host mismatch). Command:
  `bash tools/souji-census-run.sh --fleet-root <fleet> --lane souji`.
- Mistakes mined: `corpus/lessons/round-49.md` `## Mistakes` — 3 rows, each
  with receipts and a same-round executed fix (the text-mode digest-bound
  fixture class, swept and fixed where live, named limits where frozen; the
  Control-receipt grammar class that superseded freeze attempt 1 before any
  after-data; the exit-after-a-pipe receipt class caught in pre-landing
  review).

Assimilation: none — the lane repo holds no `considerthese/` directory
(named-path check 2026-11-01) and shokuknow is unreachable from this host.

## Trend verdicts

- **expansion: unchanged** — no knowledge entry, no Core promotion, no new
  PROVINCE surface; SOURCES 195 → 196 on a docs host the coverage map
  already held (the +1 W04 is that share, disclosed). The one new committed
  instrument (the r49 counter) stands over a surface the lane already
  owns.
- **quality: improved** — before: the r42 registry gate
  `r42-freeze-check-selftest` could not produce its registered green verdict
  on this host (37/41 false failures from platform-dependent fixture bytes);
  after: the gate re-derives green end-to-end from committed bytes (41/41
  raw; counter green with patches=3/3 discrimination), the fixture rule is a
  committed SKILL contract with a registry row, and the sweep receipt bounds
  the class across the inventory (one live writer repaired; frozen counters
  documented as named limits). "A checklist item can be run and produces the
  stated outcome" — the selftest now does, on this host.
- **discernment: improved** — three real mistakes mined with receipts and
  same-round executed fixes; the freeze-check instrument caught this round's
  own formatting defect at the attempt-1 freeze and the supersede landed
  before any after-data (control-first ordering preserved under
  pressure — the easy path was a post-freeze edit, and it was not taken);
  the first flawed red receipt (exit-after-pipe) was caught in review before
  landing and re-taken; fresh-start rulings re-derived, not copied; the
  Gate's reject sample is stated explicitly with a standing-rejection
  re-open.

## Stale-lane

This respawn-per-round assignment is the sole souji mission; no abandoned
concurrent lane mission.

## SHONEN

- [~] Decision tables/error patterns/checklists: `SKILL.md` (new r49
  selftest-fixture contract + the r49 gate registry row naming the failing
  arms), `corpus/SOURCES.md` (S272 added; S267 re-open receipt),
  `corpus/lessons/round-49.md` (Gate + 3 mistakes); no named outside
  promotion verifier.
- [~] End-to-end domain task executed and logged: LOG.md round-49 entry; the
  repair receipts (`census/round-49/controls/`,
  `census/round-49/records/`) — dry-run discipline preserved: nothing moved,
  nothing deleted, no removal proposed (certification OFF, K5 HELD).
- [~] Instructions executable without oral context: the frozen prereg
  (attempt 2) + counter + controls re-derive everything (freeze-check
  claims=1 findings=0 at the attempt-2 freeze and at the final tip; the
  counting commands are pasted above).
- [~] No cross-domain bleed: PROVINCE.md untouched this round (the r46/r48
  host corrections still hold; no new surface claimed); the fleet census
  script untouched (read-only, sha256 recorded per run by the adapter);
  secret-shaped findings remain routed, never read; no deletion authority
  acquired.

Open L0 carried (operator-owned, routed around, nothing assumed answered):
souji round-44 symlink-contract disposition; souji round-46 L2-floor
disposition (dispatched=0 again this round); souji round-46 staged-package
disposition; souji round-48 census conf-name contract-vs-host routing. No
new L0 question this round. Holds unchanged: certification OFF, K5 HELD,
NAMESPACE/reap holds, execution-bound audit attribution open.

### Terminal scratch receipts (quoted, per the r48 practice — landing them would re-drift the index they describe)

The terminal repair after the end-receipts landing
`7836df3e50538598f245ce3823d979de2992eb73`
(`python -B tools/souji-idx-repair.py --root . --rev 7836df3e… --receipt
<scratch>/idx-repair-end-49.txt`; tool bytes fd66d4f1…, the r48 pin):

```
CLASSES tolerated=6 repairable-paths=6 unexpected=0
REPAIR  census/round-49/records/c1-suite-tip-49.txt mode=100644 op=update-index--add--cacheinfo
REPAIR  census/round-49/records/c1-tip-49.txt mode=100644 op=update-index--add--cacheinfo
REPAIR  census/round-49/records/census-after.txt mode=100644 op=update-index--add--cacheinfo
REPAIR  census/round-49/records/freeze-check-at-tip.txt mode=100644 op=update-index--add--cacheinfo
REPAIR  census/round-49/records/idx-repair-content-49.txt mode=100644 op=update-index--add--cacheinfo
REPAIR  census/round-49/records/ntfs-exclusion-check-tip.txt mode=100644 op=update-index--add--cacheinfo
AFTER   rows=6 unexpected=0
EXIT=0
```

(the six REPAIR lines each carry a per-path blob id and sha256 proof in the
full receipt) — the host index restored to the frozen Amendment-1 tolerance
by the committed tool, no manual index command anywhere this round. The
post-repair `git status --porcelain` (scratch receipt
`porcelain-at-end.txt`) reads exactly the six tolerated control-char-path
`D ` rows and nothing else.
