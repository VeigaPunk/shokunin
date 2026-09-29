#!/usr/bin/env node
// corpus-gate.mjs — aggregator lane, round 9.  Gate id: corpus-gate-v1.
//
// WHAT THIS IS
//   A committed, re-runnable verdict script that recomputes the mechanically-checkable
//   CORPUS.md rules for one child repo (or the whole fleet of six) and prints, for each
//   repo, the rule-10 conformance verdict the aggregator ledger cites.  It exists so a
//   non-author can re-derive the aggregator's rule-10 verdicts without re-running prose.
//
// Registry block (PROTOCOL.md §Gate standard: "the rows live in each lane's SKILL.md" —
// the aggregator lane HAS NO SKILL.md; that gap is a routed defect, D-120 class.  Until
// it exists the registry row lives here and is echoed verbatim by --registry, and is
// copied into .ufo/waves/round-9/seats/gate-draft.md).
//
//   name              corpus-gate
//   kind              gate
//   version           corpus-gate-v1
//   owner             aggregator lane (/home/vgpnk/projects/shokunin), round 9
//   write scope       READ-ONLY over every surface it grades.  The only writes are
//                     throwaway trees inside os.tmpdir() (--selftest fixtures,
//                     --snapshot extraction), both removed before exit.
//   entry command     node .ufo/waves/round-9/corpus-gate.mjs --all
//                     node .ufo/waves/round-9/corpus-gate.mjs --repo <child-repo-dir>
//                     node .ufo/waves/round-9/corpus-gate.mjs --snapshot <child-repo-dir> <commit>
//                     node .ufo/waves/round-9/corpus-gate.mjs --selftest
//   verdict map       0 = clean
//                     1 = failed            (one or more CORPUS.md rule findings)
//                     2 = could-not-evaluate (no corpus/ dir, unreadable corpus, git failure)
//                     3 = failed            (frozen expectation drift -- the committed
//                                            expected verdict no longer reproduces)
//                     precedence across repos / across a snapshot: 2 > 3 > 1 > 0
//   self-test         --selftest ; expected values in
//                     .ufo/waves/round-9/corpus-gate.expected.json (selftest.cases[])
//   pinned values     .ufo/waves/round-9/corpus-gate.expected.json
//                     (selftest.cases[] + frozen[] = committed input snapshots with their
//                      committed expected verdicts)
//   round selector    --round <N>   (default 9) ; the round whose aggregator lesson r10 requires
//
// CHECKS IMPLEMENTED (each finding-id is CR-<repo>-<rule>-<n>, n a 1-based ordinal over a
// deterministic (rule, key) sort, so the same input always yields the same ids)
//
//   r2     CORPUS.md:19 — a lessons/ entry must cite its round and its evidence.
//   r4     CORPUS.md:28 — a count ("<n> <count-noun>") on a line with no backticked command.
//   r7     CORPUS.md:40 — an index row naming a corpus path that is not in the graded tree.
//   r8     CORPUS.md:43 — credential material, on the LITERAL text (`op://…` included).
//          UNIT = occurrences (not matching lines, not files): the finding text carries
//          occurrences=, lines=, files=, the graded revision, and owner= (aggregator |
//          lane, by the `round-<N>-aggregator-*.md` filename pattern) so the row routes to
//          whoever owns the bytes.  The schematic-vs-real classification is DECLARED
//          could-not-evaluate, never guessed: deciding whether a ref names a real vault
//          item needs a vault read, which is operator-gated.
//   r10    CORPUS.md:21 — the round's aggregator lesson (corpus/lessons/round-<R>-aggregator-*.md)
//          is absent.  (Rule 10's verdict itself is the `# verdict` line this gate prints per
//          repo; the presence check is the only part of the round-review duty that is
//          mechanically decidable.)
//   shonen PROTOCOL.md §File contract — SHONEN.md canonical form, per the clause "the seed
//          block must diff byte-identical modulo <name> … marks are confined to the box
//          character plus one indented evidence line per box … no other prose".  Checks the
//          header block, exactly 4 boxes with canonical text, mark char ∈ {x,~,space},
//          at most one indented evidence line per box, a non-blank evidence line required
//          for a marked box, an [x] mark line carrying a <verifier-id> token, no other
//          lines, and the trailing newline.  NOT a CORPUS.md rule; included because the
//          round's rule-10 verdict cites §File contract conformance too.
//
// RULES NOT EVALUATED, with the reason (a gate that fakes a check is worse than one that
// declares the hole):
//
//   r1  "knowledge/ entries cite a source: file path, command output, or URL".  Deciding
//       whether a token is a *source* is semantic, and resolving it needs the province tree
//       (`~/Projects/bounties` is GONE from this host, so most kasegi citations cannot be
//       resolved at all).  Not honestly mechanical.
//   r3  "A corpus entry is falsifiable or marked opinion".  Requires judging a claim's
//       falsifiability -- semantic, not mechanical.
//   r5  "A negative claim carries its sweep".  Needs negation detection plus proximity
//       matching against a search command; a proximity heuristic would fire on every
//       "no X" in prose.  Declared not-evaluated rather than faked (the round-6 ledger's
//       own rule-5 findings were hand-adjudicated).
//   r6  "A quote names its location".  Verifying frontmatter-vs-body or script-vs-installed-skill
//       requires the quoted surface, which lives outside the repo (and partly on a dead path).
//   r9  "Corrections are new entries, never rewrites; no lane edits another's corpus files".
//       ONE sub-check is mechanical (aggregator-identity authorship in `git log -- <lesson>`),
//       but it is not decisive: the identity is a commit-time string any writer can set, an
//       in-place rewrite by the legitimate owner is invisible to it, and --snapshot grades a
//       `git archive` tree that carries NO history -- so the check would be unavailable in
//       exactly the mode whose verdict must name a revision.  Declared not-evaluated.
//   box-3  Whether a box-3 (or any) [x] mark rests on a *non-author* verifier.  Deciding it
//       needs the authorship graph of past rounds (who wrote the attested round's evidence),
//       which does not live in the graded tree; the shonen check can only see that a
//       verifier-id token is present, not that the id is independent of the lane.
//   shonen-semantics  Whether a box's claim is TRUE.  The shonen check grades canonical FORM
//       only; box content is prose.
//
// OUT OF SCOPE BY CONSTRUCTION (stated so a reader is not surprised):
//   * corpus/evidence/** and corpus-root data files (kagi's *.sh/*.tsv) are not part of the
//     layout CORPUS.md:9-15 declares; r4 and r7 read the canonical surfaces only
//     (README.md, knowledge/**.md, lessons/**.md).  r8 reads EVERY text file under corpus/,
//     because rule 8's scope is "every corpus".
//   * r7 grades phantom rows (row without file).  Under-coverage (file without row) is
//     printed as a `# note` and is NOT a finding: CORPUS.md:40 makes the phantom row the
//     defect ("a seeded index naming seven entries while one existed is worse than a
//     one-row index"), and evidence/ bulk alone would bury real findings.

import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { spawnSync } from 'node:child_process';
import { fileURLToPath } from 'node:url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const VERSION = 'corpus-gate-v1';
const MAIN_ROOT = path.resolve(__dirname, '..', '..', '..');
const EXPECTED_PATH = path.join(__dirname, 'corpus-gate.expected.json');

const EXIT = { CLEAN: 0, FAILED: 1, CNE: 2, DRIFT: 3 };
const EXIT_CLASS = { 0: 'clean', 1: 'failed', 2: 'could-not-evaluate', 3: 'failed' };
const EXIT_PRECEDENCE = [2, 3, 1, 0];

const RULE_ORDER = ['r2', 'r4', 'r7', 'r8', 'r10', 'shonen'];

const REGISTRY = {
  name: 'corpus-gate',
  kind: 'gate',
  version: VERSION,
  owner: 'aggregator lane (/home/vgpnk/projects/shokunin), round 9',
  entry: {
    all: 'node .ufo/waves/round-9/corpus-gate.mjs --all',
    one: 'node .ufo/waves/round-9/corpus-gate.mjs --repo <child-repo-dir>',
    snapshot: 'node .ufo/waves/round-9/corpus-gate.mjs --snapshot <child-repo-dir> <commit>',
    selftest: 'node .ufo/waves/round-9/corpus-gate.mjs --selftest',
  },
  verdict_map: {
    '0': 'clean',
    '1': 'failed',
    '2': 'could-not-evaluate',
    '3': 'failed (frozen-expectation drift)',
  },
  verdict_precedence: '2 > 3 > 1 > 0',
  selftest_flag: '--selftest',
  pinned_values: 'corpus-gate.expected.json (selftest.cases[] + frozen[])',
  write_scope: 'read-only; writes only inside os.tmpdir() (selftest fixtures, snapshot extraction), removed before exit',
  round_flag: '--round <N> (default 9)',
  checks: [
    { rule: 'r2', corpush: 'CORPUS.md:19', what: 'a lessons/ entry cites its round and its evidence (commit hash, .ufo/reports/ path, or LOG.md)' },
    { rule: 'r4', corpush: 'CORPUS.md:28', what: 'a count claim (<n> <count-noun>) on a line with no backticked command' },
    { rule: 'r7', corpush: 'CORPUS.md:40', what: 'an index row (corpus-relative backticked path) naming a file absent from the graded tree' },
    { rule: 'r8', corpush: 'CORPUS.md:43', what: 'credential material on the literal text, incl. op:// refs; unit=occurrences; fields occurrences/lines/files/owner/revision; schematic-vs-real classification declared could-not-evaluate (needs a vault read, operator-gated)' },
    { rule: 'r10', corpush: 'CORPUS.md:21', what: 'the round\'s aggregator lesson corpus/lessons/round-<R>-aggregator-*.md is present (rule 10 verdict itself is the # verdict line)' },
    { rule: 'shonen', corpush: 'PROTOCOL.md §File contract', what: 'SHONEN.md canonical form: header, exactly 4 canonical boxes, marks confined to the box char + at most one indented evidence line, [x] mark line carries a <verifier-id>, no other lines, trailing newline' },
  ],
  not_evaluated: [
    { rule: 'r1', corpush: 'CORPUS.md:18', reason: 'semantic (is this token a source?) + province tree partly absent (~/Projects/bounties gone)' },
    { rule: 'r3', corpush: 'CORPUS.md:20', reason: 'semantic (falsifiable-or-marked-opinion)' },
    { rule: 'r5', corpush: 'CORPUS.md:33', reason: 'needs negation+proximity NL parsing; a heuristic would fire on every prose "no X"' },
    { rule: 'r6', corpush: 'CORPUS.md:36', reason: 'needs the quoted surface (frontmatter/installed skill), which lives outside the graded repo' },
    { rule: 'r9', corpush: 'CORPUS.md:47', reason: 'append-only-vs-rewrite is history-dependent; snapshot mode grades a git-archive tree with no history; author-identity is a settable commit-time string' },
    { rule: 'box-3', corpush: 'PROTOCOL.md §Promotion gates', reason: 'whether an [x] rests on a NON-author verifier needs the authorship graph of past rounds, which the graded tree does not carry; the shonen check sees a verifier-id token, not its independence' },
    { rule: 'shonen-semantics', corpush: 'PROTOCOL.md §File contract', reason: 'whether a box claim is true is prose; the shonen check grades canonical form only' },
  ],
  /** r8's classification sub-result is an exit-2-class abstention, not a verdict. */
  r8_classification: 'could-not-evaluate',
};

const DEFAULT_REPOS = [
  'kasegi-shokunin',
  'kengaku-shokunin',
  'kake-shokunin',
  'kumitate-shokunin',
  'kotoba-shokunin',
  'kagi-shokunin',
];

const TEXT_EXT = new Set(['.md', '.sh', '.tsv', '.json', '.jsonl', '.py', '.log', '.txt', '.yml', '.yaml', '.csv', '.sha256', '.mjs']);
const INDEX_EXT_RE = /\.(md|sh|tsv|json|jsonl|py|log|txt|yml|yaml|csv|sha256)$/;
const INDEX_SUBDIRS = ['knowledge/', 'lessons/', 'evidence/', 'handoffs/'];

// ---------------------------------------------------------------- helpers

function git(repoDir, args, opts) {
  const r = spawnSync('git', ['-C', repoDir].concat(args), Object.assign({ encoding: 'utf8', maxBuffer: 1 << 30 }, opts || {}));
  return { code: r.status === null ? 127 : r.status, out: r.stdout || '', err: r.stderr || '' };
}

function readText(p) {
  try {
    return fs.readFileSync(p, 'utf8');
  } catch (e) {
    return null;
  }
}

function walk(dir, base, acc) {
  let ents;
  try {
    ents = fs.readdirSync(dir, { withFileTypes: true });
  } catch (e) {
    return acc;
  }
  ents.sort((a, b) => (a.name < b.name ? -1 : a.name > b.name ? 1 : 0));
  for (const e of ents) {
    const p = path.join(dir, e.name);
    if (e.isDirectory()) walk(p, base, acc);
    else if (e.isFile()) acc.push(path.relative(base, p).split(path.sep).join('/'));
  }
  return acc;
}

function pad6(n) {
  return String(n).padStart(6, '0');
}

function first4(s) {
  return s.slice(0, 4).replace(/[^\x20-\x7e]/g, '.');
}

function excerpt(s) {
  return s.trim().replace(/\s+/g, ' ').slice(0, 60);
}

// ---------------------------------------------------------------- rule checks

const COUNT_NOUN_RE = /\b\d[\d,_]*\s+(rows?|files?|lines?|packages?|entries|dirs?|directories|commits?|sessions?|seats?|checks?|ids?|calls?|runs?|draws?|hits?|boxes|members?|scripts?|tests?|cases?|notes?|citations?|sites?|repos?|lanes?|words?|paths?|probes?|columns?|fields?|stamps?|pins?)\b/;

const CRED_PATTERNS = [
  { cls: 'op-ref', re: /op:\/\/[^\s"'`)\]<>|]*/g },
  { cls: 'sk-token', re: /\bsk-[A-Za-z0-9_-]{16,}/g },
  { cls: 'ghp-token', re: /\bghp_[A-Za-z0-9]{16,}/g },
  { cls: 'github-pat', re: /\bgithub_pat_[A-Za-z0-9_]{16,}/g },
  { cls: 'slack-token', re: /\bxox[baprs]-[A-Za-z0-9-]{8,}/g },
  { cls: 'aws-akia', re: /\bAKIA[0-9A-Z]{16}\b/g },
  { cls: 'jwt', re: /\beyJ[A-Za-z0-9_-]{6,}\.[A-Za-z0-9_-]{6,}\.[A-Za-z0-9_-]{4,}/g },
  { cls: 'private-key', re: /-----BEGIN [A-Z ]*PRIVATE KEY-----/g },
  // Bearer needs a token SHAPE, not just a word after the keyword: `Bearer auth was` and
  // `bearer patterns)` (an aggregator lesson quoting its own sweep) are prose, not credentials.
  { cls: 'bearer', re: /\bbearer\s+[A-Za-z0-9][A-Za-z0-9._+/-]{7,}/gi },
  { cls: 'cookie', re: /\b(set-)?cookie\s*:\s*\S{4,}/gi },
  { cls: 'kv-secret', re: /\b(password|passwd|api[_-]?key|access[_-]?token|auth[_-]?token|token|secret)\s*[=:]\s*\S{8,}/gi },
];

// Shape measure for an op:// ref: the number of non-empty path segments after the scheme.
// A real 1Password reference is `op://<vault>/<item>/<field>` (3).  This is a COUNT, not a
// judgement: the gate does not decide whether a ref names a real vault (see registry
// not_evaluated / r8_classification).
function opRefSegments(match) {
  return match.slice('op://'.length).split('/').filter((s) => s !== '').length;
}

// The value part of a value-class match, and whether that part is shaped like a literal
// token or like a grammar/code expression.  Again a SYNTAX fact, not a judgement about
// whether a secret is real -- `token:<w>|metachar|backslash` is a grammar, and saying so is
// what lets a reader close the finding without opening the file.
function valuePart(cls, hit) {
  if (cls === 'bearer') { const m = hit.match(/^\s*bearer\s+(.*)$/i); return m ? m[1] : hit; }
  if (cls === 'cookie') { const m = hit.match(/^\s*(?:set-)?cookie\s*:\s*(.*)$/i); return m ? m[1] : hit; }
  if (cls === 'kv-secret') { const m = hit.match(/[=:]\s*(.*)$/); return m ? m[1] : hit; }
  return hit;
}

function isLiteralShaped(v) {
  return !/[<>{}()$|"'`\\]/.test(v) && !/\s/.test(v);
}

// PROTOCOL.md §File contract, SHONEN.md canonical form (see the registry block).
const CANON_BOXES = [
  'SKILL.md contains real decision tables, error patterns, checklists, cited sources',
  'At least one end-to-end domain task executed and logged in LOG.md',
  'Instructions executable by an agent without oral context',
  'No cross-domain bleed (PROVINCE.md still accurate)',
];

function checkShonen(repoDir, label, push) {
  const raw = readText(path.join(repoDir, 'SHONEN.md'));
  if (raw === null) {
    push('shonen', 'SHONEN.md@000000#absent', 'SHONEN.md absent — the promotion checklist does not exist (PROTOCOL.md §File contract)');
    return;
  }
  const trailingNewline = raw.endsWith('\n');
  if (!trailingNewline) push('shonen', 'SHONEN.md@000000#trailing-newline', 'SHONEN.md lacks the required trailing newline (canonical form)');
  const lines = (trailingNewline ? raw.slice(0, -1) : raw).split('\n');
  const header = [`# ${label} — Promotion checklist`, '', 'Promotion to shokunin requires all of:', ''];
  for (let i = 0; i < header.length; i++) {
    if (lines[i] !== header[i]) push('shonen', `SHONEN.md@${pad6(i + 1)}#header`, `SHONEN.md:${i + 1} header line deviates from the canonical seed: got ${JSON.stringify(lines[i])}, expected ${JSON.stringify(header[i])} (modulo <name>=${label})`);
  }
  const BOX_RE = /^- \[(.)\] (.*)$/;
  const boxes = [];
  for (let i = 0; i < lines.length; i++) {
    const m = lines[i].match(BOX_RE);
    if (m) boxes.push({ idx: i, line: i + 1, mark: m[1], text: m[2] });
  }
  if (boxes.length !== 4) push('shonen', `SHONEN.md@${pad6(5)}#box-count`, `SHONEN.md carries ${boxes.length} box line(s); the canonical seed has exactly 4`);
  const consumed = new Set([0, 1, 2, 3]);
  const noVerifier = [];
  boxes.forEach((box, b) => {
    consumed.add(box.idx);
    const canon = CANON_BOXES[b];
    if (canon !== undefined && box.text !== canon) push('shonen', `SHONEN.md@${pad6(box.line)}#box-text`, `SHONEN.md:${box.line} box ${b + 1} text deviates from the canonical seed: got ${JSON.stringify(box.text)}`);
    if (!'x~ '.includes(box.mark)) push('shonen', `SHONEN.md@${pad6(box.line)}#mark-char`, `SHONEN.md:${box.line} mark character ${JSON.stringify(box.mark)} is not one of x, ~, space`);
    let ev = 0;
    let j = box.idx + 1;
    while (j < lines.length && /^\s+\S/.test(lines[j])) { ev++; consumed.add(j); j++; }
    if (ev > 1) push('shonen', `SHONEN.md@${pad6(box.line)}#evidence-count`, `SHONEN.md:${box.line} box ${b + 1} carries ${ev} indented evidence lines; the canonical form allows at most one`);
    if (box.mark !== ' ' && ev === 0) push('shonen', `SHONEN.md@${pad6(box.line)}#evidence-missing`, `SHONEN.md:${box.line} box ${b + 1} is marked ${JSON.stringify(box.mark)} but carries no indented evidence line with a resolvable pointer`);
    if (box.mark === 'x' && canon !== undefined && box.text === canon) {
      const id = lines[box.idx].slice(('- [x] ' + canon).length).trim();
      if (id === '') noVerifier.push(box.line);
    }
  });
  if (noVerifier.length) push('shonen', 'SHONEN.md@000000#no-verifier-id', `SHONEN.md ${noVerifier.length} [x] mark line(s) at ${noVerifier.join(',')} carry no <verifier-id> token after the box text — the canonical form requires one (§Promotion gates: only a non-author may write [x])`);
  for (let i = 0; i < lines.length; i++) {
    if (consumed.has(i)) continue;
    const blank = lines[i].trim() === '';
    push('shonen', `SHONEN.md@${pad6(i + 1)}#other-line`, `SHONEN.md:${i + 1} is neither the header block, a box line, nor an evidence line (${blank ? 'blank line' : 'prose'}): ${JSON.stringify(excerpt(lines[i]))}`);
  }
}

function gradeCorpus(repoDir, opts) {
  const label = opts.label;
  const round = opts.round;
  const findings = [];
  const notes = [];
  const stats = { files: 0, rules: {} };
  const corpusDir = path.join(repoDir, 'corpus');

  const push = (rule, key, text) => findings.push({ rule, key, text });

  if (!fs.existsSync(corpusDir) || !fs.statSync(corpusDir).isDirectory()) {
    return { label, exit: EXIT.CNE, findings: [], notes: ['corpus/ absent or not a directory — cannot evaluate'], stats };
  }

  const files = walk(corpusDir, corpusDir, []);
  stats.files = files.length;
  const basenames = new Set(files.map((f) => f.split('/').pop()));

  // ---- r7: index rows vs the graded tree
  const readmeRel = 'README.md';
  const readmePath = path.join(corpusDir, readmeRel);
  const indexed = new Set();
  if (!files.includes(readmeRel)) {
    push('r7', 'README.md', 'corpus/README.md is absent — no index exists (CORPUS.md:11,40)');
  } else {
    const text = readText(readmePath) || '';
    const lines = text.split(/\r?\n/);
    let fence = false;
    let skippedTemplate = 0;
    const consider = (raw, lineNo) => {
      let s = raw.trim().replace(/[.,;:]+$/, '');
      if (s === '' || !INDEX_EXT_RE.test(s)) return;
      if (/[*<>{}~$…]/.test(s) || /\.\.\./.test(s)) { skippedTemplate++; return; }
      // brace expansion: lessons/round-{1,4,5}-aggregator-audit.md
      const brace = s.match(/^(.*)\{([\d,\s]+)\}(.*)$/);
      const candidates = [];
      if (brace) {
        for (const n of brace[2].split(',').map((x) => x.trim()).filter(Boolean)) candidates.push(brace[1] + n + brace[3]);
      } else candidates.push(s);
      for (const cand of candidates) {
        const key = cand;
        const sub = INDEX_SUBDIRS.some((d) => cand.startsWith(d));
        const abs = path.join(corpusDir, cand);
        const resolved = fs.existsSync(abs) || (!sub && basenames.has(cand.split('/').pop()));
        if (resolved) indexed.add(cand);
        else if (sub) push('r7', `${key}@${pad6(lineNo)}`, `index row names ${cand} — absent from the graded tree (README.md:${lineNo}, CORPUS.md:40)`);
      }
    };
    for (let i = 0; i < lines.length; i++) {
      const l = lines[i];
      if (l.trimStart().startsWith('```')) { fence = !fence; continue; }
      if (fence) continue;
      const rng = l.match(/`([^`\n]+?\.md)`\s*(?:…|\.\.\.)\s*`([^`\n]+?\.md)`/);
      if (rng) {
        const a = rng[1].match(/^(.*?)(\d+)\.md$/);
        const b = rng[2].match(/^(.*?)(\d+)\.md$/);
        if (a && b && a[1] === b[1]) {
          const lo = Math.min(+a[2], +b[2]);
          const hi = Math.max(+a[2], +b[2]);
          if (hi - lo <= 100) for (let n = lo; n <= hi; n++) consider('`' + a[1] + n + '.md`', i + 1);
        }
      }
      const spans = l.match(/`[^`\n]+`/g) || [];
      for (const sp of spans) consider(sp.slice(1, -1), i + 1);
    }
    if (skippedTemplate) notes.push(`r7: ${skippedTemplate} backticked path template(s)/glob(s) skipped (contain *, <, {, ~, $ or …)`);
    const unindexed = files.filter((f) => f !== readmeRel && !indexed.has(f));
    notes.push(`r7 under-coverage (not a finding): ${unindexed.length}/${files.length - 1} corpus files carry no index row`);
  }

  // ---- r2: lessons cite their round and their evidence
  const lessons = files.filter((f) => f.startsWith('lessons/') && f.endsWith('.md'));
  for (const f of lessons) {
    const num = (f.split('/').pop().match(/round-(\d+)/) || [])[1];
    const text = readText(path.join(corpusDir, f));
    if (!num || text === null) continue;
    const body = text;
    const roundCited = new RegExp('\\b[Rr]ound[-_ ]?' + num + '\\b').test(body);
    const evidenceCited = /\b[0-9a-f]{7,40}\b/.test(body) || /\.ufo\/reports\//.test(body) || /LOG\.md/.test(body);
    if (!roundCited) push('r2', `${f}#missing-round-citation`, `${f} carries no citation of its own round (round-${num}) (CORPUS.md:19)`);
    if (!evidenceCited) push('r2', `${f}#missing-evidence-pointer`, `${f} carries no evidence pointer (commit hash, .ufo/reports/ path, or LOG.md) (CORPUS.md:19)`);
  }

  // ---- r10: the round's aggregator lesson
  const aggRe = new RegExp('^lessons/round-' + round + '-aggregator-.+\\.md$');
  if (!files.some((f) => aggRe.test(f))) {
    push('r10', `round-${round}`, `no corpus/lessons/round-${round}-aggregator-*.md — the round-${round} review duty has no emitted lesson (CORPUS.md:21)`);
  }

  // ---- r4: count claims without a backticked command  (canonical surfaces only)
  const mdFiles = files.filter((f) => INDEX_SUBDIRS.slice(0, 2).some((d) => f.startsWith(d)) && f.endsWith('.md')).concat(files.includes(readmeRel) ? [readmeRel] : []);
  for (const f of mdFiles) {
    const text = readText(path.join(corpusDir, f));
    if (text === null) continue;
    let fence = false;
    const lines = text.split(/\r?\n/);
    for (let i = 0; i < lines.length; i++) {
      const l = lines[i];
      if (l.trimStart().startsWith('```')) { fence = !fence; continue; }
      if (fence) continue;
      if (l.includes('`')) continue;
      if (!COUNT_NOUN_RE.test(l)) continue;
      push('r4', `${f}@${pad6(i + 1)}`, `${f}:${i + 1} count claim with no backticked command: "${excerpt(l)}" (CORPUS.md:28)`);
    }
  }

  // ---- r8: credential material, LITERAL text, every corpus file.  UNIT = occurrences.
  // The schematic-vs-real classification is declared could-not-evaluate (it needs a vault
  // read, operator-gated), so the gate never guesses it -- it reports shape facts
  // (occurrences/lines/files/maxseg) and routes by owner.
  const revTxt = opts.revision || 'unstated';
  const credGroups = new Map();
  for (const f of files) {
    const ext = path.extname(f).toLowerCase();
    if (!TEXT_EXT.has(ext)) continue;
    const text = readText(path.join(corpusDir, f));
    if (text === null) continue;
    const owner = /(^|\/)round-\d+-aggregator-[^/]*$/.test(f) ? 'aggregator' : 'lane';
    const lines = text.split(/\r?\n/);
    for (let i = 0; i < lines.length; i++) {
      for (const p of CRED_PATTERNS) {
        p.re.lastIndex = 0;
        let m;
        while ((m = p.re.exec(lines[i])) !== null) {
          if (m[0] === '') break;
          // A bearer VALUE must look like a token: at least one digit or separator. Without
          // this, `Bearer auth was` and a lesson's own `token/secret/cookie/bearer patterns`
          // sweep list read as credentials (both observed at kengaku/kagi before the filter).
          if (p.cls === 'bearer' && !/[0-9._+/-]/.test(valuePart('bearer', m[0]))) continue;
          const key = p.cls + '\u0000' + owner;
          let g = credGroups.get(key);
          if (!g) { g = { cls: p.cls, owner, occ: 0, literal: 0, lineSet: new Set(), fileSet: new Set(), first: null, maxseg: 0 }; credGroups.set(key, g); }
          g.occ++;
          g.lineSet.add(f + ':' + (i + 1));
          g.fileSet.add(f);
          if (p.cls === 'op-ref') g.maxseg = Math.max(g.maxseg, opRefSegments(m[0]));
          else if (isLiteralShaped(valuePart(p.cls, m[0]))) g.literal++;
          if (!g.first) g.first = { f, line: i + 1, first4: first4(m[0]), len: m[0].length };
        }
      }
    }
  }
  const credSorted = [...credGroups.values()].sort((a, b) => (a.cls + '#' + a.owner < b.cls + '#' + b.owner ? -1 : 1));
  for (const g of credSorted) {
    const fl = [...g.fileSet].sort();
    const shown = fl.slice(0, 6).join(',') + (fl.length > 6 ? `,+${fl.length - 6} more` : '');
    const shape = g.cls === 'op-ref' ? ` maxseg=${g.maxseg}` : ` literal_shaped=${g.literal}/${g.occ}`;
    push('r8', `${g.cls}#${g.owner}`,
      `credential-class ${g.cls} occurrences=${g.occ} lines=${g.lineSet.size} files=${g.fileSet.size} owner=${g.owner} at ${revTxt}${shape} :: classification=could-not-evaluate (needs a vault read; operator-gated) files=[${shown}] first=${g.first.f}:${g.first.line} first4="${g.first.first4}" len=${g.first.len} (CORPUS.md:43)`);
    notes.push(`r8 ${g.cls}/${g.owner} file-list: ${fl.join(' ')}`);
  }
  if (credGroups.size) notes.push('r8 classification=could-not-evaluate (exit-2-class abstention; never guessed) — the literal-text occurrence findings above stand as failed (CORPUS.md:43 reads "stay out of every corpus, including this one\'s examples")');

  // ---- shonen: PROTOCOL.md §File contract canonical form
  checkShonen(repoDir, label, push);

  // ---- ids: deterministic (rule, key) sort, 1-based per rule
  const ordered = [];
  for (const rule of RULE_ORDER) {
    const grp = findings.filter((f) => f.rule === rule).sort((a, b) => (a.key < b.key ? -1 : a.key > b.key ? 1 : 0));
    grp.forEach((f, i) => {
      ordered.push({ id: `CR-${label}-${rule}-${i + 1}`, rule, n: i + 1, text: f.text });
    });
    stats.rules[rule] = grp.length;
  }
  const exit = ordered.length === 0 ? EXIT.CLEAN : EXIT.FAILED;
  return { label, exit, findings: ordered, notes, stats };
}

// ---------------------------------------------------------------- run modes

function revisionStamp(repoDir) {
  const head = git(repoDir, ['rev-parse', 'HEAD']);
  const st = git(repoDir, ['status', '--porcelain']);
  if (head.code !== 0) return { ok: false, err: head.err.trim() };
  const dirty = st.out.split('\n').filter(Boolean).length;
  const untrackedCorpus = git(repoDir, ['ls-files', '--others', '--exclude-standard', '--', 'corpus/']).out.split('\n').filter(Boolean).length;
  const deletedCorpus = git(repoDir, ['ls-files', '--deleted', '--', 'corpus/']).out.split('\n').filter(Boolean).length;
  return { ok: true, head: head.out.trim(), short: head.out.trim().slice(0, 7), dirty, untrackedCorpus, deletedCorpus };
}

function linesForResult(res, meta) {
  const out = [];
  out.push(`# tree ${res.label} revision=${meta.revision} dirty=${meta.dirty} mode=${meta.mode}${meta.dirty > 0 ? ' provisional=1 (worktree-only bytes differ from the cited revision)' : ''}`);
  for (const f of res.findings) out.push(`${f.id}: ${f.text}`);
  for (const n of res.notes) out.push(`# note ${res.label} ${n}`);
  const failedRules = RULE_ORDER.filter((r) => res.stats.rules[r] > 0);
  out.push(`# verdict ${res.label} ${EXIT_CLASS[res.exit]} findings=${res.findings.length} rules=${failedRules.join(',') || 'none'} rules-implemented=${RULE_ORDER.join(',')}`);
  return out;
}

function runLive(repoDir, opts) {
  const abs = path.resolve(repoDir);
  const label = opts.label || path.basename(abs);
  const stamp = revisionStamp(abs);
  if (!stamp.ok) {
    return { res: { label, exit: EXIT.CNE, findings: [], notes: [`git rev-parse failed: ${stamp.err}`], stats: { files: 0, rules: {} } }, meta: { revision: 'unknown', dirty: -1, mode: 'live' } };
  }
  const res = gradeCorpus(abs, { label, round: opts.round, revision: stamp.short + '(worktree)' });
  if (res.exit !== EXIT.CNE) {
    if (stamp.untrackedCorpus > 0) res.notes.push(`live tree has ${stamp.untrackedCorpus} untracked corpus file(s) — graded as present (a snapshot of this commit would not see them)`);
    if (stamp.deletedCorpus > 0) res.notes.push(`live tree has ${stamp.deletedCorpus} tracked-but-deleted corpus file(s) — graded as absent`);
  }
  return { res, meta: { revision: stamp.head + ' (worktree)', short: stamp.short, dirty: stamp.dirty, mode: 'live' } };
}

function runSnapshot(repoDir, commit, opts) {
  const abs = path.resolve(repoDir);
  const label = opts.label || path.basename(abs);
  const rev = git(abs, ['rev-parse', commit]);
  if (rev.code !== 0) {
    return { res: { label, exit: EXIT.CNE, findings: [], notes: [`git rev-parse ${commit} failed: ${rev.err.trim()}`], stats: { files: 0, rules: {} } }, meta: { revision: commit, dirty: 0, mode: 'snapshot' } };
  }
  const full = rev.out.trim();
  const tmp = fs.mkdtempSync(path.join(os.tmpdir(), 'corpus-gate-snap-'));
  let extraction;
  try {
    const a = spawnSync('git', ['-C', abs, 'archive', commit], { maxBuffer: 1 << 30 });
    if (a.status !== 0) return { res: { label, exit: EXIT.CNE, findings: [], notes: [`git archive ${commit} failed: ${String(a.stderr).trim()}`], stats: { files: 0, rules: {} } }, meta: { revision: commit, dirty: 0, mode: 'snapshot' } };
    const t = spawnSync('tar', ['-x', '-C', tmp], { input: a.stdout, maxBuffer: 1 << 30 });
    if (t.status !== 0) return { res: { label, exit: EXIT.CNE, findings: [], notes: [`tar extraction failed: ${String(t.stderr).trim()}`], stats: { files: 0, rules: {} } }, meta: { revision: commit, dirty: 0, mode: 'snapshot' } };
    extraction = 'git archive ' + commit + ' | tar -x -C <tmp>';
    const res = gradeCorpus(tmp, { label, round: opts.round, revision: full.slice(0, 7) });
    res.notes.push(`extracted with: ${extraction}`);
    return { res, meta: { revision: full, short: full.slice(0, 7), dirty: 0, mode: 'snapshot', extract: extraction } };
  } finally {
    // temp tree removal is the gate's only cleanup
    try { fs.rmSync(tmp, { recursive: true, force: true }); } catch (e) { /* ignore */ }
  }
}

function readExpected() {
  const t = readText(EXPECTED_PATH);
  if (t === null) return null;
  try {
    return JSON.parse(t);
  } catch (e) {
    return null;
  }
}

// ---------------------------------------------------------------- selftest

const FIXTURE_README_CLEAN = [
  '# fx corpus — index',
  '',
  '## Coverage map',
  '',
  '| Entry | Covers | Sources |',
  '|---|---|---|',
  '| `knowledge/alpha.md` | the alpha surface | `cmd alpha --probe` |',
  '| `lessons/round-1.md` | round-1 method | LOG.md round-1 |',
  '| `lessons/round-8-aggregator-note.md` | aggregator round-8 note | LOG.md round-8 |',
  '',
  'Credential sweep (round 8): 0 hits (`grep -rn`; token/secret/cookie/bearer patterns).',
  '',
  '## Known gaps',
  '',
  'None.',
  '',
].join('\n');

const FIXTURE_ALPHA = [
  '# alpha',
  '',
  'The alpha surface resolves through `cmd alpha --probe`.',
  '',
  'Prose only here.',
  '',
].join('\n');

const FIXTURE_LESSON_1 = [
  '# round-1 lessons',
  '',
  'Method notes for round-1. Evidence: LOG.md round-1; commit `0abc1234`.',
  '',
].join('\n');

const FIXTURE_AGG_8 = [
  '# round-8 aggregator note',
  '',
  'Aggregator round-8 review. Evidence: LOG.md round-8; commit `0abc1234`.',
  '',
].join('\n');

// Canonical SHONEN.md, byte-identical modulo <name> (PROTOCOL.md §File contract seed block).
function fixtureShonen(name) {
  return [
    `# ${name} — Promotion checklist`,
    '',
    'Promotion to shokunin requires all of:',
    '',
    '- [ ] SKILL.md contains real decision tables, error patterns, checklists, cited sources',
    '- [ ] At least one end-to-end domain task executed and logged in LOG.md',
    '- [ ] Instructions executable by an agent without oral context',
    '- [ ] No cross-domain bleed (PROVINCE.md still accurate)',
    '',
  ].join('\n');
}

// Every fixture but fx-r10-missing carries the round-8 aggregator lesson, so that a case
// asserting a rule-8 / rule-4 / rule-2 / shonen id is not contaminated by a rule-10 id.
function baseFiles(name) {
  return {
    'SHONEN.md': fixtureShonen(name),
    'corpus/README.md': FIXTURE_README_CLEAN,
    'corpus/knowledge/alpha.md': FIXTURE_ALPHA,
    'corpus/lessons/round-1.md': FIXTURE_LESSON_1,
    'corpus/lessons/round-8-aggregator-note.md': FIXTURE_AGG_8,
  };
}

const SELFTEST_CASES = [
  { name: 'fx-clean', round: 8, files: baseFiles('fx-clean') },
  {
    name: 'fx-phantom-row', round: 8,
    files: Object.assign(baseFiles('fx-phantom-row'), {
      'corpus/README.md': FIXTURE_README_CLEAN.replace(
        '## Known gaps',
        '| `knowledge/ghost.md` | indexed but never written | `cmd ghost` |\n\n## Known gaps'),
    }),
  },
  {
    name: 'fx-cred-real', round: 8,
    files: Object.assign(baseFiles('fx-cred-real'), {
      'corpus/knowledge/beta.md': '# beta\n\nThe handler reads `op://ProdVault/ApiToken/credential` at start.\n',
    }),
  },
  {
    name: 'fx-cred-placeholder', round: 8,
    files: Object.assign(baseFiles('fx-cred-placeholder'), {
      'corpus/knowledge/beta.md': '# beta\n\nThe sweep needle is `op://vault/item/field`; cite the path, never the value.\n',
    }),
  },
  {
    name: 'fx-cred-bearer', round: 8,
    files: Object.assign(baseFiles('fx-cred-bearer'), {
      'corpus/knowledge/beta.md': '# beta\n\nA live request carried `Authorization: Bearer jt-test-pw` and was refused.\n',
    }),
  },
  {
    name: 'fx-cred-token', round: 8,
    files: Object.assign(baseFiles('fx-cred-token'), {
      'corpus/knowledge/beta.md': '# beta\n\nA synthetic sample token appears here: ghp_9f2b7c1d4e8a3065b1c9d7e2f4a60813bc5d never real.\n',
    }),
  },
  {
    name: 'fx-r4-numeral', round: 8,
    files: Object.assign(baseFiles('fx-r4-numeral'), {
      'corpus/knowledge/beta.md': '# beta\n\nThe census found 42 rows in the index.\n',
    }),
  },
  {
    name: 'fx-r2-uncited', round: 8,
    files: Object.assign(baseFiles('fx-r2-uncited'), {
      'corpus/lessons/round-3.md': '# method notes\n\nProse with no pointer of any kind.\n',
    }),
  },
  {
    name: 'fx-r10-missing', round: 8,
    files: {
      'SHONEN.md': fixtureShonen('fx-r10-missing'),
      'corpus/README.md': FIXTURE_README_CLEAN.replace(/^\| `lessons\/round-8-aggregator-note\.md`.*\n/m, ''),
      'corpus/knowledge/alpha.md': FIXTURE_ALPHA,
      'corpus/lessons/round-1.md': FIXTURE_LESSON_1,
    },
  },
  {
    name: 'fx-no-readme', round: 8,
    files: {
      'SHONEN.md': fixtureShonen('fx-no-readme'),
      'corpus/knowledge/alpha.md': FIXTURE_ALPHA,
      'corpus/lessons/round-1.md': FIXTURE_LESSON_1,
      'corpus/lessons/round-8-aggregator-note.md': FIXTURE_AGG_8,
    },
  },
  {
    name: 'fx-shonen-dev', round: 8,
    files: Object.assign(baseFiles('fx-shonen-dev'), {
      // Fleet-shaped box-3 defect: an [x] mark line with no verifier-id (one file-level
      // deviation), plus one prose line outside any box.
      'SHONEN.md': [
        '# fx-shonen-dev — Promotion checklist',
        '',
        'Promotion to shokunin requires all of:',
        '',
        '- [ ] SKILL.md contains real decision tables, error patterns, checklists, cited sources',
        '- [ ] At least one end-to-end domain task executed and logged in LOG.md',
        '- [x] Instructions executable by an agent without oral context',
        '  evidence: pointer to a runnable recipe',
        '- [ ] No cross-domain bleed (PROVINCE.md still accurate)',
        'Verifier note: prose outside any box.',
        '',
      ].join('\n'),
    }),
  },
  { name: 'fx-no-corpus', round: 8, files: { 'notes.txt': 'no corpus here\n', 'SHONEN.md': fixtureShonen('fx-no-corpus') } },
];

function buildFixture(root, files) {
  for (const rel of Object.keys(files)) {
    const p = path.join(root, rel);
    fs.mkdirSync(path.dirname(p), { recursive: true });
    fs.writeFileSync(p, files[rel]);
  }
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
    const tmp = fs.mkdtempSync(path.join(os.tmpdir(), 'corpus-gate-fx-'));
    let got;
    try {
      buildFixture(tmp, c.files);
      got = gradeCorpus(tmp, { label: c.name, round: c.round });
    } finally {
      try { fs.rmSync(tmp, { recursive: true, force: true }); } catch (e) { /* ignore */ }
    }
    const ids = got.findings.map((f) => f.id);
    const expIds = exp ? exp.expect_findings : null;
    const exitOk = exp && exp.exit === got.exit;
    const idsOk = exp && Array.isArray(expIds) && JSON.stringify(expIds) === JSON.stringify(ids);
    if (exitOk && idsOk) {
      pass++;
      process.stdout.write(`# selftest ${c.name} expect_exit=${exp.exit} got_exit=${got.exit} ids=${ids.length} PASS\n`);
    } else {
      failures.push(c.name);
      process.stdout.write(`# selftest ${c.name} FAIL expect_exit=${exp ? exp.exit : 'ABSENT'} got_exit=${got.exit}\n`);
      process.stdout.write(`#   expect_ids=${JSON.stringify(expIds)} got_ids=${JSON.stringify(ids)}\n`);
      if (exp && exp.exit !== got.exit) process.stdout.write(`#   exit mismatch: expected ${exp.exit}, got ${got.exit}\n`);
    }
  }
  const missing = expected.selftest.cases.map((c) => c.name).filter((n) => !SELFTEST_CASES.some((c) => c.name === n));
  if (missing.length) process.stdout.write(`# selftest note: expected.json declares case(s) with no fixture: ${missing.join(', ')}\n`);
  process.stdout.write(`# selftest tally ${pass}/${SELFTEST_CASES.length} ${pass === SELFTEST_CASES.length ? 'PASS' : 'FAIL'} (fixtures under os.tmpdir(), live tree untouched)\n`);
  process.exit(pass === SELFTEST_CASES.length ? EXIT.CLEAN : EXIT.FAILED);
}

// ---------------------------------------------------------------- main

function parseArgs(argv) {
  const o = { mode: null, repo: null, commit: null, round: 9, json: false, registry: false, label: null, repos: null };
  for (let i = 0; i < argv.length; i++) {
    const a = argv[i];
    if (a === '--selftest') o.mode = 'selftest';
    else if (a === '--all') o.mode = 'all';
    else if (a === '--json') o.json = true;
    else if (a === '--registry') o.registry = true;
    else if (a === '--repo') { o.mode = 'repo'; o.repo = argv[++i]; }
    else if (a.startsWith('--repo=')) { o.mode = 'repo'; o.repo = a.slice(7); }
    else if (a === '--snapshot') { o.mode = 'snapshot'; o.repo = argv[++i]; o.commit = argv[++i]; }
    else if (a === '--round') o.round = parseInt(argv[++i], 10);
    else if (a.startsWith('--round=')) o.round = parseInt(a.slice(8), 10);
    else if (a === '--label') o.label = argv[++i];
    else if (a === '--repos') o.repos = argv[++i].split(',').map((s) => s.trim()).filter(Boolean);
    else if (a === '--help' || a === '-h') o.help = true;
    else { process.stderr.write(`corpus-gate: unknown argument ${a}\n`); o.bad = a; }
  }
  return o;
}

function printRegistry() {
  const out = [];
  out.push(`# registry name=${REGISTRY.name} kind=${REGISTRY.kind} version=${REGISTRY.version}`);
  out.push(`# registry entry-all="${REGISTRY.entry.all}"`);
  out.push(`# registry verdict-map ${Object.keys(REGISTRY.verdict_map).map((k) => k + '=' + REGISTRY.verdict_map[k]).join(' ')}`);
  out.push(`# registry verdict-precedence ${REGISTRY.verdict_precedence}`);
  out.push(`# registry selftest-flag ${REGISTRY.selftest_flag} pinned=${REGISTRY.pinned_values}`);
  out.push(`# registry write-scope ${REGISTRY.write_scope}`);
  out.push(`# registry r8-classification ${REGISTRY.r8_classification}`);
  for (const c of REGISTRY.checks) out.push(`# registry check ${c.rule} ${c.corpush} ${c.what}`);
  for (const c of REGISTRY.not_evaluated) out.push(`# registry not-evaluated ${c.rule} ${c.corpush} reason=${c.reason}`);
  if (process.env.CORPUS_GATE_REGISTRY_JSON === '1') out.push('# registry json ' + JSON.stringify(REGISTRY));
  return out;
}

function combineExit(codes) {
  for (const c of EXIT_PRECEDENCE) if (codes.indexOf(c) !== -1) return c;
  return EXIT.CLEAN;
}

function main() {
  const o = parseArgs(process.argv.slice(2));
  if (o.help || o.bad) {
    process.stdout.write('usage: corpus-gate.mjs [--selftest | --repo <dir> | --all | --snapshot <dir> <commit>] [--round N] [--json] [--registry]\n');
    process.exit(o.bad ? EXIT.CNE : EXIT.CLEAN);
  }
  if (o.mode === null) {
    process.stdout.write('corpus-gate: no mode selected\n');
    printRegistry().forEach((l) => process.stdout.write(l + '\n'));
    process.exit(EXIT.CNE);
  }
  if (o.mode === 'selftest') {
    selftest();
    return;
  }

  const head = [`# ${VERSION} — CORPUS.md rules recomputed (aggregator lane round 9), round-selector=${o.round}`];
  if (o.registry) head.push(...printRegistry());
  head.forEach((l) => process.stdout.write(l + '\n'));

  const expected = readExpected();
  const results = [];
  if (o.mode === 'repo') {
    if (!o.repo) { process.stdout.write('corpus-gate: --repo needs a directory\n'); process.exit(EXIT.CNE); }
    const r = runLive(o.repo, { round: o.round, label: o.label });
    results.push(r);
  } else if (o.mode === 'snapshot') {
    if (!o.repo || !o.commit) { process.stdout.write('corpus-gate: --snapshot needs <dir> <commit>\n'); process.exit(EXIT.CNE); }
    const r = runSnapshot(o.repo, o.commit, { round: o.round, label: o.label });
    const key = `${r.res.label}@${(r.meta.short || o.commit)}`;
    const frozen = expected && expected.frozen ? expected.frozen[key] : null;
    if (!frozen) {
      process.stdout.write(`# expect ${key} ABSENT (no committed expected verdict for this revision)\n`);
    } else {
      const ids = r.res.findings.map((f) => f.id);
      const match = frozen.exit === r.res.exit && JSON.stringify(frozen.expect_findings) === JSON.stringify(ids);
      if (match) {
        process.stdout.write(`# expect ${key} MATCH exit=${r.res.exit} ids=${ids.length}\n`);
      } else {
        process.stdout.write(`# expect ${key} DRIFT committed_exit=${frozen.exit} got_exit=${r.res.exit} committed_ids=${JSON.stringify(frozen.expect_findings)} got_ids=${JSON.stringify(ids)}\n`);
        r.res.exit = EXIT.DRIFT;
        r.res.notes.push(`frozen expectation drift against ${key} — the committed expected verdict no longer reproduces`);
      }
    }
    results.push(r);
  } else if (o.mode === 'all') {
    const repos = o.repos || DEFAULT_REPOS;
    for (const name of repos) {
      const dir = path.isAbsolute(name) ? name : path.join(MAIN_ROOT, name);
      if (!fs.existsSync(dir)) {
        results.push({ res: { label: path.basename(name), exit: EXIT.CNE, findings: [], notes: [`repo directory ${dir} absent — could not evaluate`], stats: { files: 0, rules: {} } }, meta: { revision: 'absent', dirty: -1, mode: 'live' } });
        continue;
      }
      results.push(runLive(dir, { round: o.round, label: path.basename(dir) }));
    }
  }

  for (const r of results) {
    for (const l of linesForResult(r.res, r.meta)) process.stdout.write(l + '\n');
  }
  if (o.mode === 'all') {
    for (const r of results) {
      const failedRules = RULE_ORDER.filter((x) => r.res.stats.rules[x] > 0);
      process.stdout.write(`# summary ${r.res.label} rev=${(r.meta.short || r.meta.revision)} dirty=${r.meta.dirty} exit=${r.res.exit} findings=${r.res.findings.length} rules=${failedRules.join(',') || 'none'}\n`);
    }
  }
  if (o.json) {
    process.stdout.write('# json ' + JSON.stringify(results.map((r) => ({
      repo: r.res.label,
      revision: r.meta.revision,
      dirty: r.meta.dirty,
      mode: r.meta.mode,
      exit: r.res.exit,
      findings: r.res.findings,
      notes: r.res.notes,
      stats: r.res.stats,
    }))) + '\n');
  }
  const exit = combineExit(results.map((r) => r.res.exit));
  process.stdout.write(`# process-exit ${exit} (${EXIT_CLASS[exit]})\n`);
  process.exit(exit);
}

main();