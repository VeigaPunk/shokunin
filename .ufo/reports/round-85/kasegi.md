# kasegi — round 85 report (attempt 1)

Lane HEAD is `6013dc983867a90cf6f2cc486ac872315d8f4aba` on master. It is pushed: `git ls-remote origin refs/heads/master` prints that hash.

| Point | Commit |
|---|---|
| Base | `bc722e540c93b48ff159454b65a0f9f4630db1ed` |
| Freeze | `4a2d34f203519a87078f21a896dc8679137ff675` |
| C1 landing | `c0507adf685058cefc749c0e07e9b72e100b17a4` |
| C2 landing and bookkeeping | `a48fe8b9ee34cf4b38106ce0b2357bbff489cb1d` |
| Receipts | `170cadf4e7789197b25fb447fa5a1296933c8341`, `6013dc98` |

## Work performed

The round declared two claims, frozen in `.ufo/waves/round-85/claims.json` at `4a2d34f2`. Before the freeze I read the r84 closure and `corpus/lessons/round-84-verifier-spotcheck.md` (routed defects 1–6).

- **C1 — depth:verifiability (the lowest axis, score 4).** This is a move of the scored meter itself, the one resolve.py computes for SKILL.md, which answers r84 routed defect 3.
  - What changed: the 18 bare SKILL.md citations in `.ufo/waves/round-85/c1/repair-map.json` now carry their full lane paths.
  - Measured result: the meter goes from 158/741 to 167/732.
  - ReviewC1Semantics judged all 18 repairs correct (`w1/ReviewC1Semantics.md` §1).
  - Qualifier (CriticClaims A1): all of the gain is internal citations. External RESOLVES stay at 4/741, and the score is held at 4.
- **C2 — coverage, held at 8; claim type: capability acquisition `priced-claim-package`.** This is the round's sourced claim, resting on S119, S120 and S121.
  - What it is: the lane's first end-to-end domain task, `corpus/practice/curl-h1-1913733/`. It is a retrospective six-file practice package for disclosed HackerOne report 1913733 (curl, CVE-2023-28319).
  - Pricing comes from the platform record (S119), the vendor advisory (S120), the vendor's current policy (S121) and the KEV capture (S052).
  - It is logged in LOG.md, and SHONEN box 2 is now `[~]`.

Work items:

- **Controls**, executed and committed in the freeze:
  - C1 (`controls/c1-controls-r85.txt`):
    - Do-nothing: 158/741, rc 1.
    - Pad: 168/751, rc 1.
    - De-cite GONE citations: 158/723, rc 1.
    - Wrong target: 168/733, rc 1.
    - Partial (9 of 18): 164/738, rc 1.
    - Positive: 167/732, rc 0.
  - C2 (`controls/c2-controls-r85.txt`):
    - Package absent: rc 1.
    - The r43 exemplar copied in: E1 passes, E2–E5 fail, rc 1.
    - Eight pricing forgeries: each rc 1.
    - Positive pricing: rc 0.
- **Sources captured:** `corpus/source-snapshots/round-85/` holds S119, S120, S121 and the manifest; all 12 quotes are OK.
- **Package build:** ExecC2Package built the candidate. I integrated the ReviewC2Package fixes F-1..F-7 and CriticClaims D3 through `.ufo/waves/round-85/l1/build-package-r85.sh`. That includes a real verifier scan (`l1/redaction-scan-r85.txt`, 3 artifacts, 0 hits).
- **Census of record:** a full resolve.py run on a clone of the C1 landing gives SKILL 167/732 and lane 1755/6941 (`l1/census-of-record-c1-r85.txt`).
- **Landing receipt:** `l1/L1-landing-r85.txt`, measured over a `git clone --shared` checkout of `a48fe8b9`.
  - C1: P1 `SKILL-METER-RESULT pass rc=0`, P2 all instruments OK, P4 density 273.2 → 273.2.
  - C2: P1 `E2E-RESULT pass limbs=5 rc=0`, P2 `WELL-FORMED`, P3 S119–S121 rc 0, P4 three rows changed and registry 121, P6 box 2 `[~]`.
  - R136: `SF-CLEAN`.
- **Mistake mined, M85-1:** r84's SHONEN pointer edit broke the lane's own `shonen-form.py`. It printed `exit=1 SF-POINTER` at `c91c944f` and `bc722e54`. That is fixed, with QUALITY R136 and `l1/r136-check-r85.txt`.
- **Wave attacks recorded, not hidden** (lesson M85-2, routed to r86):
  - CriticClaims B3: a wrong-subject package passes the frozen e2e counter (rc 0).
  - E4 accepts empty quotes; E3 keeps the first of duplicate keys (ReviewC2Package R-01, R-02).
  - MutC2Counter: 6 of 20 mutants killed, 13 survived.
  - MutC1Counter: the frozen controls kill 4 of 20 mutants. Every control is still rejected by the limbs together, but no single limb is self-protecting.
  - C2's evidence that the package is about the right report therefore rests on ReviewC2Package's independent read, not on E1–E5.

## Landed changes

| Change | LOG.md entry | Commit |
|---|---|---|
| Freeze: claims, C1/C2 counters, controls, S119–S121 captures and queued rows | `## Round 85`, bullet 1 | `4a2d34f2` |
| SKILL.md: 18 citations repointed (17 lines); landing script | `## Round 85`, bullet 2 | `c0507adf` |
| Package `corpus/practice/curl-h1-1913733/`; S119–S121 mined; SHONEN boxes 1 and 2; QUALITY R136; lesson `corpus/lessons/round-85.md`; SCORECARD capability row and `## Round 85`; wave w1 evidence | bullets 3–7 | `a48fe8b9` |
| Landing receipt, census end, KEV feed receipt | bullet 2 | `170cadf4`, `6013dc98` |

## Before → after measurements

**C1**, measured at `a48fe8b9` in a checkout that has `.git`.

- Command: `python3 -B .ufo/waves/round-85/c1/skill-meter.py --lane . --base <git show bc722e54:SKILL.md> --after SKILL.md --map .ufo/waves/round-85/c1/repair-map.json --target 167/732 --map-sha256 b575f147…1944`
- Before: 158/741 = 21.32 %.
- After: 167/732 = 22.81 %. Limbs M1–M5 pass, rc 0.
- The full census run agrees: 167/732.
- Score: 4 → 4.

**C2**, measured at `a48fe8b9`.

- Command: `python3 -B .ufo/waves/round-85/c2/e2e-check.py --lane . --pkg corpus/practice/curl-h1-1913733`
- Before: package absent, E1–E5 fail, rc 1. No end-to-end task was logged. Registry 121, with S119–S121 queued.
- After: E1–E5 pass, rc 0. Gate `rules=8 pass=8 WELL-FORMED`. S119–S121 mined.
- Score: 8 → 8. The capability row `priced-claim-package` enters.

**Harm check.**

- depth:density: 273.2 → 273.2.
- SCORECARD and LOG: additions only.
- shonen-form: exit 1 → exit 0.

## Sources & frontier

- **Census command:** `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kasegi`
  - Round start: `kasegi ok`, rc 0 (`.ufo/waves/round-85/controls/census-start-r85.txt`).
  - Round end: `kasegi ok`, rc 0 (`l1/census-end-r85.txt`). Both carry six inherited W04 warnings.
- **Registry rows:** 118 → 121, counted with `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`. All three new rows are tier A and were opened 2026-11-07:
  - S119: the HackerOne JSON record, kind `dataset`.
  - S120: the curl CVE-2023-28319 advisory, kind `docs`.
  - S121: the curl vulnerability-disclosure policy, kind `docs`.
- **Rows touched (old → new):** S119, S120 and S121 each went `queued` → `mined`, with used-by `—` → `corpus/practice/curl-h1-1913733/report.md`. Recorded in the lesson Gate and in the SOURCES registry-changes block.
- **Sourced claim:** C2.
- **Frontier:** no new F-row. C2 moves the lane into practice, not into new knowledge.
- **Mistakes:** M85-1, M85-2 and M85-3 are in the lesson.
- **Assimilation: none.** The collision check found 91 collisions (lane 121 ids, staged 94). The guard was proven on an indented row, where it found 2 collisions (`w1/ConnectorOverlap.md` §3).
- **considerthese:** `2026-10-26.md` proposal 2 (the end-to-end task) is adopted as C2.

## Trend verdicts

- **expansion: improved.** The lane ran its first end-to-end domain task: a priced package built from three new tier-A sources. It also learned to keep three conflicting reward records as separate fields: has_bounty? false, "no bug bounty" today, and 2400 USD recorded in 2023.
- **quality: improved.**
  - SKILL.md citations resolve: 158/741 → 167/732, with all 18 repairs semantically correct.
  - The broken SHONEN gate is fixed (R136).
  - Counter weaknesses are recorded and routed: B3, R-01/R-02, the mutation survivors.
- **discernment: improved.**
  - The reviewer's CHANGES-REQUESTED was integrated rather than overridden: F-1 (a fabricated verifier) and F-2 ("paid" claimed where the record only shows the amount) are fixed.
  - The critic's internal-only qualifier is carried into SCORECARD.
  - This still needs the non-author closure check.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources. Evidence: `corpus/lessons/round-47-verifier-spotcheck.md`; the pointer was restored to canonical form this round (R136).
- [~] At least one end-to-end domain task executed and logged in LOG.md. Evidence: `corpus/practice/curl-h1-1913733/report.md`; LOG.md `## Round 85`. Non-author verification is pending.
- [~] Instructions executable by an agent without oral context. Evidence: `corpus/lessons/round-47-verifier-spotcheck.md`.
- [~] No cross-domain bleed (PROVINCE.md still accurate). Evidence: `PROVINCE.md:52` (documentation only). ConnectorOverlap found no sibling lane holding this ground.

## Round shape and other items

- **Shape:** one v1 wave `w1` of 12 seats, dispatched through the inline handoff (`w1.ready`, l1=`KasegiR85`; `w1-results.json` reports `seats 12`).
  - Roles: executor×3, reviewer×2, mutation-tester×2, critic, scout×2, scribe, connector.
  - Attack seats: 5/12.
  - Dead seats: 0.
  - No residual call. Round total: 12.
  - The validator rejects `labrat`, so the KEV probe ran as a scout (ProbeKEV).
- **Planner seat:** held by the L1.
- **Seat routes**, from the session files: ExecC2Package ran on commandcode/stealth/crouton-alpha. ReviewC2Package ran on zai/glm-5.3-flashx and fell back to anthropic/claude-haiku-5-5.
- **Inherited state:** none. The lane was clean at `bc722e54`, and there was no earlier attempt of this round.
- **Misroot sweep:** the fleet `git status` shows `.scratch/` and `trail-ids.txt`. `trail-ids.txt` predates this round and does not name kasegi, so it was not touched. This round produced no misroots.
- **Scratch:** `/fast/scratch/hyaku/kasegi-r85` was removed.
- **Stale-lane:** respawn-per-round driver; no other mission of this lane is open.
- **Tool installs:** none.
- **Open L0 questions:** R-77-E (staged-id collisions) and R-77-D are carried and were not re-filed.
