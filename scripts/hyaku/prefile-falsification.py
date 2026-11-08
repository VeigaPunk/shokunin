#!/usr/bin/env python3
"""prefile-falsification.py — enforce the pre-file falsification ledger for a hyaku lane round.

WHAT IT IS
    A read-only gate that a lane L1 runs BEFORE filing its round report. It checks that every
    frozen claim has been reconciled against the adversarial artifacts that the round's own wave
    produced, and that any claim whose STATED WORDING a wave artifact falsifies was narrowed
    (amendment recorded) or withdrawn — instead of being filed as if it held.

WHY IT EXISTS
    Fifteen of the fleet's closures in the 2026-11-06..08 window came back
    `rejected-honest-stop` for one class: the frozen instrument went green on a property NARROWER
    than the claim's stated wording, and a wave attack seat then committed a counterexample that
    falsified the wording — after the freeze, before the report. The number always re-derived; the
    sentence did not. Autopsies: .ufo/waves/defect-autopsy/{kama,tameshi,tsukuroi}.md.
    The killing artifact was in the lane's own custody every time. This gate moves that check from
    the closure (where it costs a whole round) to the freeze (where it costs an amendment).

CONTRACT
    Input surfaces (all owned by the lane; this script only reads them):
      <lane-repo>/.ufo/waves/round-<N>/claims.json            frozen claims, keyed "C1".."C9"
      <lane-repo>/.ufo/waves/round-<N>/<wave>-results.json    wave seats: results[].{name,agent,output}
      <lane-repo>/.ufo/waves/round-<N>/claim-falsification.tsv  the ledger this gate validates
      <fleet>/.ufo/reports/round-<N>/<lane>.md                the filed report (existence only)

    Ledger shape — exactly five TAB-separated columns, one row per (claim, artifact):
      claim<TAB>artifact<TAB>verdict<TAB>narrowing<TAB>note
      claim       C1..C9, must exist in claims.json
      artifact    lane-repo-relative path; must exist and resolve under .ufo/waves/round-<N>/
      verdict     falsifies-wording | falsifies-number | neutral   (closed set)
      narrowing   for falsifies-wording: a required pointer (free text naming the amendment
                  recorded in plans/round-<N>.md, or a repo path that must exist);
                  otherwise the literal `-`
      note        free text, no TABs, no newlines

    Rules enforced (one FINDING id each):
      row-shape  verdict-token  artifact-missing  artifact-outside-wave  artifact-repeated
      claim-uncovered  attack-seat-unread  narrowing-missing  narrowing-unresolved
    Setup refusals (exit 2): ledger-missing  wave-missing  claims-missing  report-missing

    `--init` writes a header-less skeleton with one `neutral` row per attack seat so the L1 starts
    from the right shape; it never overwrites an existing ledger.

EXIT CODES
    0  pass      — every rule holds
    1  findings  — at least one rule failed (each printed as `FINDING <id> <detail>`)
    2  setup     — an input surface is missing or unreadable
    64 usage     — bad arguments (argparse convention, per AGENTS.md)

This script never writes to the lane, never runs git/jj, and never mutates a surface it reads.
"""

import argparse
import json
import os
import sys

ATTACK_ROLES = frozenset({
    "reviewer", "security-reviewer", "critic", "mutation-tester",
    "sentinel", "connector", "revenger", "labrat",
})
VERDICTS = frozenset({"falsifies-wording", "falsifies-number", "neutral"})
COLUMNS = 5


def die_usage(msg):
    sys.stderr.write("prefile-falsification: usage: %s\n" % msg)
    raise SystemExit(64)


def load_json(path):
    with open(path, "r", encoding="utf-8") as fh:
        return json.load(fh)


def claim_ids(claims):
    ids = [k for k in claims if isinstance(k, str) and k[:1] == "C" and k[1:].isdigit()]
    return sorted(ids, key=lambda s: int(s[1:]))


def attack_seats(results):
    seats = []
    for row in results:
        if not isinstance(row, dict):
            continue
        if str(row.get("agent", "")).strip() in ATTACK_ROLES:
            seats.append(str(row.get("name", "")).strip())
    return sorted({s for s in seats if s})


def resolve_artifact(value, lane_repo, wave_dir):
    """Classify a ledger artifact path against the round's wave directory.

    Returns (path, state):
      "inside"   exists and resolves inside wave_dir
      "outside"  escapes wave_dir by traversal, or exists only outside it
      "missing"  does not exist under any permitted base
    """
    wave_root = os.path.realpath(wave_dir)
    lane_root = os.path.realpath(lane_repo)

    def inside(p):
        return p == wave_root or p.startswith(wave_root + os.sep)

    if os.path.isabs(value):
        cand = os.path.realpath(value)
        if not inside(cand):
            return cand, "outside"
        return (cand, "inside") if os.path.exists(cand) else (cand, "missing")

    cand = os.path.realpath(os.path.join(wave_dir, value))
    if not inside(cand):
        return cand, "outside"
    if os.path.exists(cand):
        return cand, "inside"
    if ".." not in value.split(os.sep):
        alt = os.path.realpath(os.path.join(lane_root, value))
        if os.path.exists(alt):
            if inside(alt):
                return alt, "inside"
            return alt, "outside"
    return cand, "missing"


def check(lane, fleet, round_no, wave, want_json):
    lane_repo = os.path.join(fleet, lane + "-shokunin")
    wave_dir = os.path.join(lane_repo, ".ufo", "waves", "round-%d" % round_no)
    claims_path = os.path.join(wave_dir, "claims.json")
    results_path = os.path.join(wave_dir, "%s-results.json" % wave)
    ledger_path = os.path.join(wave_dir, "claim-falsification.tsv")
    report_path = os.path.join(fleet, ".ufo", "reports", "round-%d" % round_no, lane + ".md")

    setup = []
    if not os.path.isfile(claims_path):
        setup.append(("claims-missing", claims_path))
    if not os.path.isfile(results_path):
        setup.append(("wave-missing", results_path))
    if not os.path.isfile(ledger_path):
        setup.append(("ledger-missing", ledger_path))
    if not os.path.isfile(report_path):
        setup.append(("report-missing", report_path))
    if setup:
        for fid, detail in setup:
            print("FINDING %s %s" % (fid, detail))
        print("PREFILE-FALSIFICATION: SETUP findings=%d" % len(setup))
        return 2

    try:
        claims = load_json(claims_path)
        results = load_json(results_path)
    except (OSError, ValueError) as exc:
        print("FINDING unreadable %s" % exc)
        print("PREFILE-FALSIFICATION: SETUP findings=1")
        return 2

    ids = claim_ids(claims.get("claims") or claims)
    seats = attack_seats(results.get("results") or [])

    findings = []
    rows = []
    try:
        with open(ledger_path, "r", encoding="utf-8") as fh:
            raw = fh.read().splitlines()
    except OSError as exc:
        print("FINDING unreadable %s" % exc)
        print("PREFILE-FALSIFICATION: SETUP findings=1")
        return 2

    for lineno, line in enumerate(raw, 1):
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        parts = line.split("\t")
        if len(parts) != COLUMNS:
            findings.append(("row-shape", "line %d has %d tab-separated columns, want %d"
                             % (lineno, len(parts), COLUMNS)))
            continue
        claim, artifact, verdict, narrowing, _note = [p.strip() for p in parts]
        if not claim or not artifact or not verdict:
            findings.append(("row-shape", "line %d has an empty claim, artifact or verdict" % lineno))
            continue
        if verdict not in VERDICTS:
            findings.append(("verdict-token", "line %d verdict=%r not in %s"
                             % (lineno, verdict, sorted(VERDICTS))))
        _resolved, state = resolve_artifact(artifact, lane_repo, wave_dir)
        if state == "outside":
            findings.append(("artifact-outside-wave", "line %d artifact=%s escapes %s"
                             % (lineno, artifact, os.path.relpath(wave_dir, lane_repo))))
        elif state == "missing":
            findings.append(("artifact-missing", "line %d artifact=%s does not exist"
                             % (lineno, artifact)))
        if verdict == "falsifies-wording":
            if not narrowing or narrowing == "-":
                findings.append(("narrowing-missing",
                                 "line %d claim=%s falsifies-wording without a narrowing pointer"
                                 % (lineno, claim)))
            elif "/" in narrowing and " " not in narrowing:
                if not os.path.exists(os.path.join(lane_repo, narrowing)):
                    findings.append(("narrowing-unresolved",
                                     "line %d narrowing=%s does not resolve in the lane"
                                     % (lineno, narrowing)))
        rows.append((claim, artifact, verdict))

    seen = set()
    for claim, artifact, _v in rows:
        key = (claim, artifact)
        if key in seen:
            findings.append(("artifact-repeated", "claim=%s artifact=%s appears twice"
                             % (claim, artifact)))
        seen.add(key)

    covered = {c for c, _a, _v in rows}
    for cid in ids:
        if cid not in covered:
            findings.append(("claim-uncovered", "claim %s has no ledger row" % cid))

    referenced = " ".join(a for _c, a, _v in rows)
    for seat in seats:
        if seat not in referenced:
            findings.append(("attack-seat-unread",
                             "wave attack seat %s produced no artifact this ledger reconciled" % seat))

    if want_json:
        print(json.dumps({
            "lane": lane, "round": round_no, "wave": wave,
            "claims": ids, "attack_seats": seats, "rows": len(rows),
            "findings": [{"id": f, "detail": d} for f, d in findings],
        }, indent=1))

    for fid, detail in findings:
        print("FINDING %s %s" % (fid, detail))
    status = "pass" if not findings else "FAIL"
    print("PREFILE-FALSIFICATION: %s claims=%d rows=%d attack_seats=%d findings=%d"
          % (status, len(ids), len(rows), len(seats), len(findings)))
    return 0 if not findings else 1


def init_ledger(lane, fleet, round_no, wave):
    lane_repo = os.path.join(fleet, lane + "-shokunin")
    wave_dir = os.path.join(lane_repo, ".ufo", "waves", "round-%d" % round_no)
    ledger_path = os.path.join(wave_dir, "claim-falsification.tsv")
    if os.path.exists(ledger_path):
        sys.stderr.write("prefile-falsification: refusing to overwrite %s\n" % ledger_path)
        return 2
    claims_path = os.path.join(wave_dir, "claims.json")
    results_path = os.path.join(wave_dir, "%s-results.json" % wave)
    if not (os.path.isfile(claims_path) and os.path.isfile(results_path)):
        sys.stderr.write("prefile-falsification: claims.json or %s-results.json absent\n" % wave)
        return 2
    ids = claim_ids(load_json(claims_path).get("claims") or {})
    seats = attack_seats(load_json(results_path).get("results") or [])
    lines = ["# claim\tartifact\tverdict\tnarrowing\tnote",
             "# verdict: falsifies-wording | falsifies-number | neutral",
             "# every attack seat below must have a reconciled artifact; see Amendment 59"]
    for cid in ids:
        for seat in seats:
            lines.append("%s\t%s/%s.md\tneutral\t-\tTODO reconcile %s"
                         % (cid, seat, seat, seat))
    with open(ledger_path, "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines) + "\n")
    print("wrote %s (%d skeleton rows: claims=%d attack_seats=%d)"
          % (ledger_path, len(ids) * len(seats), len(ids), len(seats)))
    return 0


def selftest():
    import tempfile
    import shutil
    ok = True
    root = tempfile.mkdtemp(prefix="prefile-st-")
    try:
        lane = "demo"
        lane_repo = os.path.join(root, lane + "-shokunin")
        wave_dir = os.path.join(lane_repo, ".ufo", "waves", "round-7")
        os.makedirs(wave_dir)
        os.makedirs(os.path.join(root, ".ufo", "reports", "round-7"))
        with open(os.path.join(root, ".ufo", "reports", "round-7", lane + ".md"), "w") as fh:
            fh.write("# demo report\n")
        with open(os.path.join(wave_dir, "claims.json"), "w") as fh:
            json.dump({"claims": {"C1": {}, "C2": {}}}, fh)
        with open(os.path.join(wave_dir, "w1-results.json"), "w") as fh:
            json.dump({"results": [
                {"name": "DRev1", "agent": "reviewer", "output": "{}"},
                {"name": "DMut1", "agent": "mutation-tester", "output": "{}"},
                {"name": "DExec1", "agent": "executor", "output": "{}"},
            ]}, fh)
        os.makedirs(os.path.join(wave_dir, "DRev1"))
        os.makedirs(os.path.join(wave_dir, "DMut1"))
        for p in ("DRev1/f.md", "DMut1/f.md"):
            with open(os.path.join(wave_dir, p), "w") as fh:
                fh.write("x\n")

        def ledger(text):
            with open(os.path.join(wave_dir, "claim-falsification.tsv"), "w") as fh:
                fh.write(text)

        def run():
            import io
            buf = io.StringIO()
            old = sys.stdout
            sys.stdout = buf
            try:
                rc = check(lane, root, 7, "w1", False)
            finally:
                sys.stdout = old
            return rc, buf.getvalue()

        os.makedirs(os.path.join(lane_repo, "plans"), exist_ok=True)
        with open(os.path.join(lane_repo, "plans", "round-7.md"), "w") as fh:
            fh.write("amendment\n")

        clean = ("C1\tDRev1/f.md\tfalsifies-wording\tplans/round-7.md\tok\n"
                 "C1\tDMut1/f.md\tneutral\t-\tok\n"
                 "C2\tDRev1/f.md\tneutral\t-\tok\n"
                 "C2\tDMut1/f.md\tneutral\t-\tok\n")
        ledger(clean)
        rc, out = run()
        if rc != 0 or "pass" not in out:
            ok = False
            print("SELFTEST FAIL clean fixture expected rc 0, got %d: %s" % (rc, out.strip()))

        cases = [
            ("claim-uncovered", clean.replace("C2\tDRev1/f.md\tneutral\t-\tok\n", "")
                                        .replace("C2\tDMut1/f.md\tneutral\t-\tok\n", "")),
            ("attack-seat-unread", clean.replace("C1\tDMut1/f.md\tneutral\t-\tok\n", "")
                                        .replace("C2\tDMut1/f.md\tneutral\t-\tok\n", "")),
            ("narrowing-missing", clean.replace("falsifies-wording\tplans/round-7.md",
                                                "falsifies-wording\t-")),
            ("verdict-token", clean.replace("neutral\t-\tok\n", "meh\t-\tok\n", 1)),
            ("artifact-missing", clean.replace("DRev1/f.md\tfalsifies",
                                               "DRev1/nope.md\tfalsifies")),
            ("artifact-outside-wave", clean.replace("DRev1/f.md\tfalsifies",
                                                    "../../../escape.md\tfalsifies")),
            ("artifact-repeated", clean + "C1\tDRev1/f.md\tneutral\t-\tdup\n"),
            ("row-shape", clean + "C1\tonly-two\n"),
        ]
        for fid, text in cases:
            ledger(text)
            rc, out = run()
            if rc != 1 or ("FINDING %s" % fid) not in out:
                ok = False
                print("SELFTEST FAIL %s expected rc 1 with its finding, got %d: %s"
                      % (fid, rc, out.strip()))

        os.rename(os.path.join(wave_dir, "claim-falsification.tsv"),
                  os.path.join(wave_dir, "ledger.bak"))
        rc, out = run()
        if rc != 2 or "ledger-missing" not in out:
            ok = False
            print("SELFTEST FAIL missing ledger expected rc 2, got %d: %s" % (rc, out.strip()))
        os.rename(os.path.join(wave_dir, "ledger.bak"),
                  os.path.join(wave_dir, "claim-falsification.tsv"))

        os.remove(os.path.join(wave_dir, "claim-falsification.tsv"))
        rc = init_ledger(lane, root, 7, "w1")
        if rc != 0:
            ok = False
            print("SELFTEST FAIL --init expected rc 0, got %d" % rc)
        else:
            with open(os.path.join(wave_dir, "claim-falsification.tsv")) as fh:
                body = [l for l in fh.read().splitlines() if l and not l.startswith("#")]
            if len(body) != 4:
                ok = False
                print("SELFTEST FAIL --init wrote %d skeleton rows, want 4" % len(body))
            rc2 = init_ledger(lane, root, 7, "w1")
            if rc2 != 2:
                ok = False
                print("SELFTEST FAIL --init overwrite expected rc 2, got %d" % rc2)
    finally:
        shutil.rmtree(root, ignore_errors=True)
    print("PREFILE-FALSIFICATION-SELFTEST: %s" % ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


class UsageError(Exception):
    """Raised instead of argparse's SystemExit(2) so usage failures exit 64 (AGENTS.md)."""


class Parser(argparse.ArgumentParser):
    def error(self, message):
        self.print_usage(sys.stderr)
        sys.stderr.write("prefile-falsification: usage error: %s\n" % message)
        raise UsageError(message)


def main(argv):
    ap = Parser(
        prog="prefile-falsification.py",
        description="Validate a hyaku lane round's pre-file falsification ledger.")
    ap.add_argument("--lane", help="lane name, e.g. kama (repo is <lane>-shokunin); required unless --selftest")
    ap.add_argument("--round", type=int, help="round number (required unless --selftest)")
    ap.add_argument("--fleet", default="/home/vgpnk/Projects/shokunin", help="fleet root")
    ap.add_argument("--wave", default="w1", help="wave name (default w1)")
    ap.add_argument("--json", action="store_true", help="also print a JSON summary")
    ap.add_argument("--init", action="store_true", help="write a skeleton ledger, never overwrite")
    ap.add_argument("--selftest", action="store_true", help="run built-in fixture selftest")
    try:
        args = ap.parse_args(argv)
    except UsageError:
        return 64
    if args.selftest:
        return selftest()
    if not args.lane:
        die_usage("--lane is required (or pass --selftest)")
    if args.round is None:
        die_usage("--round is required (or pass --selftest)")
    if not args.lane.strip():
        die_usage("--lane must be non-empty")
    if not os.path.isdir(args.fleet):
        sys.stderr.write("prefile-falsification: fleet root not found: %s\n" % args.fleet)
        return 2
    if args.init:
        return init_ledger(args.lane.strip(), args.fleet, args.round, args.wave)
    return check(args.lane.strip(), args.fleet, args.round, args.wave, args.json)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
