# kaika W3 — non-author verification: kagi round 21

Reviewer: `W3ReviewKagi` (non-author; the lane `kagi-shokunin` authored both commits). Subject: `kaika/round`, base `aea7a4301`, head `e1544c194`. Scratch `/tmp/kaika-verify/kagi/` (deleted after this write). Fetched web content was treated as data.

## Recommendation

**REJECT as landed.** The AXES admission rule requires every claim to verify and no axis to be harmed. C2 (calibration) does not verify as an axis move, and as landed the expansion trend fails the LEARNING.md "harmed" test (entries E1 and E3 fail their own admission bar as written).

**Partial admit recommended:** C1 (depth 8→9) verifies, and the C3 capability row (source registry + census gate) verifies. The three knowledge entries and the C2 claim need the repairs in D1–D3 before they can be admitted.

## Check results

1. **Provenance: PASS.** `git -C <wt> log --format='%h %an <%ae> | %cn <%ce> | %s' aea7a4301..e1544c194` →
   `e1544c1 kagi-shokunin <kagi@shokunin.local> | kagi-shokunin <kagi@shokunin.local> | round-21: post-landing correction …`
   `c41af82 kagi-shokunin <kagi@shokunin.local> | kagi-shokunin <kagi@shokunin.local> | round-21: admit dotenv byte contract …`
   `git merge-base --is-ancestor c41af82 e1544c194` → yes. Branch `kaika/round`; `git status --short` empty.

2. **Append-only: PASS for the named files.** `git diff --numstat aea7a4301 e1544c194 -- LOG.md corpus/lessons corpus/QUALITY.md` → `LOG.md 80/0`, `corpus/QUALITY.md 65/0` (new), `corpus/lessons/round-21.md 121/0` (new). `grep -nE '^-[^-]'` over that diff → no output. `corpus/SOURCES.md` is new (0 deletions).
   Outside the named list, in-place edits exist: `corpus/claim-ledger.tsv` (4 pinned rows rewritten: R12-02 29→36, R12-03 56→63, R13-01 20→23, R14-01 21/18→24/21), `corpus/stamps.tsv` (9 lines deleted), `SCORECARD.md` (3 deleted lines), `SHONEN.md` (8 lines rewritten, `[x]` 4→`[~]`), `SKILL.md`, `PROVINCE.md`, `corpus/README.md`. Each is logged in LOG.md or the lesson. See D6.

3. **Claims: see §Per-claim verdicts** (counts run at both commits).

4. **SOURCES: PASS.**
   `bash /home/vgpnk/Projects/shokunin/.tower/worktrees/kaika/fleet-census/scripts/sources-census.sh validate /home/vgpnk/Projects/shokunin/.tower/worktrees/kaika/kagi-shokunin` → `kagi-shokunin	ok	…/corpus/SOURCES.md`, exit 0.
   Lane gate at head: `bash corpus/sources-census.sh` → `SOURCES_CENSUS: CLEAN (rows=16 A=14 B=0 C=2 queued=1 mined=14 rejected=1 entries_sourced=3 legacy=21)`; `--selftest` → `SOURCES_CENSUS_SELFTEST: PASS (47 cases)`.
   Re-opened all 16 URLs (`curl -sL`, sha256 vs the row's `Fetch sha256`): 14 MATCH (S001–S004, S007–S016); 2 DIFF — S005 (tier C lead; recorded `f7ba8254…`, fetched `12a25d11…`) and S006 (tier A announcement; recorded `39a869df…`, fetched `ca20af8d…`; the quotes still resolve). See D5.
   Quote checks (tag-stripped, normalised text; `python3` over the fetched bytes):

   | row | location | quote (≤25 words) | result |
   |---|---|---|---|
   | S001 (A) | §Use `op run` to pass environment variables | "provisioned for the duration of the process." | PRESENT |
   | S006 (A) | §Try 1Password Credential Broker today | "available for all Enterprise Password Manager Business customers" | PRESENT |
   | S007 (A) | §GitHub Actions | "add a new secret for your GitHub organization" | PRESENT |
   | S010 (A) | §Key groups | "By default, the threshold is set to the number of key groups." | PRESENT |
   | S011 (A) | §`rotate` command | "Use updatekeys if you want to add a key without rotating the data key." | PRESENT |
   | S013 (A) | §Lease, renew, and revoke (note) | "does not issue leases although it will sometimes return a lease duration" | PRESENT |
   | S014 (A) | §JWT/OIDC auth method | "The JWT auth method can be used to authenticate with OpenBao using OIDC" | PRESENT (page text is "jwt"; case-only difference) |
   | S016 (A) | §Token hierarchies and orphan tokens | "When a parent token is revoked, all of its child tokens -- and all of their leases -- are revoked as well." | PRESENT |
   | S008 (rejected) | §Documentation | "You can find the SOPS documentation on getsops.io" | PRESENT; README (1,909 B) has no recipient, key-group or rotation text → reject supported |
   | S002 (A) | Connect-server diagram caption | "The Connect server is part of your environment, and communicates to Your Apps using access tokens and a REST API." | PRESENT as the image `alt` attribute |
   | S007 | "public beta" (critic claim) | "public beta" | ABSENT — confirms the entry's erratum |

   Absence-sweep counts in E3 reproduce exactly (same normalisation): `tokenreview` S012 0 / S014 0; `jwks pairs` S012 1 / S014 0; `exactly match` S012 3 / S014 0.
   Lane-fit (QA7): `rg -il -e sops -e openbao -e 'credential broker' -e 'connect server' --glob '*.md' --hidden /home/vgpnk/Projects/shokunin` (kagi lane excluded from the hits) → only `.ufo/reports/round-1/kama.md`; no sibling corpus claims the ground.

5. **Discernment spot-check: see §Spot-check.** Admits 0 of 2 agree (as landed); rejects 3 of 3 agree.

6. **New entries: header trio present (lines 1–4 of each), recheck runs, claims mostly match.** `source:` / `verified-at:` / `recheck:` are present in all three entries. The recheck (re-opening the cited rows) was run as in check 4. Defects in the bodies: D1.

7. **Credentials: PASS.** `git diff aea7a4301..e1544c194 | grep -nE 'op://[A-Za-z0-9]|BEGIN [A-Z ]*PRIVATE KEY|ghp_[A-Za-z0-9]{20,}|AKIA[0-9A-Z]{16}|xox[baprs]-[A-Za-z0-9]'` → no output (exit 1). A broader sweep over added lines (`op://`, `PRIVATE`, `ghp_`, `AKIA`, `xox`, JWT-shaped) → no output.

8. **Report: conforms in structure, with content defects.** Present in order: Work performed (line 10), Landed changes, Before → after measurements, SHONEN, Sources & frontier, Mistakes, Trend verdicts, L0 questions, Integrator notes. Round commits cited (`c41af82`, `e1544c1`). No `[x]` (SHONEN `[~]` ×4, each with a pointer). Defects: D3 (unnamed 26-row set), D8 (search-log arithmetic and cited command), D9 (unresolved count not reproduced).

## Per-claim verdicts

Counts were run with a script on `git archive` extracts of `aea7a4301` (base) and `e1544c194` (head).

| claim | command | base | head | report | verdict |
|---|---|---|---|---|---|
| C1 depth | `grep -c DOTENV_OBS corpus/knowledge/op-ref-consumption.md` | 0 | 6 | 0→6 | matches |
| C1 | `grep -c DOTENV_BYTES corpus/claim-ledger.tsv` | 0 | 1 | — | matches |
| C1 | `awk -F'\t' '$1=="R12-02"{print $3}' corpus/claim-ledger.tsv` | `^OP_REF_SELFTEST: PASS \(29 cases\)` | `(36 cases)` | 29→36 | matches |
| C1 | `bash corpus/op-ref-probe.sh --dotenv-bytes` (op 2.41.0) | CLEAN checks=6 failed=0, exit 0 | same | CLEAN, exit 0 | matches |
| C1 | `bash corpus/op-ref-probe.sh --selftest` | PASS (36 cases) | PASS (36 cases) | — | matches (the 29-case pin was stale at base) |
| C1 | probe stamp equality (`awk` + `sha256sum`) | 1 | 0 | 1→0 | matches |
| C1 | `sha256sum --check` over `corpus/stamps.tsv` | 9 mismatches | 5 mismatches (the 5 named-debt rows) | "only the 5 named-debt rows" | matches |
| C2 calibration | `awk -F'|' '/^\| M[0-9]/ && $6 ~ /QM/' corpus/lessons/round-21.md \| wc -l` | file absent | 11 | 0→11 | matches |
| C2 | `awk -F'|' '/^\| Q[AM][0-9]/' corpus/QUALITY.md \| wc -l` | file absent | 21 | 0→21 | matches |
| C2 | `grep -c '^- \[x\]' SHONEN.md` | 4 | 0 | 4→0 | matches |
| C2 | `grep -c '^- \[~\]' SHONEN.md` | 0 | 4 | — | matches |
| C3 capability | `validate` (fleet census) | — | exit 0 | exit 0 | verified |
| C3 | lane gate CLEAN / selftest | absent | CLEAN; 47 PASS | absent→CLEAN | verified |
| C3 coverage | `ls corpus/knowledge/*.md \| wc -l` | 21 | 24 | 21→24 | matches (entries contested, D1) |
| C3 | `grep -c '^## Frontier' corpus/README.md`; `'^## Known gaps'` | 0; 0 | 1; 1 | 0→1 | matches |
| C3 | `awk '/^## Capabilities/,/^## Saturation/' SCORECARD.md \| grep -c '^\| '` | 2 | 3 | 2→3 | matches |

Verdicts:
- **C1 depth 8→9: `verified`.** The probe reproduces CLEAN with op 2.41.0 at both commits, and the ledger rows match. Caveat: the 0→6 count is self-authored text. The evidence that carries the claim is the probe run and the sources. The §11 bytes match the probe's literals (`corpus/op-ref-probe.sh:136–141`).
- **C2 calibration: `not-verified` as an axis move.** The counts measure rows the lane wrote. The score stays at 9 (9→9), and the discernment check that calibration rests on was not performed at landing (performed here: §Spot-check). The `[x]`→`[~]` change is a correction, not a calibration gain.
- **C3 capability: `verified`.** The gate runs clean at head, and its selftest runs 47 cases. **C3 coverage: `unchanged` as scored** (claimed 9→9; the entries are vendor documentation, not governed surfaces). Admission of the entries is contested (D1).
- **Ledger, no regressions:** the full ledger was re-run row by row at both trees (see §Ledger). No row went green→red.

## Per-axis recommended verdicts

| axis | lane score | recommended | basis |
|---|---|---|---|
| depth | 8→9 | **verified** | C1 |
| coverage | 9→9 | unchanged | no coverage claim; no harm |
| operability | 9→9 | unchanged | census gate booked as capability, not axis move (SCORECARD); no harm |
| freshness | 9→9 | unchanged | re-measured on op 2.41.0; `legacy=21` entries still lack `recheck:`; no harm |
| calibration | 9→9 | unchanged; **C2 not-verified** | D2; the score should not be raised on this evidence |
| adjacency | 9→9 | unchanged | cross-lane sweep (QA7) found no contested claim; no harm |

No axis is reduced by this round.

## Trend verdicts

- **expansion: harmed as landed** (lane: `improved`). LEARNING.md defines `harmed` as an admitted entry failing the bar it was admitted under. E1 fails QA2 as written: line 16 says the Broker is a "public preview" and gives no plan scope, and the erratum (line 34) gives the scope the body lacks. E3 fails QA3/QA9 as written: line 17 generalises the external-JWT clock to "the issuer (IdP, Kubernetes)", line 18 keeps the withdrawn "Vault/OpenBao token TTL" label, and line 20 says "only a write; no lease, nothing expires" (the erratum at lines 107–110 withdraws it). An erratum that marks a body sentence without rewriting it does not satisfy a criterion that judges the sentence. It becomes `improved` once the body cells are rewritten and re-reviewed.
- **quality: improved** (lane: `improved`; reviewer concurs). Verified: R12-02 (36), R12-03 (63), R13-01 (23), R14-01 (24/21) reconcile at head and were red at base. Every admitted-entry defect found in the post-landing review is marked by an erratum, so no entry is left unmarked. Caveat: the marked-but-unrewritten sentences (D1) remain in the entries.
- **discernment: unchanged, with an open disagreement** (lane: `unchanged`; reviewer concurs on the value). The outside spot-check (below) shows 0 of 2 admits agreeing and 3 of 3 rejects agreeing. The admit disagreement is not yet a criterion. Recommended addition: QA10 — an erratum does not repair a body sentence that the bar fails; the sentence is rewritten or removed, and the errata are kept as the record. Without QA10 with a lesson, the disagreement stays unlearned, which is `harmed` under LEARNING.md.

## Spot-check (LEARNING.md §Discernment)

| # | gate decision | item | reviewer | reason |
|---|---|---|---|---|
| A1 | admit | `corpus/knowledge/sops-age-key-rotation.md` (E2) | **disagree** (as landed) | The core distinction (recipient ≠ data key ≠ values) and the compromise order match S011 (digest MATCH; quotes present). The body still states "independent custodians" (line 49; S010 says key groups, not people) and "kagi does not run SOPS today" (line 68; the sweep supports only corpus mentions, as the entry's own erratum at lines 98–99 says). QA3/QA6 fail as written. Repair: rewrite lines 49 and 68. |
| A2 | admit | `corpus/knowledge/onepassword-machine-credentials.md` item 4 (E1, line 16) | **disagree** | The sentence states public-preview status and says the Broker delivers "without standing vault access". S006 contrasts an integration key with a Service Account token that "carries standing access"; it does not say that about Broker delivery. Plan scope is missing from the sentence (QA2); the erratum (line 34) cannot supply it. Repair: state the Enterprise Password Manager Business scope and the source's actual wording in the sentence. |
| R1 | reject | S008 SOPS README (row `rejected`) | **agree** | Fetched README has only the pointer "You can find the SOPS documentation on getsops.io" and the format/backend list; no lifecycle mechanics. |
| R2 | reject | candidate "Credential Broker removes every secret from CI" | **agree** | S007 (§GitHub Actions): "add a new secret for your GitHub organization", holding `OP_INTEGRATION_KEY`; S006: the integration key "is an encryption key". The "removes every secret" claim is contradicted. |
| R3 | reject | candidate "a Vault KV read carries a lease" | **agree** | S013 (digest MATCH): KV "does not issue leases although it will sometimes return a lease duration". |

## Ledger re-run

Every ledger row's command was run from its own tree, with the expected exit and last-line regex from `claim-ledger.tsv`. Base and head were run in the same environment.

- Head: 28 PASS / 11 FAIL. Base: 22 PASS / 17 FAIL. **No PASS→FAIL between base and head.**
- Changed FAIL→PASS at head: R12-03, R13-01, R14-01, R21-02, R21-03, R21-04. R21-01 passes at both.
- Failing at both trees (host-dependent or pre-existing; not this round's regressions): R11-01, R11-02, R11-04, R11-06 (exit 2 vs expected 1), R11-08 (citations, see D9), R12-01 (`the-janitor` absent: SETUP), R13-03 (`cells`: the named round-20 attempt-heading debt), R15-01, R16-01, R16-03 (`--falsify` 15/18 at both), R17-01.
- Not run: `claim-ledger.sh verify` (R18-01 reads host files; the lane's and my reasons agree).

## Defects by severity

**High**
- **D1 — E1 and E3 bodies assert what their own errata withdraw; E2 likewise.** E1 line 16 (no plan scope; "without standing vault access"). E3 line 17 ("the issuer (IdP, Kubernetes)"), line 18 ("Vault/OpenBao token TTL"; errata line 108 withdraws the label), line 20 ("nothing expires"; erratum line 110). E2 lines 49 and 68. QA9's weak-signal list names this exact pattern ("never expires" where the page says "issues no lease"). Fix: rewrite the body cells, keep the errata as the record, then re-review. The round lesson calls these "marked by an erratum"; marking is not repair under QA2/QA3/QA9.
- **D2 — C2 calibration is not verified as an axis move.** The counts measure the lane's own new rows (0→11, 0→21). The score is held at 9, and the outside discernment check was not performed at landing. The `[x]` 4→0 change is a correction. Fix: drop C2 as a claim, or re-file it with a named non-author judgment.
- **D3 — QM12 is unmet by its own landing.** QM12 (`corpus/QUALITY.md`) requires that "the skipped rows [be] listed by id with the reason". The report (line 51) says "26 hermetic/repo-only ledger rows re-run individually, 26/26 PASS" without naming them; the lesson's post-landing table claims a "skipped-row list" that does not exist. Fix: list the 26 by id, and the skipped rows with reasons.

**Medium**
- **D4 — the admission bar is not verifiably prior to dispatch.** `corpus/QUALITY.md` (the QA1–QA8 bar the plan calls "written before dispatch") first appears in `c41af82`, in the same commit as the entries it gates. Not verifiable from git; recorded for the operator.
- **D5 — fetch digests for S005 and S006 do not reproduce** (`curl -sL` today: S006 `ca20af8d…` vs recorded `39a869df…`; S005 `12a25d11…` vs `f7ba8254…`). The S006 quotes still resolve. The "Fetch sha256" cell is evidence for the claim, so it should say the page is dynamic and record the 2026-10-19 bytes actually relied on.
- **D6 — pinned-expectation re-pins rewritten in place** (ledger R12-02 29→36, R12-03 56→63, R13-01 20→23, R14-01 21→24). The values match measured output at head (§Ledger), so this is not forcing a green. But `SKILL.md` lists "changing an expectation to force green" as an anti-pattern, and the lesson should say the new values are measured outputs, not targets.
- **D7 — two census implementations.** The lane's `corpus/sources-census.sh` (450 lines) and the fleet `fleet-census/scripts/sources-census.sh` (653 lines) both implement the contract census. Both pass. Maintaining two copies conflicts with "delete dead weight"; the lane should cite the fleet tool or justify its copy.

**Low**
- **D8 — search-log count and command.** `corpus/SOURCES.md` search log cites `grep -cE '^\| S[0-9]{3} ' …/kagi-art.md`, which returns **0** (the dossier uses `|S001|` with no spaces). The count 29 reproduces with `grep -cE '^\|[[:space:]]*S[0-9]{3}'` (returns 29). Also "16 opened, 13 left as leads, 1 rejected" sums to 30 for 29 identified: the rejected row is one of the 16.
- **D9 — "23 pre-existing unresolved" pointers not reproduced.** `bash corpus/claim-ledger.sh citations`, run in a layout whose `../.ufo` links to the fleet `.ufo`, gives `unresolved=15 labeled=13` at both base and head, with identical UNRESOLVED sets (line numbers shifted in README). No round-21 pointers. The lane's "no new unresolved" conclusion reproduces; its count of 23 does not, and the report should state the layout it measured in.

## Verification gaps

- `claim-ledger.sh verify` not run (same as the lane).
- op probes ran on op 2.41.0 only. The round-20 op 2.40.0 observations (cited in §11) were not re-measured.
- The L2 swarm dispatch claims (11 members, godspeed prefix) are outside my check list and were not verified.
- The 26-row set in the report cannot be reconstructed from the record (D3).
- Scratch `/tmp/kaika-verify/kagi/` deleted after this write.
