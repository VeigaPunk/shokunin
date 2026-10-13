# Refresh 8 D-queue census

Measurement stamp: `date -u` → `Tue 29 Sep 2026 03:26:03 AM UTC` (initial census). Later event checks were run immediately afterward; each command is included verbatim below.

## D-key census

- **Distinct keys:** 146.
- **Maximum key:** `D-150`.
- **Next free contiguous key:** `D-151`.
- **Gaps in the numeric span:** `D-34`, `D-36`, `D-37`, `D-38` (historically closed/folded; do not reuse for this refresh).
- **Commands:**
  ```sh
  grep -oE '^\| D-[0-9]+' .ufo/reports/AGGREGATE.md | sort -u
  grep -oE '^\| D-[0-9]+' .ufo/reports/AGGREGATE.md | sort -u | wc -l
  grep -oE '^\| D-[0-9]+' .ufo/reports/AGGREGATE.md | grep -oE '[0-9]+' | sort -n -u | awk 'NR>1 && $1!=prev+1 {print "gap: "prev" -> "$1} {prev=$1} END {print "max: "$1}'
  ```
  Output: `146`; gaps `33 -> 35` and `35 -> 39`; max `150`.

### Divergent-text collision check

- **Result:** **0 true divergent-text collisions.**
- The scan found **160** D-definition rows and 14 keys repeated in later status-movement tables (`D-15`, `D-16`, `D-39`, `D-40`, `D-48`, `D-51`, `D-59`, `D-61`, `D-75`, `D-77`, `D-78`, `D-79`, `D-82`, `D-86` as observed in the row-level inspection; `D-75` has a parenthetical status form). These are status echoes, not competing queue definitions.
- The actual documented collision class is D-87: protocol attempted to reuse `D-50`…`D-58`; the ledger refused those numbers and re-keyed the nine protocol rows as `D-111`…`D-119`.
- Reproduction commands:
  ```sh
  grep -nE '^\| D-[0-9]+' .ufo/reports/AGGREGATE.md | awk -F: '{print $1}' > /tmp/dlines.txt
  wc -l /tmp/dlines.txt
  grep -nE '^\| D-(15|16|39|40|48|51|59|61|75|77|78|79|82|86)\b' .ufo/reports/AGGREGATE.md
  grep -nE '^\| D-5[0-8] ' .ufo/reports/AGGREGATE.md
  ```
  The first command returned `160`; the second shows each duplicate as a queue row plus a status echo; the third shows the nine pre-existing D-50…D-58 owners.

## Fold status

Both required folds are explicitly present and still valid in the ledger:

- **`D-39 ⊇ D-85`: FOLDED**, canonical key D-39; D-85 is the endpoint correction rider. The ledger re-runs endpoint health and stale endpoint pointers in the D-39 status row.
- **`D-51 ⊇ D-84`: FOLDED**, canonical key D-51; D-84 is the citation-gate rider. The cited gate still reproduces the same aggregator-owned lesson case.

Evidence/commands:
```sh
grep -nE 'fold|⊇|superset|subsum' .ufo/reports/AGGREGATE.md
grep -nE '^\| D-(39|51) .*⊇' .ufo/reports/AGGREGATE.md
```
This locates the canonical status rows at §13.2 and the later reaffirmation: `D-39 ⊇ D-85` and `D-51 ⊇ D-84`.

## OPEN-row disposition hints

These are hints for L1 review, not unilateral status changes.

| Row | Current/open signal | Event/status hint and exact evidence |
|---|---|---|
| D-40 | OPEN, blocked-external; kama mint-or-reject | The old L0 question remains byte-stale: `diff <(git show e333e7c:.ufo/l0-questions.md \| sed -n '2p') <(sed -n '2p' .ufo/l0-questions.md)` returned `LINE2 IDENTICAL`. However, kama was subsequently minted in probation: MANIFEST has a `type: "mint"`, `round: 11.5`, `minted: []`, with notes naming `kama-shokunin`; operator relaunch commit is `17c1fad`. Disposition hint: **substantive decision occurred, but formal L0 answer/roster accounting remains open**.
| D-77 | OPEN in original queue row | `head -40 SCORECARD.md` shows explicit protocol ownership and an `## Aggregator lane` section (line 129); `grep -nE '^#{2,4} ' SCORECARD.md` shows the separate lane section. Disposition hint: **ruling implemented; candidate for closure after L1 confirms the ownership-line wording**.
| D-82 | WATCH, mint-trigger watch | Existing three-artifact trigger was previously below bar; current mint table says it fired again. No automatic closure: **re-test trigger threshold; do not treat kama's mint as kessho's trigger**.
| D-87 | OPEN, collision row | Ledger explicitly refused protocol's reused D-50…D-58 numbers and re-keyed them D-111…D-119. Disposition hint: **key collision repaired; retain the process defect until protocol's references are confirmed migrated**.
| D-127 | OPEN, main-repo gate registry | `ls SKILL.md` returned `No such file or directory`; `PROTOCOL.md` §Gate standard says registry rows live in each lane's `SKILL.md`. Disposition hint: **still open; P-v proposes a home for the two main-repo lanes**.
| D-129 | OPEN, missing round-8 wave evidence | `git ls-files .ufo/waves/ \| awk -F/ '{print $3}' \| sort \| uniq -c` listed rounds 1 and 9–14, but no `round-8`; `ls .ufo/waves/` likewise showed no round-8 directory. Disposition hint: **still open**.
| D-133 | OPEN, kagi box-3 vs gates | `grep -nE '^- \[' kagi-shokunin/SHONEN.md` returned all four `[x]`; `claim-ledger.sh citations` completed `CITATION_GATE: CLEAN (cites=866 docs=49 unresolved=0 ephemeral=0 labeled=13)`, but `claim-ledger.sh verify` timed out (`verify_exit=124`) and `transcript-scan.sh` returned `tscan_exit=1`, `TRANSCRIPT_SCAN: HITS=2`. Disposition hint: **citation sub-gate discharged, box-3 contradiction remains**.
| D-146 | OPEN/relevant re-accumulation class | `git ls-files -o --exclude-standard .ufo/prompts \| wc -l` returned `9`, including `kama-round-2.md`; **not discharged**.

Additional kama/mint/relaunch scan:
```sh
grep -nE '^\| D-[0-9]+' .ufo/reports/AGGREGATE.md | grep -inE 'kama|mint|relaunch'
```
This identifies D-40 and D-82 in D-row text (and D-87's mint-parallel wording). The current MANIFEST check was:
```sh
python3 -c "import json; m=json.load(open('MANIFEST.json')); print('roster:',[l if isinstance(l,str) else l.get('name') for l in m.get('roster',[])]); print('rounds:',len(m.get('rounds',[]))); print('minted:',[r.get('minted') for r in m.get('rounds',[])])"
```
It showed roster of six original lanes, 48 rounds, and no nonempty `minted` list; a separate `type: mint` probation record exists at round 11.5.

## P-key proposal census

- Required count command:
  ```sh
  grep -cE 'proposal.*P-[a-z]' .ufo/reports/AGGREGATE.md
  ```
  Output: **11**.
- Enumeration command:
  ```sh
  grep -rhoE 'P-[a-z]{1,2}\b' .ufo/reports/round-1[0-8]/*.md SCORECARD.md 2>/dev/null | sort -u | tr '\\n' ' '
  ```
  Output: `P-q P-s P-v` in the later-report subset. Ledger-wide enumeration (`grep -noE 'P-[a-z]+' .ufo/reports/AGGREGATE.md`) finds the contiguous proposal series **P-a through P-v** (with repeated references).
- **Next free proposal key:** `P-w`.

## Proposed allocation

L1 assigns actual keys. Proposed contiguous block beginning at the next free key:

- **D-151:** post-mint accounting defect — kama probation mint/launch exists, but roster remains six lanes and the mint record has `minted: []` rather than a populated minted-id entry.
- **D-152:** kama lane integration hygiene — `kama-shokunin/` is absent from `.gitignore`; `git check-ignore -v kama-shokunin` returned no match, while `kumitate-shokunin/` is ignored.
- **D-153:** kagi box-3 contradiction follow-up, only if L1 elects to split it from existing D-133 after the gate re-run (otherwise leave unallocated).

No key is proposed for a merely repeated status echo or for either folded rider. Proposals remain contiguous from `D-151`; do not backfill the historical gaps.