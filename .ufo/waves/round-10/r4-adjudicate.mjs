#!/usr/bin/env node
// r4-adjudicate.mjs — aggregator lane, round 10.  Gate id: r4-adjudicate-v1.
//
// WHAT THIS IS
//   Round 9's corpus-gate.mjs grades CORPUS.md rule 4 ("A count carries its command":
//   CORPUS.md:28, "Any number in a corpus entry (rows, files, lines, packages) is written
//   as `<number> — <command> <date>`") by matching `\b\d[\d,_]*\s+<count-noun>\b` on a line
//   that carries no backticked command.  That check is a HEURISTIC and the round-9 seat
//   declared three false-positive classes for it and never implemented them
//   (.ufo/waves/round-9/corpus-gate.mjs:30 declares "a count (<n> <count-noun>) on a line
//   with no backticked command"; .ufo/waves/round-9/CONTEXT.md records "r4 264 findings").
//
//   This script adjudicates every r4 finding the gate emits into exactly ONE of five
//   classes — violation, fp-entity-designation, fp-design-arithmetic, fp-quoted-refutation,
//   undecided — so the r4 cell of a CORPUS.md rule-10 verdict is a partition
//   (violations + classified FPs + undecided = r4) and not a raw heuristic count.
//
//   It SPAWNS the frozen round-9 gate (read-only), or replays a committed gate capture, and
//   never re-implements the r4 sweep: the finding set is always the gate's.
//
// Registry block (PROTOCOL.md §Gate standard: the eight fields)
//
//   name              r4-adjudicate
//   kind              gate
//   version           r4-adjudicate-v1
//   entry command     node .ufo/waves/round-10/r4-adjudicate.mjs --live --all [--round N]
//                     node .ufo/waves/round-10/r4-adjudicate.mjs --live --repo <child-repo-dir>
//                     node .ufo/waves/round-10/r4-adjudicate.mjs --frozen <child-repo-dir> <commit>
//                     node .ufo/waves/round-10/r4-adjudicate.mjs --frozen-all
//                     node .ufo/waves/round-10/r4-adjudicate.mjs --from-json <file>
//                     node .ufo/waves/round-10/r4-adjudicate.mjs --selftest
//   verdict map       0 = clean              (no `violation` finding in any graded repo)
//                     1 = failed             (>=1 `violation` finding)
//                     2 = could-not-evaluate (missing/unparseable gate json, gate exit 2,
//                                            unreadable tree, classification dropped a finding)
//                     3 = failed             (frozen expectation drift -- the committed
//                                            per-class tallies no longer reproduce)
//                     precedence across repos / keys: 2 > 3 > 1 > 0
//   self-test         --selftest ; expected values in
//                     .ufo/waves/round-10/r4-adjudicate.expected.json (selftest.cases[])
//   pinned values     .ufo/waves/round-10/r4-adjudicate.expected.json
//                     (selftest.cases[] + frozen[] per-class tallies + capture.json_line)
//   write scope       READ-ONLY over every graded surface.  The only writes are throwaway
//                     trees inside os.tmpdir() (--selftest fixtures), removed before exit.
//                     --frozen/--frozen-all delegate snapshot extraction to the gate, which
//                     extracts into its own os.tmpdir() tree and removes it.
//   owner             aggregator lane (/home/vgpnk/projects/shokunin), round 10
//
//   home clause       PROTOCOL.md §Gate standard: "Registry. The schema is this section's; the
//                     rows live in each lane's SKILL.md", and closure "grades no gate
//                     conformant until its registry row exists in the lane's own SKILL.md".
//                     The aggregator lane is a MAIN-REPO lane: it has no SKILL.md and no child
//                     repo to put one in, so "the rows live in each lane's SKILL.md" has no
//                     satisfiable referent for this gate.  Routed as defect D-127 / proposal
//                     P-v (a main-repo registry home).  Therefore, honestly: this gate is NOT
//                     declared conformant.  It carries the eight required fields above and
//                     names the clause it cannot satisfy instead of asserting conformance.
//
// CLASSES AND DECIDING TESTS (exactly one class per finding; per-token precedence below)
//   The class-intent framing follows the round-10 revenger seat's reconstruction of rule 4 from
//   the four round-1 defects (.ufo/waves/round-10/seats/revenger-rule4-intent.md §Recommended
//   deciding tests): (a) an observed inventory/result with no nearby executable command/date,
//   (b) an entity designation, (c) planned/design arithmetic including design ranges, (d) a
//   number quoted inside a rule-9-mandated correction.
//
//   fp-quoted-refutation     CORPUS.md rule 9 REQUIRES corrections to be new entries that quote
//                            the superseded text (CORPUS.md:47 "Corrections are new entries,
//                            never rewrites"; the rule-4/rule-9 collision of ledger row
//                            D-141).  A count inside that mandated quote is not a rule-4
//                            defect.
//     t-refutation-mandated-quote  a refutation marker on the line OR in the enclosing entry
//                            (nearest preceding heading, at most 28 lines back) AND the matched
//                            count inside a quoted span or a struck (`~~…~~`) cell.
//                            markers: falsif*, correct*, fix(ed|es), errat*, retract*, supersed*,
//                            unreproducible, irreproducible, "not re-derivable"
//   fp-entity-designation    the number is part of a proper designation, not a measurement.
//     t-entity-keyword       `round|task|box|phase|step|rule|seat|slot|stage|gate|item|entry|arm|draft`
//                            immediately before the number: "round 12", "task 27", "rule 4"
//     t-entity-code          an uppercase code glued to the number: "D-141", "R11", "S8",
//                            "PQ-12", "AD-9", "CE1"
//     t-entity-designation-head  a registry/section code immediately heading the token, separator
//                            optional: "census — S8 (60 members)", "R11: 47 of 47 members"
//     t-entity-leading-zero  a leading-zero numeral is a mode/identifier, not a decimal count:
//                            "0700 dirs", "0600 files"
//     t-entity-date-component the numeral is a date/time component: "2026-09-28", "09-26",
//                            "16:15:02"
//     t-entity-quoted-id     a quoted designation the number labels: `"27 test-timeout: …"`
//   fp-design-arithmetic     the number is an operand or result of inline design arithmetic.
//     t-arith-product        <n> <noun> ×|*|x <n> … (= <n>) : "12 tasks × 2 conditions = 24 runs"
//     t-arith-equation       <n> <noun> = <n> … (also when the right-hand side wraps to the next
//                            line): "21 rows = 12 live / 3 pruned", "9 members = ×7 + …"
//     t-arith-sum            <n> <noun> + <n> … with an `=` on the line: a design sum
//                            (a bare `+` chain WITHOUT `=` is a list separator, not arithmetic:
//                             it stays a violation -- kagi:corpus/lessons/round-13.md:111)
//     t-arith-range-design   a range end on a line carrying a design/modal marker
//                            (phase|plan|floor|budget|procedure|proposal|will|design|sample|target|
//                             norm|trigger|threshold|bound|limit|cap|cadence): "8–12 runs" under
//                            "Phase 3 transfer", "36–40 runs" under "Floor"
//     t-arith-estimate-design an approximation marker (~ ≈ about roughly) plus a design/norm
//                            marker on the line: "~30 lines of python" under "Spotcheck procedure",
//                            "~600 lines is a split trigger, not a norm"
//   undecided                a count claim this classifier cannot adjudicate mechanically.
//     t-undecided-threshold  the number is governed by a comparison operator (>= <= > < ±):
//                            a predicate bound, not a count
//     t-undecided-entry-command  the enclosing entry (heading-bounded, <=28 lines back) or the
//                            enclosing paragraph (blank-line bounded, <=8 lines each way) carries
//                            a command-shaped backticked span ("wc -l …", "grep -rn … | wc -l"),
//                            so the flagged numeral may be that command's output; a line-level
//                            finding cannot tell which.  The span is quoted in the `# note`.
//     t-ambiguous-operator   the number is adjacent to a design-matrix operator whose other
//                            operand is non-numeric: "18 files × AD-1…AD-9"
//     t-line-unresolved      file:line cannot be resolved in the graded tree at the named revision
//     t-line-mismatch        the resolved line no longer carries the gate's quoted excerpt
//     t-undecided-no-token   the gate flagged the line but a re-match of its own count regex
//                            finds no token
//   violation                none of the above: a measured count with no backticked command.
//                            THIS is the class that must survive.
//     t-count-no-command     default
//     t-delta-arrow          MEASUREMENT COUNTER, not arithmetic: the number is one end of a
//                            before/after pair (`9→4`, `81→82`, `471/61`, `76 → 77`, `18→1`,
//                            `:161→:162`).  Rule for arithmetic-vs-delta: an operator counts as
//                            ARITHMETIC only when it is `×`/`*`/` x ` with a numeric partner, or
//                            `=`/`+` with numeric partners AND an `=` in the expression.  Arrows
//                            (→ -> ⇒ =>) and `/` between numbers are BEFORE/AFTER or ratio
//                            measurements and are excluded from arithmetic by construction --
//                            a delta pair is evidence that a count was measured twice, so it
//                            keeps the violation class.
//     t-range-dash           MEASUREMENT COUNTER: the number is one end of a range
//                            (`2–25 files`, `14–197 line`, `1317-1318 calls`, `~15-45 lines`)
//                            with no design/modal marker on the line.
//
// PER-TOKEN PRECEDENCE (declared, deterministic): refutation > entity > delta/range >
// arithmetic > threshold > entry-command > ambiguous-operator > default violation.  Per-line
// aggregation: a line is a `violation` if ANY matched token resolves to a violation; else
// `undecided` if any token resolves to undecided; else the false-positive class of the explained
// tokens (class order refutation > entity > arithmetic when a line mixes false-positive reasons).
// The deciding token and its test are the ones printed on the `# finding` line, and any mix is
// printed as a `# note`.
//
// RULE-4 TUPLE (P-u, ledger AGGREGATE.md:1869-1874): every surviving `violation` row carries
// `tuple=unit:<noun>,command:missing,date:<present|absent>` read off the flagged line -- the unit
// is the count noun the gate's own regex matched, the command is absent by construction (the gate
// flags only lines with no backtick), and the date is an ISO stamp on the line.  Whether the unit
// DISAMBIGUATES the population (the "entries" 82/78/recursive ambiguity) is semantic and is
// declared not-evaluated, not guessed.
//
// QUOTE DETECTION is line-local: a matched `"`/`“…”`/`~~` pair bounds a span; an UNMATCHED `"`
// is treated as opening a span that runs to end-of-line, because these corpora quote across
// lines (kasegi-shokunin:corpus/knowledge/operator-queue.md:34 opens a quote that closes on
// the next line).
//
// OUT OF SCOPE BY CONSTRUCTION (so a reader is not surprised):
//   * the adjudicator never edits a finding set.  `--round` is passed through to the gate, and
//     --live/--frozen/--from-json all classify exactly the r4 findings the gate emitted; the
//     per-repo assert `classified == gate r4` is what makes that checkable, and a mismatch is
//     exit 2 rather than a silently smaller cell.
//   * the r4 sweep itself (which lines are flagged) is NOT re-implemented and NOT re-graded:
//     a token that is not a count at all (a verb that looks like a count-noun) still arrives
//     here as a line-level finding and stays `violation`; the adjudicator narrows only by the
//     declared classes above.
//   * `--live` reads the WORKTREE (that is what the gate's live mode grades, and its revision
//     string carries `(worktree)`); a line that moved between the gate run and the resolution
//     is reported `undecided t-line-mismatch` rather than guessed.
//
// NOT EVALUATED (declared, not faked):
//   * whether the *noun* in a matched token is a noun (semantic).
//   * whether a violation's missing command is recoverable (needs the lane's history).
//   * the r8/r2/r7/r10/shonen findings: this gate adjudicates rule 4 only; it prints the gate's
//     other findings as a note count so a reader can see the verdict cell is not the whole gate.

import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { spawnSync } from 'node:child_process';
import { fileURLToPath } from 'node:url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const VERSION = 'r4-adjudicate-v1';
const MAIN_ROOT = path.resolve(__dirname, '..', '..', '..');
const GATE_PATH = path.join(MAIN_ROOT, '.ufo', 'waves', 'round-9', 'corpus-gate.mjs');
const GATE_EXPECTED_PATH = path.join(MAIN_ROOT, '.ufo', 'waves', 'round-9', 'corpus-gate.expected.json');
const EXPECTED_PATH = path.join(__dirname, 'r4-adjudicate.expected.json');

const EXIT = { CLEAN: 0, VIOLATION: 1, CNE: 2, DRIFT: 3 };
const EXIT_CLASS = { 0: 'clean', 1: 'failed', 2: 'could-not-evaluate', 3: 'failed' };
const EXIT_PRECEDENCE = [2, 3, 1, 0];

const CLASSES = ['violation', 'fp-entity-designation', 'fp-design-arithmetic', 'fp-quoted-refutation', 'undecided'];

// test name -> { class, when }  (single source of truth: a finding's class is its test's class)
const TESTS = {
  't-count-no-command': { cls: 'violation', when: 'measured count, no backticked command on the line' },
  't-delta-arrow': { cls: 'violation', when: 'before/after measurement pair (→ -> ⇒ => or / between numbers)' },
  't-range-dash': { cls: 'violation', when: 'range measurement (hyphen/en-dash/em-dash between numbers)' },
  't-entity-keyword': { cls: 'fp-entity-designation', when: 'round|task|box|phase|step|rule|seat|slot|stage|gate|item|entry|arm|draft before the numeral' },
  't-entity-code': { cls: 'fp-entity-designation', when: 'uppercase code glued to the numeral (D-141, R11, PQ-12, AD-9)' },
  't-entity-designation-head': { cls: 'fp-entity-designation', when: 'a registry/section code immediately heads the token, with or without a separator (S8 (60 members), R11: 47 members)' },
  't-entity-leading-zero': { cls: 'fp-entity-designation', when: 'leading-zero numeral (mode/identifier, not a decimal count)' },
  't-entity-date-component': { cls: 'fp-entity-designation', when: 'date/time component (2026-09-28, 09-26, 16:15:02)' },
  't-entity-quoted-id': { cls: 'fp-entity-designation', when: 'quoted designation the numeral labels ("27 test-timeout: …")' },
  't-arith-product': { cls: 'fp-design-arithmetic', when: 'numeral ×|*|x numeral (optionally = numeral)' },
  't-arith-equation': { cls: 'fp-design-arithmetic', when: 'numeral <noun> = numeral …' },
  't-arith-sum': { cls: 'fp-design-arithmetic', when: 'numeral + numeral with an = on the line' },
  't-arith-range-design': { cls: 'fp-design-arithmetic', when: 'range end (hyphen/en-dash) on a line carrying a design/modal marker (phase, floor, plan, ...)' },
  't-arith-estimate-design': { cls: 'fp-design-arithmetic', when: 'approximation marker (~, ≈, about) plus a design/norm marker on the line (procedure, norm, trigger, ...)' },
  't-undecided-threshold': { cls: 'undecided', when: 'comparison operator bounds the numeral (>= <= > < ±)' },
  't-undecided-entry-command': { cls: 'undecided', when: 'the enclosing entry or paragraph carries a command-shaped backticked span; whether it backs the flagged numeral is not decidable from the line' },
  't-ambiguous-operator': { cls: 'undecided', when: 'design-matrix operator ×|*|x with a non-numeric partner' },
  't-line-unresolved': { cls: 'undecided', when: 'file:line unresolvable in the graded tree at the named revision' },
  't-line-mismatch': { cls: 'undecided', when: 'resolved line no longer carries the gate excerpt' },
  't-undecided-no-token': { cls: 'undecided', when: 'gate flagged the line, its own count regex re-matches nothing' },
};

const REGISTRY = {
  name: 'r4-adjudicate',
  kind: 'gate',
  version: VERSION,
  owner: 'aggregator lane (/home/vgpnk/projects/shokunin), round 10',
  entry: {
    all: 'node .ufo/waves/round-10/r4-adjudicate.mjs --live --all',
    one: 'node .ufo/waves/round-10/r4-adjudicate.mjs --live --repo <child-repo-dir>',
    frozen: 'node .ufo/waves/round-10/r4-adjudicate.mjs --frozen <child-repo-dir> <commit>',
    frozen_all: 'node .ufo/waves/round-10/r4-adjudicate.mjs --frozen-all',
    from_json: 'node .ufo/waves/round-10/r4-adjudicate.mjs --from-json <file>',
    selftest: 'node .ufo/waves/round-10/r4-adjudicate.mjs --selftest',
    registry: 'node .ufo/waves/round-10/r4-adjudicate.mjs --registry',
  },
  verdict_map: {
    '0': 'clean',
    '1': 'failed',
    '2': 'could-not-evaluate',
    '3': 'failed (frozen-expectation drift)',
  },
  verdict_precedence: '2 > 3 > 1 > 0',
  selftest_flag: '--selftest',
  selftest_count: 26,
  pinned_values: 'r4-adjudicate.expected.json (selftest.cases[] + frozen[] + capture.json_line)',
  write_scope: 'read-only; writes only inside os.tmpdir() (--selftest fixtures), removed before exit',
  round_flag: '--round <N> (default 10; --frozen/--frozen-all use the gate\'s 9, the frozen captures\' selector)',
  reads: 'node .ufo/waves/round-9/corpus-gate.mjs (spawned, read-only) + .ufo/waves/round-9/corpus-gate.expected.json + the graded corpus/ trees',
  home_clause: 'UNSATISFIABLE FOR THIS LANE -- PROTOCOL.md §Gate standard puts registry rows in each lane\'s SKILL.md and grades no gate conformant until the row exists there; the aggregator lane is a main-repo lane with no SKILL.md (D-127 / proposal P-v). This gate is NOT declared conformant; the eight fields above are carried here instead.',
  classes: CLASSES.map((c) => ({ class: c, tests: Object.keys(TESTS).filter((t) => TESTS[t].cls === c) })),
  not_evaluated: [
    { item: 'r4 lines the gate did not flag', reason: 'the adjudicator partitions the gate\'s finding set; it never re-sweeps (a re-sweep would make the cell uncomparable to the gate it cites)' },
    { item: 'noun-ness of a matched token', reason: 'semantic; a verb that looks like a count-noun stays a violation rather than being excused by an undeclared class' },
    { item: 'recoverability of a missing command', reason: 'needs the lane history, which does not live in the graded tree' },
    { item: 'r2/r7/r8/r10/shonen findings', reason: 'this gate adjudicates CORPUS.md rule 4 only; the other rules are counted in a note' },
  ],
};

// The gate's own count regex, copied verbatim from .ufo/waves/round-9/corpus-gate.mjs
// (COUNT_NOUN_RE).  Copied, not imported: the gate is frozen evidence and must not be edited,
// and a re-export would couple the two files' loads.
const COUNT_NOUN_RE = /\b\d[\d,_]*\s+(rows?|files?|lines?|packages?|entries|dirs?|directories|commits?|sessions?|seats?|checks?|ids?|calls?|runs?|draws?|hits?|boxes|members?|scripts?|tests?|cases?|notes?|citations?|sites?|repos?|lanes?|words?|paths?|probes?|columns?|fields?|stamps?|pins?)\b/g;

// ---- detection regexes (one per named test; each is declared in the registry block above)
const REFUTATION_RE = /\b(?:falsif\w*|falsely|correct\w*|fix(?:ed|es)?|errat\w*|retract\w*|supersed\w*|unreproducible|irreproducible|not re-derivable)\b/i;
const DESIG_KEYWORD_RE = /(?:^|[^\w])(?:rounds?|tasks?|boxes|box|phases?|steps?|rules?|seats?|slots?|stages?|gates?|items?|entry|entries|arms?|drafts?)[-#]?\s*#?\s*$/;
const DESIG_CODE_RE = /(?:^|[^\w])[A-Z]{1,3}[-#]?\s*$/;
// A registry/section code immediately heading the token, separator optional:
//   "census — S8 (60 members)"  "R11: 47 of 47 members"  "AD-9 file-path clause"
const DESIG_HEAD_RE = /(?:^|[^\w])[A-Z][A-Z0-9]{0,3}\s*(?:[-:—–]\s*)?\(?\s*$/;
// Design/modal markers (revenger-rule4-intent.md §Recommended deciding tests, class (c)):
// a planned equation/range/budget/estimate is design text, not an observed census.
const DESIGN_MARKER_RE = /\b(?:phases?|plans?|planned|planning|floor|budget|procedure|proposals?|proposed|design|sample|targets?|norms?|triggers?|thresholds?|bounds?|limits?|caps?|cadence|will)\b/i;
const ESTIMATE_RE = /(?:~|≈|\babout\s|\broughly\s|\border of\b)/;
const CMD_SPAN_RE = /`([^`\n]+)`/g;
const CMD_WORD_RE = /^\s*\$?\s*(?:wc|ls|find|grep|rg|git|cat|jq|sed|awk|du|sort|uniq|sqlite3|node|python3?|bash|sh|npm|bun|printf|echo|tar|xargs)\b/;
const LEAD_ZERO_RE = /^0\d+$/;
const DATETIME_PREFIX_RE = /(?:^|[^\d])(?:(?:19|20)\d{2}[-/](?:0[1-9]|1[0-2])-|(?:0[1-9]|1[0-2])-|\d{2}:\d{2}:|\d{2}T\d{2}:)$/;
const DELTA_BEFORE_RE = /\d[\d,._]*:?\s*(?:→|->|⇒|=>|\/)\s*:?\s*$/;
const DELTA_AFTER_RE = /^\s*(?:→|->|⇒|=>)\s*\d/;
const RANGE_BEFORE_RE = /(?:^|[^\d])\d[\d,._]*\s*[-–—]\s*$/;
const THRESHOLD_BEFORE_RE = /(?:≥|≤|>=|<=|>|<|±)\s*$/;
const PRODUCT_TAIL_RE = /^\s*(?:×|\*|x)\s+\d/;
const PRODUCT_HEAD_RE = /\d[\d,._]*\s+(?:×|\*|x)\s+$/;
const EQ_TAIL_RE = /^\s*=\s*\d/;
const EQ_HEAD_RE = /\d[^=]{0,24}=\s*$/;
const SUM_TAIL_RE = /^\s*\+\s*\d/;
const MATRIX_OP_TAIL_RE = /^\s*(?:×|\*)\s+(?!\d)/;
const QUOTED_OPEN_RE = /(?:^|[^\w])(?:["“])$/;

// ---------------------------------------------------------------- helpers

function git(dir, args) {
  const r = spawnSync('git', ['-C', dir].concat(args), { encoding: 'utf8', maxBuffer: 1 << 30 });
  return { code: r.status === null ? 127 : r.status, out: r.stdout || '', err: r.stderr || '' };
}

function readText(p) {
  try {
    return fs.readFileSync(p, 'utf8');
  } catch (e) {
    return null;
  }
}

function collapse(s) {
  return s.trim().replace(/\s+/g, ' ');
}

/** The gate's excerpt(): first 60 collapsed chars.  Kept identical so the staleness check
 *  compares like with like. */
function gateExcerpt(s) {
  return s.trim().replace(/\s+/g, ' ').slice(0, 60);
}

function quoteField(s) {
  return '"' + String(s).replace(/\\/g, '\\\\').replace(/"/g, '\\"') + '"';
}

function tokenField(s) {
  return /\s/.test(s) ? quoteField(s) : s;
}

function sortedKeys(obj) {
  if (Array.isArray(obj)) return obj.map(sortedKeys);
  if (obj && typeof obj === 'object') {
    const out = {};
    for (const k of Object.keys(obj).sort()) out[k] = sortedKeys(obj[k]);
    return out;
  }
  return obj;
}

function combinedExit(codes) {
  for (const c of EXIT_PRECEDENCE) if (codes.indexOf(c) !== -1) return c;
  return EXIT.CLEAN;
}

// ---------------------------------------------------------------- source resolution

/** The graded bytes for one gate-json entry.
 *  live      -> the worktree file (that is what the gate's live mode graded)
 *  snapshot  -> `git show <commit>:corpus/<rel>` (the gate graded a `git archive` of <commit>)
 *  A per-file failure is a per-finding `undecided t-line-unresolved`; a tree-level failure
 *  (absent directory, bad revision) is repo-level could-not-evaluate. */
function makeSource(entry, dirOverride) {
  const dir = dirOverride || path.join(MAIN_ROOT, entry.repo);
  const worktree = /\(worktree\)\s*$/.test(entry.revision || '');
  const tree = String(entry.revision || '').replace(/\s*\(worktree\)\s*$/, '');
  const mode = entry.mode === 'snapshot' ? 'snapshot' : 'live';
  const out = { dir, tree, worktree, mode, ok: true, reason: null };
  if (!fs.existsSync(dir)) {
    out.ok = false; out.reason = `repo directory ${dir} absent`;
    return out;
  }
  if (mode === 'snapshot') {
    const r = git(dir, ['rev-parse', '--verify', tree + '^{commit}']);
    if (r.code !== 0) { out.ok = false; out.reason = `git rev-parse ${tree} failed: ${r.err.trim()}`; }
  } else if (!fs.existsSync(path.join(dir, 'corpus'))) {
    out.ok = false; out.reason = `corpus/ absent under ${dir}`;
  }
  out.read = (rel) => {
    if (mode === 'snapshot') {
      const r = git(dir, ['show', tree + ':corpus/' + rel]);
      return r.code === 0 ? r.out : null;
    }
    return readText(path.join(dir, 'corpus', rel));
  };
  return out;
}

// ---------------------------------------------------------------- classifier

function quoteSpans(line) {
  const spans = [];
  for (const pair of [['"', '"'], ['“', '”'], ['~~', '~~']]) {
    let i = 0;
    for (;;) {
      const a = line.indexOf(pair[0], i);
      if (a < 0) break;
      const b = line.indexOf(pair[1], a + pair[0].length);
      if (b < 0) { spans.push([a, line.length + 1]); break; }
      spans.push([a, b + pair[1].length]);
      i = b + pair[1].length;
    }
  }
  return spans;
}

function insideQuote(line, start, end) {
  return quoteSpans(line).some(([a, b]) => a <= start && end <= b);
}

/** The enclosing entry: the nearest preceding ATX heading, at most `back` lines up.
 *  Returns { text, start } with start = 1-based line number of the heading (or 1). */
function entryText(read, rel, ln, back) {
  const raw = read(rel);
  if (raw === null) return { text: '', start: ln };
  const lines = raw.split(/\r?\n/);
  let lo = Math.max(0, ln - 1 - back);
  for (let i = ln - 1; i >= lo; i--) {
    if (/^#{1,6}\s/.test(lines[i])) { lo = i; break; }
  }
  return { text: lines.slice(lo, ln).join('\n'), start: lo + 1 };
}

/** The enclosing paragraph: blank-line bounded, at most `cap` lines each way. */
function paragraphText(read, rel, ln, cap) {
  const raw = read(rel);
  if (raw === null) return { text: '', start: ln };
  const lines = raw.split(/\r?\n/);
  let lo = ln - 1;
  while (lo > 0 && lines[lo - 1].trim() !== '' && ln - 1 - lo < cap) lo--;
  let hi = ln;
  while (hi < lines.length && lines[hi].trim() !== '' && hi - (ln - 1) < cap) hi++;
  return { text: lines.slice(lo, hi).join('\n'), start: lo + 1 };
}

/** A command-shaped backticked span: a shell word (optionally after `$ `) with arguments, or a
 *  pipeline.  A bare path or a prose backtick is NOT a command (`knowledge/foo.md`,
 *  `SCORECARD.md:108`).  Used by t-undecided-entry-command only. */
function commandSpan(text) {
  if (!text) return null;
  for (const m of text.matchAll(/`([^`\n]+)`/g)) {
    const s = m[1];
    if (/\s\|\s/.test(s)) return s;
    if (CMD_WORD_RE.test(s) && /\s/.test(s.trim())) return s;
  }
  return null;
}

function classifyToken(line, m, ctx) {
  const tok = m[0];
  const ns = m.index;
  const ne = ns + tok.length;
  const num = (tok.match(/^\d[\d,_]*/) || [tok])[0];
  const head = line.slice(Math.max(0, ns - 26), ns);
  const before = line.slice(Math.max(0, ns - 20), ns);
  const tail = line.slice(ne, ne + 26);
  const after = line.slice(ns + num.length, ns + num.length + 20);
  const quoted = insideQuote(line, ns, ne);
  const design = DESIGN_MARKER_RE.test(line);

  // precedence 1 — rule 9 MANDATES the quoted correction (D-141)
  if (quoted && (ctx.lineMarker || ctx.entryMarker)) return { test: 't-refutation-mandated-quote', token: tok };
  // precedence 2 — entity designation (a numeral that labels an object, not a population)
  if (LEAD_ZERO_RE.test(num)) return { test: 't-entity-leading-zero', token: tok };
  if (num.length <= 4 && DATETIME_PREFIX_RE.test(head)) return { test: 't-entity-date-component', token: tok };
  if (DESIG_KEYWORD_RE.test(before)) return { test: 't-entity-keyword', token: tok };
  if (DESIG_HEAD_RE.test(head)) return { test: 't-entity-designation-head', token: tok };
  if (DESIG_CODE_RE.test(before)) return { test: 't-entity-code', token: tok };
  if (quoted && QUOTED_OPEN_RE.test(head) && tail.startsWith('-')) return { test: 't-entity-quoted-id', token: tok };
  // precedence 3 — measurement counters: a delta keeps the violation class (it is an
  // observation taken twice, not design arithmetic); a design-marked range is design text.
  if (DELTA_BEFORE_RE.test(before) || DELTA_AFTER_RE.test(after)) return { test: 't-delta-arrow', token: tok };
  if (RANGE_BEFORE_RE.test(head)) {
    if (design) return { test: 't-arith-range-design', token: tok };
    return { test: 't-range-dash', token: tok };
  }
  // precedence 4 — inline design arithmetic
  if (PRODUCT_TAIL_RE.test(tail) || PRODUCT_HEAD_RE.test(head)) return { test: 't-arith-product', token: tok };
  if (EQ_TAIL_RE.test(tail) || EQ_HEAD_RE.test(head)) return { test: 't-arith-equation', token: tok };
  // an identity whose right-hand side wraps to the next line ("… 9 members =" / "`probe-*.mjs` ×7 + …")
  if (/^\s*=\s*[*_\s]*$/.test(tail) && ctx.nextLine && /(?:[×*+]\s*`?\d)|(?:\d[\d,._]*\s*[×*+])/.test(ctx.nextLine)) {
    return { test: 't-arith-equation', token: tok };
  }
  if (SUM_TAIL_RE.test(tail) && line.slice(Math.max(0, ns - 40), ne + 40).includes('=')) return { test: 't-arith-sum', token: tok };
  if (ESTIMATE_RE.test(line) && design) return { test: 't-arith-estimate-design', token: tok };
  // precedence 5 — undecided
  if (THRESHOLD_BEFORE_RE.test(before)) return { test: 't-undecided-threshold', token: tok };
  if (ctx.commandSpan) return { test: 't-undecided-entry-command', token: tok };
  if (MATRIX_OP_TAIL_RE.test(tail)) return { test: 't-ambiguous-operator', token: tok };
  return { test: 't-count-no-command', token: tok };
}

/** One r4 finding -> exactly one class.  Returns { cls, test, token, note, excerpt, line }. */
function adjudicateFinding(src, rel, ln, finding) {
  const raw = src.read(rel);
  if (raw === null) {
    return { cls: 'undecided', test: 't-line-unresolved', token: '-', excerpt: finding.excerpt,
      note: `file corpus/${rel} unreadable in ${src.mode} mode at ${src.tree}` };
  }
  const lines = raw.split(/\r?\n/);
  if (ln - 1 >= lines.length) {
    return { cls: 'undecided', test: 't-line-unresolved', token: '-', excerpt: finding.excerpt,
      note: `corpus/${rel} has ${lines.length} lines; the gate cited line ${ln}` };
  }
  const line = lines[ln - 1];
  if (finding.excerpt && collapse(line).slice(0, finding.excerpt.length) !== finding.excerpt) {
    return { cls: 'undecided', test: 't-line-mismatch', token: '-', excerpt: gateExcerpt(line),
      note: `line ${ln} has moved since the gate ran: gate excerpt ${quoteField(finding.excerpt)} != current ${quoteField(gateExcerpt(line))}` };
  }
  const lineMarker = REFUTATION_RE.test(line);
  const entry = entryText(src.read, rel, ln, 28);
  const para = paragraphText(src.read, rel, ln, 8);
  const entryMarker = !lineMarker && REFUTATION_RE.test(entry.text);
  const entryCmd = commandSpan(entry.text);
  const paraCmd = entryCmd ? null : commandSpan(para.text);
  const rest = lines.slice(ln);
  const nextIdx = rest.findIndex((l) => l.trim() !== '');
  const ctx = {
    lineMarker,
    entryMarker,
    commandSpan: entryCmd || paraCmd,
    commandWhere: entryCmd ? `entry@${entry.start}` : (paraCmd ? `paragraph@${para.start}` : null),
    nextLine: nextIdx >= 0 ? rest[nextIdx] : null,
  };
  COUNT_NOUN_RE.lastIndex = 0;
  const toks = [];
  let m;
  while ((m = COUNT_NOUN_RE.exec(line)) !== null) {
    if (m[0] === '') break;
    const r = classifyToken(line, m, ctx);
    toks.push({ test: r.test, token: r.token, cls: TESTS[r.test].cls });
  }
  if (toks.length === 0) {
    return { cls: 'undecided', test: 't-undecided-no-token', token: '-', excerpt: gateExcerpt(line),
      note: 'the gate flagged this line but a re-match of its own count regex finds no token' };
  }
  const U = toks.filter((t) => t.cls === 'violation');
  const A = toks.filter((t) => t.cls === 'undecided');
  const E = toks.filter((t) => t.cls.startsWith('fp-'));
  let pick;
  if (U.length) pick = U[0];
  else if (A.length) pick = A[0];
  else {
    const order = CLASSES.filter((c) => c.startsWith('fp-'));
    const cls = order.filter((c) => E.some((t) => t.cls === c))[0] || E[0].cls;
    pick = E.filter((t) => t.cls === cls)[0];
  }
  const parts = [];
  if (toks.length > 1) parts.push(`line carries ${toks.length} matched tokens: [${toks.map((t) => tokenField(t.token) + '=' + t.cls + '/' + t.test).join(', ')}]`);
  if (pick.test === 't-undecided-entry-command') parts.push(`enclosing ${ctx.commandWhere} carries a command-shaped span ${tokenField(ctx.commandSpan)}; whether it backs this numeral is not decidable from the flagged line`);
  return { cls: pick.cls, test: pick.test, token: pick.token, excerpt: gateExcerpt(line),
    tuple: pick.cls === 'violation' ? tupleNote(line, pick.token) : null,
    note: parts.length ? parts.join(' | ') : null, line };
}

/** The rule-4 tuple `<number> — <unit> — <command> <date>` as far as it can be read off the
 *  flagged line: the unit is the count noun the gate's own regex matched (`unit:absent` when it
 *  matched no noun), the command is absent by construction (the gate flags only lines with no
 *  backtick), and the date is present iff the line carries an ISO stamp.  Whether the unit
 *  DISAMBIGUATES the population is not evaluated (registry not_evaluated). */
function tupleNote(line, token) {
  const unit = (token.match(/\s+([A-Za-z]+)$/) || [])[1];
  const date = /\b(?:19|20)\d{2}-\d{2}-\d{2}\b|\b\d{2}:\d{2}(?::\d{2})?\s*Z\b/.test(line);
  return `unit:${unit ? unit.toLowerCase() : 'absent'},command:missing,date:${date ? 'present' : 'absent'}`;
}

// ---------------------------------------------------------------- gate json plumbing

function parseGateJson(text) {
  const line = String(text).split(/\r?\n/).find((l) => l.startsWith('# json '));
  if (!line) return null;
  try {
    return JSON.parse(line.slice('# json '.length));
  } catch (e) {
    return null;
  }
}

function findParse(text) {
  const m = /^(\S+):(\d+) count claim with no backticked command: "(.*)" \(CORPUS\.md:28\)$/.exec(text);
  if (!m) return null;
  return { file: m[1], line: parseInt(m[2], 10), excerpt: m[3] };
}

function spawnGate(args) {
  const r = spawnSync(process.execPath, [GATE_PATH].concat(args), { encoding: 'utf8', maxBuffer: 1 << 30 });
  return { code: r.status === null ? 127 : r.status, out: r.stdout || '', err: r.stderr || '' };
}

/** Classify every r4 finding of one gate-json entry.  `dirOverride` pins the tree (selftest,
 *  or --repo with --from-json). */
function adjudicateEntry(entry, dirOverride) {
  const out = {
    repo: entry.repo,
    revision: entry.revision,
    tree: String(entry.revision || '').replace(/\s*\(worktree\)\s*$/, ''),
    worktree: /\(worktree\)\s*$/.test(entry.revision || ''),
    dirty: entry.dirty,
    mode: entry.mode,
    gateExit: entry.exit,
    gateR4: 0,
    classified: 0,
    counts: {},
    findings: [],
    notes: [],
    exit: EXIT.CLEAN,
    ourFindings: [],
  };
  for (const c of CLASSES) out.counts[c] = 0;
  const src = makeSource(entry, dirOverride);
  if (!src.ok) {
    out.exit = EXIT.CNE;
    out.notes.push(`could-not-evaluate: ${src.reason}`);
    return out;
  }
  if (entry.exit === EXIT.CNE) {
    out.exit = EXIT.CNE;
    out.notes.push('could-not-evaluate: the gate returned exit 2 for this repo (no corpus/, unreadable corpus, or git failure)');
    return out;
  }
  const all = Array.isArray(entry.findings) ? entry.findings : [];
  const r4 = all.filter((f) => f.rule === 'r4');
  out.gateR4 = r4.length;
  const gateStatsR4 = entry.stats && entry.stats.rules ? entry.stats.rules.r4 : null;
  if (gateStatsR4 !== null && gateStatsR4 !== undefined && gateStatsR4 !== out.gateR4) {
    out.exit = EXIT.CNE;
    out.notes.push(`could-not-evaluate: gate stats.rules.r4=${gateStatsR4} but the finding list carries ${out.gateR4} r4 id(s) — the json is internally inconsistent`);
    return out;
  }
  const otherRules = {};
  for (const f of all) if (f.rule !== 'r4') otherRules[f.rule] = (otherRules[f.rule] || 0) + 1;
  out.otherRules = otherRules;

  for (const f of r4) {
    const parsed = findParse(f.text || '');
    if (!parsed) {
      out.findings.push({ id: f.id, cls: 'undecided', test: 't-line-unresolved', file: null, line: null, token: '-', excerpt: '', note: 'the gate finding text is not in the r4 shape' });
      out.counts.undecided++;
      continue;
    }
    const r = adjudicateFinding(src, parsed.file, parsed.line, parsed);
    if (!TESTS[r.test] || TESTS[r.test].cls !== r.cls) {
      out.exit = EXIT.CNE;
      out.notes.push(`could-not-evaluate: internal class/test inconsistency for ${f.id} (${r.test}/${r.cls})`);
      return out;
    }
    out.findings.push({
      id: f.id, cls: r.cls, test: r.test, file: parsed.file, line: parsed.line,
      token: collapse(r.token), excerpt: r.excerpt, tuple: r.tuple || null, note: r.note,
    });
    out.counts[r.cls]++;
  }
  out.classified = out.findings.length;
  if (out.classified !== out.gateR4) {
    out.exit = EXIT.CNE;
    out.notes.push(`could-not-evaluate: classification dropped findings — classified=${out.classified} gate-r4=${out.gateR4}`);
    return out;
  }
  const sum = CLASSES.reduce((a, c) => a + out.counts[c], 0);
  if (sum !== out.classified) {
    out.exit = EXIT.CNE;
    out.notes.push(`could-not-evaluate: class partition sums to ${sum}, classified=${out.classified}`);
    return out;
  }
  out.exit = out.counts.violation > 0 ? EXIT.VIOLATION : EXIT.CLEAN;
  return out;
}

// ---------------------------------------------------------------- output

function entryLines(e) {
  const out = [];
  const ident = `rev=${e.tree} dirty=${e.dirty} mode=${e.mode}${e.worktree ? ' worktree=1' : ''}`;
  out.push(`# adjudicated ${e.repo} rev=${e.tree} dirty=${e.dirty} mode=${e.mode}${e.worktree ? ' worktree=1' : ''} r4=${e.gateR4} violation=${e.counts.violation} fp-entity=${e.counts['fp-entity-designation']} fp-arith=${e.counts['fp-design-arithmetic']} fp-refutation=${e.counts['fp-quoted-refutation']} undecided=${e.counts.undecided}`);
  for (const c of CLASSES) out.push(`# class ${e.repo} ${c} ${e.counts[c]} ${ident}`);
  for (const f of e.findings) {
    const loc = f.file === null ? 'unresolved' : `${e.repo}:corpus/${f.file}:${f.line}`;
    out.push(`# finding ${f.id} ${f.cls} ${f.test} ${loc} ${tokenField(f.token)} ${quoteField(f.excerpt)} ${ident}${f.tuple ? ' tuple=' + f.tuple : ''}`);
  }
  for (const f of e.findings) if (f.note) out.push(`# note ${e.repo} ${f.id} ${f.note}`);
  if (!e.worktree) out.push(`# source ${e.repo} bytes read from git show ${e.tree}:corpus/** (the gate graded a git archive of this commit)`);
  for (const n of e.notes) out.push(`# note ${e.repo} ${n}`);
  out.push(`# assert ${e.repo} classified=${e.classified} gate-r4=${e.gateR4} ${e.classified === e.gateR4 ? 'MATCH' : 'MISMATCH'}`);
  if (e.otherRules && Object.keys(e.otherRules).length) {
    out.push(`# note ${e.repo} gate findings outside r4 (not adjudicated here): ${Object.keys(e.otherRules).sort().map((r) => r + '=' + e.otherRules[r]).join(' ')}`);
  }
  return out;
}

function printRegistry() {
  const r = REGISTRY;
  const out = [];
  out.push(`# registry name=${r.name} kind=${r.kind} version=${r.version}`);
  out.push(`# registry owner ${r.owner}`);
  out.push(`# registry entry-all "${r.entry.all}"`);
  out.push(`# registry entry-one "${r.entry.one}"`);
  out.push(`# registry entry-frozen "${r.entry.frozen}"`);
  out.push(`# registry entry-frozen-all "${r.entry.frozen_all}"`);
  out.push(`# registry entry-from-json "${r.entry.from_json}"`);
  out.push(`# registry verdict-map ${Object.keys(r.verdict_map).map((k) => k + '=' + r.verdict_map[k]).join(' ')}`);
  out.push(`# registry verdict-precedence ${r.verdict_precedence}`);
  out.push(`# registry selftest-command "${r.entry.selftest}" spelling=--selftest cases=${r.selftest_count}`);
  out.push(`# registry pinned-values ${r.pinned_values}`);
  out.push(`# registry write-scope ${r.write_scope}`);
  out.push(`# registry round-selector ${r.round_flag}`);
  out.push(`# registry reads ${r.reads}`);
  out.push(`# registry home-clause ${r.home_clause}`);
  for (const c of r.classes) out.push(`# registry class ${c.class} tests=${c.tests.join(',')}`);
  for (const t of Object.keys(TESTS)) out.push(`# registry test ${t} class=${TESTS[t].cls} ${TESTS[t].when}`);
  for (const n of r.not_evaluated) out.push(`# registry not-evaluated item="${n.item}" reason=${n.reason}`);
  if (process.env.R4_ADJUDICATE_REGISTRY_JSON === '1') out.push('# registry json ' + JSON.stringify(sortedKeys(REGISTRY)));
  return out;
}

// ---------------------------------------------------------------- modes

function readExpected() {
  const t = readText(EXPECTED_PATH);
  if (t === null) return null;
  try {
    return JSON.parse(t);
  } catch (e) {
    return null;
  }
}

function runCaptureLines(captures, label) {
  // captures: [{ text, source }]
  const entries = [];
  const problems = [];
  for (const cap of captures) {
    const json = parseGateJson(cap.text);
    if (json === null) { problems.push(`# cne ${label} could-not-evaluate: no parseable "# json" line in ${cap.source}`); continue; }
    for (const e of json) entries.push({ entry: e, dir: cap.dir });
  }
  return { entries, problems };
}

function emitEntries(entries, o, extra) {
  const lines = [];
  const results = [];
  for (const { entry, dir } of entries) {
    const e = adjudicateEntry(entry, dir);
    results.push(e);
    lines.push(...entryLines(e));
  }
  for (const p of extra) lines.push(p);
  return { lines, results };
}

// ---------------------------------------------------------------- selftest

const FX_ALPHA_HEAD = '# alpha\n\nThe alpha surface resolves through `cmd alpha --probe`.\n';

function fixtureFiles(name) {
  // A fixture is a throwaway corpus tree under os.tmpdir(); the label is the case name, so the
  // synthesized finding ids are CR-<case>-r4-<n> exactly like the gate's.
  return { 'corpus/knowledge/alpha.md': FX_ALPHA_HEAD, 'corpus/README.md': `# ${name} fixture corpus\n\n| Entry | Covers |\n|---|---|\n| \`knowledge/alpha.md\` | alpha |\n` };
}

const SELFTEST_CASES = [
  { name: 'fx-clean', lines: [], expect_file: 'corpus/knowledge/alpha.md', expect_line: 1, findings: [] },
  { name: 'fx-violation-plain', findings: [{ file: 'corpus/knowledge/beta.md', line: 3 }],
    files: { 'corpus/knowledge/beta.md': '# beta\n\nThe census found 42 rows in the index.\n' } },
  { name: 'fx-delta-arrow', findings: [{ file: 'corpus/knowledge/beta.md', line: 3 }],
    files: { 'corpus/knowledge/beta.md': '# beta\n\nThe pin set went 33 → 44 rows this round.\n' } },
  { name: 'fx-range-dash', findings: [{ file: 'corpus/knowledge/beta.md', line: 3 }],
    files: { 'corpus/knowledge/beta.md': '# beta\n\nThe sweep covered 14–197 lines of prose.\n' } },
  { name: 'fx-entity-keyword', findings: [{ file: 'corpus/knowledge/beta.md', line: 3 }],
    files: { 'corpus/knowledge/beta.md': '# beta\n\nThe round-9 probes ran before the fix landed.\n' } },
  { name: 'fx-entity-code', findings: [{ file: 'corpus/knowledge/beta.md', line: 3 }],
    files: { 'corpus/knowledge/beta.md': '# beta\n\nThe PQ-12 pin persist row was added this round.\n' } },
  { name: 'fx-entity-leading-zero', findings: [{ file: 'corpus/knowledge/beta.md', line: 3 }],
    files: { 'corpus/knowledge/beta.md': '# beta\n\nThe transcript is 0700 dirs + 0600 files, same-user boundary.\n' } },
  { name: 'fx-entity-designation-head', findings: [{ file: 'corpus/knowledge/beta.md', line: 1 }],
    files: { 'corpus/knowledge/beta.md': '# Remaining scripts census — S8 (60 members)\n' } },
  { name: 'fx-entity-date', findings: [{ file: 'corpus/knowledge/beta.md', line: 3 }],
    files: { 'corpus/knowledge/beta.md': '# beta\n\nAll read 2026-09-28, line pins re-verified after the draft.\n' } },
  { name: 'fx-entity-quoted-id', findings: [{ file: 'corpus/knowledge/beta.md', line: 3 }],
    files: { 'corpus/knowledge/beta.md': '# beta\n\nIt closes corpus gap "27 test-timeout: the harness races".\n' } },
  { name: 'fx-arith-product', findings: [{ file: 'corpus/knowledge/beta.md', line: 3 }],
    files: { 'corpus/knowledge/beta.md': '# beta\n\nPhase 2 core: 12 tasks × 2 conditions = 24 runs.\n' } },
  { name: 'fx-arith-equation', findings: [{ file: 'corpus/knowledge/beta.md', line: 3 }],
    files: { 'corpus/knowledge/beta.md': '# beta\n\nRegistry census: 21 rows = 12 live / 3 pruned / 3 broken.\n' } },
  { name: 'fx-arith-sum', findings: [{ file: 'corpus/knowledge/beta.md', line: 3 }],
    files: { 'corpus/knowledge/beta.md': '# beta\n\nThe split is 12 rows + 9 rows = 21 rows over two files.\n' } },
  { name: 'fx-arith-range-design', findings: [{ file: 'corpus/knowledge/beta.md', line: 3 }],
    files: { 'corpus/knowledge/beta.md': '# beta\n\n- **Phase 3 transfer**: 8–12 runs public slices only.\n' } },
  { name: 'fx-arith-estimate-design', findings: [{ file: 'corpus/knowledge/beta.md', line: 1 }],
    files: { 'corpus/knowledge/beta.md': '# Spotcheck procedure (no new tooling needed; ~30 lines of python)\n' } },
  { name: 'fx-arith-equation-wrapped', findings: [{ file: 'corpus/knowledge/beta.md', line: 3 }],
    files: { 'corpus/knowledge/beta.md': '# beta\n\n- The cluster boundary is a rule. 9 members =\n  `probe-*.mjs` ×7 + `atomic-write.mjs` + `fake-omp.mjs`.\n' } },
  { name: 'fx-refutation-line', findings: [{ file: 'corpus/knowledge/beta.md', line: 3 }],
    files: { 'corpus/knowledge/beta.md': '# beta\n\nRound-13 correction: earlier text said "9 of 12 rows carry the flag".\n' } },
  { name: 'fx-refutation-entry', findings: [{ file: 'corpus/knowledge/beta.md', line: 5 }],
    files: { 'corpus/knowledge/beta.md': '# beta\n\n## Corrections to the round-6 note\n\nThe "20 rows" figure was wrong; the registry holds more.\n' } },
  { name: 'fx-refutation-beats-delta', findings: [{ file: 'corpus/knowledge/beta.md', line: 3 }],
    files: { 'corpus/knowledge/beta.md': '# beta\n\nCorrected: the tally "9→4 files" was wrong.\n' } },
  { name: 'fx-undecided-threshold', findings: [{ file: 'corpus/knowledge/beta.md', line: 3 }],
    files: { 'corpus/knowledge/beta.md': '# beta\n\nA member counts only with ≥1 line anchor in its own file.\n' } },
  { name: 'fx-undecided-ambiguous', findings: [{ file: 'corpus/knowledge/beta.md', line: 3 }],
    files: { 'corpus/knowledge/beta.md': '# beta\n\n## Verdict matrix (18 files × AD-1…AD-9)\n' } },
  { name: 'fx-undecided-entry-command', findings: [{ file: 'corpus/knowledge/beta.md', line: 7 }],
    files: { 'corpus/knowledge/beta.md': '# beta\n\n## Census\n\nSource: `wc -l config/registry.jsonl`\n\nThe census found 42 rows in the index.\n' } },
  { name: 'fx-mixed-entity-count', findings: [{ file: 'corpus/knowledge/beta.md', line: 3 }],
    files: { 'corpus/knowledge/beta.md': '# beta\n\nRound-12 citation audit (independent reviewer: 74 citations checked).\n' } },
  { name: 'fx-line-unresolved', findings: [{ file: 'corpus/knowledge/alpha.md', line: 99, excerpt: 'the alpha surface resolves' }] },
  { name: 'fx-line-mismatch', findings: [{ file: 'corpus/knowledge/alpha.md', line: 3, excerpt: 'a line that the gate saw and that no longer exists' }] },
  { name: 'fx-multi-finding', findings: [
    { file: 'corpus/knowledge/beta.md', line: 3 },
    { file: 'corpus/knowledge/gamma.md', line: 3 },
  ],
    files: {
      'corpus/knowledge/beta.md': '# beta\n\nThe census found 42 rows in the index.\n',
      'corpus/knowledge/gamma.md': '# gamma\n\nThe round-9 probes ran before the fix landed.\n',
    } },
];

function buildFixture(root, files) {
  for (const rel of Object.keys(files)) {
    const p = path.join(root, rel);
    fs.mkdirSync(path.dirname(p), { recursive: true });
    fs.writeFileSync(p, files[rel]);
  }
}

/** Synthesize the gate's `# json` line for one fixture case.  The finding TEXT is built in the
 *  gate's exact shape, and every injected finding whose line resolves is validated against the
 *  fixture bytes (the line must exist, carry no backtick, and re-match the gate's count regex) —
 *  injected, never trusted. */
function fixtureCapture(c, root) {
  const findings = [];
  const notes = [];
  let n = 0;
  for (const f of c.findings) {
    n++;
    const raw = readText(path.join(root, f.file));
    const lines = raw === null ? null : raw.split(/\r?\n/);
    const line = lines && f.line - 1 < lines.length ? lines[f.line - 1] : null;
    let excerpt = f.excerpt;
    if (excerpt === undefined) {
      if (line === null) throw new Error(`${c.name}: injected finding ${f.file}:${f.line} has no resolvable line and no explicit excerpt`);
      if (line.includes('`')) throw new Error(`${c.name}: injected finding ${f.file}:${f.line} carries a backtick; the gate would not have flagged it`);
      COUNT_NOUN_RE.lastIndex = 0;
      const matches = COUNT_NOUN_RE.test(line);
      COUNT_NOUN_RE.lastIndex = 0;
      if (!matches) throw new Error(`${c.name}: injected finding ${f.file}:${f.line} does not re-match the gate's count regex: ${JSON.stringify(line)}`);
      excerpt = gateExcerpt(line);
    } else {
      notes.push(`injected finding ${n} (${f.file}:${f.line}) carries an explicit excerpt and is therefore not byte-validated`);
    }
    findings.push({ id: `CR-${c.name}-r4-${n}`, rule: 'r4', n, text: `${f.file}:${f.line} count claim with no backticked command: "${excerpt}" (CORPUS.md:28)` });
  }
  return { json: [{ repo: c.name, revision: `${c.name} (worktree)`, dirty: 0, mode: 'live', exit: findings.length ? 1 : 0, findings, notes, stats: { files: 1, rules: { r4: findings.length } } }], notes };
}

function selftest() {
  const expected = readExpected();
  if (!expected || !expected.selftest || !Array.isArray(expected.selftest.cases)) {
    process.stdout.write(`# selftest could-not-evaluate: ${EXPECTED_PATH} missing or unreadable\n`);
    process.exit(EXIT.CNE);
  }
  const expByName = new Map(expected.selftest.cases.map((c) => [c.name, c]));
  let pass = 0;
  const failures = [];
  for (const c of SELFTEST_CASES) {
    const exp = expByName.get(c.name);
    const tmp = fs.mkdtempSync(path.join(os.tmpdir(), 'r4-adjudicate-fx-'));
    let gotExit = null;
    let gotIds = null;
    let gotTests = [];
    let fixtureNote = '';
    try {
      buildFixture(tmp, Object.assign(fixtureFiles(c.name), c.files || {}));
      const cap = fixtureCapture(c, tmp);
      fixtureNote = cap.notes.join('; ');
      const entries = cap.json.map((e) => ({ entry: e, dir: tmp }));
      const results = entries.map(({ entry, dir }) => adjudicateEntry(entry, dir));
      gotExit = combinedExit(results.map((r) => r.exit));
      gotIds = results.flatMap((r) => r.findings.map((f) => `${f.id}:${f.cls}`));
      gotTests = results.flatMap((r) => r.findings.map((f) => `${f.id}:${f.test}`));
    } catch (e) {
      gotExit = 'ERROR:' + (e && e.message ? e.message : String(e));
      gotIds = [];
    } finally {
      try { fs.rmSync(tmp, { recursive: true, force: true }); } catch (e) { /* ignore */ }
    }
    const expIds = exp ? exp.expect_class_ids : null;
    const exitOk = exp && exp.expect_exit === gotExit;
    const idsOk = exp && Array.isArray(expIds) && JSON.stringify(expIds) === JSON.stringify(gotIds);
    if (exitOk && idsOk) {
      pass++;
      process.stdout.write(`# selftest ${c.name} expect_exit=${exp.expect_exit} got_exit=${gotExit} ids=${gotIds.length} PASS\n`);
    } else {
      failures.push(c.name);
      process.stdout.write(`# selftest ${c.name} FAIL expect_exit=${exp ? exp.expect_exit : 'ABSENT'} got_exit=${gotExit} ids=${gotIds.length}\n`);
      process.stdout.write(`#   expect_ids=${JSON.stringify(expIds)}\n`);
      process.stdout.write(`#   got_ids=${JSON.stringify(gotIds)}\n`);
      if (gotTests.length) process.stdout.write(`#   got_tests=${JSON.stringify(gotTests)}\n`);
    }
    if (fixtureNote) process.stdout.write(`#   fixture-note ${fixtureNote}\n`);
  }
  const missing = expected.selftest.cases.map((c) => c.name).filter((n) => !SELFTEST_CASES.some((c) => c.name === n));
  if (missing.length) process.stdout.write(`# selftest note: expected.json declares case(s) with no fixture: ${missing.join(', ')}\n`);
  const extra = SELFTEST_CASES.map((c) => c.name).filter((n) => !expByName.has(n));
  if (extra.length) process.stdout.write(`# selftest note: fixture(s) with no committed expectation: ${extra.join(', ')}\n`);
  process.stdout.write(`# selftest tally ${pass}/${SELFTEST_CASES.length} ${pass === SELFTEST_CASES.length ? 'PASS' : 'FAIL'} (fixtures under os.tmpdir(), live tree untouched)\n`);
  process.exit(pass === SELFTEST_CASES.length ? EXIT.CLEAN : EXIT.VIOLATION);
}

// ---------------------------------------------------------------- frozen-all

function frozenAll() {
  const ge = readText(GATE_EXPECTED_PATH);
  let gateExpected = null;
  try { gateExpected = ge === null ? null : JSON.parse(ge); } catch (e) { gateExpected = null; }
  if (!gateExpected || !gateExpected.frozen) {
    process.stdout.write(`# cne frozen-all could-not-evaluate: ${GATE_EXPECTED_PATH} missing or unreadable\n`);
    process.exit(EXIT.CNE);
  }
  const expected = readExpected();
  const mine = expected && expected.frozen ? expected.frozen : {};
  const keys = Object.keys(gateExpected.frozen).sort();
  const lines = [];
  const codes = [];
  let match = 0;
  for (const key of keys) {
    const g = gateExpected.frozen[key];
    const dir = path.join(MAIN_ROOT, g.repo);
    const spawned = spawnGate(['--snapshot', dir, g.commit, '--round', '9', '--json']);
    const json = parseGateJson(spawned.out);
    lines.push(`# gate ${key} spawn="node .ufo/waves/round-9/corpus-gate.mjs --snapshot ${g.repo} ${g.commit.slice(0, 7)} --round 9 --json" exit=${spawned.code}`);
    if (json === null) {
      lines.push(`# cne ${key} could-not-evaluate: the gate emitted no parseable "# json" line`);
      codes.push(EXIT.CNE);
      continue;
    }
    const entry = json[0];
    const e = adjudicateEntry(entry, dir);
    lines.push(...entryLines(e));
    const gateStatR4 = g.stats && typeof g.stats.r4 === 'number' ? g.stats.r4 : null;
    const gateIdR4 = Array.isArray(g.expect_findings) ? g.expect_findings.filter((i) => /-r4-\d+$/.test(i)).length : null;
    const measured = {
      r4: e.gateR4, exit: e.exit,
      violation: e.counts.violation,
      'fp-entity-designation': e.counts['fp-entity-designation'],
      'fp-design-arithmetic': e.counts['fp-design-arithmetic'],
      'fp-quoted-refutation': e.counts['fp-quoted-refutation'],
      undecided: e.counts.undecided,
    };
    const pin = mine[key];
    if (gateStatR4 !== null && gateStatR4 !== e.gateR4) {
      lines.push(`# cne ${key} could-not-evaluate: the gate re-run reports r4=${e.gateR4}, its committed expected file pins stats.r4=${gateStatR4}`);
      codes.push(EXIT.CNE);
      continue;
    }
    if (gateIdR4 !== null && gateIdR4 !== e.gateR4) {
      lines.push(`# cne ${key} could-not-evaluate: the gate re-run reports r4=${e.gateR4}, its committed expected file lists ${gateIdR4} r4 id(s)`);
      codes.push(EXIT.CNE);
      continue;
    }
    const measuredLine = `r4=${measured.r4} violation=${measured.violation} fp-entity=${measured['fp-entity-designation']} fp-arith=${measured['fp-design-arithmetic']} fp-refutation=${measured['fp-quoted-refutation']} undecided=${measured.undecided} exit=${measured.exit}`;
    if (!pin) {
      lines.push(`# expect ${key} ABSENT measured ${measuredLine}`);
      codes.push(EXIT.DRIFT);
      continue;
    }
    const drift = [];
    if (pin.r4 !== measured.r4) drift.push(`r4 pinned=${pin.r4} got=${measured.r4}`);
    if (pin.exit !== measured.exit) drift.push(`exit pinned=${pin.exit} got=${measured.exit}`);
    for (const c of CLASSES) {
      const p = pin.counts ? pin.counts[c] : null;
      if (p !== measured[c]) drift.push(`${c} pinned=${p} got=${measured[c]}`);
    }
    if (drift.length) {
      lines.push(`# expect ${key} DRIFT ${drift.join('; ')}`);
      codes.push(EXIT.DRIFT);
    } else {
      match++;
      lines.push(`# expect ${key} MATCH r4=${measured.r4} violation=${measured.violation} fp-entity=${measured['fp-entity-designation']} fp-arith=${measured['fp-design-arithmetic']} fp-refutation=${measured['fp-quoted-refutation']} undecided=${measured.undecided} gate-expected-r4=${gateStatR4 === null ? 'unpinned' : gateStatR4} gate-expected-r4-ids=${gateIdR4 === null ? 'unpinned' : gateIdR4}`);
      codes.push(measured.exit);
    }
  }
  lines.push(`# expect tally ${match}/${keys.length} ${match === keys.length ? 'MATCH' : 'DRIFT'}`);
  const exit = combinedExit(codes);
  lines.push(`# process-exit ${exit} (${EXIT_CLASS[exit]})`);
  lines.forEach((l) => process.stdout.write(l + '\n'));
  process.exit(exit);
}

// ---------------------------------------------------------------- main

function parseArgs(argv) {
  const o = { mode: null, repo: null, commit: null, round: 10, json: false, registry: false, file: null, all: false };
  for (let i = 0; i < argv.length; i++) {
    const a = argv[i];
    if (a === '--selftest') o.mode = 'selftest';
    else if (a === '--frozen-all') o.mode = 'frozen-all';
    else if (a === '--all') { o.all = true; if (!o.mode) o.mode = 'live'; }
    else if (a === '--live') { if (!o.mode) o.mode = 'live'; }
    else if (a === '--json') o.json = true;
    else if (a === '--registry') o.registry = true;
    else if (a === '--repo') { o.repo = argv[++i]; if (!o.mode) o.mode = 'live'; }
    else if (a.startsWith('--repo=')) { o.repo = a.slice(7); if (!o.mode) o.mode = 'live'; }
    else if (a === '--from-json') { o.mode = 'from-json'; o.file = argv[++i]; }
    else if (a.startsWith('--from-json=')) { o.mode = 'from-json'; o.file = a.slice(12); }
    else if (a === '--frozen') { o.mode = 'frozen'; o.repo = argv[++i]; o.commit = argv[++i]; }
    else if (a === '--round') o.round = parseInt(argv[++i], 10);
    else if (a.startsWith('--round=')) o.round = parseInt(a.slice(8), 10);
    else if (a === '--help' || a === '-h') o.help = true;
    else { process.stderr.write(`r4-adjudicate: unknown argument ${a}\n`); o.bad = a; }
  }
  return o;
}

const USAGE = 'usage: r4-adjudicate.mjs [--selftest | --frozen-all | --live --all | --live --repo <dir> | --frozen <dir> <commit> | --from-json <file>] [--round N] [--json] [--registry]\n';

function main() {
  const o = parseArgs(process.argv.slice(2));
  if (o.help || o.bad) {
    process.stdout.write(USAGE);
    process.exit(o.bad ? EXIT.CNE : EXIT.CLEAN);
  }
  if (o.registry && !o.mode) {
    printRegistry().forEach((l) => process.stdout.write(l + '\n'));
    process.exit(EXIT.CLEAN);
  }
  if (o.mode === null) {
    process.stdout.write('r4-adjudicate: no mode selected\n' + USAGE);
    printRegistry().forEach((l) => process.stdout.write(l + '\n'));
    process.exit(EXIT.CNE);
  }
  if (o.mode === 'selftest') { selftest(); return; }
  if (o.mode === 'frozen-all') { frozenAll(); return; }

  const head = [];
  head.push(`# ${VERSION} — CORPUS.md rule-4 findings adjudicated (aggregator lane round 10)`);
  if (o.mode === 'live') head.push(`# round-selector=${o.round} (the gate's round selector; r4 is round-independent)`);
  if (o.mode === 'frozen' || o.mode === 'from-json') head.push('# round-selector=9 for the gate spawn when the capture came from a frozen snapshot (see the # gate line)');
  if (o.registry) head.push(...printRegistry());
  head.forEach((l) => process.stdout.write(l + '\n'));

  const captures = [];
  const problems = [];
  let label = o.mode;

  if (o.mode === 'live' && o.all) {
    const spawned = spawnGate(['--all', '--round', String(o.round), '--json']);
    head.push(`# gate spawn="node .ufo/waves/round-9/corpus-gate.mjs --all --round ${o.round} --json" exit=${spawned.code} (exit 1 = rule findings, not a gate error)`);
    process.stdout.write(head[head.length - 1] + '\n');
    const json = parseGateJson(spawned.out);
    if (json === null) {
      process.stdout.write(`# cne live-all could-not-evaluate: the gate emitted no parseable "# json" line (gate exit ${spawned.code})\n`);
      if (spawned.err.trim()) process.stdout.write(`# cne live-all gate stderr: ${spawned.err.trim().split('\n')[0]}\n`);
      process.stdout.write(`# process-exit ${EXIT.CNE} (${EXIT_CLASS[EXIT.CNE]})\n`);
      process.exit(EXIT.CNE);
    }
    if (spawned.code === EXIT.CNE) {
      process.stdout.write(`# note live-all the gate returned exit 2; per-repo could-not-evaluate is reported below\n`);
    }
    captures.push({ entries: json, source: `gate --all --round ${o.round}`, dir: null });
  } else if (o.mode === 'live' && o.repo) {
    const dir = path.resolve(MAIN_ROOT, o.repo);
    const spawned = spawnGate(['--repo', dir, '--round', String(o.round), '--json']);
    process.stdout.write(`# gate spawn="node .ufo/waves/round-9/corpus-gate.mjs --repo ${o.repo} --round ${o.round} --json" exit=${spawned.code}\n`);
    const json = parseGateJson(spawned.out);
    if (json === null) {
      process.stdout.write(`# cne live-repo could-not-evaluate: the gate emitted no parseable "# json" line (gate exit ${spawned.code})\n`);
      process.stdout.write(`# process-exit ${EXIT.CNE} (${EXIT_CLASS[EXIT.CNE]})\n`);
      process.exit(EXIT.CNE);
    }
    captures.push({ entries: json, source: `gate --repo ${o.repo} --round ${o.round}`, dir });
  } else if (o.mode === 'frozen') {
    const dir = path.resolve(MAIN_ROOT, o.repo);
    const spawned = spawnGate(['--snapshot', dir, o.commit, '--round', '9', '--json']);
    process.stdout.write(`# gate spawn="node .ufo/waves/round-9/corpus-gate.mjs --snapshot ${o.repo} ${o.commit} --round 9 --json" exit=${spawned.code}\n`);
    const json = parseGateJson(spawned.out);
    if (json === null) {
      process.stdout.write(`# cne frozen could-not-evaluate: the gate emitted no parseable "# json" line (gate exit ${spawned.code})\n`);
      process.stdout.write(`# process-exit ${EXIT.CNE} (${EXIT_CLASS[EXIT.CNE]})\n`);
      process.exit(EXIT.CNE);
    }
    captures.push({ entries: json, source: `gate --snapshot ${o.repo} ${o.commit}`, dir });
  } else if (o.mode === 'from-json') {
    if (!o.file) {
      process.stdout.write('# cne from-json could-not-evaluate: --from-json needs a file\n');
      process.exit(EXIT.CNE);
    }
    const text = readText(o.file);
    if (text === null) {
      process.stdout.write(`# cne from-json could-not-evaluate: ${o.file} unreadable\n`);
      process.exit(EXIT.CNE);
    }
    let jsonLine = null;
    if (text.split(/\r?\n/).some((l) => l.startsWith('# json '))) jsonLine = text;
    else {
      let doc = null;
      try { doc = JSON.parse(text); } catch (e) { doc = null; }
      if (doc && doc.capture && typeof doc.capture.json_line === 'string') jsonLine = doc.capture.json_line;
    }
    const json = jsonLine === null ? null : parseGateJson(jsonLine);
    if (json === null) {
      process.stdout.write(`# cne from-json could-not-evaluate: ${o.file} carries neither a "# json " line nor capture.json_line\n`);
      process.exit(EXIT.CNE);
    }
    const dirOverride = o.repo ? path.resolve(MAIN_ROOT, o.repo) : null;
    captures.push({ entries: json, source: `${o.file} (capture replayed; snapshot revisions read with git show, worktree revisions from the worktree)`, dir: dirOverride });
  } else {
    process.stdout.write(`r4-adjudicate: mode ${o.mode} needs --all, --repo or --snapshot arguments\n`);
    process.exit(EXIT.CNE);
  }

  const lines = [];
  const results = [];
  for (const cap of captures) {
    for (const entry of cap.entries) {
      const e = adjudicateEntry(entry, cap.dir);
      results.push(e);
      lines.push(...entryLines(e));
    }
  }
  lines.forEach((l) => process.stdout.write(l + '\n'));
  for (const p of problems) process.stdout.write(p + '\n');

  const totals = {};
  for (const c of CLASSES) totals[c] = results.reduce((a, r) => a + r.counts[c], 0);
  totals.r4 = results.reduce((a, r) => a + r.gateR4, 0);
  totals.classified = results.reduce((a, r) => a + r.classified, 0);
  process.stdout.write(`# tally repos=${results.length} r4=${totals.r4} violation=${totals.violation} fp-entity=${totals['fp-entity-designation']} fp-arith=${totals['fp-design-arithmetic']} fp-refutation=${totals['fp-quoted-refutation']} undecided=${totals.undecided}\n`);

  const exit = combinedExit(results.map((r) => r.exit));
  if (o.json) {
    const doc = {
      version: VERSION,
      mode: o.mode,
      round: o.round,
      exit,
      exit_class: EXIT_CLASS[exit],
      classes: CLASSES,
      totals,
      repos: results.map((r) => ({
        repo: r.repo, revision: r.revision, tree: r.tree, worktree: r.worktree, dirty: r.dirty, mode: r.mode,
        gate_exit: r.gateExit, gate_r4: r.gateR4, classified: r.classified, counts: r.counts,
        other_rules: r.otherRules || {}, exit: r.exit, notes: r.notes,
        findings: r.findings.map((f) => ({
          id: f.id, class: f.cls, test: f.test, file: f.file === null ? null : `corpus/${f.file}`, line: f.line,
          token: f.token, excerpt: f.excerpt, tuple: f.tuple || null, note: f.note || null,
        })),
      })),
    };
    process.stdout.write('# json ' + JSON.stringify(sortedKeys(doc)) + '\n');
  }
  process.stdout.write(`# process-exit ${exit} (${EXIT_CLASS[exit]})\n`);
  process.exit(exit);
}

main();