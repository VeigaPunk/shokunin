# kaika W3 critic — kotoba round 46

Read-only non-author review of head `04192c252`. I leave admission/rejection to the canonical judge.

## C1 — depth / scope-file cwd seam

- **Counterexample and evidence:** the report's printed counting command, `PYTHONDONTWRITEBYTECODE=1 python3 -B .ufo/round-46/evidence/w2/c1/runner.py`, exits 2 with argparse usage: `runner.py` requires `--worktree`, `--comparator`, `--source`, and `--arm` (`.ufo/round-46/evidence/w2/c1/runner.py:100-108`). Thus the command as reported cannot reproduce the claim. I reran with required args (using scratch-only files):

  ```sh
  LANE=/home/vgpnk/Projects/shokunin/.tower/worktrees/kaika/kotoba-shokunin
  SCRATCH=/tmp/kaika-verify/kotoba
  mkdir -p "$SCRATCH"/c1/{frozen,candidate,control}/receipts
  PYTHONDONTWRITEBYTECODE=1 python3 -B "$LANE/.ufo/round-46/evidence/w2/c1/runner.py" --worktree "$LANE" --scratch "$SCRATCH/c1/frozen" --comparator "$SCRATCH/compare-1101213a.py" --source frozen --arm planted-relative --committed-source "$SCRATCH/compare-ccf41c23.py"
  PYTHONDONTWRITEBYTECODE=1 python3 -B "$LANE/.ufo/round-46/evidence/w2/c1/runner.py" --worktree "$LANE" --scratch "$SCRATCH/c1/candidate" --comparator "$LANE/verifiers/compare_harness_independent.py" --source worktree --arm planted-relative --committed-source "$SCRATCH/compare-ccf41c23.py"
  PYTHONDONTWRITEBYTECODE=1 python3 -B "$LANE/.ufo/round-46/evidence/w2/c1/runner.py" --worktree "$LANE" --scratch "$SCRATCH/c1/control" --comparator "$LANE/verifiers/compare_harness_independent.py" --source worktree --arm absolute-control --committed-source "$SCRATCH/compare-ccf41c23.py"
  ```

  The frozen comparator accepted the planted-relative superset (exit 0); the landed `778b367e…` comparator rejected it as `laundering` (exit 2); the absolute planted control on the landed comparator exited 0. These values are the outputs of the three commands above. The final comparator blob matches the tested bytes: `git show f2f9ee1:verifiers/compare_harness_independent.py | sha256sum` and the same command with `04192c252` both returned `778b367e…`. The replay supports the code change, although the report's no-argument counting command is defective.
- **Axis eligibility counterexample:** `MISSION.md` assigns kotoba depth + consistency; `SCORECARD.md` marks the other axes advisory, yet its round-46 saturation note explicitly records an unresolved all-axes reading under which freshness/adjacency are below depth. C1 is the lowest owned-axis move, but not the lowest axis under that broader reading. This is a policy ambiguity, not a falsification of the code fix.
- **Impacted axes:** depth claim eligibility; freshness/adjacency under the unresolved broader reading.
- **Smallest safe correction:** append the actual argument-bearing replay commands to the report/record, and settle whether “lowest non-retired” means owned axes before using C1 for that obligation. No further code change is supported by the replays.

## C2 — operability / live JSON and duplicate members

- **Counterexample and evidence:** the report's `HOME=<snapshot>` command is a placeholder, not a runnable shell command as printed. I reran the matrix from the lane root using a synthetic, stable carrier under scratch:

  ```sh
  cd /home/vgpnk/Projects/shokunin/.tower/worktrees/kaika/kotoba-shokunin
  HOME=/tmp/kaika-verify/kotoba/home R46_MATRIX_OUT=/tmp/kaika-verify/kotoba/matrix/out PYTHONDONTWRITEBYTECODE=1 python3 -B .ufo/round-46/evidence/w2/l1-matrix/r46_l1_matrix.py
  ```

  On the landed head, the honest control stayed exit 0 with 24/24 protocol and 20/24 strict agreement; `live-summary-and-mirror-optout` also stayed exit 0 on the candidate. The latter arm removes `observed`, `modes`, `verdicts`, and `summary_paths` before passing caller-supplied JSON (`r46_l1_matrix.py:183-188`); it is a false-green if arbitrary JSON files are in the threat model. Other registered shadows and the nested duplicate arm rejected in this same replay.
- **Boundary / tradeoff:** the comparator's own contract says checks establish consistency, not provenance, and bounds the claim to contradictory copies (`verifiers/compare_harness_independent.py:41-50`). Its CLI accepts caller-selected `--live-json` (`:2529-2531`) and has no producer signature. Therefore a coherent or mirror-omitting caller-authored payload is not authenticated by the new checks. This is a deliberate trust-boundary choice only if those payloads are explicitly outside the guarantee; mirror checks alone cannot establish provenance. The report correctly labels C2 `improved-bounded`, not closed.
- **Impacted axis:** operability.
- **Smallest safe correction:** preserve the bounded wording and name the untrusted-input exclusion alongside the residual arm; if arbitrary `--live-json` must be safe, require authenticated producer output or rerun the producer rather than treating consistency as provenance.

## C3 — calibration / scoped-out metadata

- **Counterexample and evidence:** held-out P5 changes only a row-level `kind` to contradict the committed scope entry, leaving reason/evidence/probe and the recomputed observation matching; it exits 0 on both comparators (`.ufo/round-46/scouts/w2-critic.md:34,44`). The code validates the committed entry's kind enum (`compare_harness_independent.py:925-934`) and compares the nested `probe.kind` with the global contract (`:1126-1130`), but never compares the row's `kind` with `committed[cid]["kind"]`. The report discloses this residual, so it is a limit on class-wide closure rather than a hidden regression.
- **Separate scope limit:** committed scope-out rows remain payload-selectable when their committed probe matches (reviewer HIGH-2, `.ufo/round-46/scouts/w2-reviewer.md:30-33`; scope contract `verifiers/harness-independent-scope.json:6`). C3's metadata checks do not prove that those rows' live values were independently checked. This is pre-existing design, not a new C3 code regression; it blocks any broader claim that the scope-out decision itself is authenticated.
- **Impacted axis:** calibration.
- **Smallest safe correction:** compare any row-level `kind`/`blocker_kind` to the committed entry and add the P5 regression arm, or explicitly narrow the claim to the reason/evidence/probe fields that are checked. Keep the payload-selectable scope-out behavior explicitly outside that narrower claim.

## Corpus and scope checks

- Reopened S002, S003, S004, S011, and the official Agent Skills spec. S002's `Lenient validation` says name mismatch is “warn, load anyway”; that directly contradicts S011's claim that a mismatched skill “will not load.” S003's Anthropic `Skill structure` field list contains “Cannot contain XML tags”; the official open spec does not make that vendor-specific rule. S011 is correctly marked community/C and rejected for the stated client-behavior and attribution errors; the sampled quotes and anchors are present. No tier inflation was found in these samples.
- `sources-census.sh validate /home/vgpnk/Projects/shokunin/.tower/worktrees/kaika/kotoba-shokunin` returned clean. That checks registry structure/enums/path existence, not quote truth; the source reopens above supply the semantic spot-check.
- **Stale premise / padding risk:** `corpus/SOURCES.md` §Search log says the contract asks for a row-count range, while `SOURCES-CONTRACT-v1.md` §Rules 4 says “There is no row quota.” This is a false stop rationale and a Goodhart pressure, not evidence that any particular row was padded. Append an erratum correcting the rationale; do not rewrite registry history.
- **Known dead recheck remains debt:** `corpus/knowledge/harness-independent-round41-census.md:3` still names the uncommitted round-45 runner. Its appended round-46 correction (`:109-115`) accurately marks it dead and says a rederived replay is needed; this is not a passing `recheck:` under Q04. Keep it explicitly blocked until a runnable recheck is derived rather than treating the annotation as repair.
- **Scope:** no sibling-province bleed found. `PROVINCE.md` §Core explicitly lists `verifiers/compare_harness_independent.py`; this work hardens that lane-owned instrument and its input contract.

I did not rerun the full gate battery or copy private session transcripts. The C2/C3 matrix replay above used only the synthetic carrier and is not a fresh reproduction against the original live-session snapshot.