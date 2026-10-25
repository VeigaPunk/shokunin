# revenger — fleet round 1 (kaika continuation, 2026-10-19)

Lane commits (worktree `.tower/worktrees/kaika/revenger-shokunin`, branch `kaika/round`, base `8bbcb4e`, all authored `revenger-shokunin <revenger@shokunin.local>`):
`a7acc20` (pre-admission bar, map and mistakes) → `35b2e8b` (round work; after-numbers measured here) → **`19b3174`** (SCORECARD + LOG record; lane HEAD).
Steered round 1 (fleet `.ufo/waves/kaika/steer.md`). Fail-closed checks passed: fleet-root `.ufo/reports/round-1/revenger.md` was absent, and the lane `LOG.md` had not closed round 1.

## Work performed

Declared claims (3, on distinct axes, causally separable):
- **C1 calibration** (lowest axis, tied with coverage at 5.0): saved-ledger runnability, 2/4 → 4/4.
- **C2 coverage**, split into criterion K (knowledge-map ground) plus a **capability acquisition**, `sources-curation`: a contract-v1 `corpus/SOURCES.md` and 4 gated knowledge entries.
- **C3 freshness**, adopted as a scored axis on evidence: dated live re-verification of the two pre-contract knowledge entries.

None of the three is exploratory.

- Re-read `PROTOCOL.md` and `PROTOCOL-APPENDIX.md` plus `MISSION.md`, `AXES.md`, `LEARNING.md`, `CORPUS.md`, the W1 dossiers and SOURCES contract v1. The lane's ledgers are its own; the clobbered fleet-root SCORECARD/LOG were ignored.
- Mined 19 mistake classes from this lane's rejected, halted and corrected rounds into `corpus/lessons/round-1.md:27-59`. The RevScribe L2 pointer audit (`.ufo/waves/kaika-r1/scribe-pointer-audit.md`) found 4 defective pointers, all fixed before commit.
- Built the admission bar `corpus/QUALITY.md` (Q01–Q10, each citing its mistake class) and a 14-row coverage map with `## Frontier` (`corpus/README.md`). Both were committed **before** any admission at `a7acc20`, so expansion eligibility uses frozen statuses.
- Dispatched **one batched `task` call of 10 L2s**: planner, connector, 4 executors, scribe, scout, reviewer, critic (`.ufo/waves/kaika-r1/dispatch.md`). No model was passed. Each prompt led with `/skill:godspeed` plus the verbatim directive bytes. File sets were disjoint, and no L2 committed.
- C1: the executors applied the `7c3ce19` ROOT/HIST split to `corpus/verify_icon_languages.py` and `corpus/verify_multi_icon_states.py` (`35b2e8b`). Evidence: `.ufo/waves/kaika-r1/exec-{lang,multi}-ledger.md`. The pre-landing oracle is `reviewer-oracle.md`.
- C2: the executors opened primary sources and drafted 4 entries. L1 integrated `corpus/SOURCES.md` (15 rows) and gated each entry. L1 caught three author errors before admission (C11 decode, C12 anchor, C13 forgery count). The post-landing critic found four derivation gaps (`critic-post.md`). Those gaps were fixed and became M20 → Q11 (`corpus/lessons/round-1.md:61-` `## Gate — kaika continuation`).
- C3: the scout re-probed 13 host facts (`.ufo/waves/kaika-r1/scout-freshness.md`) and L1 re-ran the probes. Headers and `## Re-verification 2026-10-19` tables went into `corpus/knowledge/seed.md` and `corpus/knowledge/2026-10-12-rea-readiness-checklist.md`, with the base bytes preserved.
- Post-landing wave: reviewer (`reviewer-post.md`: C1 and C3 verified), critic (`critic-post.md`), mutation-tester (`mutation-post-l2.md`: 22/22 killed). L1's own mutation run is `mutation-post.md` (10/12 killed; named gap below). **Provider exhaustion:** the first mutation-tester seat died with `resource_exhausted: Reached free model rate limit` (m_swe route) and was re-dispatched as a fresh spawn. Earlier, the post-landing batch hit `Background job limit reached (100)` and was retried unchanged.
- Correction appended: the universal `ev = f(content, path, params)` (`LOG.md:720`, `SCORECARD.md:135`) is family-scoped per kaidoku's adjudication (fleet `MANIFEST.json:2782`); see `LOG.md:776`.

## Landed changes

| change | LOG entry | commit |
|---|---|---|
| `corpus/QUALITY.md` Q01–Q10; `corpus/README.md` map + Frontier; lesson `## Mistakes` (M01–M19) | `LOG.md:771` | `a7acc20` |
| ROOT/HIST replay in two PE ledgers, plus a new receipt-command check | `LOG.md:772` | `35b2e8b` |
| `corpus/SOURCES.md` (15 rows), 4 admitted entries, lesson `## Gate`, Q11, M20, map `held` ×4 | `LOG.md:773-774` | `35b2e8b` |
| Freshness headers and re-verification tables on 2 entries | `LOG.md:775` | `35b2e8b` |
| L2 wave artifacts `.ufo/waves/kaika-r1/*` | `LOG.md:769` | `35b2e8b` |
| SCORECARD kaika axes table, capability row, saturation 7.0 / N=3, planned; M15 correction | `LOG.md:766-777` | `19b3174` |

## Before → after measurements

Every row was measured from isolated `git archive` snapshots under `/var/tmp`, unless noted.

| claim | counting command | before | after | commits |
|---|---|---|---|---|
| C1 calibration | `SCORECARD.md:32-43` (C) | `CALIBRATION 2 / 4 score= 5.0`, `REPLAY 8 / 10` | `CALIBRATION 4 / 4 score= 10.0`, `REPLAY 10 / 10` | `8bbcb4e` → `35b2e8b` |
| C2 coverage K | `git show a7acc20:corpus/README.md \| grep -cE '^\| C[0-9]+ .*\| held \|$'`, then the same on HEAD | 0 / 14 (0.0) | 4 / 14 (2.9) | `a7acc20` → `35b2e8b` |
| C2 expansion | the expansion script (`LOG.md:773`; it counts entries absent at `8bbcb4e` whose `coverage-map:` row was uncovered/partial at `a7acc20` and whose `source:` cites a `mined` row listing them) | 0 (`SOURCES.md` absent) | `EXPANSION uncovered=2 partial=2 total=4` | `8bbcb4e` → `35b2e8b` (worktree, clean) |
| C2 capability | the 7 census commands of contract v1 §Census on `corpus/SOURCES.md` | file absent | 15 rows; malformed 0; `A=14 C=1`; `mined=12 queued=1 rejected=2`; dup / enum / missing-path checks print nothing | `35b2e8b` |
| C3 freshness | `grep -cE '^\| [FK][0-9]+ .*\| (holds\|STALE)'` over both entries, plus `^verified-at: 2026-10-19` | unscored; base text vs live host 8/18 facts hold (4.4); 0 flagged; 0/2 dated | 18/18 hold or flagged (10.0); 10/10 stale flagged; 2/2 dated | `8bbcb4e` → `35b2e8b` |
| guard: coverage F | `SCORECARD.md:45-57` (F) | `COVERAGE 4 / 8 score= 5.0` | `COVERAGE 4 / 8 score= 5.0` | unchanged |

No axis was harmed. Inputs are unchanged (`git diff --stat 8bbcb4e -- corpus/fixtures corpus/live` is empty, per reviewer-post). Require/raise counts did not drop, and the base bytes of both C3 entries are contiguous in their new files.

Per-axis self-verdicts, pending non-author verification: calibration **improved**; coverage-K **improved**; coverage-F **unchanged**; freshness **improved**; depth (retired guardrail) **unchanged**; adjacency **unchanged**.

## SHONEN

- [ ] SKILL.md contains real decision tables, error patterns, checklists, cited sources — `SKILL.md` is still absent (named debt, `corpus/README.md` §Known gaps). Untouched this round.
- [~] At least one end-to-end domain task executed and logged in LOG.md — `LOG.md:772`: relocated replay of the r42–r49 saved PE ledgers, 4/4 at `35b2e8b`; non-author L2 review `.ufo/waves/kaika-r1/reviewer-post.md`. Author lane only.
- [~] Instructions executable by an agent without oral context — the census, expansion and freshness commands above, and each knowledge entry's `recheck:`, ran from the lane root at `35b2e8b`. No outside verifier yet.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — `.ufo/waves/kaika-r1/connector.md` §3. The kaidoku overlap is reported, not absorbed; custody records are kept on the Frontier as adjacent.

## Sources & frontier

- SOURCES rows: 0 → 15. Count: `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`.
- Added by tier: A=14 (9 web primary or official: SWGDE ×2, NIST CFTT, FIPS 180-4, DHS index, RFC 3227, MS PE spec, Unicode 18 ch.3, Python codecs; 4 own-work: S001, S013, S014, S015; 1 local installed-skill docs: S002) and C=1 (S012 Wikipedia, rejected).
- Rejected rows: S008 (RFC 3227) and S012 (Wikipedia), each with reason and flip.
- Rows touched old→new: none (all new).
- Re-opened by L1: S003, S005, S006, S010. Re-opened by the lane critic: S004, S009, S011. All quotes verbatim.
- Frontier rows advanced: none moved into core. C07 firmware was reordered to first after the freshness probe found binwalk 3.1.0 and unblob 26.6.4 on the host, which match REA's 3.1.x/26.6.x requirement. C03 managed is blocked: `dotnet` is on PATH but has no SDK.
- Map: 4 rows moved to `held` (C01, C11 from uncovered; C12, C13 from partial).

## Mistakes

- Classes mined: 20 (M01–M19 from history; M20 learned in this round's gate). Captured by a criterion: 18. `none` with reason: 2 (M03, M16, process rules). Count: `awk -F'|' '/^\| M[0-9]+ /{n++; if ($5 ~ /none/) z++} END{print n, n-z, z}' corpus/lessons/round-1.md` → `20 18 2`.
- Criteria added: Q01–Q10 (new file) and Q11, which supersedes Q08. M20 is the class behind Q11: the gate checked values instead of the derivations carried in the entries.

## Trend verdicts

- **Expansion: improved.** 4 admitted entries on rows the map did not hold (2 uncovered, 2 partial), each citing mined rows. A new kind of source (forensic-standards bodies) and one capability entered.
- **Quality: improved.** 10 stale facts flagged with current values, 0 left unmarked; the two replays re-verify after relocation; no admitted entry failed its re-check.
- **Discernment: unchanged** pending the outside spot-check. In-lane, the critic/L1 disagreement became a grounded criterion (M20 → Q11). Per `LEARNING.md`, L2s are the lane and do not count as outside discernment. Spot-check targets: admit `corpus/knowledge/utf16-unpaired-surrogates-in-resource-names.md`; reject `long-term-fixity-evidence-records` (`corpus/lessons/round-1.md` gate table).

## L0 questions

- revenger | round-1 | Rule on the kaidoku/revenger shipped-artifact overlap (tsukuroi ADJ-06, existing fleet `.ufo/l0-questions.md:42`). Proposed split, `connector.md` §3: revenger holds byte-level artifact structure, byte oracles and evidence-ledger standards; kaidoku holds REA server operations and provider lifecycle.
- revenger | round-1 | The REA MCP server now registered for the omp host pins `rea-agents@6.5.0`, while the installed skill names `rea-agents@6.7.0` (S001, S002). Which version should lane producer runs pin going forward? Saved records stay bound to 6.4.0.

## Integrator notes

- **Push precedence:** the standing operator rule "No push" overrides MISSION.md's commit-then-push. All lane work is committed (`19b3174`), and nothing was pushed. This report is uncommitted for the integrator to commit with `--author="revenger-shokunin <revenger@shokunin.local>"`.
- MANIFEST `rounds[]` holds 0 revenger entries while the lane LOG has r1–r60 plus fleet round 1 (W1 STATE §2). Integrator-owned.
- The earlier routing blocker (`MISSING_BINDING`, prior width-32 contract) is not re-asserted: the current dispatch contract was satisfied by the 10-member batch. The alias matrix in `.ufo/waves/fleet-round-1-interactive/` remains historical evidence.
- Harness hazard observed: `cd` was broken and work ran via `cwd`/absolute paths; a fleet-root `git status` check showed no revenger strays. Rate limits: one m_swe executor-class seat exhausted, and the 100-job cap was hit once.
- Known gap carried: the new receipt-command clause in both verifiers has no in-script forged-receipt control. The L1 mutant deleting it survives the script's own run (`mutation-post.md`); it is planned for next round.

## Post-review fixes

Lane commit **`8df2fce`** ("round-1: post-review fixes"; parent `19b3174`; author `revenger-shokunin`). No new claims. These fixes respond to the orchestrator's adjudication: C1 verified, C2 knowledge-map 0→4/14 verified, C3 verified under the freshness axis and relabeled **stored assertions re-verified**.

1. **E09 fixed.** In-place `recheck` edits per contract rule 2, logged old→new in `corpus/lessons/round-1.md` `## Post-review fixes`: S008 `—` → `on-release`; S012 `—` → `180d`.
2. **Q11 applied.** Each of the four admitted entries gained an appended `## Provenance (Q11, appended 2026-10-19)` block with every derivation command and its observed output, including `curl` re-matches of the S003–S006 and S010 quotes. The diffs are pure appends: `git diff | grep -c '^-[^-]'` → 0 for each entry.
3. **M14 pointer.** An appended correction in the lesson gives `SCORECARD.md:9,19-20` at `8bbcb4e`; the original row cited `:9,20-21`. Those lines are now superseded by `SCORECARD.md:121-144`.
4. **Expansion counting command**, run from the lane root at `8df2fce`:

```sh
python3 -B -c 'import pathlib,re,subprocess
mapc="a7acc20"; base="8bbcb4e"
st={}
for l in subprocess.run(["git","show",mapc+":corpus/README.md"],capture_output=True,text=True,check=True).stdout.splitlines():
 c=[x.strip() for x in l.split("|")]
 if len(c)==7 and re.fullmatch(r"C[0-9]+",c[1]): st[c[1]]=c[5]
rows={}
for l in pathlib.Path("corpus/SOURCES.md").read_text().splitlines():
 c=[x.strip() for x in l.split("|")]
 if len(c)==13 and re.fullmatch(r"S[0-9]{3,}",c[1]): rows[c[1]]=(c[8],{x.strip() for x in c[11].split(",")})
n={"uncovered":0,"partial":0}
for p in sorted(pathlib.Path("corpus/knowledge").glob("*.md")):
 rel=p.as_posix()
 if subprocess.run(["git","cat-file","-e",base+":"+rel],capture_output=True).returncode==0: continue
 t=p.read_text(); m=re.search(r"(?m)^coverage-map:\s*(C[0-9]+)\s*$",t)
 ids=set(re.findall(r"(?m)^source:\s*(S[0-9]{3,})",t))
 hdr=all(re.search(r"(?m)^"+h+r":\s*\S",t) for h in ("verified-at","recheck"))
 ok=m and hdr and st.get(m.group(1)) in n and any(rows.get(i,("",set()))[0]=="mined" and rel in rows[i][1] for i in ids)
 print(rel, m.group(1) if m else None, st.get(m.group(1)) if m else None, "COUNTED" if ok else "not-counted")
 if ok: n[st[m.group(1)]]+=1
print("EXPANSION uncovered=%d partial=%d total=%d"%(n["uncovered"],n["partial"],sum(n.values())))'
```

```text
corpus/knowledge/digest-scope-versus-provenance.md C13 partial COUNTED
corpus/knowledge/pe-resource-directory-layout.md C01 uncovered COUNTED
corpus/knowledge/tool-validation-by-function-and-version.md C12 partial COUNTED
corpus/knowledge/utf16-unpaired-surrogates-in-resource-names.md C11 uncovered COUNTED
EXPANSION uncovered=2 partial=2 total=4
exit=0
```

5. **Census validate**, re-run after commit `8df2fce`:
   `bash /home/vgpnk/Projects/shokunin/.tower/worktrees/kaika/fleet-census/scripts/sources-census.sh validate /home/vgpnk/Projects/shokunin/.tower/worktrees/kaika/revenger-shokunin`

```text
revenger-shokunin	ok	/home/vgpnk/Projects/shokunin/.tower/worktrees/kaika/revenger-shokunin/corpus/SOURCES.md
exit=0
```

   This was measured on script sha256 `0658116c…` (untracked, mtime 19:27:50 −0300). Two earlier versions of the same script, captured while its owner was editing it, are integrator notes for the census owner:
   - The first reported E08 on every row: its `date -d` local-midnight epoch is compared against a UTC `today`, which is a −0300 artifact.
   - The second hit a gawk parse error (`/https?:\\/\\/…/`). The "ok" it printed was vacuous.

   The script's `selftest` then exited 3 on a missing `injection-shokunin` fixture. The contract v1 §Census commands also run clean at `8df2fce`: 15 rows, 0 malformed, no dup/enum/missing-path/E08/E09 findings.
