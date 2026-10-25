# kaidoku — round 32, attempt 2

## Work performed

Declared claims: **R32-C1 coverage**, ARM64X hybrid PE native-view import/overview enters bounded Core; **R32-C2 calibration**, four outside-recorded capabilities versus the SCORECARD summary. **Author verdict: rejected-honest-stop** — C1 verifies narrowly; C2's unchanged counter admits denial and word-bag controls. No re-freeze or exploratory relabel.

- C1: twelve author-built exported-leaf DLLs, original envelopes/IDs, independent byte readers and LLVM witnesses; native view only, not EC/dual-view recovery or runtime. Entry `corpus/knowledge/2026-10-23-r32-arm64x-hybrid-pe.md`; fresh review `.ufo/waves/round-32/a2residual/FinalC1Measure.md`.
- C2: truthful historical-summary maintenance landed, but explicit denial scores the same 4/4 as the repair. **Full fixture and original receipt landed at `411f3a80a1efefabe2ba12f227147023cfbce4bd`**, `.ufo/waves/round-32/controls/c2-negative/`; independent replay `.ufo/waves/round-32/a2residual/FinalC2FalseReplay.md`.
- All seven r31 routed defects addressed first: QUALITY 57 includes README/filenames; append-only 7/23 and timing corrections; SKILL names the three live 6.7.0 probes; w1 `CriticSeparability` erratum; actual r31-report gate receipt; write mode exits 3 with no target line. NoGitguard remains intentionally unclaimed. Mapping: `.ufo/waves/round-32/a2residual/FinalR31Routing.md`.
- Sources S098/S099 mined, S100 retained as a scoped rejection; thirteen located quotes reopened with negative controls. `corpus/lessons/round-32.md` Gate; `.ufo/waves/round-32/a2residual/FinalSourceReopen.md`.
- Inherited freezes were rechecked; seven untrusted dispatch/registry leftovers discarded, never used for claim outcomes. `.ufo/waves/round-32/attempt1-discard.json` and `a2audit/A2AttemptForensics.md` under that wave root.

## Landed changes

Lane shipping tip: **`547d6f2c9f7b67201ec8eb60a04320127048003d`** (helper returned `landed 547d6f2c9f7b67201ec8eb60a04320127048003d`). Measurement revision: `9ef97f08b655d951650ba5d32f41f1b1cf9653f4`; later changes record results/receipts, not frozen instruments or carrier bytes.

| commits | change | LOG linkage |
|---|---|---|
| inherited `9a73680a`, `9d54070b`, `f382e3b7` | C1 and superseded/active C2 freezes; rechecked pins and before receipts | `LOG.md:3037-3039` |
| `411f3a80a1efefabe2ba12f227147023cfbce4bd` | complete denial fixture, patch, receipt and honest stop | `LOG.md:3041` |
| `33393e594f1e278777fa49020b42c66ac4fa352e` | all ten fresh pre-data control receipts; r31 repairs and disclosure ledgers | `LOG.md:3040,3043` |
| `bb0af56c29e7b4c11d0583ed6697d0e17aba9d26` | original C1 data, sourced bounded Core/docs, truthful repertoire maintenance | `LOG.md:3043-3047` |
| `bbdd793d55807cfea9193ef5aaf0ae86a5c25a10` | independent PE reader/captures, model/backoff/status provenance | `LOG.md:3048-3049` |
| `9ef97f08b655d951650ba5d32f41f1b1cf9653f4` | eight fresh residual reviews and retained independent/source witnesses | `LOG.md:3050-3054` |
| `547d6f2c9f7b67201ec8eb60a04320127048003d` | final measurements, SCORECARD and disclosed conformance findings | `LOG.md:3055-3058` |

No domain-source or sibling remote was pushed. No MANIFEST or driver state was edited.

## Before → after measurements

The predicates remain `P1-pass` / `P2-match` in the original frozen files. Existing owned-proxy scores stay 10 → 10; these bounded counts are not domain-wide mastery scores.

**C1 command** (explicit existing provider environment, Git routing unset):

```sh
env -u GIT_DIR -u GIT_WORK_TREE -u GIT_INDEX_FILE \
  GHIDRA_INSTALL_DIR=/home/vgpnk/.local/opt/ghidra_12.1.4_PUBLIC \
  JAVA_HOME=/usr/lib/jvm/java-21-openjdk \
  python3 -I -B tools/round-32/c1-arm64x-positive.py --root /home/vgpnk/Projects/shokunin/kaidoku-shokunin --rev <REV>
```

- Before at `283aad7f`: exit **2**, missing pinned inputs; only a Frontier ARM64X reserve exists. `province_ok=0` was **not evaluated/printed** by that run (frozen-prose erratum). Receipt `.ufo/waves/round-32/a2before/c1-base.txt`.
- After at `9ef97f08b655d951650ba5d32f41f1b1cf9653f4`: `carriers=12 pass=12 target=12 entry_ok=1 (ok) province_ok=1 (ok)`, exit **0**. Receipt `.ufo/waves/round-32/a2after/c1-at-9ef97f08.txt`.
- Fresh author-dispatched reviewer independently reran the counter at product `bb0af56c`, and compared committed envelopes with its own byte reader/LLVM. Receipt `.ufo/waves/round-32/a2residual/FinalC1Measure.md`; independent comparison `.ufo/waves/round-32/final-c1-witness/compare-own.json`. No outside-admission credit is implied.

**C2 command:**

```sh
python3 -I -B tools/round-32/c2-capability-calibration-v3.py --root /home/vgpnk/Projects/shokunin/kaidoku-shokunin --rev <REV>
```

- Base: `statements=4 match=1 target=4 reverse_mismatch=0`, exit **1** (`.ufo/waves/round-32/a2before/c2v3-base.txt`).
- Measured `9ef97f08b655d951650ba5d32f41f1b1cf9653f4`: `statements=4 match=4 target=4 reverse_mismatch=0`, exit **0** (`.ufo/waves/round-32/a2after/c2v3-at-9ef97f08.txt`).
- **Falsified as an improvement measure:** denial and five-word bags also reach 4/4, exit 0. Original committed receipt `.ufo/waves/round-32/controls/c2-negative/receipt.json`; fresh replay `.ufo/waves/round-32/a2residual/FinalC2FalseReplay.md`. Numerical alignment earns no calibration gain.

Other exercised checks at `9ef97f08b655d951650ba5d32f41f1b1cf9653f4`:
- Freeze integrity for all three claim files: CLEAN, exits 0, 8/2/2 pins (`.ufo/waves/round-32/a2after/freeze-claims.json-at-9ef97f08.txt`, `.ufo/waves/round-32/a2after/freeze-claims-v2.json-at-9ef97f08.txt`, `.ufo/waves/round-32/a2after/freeze-claims-v3.json-at-9ef97f08.txt`).
- Disclosure audits: exits 0, exact 19/19 and 24/24 (`.ufo/waves/round-32/a2after/ledger-v1-at-9ef97f08.txt`, `ledger-v2-at-9ef97f08.txt`). V3's historical-anchor unpinned-instrument flag remains disclosed; this is not a claim that every freeze is clean.
- Strict timestamp gate: **exit 1**, four planned-deadline occurrences, not future run instants (`.ufo/waves/round-32/a2after/timestamps-strict-at-9ef97f08.txt`). No exemption/green verdict. The diagnostic quotes those deadlines; this measurement is of the named revision, not a later bookkeeping tip.

## Sources & frontier

Rows **97 → 100**; tier A 91 → 94, B 5 → 5, C 1 → 1; mined 95 → 97, rejected 2 → 3; malformed 0 → 0. Added: S098/S099 mined, S100 rejected, all A within their stated scope. Existing status/recheck/used-by fields: **unchanged**. Source S100 rejects only missing CHPE offset/tag definitions, not the page's machine-type content. ARM64X native-view synthetic-leaf coverage moves to bounded Core; published hybrids, EC/dual-view recovery, internal functions and runtime remain Frontier.

Reproduction command (the per-revision Python argv was exercised twice; exact argv/output receipts `.ufo/waves/round-32/a2after/source-count-base.txt` and `source-count-after.txt`):

```sh
unset GIT_DIR GIT_WORK_TREE GIT_INDEX_FILE
LANE=/home/vgpnk/Projects/shokunin/kaidoku-shokunin
for REV in 283aad7fe56d82f4ed4f8e43f099c2e1ceed5525 9ef97f08b655d951650ba5d32f41f1b1cf9653f4; do
  python3 -I -B -c "import collections,re,subprocess,sys; root,rev=sys.argv[1:]; text=subprocess.check_output(['git','-C',root,'show',rev+':corpus/SOURCES.md'],text=True); rows=[x.split('|') for x in text.splitlines() if re.match(r'^\\|[ \\t]*S[0-9]{3,}[ \\t]*\\|',x)]; print('rows='+str(len(rows))); print('tiers='+str(dict(sorted(collections.Counter(x[4].strip() for x in rows).items())))); print('status='+str(dict(sorted(collections.Counter(x[8].strip() for x in rows).items())))); print('malformed='+str(sum(len(x)!=13 for x in rows)))" "$LANE" "$REV"
done
```

Observed outputs (each exit 0):

```text
before:
rows=97
tiers={'A': 91, 'B': 5, 'C': 1}
status={'mined': 95, 'rejected': 2}
malformed=0
after:
rows=100
tiers={'A': 94, 'B': 5, 'C': 1}
status={'mined': 97, 'rejected': 3}
malformed=0
```

Census command, both calls:

```sh
/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kaidoku
```

Before 06:45:22Z, `.ufo/waves/round-32/a2before/census-start.txt`:

```text
kaidoku	W04	S033 duplicate url github.com/NationalSecurityAgency/ghidra/pull/9348 across scopes
kaidoku	W04	S047 duplicate url go.dev/dl/?mode=json&include=all`, across scopes
kaidoku	W04	S054 duplicate url developer.android.com/ndk/guides/abis across scopes
kaidoku	W04	S062 duplicate url raw.githubusercontent.com/sigrokproject/sigrok-cli/sigrok-cli-0.7.2/doc/sigrok-cli.1 across scopes
kaidoku	W04	S069 duplicate url www.wireshark.org/docs/man-pages/tshark.html across scopes
kaidoku	W04	S083 duplicate url registry.npmjs.org/rea-agents/-/rea-agents-6.5.0.tgz across scopes
kaidoku	W04	S090 duplicate url registry.npmjs.org/rea-agents/-/rea-agents-6.5.0.tgz across scopes
kaidoku	W04	S092 duplicate url registry.npmjs.org/rea-agents/-/rea-agents-6.5.0.tgz across scopes
kaidoku	ok	/home/vgpnk/Projects/shokunin/kaidoku-shokunin/corpus/SOURCES.md
exit=0
```

After 07:35:01Z, `.ufo/waves/round-32/a2after/census-end.txt`:

```text
kaidoku	W04	S033 duplicate url github.com/NationalSecurityAgency/ghidra/pull/9348 across scopes
kaidoku	W04	S047 duplicate url go.dev/dl/?mode=json&include=all`, across scopes
kaidoku	W04	S054 duplicate url developer.android.com/ndk/guides/abis across scopes
kaidoku	W04	S062 duplicate url raw.githubusercontent.com/sigrokproject/sigrok-cli/sigrok-cli-0.7.2/doc/sigrok-cli.1 across scopes
kaidoku	W04	S069 duplicate url www.wireshark.org/docs/man-pages/tshark.html across scopes
kaidoku	W04	S083 duplicate url registry.npmjs.org/rea-agents/-/rea-agents-6.5.0.tgz across scopes
kaidoku	W04	S090 duplicate url registry.npmjs.org/rea-agents/-/rea-agents-6.5.0.tgz across scopes
kaidoku	W04	S092 duplicate url registry.npmjs.org/rea-agents/-/rea-agents-6.5.0.tgz across scopes
kaidoku	ok	/home/vgpnk/Projects/shokunin/kaidoku-shokunin/corpus/SOURCES.md
exit=0
```

## Trend verdicts

- **expansion: improved** — sourced, bounded hybrid edge class enters Core (`PROVINCE.md` round-32 table; C1 receipt).
- **quality: improved** — full-envelope/byte evidence and r31 corrections, with frozen-gate/selftest and timestamp conformance limits explicitly retained (`corpus/lessons/round-32.md`). No failed recheck is left marked successful.
- **discernment: improved** — the outside r31 scope disagreement became QUALITY 57 with a red-before sweep; C2's false accepts stop the round rather than change the rule. Current non-author admission/spot-check remains pending.

## SHONEN

- [~] Decision tables/error patterns/checklists/citations: `SKILL.md` ARM64X section and round-31 SQLite table; author-dispatched reviews only.
- [~] End-to-end task: C1 original runs and final measurement (`LOG.md:3043-3044,3055`).
- [~] Executable instructions: explicit provider/recheck recipe, fresh `FinalC1Measure.md`; no named outside verifier.
- [~] Boundary: native-view-only Core and remaining Frontier in `PROVINCE.md`; existing kaidoku/revenger overlap remains unresolved, not silently absorbed.

## Shape, containment and remaining limits

- **Shape:** one validated v1 audit/control wave 32 + one ordinary residual call 8 (<32 genuine attack items), **40 accepted/returned seats this attempt**, no dead/cancelled. Audit roles: critic13, reviewer7, scribe4, executor3, scout2, revenger1, connector1, mutation-tester1. Residual: reviewer4, critic4. L1 holds the planner seat. Registries/status/model records: `.ufo/waves/round-32/a2audit-settle.json`, `a2residual-settle.json`, `a2audit-models.json`.
- Original attempt: 36 planned registry members excluded, no reports used; only a 12-start count appears in untrusted inherited logs. Started seats' `omp SIGSEGV` at 06:19:06Z is assignment-supplied; individual old death records mostly unavailable. Do not invent 36 actual deaths or an exact observed round-total beyond the 40 confirmed new starts. Old planned+new membership is at most 76; old start uncertainty is explicit in `attempt1-discard.json`.
- Capacity: two async gate acquisitions refused; one residual task call refused 8/8 at the effective 100-job ceiling. Main authorized the same eight names/order/content to be resent; all eight then started (harness `-2` suffixes). Refusals are not seat deaths. `.ufo/waves/round-32/a2residual-capacity.json`, `a2residual-dispatch.json`.
- Actual answering models/backoffs are retained, not inferred from role names. C2 denial/shortcut critics answered with gpt-6.1-sol; primary source scribe with gpt-6-luna; independent build/PE executors continued via configured DeepSeek fallback after 429. Reviewer fallback histories are recorded. No safety-filter reroute was observed.
- Limits: metadata-only hybrid classifier accepts forged tags; first-added ordering is a committer-time proxy; source doc gates are lexical; five selftest mutants survive; archived secondary gates lack separate selftests. NoGitguard is unimplemented. Auxiliary r17 partial-positive timing is unknown. `A2AttemptForensics` used scoped `find` under inherited scratch contrary to the disk directive (M32-4); that inventory supports no claimed outcome.
- Existing cross-domain question: tsukuroi round-1 kaidoku/revenger arbitration remains unresolved; reader import coverage does not claim PE-format/build-tool ownership. No new L0 question. Hold `U064N008Hf47eb933` remains untouched.
- Tool installs/updates: none executed/reported in attempt 2; existing LLVM23.1.3 and REA6.5.0/provider paths were used. Stale-lane: this sole respawned round progressed through its landed commits; no other kaidoku mission is open.

## Pre-file receipt

All 40 accepted attempt-2 seats settled before the L1 measurements and this receipt; wave slots were released. Required fleet-root `git status --porcelain` misroot sweep found no owned plaintext misroots (ownership identifiers searched across the untracked plaintext files, no matches); operator configuration, driver state and unrelated files were untouched.

Executed `/home/vgpnk/Projects/shokunin/kaidoku-shokunin/tools/round-29/prefile-check.sh /home/vgpnk/Projects/shokunin/kaidoku-shokunin` (read-only), UTC 2026-10-23T07:48:57+00:00 → 2026-10-23T07:48:58+00:00. This gate checks tree cleanliness and disclosure audits, not C2 validity or the red timestamp gate. Exact output:

```text
prefile: tree clean
prefile: round-24 gate --disclosures corpus/claim-freezes.tsv at 547d6f2c9f7b67201ec8eb60a04320127048003d exit=0
prefile: round-29 gate --disclosures corpus/claim-freezes-v2.tsv at 547d6f2c9f7b67201ec8eb60a04320127048003d exit=0
prefile: PASS
exit=0
```

Lane helper state:

```text
state branch=main local=547d6f2c9f7b67201ec8eb60a04320127048003d remote=547d6f2c9f7b67201ec8eb60a04320127048003d ahead=0 behind=0 head=detached tracked=0 untracked=0
exit=0
```
