# kasegi — round 86 report (attempt 1)

Lane repo `/home/vgpnk/Projects/shokunin/kasegi-shokunin`. Base `d7296645c2cd9f631329fa8e2f38328a4c9c89a5`, freeze `252df0c90c066d83d229e3107811a6bc05e8feed`, final lane hash `0299cb279cb56431e839557b7ce26cafa3be449e` (`git ls-remote origin refs/heads/master` prints it). L1: KasegiR86. Stale-lane: respawn-per-round driver; no other mission of this lane is open. Earlier attempts: none (`.ufo/watchdog.log` shows only the attempt-1 launch line for round 86).

## Work performed

Declared claims (frozen in `.ufo/waves/round-86/claims.json` at `252df0c9`, every control executed and committed before the freeze):

- **C1 — depth:verifiability** (lowest axis, score 4). Repoint 203 distinct bare snapshot citations in `corpus/knowledge/*.md` to full lane paths, so the resolve.py meter over the knowledge scope goes 398/1721 → exactly 596/1716 (counter `.ufo/waves/round-86/c1/knowledge-meter.py`, limbs M1–M6).
- **C2 — coverage** (held 8; capability extension of `priced-claim-package`). Build the second priced practice package `corpus/practice/curl-ibb-h1-1997312` (HackerOne IBB report 1997312, payer side of CVE-2023-28319), passing a new subject-bound counter `.ufo/waves/round-86/c2/e2e-check.py` (E0–E5). This is the round's sourced claim (S122, S123).

Work items:

- Protocol load and history: r85 spot-check routed defects 1–4 (`corpus/lessons/round-85-verifier-spotcheck.md` §6); r85 plan rows (`SCORECARD.md` Round 85). The planned "second SKILL tranche" was found to be 31 command strings, not citations (lesson M86-1), so C1 moved to the knowledge scope.
- Sources opened by the L1, then captured: S122 and S123 (`corpus/source-snapshots/round-86/`, manifest quotes rc 0 via `source-recheck.py`).
- C1 pre-freeze controls (`.ufo/waves/round-86/controls/c1-controls-r86.txt`): do-nothing 398/1721 rc 1; partial 494/1716 rc 1; de-cite 398/1518 rc 1; pad 597/1717 rc 1; wrong-file M4 rc 1; wrong map sha M6 rc 1; positive 596/1716 rc 0.
- C2 pre-freeze controls (`.ufo/waves/round-86/controls/c2-controls-r86.txt`): 22 negatives rc 1 (absent package, r85 package, r43 exemplar, two B3-class wrong-subject packages, 17 pricing forgeries), positive pricing rc 0.
- C1 landing `fdb5f4af`: P1 `KNOWLEDGE-METER base=398/1721 after=596/1716 target=596/1716 keys=203`, M1–M6 pass, rc 0; P2 10/10 instrument sha256 OK; P3 only `corpus/knowledge/` (14 files, 292 lines); P4 density 273.2 (`.ufo/waves/round-86/l1/c1-landing-r86.txt`).
- ReviewC1Semantics Finding 1: 4 keys (`S020.txt`, `S021.txt`, `S023.txt`, `S025.txt`) quote the round-40 manifest record's `path` field; the repoint misquoted it. Reverted in `e73c1f94`; tip meter 596/1720 (`.ufo/waves/round-86/l1/c1-correction-r86.txt`).
- ExecC1Registry: 198/203 values match the registry capture path, 5 rows name none, 0 contradict (`.ufo/waves/round-86/w1/ExecC1Registry.md`). ExecC1Harm: no lane gate verdict changes (`.ufo/waves/round-86/w1/ExecC1Harm.md` §Verdict).
- C2 kill: S122 as captured carried HackerOne-issued AWS STS presigned-URL session-token material. The r43 gate's R-NOSECRET refuses it (E1) while E2 requires those exact bytes (`.ufo/waves/round-86/w1/ExecC2Package.md`, `.ufo/waves/round-86/w1/ReviewC2Package.md` F-1, `.ufo/waves/round-86/w1/CriticClaims.md` B1).
- Credential incident: the token was pushed live in freeze `252df0c9` (expiry 2026-11-07T01:58:29Z). The same shape was already in a pushed r85 receipt. Both, plus three seat copies, are redacted at the tip (`.ufo/waves/round-86/l1/redact-presigned-r86.txt`); history unchanged. L0 question filed.
- Package integrated post-freeze with ReviewC2Package F-2..F-8 applied (`.ufo/waves/round-86/l1/build-package-r86.py`): gate `rules=8 pass=8 verdict=WELL-FORMED`, redaction scan `bad=0` (`.ufo/waves/round-86/l1/redaction-scan-r86.txt`). The frozen counter passes E0–E5 on the redacted bytes and fails E1/E2 on the frozen bytes (`.ufo/waves/round-86/l1/c2-postfreeze-r86.txt`). This is post-freeze evidence, not admission.
- Frontier step: S122/S123 queued → mined; R137 added; three mistakes mined (`corpus/lessons/round-86.md:49-71`).
- Swarm: one v1 wave `w1`, 12 seats, validated under `ufo-wave-policy.json` (spawn 12), dispatched via the inline handoff (`.ufo/waves/round-86/w1.ready`, WAVE-DONE received). Roles: executor×3 (ExecC2Package, ExecC1Registry, ExecC1Harm), reviewer×2, mutation-tester×2, critic×2 (CriticClaims, CriticRoot), scout×1, scribe×1, connector×1. Attack seats 6/12 = 50 %. Dead seats: 0; all 12 wrote reports. `w1-results.json` carries no outputs (orchestrator kernel restart note), so the evidence is the seat report files. No residual call; round total 12. The validator refused `labrat` as a role, so that item ran as critic CriticRoot. Planner seat: held by the L1 (validator rejects `planner`).

## Landed changes

| Commit | Change | LOG.md |
|---|---|---|
| `252df0c90c066d83d229e3107811a6bc05e8feed` | freeze: claims, counters, map, controls + receipts, S122/S123 captures + manifest, SOURCES rows queued | `LOG.md:2953` (Round 86) |
| `fdb5f4afda6999765a9be6f5a3541f99c1c103d3` | C1 landing: frozen map applied to 14 knowledge files | `LOG.md:2953` |
| `e73c1f945b5c08f5ecfec13d9ff5acfaf8f865d0` | revert 4 misquoting repoints (ReviewC1Semantics F1) | `LOG.md:2953` |
| `b079a106f4108f5dea377ff72e1ef1ef5bd2efb5` | redaction of S122 + r85 receipt; package `corpus/practice/curl-ibb-h1-1997312`; S122/S123 mined; QUALITY R137; SHONEN box 2 pointer extended (shonen-form `canonical=1 SF-CLEAN exit=0`); SCORECARD/LOG/lesson | `LOG.md:2953` |
| `fd45c41ee729cff8925fb7dcf03cfc9440352cb9` | wave evidence (spec, dispatch, results, 12 seat reports and receipts; token values scrubbed) | `LOG.md:2953` |
| `1a6ea6223fbafdea5d14e591c2cbe1a8cbd45db2` | ScoutSources live KEV catalog receipt (>1 MiB, named explicitly) | `LOG.md:2953` |
| `0299cb279cb56431e839557b7ce26cafa3be449e` | round-end census receipt, tip meter reading | `LOG.md:2953` |

## Before → after measurements

- **C1** — counting command: `python3 -B .ufo/waves/round-86/c1/knowledge-meter.py --lane <git clone --shared of fdb5f4af under /fast/scratch/hyaku/kasegi-r86/> --base-rev d7296645c2cd9f631329fa8e2f38328a4c9c89a5 --map .ufo/waves/round-86/c1/repair-map.json --target 596/1716 --map-sha256 dd40455a379eb53b75bf5a15772fe675efae79eda2516ea7fac50f86420bce12`.
  - Measured at `fdb5f4af`: 398/1721 (23.13 %) → 596/1716 (34.73 %), M1–M6 pass, rc 0. **Verdict: frozen predicates P1–P4 met at the landing commit.**
  - Qualifiers: (a) 4/203 keys were quoted manifest fields, reverted in `e73c1f94`, so the tip reads 596/1720 (34.65 %; `--measure-rev 0299cb27`); do not quote 596/1716 for the tip. (b) CriticClaims calls it nominal in class: an internal repoint, external RESOLVES unmoved, score held 4. (c) P2 is quoted at `fdb5f4af`: the post-freeze S122 redaction changes two pinned instrument hashes, so P2 at the tip fails for those two pins (CriticClaims relay). (d) Root dependence: the frozen root is a scratch clone; at the lane's own path the reading is +1 (`../MISSION.md:49-56`; CriticRoot).
- **C2** — counting command: `python3 -B .ufo/waves/round-86/c2/e2e-check.py --lane . --pkg corpus/practice/curl-ibb-h1-1997312`. Frozen bytes: E1 FAIL (gate_rc 1) and E2 FAIL. **Verdict: NOT VERIFIED (killed as frozen).** After the post-freeze redaction: E0–E5 pass, rc 0, at `b079a106` (`.ufo/waves/round-86/l1/c2-postfreeze-r86.txt`); not admission evidence. Known counter limits (CriticClaims B2, MutC2Counter 15/39 killed): E0 binds labels, not the body.
- depth:density: `python3 corpus/instruments/density.py SKILL.md --label x` 273.2 → 273.2.

## Sources & frontier

- Counting command: `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md` → 121 at base `d7296645`, 123 at `0299cb27`.
- Rows added by tier: A ×2. S122 is a dataset (HackerOne JSON record of IBB 1997312); S123 is docs (the curl lead developer's 2026-01-26 end-of-bounty post).
- Rows touched old → new: S122 `queued` → `mined`, used-by `—` → `corpus/practice/curl-ibb-h1-1997312/report.md`, scope cell "which the record leaves null" → "the record carries no bounty-amount field". S123 `queued` → `mined`, used-by → the same report. Changes are logged in `corpus/SOURCES.md` Registry changes and in the lesson Gate.
- Frontier rows advanced: the r85 deferred leads (IBB 1997312, end-of-bounty post) are now mined. New deferred lead: curl `docs/BUG-BOUNTY.md`@435acbd379, "decided and paid by the Internet Bug Bounty". Rejected for the 2023 award: the IBB 80/20 split, first archived 2024-07-27.
- Census: start `sources-census.sh validate --root /home/vgpnk/Projects/shokunin kasegi` exit 0 (`.ufo/waves/round-86/controls/census-start-r86.txt`); end exit 0 (`.ufo/waves/round-86/l1/census-end-r86.txt`). Both carry the same 6 inherited W04 warnings (S028, S029, S072, S076, S080, S085).
- Mined mistakes: M86-1 (planned tranche of non-citations → R137, shown able to fail `.ufo/waves/round-86/l1/r137-check-r86.txt`), M86-2 (credential material captured and pushed), M86-3 (no full-package positive control before the freeze).
- Assimilation: none. Lane 123 ids, staged 94, 93 collisions, none identical; the guard proof is nonempty (`.ufo/waves/round-86/w1/ConnectorOverlap.md` §2). considerthese: no fitting unimplemented proposal.

## Trend verdicts

- **expansion: improved** — two tier-A sources mined (121 → 123), and a second package resolves the payer field the r85 package left open. C2 is not credited.
- **quality: unprovable-but-better** — 199 knowledge-scope snapshot citations now resolve, with anchors in range and 198 matching the registry. But the round also pushed live credential material (M86-2, redacted at tip) and briefly misquoted 4 manifest fields (reverted). The operator should rule. Non-author reviewers on record: ReviewC1Semantics, ReviewC2Package.
- **discernment: improved** — the reviewer's semantic finding was integrated, not overridden (4 keys reverted). C2 was killed on its frozen rule rather than reframed. The IBB 80/20 split was rejected as anachronistic for a 2023 award. R137 grounds a criterion in M86-1.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — `SHONEN.md` box 1 pointer unchanged (`corpus/lessons/round-47-verifier-spotcheck.md`).
- [~] At least one end-to-end domain task executed and logged in LOG.md — `corpus/practice/curl-h1-1913733/report.md`; round 86 adds `corpus/practice/curl-ibb-h1-1997312/report.md` (`LOG.md:2953`); non-author verification pending.
- [~] Instructions executable by an agent without oral context — `corpus/lessons/round-47-verifier-spotcheck.md` (unchanged).
- [~] No cross-domain bleed (PROVINCE.md still accurate) — `PROVINCE.md` unchanged; documentation only, no live target contacted.

## Operator notes

- **Open L0:** `kasegi | round-86 | …` (history of `252df0c9` and r85 receipt holds an expired HackerOne presigned STS token; tip redacted; rewrite/report decision).
- **Tool installs:** none.
- **Inherited state:** none (clean lane at start). Seat files edited by the L1: token values scrubbed in `w1/MutC2Counter.md`, `w1/MutC2Counter-receipts/satisfiability.txt`, and the candidate's `evidence/S122.txt`.
- **Misroot sweep:** `git -C /home/vgpnk/Projects/shokunin status --porcelain` shows only `.scratch/run15-wrapup/misroot-cff0b4cb/` (orchestrator-owned) and `trail-ids.txt` (1 byte, created 20:36 local, before this round's 21:55 launch; not this lane's). No misroot.
