# kake round 85 — bounded registry discoverability and Referrer-Policy decoding

## Work performed

Declared claims: **C1 calibration** (lowest owned axis 2 HOLD), complete discoverable registry rows for three r84 instruments **0/3→3/3**; **C2 freshness** (10 HOLD), a separate sourced ordered Referrer-Policy decoder **0/10→10/10**. Both finite targets measured met, author-side; non-author closure owns admission. No claim that the whole D84 queue or general semantic-equivalence frontier is closed.

- Registered the three historical/experimental instruments with truthful CLI/exit/selftest/proof/scope/owner fields; `SKILL.md` round-85 registry; `w1/ExecRegistry.md` audit. C1 is discovery, not gate soundness.
- Landed `scripts/referrer_policy_effective.py`, a genuine sequential last-recognized-token walk with strict JSON input and 0/1/64 interface; `controls/decoder-selftest.txt`: 32/32, exit 0. ReviewCounter/CriticClaims disclose that the ten frozen cases alone admit a canned discriminator.
- Executed retained-property task: read ordered Referrer-Policy fields from six actual r81/r82 property capture receipts, decode and hand off absence (empty token, never browser default). Separate synthetic reversed r84 pair yields strict-origin versus no-referrer; `controls/integrated-trial.json`. No property fetched or published.
- Curated S458 and a new knowledge entry; lesson Gate/Mistakes and QUALITY criterion retain r84 semantic failure and counter limitations. `corpus/knowledge/referrer-policy-effective.md`, `corpus/lessons/round-85.md`.
- One validated v1 wave, ten requested and ten nonempty settled: scout 1, executor 3, scribe 2, reviewer 2, critic 1, connector 1; attack 3/10=30%; no dead seats, replacements or residual calls. `w1-results.json`, `w1-accounting.json`. Results omit agent IDs/status; none invented. WAVE-DONE preceded L1-only production integration; seats wrote only disjoint candidate/evidence paths. Planner held by L1, scout planning data-walk; literal dispatched-planner disagreement remains open. Actual routing read before dispatch: all roles @m_zfl; no model passed, actual answering model not claimed.
- Frozen unchanged-base controls were committed before dispatch. Additional shortcut controls were captured late after ready handoff, explicitly labelled in `controls/late-shortcut-c1.txt`/`late-shortcut-c2.txt`: this sequence defect is not concealed or retroactively frozen. Predicates/targets never moved after scoring.

Evidence paths above are relative to lane `.ufo/waves/round-85/` unless prefixed corpus/scripts/SKILL.

## Landed changes

Every item is tied to `LOG.md:2792` (Round 85):

| Commit | Landed work |
|---|---|
| 2f042c370b5f11b84d4f8c9e5d066517aef646b8 | Frozen independent claims, count.py, red committed-base controls, census-before and operative-binding receipt |
| 856fa46bbeaf23d5d625be5d448852a6fe22c6e0 | Validated ten-seat spec, dispatch and ready handoff |
| aea07bf3c1d9e5ad50453af4e11cc52faf420e51 | Decoder, registry rows, source/knowledge/lesson/QUALITY/README/PROVINCE updates, wave results/accounting, selftest/property trial and disclosed shortcut controls |
| 21211219803af39c6e5e369fc2a267e38bb08c38 | Revision-pinned carrier after receipts, SCORECARD capability and LOG records |

Final lane tip `21211219803af39c6e5e369fc2a267e38bb08c38` is pushed: `git -C /home/vgpnk/Projects/shokunin/kake-shokunin ls-remote origin refs/heads/master` printed that exact hash. No inherited uncommitted work existed at launch; integrator-authored r84 spotcheck remained untouched. Uncommitted pre-freeze broad planning draft was discarded before scoring; frozen scope is only these two bounded claims.

## Before → after measurements

Same frozen command, once for each claim/revision:

```sh
python3 -B .ufo/waves/round-85/count.py --root . --revision <rev> --claim c1 --work /fast/scratch/hyaku/kake-r85/L1-count
python3 -B .ufo/waves/round-85/count.py --root . --revision <rev> --claim c2 --work /fast/scratch/hyaku/kake-r85/L1-count
```

| Claim | Base bdabc6bc8f762a16c6c19c524c4ac84528eb4bf7 | Carrier aea07bf3c1d9e5ad50453af4e11cc52faf420e51 | Receipts |
|---|---|---|---|
| C1 | `C1 complete=0/3 missing=3 met=false`, exit 1 | `C1 complete=3/3 missing=0 met=true`, exit 0 | controls/base-c1.txt → controls/after-c1-carrier.txt |
| C2 | `C2 cases=0/10 met=false`, exit 1 | `C2 cases=10/10 met=true`, exit 0 | controls/base-c2.txt → controls/after-c2-carrier.txt |

No re-scoring the legacy numeric ceiling: calibration 2→2 HOLD, freshness 10→10 HOLD, operability unchanged. Offline freshness sweep exit 0 is explicitly partial (remote/history skipped), not a complete publishing check. C1 false-row and C2 canned-output counterexamples remain disclosed; source-inspected mappings, sequential code, independent reference trial and 32/32 subprocess selftest are separate evidence, not repairs to the frozen numerator. Counter has no selftest interface and is registered as a finite instrument, not a conformant standing gate.

## Sources & frontier

Registry rows **195→196**; added tier A=1 (S458, mined), B=0, C=0. No old status/recheck/used-by cell changed. New row only: absent→mined, used-by corpus/knowledge/referrer-policy-effective.md. Bounded field-specific interpretation advanced into held Frontier ground; no general classifier semantics or browser execution promoted. Source opened this round: https://w3c.github.io/webappsec-referrer-policy/, §8.1 step 3; retained quote/location/date in lesson Gate. The separate TR rendering is identified rather than conflated with the registry URL.

Counting command: `python3 -c 'import pathlib,re; print(len(re.findall(r"^ {0,3}\|\s*S\d{3,}\s*\|",pathlib.Path("corpus/SOURCES.md").read_text(),re.M)))'` at base/carrier yields 195/196 (raw regex row census in integration transcript).

Required command, both recorded exits 0:

```sh
/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kake
```

Before:
```text
kake	W04	S033 duplicate url www.rfc-editor.org/rfc/rfc9110.txt across scopes
kake	W04	S088 duplicate url www.rfc-editor.org/rfc/rfc9110.html across scopes
kake	W04	S092 duplicate url html.spec.whatwg.org/multipage/syntax.html across scopes
kake	W04	S098 duplicate url www.rfc-editor.org/rfc/rfc3986.txt across scopes
kake	W04	S099 duplicate url www.rfc-editor.org/rfc/rfc9309.html across scopes
kake	W04	S102 duplicate url www.sitemaps.org/protocol.html across scopes
kake	W04	S110 duplicate url www.w3.org/TR/xml across scopes
kake	W04	S111 duplicate url docs.python.org/3/library/urllib.parse.html across scopes
kake	W04	S115 duplicate url docs.python.org/3/library/urllib.parse.html across scopes
kake	W04	S116 duplicate url docs.python.org/3/library/urllib.parse.html across scopes
kake	W04	S117 duplicate url www.rfc-editor.org/rfc/rfc3986.txt across scopes
kake	W04	S127 duplicate url www.rfc-editor.org/rfc/rfc9844.txt across scopes
kake	W04	S416 duplicate url ziyuan.baidu.com/college/courseinfo?id=1399 across scopes
kake	W04	S417 duplicate url ziyuan.baidu.com/college/courseinfo?id=267&page=15 across scopes
kake	W04	S427 duplicate url developers.google.com/crawling/docs/crawlers-fetchers/overview-google-crawlers across scopes
kake	W04	S433 duplicate url www.rfc-editor.org/rfc/rfc9110.html across scopes
kake	W04	S445 duplicate url html.spec.whatwg.org/multipage/links.html across scopes
kake	W04	S450 duplicate url html.spec.whatwg.org/multipage/semantics.html across scopes
kake	W04	S451 duplicate url www.rfc-editor.org/rfc/rfc3339.txt across scopes
kake	W04	S453 duplicate url www.rfc-editor.org/rfc/rfc9110.txt across scopes
kake	W04	S454 duplicate url www.rfc-editor.org/rfc/rfc9110.txt across scopes
kake	W04	S455 duplicate url www.rfc-editor.org/rfc/rfc9110.txt across scopes
kake	ok	/home/vgpnk/Projects/shokunin/kake-shokunin/corpus/SOURCES.md
census_exit=0
```

After (the receipt's command prefix is retained verbatim):
```text
command=["/home/vgpnk/Projects/shokunin/scripts/sources-census.sh", "validate", "--root", "/home/vgpnk/Projects/shokunin", "kake"]
kake	W04	S033 duplicate url www.rfc-editor.org/rfc/rfc9110.txt across scopes
kake	W04	S088 duplicate url www.rfc-editor.org/rfc/rfc9110.html across scopes
kake	W04	S092 duplicate url html.spec.whatwg.org/multipage/syntax.html across scopes
kake	W04	S098 duplicate url www.rfc-editor.org/rfc/rfc3986.txt across scopes
kake	W04	S099 duplicate url www.rfc-editor.org/rfc/rfc9309.html across scopes
kake	W04	S102 duplicate url www.sitemaps.org/protocol.html across scopes
kake	W04	S110 duplicate url www.w3.org/TR/xml across scopes
kake	W04	S111 duplicate url docs.python.org/3/library/urllib.parse.html across scopes
kake	W04	S115 duplicate url docs.python.org/3/library/urllib.parse.html across scopes
kake	W04	S116 duplicate url docs.python.org/3/library/urllib.parse.html across scopes
kake	W04	S117 duplicate url www.rfc-editor.org/rfc/rfc3986.txt across scopes
kake	W04	S127 duplicate url www.rfc-editor.org/rfc/rfc9844.txt across scopes
kake	W04	S416 duplicate url ziyuan.baidu.com/college/courseinfo?id=1399 across scopes
kake	W04	S417 duplicate url ziyuan.baidu.com/college/courseinfo?id=267&page=15 across scopes
kake	W04	S427 duplicate url developers.google.com/crawling/docs/crawlers-fetchers/overview-google-crawlers across scopes
kake	W04	S433 duplicate url www.rfc-editor.org/rfc/rfc9110.html across scopes
kake	W04	S445 duplicate url html.spec.whatwg.org/multipage/links.html across scopes
kake	W04	S450 duplicate url html.spec.whatwg.org/multipage/semantics.html across scopes
kake	W04	S451 duplicate url www.rfc-editor.org/rfc/rfc3339.txt across scopes
kake	W04	S453 duplicate url www.rfc-editor.org/rfc/rfc9110.txt across scopes
kake	W04	S454 duplicate url www.rfc-editor.org/rfc/rfc9110.txt across scopes
kake	W04	S455 duplicate url www.rfc-editor.org/rfc/rfc9110.txt across scopes
kake	ok	/home/vgpnk/Projects/shokunin/kake-shokunin/corpus/SOURCES.md
exit=0
```

22 W04 warnings unchanged, not failures. Assimilation: none — no staged package adopted. Connector's collision receipt finds 8 shared IDs, all matching URL sets; S458 is absent from both input registries before this round. `considerthese/2026-10-26.md` proposal 5 mined into lesson's historical-versus-current gate table, without pretending historical-red status excuses false accepts. Mistake fix is shown red-before by absent decoder and reversed-token witness; finite shortcut weakness and late controls remain explicitly disclosed.

D84-1 addressed within registry discovery; D84-2/3 remain open; D84-4 has read-before-dispatch and single-integration-owner mitigations but planner interpretation remains unresolved. Existing L0 questions unchanged; no new operator decision needed. Cross-domain browser/runtime observation belongs to tabi and credential custody to kagi; neither absorbed. No tool installs/upgrades; pacman untouched. Scratch round tree removed after landing. Fleet misroot sweep `controls/fleet-misroot-sweep.txt`: no attributable kake/r85 root file; unrelated orchestrator scratch and root `after` untouched.

## Trend verdicts

- **expansion: improved** — separate sourced field-specific entry/capability on previously unheld effective-token ground, S458 and retained trial; generic semantics remain frontier.
- **quality: improved, bounded** — truthful registry mappings and separate last-recognized decoder with red-before/green-after evidence; r84 experimental overreach remains marked rather than silently approved. No owned-axis harm observed on exercised checks.
- **discernment: unchanged pending outside review** — author-side reviewers agree on the counterexample and expose counter shortcuts, but no self-dispatched seat substitutes for non-author admit/reject judgment.

Stale-lane: respawn-per-round; no other kake mission open. No round 86 started. No publication, deploy, account, DNS, credentials, MANIFEST or upstream source mutation.

## SHONEN

- [~] Decision tables/checklists/sources: SKILL.md and corpus/knowledge/referrer-policy-effective.md; author assertion, no promotion.
- [ ] End-to-end checklist gap remains the historical missing receipt named in SHONEN.md box 2; this bounded retained-data trial does not erase it.
- [~] Executable instructions: decoder command/selftest and revision-pinned count commands; no non-author promotion verifier.
- [~] Province boundaries: PROVINCE.md round-85 scope preserves browser/publishing authority; no cross-domain absorption.
