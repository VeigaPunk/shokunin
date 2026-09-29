# Aggregator r11 connector — overlap and routing

Cutoff for volatile checks: **2026-09-29T03:37:47Z**. Commands below ran from the main-repo root. No fleet or child-repo state was changed.

## State

- **MANIFEST discrepancy is shared discovery/repair, not a zero-trace mint.** At 03:35:33Z the roster still had six IDs and 48 round entries. Entry `rounds[36]` is already `type:"mint"`, has no `lanes` map, and its note names kama/probation, but `minted: []`; r13/r14 entries have no kama lane status and their `minted` arrays are empty (or absent on later corrections). So “no ledger mention” is too strong; the missing part is machine-readable mint identity and a complete, attributable mint record. `.ufo/l0-questions.md` was the only path in the path-limited `17c1fad` stat despite the commit subject saying “kama row”; kama’s child repo has an r1 commit. See C1–C2.
- **Do not treat the missing roster row as an error yet.** The current lifecycle deliberately withholds a lane-initiated sibling’s roster row until three verified self-iteration rounds; the existing manifest note says that is why kama is in probation. The separate `type:"mint"` schema is explicitly for a *lane-initiated* mint and requires a mint-evidence pointer, probation note, and roster/ROADMAP status. The stated origin here is operator-directed, so the unresolved question is how that origin must be recorded—not whether to force kama into the roster now. File one unkeyed ledger finding for L1 to route to **protocol/integrator**: reconcile the operator-origin mint with the `minted` field and required evidence/status (or explicitly rule that the current note is sufficient). Do not patch `MANIFEST.json` or `PROTOCOL.md` from this seat; protocol owns appending rounds entries, and the current contract already assigns that work to the integrator. See C5 and C6.
- **Dormancy boundary:** kama is not a dormancy pair on the evidence here: r1 is complete and r2 is live per the supplied dispatch context, not two consecutive dispatched-and-reported rounds with no LOG activity. Protocol r13/r14 marker reports are failed markers under the given report contract and are excluded from dormancy pairs. The mint entry is also a recognized non-closure entry, not a lane-status tally. Keep kama visible as **minted/probation**, not as a fresh unserved-demand candidate and not as dormant; re-evaluate roster promotion only at the lifecycle threshold. (Lifecycle and marker classification: `PROTOCOL.md` §Lifecycle and the task’s marker rule.)

## Recent-work overlap map (rounds 14–18 plus kama r1)

| Lane | Intersection with mint / dormancy / corpus review | Action |
|---|---|---|
| **protocol** | r13/r14 reports are marker-only, so they cannot close a dormancy pair. The manifest has a narrative kama mint note but no explicit `minted` ID. Protocol/integrator is the manifest writer; aggregator is the discovery and routed-defect queue. | **route** — one ledger row to protocol/integrator; do not re-litigate lifecycle or force a roster row. |
| **kama** | r1 is the newly minted endpoint-identity lane; its cross-lane scope separates endpoint/service/model identity (kama) from credentials/request hygiene (kagi), route resolution (kumitate), agent wording (kotoba), evaluation (kengaku), and host edits (operator). It changes the mint/probation census, not the dormancy count. `MINT.md`/`cross-lane-scope.md` also show why kagi’s credential/endpoint findings are adjacent evidence rather than duplicate ownership. | **report** — represent as minted/probation, not a candidate duplicate; pass owner-specific findings to the named lane. |
| **kasegi** | r15 source-tree/citation-survival work is corpus-review evidence, not mint demand or dormancy. It is upstream of kake’s path-freshness work. The r11 registry ruling names **kasegi**, not kengaku, for the decree-ledger half of D-86. | **report** — retain as source-provenance context; do not let vanished source paths become a dormant-lane signal. |
| **kake** | r14/r15 freshness work tests corpus-path drift. My 03:33:33Z offline rerun found 48 resolved, 10 declared absent, 7 unresolved, 0 path drift, history `MATCH`; `complete:false` and all armed remote checks were skipped. This is useful citation-state evidence, not a fleet mint/dormancy grade or a full freshness pass. | **duplicate-risk** — use its citations as corpus-review context, but do not count its sweep as a second independent proof or as a dormancy signal. |
| **kagi** | r14/r15 turned the credential-hygiene checklist into a runnable declaration. The current `--ratio` command reports 9/16 runnable against floor 8, 7 by-hand; that is only the ratio mode, not a full checklist verdict. Its credential/request boundary is adjacent to kama’s endpoint identity, not the same check. | **report** — keep the evidence lane-local; route endpoint identity to kama and credential/auth hygiene to kagi. |
| **kumitate** | Its r14/r15 proxy and runtime-remainder work are lane-local scorecard/corpus evidence. The current proxy check is red on `PIN_DRIFT` (`pin.round-gate` declared and computed digests differ); its own documentation says it is not a fleet grade. Kumitate is also the routing/tooling side of D-86. | **route** — return the pin drift to kumitate; keep the D-86 boundary settled and route only the missing province follow-through. |
| **kotoba** | r14 coverage and instruction-surface evidence intersects corpus review; its prompt/agent wording ownership is separate from kama’s service identity. It contributes no mint/dormancy evidence by itself. | **report** — include in corpus review only; do not count checklists or prompt edits as LOG-based dormancy evidence. |
| **kengaku** | The gate-standard proposal is older than the 14–18 work window: protocol r12 resolved it as a three-valued outer verdict (`clean|failed|could-not-evaluate`) with lane-owned inner vocabularies. It is not an open Kengaku proposal to re-run. Kengaku is not named in the canonical D-86 split. | **none** — do not duplicate the closed gate ruling or assign D-86 to kengaku. |

### Cross-lane ownership edge

Kama’s boundary artifact explicitly assigns: endpoint/service/model identity → kama; credential/request/auth hygiene → kagi; route/dispatch resolution → kumitate; instruction/agent wording → kotoba; task/evaluation claims → kengaku; host-service/config changes → operator. The older 8080/34113 mismatch is therefore a shared *handoff*, not a reason for any one lane to absorb another lane’s edits. Kagi’s r15 handler port `40961` and its CDP/profile adjacency with kake are not kama’s model endpoint identity. Source: `kama-shokunin/corpus/knowledge/cross-lane-scope.md:3,12-30,38-51`, `kagi-shokunin/corpus/lessons/round-15.md`, and `kagi-shokunin/SKILL.md` checklist. Do not infer a current live endpoint state from those historical observations.

## Contested-scope checks

- **D-77 — ruled, do not reopen.** Protocol r11 settles per-lane sections in the single canonical `SCORECARD.md`/`LOG.md`, with each lane committing only its own section hunks; `55e23de` is the reference. AGGREGATE’s latest status says `RULED`. A stale root `SCORECARD.md` passage still says “ruling owed”; treat that as stale wording to clean up, not a live dispute or a reason to switch to per-lane filenames. Evidence: C4.
- **D-86 — ruling closed, follow-through open.** Protocol r11 assigns decree ledger → **kasegi**, routing plus `registry-check` → **kumitate**; both owe a `PROVINCE.md` record, so no re-arbitration. The task’s “kengaku/kumitate” locator does not match the canonical ruling: kengaku is not a D-86 owner. The requested case-insensitive literal scan found no `fleet/registry` text in any `*-shokunin/PROVINCE.md`; current kasegi/kumitate province text also does not state this split. Keep the missing record as D-76 follow-through, routed to kasegi and kumitate. Evidence: C4, plus `kasegi-shokunin/PROVINCE.md:17-18` and `kumitate-shokunin/PROVINCE.md:1-6`.
- **D-120 — closed, no root `SHONEN.md` workaround required.** The original main-repo premise was corrected: protocol’s r11 report assesses its canonical boxes against its own artifacts; aggregator re-filed its round-7 assessment under the heading in round 8. Both main-repo lanes adopted the report-local canonical assessment, and the root `SHONEN.md` is still absent as expected. Do not add one or re-route the old question. Evidence: C4.

## Evidence commands

Every command below is copy-paste runnable from the main-repo root. Dates are the observed UTC run instants; reruns will of course produce new timestamps.

**C1 — manifest roster and mint/round 13–14 fields** (run 2026-09-29T03:35:33Z):
```sh
python3 -c 'import json; d=json.load(open("MANIFEST.json")); print("roster="+repr([x["id"] for x in d["roster"]])+" rounds="+str(len(d["rounds"]))); [(print(i,"round=",r.get("round"),"type=",r.get("type"),"lanes=",r.get("lanes",{}),"minted=",repr(r.get("minted","<absent>")),"note_has_kama=","kama" in r.get("notes",""))) for i,r in enumerate(d["rounds"]) if r.get("round") in (13,14) or r.get("type")=="mint"]' && date -u +'%Y-%m-%dT%H:%M:%SZ'
```

**C2 — commit/path and kama child history** (run 2026-09-29T03:35:38Z):
```sh
git show --format='%h %aI %s' --stat --oneline 17c1fad -- MANIFEST.json ROADMAP.md .ufo/l0-questions.md; git -C kama-shokunin log -2 --format='%h %aI %s'; date -u +'%Y-%m-%dT%H:%M:%SZ'
```

**C3a — kumitate proxy** (run 2026-09-29T03:33:33Z; exit 1):
```sh
node kumitate-shokunin/scripts/proxy-check.mjs; rc=$?; date -u +'%Y-%m-%dT%H:%M:%SZ'; exit "$rc"
```

**C3b — kake offline freshness summary** (run 2026-09-29T03:33:33Z; partial/offline, not a full pass):
```sh
set -o pipefail; node kake-shokunin/scripts/freshness-sweep.mjs --offline --json | node -e 'let s="";process.stdin.on("data",d=>s+=d).on("end",()=>{const d=JSON.parse(s);const p=d.sections.paths,h=d.sections.history;console.log(JSON.stringify({generatedAt:d.generatedAt,complete:d.complete,code:d.code,pathCounts:p.counts,historyVerdict:h.verdict,armedChecksSkipped:d.skipped,gateWarnings:d.gateWarnings,reasons:d.reasons},null,2));process.exitCode=d.code})'; rc=$?; date -u +'%Y-%m-%dT%H:%M:%SZ'; exit "$rc"
```

**C3c — kagi ratio only** (run 2026-09-29T03:33:33Z):
```sh
bash kagi-shokunin/corpus/checklist-run.sh --ratio; rc=$?; date -u +'%Y-%m-%dT%H:%M:%SZ'; exit "$rc"
```

**C4 — source snapshot for D-77/D-86/D-120, gate ruling, province literal scan, and root SHONEN existence** (run 2026-09-29T03:33:48Z):
```sh
python3 -c 'import json; from pathlib import Path; d=json.load(open("MANIFEST.json")); print("MANIFEST roster="+repr([x["id"] for x in d["roster"]])+" rounds="+str(len(d["rounds"]))); [(print("manifest["+str(i)+"]="+json.dumps(r,sort_keys=True))) for i,r in enumerate(d["rounds"]) if r.get("type")=="mint" or r.get("round") in (13,14)]; spans={".ufo/reports/AGGREGATE.md":[(735,735),(1235,1240),(1468,1488)],".ufo/reports/round-11/protocol.md":[(222,248)],".ufo/reports/round-12/protocol.md":[(116,130),(341,344)],"PROTOCOL.md":[(157,169),(329,367)],"SCORECARD.md":[(133,135)]}; [(print("--- "+f+":"+str(a)+"-"+str(b)),print("\n".join(f"{i+1}: {s}" for i,s in enumerate(Path(f).read_text().splitlines()[a-1:b],a-1)))) for f,rs in spans.items() for a,b in rs]; hits=[(str(p),i,s) for p in Path(".").glob("*-shokunin/PROVINCE.md") for i,s in enumerate(p.read_text().splitlines(),1) if "fleet/registry" in s.lower()]; print("PROVINCE fleet/registry hits="+repr(hits)); print("SHONEN exists="+str(Path("SHONEN.md").exists()))' && date -u +'%Y-%m-%dT%H:%M:%SZ'
```

**C5 — mint-entry schema excerpt** (run 2026-09-29T03:37:47Z):
```sh
python3 -c 'from pathlib import Path; p=Path("PROTOCOL.md"); x=p.read_text().splitlines(); print("\n".join(f"{n}: {x[n-1]}" for n in range(201,212)))' && date -u +'%Y-%m-%dT%H:%M:%SZ'
```

**D-86 literal command specified for the routing check:**
```sh
grep -in 'fleet/registry' */PROVINCE.md
```
It should print no matches (exit 1) against the snapshot checked above; C4’s case-insensitive root-wide scan recorded `hits=[]` at 03:33:48Z.
