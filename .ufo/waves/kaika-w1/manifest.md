# W1 — MANIFEST.json ledger consistency audit

- **Scope:** `/home/vgpnk/Projects/shokunin/MANIFEST.json` (294 `rounds[]` entries, 13 roster rows; `wc -lc` = 5407 lines / 306760 B) vs `/home/vgpnk/Projects/kimi-shokunin/templates/MANIFEST.schema.json`, plus roster drift vs `shokunin.conf` `LANES` and `README.md` roster table.
- **Validator note:** no JSON-schema validator installed (`python3 -c "import jsonschema"` → ModuleNotFoundError; `ajv`/`check-jsonschema` absent; node `require('ajv')` fails). All results below are a hand-rolled jq walk. **`jq` here is jaq 3.1.1, not jq** — bare `select(f|g)` binds `.` differently than jq; every query uses `as`-bindings. All commands verified against `jaq` on this host.
- **Protocol authority:** `PROTOCOL.md:239–310` (round-entry shape, row identity, append-only) is stricter and newer than the upstream schema. Both lenses are reported.

## 1. Entry shapes — `jq -r '.rounds[]|"\(.type // "NULL")\t\(keys_unsorted|join("+"))"' MANIFEST.json | sort | uniq -c`

294 entries, **31 distinct key-shapes** grouped under **11 type values** (`jq -r '.rounds[].type' MANIFEST.json | sort | uniq -c`):

| count | type | dominant shape |
|---|---|---|
| 129 | closure | `round,date,type,closed_at,lanes,lane_rounds[,supersedes,promotions,minted,admitted,verdicts,protocol_updates],notes` — 13 sub-shapes |
| 63 | train | `round,date,type,lane,verdicts,notes[,commit]` — per-lane verdict, axis-keyed `verdicts` |
| 56 | closure-correction | `round,date,type,closed_at,supersedes,lanes[,lane_rounds,minted,promotions,admitted,verdicts,protocol_updates],notes` — 8 sub-shapes |
| 13 | retroactive-closure | `round,date,type,closed_at,lanes[,lane_rounds,promotions,minted],notes` — 3 sub-shapes |
| 10 | mint | `round,date,type,minted,notes` (fractional `round` 11.5 also occurs) |
| 9 | craft | `type,lane,round,date,claims,verdict,axes,wave,gate_sha,report,evidence,note` |
| 5 | **(none)** | `round,lane,loop,position,provider,model,requested_workers,filed,verdict,admitted,claims,baseline_commit,close_commit,note,receipt` — kotodama loop-ledger rows |
| 3 | ops | two shapes; the two newer carry `closed_at,program,status,report[,commit],minted,promotions` |
| 3 | train+audit (2) / train+audit+unlock (1) | `train` shape + `commit` |
| 2 | work | `round,date,type,lanes,minted,protocol_updates,notes` (no `closed_at`, no `lane_rounds`) |
| 1 | scaffold | `round,date,type,notes` |

- Date range `2026-09-28 .. 2026-10-19`; `round` values 0 .. 104 (incl. fractional 1.5, 11.5).
- **Eras:** 2026-09-28/29 fleet-keyed (work/retroactive-closure/closure, multi-lane, no `lane_rounds` on the oldest) → 2026-10-13+ mixed lane-keyed (train/craft/loop) and single-lane closure entries where `round` is the lane's own counter → 2026-10-17+ per-lane single-row closures.

## 2. Schema violations (jq walk of `MANIFEST.schema.json`)

| violations | rule |
|---|---|
| 75 | `type` not in enum: 63 `train`, 9 `craft`, 2 `train+audit`, 1 `train+audit+unlock` — the per-lane verdict era is entirely absent from the schema's type list |
| 24 | `lanes` value `closed` not in `{ok, failed, not-dispatched, in-flight}` — entries 142–165: mori lr 2–11, chousa lr 2–11, kengaku lr 19–22 |
| 5 | missing `type` — kotodama loop rows (entries 272, 277, 279, 291, 293); same 5 also missing `date` |
| 44 | `supersedes` carries `entry` — violates schema `additionalProperties:false`, but **`PROTOCOL.md:302–304` explicitly allows `entry` as the disambiguator**; the schema lags the fleet protocol |
| 1 | `not-dispatched` row without `closed_at` — round-1 `work` entry (kagi), 2026-09-28; violates both schema `allOf` and `PROTOCOL.md:251–252` |
| 1 | `round: null` — entry 138 (multi-lane snapshot closure keyed only by `lane_rounds`); fails schema `type:number` |
| 0 | bad `date`/`closed_at` formats, bad lane-id patterns, bad `lane_rounds` values, dangling `supersedes` targets |

Non-violation noted: `roundEntry` has no `additionalProperties:false`, so every era's extension keys (`verdicts`, `commit`, `receipt`, `wave`, `gate_sha`, `loop`, `program`, `status`, …) pass the schema formally while being fully undescribed.

## 3. Semantic defects (beyond formal schema)

1. **`round` namespace collision.** Fleet era: `round` = fleet round (`(lane, entry.round)` per `PROTOCOL.md:283–289`). Lane era: `round` = the lane's own counter (e.g. souji entries 222–245: `round` 1–11 with `lane_rounds` absent — lane-round semantics; chousa `closed` entries carry `round` 12–21 while `lane_rounds` is 2–11 — neither). Same key, two domains; the protocol's row-identity clause only governs the first.
2. **`closed` rows supersede partially.** 24 raw `closed` rows → 21 stand after last-wins; the status is not in the enum and `closed`/`ok` are used interchangeably for identical lane-rounds (chousa round-1 closure says `in-flight`, later craft entries show the work landed).
3. **Ambiguous `supersedes`.** Entry 24 (closure-correction, `11|closure-correction|2026-09-28`) omits `entry` while **3 candidates** match the triple — the exact case `PROTOCOL.md:302–305` gates on. 27 (round,type,date) triples collide overall (`0|mint|2026-10-14` ×6, `11|closure-correction|2026-09-28` ×3, `37–42|closure|2026-10-19` ×2 each…).
4. **Unresolved `in-flight` debt — 10 rows** (last-wins over `(lane, entry.round)`): `aggregator|12`, `chousa|1`, `kagi|17`, `kake|18`, `kama|2`, `kasegi|18`, `kengaku|15`, `kotoba|17`, `kumitate|17`, `protocol|15`. `kama|2` has been debt since 2026-09-29.
5. **`verdicts` is untyped.** Values are free strings: `improved x449`, `unchanged x224`, plus `improved-incomplete`, `improved-bounded`, `verified`, `harmed x1`, and long prose verdicts — and one `_note` key smuggled into an axis map. Axis vocabulary itself drifted: era-1 `expansion/quality/discernment` vs current `adjacency/calibration/coverage/depth/freshness/operability` (+`consistency` once).
6. **Zero rows for `revenger`** — rostered since 2026-10-11, but no `lanes` row, `lane_rounds`, `train`, `craft`, loop, or mint entry ever names it (verified: `jq` lane-key sweep). Rostered lane with an empty ledger.
7. **`kama` probation never resolved**: minted 2026-09-29 via `round:11.5` mint entry with `minted:[]` and "roster row withheld" note; roster row exists; ledger coverage stops at lane-round 4 (entry 138).
8. **Lanes with no `lane_rounds` coverage at all**: `audio`, `game-dev-3d`, `mado`, `revenger`, `souji`, `tabi`, `tameshi`, `tsukuroi` (souji uses `round` instead; the others appear only in `train` rows).

## 4. Roster drift — three registries disagree

`MANIFEST.json` roster (13): audio, game-dev-2d, game-dev-3d, kagi, kaidoku, kake, kama, kasegi, kengaku, kotoba, kumitate, lore, revenger.
`shokunin.conf` `LANES` (20 incl. 2 meta): aggregator, chousa, kagi, kaidoku, kake, kama, kasegi, kengaku, kotoba, kotodama, kumitate, lore, mado, mori, protocol, revenger, souji, tabi, tameshi, tsukuroi.
`README.md` roster table (16): adds chousa, kotodama, mori to the manifest's 13 minus none — omits mado, souji, tabi, tameshi, tsukuroi.

- **Minted but never rostered (8):** tameshi, mado, tsukuroi, tabi, mori, chousa (all minted 2026-10-14 per `round:0` mint entries), kotodama (2026-10-17), souji (2026-10-18). PROTOCOL.md:49–50 says the roster row lands *after probation*, notes recording the state meanwhile — so this is expected drift **unless** probation has passed; chousa is at round 24, mori at 11, tabi/tameshi/tsukuroi/mado at 11 — all past the ≥3-round probation bar, rows still absent. Mori/chousa/kotodama are in README but not the machine roster: **the canonical registry (`PROTOCOL.md:448`) disagrees with its human mirror**.
- **In conf but absent from README:** tameshi, mado, tsukuroi, tabi, souji (all exist on disk as `<id>-shokunin/`).
- **In roster + README but absent from conf:** audio, game-dev-2d, game-dev-3d — three live lanes the watchdog cannot dispatch.
- **In conf only (meta lanes):** protocol, aggregator — main-repo lanes, no roster row by design, but they do appear in `lanes` maps (24 + 28 rows); the roster-vs-ledger-key distinction should be explicit.
- `souji` exists on disk (`souji-shokunin/`), is in conf, has 11 lane-rounds closed — and appears in no registry table anywhere.

## 5. Proposed forward-only canonical entry shape (no history rewrites)

One record per lane-round-event, self-keyed — `round` never carries lane identity again:

```json
{
  "round": N,                 // REQUIRED integer — fleet round for work/closure/ops/mint;
                              // for lane-verdict types, the lane's own round (renamed below)
  "date": "YYYY-MM-DD",
  "type": "closure",          // enum += train, craft, loop, verdict
  "closed_at": "…T…+00:00",   // REQUIRED on every entry carrying a lanes map
  "lane": "<id>",             // REQUIRED on single-lane types (train/craft/loop/verdict)
  "lane_round": N,            // REQUIRED integer on single-lane types — replaces
                              // the overloaded .round
  "lanes": {"<id>": "ok|failed|not-dispatched|in-flight"},   // 'closed' must not appear;
                              // lane_rounds REQUIRED for every key, not only divergent ones
  "lane_rounds": {"<id>": N},
  "supersedes": {"round":N, "type":"…", "date":"…", "entry":I},  // entry REQUIRED
  "verdict": "admitted|rejected-honest-stop|harmed|blocked",
  "verdicts": {"<axis>": "improved|harmed|unchanged|unprovable-but-better"},
  "report": ".ufo/reports/round-<N>/<id>.md",
  "commit": "<repo>@<sha>",
  "minted": ["<id>"], "promotions": [{"id","from","to"}],
  "notes": "…"
}
```

Forward-only diffs from today's soup: (a) schema enum adds `train|craft|loop|verdict` and drops `closed` from status; (b) `lane` + `lane_round` become the canonical row key — `round` on single-lane types is deprecated-but-tolerated read-side, never written; (c) `lane_rounds` is total, not divergence-only; (d) `supersedes.entry` mandatory (the 2026-09-28 collision proved `(round,type,date)` insufficient); (e) `verdicts` values constrained to the four essence verdicts — prose moves to `notes`/`verdict_evidence`; (f) `closed_at` required whenever `lanes` exists; (g) `report`/`commit`/`evidence` first-class keys so a row is derivable without parsing notes. No existing entry is touched — all constraints apply to appends only, and the read path below covers every historical shape.

## 6. Last-round-per-lane jq (all shapes, verified against jaq 3.1.1)

Reads `lane_rounds` when present, `lane`+`round` for train/craft/loop verdict rows, `round` for lane-keyed single-lane closures — one entry per lane, latest wins on entry index then round number:

```jq
jq -r '
reduce (.rounds | to_entries[]) as $e ({};
  $e.value as $v
  | ( {} 
      + (if $v.lanes then
           ($v.lanes | keys | map({key: ., value: ($v.lane_rounds[.] // $v.round)}) | from_entries)
         else {} end)
      + (if $v.lane then {($v.lane): $v.round} else {} end)
    ) as $x
  | reduce ($x | to_entries[]) as $p (.;
      if $p.value > (.[$p.key].round // -1)
      then .[$p.key] = {round: $p.value, entry: $e.key, type: $v.type, date: $v.date}
      else . end))
| to_entries | sort_by(.key) | .[]
| "\(.key)\t\(.value.round)\tentry \(.value.entry) (\(.value.type) \(.value.date))"' MANIFEST.json
```

Output (verified): aggregator 12 · audio 65 · chousa 23 · game-dev-2d 104 · game-dev-3d 73 · kagi 19 · kaidoku 14 · kake 19 · kama 4 · kasegi 20 · kengaku 22 · kotoba 45 · kotodama 48 · kumitate 17 · lore 102 · mado 11 · mori 11 · protocol 15 · souji 11 · tabi 11 · tameshi 11 · tsukuroi 11 — **22 lanes; `revenger` absent (no ledger rows)**. Caveat: `round` is compared across namespaces (fleet rounds for protocol/aggregator era, lane rounds elsewhere) — defensible only because both order by lane counter; the shape proposal in §5 removes the ambiguity.

## 7. Cross-checks vs lane truth

- `chousa-shokunin/LOG.md` tail: "rounds 12–23 all admitted; round 24 registered" — matches ledger last=23 (craft entries 15–23) and the `closed` lr-2..11 rows.
- `mori-shokunin/LOG.md` tail: "rounds: 10 → 11" — matches lr 11 (but recorded `closed`, a non-status).
- Ledger reports `.ufo/reports/round-<N>/<lane>.md` derivability per `PROTOCOL.md:290–291` — not spot-checked against disk this pass (read-only wave; flag for a gate query `test -f` sweep).

## 8. Recommendations (ranked)

1. **Reconcile the three registries in one append:** one `ops`/`mint` entry ratifying roster rows for the 8 minted lanes past probation (or explicitly extending probation per lane), plus a README row add for mado/tabi/tameshi/tsukuroi/souji and `shokunin.conf` LANES lines for audio/game-dev-2d/game-dev-3d — the conf/roster gap means 3 rostered lanes can't be dispatched and 8 live lanes have no machine-registry row.
2. **Stop writing `closed` and stop overloading `round`** — adopt the §5 shape at the next append; schema PR upstream adds `entry` to `supersedes` and the four missing `type` values so the lagging `kimi-shokunin` schema stops false-failing conformant entries.
3. **Drain the 10 `in-flight` rows** via closure-corrections carrying `entry`-disambiguated `supersedes` (entry 24's ambiguity is the precedent to not repeat), and give `revenger` its first ledger row — a rostered lane with zero rows is indistinguishable from a dead one.
