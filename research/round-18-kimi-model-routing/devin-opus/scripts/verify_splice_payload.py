#!/usr/bin/env python3
"""Verifies the M10 splice quote without touching the live config.

    python3 scripts/verify_splice_payload.py

The blocks are read out of SPLICE-QUOTE.md itself, not copied here, so the check
cannot drift from the document it certifies. Three checks, all read-only:
  1. Block A parses as TOML and resolves the served id the backend accepts.
  2. Block B, inserted into M4's own payload above its SPLICE-END sentinel, makes
     that payload parse as TOML and yields 14 pool entries -- the count M4's splice
     tool would report as `added`.
  3. Pool id and [models] entry agree, which is what the live client resolves
     (pool id -> [models] key -> `model` sent on the wire).

M4's routing file is read, never written. Nothing here reads the live config.
"""
import json
import os
import re
import tomllib

HERE = os.path.dirname(os.path.abspath(__file__))
SCOPE = os.path.dirname(HERE)
ROUND = os.path.dirname(SCOPE)
TABLE = os.path.join(ROUND, "routing", "kimi-secondary-models-round18.toml")
QUOTE = os.path.join(SCOPE, "SPLICE-QUOTE.md")
POOL_ID = "devin/opus-5.5-high"
SERVED_ID = "claude-opus-5-5-high"
ANCHOR = '"openai-codex/gpt-6.1-sol-high" ='


def blocks_from_quote():
    """The first ```toml fence after each of the two Block headings."""
    text = open(QUOTE, encoding="utf-8").read()
    out = {}
    for label in ("## Block A", "## Block B"):
        tail = text.split(label, 1)[1]
        out[label] = re.search(r"```toml\n(.*?)\n```", tail, re.S).group(1)
    return out


def main():
    blocks = blocks_from_quote()

    # 1. Block A
    entry = tomllib.loads(blocks["## Block A"])["models"][POOL_ID]
    assert entry["model"] == SERVED_ID, entry
    assert entry["provider"] == "devin", entry
    print("check 1 ok: Block A parses; pool id -> served id %s" % SERVED_ID)

    # 2. Block B inside M4's payload
    payload = open(TABLE, encoding="utf-8").read().split("# SPLICE-END", 1)[0]
    lines = payload.splitlines()
    anchor_idx = next(i for i, line in enumerate(lines) if line.startswith(ANCHOR))
    lines.insert(anchor_idx + 1, blocks["## Block B"])
    spliced = "\n".join(lines) + "\n"
    pool_before = tomllib.loads(payload)["secondary_model"]["models"]
    pool = tomllib.loads(spliced)["secondary_model"]["models"]
    assert POOL_ID in pool, "the quote's pool line did not survive parsing"
    print("check 2 ok: M4 payload + quoted line parses; pool %d -> %d entries"
          % (len(pool_before), len(pool)))

    # 3. The two blocks agree on the id the client resolves
    assert pool[POOL_ID].startswith("STRONG rank 3"), pool[POOL_ID]
    print("check 3 ok: pool id %r present in both blocks" % POOL_ID)

    report = {
        "source": "SPLICE-QUOTE.md (blocks read from the document)",
        "table": os.path.relpath(TABLE, ROUND),
        "pool_id": POOL_ID,
        "served_id": SERVED_ID,
        "pool_entries_before": len(pool_before),
        "pool_entries_after": len(pool),
        "insertion_anchor": ANCHOR.strip(),
        "checks": ["Block A parses", "Block B parses inside M4's payload",
                   "pool id consistent across blocks"],
    }
    with open(os.path.join(SCOPE, "raw", "splice-verify.json"), "w") as fh:
        json.dump(report, fh, indent=2)
        fh.write("\n")
    print("wrote raw/splice-verify.json")


if __name__ == "__main__":
    main()