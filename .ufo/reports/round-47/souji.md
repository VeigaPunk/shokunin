# souji — round 47 (Windows host; fresh-start after three rejected closures)

## Work performed

Two declared claims, two distinct axes; C1 works the lowest non-retired axis
(calibration 7). Preregistration frozen at `0027c977` (0027c977452e06d041a750a5a8c33b1fd5de57db)
before any after-data existed; `tools/souji-freeze-check.py` reads
`SUMMARY claims=2 findings=0` at the freeze and at the final tip `04b5e319`
(04b5e319322543c77472149973adb2cb47804764). Both do-nothing controls were
committed inside the freeze commit (control-first). No wave was dispatched:
this host has no seat dispatch surface (standing L0 question; dispatched=0,
completed=0, dead=0; no WAVE-DONE claimed; nothing assumed answered).

- **C1 (calibration)** — land the three r46 carry-in defects as append-only
  SCORECARD corrections and re-derive the r46 landing-suite receipt at this
  round's tip (the "standing instrument" planned item). Evidence:
  `census/round-47/c1-items.tsv` (frozen population), corrections in
  SCORECARD.md `### R46 carry-in corrections`, receipts
  `census/round-47/records/c1-base-green.txt` (base re-run after the index
  repair) and `census/round-47/records/c1-tip-47.txt` (tip re-run).
- **C2 (coverage, sourced on S270)** — convert the r46 workspace census rows
  for the four named candidates into per-artifact receipts (mission
  receipt flow, dry-run): the three `no-origin-master` lane clones and the
  foreign `helpers-r74/` root. Evidence: `census/round-47/c2-targets.tsv`
  (frozen population), `census/round-47/records/per-artifact-receipts.tsv`
  (raw tool output, one invocation), provenance index
  `census/round-47/records/receipt-commands.txt`, counter
  `census/round-47/c2-counter.py` with tip receipt
  `census/round-47/records/c2-counter-tip.txt`.
- **Enabling host work (disclosed, not claimed):** (1) targeted index repair
  after the e469084 spot-check landing drifted this host's index
  (`corpus/lessons/round-47.md` Mistakes row 1; receipt
  `census/round-47/records/c1-base-green.txt` header); (2)
  `tools/souji-verify.sh` `find_repo_for` termination repair for artifacts
  outside any git repository on this host — MSYS `dirname` bottoms out at
  `.`, so the walk spun forever and no T4 verdict was producible
  (Mistakes row 2; evidence `census/round-47/records/t4-spin-probe.txt`;
  consumer checks `records/verify-selftest-base.txt` vs
  `records/verify-selftest-repaired.txt` — identical exit 1, identical 47
  checks, the same 8 pre-existing host failures, outputs differing only in
  scratch paths and random fixture hashes — and
  `records/r17-jj-receipts-repaired.txt`: the registered gate is
  could-not-evaluate on this host because the fixture hard-codes /var/tmp
  and /var is not creatable here; environment-level, same for base bytes).
  The repair is strictly narrowing (termination only), committed
  (08646f36) before the T4 receipt it enables; the frozen preregistration
  text is unchanged (freeze-check still reads findings=0 at the tip).
- **r46 carry-in dispositions (all four addressed):** (1) the `assertions=522`
  cell is superseded by an append-only correction row carrying the measured
  533 (receipt + verifier §3 + own base re-run); (2) the "56 W04" prose is
  superseded by 57 (correction row + erratum here); (3) the before-census
  citation is corrected to a host-valid base — this round commits one
  (`census/round-47/records/census-before.txt`, explicit-lane-directory
  form, rc 0, 57 W04) beside the r46 rc-2 conf-name receipt; (4) the
  Amendment-1 NTFS exclusion set was re-derived at base and tip — exactly
  the six pinned paths of
  `state/hyaku/ntfs-excluded/shokunin-repo-hygiene.txt` — and not widened
  (`records/ntfs-exclusion-check-base.txt`, `-tip.txt`).

### Fresh-start rulings (round prompt §7) — what was ruled out and why

| prior rejected shape | ruling |
|---|---|
| r43 — preregistration landed after ready handoff; instruments that cannot bind their tokens (C1 counter not binding the captured derived token; memorizer control) | ruled out by freezing `census/round-47/preregistration.txt` at 0027c977 before any after-data, with digest-pinned counters/populations and both do-nothing controls committed in the freeze commit; freeze-check (the r41 tool built for exactly this defect) reads findings=0 at freeze and tip. No new token-binding instrument was written this round, so no new unbound-token surface exists. |
| r44 — a frozen predicate honest work cannot meet (`registered=0` exit 1) | ruled out by deriving both targets from states that already hold at the base (C1: the r46 counter's own frozen predicate, green at base by receipt before C1 was drafted) or that an installed tool produces directly (C2 receipts), with red do-nothing controls proving the targets are not free. |
| r45 — the different-instrument limit (0-to-green by swapping instruments; axis-fit unprovable) | ruled out by re-using the r46 instrument byte-unchanged for C1 (its sha-pin kills any drift) — no new instrument, so no instrument-swap 0-to-green exists — and by C2 measuring produced artifacts, not instrument agreement. |
| r43/r45 — L2-floor waves (lane-dead attempts, undispatched plans) | ruled out: no dispatch surface exists on this host; the round declares no wave-dependent claim (dispatched=0 disclosed; L0 question standing). |

## Landed changes

| change | commit | LOG evidence |
|---|---|---|
| freeze: preregistration, populations, counter, controls, before-census + NTFS base receipts, S270 capture | `0027c977452e06d041a750a5a8c33b1fd5de57db` | LOG.md round-47 bullet 1 |
| content: SCORECARD corrections + round-47 section; SOURCES S270; lesson (2 mistakes); LOG entry; C2 receipts TSV + provenance + spin probe + selftest-identity + r17 receipts; souji-verify repair | `08646f362cf50b662e4898b2fed37b5ab82235b9` | LOG.md round-47 bullets 2–5 |
| end receipts: C1 tip receipt, C2 counter tip receipt, census-after, NTFS tip re-check | `04b5e319322543c77472149973adb2cb47804764` | LOG.md round-47 bullet 5 |

All three commits authored `souji-shokunin <souji@shokunin.local>` through
the index-free plumbing helper, named paths only, pushed to origin master
(`git ls-remote` printed each sha at landing). After each landing the host
index was repaired for exactly the committed paths (targeted
`update-index --cacheinfo` with HEAD mode+blob after sha256 byte-verify);
porcelain ends at exactly the six tolerated control-char-named staged
deletions. The report file is fleet-side (not committed by the lane).

## Before → after measurements

| claim | before → after (counting command) | measured commit |
|---|---|---|
| C1 correction rows | `grep -c "^R46-CORRECTIO[N]" SCORECARD.md` reads `0` at base e469084b → `3` at the tip | `04b5e319322543c77472149973adb2cb47804764` |
| C1 standing instrument | `python -B census/round-46/c1-counter.py --root . --rev 04b5e319322543c77472149973adb2cb47804764 --work <scratch>` prints `SUMMARY assertions=538 mismatches=70 registered=70 corrected=0 exempted=0 unfiled=0` (base, after the index repair: assertions=533, same shape — `records/c1-base-green.txt`; +5 new assertions, all resolving) | `04b5e319322543c77472149973adb2cb47804764` |
| C1 freeze grammar | `python -B tools/souji-freeze-check.py --root . --prereg census/round-47/preregistration.txt --rev 04b5e319322543c77472149973adb2cb47804764` prints `SUMMARY claims=2 findings=0` at the freeze `0027c977452e06d041a750a5a8c33b1fd5de57db` and at the tip | `04b5e319322543c77472149973adb2cb47804764` |
| C2 receipts | `python -B census/round-47/c2-counter.py --root . --rev 04b5e319322543c77472149973adb2cb47804764` prints `RECEIPTS rows=4 targets=4 findings=0` (base: the receipts path absent, `git cat-file -e` rc 128 — the do-nothing control) | `04b5e319322543c77472149973adb2cb47804764` |

Detail:

- **C1** — the three append-only corrections carry the receipt-backed values:
  (a) the r46 cell literal `assertions=522` superseded by the measured 533
  (`census/round-46/records/c1-tip-green.txt` at 32f48da0…, verifier §3, own
  base re-run `records/c1-base-green.txt`); (b) the r46 report prose "56
  W04" superseded by 57; (c) the r46 before-census citation corrected to a
  host-valid base (`records/census-conf-name-host.txt` rc 2 plus this
  round's `records/census-before.txt` rc 0, 57 W04). The standing instrument
  re-derives green at the tip (`records/c1-tip-47.txt`).
- **C2** — raw verdicts (`records/per-artifact-receipts.tsv`, one invocation
  of `bash tools/souji-verify.sh <T1..T4>`, rc 0, tool sha e6cb3f93…):
  kotodama `NOT-SAFE secrets-refusal`; binary-forensics `NOT-SAFE dirty
  unpushed=0 dirty=153` (live unpushed work confirmed by real diffs;
  131→150→153 across the round's three observations); reverse-engineering
  `NOT-SAFE secrets-refusal`; helpers-r74 `NOT-SAFE none
  obsidian=no-matching-ledger-row; stale=not-scratch-type`. Nothing moved,
  deleted, or proposed for removal; secret-shaped descendant findings are
  routed (kagi/operator), never read.

## Sources & frontier

Census before→after (explicit-lane-directory form — the conf-name form stays
rc 2 on this host, PROVINCE correction): before
`census/round-47/records/census-before.txt` rc 0, `shokunin-repo-hygiene ok`,
57 W04; after `census/round-47/records/census-after.txt` rc 0, 58 W04, rows
193 → 194. Command:
`bash <fleet>/scripts/sources-census.sh validate --root <fleet-root> <lane-dir>`
(exit 0 required at round end: held). The +1 W04 is S270 itself sharing
git-scm.com/docs/git-clone with S102 (r21 relocation transport) across
different scopes — a warning, not a finding (S125 precedent). S270 opened
live 2026-10-31 (HTTP 200; capture
`census/round-47/sources/git-clone-located-quote.txt`); located quote
(18 words): "Clones a repository into a newly created directory, creates
remote-tracking branches for each branch in the cloned repository"
(DESCRIPTION ¶1). Sourced claim: C2 (the no-origin-master naming half). No
existing row's status, recheck or used-by cell changed. Mistakes mined:
`corpus/lessons/round-47.md` `## Mistakes` (2 rows, each with receipts and a
fix executed this round).

Assimilation: none — the lane repo holds no `considerthese/` directory
(named-path check 2026-10-31) and shokuknow is unreachable from this host.

## Trend verdicts

- **expansion: unchanged** — no knowledge entry, no Core promotion, no
  capability row; one sourced row (S270) on existing receipt-ground and the
  conversion of census classifications into receipts on already-enumerated
  targets.
- **quality: unchanged** — no admitted entry was re-verified or superseded;
  the souji-verify repair is behavior-preserving by the selftest-identity
  receipt and fixes termination only (a real host operability defect, but no
  score move is claimed and no admission rests on it).
- **discernment: improved** — two real mistakes mined with root causes,
  receipts and executed fixes (host index drift outside the frozen
  tolerance; `find_repo_for` infinite spin off-Windows-invisible); a
  self-reference trap in the round's own counting command (the marker
  literal appearing in the measurement table) was caught before data;
  preregistration frozen control-first with red controls; fresh-start
  rulings derived from the three rejected closures.

## Stale-lane

This respawn-per-round assignment is the sole souji mission; no abandoned
concurrent lane mission.

## SHONEN

- [~] Decision tables/error patterns/checklists: `SKILL.md` (receipt
  taxonomy, false-SAFE signatures), `corpus/SOURCES.md` (S270 added),
  `corpus/lessons/round-47.md` Gate; this round adds the find_repo_for
  error pattern to the lesson; no named outside promotion verifier.
- [~] End-to-end domain task executed and logged: LOG.md round-47 entry;
  `census/round-47/records/per-artifact-receipts.tsv` (four real artifacts
  classified by the installed tool, dry-run, nothing removed).
- [~] Instructions executable without oral context: the frozen
  preregistration + counters + controls re-derive everything
  (`tools/souji-freeze-check.py` findings=0 at tip; commands pasted above).
- [~] No cross-domain bleed: PROVINCE.md unchanged this round;
  secret-shaped descendants routed, never read (kotodama,
  reverse-engineering verdicts cite paths only); no deletion authority
  acquired (certification OFF, K5 HELD).

Open L0 carried (operator-owned, routed around, nothing assumed answered):
souji round-44 symlink-contract disposition; souji round-46 L2-floor
disposition (dispatched=0 again this round); souji round-46 staged-package
disposition. Holds unchanged: certification OFF, K5 HELD, NAMESPACE/reap
holds, execution-bound audit attribution open.
