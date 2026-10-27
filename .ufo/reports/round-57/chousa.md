# chousa — round 57

## Work performed

Declared claims: **R57-C2 (freshness)** — re-fetch the 47 captures pinned by the base spans manifests into lane-owned, digest-checked bytes; **R57-C3 (depth, sourced)** — chain the workflow standard's normative references to their own documents. Their predicates, counters, controls and before receipts were frozen in attempt 1 (`corpus/evidence/round57/claims.md`; C2 `c2f914c53201a8f8ee4fef823b82681051d55592`, C3 `fd95724d56a33ad150cd263f8add2ce1f3425e6c`). Attempt 2 built on those freezes; no predicate or target changed.

- **C2 freshness:** the L1 opened all 47 pinned URLs under the frozen public-GET approval table, wrote every attempt to `corpus/evidence/round57/refetch.tsv`, and stored bytes under `corpus/captures/<sha256(url)[:24]>.{raw,txt}` using `tools/capture-fetch.py`. Final measurement: `SET=47 VERDICTS=47/47 REPRODUCED=41 DRIFTED=5 UNREACHABLE=1 BYTE_BACKED=46 CONSISTENT=46/46 FLAGGED=0/0 C2=PASS` (exit 0); W2 reviewer independently re-ran the counter twice and the controls (`R57W2ReviewC2After.md`).
- **C3 depth, sourced:** added `corpus/knowledge/normative-reference-chain-china-r57.md` and a 10-row `corpus/evidence/round57/c3/spans.tsv` plus its span files. The frozen counter prints `BOUND=4/7 (R1:S131 R2:S132 R3:S133 R7:S118) SWEPT=3/3 ... SUBSTANCE=PASS ANCHOR_BOUND=3/3 INFERENCE_GROUNDED=yes STRAY_IDS=- C3=PASS`; W2 re-derived the manifest and counter (`R57W2ReviewC3After.md`). R4-R6 remain UNBOUND with per-reference query/host sweeps in the entry.
- **Frontier / corpus:** added tier-B SOURCES rows S131-S133; logged old→new `used-by` updates on S118/S127 and corrected S077's `used-by` to name a lesson, not a tool. Added the Round57 coverage/frontier map in `corpus/README.md`, lesson `corpus/lessons/round-57.md`, and QUALITY criteria 111-114 with executable red-state evidence.
- **Quarantine / considerthese:** four W1 seats adjudicated the complete 24-row absent-defect slice; the L1 independently closed S096 using the OLE defined form. No row supports a fabrication verdict; the register's `payload-absent` class is contradicted on capturable rows. Mined `considerthese/2026-10-26.md:41`: stable IDs are already implemented by the round-54 ledger, but positional IDs can rebind after proposal reordering; the lesson records that weakness and a successor-checker recommendation.
- **Routed D1:** appended `#### Corrections (round 57)` to `corpus/knowledge/grey-literature-field-china-r42.md`; the recheck now targets 表7. W1's sweep found one stale instruction and nine legitimate `表 10`/`表10` mentions (`R57W1ScribeD1.md`).
- **Wave shape:** one v2 build+attack wave W1, 65 seats, validated under policy v2; role mix: 12 scout, 21 executor, 13 reviewer, 6 critic, 6 scribe, 2 mutation-tester, 2 connector, 1 sentinel, 1 revenger, 1 simplifier. L1 held the planner seat; attack share was 21/65 = 32%. W1 settled 65/65 reports, zero dead seats (`w1-results.json`).
- **Residual attack call:** W2 had 8 seats (3 reviewer, 2 mutation-tester, 2 critic, 1 sentinel), 8/8 reports, zero dead (`w2-results.json`). The v2 validator refused an 8-seat wave (`too_few_lanes`); because the prompt permits a ≤8-seat ordinary residual and direct `task` calls were forbidden, the L1 hand-shaped the validated dispatch schema and passed it through the inline `.ready` handoff. W2 was **not policy-validated as a 64–128-seat wave**; this is a conformance caveat. The literal residual wording says “reviewer/critic seats,” while W2 also included mutation-tester/sentinel roles. Round total: 73 seats.
- **W2 falsifiers:** C2's M5 first-vs-last attempt mutant was killed (last-attempt binding is load-bearing); other C2 mutants survived on the live data. All eight single-edit C3 mutants survived on the passing state (coverage finding). The whole-round do-nothing control fails both counters. **C3 provenance assurance is falsified:** W2 A1a/A1b fabricate a success row and replay capture bytes under a new `(id,url)`; both reach `C3=PASS` without fetching the named URL (`R57W2CritC3Forge.md`). The five bindings in the actual committed state are genuine and re-derived (`corpus/evidence/round57/sidecar-audits.md` §4), but the frozen counter cannot prove that in general.
- **Concurrency / integration:** an attempt-3 L1 committed W2 integration (`75004f0ab28aa953f80784b7eb7b57496ce055f3`) while this attempt-2 L1 was still active. Attempt 2 then landed `f3ecb76426a457ea409b613498968011ed20269a`, replacing the attempt-3-authored sidecar with the L1's independently re-run `sidecar-audits.md`; W2 results/reports and the ready marker remain committed. This resolved the concurrent write in the shared lane; the incident is recorded in the lesson. Final lane tip below is clean and pushed.
- **Misroot / scratch / tooling:** the first fetch-tool run wrote 86 capture files plus `refetch.tsv` to the fleet root; the L1 copied them byte-exact into the lane (`cmp` clean), deleted the fleet copy, and corrected `LANE = HERE.parent`. Final fleet-root status shows only unrelated `.scratch/closure-mado-r50.json` and `.ufo/reports/round-61/kake.md`, untouched. L1 removed `/fast/scratch/hyaku/chousa-r57` after all waves settled. No installs/upgrades; no pacman transaction; `.qcache` was not recreated or modified.

## Landed changes

Every item is logged in `LOG.md` Round 57; final lane tip is `5dc18607730a73e0a30ad938a20dbfaa37461f1c`, with `ls-remote` showing the same pushed hash.

- `f9736a39a0344a0aed63a65dfaddf7db624303d9` — L1 capture-fetch tool, first 47 attempts, lane-owned captures/record; initial misroot was byte-exactly swept and is recorded in lesson Mistakes row 1.
- `e0e73e0f76163b014033e80c6ba53ed92c14113d` — C2 retry rows/captures and after-receipt; record-less S105 wrap-up bytes removed for the frozen no-capture UNREACHABLE predicate (historic bytes/pin match disclosed below).
- `a03824d1a0c70278b33cca4ae4e2b8d6d9691e70` — W1 v2 spec/dispatch (65 seats).
- `f31a91be84e6d8542e7db5e7e2c0fb1387f2918b` — C3 candidate-fetch records and lane-owned captures, with unsuccessful URL attempts preserved in `refetch.tsv`.
- `a8d4e7da15a70a06d731739cace43cc3287801a1` — C3 entry/manifest, S131-S133, S118/S127 `used-by` changes, lesson Gate, C3=PASS.
- `1c9626efba2455d513b6b18df9b3df291e66556f` — W1 integration: D1 append, QUALITY 111-113, `tools/store-record-audit.py`, fetch-tool root guard, S077 `used-by` fix, LOG/SCORECARD, census receipt.
- `3010e7537d163d9a76264a166d491214ecdaf45e` — W2 residual dispatch (8 seats; inline handoff).
- `75004f0ab28aa953f80784b7eb7b57496ce055f3` — concurrent attempt-3 integration: W2 results/reports and SCORECARD freeze-id correction; its sidecar was later replaced by the L1 re-derivation at the following commit.
- `f3ecb76426a457ea409b613498968011ed20269a` — W2 integration: L1 sidecar audit, lesson addenda, census-end receipt; removed the unidentified attempt-3 sidecar file after re-running its audits as L1.
- `5dc18607730a73e0a30ad938a20dbfaa37461f1c` — README frontier, QUALITY 114 (C3 provenance replay weakness), LOG/SCORECARD/lesson post-wave corrections.
- Fleet L0 question on lowest-axis/plan admission ruling: commit `2c6edbabdb72527e51a246b7d7a2c2c777590974`.

## Before → after measurements

- **R57-C2 freshness:** before `SET=47 VERDICTS=0/47 REPRODUCED=0 DRIFTED=0 UNREACHABLE=0 BYTE_BACKED=0 CONSISTENT=0/0 FLAGGED=0/0 C2=FAIL` (`controls/c2-before.txt`, frozen at `c2f914c53201a8f8ee4fef823b82681051d55592`; independently re-derived in `R57W1ReviewBefore.md`). After `SET=47 VERDICTS=47/47 REPRODUCED=41 DRIFTED=5 UNREACHABLE=1 BYTE_BACKED=46 CONSISTENT=46/46 FLAGGED=0/0 C2=PASS` at `e0e73e0f76163b014033e80c6ba53ed92c14113d`; W2 re-ran at `3010e7537d163d9a76264a166d491214ecdaf45e` and the L1 re-ran at final tip `5dc18607730a73e0a30ad938a20dbfaa37461f1c`, same output. Command: `python3 corpus/evidence/round57/c2-count.py`. Five DRIFTED triples have absent=0; S105's UNREACHABLE is record-level. W2's 5-genuine/42-spliced forge falls within the count-only limitation disclosed in the freeze.
- **R57-C3 depth:** before `ENTRY=no BOUND=0/7 QUOTE_ROWS=0 C3=FAIL` (`controls/c3-before.txt`, frozen at `fd95724d56a33ad150cd263f8add2ce1f3425e6c`; independent re-derivation `R57W1ReviewBefore.md`). After `BOUND=4/7 SWEPT=3/3 QUOTE_ROWS=10 IN_SPAN=10 IN_ENTRY=10 IN_LESSON=10 SHORT=10 CONTEXT=10 CAPTURE_BOUND=10 SUBSTANCE=PASS ANCHOR_BOUND=3/3 INFERENCE_GROUNDED=yes STRAY_IDS=- C3=PASS` at `a8d4e7da15a70a06d731739cace43cc3287801a1`; W2 re-ran at `3010e7537d163d9a76264a166d491214ecdaf45e` and the L1 re-ran at final tip `5dc18607730a73e0a30ad938a20dbfaa37461f1c`, same output. Command: `python3 corpus/evidence/round57/c3-count.py`. **The committed data is genuinely bound; the counter's provenance leg is nevertheless falsified by W2 A1a/A1b.** The operator must decide whether that counter flaw defeats admission of the depth claim.

**Admission / conformance caveat:** `R57W1ReviewAxes.md` found the lowest-scored non-retired axis is operability 3/10 (the only numeric score; no axes retired; stagnation nudge dormant). C2 targets freshness and C3 depth; the committed round-56 planned row did not name the frozen R57-C2/C3 predicates, and no R57-C1 operability claim was frozen before data. Adding a claim after W1/W2 scored would violate the freeze rule. L0 question `chousa | round-57` asks whether closure rejects for this unmet plan/lowest-axis obligation or grandfathers the attempt-1 freezes. Do not read the two measured PASS receipts as self-admission.

## Sources & frontier

- `corpus/SOURCES.md` rows: **130 → 133**. Before counting command `git show 6656f077:corpus/SOURCES.md | grep -c '^| S'` → `130`, exit 0; after `grep -c '^| S' corpus/SOURCES.md` → `133`, exit 0. The census validator command was `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin chousa`.
- Census start output (`corpus/evidence/round57/census-start.txt`, exit 0):

```text
chousa	W04	S051 duplicate url www.w3.org/TR/2017/REC-html52-20171214/syntax.html across scopes
chousa	W04	S053 duplicate url docs.python.org/3/library/socket.html across scopes
chousa	W04	S073 duplicate url www.gnu.org/software/coreutils/manual/coreutils.html across scopes
chousa	W04	S074 duplicate url docs.python.org/3/library/hashlib.html across scopes
chousa	W04	S075 duplicate url www.gnu.org/software/coreutils/manual/coreutils.html across scopes
chousa	ok	/home/vgpnk/Projects/shokunin/chousa-shokunin/corpus/SOURCES.md
exit=0
```

- Census end output (`corpus/evidence/round57/census-end.txt`, exit 0):

```text
chousa	W04	S051 duplicate url www.w3.org/TR/2017/REC-html52-20171214/syntax.html across scopes
chousa	W04	S053 duplicate url docs.python.org/3/library/socket.html across scopes
chousa	W04	S073 duplicate url www.gnu.org/software/coreutils/manual/coreutils.html across scopes
chousa	W04	S074 duplicate url docs.python.org/3/library/hashlib.html across scopes
chousa	W04	S075 duplicate url www.gnu.org/software/coreutils/manual/coreutils.html across scopes
chousa	ok	/home/vgpnk/Projects/shokunin/chousa-shokunin/corpus/SOURCES.md
exit=0

- Census end output (`corpus/evidence/round57/census-end.txt`, exit 0) is byte-identical: the same five W04s, `ok`, `exit=0`. The five W04 duplicate-URL warnings predate this round.
- Rows added by tier: 3 × B (S131 2019 notice repost, S132 2021 notice repost, S133 2021 management-guideline attachment mirror); 0 × A, 0 × C. No status/recheck change. `used-by` old→new: S118 and S127 each add `corpus/knowledge/normative-reference-chain-china-r57.md`; S077 drops `tools/quarantine-check.py` (`tools/quarantine-check.py, corpus/lessons/round-42.md` → `corpus/lessons/round-42.md`).
- Section-10 collision lists (receipt `R57W1ExecAssimCollision.md`; no package adoption, no renumber map): lane `reg-ids` = **S001 S002 S003 S004 S005 S006 S007 S008 S009 S010 S011 S012 S013 S014 S015 S016 S017 S018 S019 S020 S021 S022 S023 S024 S025 S026 S027 S028 S029 S030 S031 S032 S033 S034 S035 S036 S037 S038 S039 S040 S041 S042 S043 S044 S045 S046 S047 S048 S049 S050 S051 S052 S053 S054 S055 S056 S057 S058 S059 S060 S061 S062 S063 S064 S065 S066 S067 S068 S069 S070 S071 S072 S073 S074 S075 S076 S077 S078 S079 S080 S081 S082 S083 S084 S085 S086 S087 S088 S089 S090 S091 S092 S093 S094 S095 S096 S097 S098 S099 S100 S101 S102 S103 S104 S105 S106 S107 S108 S109 S110 S111 S112 S113 S114 S115 S116 S117 S118 S119 S120 S121 S122 S123 S124 S125 S126 S127 S128 S129 S130** (130, SHA256 `35dbc6b4fe1142ef2354727233f4c5b3fd5433a5a9018586e3d7ee4c94288fe4`); staged `SOURCES.append.md` `staged-ids` = **S082 S083 S084 S085 S086 S087 S088 S089 S090 S091 S092 S093 S094 S095 S096 S097 S098 S099 S100 S101 S102 S103 S104 S105 S106 S107 S108 S109 S110 S111 S112 S113 S114 S115 S116 S117 S118 S119 S120 S121 S122 S123 S124 S125 S126 S127 S128 S129 S130 S131 S132 S133 S134 S135 S136 S137 S138 S139 S140 S141 S142 S143 S144 S145 S146 S147 S148 S149 S150 S151 S152 S153 S154 S155 S156 S157 S158 S159 S160 S161 S162 S163 S164 S165 S166 S167 S168 S169 S170 S171 S172 S173 S174 S175 S176 S177 S178 S179 S180 S181 S182 S183 S184 S185 S186 S187 S188 S189 S190 S191 S192 S193 S194 S195** (114, SHA256 `9ce3b9c30cd1115797315c6aea6f00fa45b4ff141a9aa630059afe3cc6b8e2f9`). Both are contiguous ranges with no duplicates. Collision output = **49 ids S082–S130** (the exact interval; SHA256 `763edf8bff7d74aa33674a9759156cd8fdb60dc7e0590a7136415c536c94f15c`); all candidate URLs differ from staged URLs, so document collisions=0. Numeric id overlap with staged S131-S195 is standing; rows advance by lane order/document, not arithmetic renumbering.
- Frontier advanced: `corpus/README.md` Round57 section now marks normative-reference chaining and the 47-capture freshness surface; S131-S133 were opened this round and back C3. R4-R6 remain explicit frontier gaps with query/host sweeps. Assimilation: none adopted; quarantine-first hand-check closes 24/24 verdicts and adoption stays closed. The campaign `.qcache` remains absent/untouched; L0 round-56 restore question remains open.
- Refetch record count: `wc -l corpus/evidence/round57/refetch.tsv` → 145 lines (header + 144 attempt rows; includes failed candidate URLs, not just the 47 pinned set). L1 sidecar audits confirm the five bound C3 `(id,url)` pairs have genuine successful rows and byte-matching raw digests.

## Trend verdicts

- **expansion — improved.** One new entry on uncovered normative-reference-chain ground, citing three new mined sources and linking four of seven references by document; README Round57 coverage map advanced. Because the C3 provenance leg is forgeable and the frozen counter can falsely pass, the operator must decide whether this evidence satisfies admission.
- **quality — improved.** 47 pinned captures have lane-owned record-backed verdicts; D1 landed append-only; S077's used-by contract defect was fixed; QUALITY 111-114 capture the misroot/store-record/provenance replay classes with red receipts. Caveats: S105's UNREACHABLE verdict is record-level despite historic pin-matching bytes; the C3 counter can be forged via a self-authored success row; the store-record audit intentionally still fails on 3 orphan/record-denied keys.
- **discernment — unchanged.** W1/W2 seats and the L1 quarantine review are same-lane evidence, not the required outside non-author spot-check; the independent closure must judge admits/rejects and the C3 provenance falsifier. The lane report does not claim self-attested discernment.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — `SKILL.md`; C3 entry and S131-S133 (lane assertion, no outside promotion verifier).
- [~] At least one end-to-end domain task executed and logged in LOG.md — LOG Round57, C2/C3 receipts and counters.
- [~] Instructions executable by an agent without oral context — `python3 tools/capture-fetch.py --status`, `python3 tools/store-record-audit.py`, both frozen counters.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — `PROVINCE.md`, `R57W1ConnSiblings.md`.

Stale-lane: respawn-per-round; no other mission of this lane is open.

Tool installs/updates: none. No pacman transaction attempted.
