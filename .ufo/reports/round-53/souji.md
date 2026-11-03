# souji round 53 — report (L1: SoujiR53, attempt 1)

Lane repo: /home/vgpnk/Projects/shokunin/souji-shokunin (jj-colocated; branch master).
Base 9bf9234ae4d11c7b31706354302a9e95ad0d1f81 (the r52 non-author verifier spot-check
commit, verdict ok/admitted). Final lane tip: fd854c7c57f401bf18d2310b1b386490d593e898
(pushed; `git ls-remote origin refs/heads/master` → fd854c7c…, local=remote ahead=0).

## Work performed

Declared claims (frozen in census/round-53/preregistration.txt, freeze commit
61838b54112354acae5ae0534425f366c14e658c, before any claim receipt):

- **C1 — calibration 7 (the lane's lowest-scoring non-retired axis):** the
  annotation-agreement counter is amended to v2 (census/round-53/c1-counter.py) — the
  five named r52 limits become five checks with finding ids (MULTIPLE-ANNOTATIONS,
  RECORD-SHA-MISMATCH, INERT-CORRECTION, CORRECTION-IN-FENCE, DELETED-LINES), shown able
  to fail over six committed fixtures; the frozen v1 counter
  (census/round-52/c1-counter.py, bytes never edited) is the do-nothing control arm.
- **C2 — coverage 8:** the capture counter is amended to v2
  (census/round-53/c2-counter.py) — sort order, `#`-leading names and RECEIPT_VERSION=1
  run-receipt binding instrumented, shown able to fail over four committed fixtures plus
  a fresh committed round-53 fleet-root capture.

Work items, each with evidence:

- Round-start census (contract command): `scripts/sources-census.sh validate --root
  /home/vgpnk/Projects/shokunin souji` → exit 0 (conf form resolves lane souji on this
  host); adapter receipt census/round-53/records/census-before-receipt.txt (verify ok,
  conf_rc=0 dir_rc=0 w04=60 result=ok) + census-before.txt; base-note.txt;
  porcelain-at-base.txt (1 line: the round's own census/round-53/ dir).
- Preregistration + instruments frozen in ONE commit before any claim receipt:
  61838b54 — prereg (both predicates, kill rules, controls, counter pins), c1-counter.py
  v2 (sha256 a7928d05df794f14d5d0213ddb78d042f62819b52f5c49b3c838a1b96da1ed15),
  c2-counter.py v2 (sha256 6515b97553dd6f6d207d638de2520c4367a56a1a37ff7329b9d914c329a349b7),
  fixtures/build-fixtures.py (sha256 d5ce557ebdc715a0e2ec2cb8c8ae4c726dbd78e123eb11fedc4892f27a68339b),
  selftests (c1-selftest.txt: SELFTEST pass cases=6; c2-selftest.txt: SELFTEST pass
  cases=4), expected verdict TSVs, red do-nothing controls (c1-control-donothing.txt:
  PRISTINE FAIL C1V2-COUNTER-ABSENT; c2-control-donothing.txt: PRISTINE FAIL
  FLEET-CENSUS-ABSENT), pre-flight receipts.
- Fresh round-53 fleet-root capture with the committed tool (bytes unchanged — pinned by
  the r52 capture's TOOL_SHA256 e7e79952…): census/round-53/records/fleet-root-census.tsv
  (ENTRIES=49, tracked 22 / ignored 22 / untracked-stray 5 / symlink 0, identical class
  counts to r52) + RECEIPT_VERSION=1 run receipt binding CAPTURE_SHA256
  922112361cdd257451e2f62820815ce19493c7d94d06c73c1b40f5dc9756f904 at fleet HEAD
  6e312f2e; committed at 1a53bcabc91d97b1a930abeb0d9d23ffbae19b81.
- Claim matrices taken post-freeze: census/round-53/records/c1-matrix-v1.tsv (v1 exit 0
  on ALL SIX fixtures — the five attacks accepted), c1-matrix-v2.tsv (v2 exit 1 with the
  named finding on F2–F6, exit 0 on F1), c2-matrix-v1.tsv (v1 exit 0 on ALL FOUR), 
  c2-matrix-v2.tsv (v2 exit 1 named findings FA1–FA3, exit 0 on FH); tip receipts
  c1-tip.txt / c2-tip.txt at the content tip (both exit 0).
- Wave w1 (ONE v1 wave, 12 seats, band 8–16): scout ×1, executor ×3, scribe ×1,
  reviewer ×2, critic ×1, mutation-tester ×1, sentinel ×1, connector ×1, revenger ×1;
  attack seats 4/12 = 33% (≥25%); connectors 1 (≤2); roles span m_flash (executor, scout,
  revenger, mutation-tester), m_mim (scribe, connector, sentinel) and m_zfl (reviewer,
  critic) per the run-15 route table — no `model` argument was passed; routes came from
  the global table. WAVE-DONE received for all 12 seats; **no dead seats**; no residual
  call (the round total is 12). The planner seat is held by the L1 (frozen topology,
  never a swarm seat); a bounded planning data-walk rode scout01/connector01 items.
  Results: .ufo/waves/round-53/w1-results.json (per-seat name/agent/id/status/output);
  the lane-local wave dir is gitignored, findings copied into
  corpus/lessons/round-53.md `## Wave findings`.
- Independent reproduction inside the round: S53executor01 AGREE 12/12 C1 matrix cells
  (rebuilt fixtures, both arms); S53executor02 PASS on every C2 predicate line + the
  real capture verifies (exit 0 receipt=ok sorted=ok) + the r52-prose-receipt grammar
  boundary is real (RECEIPT-MALFORMED); S53executor03 standing receipts (below).
- Attack findings (all classified named-limit vs routed-defect in the lesson; the frozen
  bytes were never edited): R1 fence grammar backtick-only (tilde/4-tick bypass);
  R2 zone-edge truncation (a `(79)` at offset 30 reads `stated=7`); R3 a correction's
  `recomputed=` never validated on a matched site; R4 `#`-shape refusal
  no-whitespace-only (sentinel S1 HIGH; scribe shape matrix; reviewer02 5b/5d/5e/5f);
  R5 receipt extra keys / CRLF unnamed; R6 tool pin absent (hardening routed:
  `--tool-sha256`); R7 fixture coverage (receipt-ENTRIES + symlink branches unexercised —
  mutation01 8/10 killed, 2 survivors M-F1/M-F2); R8 builder hardening (sentinel S3 LOW);
  R9 oracle/builder not digest-pinned (sentinel S4); R10 fixture rev determinism;
  R11 receipt binds bytes not path; R12 exit-code ambiguity (inherited); R13 wording
  drifts (critic: both claims SURVIVE the frozen predicate; the titles' "closes" wording
  is partially falsified — named limits routed, not kill-rule fires).
- Frontier step: S276 opened live (gitignore(1) PATTERN FORMAT comment rule; HTTP 200,
  50560 bytes, sha256 8b10cfe3d03aabce47fb5259b00d6ac7071d9c2c034d6b4410cbc2abaa983fcd;
  located quote 9 words "A line starting with # serves as a comment.", verified a
  substring of the tag-stripped capture by the scribe seat AND re-verified by the L1);
  knowledge entry corpus/knowledge/fleet-root-capture-receipt-grammar.md admitted
  (source S276; provenance trio; recheck = the v2 counter command).
- Closed r52 routed items: the `.omp` name-rule dedicated control landed (S53revenger01:
  tracked `.omp/` accepted rc 0, credential-shaped `.env` refused rc 2 — the r52 fix
  shown able to fail); freeze-message discipline verified PASS against
  `git show --stat 61838b54`; dated-observation census (S53scout01): 17 live-claim rows
  examined — 12 expired dated observations (none transcription defects), 3 reproduce
  exactly, 2 not re-derivable; no correction proposed; the two r52 routed dated
  observations (LOG.md:18, corpus/README.md:40) reproduce at the r53 tip.
- New defect found and filed (post-wave L1 sweep): two r52 annotations state
  "corpus/SOURCES.md 274 -> 275 rows" (LOG.md:2527, corpus/README.md:870); the census
  command recomputes 198 at f778b9d1 and 199 at 9bf9234a (200 with S276) — the figures
  are the last row's S-ids misread as a count. Filed by R53-CORRECTION lines in
  SCORECARD.md (append-only; the stale texts stay).
- Landing-suite defect found and resolved: the r46 landing suite at the r53 tip read
  unfiled=4 (the r53 measurement table's four bare receipt tokens
  `c1-matrix-v2.tsv`/`c1-tip.txt`/`c2-matrix-v2.tsv`/`c2-tip.txt` at SCORECARD.md
  lines 1276–1277 do not resolve); registered as R53-01..04 in the r44 register
  (corpus/lessons/round-44.md, derived full paths, scope r53-measurement-table-bare-tokens);
  the suite then reads registered=74 unfiled=0 rc 0 at 13b5d23f
  (census/round-53/records/landing-suite-tip.txt).
- Standing no-harm receipts at the r53 tip (census/round-53/records/standing-tip.txt):
  r52 c1 counter filed=2 unfiled=0 rc 0; r52 c2 counter exit 0 on the r52 capture;
  r51 c1 counter corr=ok dup=ok ntfs=ok listing=ok rc 0; r51 c2 counter shape=ok
  drift=ok receipts=ok limit=ok rows=126 added=79 removed=2 rc 0; NTFS exclusion
  tolerance not widened (6 at the r51 base, 6 at the r53 tip, same bytes — executor03).
- End-of-round census: census-after.txt + census-after-receipt.txt (verify ok,
  conf_rc=0 dir_rc=0 w04=61 result=ok) — exit 0 at round end ✓.
- Misroot sweep before the report: `git -C /home/vgpnk/Projects/shokunin status
  --porcelain` → only .scratch/* rows (orchestrator-owned run state, never a misroot);
  no seat wrote anything at the fleet root. One L1 misroot incident was self-caught and
  reverted (below).
- Tool installs: none (no tool was installed or upgraded by the L1 or reported by a seat;
  nothing to record under the tooling authorization).

## Landed changes

Every change is tied to a LOG.md entry (## Round 53) and to the commit that carries it:

| commit | carries |
|---|---|
| 61838b54112354acae5ae0534425f366c14e658c | freeze: prereg + both v2 counters + fixture builder + selftests/expected TSVs + red do-nothing controls + pre-flight receipts (census-before, base-note, porcelain-at-base) |
| 1a53bcabc91d97b1a930abeb0d9d23ffbae19b81 | C2 capture: fleet-root-census.tsv + RECEIPT_VERSION=1 run receipt (tool bytes unchanged) |
| a1156d8579847dccc9185cc677c4e23e277e7123 | content: S276 registry row + knowledge entry fleet-root-capture-receipt-grammar.md (same commit, K1) + S276 source captures + lesson round-53 (Gate, wave findings, Mistakes) + LOG round 53 + README frontier note |
| 52b98434f68050e8d24e8e15ccf4aaf960cef70b | measurements: SCORECARD r53 corrections (R53-CORRECTION ×2, append-only) + r53 measurement table + planned r54; SKILL r53 contracts (both v2 gates, pinned digests); matrix receipts + tip receipts + run-matrix.sh |
| 13b5d23fc64cbef17e1b52506943ca4f8db136ab | register: R53-01..04 in the r44 register (the four bare tokens' derived full paths) |
| fd854c7c57f401bf18d2310b1b386490d593e898 | end-of-round checks: census-after + receipt, landing-suite receipt at 13b5d23f, standing receipts at the r53 tip |

## Before → after measurements

One per claim; each counting command is pasteable and was re-run at the named commit
(the L1's own runs; independently reproduced inside the round by S53executor01 (C1,
12/12 cells) and S53executor02 (C2, every predicate line)).

**C1 (calibration 7 — instrument kill-power).**
- Before (v1 arm = the do-nothing control instrument, frozen r52 bytes): v1 exits 0 on
  ALL SIX fixtures, including the five attack states —
  `python3 -B census/round-52/c1-counter.py --root <fixture> --rev <tip> --scratch DIR`
  per fixture; receipts census/round-53/records/c1-matrix-v1.tsv (measured at the
  fixture tips; fixture bytes deterministic, commit ids wall-clock dependent — named
  limit R10).
- After (v2 arm): `python3 -B census/round-53/c1-counter.py --root <fixture> --rev <tip>
  --base <base-or-tip> --record-sha256 <fixture pin> --scratch DIR` → exit 1 with the
  named finding on F2–F6, exit 0 on F1; receipts census/round-53/records/
  c1-matrix-v2.tsv. Real lane: `python3 -B census/round-53/c1-counter.py --root LANE
  --rev a1156d8579847dccc9185cc677c4e23e277e7123 --base
  9bf9234ae4d11c7b31706354302a9e95ad0d1f81 --record-sha256
  2b90a262c29772d4a9a7bd5ab29ce06b9d8f350832f0d0cd5114d52b0f6dad30 --scratch DIR` →
  `SUMMARY sites=2 mismatches=2 filed=2 unfiled=0 record_sha=ok appended=ok multi=0
  inert=0 fenced=0`, exit 0 (census/round-53/records/c1-tip.txt).
- Do-nothing control (committed at the freeze): census/round-53/controls/
  c1-control-donothing.txt — `PRISTINE FAIL C1V2-COUNTER-ABSENT` at base (the amended
  instrument does not exist without this round's work; the honest state was already
  green under v2 at base — disclosed inside; the claim's work is the kill-power).

**C2 (coverage 8 — instrumented grammar surface).**
- Before (v1 arm): `python3 -B census/round-52/c2-counter.py --root <fixture> --rev <tip>
  --scratch DIR` → exit 0 on ALL FOUR fixtures including the three attack captures;
  receipts census/round-53/records/c2-matrix-v1.tsv.
- After (v2 arm): `python3 -B census/round-53/c2-counter.py --root <fixture> --rev <tip>
  --capture census/round-52/records/fleet-root-census.tsv --receipt
  census/round-53/records/fleet-root-census-run.txt --scratch DIR` → exit 1 with the
  named finding on FA1–FA3, exit 0 on FH; receipts census/round-53/records/
  c2-matrix-v2.tsv. Real capture: same command with `--root LANE --rev
  1a53bcabc91d97b1a930abeb0d9d23ffbae19b81` → `SUMMARY entries=49 rows=49
  unclassified=0 class_mismatch=0 counts=ok tool_sha=ok removal_proposed=0 receipt=ok
  sorted=ok`, exit 0 (census/round-53/records/c2-tip.txt).
- Do-nothing control (committed at the freeze): census/round-53/controls/
  c2-control-donothing.txt — `PRISTINE FAIL FLEET-CENSUS-ABSENT` at base.

No owned axis score changed (calibration 7, coverage 8, operability 8): both claims are
instrument amendments; the honest states stay green (no-harm, standing receipts above).

## Sources & frontier

- Census before (round start): `scripts/sources-census.sh validate --root
  /home/vgpnk/Projects/shokunin souji` → exit 0 (census/round-53/records/
  census-before.txt + v1 receipt, verify ok, w04=60). Census after (round end): exit 0
  (census/round-53/records/census-after.txt + v1 receipt, verify ok, w04=61 — the +1 is
  the S276 duplicate-URL warning, disclosed; W04 is the lane's expected shared-URL
  warning class).
- Registry rows before → after: `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|'
  corpus/SOURCES.md` → 199 before (at base 9bf9234a) → 200 after (with S276).
- Rows added by tier: A: 1 (S276, gitignore(1) manual — docs). B/C: 0.
- Rows touched old→new: S276 only (drafted `queued` → landed `mined` in the same commit
  as the entry it cites); no existing row's status, recheck or used-by changed.
- Frontier rows advanced: none (no ground line added; the entry lands on the Core
  surface the lane already owns — fleet root hygiene; corpus/README.md r53 note).
- Sourced claim: C2's knowledge entry (fleet-root-capture-receipt-grammar.md) cites S276,
  opened this round; the entry's `source:` and the S276 row's `used-by` agree (K1-checked
  by the scribe seat on a fixture: 0 new K1 findings; E-codes 0).
- Mistake mined: corpus/lessons/round-53.md `## Mistakes` — six rows (instrument
  narrower than title; oracle/builder unpinned; fixture rev determinism; builder
  hardening; the 274→275 annotation class; the control-design correction), each with
  class · evidence · captured-by · fix.
- Assimilation: none — shokuknow's merge/souji package stays held by the open r46 L0
  question on mass id drift; this round adopted nothing from it.
- considerthese/: no such directory in this lane (`ls | grep -ci consider` → 0).

## Trend verdicts

- **expansion: improved** — one admitted knowledge entry on ground the coverage map did
  not hold (the capture grammar + RECEIPT_VERSION=1 receipt binding), `source:` citing
  S276 opened this round; SOURCES 199→200 rows; no capability row owed (no new
  capability — both claims amend existing instruments).
- **quality: improved** — two instruments' kill-power raised over committed attack
  fixtures (the matrices); the r52 `.omp` control closed (shown able to fail); no
  admitted entry failed a re-check (standing receipts green at the tip); the two stale
  r52 annotations found and filed append-only.
- **discernment: improved** — the wave's attack seats found 13 routed defects in the
  frozen instruments and every one is named, classified and routed (not hidden); the
  critic's falsification (the titles' "closes" wording is partially falsified while both
  frozen predicates survive) is recorded verbatim in the lesson; the two stale
  annotations the r52 round missed were caught by this round's own sweep. Spot-check
  result: pending the round's non-author closure (the lane does not claim it).

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources
  — SKILL.md `## Round 53 contracts` adds both v2 gate registry rows (entry commands,
  verdict maps, self-tests, pinned digests, write scope, owner); asserted by the lane
  (SoujiR53), evidence: SKILL.md r53 section; verifier: pending non-author closure.
- [~] At least one end-to-end domain task executed and logged in LOG.md — LOG.md
  `## Round 53`: the full round executed end to end (freeze → wave → capture →
  matrices → content → measurements → register → end checks), six commits; asserted by
  the lane; verifier: pending non-author closure.
- [~] Instructions executable by an agent without oral context — the v2 counters'
  selftests re-run green from committed bytes alone (`python3 -B census/round-53/
  c1-counter.py --selftest --work DIR` → SELFTEST pass cases=6; c2 → cases=4) and the
  fixture builder rebuilds every fixture from its committed bytes; asserted by the lane
  (executor01/02 reproduced both matrices from the committed builder without oral
  context); verifier: pending non-author closure.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — PROVINCE.md unchanged this
  round; the connector scan found no sibling overlap on the three worked surfaces
  (.ufo/waves/round-53/w1/S53connector01.md); asserted by the lane; verifier: pending
  non-author closure.

## Stale-lane, holds, L0, incidents

- Stale-lane: none — this is the respawn-per-round driver's souji round 53 (attempt 1;
  launched 2026-11-03T16:19:50-03:00, watchdog line 2075); no other mission of this lane
  is open; the round is progressing (six commits landed and pushed this session).
- Holds unchanged: certification OFF, K5 HELD, NAMESPACE/reap holds, execution-audit
  attribution open.
- Open L0 questions (routed around, never assumed answered): credential-shaped names
  refuse-vs-redact (souji | round-52); `ignored`-column derivation (souji | round-52);
  r46 mass id drift (souji | round-46, assimilation held); r48 census conf-form
  (souji | round-48/50; on this Linux host the conf form resolves rc 0 — recorded, the
  operator may close it for this host).
- Misroot incident (self-caught, reverted, disclosed): the round's LOG entry was
  appended twice to the FLEET ROOT's LOG.md (the protocol lane's file) by a
  relative-path `cat >> LOG.md` from a temporary shell whose cwd was the fleet root;
  both times the fleet diff showed exactly the 52 appended lines and nothing else, the
  file was restored from HEAD byte-exact (`git show HEAD:LOG.md > LOG.md`;
  `git status --porcelain -- LOG.md` empty after), and the entry landed in the lane's
  LOG.md via an absolute-path write. Recorded in corpus/lessons/round-53.md Mistakes.
- Scratch discipline: every clone/fixture/work dir lived under
  /fast/scratch/hyaku/souji-r53/<seat>/ (NVMe); seats deleted their trees before
  yielding (executor03 receipts: `REMOVED rc=0 before_size=309M`); no committed tool
  hardcodes /tmp (sentinel S3 names the builder's residual gaps — routed); the L1
  removes /fast/scratch/hyaku/souji-r53 after this report.
- Wave artifacts: the lane-local wave dir (.ufo/waves/round-53/) is gitignored in the
  lane repo; the findings are copied into the lesson. The FLEET-side copy of the wave
  dir (dispatch/ready/results) remains uncommitted in the fleet repo — the same
  run-15 practice the r52 verifier routed to the protocol integrator (status-neutral;
  dispatch evidence rests on the watchdog lines + the committed prompt).
