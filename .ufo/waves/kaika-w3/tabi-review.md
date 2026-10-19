# kaika W3 — non-author verification: tabi round 1

Verifier: W3ReviewTabi (fresh task dispatched by the orchestrator; not the lane).
Lane head: `9e3b607de722b95da2d7fa83a85d3d38fe11286a` (branch `kaika/round`); work commit `a4115fafce511b7f140ea176bcd0807ebf141fc6`; base `40a6de87f72b78d90ea627ad89717e55f219001e`.
Scratch: `/tmp/kaika-verify/tabi/` (archives `base/ work/ head/`, clone `clone/`, mutation tree `mut/`). Lane worktree read-only; `git status --short` on it is empty.
This review is a recommendation; the orchestrator adjudicates.

## Summary

**Recommendation: ADMIT WITH CONDITIONS, not a clean admit.** Provenance, append-only, credentials, the SOURCES census and every counting command reproduce. Three defects are material.

- **M-1 (Major, fix before closure):** an unmeasured host fact is written as observed fact in three places. The lane's own note labels it inference. This is the calibration axis itself.
- **M-2 (Major, promotion):** the four `[x]` SHONEN boxes name lane-dispatched verifiers. The report's L0 Q4 premise ("named non-author verifiers") does not hold under PROTOCOL.
- **M-3 (Major, scoring):** coverage 8→9 is reproducible as a count, but it is not the AXES coverage measure, and PROVINCE.md is unchanged.

Per claim: **C1 verified.** **C2 verified as count; capability verified; coverage score needs ruling (M-3).** **C3 counts verified; calibration score held at 8 until M-1 is corrected.**

## 1. Provenance (check 1) — PASS

`git log --format='%h %an <%ae> | %cn <%ce> | %s' 40a6de87f..9e3b607de`:
```
9e3b607 tabi-shokunin <tabi@shokunin.local> | tabi-shokunin <tabi@shokunin.local> | round-1: record measurements, capability, saturation and plan against a4115fa
a4115fa tabi-shokunin <tabi@shokunin.local> | tabi-shokunin <tabi@shokunin.local> | round-1: sources registry + census gate, three current-art notes, drift reconciliation, mistakes→QUALITY; r07 recorded without credit
```
Both commits carry the lane identity as author and committer. `a4115fa` is an ancestor of `9e3b607`.

## 2. Append-only (check 2) — PASS, with one benign line change

`git diff --numstat 40a6de87f..9e3b607de -- LOG.md SCORECARD.md corpus/QUALITY.md corpus/README.md SKILL.md`:
```
47 0 LOG.md   53 0 SCORECARD.md   22 0 corpus/QUALITY.md   73 0 corpus/README.md   22 1 SKILL.md
```
- The only deleted line is `SKILL.md` line 1596 at base (`safety evidence; post-commit output identifies the corrected carrying commit.` with no trailing newline). It is re-emitted with a newline, and the errata block is appended after it.
- Byte-prefix check, `cmp -n <base-size> base head` for LOG (39496 B), SCORECARD (34018 B), QUALITY (329 B), README (13486 B), SKILL (125194 B): **all PREFIX_OK.**
- `corpus/SOURCES.md` is new at this round. No in-place change exists to audit.
- Protected files unchanged (absent from numstat): `corpus/lessons/round-1.md`, `PROVINCE.md`, `SHONEN.md`, `scripts/check-freshness.mjs`.

## 3. Claims (check 3) — every counting command re-run

Script `/tmp/kaika-verify/tabi/claims.sh <rev>`, which is the SCORECARD command set with the markdown `\|` unescaped. The C3a sort is locale-pinned (see m-2).

| Claim / command | 40a6de87f (base) | a4115fa (work) | 9e3b607 (head) | Report says | Verdict |
|---|---|---|---|---|---|
| C1a `git ls-tree -r --name-only <rev> \| grep -c '^corpus/evidence/kaika-fleet-round-1/operability/selftest-receipt.txt$'` | 0 | 1 | 1 | 0→1 | verified |
| C1b `node scripts/check-sources.mjs --self-test` | exit 1 (`Cannot find module`; script absent) | `SOURCES_SELFTEST verdict=clean cases=25`, exit 0 | `SOURCES_SELFTEST verdict=clean cases=25`, exit 0 | absent → clean 25 | verified |
| C2a `git grep -l '^source: S[0-9]\{3,\}' <rev> -- corpus/knowledge \| wc -l` | 0 | 3 | 3 | 0→3 | verified |
| C2b `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md` | 0 (absent) | 27 | 27 | 0→27 | verified |
| C2c contract census (SOURCES-CONTRACT-v1 §Census), head | — | — | rows 27; malformed 0; `A=21 B=4 C=2`; `mined=19 queued=6 rejected=2`; dup/enum/inflation/missing used-by: no output | A21 B4 C2; mined19 queued6 rejected2 | verified |
| C3a unmapped knowledge notes (`comm -23` of knowledge listing vs README mentions) | 15 | 0 | 0 | 15→0 | verified |
| C3b evidence groups (`user-2*`, `pstack-2*-r*`) absent from LOG | 1 (`user-20261015-r07`) | 0 | 0 | 1→0 | verified |
| C3c training rounds 1–11 without lesson | 1 (`round-11`) | 0 | 0 | 1→0 | verified |
| C3d `grep -c 'kaika-fleet-round-1.md#mistakes' corpus/QUALITY.md` | 0 | 7 | 7 | 0→7 | verified |

Other no-harm and scope commands:

- README map diff `diff <(ls corpus/knowledge \| sort) <(grep -o 'knowledge/[a-z0-9-]*\.md' corpus/README.md \| sed 's\|knowledge/\|\|' \| sort -u)`: base exit 1 (22 diff lines); head exit 0 (0 lines). Notes 26→29; lessons 26→28.
- `check-freshness.mjs --worktree` (clone at base and head): `FRESHNESS_GATE verdict=clean matched=34 unique=34`, both. Self-test `cases=12` at head.
- `check-round-contract.mjs`: `ROUND_CONTRACT verdict=clean rounds=10`, both. Self-test `cases=4`.
- `check-user-round-contract.mjs`: `verdict=failed finding=round_count detail=Found 6 user rounds, expected 10`, both (pre-existing). Self-test `cases=4`.
- Expansion words at base (`grep -rliw`, `corpus SKILL.md PROVINCE.md`): `bidi` 0, `flak` 0 (`-i` substring), `aria` 0 (`-w -i`).

Claim verdicts:

- **C1 operability 7→8: verified.** Re-run counts reproduce. Base gate absent; head gate passes its own 25 cases. Fresh self-test output matches the committed receipt on its 25 PASS / 0 FAIL lines, and the receipt also holds the `EXIT_CODE` lines. Mutation test below shows the gate can fail.
- **C2 coverage 8→9 + capability `sources-registry`: capability verified; coverage verified as a count only.** The registry census is clean, the capability runs, and three notes sit on ground with zero base hits. The AXES coverage measure is "fraction of the domain's real surfaces the skill governs" (AXES.md table). PROVINCE.md is unchanged and no denominator is measured, so 8→9 is not re-derivable from that definition (M-3).
- **C3 calibration 8→9: counts verified; score not yet supported.** Drift 15→0 reproduces. The metric is mention-based (critic dissent is correct that it can be gamed; I sampled 3 of 15 README rows, all faithful). The round also introduces an unmeasured assertion as fact (M-1). Calibration is the axis that catches exactly this.

Mutation test (gate can fail): in `mut/corpus/SOURCES.md` S013's tier changed `A`→`D`, run `node scripts/check-sources.mjs --file corpus/SOURCES.md` from inside `mut/`:
`FINDING id=bad_tier fleet=E06 row=S013 detail=tier_invalid`, `SOURCES_GATE verdict=failed … findings=20`, exit 1. The E11 `used_by_missing` findings are artifacts of my scratch tree, which omits `corpus/knowledge/`.

## 4. SOURCES (check 4) — PASS

`bash /home/vgpnk/Projects/shokunin/.tower/worktrees/kaika/fleet-census/scripts/sources-census.sh validate /home/vgpnk/Projects/shokunin/.tower/worktrees/kaika/tabi-shokunin`:
```
tabi-shokunin	ok	/home/vgpnk/Projects/shokunin/.tower/worktrees/kaika/tabi-shokunin/corpus/SOURCES.md
EXIT=0
```
Lane gate on head tree: `SOURCES_GATE verdict=clean rows=27 tiers=A:21,B:4,C:2 status=queued:6,mined:19,rejected:2 findings=0`, exit 0. The `--since 2026-10-19` form is also clean.

Re-opened rows (fetched this session; "sha match" = raw bytes equal the Gate's sha256):

| Row | Tier | Gate quote / anchor | Re-open result |
|---|---|---|---|
| S004 `remote_debugging_server.cc` | A (code, new, mined) | anchor `.cc:160-183, 335-424; .h:28-50` | sha `ea72757acd7c3bff…` = Gate. Lines confirmed: `:164` `kDevToolsRemoteDebuggingAllowed`; `:169-170` `#if BUILDFLAG(GOOGLE_CHROME_BRANDING)` / `constexpr bool default_user_data_dir_check_enabled = true;`; `:177` `is_default_user_data_dir.value_or(true)`; `:292-294` `EnableDefaultUserDataDirCheckForTesting`. |
| S004 `.h` | A | Gate: "Enables the default user data dir check even for non-Chrome branded builds, for testing" (.h:47–48) | sha `841c6f67378c05cd…` = Gate; quote present at .h:47. |
| S001 blog | A (docs, new, mined) | "These switches will no longer be respected if attempting to debug the default Chrome data directory" | Present verbatim (line-wrapped), published 2025-03-17. Page hash differs from the Gate (dynamic page). The Gate discloses this. |
| S017 release notes | A (docs, new, mined) | "New `--shuffle` command line option schedules tests in a random order" | Present; example `shuffle seed 271828182` and replay `--shuffle 271828182` as the note states. |
| S027 duncanlock post | C (community, **rejected**) | "add `--remote-debugging-port=9222` on the end of the command line" | sha `e36d660b349e1db8…` = Gate; quote verbatim; dated 2023-05-27. |
| S026 SO answer 74926242 | C (community, **rejected**) | `await new Promise(resolve => setTimeout(resolve, 5000));` | Live API: score 13; line present. |
| S018 ICST 2025 PDF | A (paper, mined) | Table V groups 62/47/14, 123 tests, 49 projects | PDF sha prefix `9304083f19871e11` = Gate; text shows 123 tests / 49 projects and 50.4 / 38.2 / 11.4 %. |
| S002 CDP viewer | A | "CDP is not a public or supported API for Chrome, and it does not guarantee backwards compatibility" | sha `ba8018bb02f36068…` = Gate; contains `strictly requires PUT`. |
| S005 W3C WD | A (spec) | matrix negatives | Dated WD URL HTTP 200. `insertText`, `captureBeyondViewport`, `getNavigationHistory`: 0 hits each. No `browsingContext` navigation-stop command (only `stopScreencast`). |

Rows at risk: S022 Gate sha is the empty-body digest `e3b0c442…`, disclosed in the Gate. S022 is `queued`, so no admit depends on it (m-5).

## 5. Discernment spot-check (LEARNING.md) — recorded for orchestrator

| Sample | Gate decision | Check | Verdict | Reason |
|---|---|---|---|---|
| `knowledge/chrome-remote-debugging-profile-boundary.md` | admit | §2 anchors and S001/S004 quotes reproduced from fetched bytes | **agree** | Source-backed and correctly hedged in the note body (§3 `[inference]`, §4, Unknowns 1). The defect is propagation, not the note (M-1). |
| `knowledge/webdriver-bidi-capability-matrix.md` | admit | Negative claims re-tested against WD 2026-10-08 | **agree** | Zero hits for `insertText` / `captureBeyondViewport` / `getNavigationHistory`; no navigation-stop command. Every row says `locally measured: no`. |
| `knowledge/web-flake-retry-evidence.md` | admit | S017 and S018 numbers re-derived | **agree** | `--shuffle` text confirmed; 123/49 and 50.4/38.2/11.4 % confirmed; arithmetic 62+47+14=123 holds. |
| S026 (fixed 5 s sleep) | reject (C, community) | Quote in live answer | **agree** | A bare sleep records no state transition and contradicts the lane's own settle rule (SKILL §Settle-wait `:496`). Flip condition stated. |
| S027 (port 9222 on everyday profile) | reject (C, community) | Quote verbatim | **agree** | The post says "existing instance" and does not name a profile; the everyday-profile reading is an inference, but the reject is sound on the lane's shape-only rule and S001. |
| `user-20261015-r07` as round credit | reject (no credit) | Receipt sha256 and aggregate | **agree** | `sha256sum` of r01 and r07 `selftest-receipt.txt` both `77374a717a2f4e380314…`; aggregate `results` 32 × `verdict=PASS`, so the wave ran, but it adds no new capability or reviewer. |

The report says discernment is "unchanged, pending". On this sample the gate agrees 6/6. The one disagreement-class defect (M-1 propagation) is not yet a lesson; see §11.

## 6. New knowledge entries (check 6) — PASS

- Header trio present, in order, in all three notes (`source:` / `verified-at:` / `recheck:`).
- Recheck commands run: chrome note recheck (re-fetch `remote_debugging_server.cc`, check the `IsRemoteDebuggingAllowed` block); BiDi recheck (re-fetch the W3C WD, re-audit the anchors); flake recheck (Playwright docs for shuffle; ICST PDF). Chromium version from `pacman -Q chromium` → `152.0.7977.82-1` (`chromium` binary not executed).
- Claims match sources in every sampled case (§4).
- Each `used-by` in SOURCES cites the note, and each note cites its `mined` rows (census `missing used-by` = none).

## 7. Credentials (check 7) — PASS

`git diff 40a6de87f..9e3b607de | grep -nE 'op://[A-Za-z0-9]|BEGIN [A-Z ]*PRIVATE KEY|ghp_[A-Za-z0-9]{20,}|AKIA[0-9A-Z]{16}|xox[baprs]-[A-Za-z0-9]'` prints nothing (exit 1).

Broader sweep hits, both benign: `scripts/check-sources.mjs:1339` is the detector regex `/BEGIN[\s\S]{0,100}PRIVATE KEY/`. `check-sources.mjs:1439` is a synthetic self-test fixture `'ghp_fixtureSecretValue'` (19 chars, below the 20-char pattern), used by the `credential-material` case.

## 8. Report (check 8) — conforms, with one misstatement

- Required sections present: Work performed, Landed changes, Before→after measurements, SHONEN, Sources & frontier, Mistakes, Trend verdicts, L0 questions, Integrator notes.
- No `[x]` in the report's SHONEN section (all `[~]`), and no non-author attestation is claimed for this round.
- Cites round commits `a4115fa` and `9e3b607`.
- Every pointer I resolved holds: `SKILL.md:1598-1617`, `LOG.md:464-476`, `LOG.md:477-507`, `SCORECARD.md:393-421`, `corpus/README.md:161-169` and `:171-194`, `corpus/lessons/kaika-fleet-round-1.md:12-30` (Mistakes) and `:32-84` (Gate), `corpus/QUALITY.md` criteria 6–13, `corpus/evidence/kaika-fleet-round-1/{operability/selftest-receipt.txt,sources/census-receipt.txt}`, and `corpus/knowledge/multi-step-journey.md` / `executor-test-sufficiency.md`.
- Mistakes evidence re-run: M1 `git cat-file -t b377007877be2d104cc9e3da56cf81a24ab0d` → fatal, rc 128. M7 Brave in 21 of 26 lesson files. M11 `round-11.md` absent at base. M12 README `:5-9` text. M4 SKILL `:1577` erratum. All hold.
- Misstatement: the report's C2 knowledge bullet says "This host's unbranded Chromium 152 does not enforce it" as fact. The note labels the same claim as inference (M-1).
- SHONEN file pointers: each `[~]` pointer resolves.

## 9. Per-axis recommended verdicts

| Axis | Lane self-score | Recommended | Basis |
|---|---|---|---|
| depth | 8 → 8 | **8 (unchanged)** | No depth claim; SKILL errata rows are not a depth move. |
| coverage | 8 → 9 | **8, pending ruling on M-3** (9 only if the orchestrator accepts the note/row count as the coverage measure) | Count reproduces; not the AXES fraction; PROVINCE.md unchanged. Capability `sources-registry` verified separately. |
| operability | 7 → 8 | **8 (verified)** | C1b, mutation test, receipt match. |
| freshness | 8 → 8 | **8 (unchanged)** | FRESHNESS_GATE clean 34/34 at base and head; new notes carry dated recheck lines. |
| calibration | 8 → 9 | **8 until M-1 is corrected and M-2 is handled** | Drift 15→0 reproduces; the round adds an unmeasured fact as observation in SKILL errata, README and LOG; SHONEN verifier labels overstate non-author review. |
| adjacency | 8 → 8 | **8 (unchanged)** | kaidoku Playwright install cited, not absorbed; no bleed found. |

## 10. Defects by severity

**Major**

- **M-1 — Inference promoted to observation (calibration; QUALITY #3).**
  - Note labels it inference: chrome note §4, `corpus/knowledge/chrome-remote-debugging-profile-boundary.md:59-60`: "[inference: the check is branding-gated §2 — the refusal was never measured locally]". Unknowns 1, `:108`: "never observed because branded Chrome is not installed".
  - Stated as fact in three places:
    - `SKILL.md:1606` (errata decision row): "this host's unbranded Chromium does **not** — never rely on the browser's refusal as the guard".
    - `corpus/README.md:167`: "so this host's unbranded Chromium does not enforce it".
    - `LOG.md:491`: "unbranded Chromium here does not enforce it".
  - The report's C2 bullet has the same wording.
  - The source supports the inference (`IsRemoteDebuggingAllowed` gate is branding-gated, default `false` unless the test hook runs), but nothing was measured. Measuring would require the user's default profile, which the lane forbids.
  - Fix as an appended correction commit: reword each to "source-level inference (unmeasured on this host)" and cite the note's §4.
- **M-2 — SHONEN `[x]` verifiers are lane subagents (promotion; PROTOCOL §Promotion gates).**
  - `SHONEN.md:6-7`: "verifier: TABI-B4, scribe, non-author; corroborated by the TABI-R3-4 executor test". `:15-16`, `:22-24`, `:31-32` name the same seats. These are lane-dispatched (PROTOCOL: "a subagent the lane dispatched is still the lane").
  - Under the gate, those four `[x]` count as `[~]`.
  - The report's L0 Q4 premise, "SHONEN has been 4/4 with named non-author verifiers since round 3", is therefore unsupported. The orchestrator should not count it as promotion evidence. Route to the operator; SHONEN is byte-pinned, so the re-baseline is an operator act.
- **M-3 — Coverage measure is not the axis definition (scoring).**
  - AXES: coverage = "fraction of the domain's real surfaces the skill governs"; PROVINCE.md unchanged; C2 measures note and row counts. Ruling needed (see §9).

**Minor / notes**

- **m-1 — Drift counter blind to kaika evidence groups.** The C3 pattern `^(user-2|pstack-2.*-r)` does not match `kaika-fleet-round-1`. The integrator note acknowledges this. A future unrecorded kaika group would not show in C3b.
- **m-2 — C3 command sort locale.** As printed (`sort` without `LC_ALL=C`), base emits `comm: input is not in sorted order` on this host. The value 15 reproduces; the stderr noise does not.
- **m-3 — C1 counting command cannot fail.** `node … --self-test | tail -1` returns `tail`'s exit status. The receipt holds `EXIT_CODE` lines, so the evidence is fine; the printed command is not.
- **m-4 — `--file REL` resolves against the script's repo.** Observed: run the head script from `mut/` with `--file corpus/SOURCES.md`; it read head's file, not `mut/`'s. The usage text does not say so.
- **m-5 — S022 Gate sha = empty-body digest** (`e3b0c442…`). Disclosed in the Gate; `queued`; no admit depends on it.
- **m-6 — SKILL.md no-EOL line.** Benign; byte-prefix holds (§2).
- **m-7 — QUALITY 6–11, 13 are prose; no gate enforces them.** Each cites a Mistakes row with captured-by `none` before this round (verified in the lesson table). Enforcement is not claimed.
- **m-8 — Round "Mistakes" M1 evidence** uses a 37-hex pin; carried as O13 and left unrepaired. Reported, not a defect of this round.

## 11. Trend verdicts (expansion / quality / discernment)

- **Expansion: improved.** Three admitted notes on ground with zero base hits (`bidi` 0, `flak` 0, `aria` 0 word-level). Each cites `mined` rows, census clean. Caveat: `--user-data-dir` hygiene was already in 109 files; the new fact is the ≥136 refusal's branding gate, which was absent.
- **Quality: improved, conditional on M-1.** New entries pass the header trio, recheck and source checks (§4, §6). No existing entry was re-verified and found stale. The overstatement in SKILL/README/LOG is a quality defect in a durable row.
- **Discernment: improved on this sample (6 of 6 agree, §5), conditional.** The propagation defect (M-1) must become a lesson with a grounded QUALITY criterion, as LEARNING requires. If it is left unlearned, the verdict becomes `harmed`.

## 12. Admit / reject recommendation

**ADMIT WITH CONDITIONS.**

1. **C1 operability 7→8:** admit.
2. **C2:** admit the `sources-registry` capability and the expansion. Hold coverage at 8 unless the orchestrator accepts the count measure (M-3).
3. **C3 calibration:** hold at 8 until M-1 is corrected by an appended commit (SKILL errata row, README `:167`, LOG `:491`, and the report's C2 wording). The lesson records the propagation miss as a discernment disagreement.
4. **SHONEN / promotion:** no `[x]` promotion. Correct the L0 Q4 premise and route to the operator (M-2).
5. Log m-1 to m-8 as integrator notes.

## 13. Verification gaps

- The 11-seat swarm dispatch, `/skill:godspeed` and verbatim `directive.md` bytes, and the executor stalls: no transcripts in my inputs; unverified.
- The host-enforcement claim is source-level only. Measuring it needs the user's default profile, which the lane forbids.
- Mention-count gaming for C3: 3 of 15 README rows sampled (`archive-receipt-r5`, `closeout-r11`, `async-step-evidence`); all faithful. Not a full audit.
- S001 live page differs from the Gate sha (dynamic page; disclosed). Quote verified.
- `user-20261015-r07` aggregate counted from `results[].verdict`; seat-level content not re-read.

## 14. Cleanup

Scratch `/tmp/kaika-verify/tabi/` is deleted after this file is written. No file in the lane, the fleet ledger, or any sibling was modified. No branch was switched and nothing was staged or committed.
