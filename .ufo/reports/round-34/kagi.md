# kagi — round 34 report

Lane tip (landed and pushed): `aa43fdb52396f5f6d5f283bb95776cb40b328e53`.
`git -C /home/vgpnk/Projects/shokunin/kagi-shokunin ls-remote origin refs/heads/master`
printed that hash. Frozen BASE `f9dc06fd8f6b43c175193c76dc6350468f551634`; plan-only
commit `5a2f145ee80b6879a833c2e70d16f2671d103367`.

## Work performed

Declared claims: **C1 calibration** — SD7–SD9 self-description mismatch sum5→0;
**C2 operability** — prefreeze selftest11→12 plus observed M7 mutant failure;
**C3 coverage** — AccessKey custody entry and frozen registry/census totals.
**C1/C2 target readings verified to their bounded predicates; C3 NOT ADMITTED.
The round is an honest stop, not an admitted round.** Independent closure remains external.

- Delivered SD7 script-name presence, SD8 lesson-range upper endpoints and SD9
  provenance-presence checks; repaired three registry omissions, the README range,
  and the prefreeze entry trio. Evidence: `corpus/self-description-sweep.sh`,
  `SKILL.md` round34 registry, `corpus/lessons/round-34.md`; final producer receipts
  `.ufo/waves/round-34/final/c1-*-final-producer.txt`.
- Preserved ten selftest cases while strengthening two fixtures after M5/M6 survived
  MutSweep. Both mutants now FAIL; retained evidence
  `.ufo/waves/round-34/build/receipts/sd9-hardening-*.txt`. No predicate was widened.
- Added real relative-work execution and the canonicalization-removal red witness;
  rebuilt M7 against the shipped twelve-case bytes. Evidence:
  `.ufo/waves/round-34/final/prefreeze-selftest.txt`,
  `.ufo/waves/round-34/build/receipts/gate-unfixed-relative-work.txt`,
  `.ufo/waves/round-34/mut/m7-shipped.txt`.
- Assimilated one Alibaba RAM credential-custody theme as one corrected entry;
  opened all five vendor sources myself and own-work source S088. Six rows/captures
  land. Entry: `corpus/knowledge/aliyun-accesskey-credential-custody.md`;
  provenance: `corpus/source-fetches.tsv`; Gate quotes and refusal reasons:
  `corpus/lessons/round-34.md`.
- Closed the concrete round33 registry/provenance/count/evidence defects, but did
  not rewrite its historical report or manufacture earlier execution. R33-6's
  command-attribution error is corrected here; R33-7 now has an executed docs receipt.
  Full dispositions: lesson §Migrations. QM35/QM36 carry mined mistakes and red witnesses.
- Connector found no sibling ownership of Alibaba RAM credential custody in its
  bounded20-lane scan. Kama already holds a self-description instrument class:
  C1 is a kagi-local extension, not fleet-unique invention.
  `.ufo/waves/round-34/build/ConnOverlap.md`.

## Landed changes

Every item is tied to `LOG.md` **Round34**, lines1687–1695:

| Work | Carrying commit(s) |
|---|---|
| Frozen plan, ten executed BASE controls and START receipts | `5a2f145ee80b6879a833c2e70d16f2671d103367` |
| Two gates, three registry rows, corrected docs, AccessKey entry, S083–S088, lesson, QM35/QM36, ledger migrations and111 stamps | `b4e9fd9a474583db69b9601d162c6eb9e54ce0d6` |
| Parser-compatible post-move heading, valid encoded source locator and recorded first verification | `fb3d3ccd7f9714377690388431c30efd4fb9d82a` |
| Remaining score evidence cells and corrected cell audit | `c5e0ecef2843dc8fded337780c579102ef8c9ee8` |
| Final measured SCORECARD record, frozen counters and remaining wave receipts | `aa43fdb52396f5f6d5f283bb95776cb40b328e53` |

No operator/integrator-authored lesson was edited. Source package and sibling repos
remained read-only. No new capability-table row or scalar-score increase is claimed.

## Before → after measurements

### C1 — bounded target verified, counter-strength defect disclosed

Exact frozen counter (from lane root):

```sh
bash corpus/self-description-sweep.sh | awk -F'[ =()]' \
  '{for(i=1;i<NF;i++) if($i ~ /^SD[789]$/) s+=$(i+1)} END{print s+0}'
```

Delivered counter at `c5e0ecef…` over BASE extraction: **5** (SD7=3 SD8=1 SD9=1),
producer exit1. Same counter on `c5e0ecef…`: **0** (SD7=0 SD8=0 SD9=0), producer
exit1. Three integrator-owned SD6 findings remain, as excluded at freeze.
Both runs retained complete component-bearing output, not SETUP:
`final/c1-base-final.txt`, `final/c1-tip-final.txt` and their producer files
under `.ufo/waves/round-34/`. `--selftest`: PASS7→PASS10, exit0
(`controls/prefreeze-base.txt`, `final/sweep-selftest.txt`).

**Reviewer dissent:** ReviewC1 shows the frozen awk returns0 for SETUP/empty output,
and presence checks can be satisfied cosmetically. The frozen counter is unchanged;
our actual measured producer did evaluate and exposes all three components.
No semantic registry/provenance completeness is inferred. The helper and delivered
counter match this BASE, not universally. Source SHA:
`45d8e4a2d0bbf152d1f21a7acc073dbe6cc987cb857e2f903df6a7bb6fe640a9`.

### C2 — target readings verified, normalized receipt labelled

```sh
bash corpus/prefreeze-control.sh --selftest | tail -1
grep -c 'CASE base-isolation FAIL' .ufo/waves/round-34/mut/m7-shipped.txt
```

BASE: PASS11; receipt absent (existence control0; literal grep on an absent file
would exit2, not print0). After: **PASS12**, exit0; receipt counter **1**, exit0.
Selftest executed at `b4e9fd9a…`; final counter and SHA binding at `c5e0ecef…`.
Shipped source SHA `ca338da7c7400e07fa551c42b02a4bb6b7bedf4c47bda849e1aa162fbc86493a`.
Receipts: `final/prefreeze-selftest.txt`, `final/remaining-counters.txt`,
`mut/m7-shipped.txt` under `.ufo/waves/round-34/`.

The raw ck line pads its case name; the matching single-space line is an explicitly
**derived normalized verdict**, not raw stdout. Raw output, exit1, source/mutant
digests are retained. M7 fails **both** base-isolation and relative-work;
ReviewC2's stronger exclusivity test fails, while the frozen predicate requires the
named witness, not exclusivity. A handwritten or wrong-SHA receipt could satisfy
literal grep; observed execution and identity evidence are supplied separately.

### C3 — NOT ADMITTED; frozen kill rule fires

```sh
ls corpus/knowledge/aliyun-accesskey-credential-custody.md | wc -l
grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md
bash corpus/sources-census.sh
```

| Reading | BASE | Frozen target | Actual |
|---|---:|---:|---:|
| Entry files | 0 | 1 | 1 |
| Registry rows | 82 | 87 | **88** |
| Sourced entries | 12 | 13 | **14** |
| Legacy entries | 22 | 21 | 21 |
| Captured registry ids | 82 | 87 | **88** |

Population error: migrating prefreeze provenance adds one sourced entry before the
new AccessKey entry adds another; its valid own-work provenance also requires S088.
Neither entry is deleted, provenance stripped, census narrowed, nor target rewritten.
Census is CLEAN exit0 at the **actual** counts (`final/census-tip.txt`, executed at
`b4e9fd9a…`, unchanged registry population thereafter); final entry/row counters at
`c5e0ecef…`. CriticClaims independently identifies the cross-claim coupling. This
prevents round admission despite useful landed content.

## Sources & frontier

- Registry82→88; added **A=5, B=1, C=0** (four primary Chinese vendor docs, one
  Japanese translation tierB, one own-work source). Mined78→84. Existing
  status/recheck/used-by cells unchanged; no existing row silently corrected.
- Entry coverage: one new cloud-IAM AccessKey custody entry. This was uncovered
  ground, not release-clock frontier movement; release clocks remain the frontier.
- `Assimilation: one AccessKey-custody theme, one corrected entry admitted; original
  staged text refused as-is (application handling, idle-key branch and object scope).
  Flip and located quotes are in corpus/lessons/round-34.md Gate.`
- Staged→lane document map: S140→S083, S141→S084, S142→S085, S143→S086,
  S145→S087. Complete id lists are committed as
  `.ufo/waves/round-34/assimilation/reg-ids` and `staged-ids`; their intersection
  (`collisions`) has31 ids (S052–S082); selected-id collisions0. Indented-row witness
  and quarantine selection are in `selection.json`. Eight unselected quarantine
  rows remain quarantined; no new fabrication verdict is asserted for them.
- Append pregated in scratch: fleet census exit0 and lane census exit0 at88 rows;
  receipts `assimilation/scratch-fleet-census.txt`, `scratch-lane-census.txt`.
  Multi-source-line draft fails the existing census with five findings
  (`multiple-source-lines-red.txt`); installation consolidates the same five ids.
  Captures are reconciled to preserved ScoutSources bodies, not another seat's
  removed independent bytes. Normalized quote locations all succeed.
- Latest considerthese file reopened; no proposal selected for the reasons in the
  lesson. No operator-authored proposal file edited.
- Mistakes M34-1..M34-5 recorded with evidence, captured-by and bounded fixes;
  QM35/QM36 grounded in actual red-before receipts. Independent admit/reject
  spot-check remains for non-author closure, not supplied by our own seats.

Required fleet-census command, run at round start and end:

```sh
/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kagi
```

START output, **exit0**, `controls/fleet-census-start.txt`:

```text
kagi	W04	S019 duplicate url www.1password.dev/brokered-access across scopes
kagi	W04	S020 duplicate url 1password.com/blog/1password-credential-broker-public-preview across scopes
kagi	W04	S021 duplicate url openbao.org/docs/concepts/tokens across scopes
kagi	W04	S022 duplicate url developer.hashicorp.com/vault/docs/auth/jwt across scopes
kagi	W04	S023 duplicate url developer.hashicorp.com/vault/docs/concepts/lease across scopes
kagi	W04	S025 duplicate url openbao.org/docs/auth/jwt across scopes
kagi	W04	S026 duplicate url openbao.org/docs/concepts/tokens across scopes
kagi	W04	S032 duplicate url www.1password.dev/brokered-access across scopes
kagi	W04	S039 duplicate url www.python.org/downloads/feed.rss across scopes
kagi	W04	S040 duplicate url docs.python.org/3/library/re.html across scopes
kagi	W04	S041 duplicate url docs.python.org/3/library/html.html across scopes
kagi	W04	S045 duplicate url semver.org/spec/v2.0.0.html across scopes
kagi	W04	S050 duplicate url docs.github.com/en/actions/concepts/security/openid-connect across scopes
kagi	W04	S051 duplicate url csrc.nist.gov/pubs/sp/800/57/pt1/r6/ipd across scopes
kagi	W04	S069 duplicate url www.1password.dev/brokered-access across scopes
kagi	W04	S070 duplicate url www.1password.dev/brokered-access/custom-workflow across scopes
kagi	ok	/home/vgpnk/Projects/shokunin/kagi-shokunin/corpus/SOURCES.md
```

END output, **exit0**, `final/fleet-census-tip.txt`:

```text
kagi	W04	S019 duplicate url www.1password.dev/brokered-access across scopes
kagi	W04	S020 duplicate url 1password.com/blog/1password-credential-broker-public-preview across scopes
kagi	W04	S021 duplicate url openbao.org/docs/concepts/tokens across scopes
kagi	W04	S022 duplicate url developer.hashicorp.com/vault/docs/auth/jwt across scopes
kagi	W04	S023 duplicate url developer.hashicorp.com/vault/docs/concepts/lease across scopes
kagi	W04	S025 duplicate url openbao.org/docs/auth/jwt across scopes
kagi	W04	S026 duplicate url openbao.org/docs/concepts/tokens across scopes
kagi	W04	S032 duplicate url www.1password.dev/brokered-access across scopes
kagi	W04	S039 duplicate url www.python.org/downloads/feed.rss across scopes
kagi	W04	S040 duplicate url docs.python.org/3/library/re.html across scopes
kagi	W04	S041 duplicate url docs.python.org/3/library/html.html across scopes
kagi	W04	S045 duplicate url semver.org/spec/v2.0.0.html across scopes
kagi	W04	S050 duplicate url docs.github.com/en/actions/concepts/security/openid-connect across scopes
kagi	W04	S051 duplicate url csrc.nist.gov/pubs/sp/800/57/pt1/r6/ipd across scopes
kagi	W04	S069 duplicate url www.1password.dev/brokered-access across scopes
kagi	W04	S070 duplicate url www.1password.dev/brokered-access/custom-workflow across scopes
kagi	ok	/home/vgpnk/Projects/shokunin/kagi-shokunin/corpus/SOURCES.md
```

The detailed population summary above comes from **bash corpus/sources-census.sh**,
not the fleet validator: START CLEAN rows82/sourced12/legacy22/captures82, exit0;
END CLEAN rows88/sourced14/legacy21/captures88, exit0. Both commands' outputs and
exit codes remain separately attributed (round33 routed defect R33-6).

## Trend verdicts

- **expansion: improved.** One sourced entry on newly held cloud-IAM custody ground;
  five vendor rows plus own-work provenance migration. The frozen coverage claim
  nevertheless fails; content expansion is not a claim-target pass.
- **quality: improved.** Executed relative-work/M7 red witnesses, two closed mutation
  escapes, valid provenance and corrected source-object boundaries. Marked limits
  remain: fail-open frozen awk, SD9 first-line/presence bounds, and policy reds.
- **discernment: improved.** Round33 disagreements become QM35/QM36 and observed
  failure receipts; C3's own arithmetic is reported failed rather than re-scoped.
  This is lesson-backed improvement, not independent agreement or promotion.

## SHONEN

- [~] Decision tables, failure patterns and cited checklist — `SKILL.md`, including
  the three complete round34 registry rows; no non-author checkmark claimed.
- [~] End-to-end task logged — existing `LOG.md` round3 auth-gate outcome remains;
  round34 executes BASE-control and public-source curation work, not live vault ops.
- [~] Executable instructions — PASS12/PASS10 selftests, CLEAN source/docs/EOL receipts
  under `.ufo/waves/round-34/final/`; counter limitations explicitly recorded.
- [~] Province boundary maintained — `PROVINCE.md` round34 core bullet,
  `build/ConnOverlap.md`; CDP/profile contest remains reported, not adjudicated.

## Round shape and residual findings

One v1 wave `kagi-r34-build`: **13 seats** — 3 executor, 3 scribe, 2 scout,
1 connector, 2 reviewer, 1 critic, 1 mutation-tester. Attack4/13=30.8%; connector1.
L1 holds planner (validator excludes planner); no residual call, nested spawn or
replacement. Plan's14-seat line is a typo; actual dispatch/results name13, not14.
WAVE-DONE received **before report**; all13 settled with nonempty results, dead0.
ExecSD resumed in the same identity to close M5/M6; no new seat.

Additional exercised checks: docs CLEAN entries35/row-linked32/by-hand3, exit0;
EOL CLEAN, exit0; self-counts POLICY claims62/stale0/policy2, exit2;
corrected cells POLICY cells252/row_pointed183/stamp_pointed124/policy2, exit2.
R25-02 FAIL and R29-01/R29-02 POLICY persist. The audit also reports non-ledger
closure-identifier MISSING-ID tokens, including seven in this round's appended LOG
correction; historical LOG bytes and integrator-owned lessons were not rewritten to
hide those findings. The initial candidate had an invalid score heading and a URL
misclassified as a sibling path; both corrected in subsequent commits, with the
first failed receipts preserved. Final sweep's SD6 returns to the three frozen
integrator-owned residuals. No claim that every audit is CLEAN.

- **Stale-lane:** respawn-per-round; no other mission of kagi is open.
- **Misroot sweep:** fleet status showed only orchestrator `.scratch/` artifacts and
  pre-existing `after`; none belongs to this round's seats. Left untouched.
- **Tool installs:** none; pacman pause respected. No vault/account/handler contact.
- **L0:** no new question. Existing kagi round30/round32 operator-policy residuals
  remain unanswered; no policy fix is claimed.
- **Scratch:** `/fast/scratch/hyaku/kagi-r34` removed after lane landing.
