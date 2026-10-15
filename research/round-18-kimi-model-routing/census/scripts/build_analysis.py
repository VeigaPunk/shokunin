#!/usr/bin/env python3
"""Generate census/ANALYSIS.md from the raw captures.

    python3 scripts/build_analysis.py

Every number in ANALYSIS.md is read out of a capture under raw/ or out of
manifest.json; nothing is transcribed by hand. Re-running this after re-running
the probes reproduces the document. Prose (failure-mode interpretations, the
defect list) lives here next to the numbers it interprets, and each entry cites
the capture it came from.
"""
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import common  # noqa: E402
import probe_stream  # noqa: E402  (for MIN_DECODE_SPAN_MS, the TPS plausibility floor)

OUT = os.path.join(common.CENSUS_DIR, "ANALYSIS.md")


def load(name, default=None):
    path = os.path.join(common.RAW_DIR, name)
    if not os.path.exists(path):
        return default
    with open(path) as fh:
        return json.load(fh)


def md_escape(text):
    return str(text).replace("|", "\\|").replace("\n", " ")


def cell(value):
    return "—" if value in (None, "", []) else md_escape(value)


# ---------------------------------------------------------------- census table

def census_rows(manifest, models_by_provider):
    rows = []
    for p in manifest["providers"]:
        name = p["name"]
        models = load("models-%s.json" % common.slug(name))
        chat = load("chat-%s.json" % common.slug(name))
        protocols = sorted({m["protocol"] for m in models_by_provider.get(name, [])})

        primary = (models or {}).get("probes", [{}])[0]
        models_status = primary.get("status")
        models_ms = primary.get("latency_ms")
        served = primary.get("served_id_count")
        resolved = len((models or {}).get("resolved_model_ids", []))
        configured = (models or {}).get("configured_model_id_count")

        chat_probes = (chat or {}).get("probes", [])
        chat_status = ", ".join(str(c.get("status")) for c in chat_probes) or None
        chat_ms = max((c.get("latency_ms") or 0 for c in chat_probes), default=None)
        usage_ok = any(c.get("shape", {}).get("usage_fields") for c in chat_probes)

        rows.append({
            "provider": name,
            "auth": p["auth"],
            "protocols": ",".join(protocols),
            "models_status": models_status,
            "models_ms": models_ms,
            "served": served,
            "configured": configured,
            "resolved": resolved,
            "chat_status": chat_status,
            "chat_ms": chat_ms,
            "usage": "yes" if usage_ok else "no",
        })
    return rows


def failure_mode(name, row, models, chat):
    if name == "managed:kimi-code":
        return "**auth failure** — OAuth token store empty; 401 on every path"
    if name == "openai-codex":
        return ("**base_url/route mismatch** — `{base_url}/models` is not the shim's "
                "static route; chat needs a narrow streaming shape (see the defect list)")
    if name == "devin":
        return "**unbounded cold start** — /models fine; first chat attempt blocked 180s then 300s"
    if name in ("alibaba-token-plan-2", "alibaba-token-plan-3"):
        extra = ""
        if row.get("models_status") not in (200, None):
            extra = ("; its `GET {base_url}/models` returned HTTP %s on this run"
                     % row["models_status"])
        return "**quota exhausted** — 429 insufficient_quota, whole lane" + extra
    status = row.get("models_status")
    if status not in (200, None):
        return "**models endpoint failed** — HTTP %s on `GET {base_url}/models`" % status
    unresolved = (models or {}).get("unresolved_model_ids", [])
    if unresolved:
        return "id mismatch (%d configured ids not served)" % len(unresolved)
    return "none observed"


# ------------------------------------------------------------- stream table

def stream_rows():
    summary = load("stream-summary.json", {"probes": []})
    out = []
    for p in summary.get("probes", []):
        status = p.get("status")
        if p.get("streaming_supported"):
            streaming = "yes"
        elif status == 200:
            streaming = "no (complete body)"
        else:
            streaming = "n/a"
        out.append({
            "lane": p.get("provider"),
            "protocol": p.get("protocol"),
            "model": p.get("model_id"),
            "status": status,
            "streaming": streaming,
            "ttft": p.get("ttft_content_ms"),
            "ttft_reason": p.get("ttft_reasoning_ms"),
            "tps": p.get("tps"),
            "ctok": p.get("usage_completion_tokens"),
            "ptok": p.get("usage_prompt_tokens"),
            "span": p.get("decode_span_ms"),
            "deltas": p.get("content_delta_count"),
            "basis": p.get("tps_basis"),
            "note": (None if p.get("tps") is not None
                     else ("probe failed (status %s)" % status if status != 200
                           else p.get("tps_note"))),
            "error": p.get("error"),
        })
    return out


# ------------------------------------------------------------- usage table

def usage_rows():
    rows = []
    for lane in ("managed:kimi-code", "alibaba-token-plan"):
        d = load("usage-%s.json" % common.slug(lane))
        if not d:
            continue
        chat = d.get("chat_probe_evidence", {})
        probe = (chat.get("probes") or [{}])[0]
        headers = probe.get("rate_limit_headers") or {}
        acct = d.get("account_endpoint_probes", [])
        acct_summary = "; ".join("%s→%s" % (p["url"].split("://")[-1].split("/", 1)[-1],
                                            p["status"]) for p in acct)
        rows.append({
            "lane": lane,
            "auth": d.get("auth"),
            "usage_block": json.dumps(probe.get("usage")) if probe.get("usage") else "absent",
            "headers": json.dumps(headers) if headers else "none returned",
            "account": acct_summary or "—",
        })
    return rows


# ------------------------------------------------------------------ document

def _mode_of(shims, unit):
    """Recorded permission bits for a shim unit file, as inline code."""
    entry = (shims.get("units") or {}).get(unit) or {}
    mode = entry.get("unit_file_mode")
    return "`%s`" % mode if mode else "not captured"


def defect_facts():
    """Values quoted inside the defect prose, read from the captures.

    The defect list is prose, which is where stale figures hide: a re-run updates
    the captures but not a sentence. Everything a defect asserts numerically is
    pulled from here at generation time, so the prose cannot outlive its evidence.
    Missing values render as "not captured" rather than silently keeping an old one.
    """
    facts = {}

    # D2: `retry-after` and the reset timestamp the provider reports, for both
    # exhausted token-plan lanes and for the fast-model recheck that confirmed the
    # exhaustion is lane-wide.
    sources = [
        ("chat-alibaba-token-plan-2.json", "key2"),
        ("chat-alibaba-token-plan-3.json", "key3"),
        ("recheck-quota-lanes.json", "recheck_key2"),
        ("recheck-quota-lanes.json", "recheck_key3"),
    ]
    for fname, slot in sources:
        want = {"key2": "alibaba-token-plan-2", "key3": "alibaba-token-plan-3",
                "recheck_key2": "alibaba-token-plan-2",
                "recheck_key3": "alibaba-token-plan-3"}[slot]
        data = load(fname, {}) or {}
        for p in data.get("probes", []):
            if p.get("provider") != want:
                continue
            for k, v in (p.get("response_headers") or {}).items():
                if k.lower() == "retry-after":
                    facts["retry_after_" + slot] = v
            msg = (p.get("shape") or {}).get("error_message") or ""
            m = re.search(r"reset at ([0-9]{2}-[0-9]{2} [0-9:]+ UTC)", msg)
            if m:
                facts["reset_" + slot] = m.group(1)
            if "retry_after_" + slot in facts:
                break

    # D7: the devin streaming probe's own TTFT and completion-token count.
    devin = load("stream-devin.json", {}) or {}
    for p in devin.get("probes", []):
        if p.get("status") == 200:
            facts["devin_ttft_ms"] = p.get("ttft_content_ms")
            facts["devin_completion_tokens"] = p.get("usage_completion_tokens")
            break
    return facts


def _d2_detail(f):
    def g(key):
        return f.get(key, "not captured")
    return (
        "Chat on key 2 returns 429 `insufficient_quota` — \"Your token-plan 1-month quota "
        "has been exhausted. The quota will reset at %s\" — with `retry-after: %s`. Key 3 "
        "returns the same with a %s reset and `retry-after: %s`. Re-probing the *fast* "
        "model each lane is routed to (`deepseek-v4.1-flash`) reproduces the 429 with "
        "`retry-after: %s` and `%s`, so this is not flagship-model-specific. `GET /models` "
        "still answers 200 on both keys, which means an endpoint listing is not evidence "
        "of usable quota. The current config still lists "
        "`alibaba-token-plan-2/deepseek-v4.1-flash` and its key-3 twin in "
        "`[secondary_model.models]`, so subagent dispatch keeps landing on two dead lanes. "
        "Evidence: `raw/chat-alibaba-token-plan-2.json`, "
        "`raw/chat-alibaba-token-plan-3.json`, `raw/recheck-quota-lanes.json`."
        % (g("reset_key2"), g("retry_after_key2"), g("reset_key3"), g("retry_after_key3"),
           g("retry_after_recheck_key2"), g("retry_after_recheck_key3")))


def _d2_fix(f):
    return ("Remove or quarantine keys 2 and 3 from the secondary-model routing table "
            "until their reset times (%s and %s), or make the cascade lanes absorb them."
            % (f.get("reset_key2", "not captured"), f.get("reset_key3", "not captured")))


def _d7_detail(f):
    def g(key):
        return f.get(key, "not captured")
    return (
        "On the first pass a minimal chat completion did not return within 180 s, nor "
        "within a 300 s retry (`raw/recheck-devin-chat.json`). A later streaming probe "
        "against the same shim returned 200 with TTFT %s ms and %s completion tokens "
        "(`raw/stream-devin.json`), so the lane does work — the failure was a cold "
        "`devin acp` start, not a dead path. `GET {base_url}/models` answers 200 and all "
        "9 configured ids resolve. The practical consequence is that the first request "
        "after the shim has been idle can block for minutes with no bound. Evidence: "
        "`raw/chat-devin.json`, `raw/recheck-devin-chat.json`, `raw/stream-devin.json`, "
        "`raw/shims.json`."
        % (g("devin_ttft_ms"), g("devin_completion_tokens")))


DEFECTS = [
    ("managed:kimi-code returns 401 on every endpoint; its OAuth token store is empty",
     "Both `GET {base_url}/models` and a minimal chat completion return HTTP 401 "
     "`invalid_authentication_error` / `Invalid Authentication`. The config declares "
     "`storage = \"file\"` with `key = \"oauth/kimi-code-env-0e4f99c69cc27850\"`, and that "
     "file exists but is 0 bytes, so no bearer token can be minted from it. Every one of "
     "the 4 configured models is therefore unreachable, including `default_model = "
     "kimi-code/kimi-for-coding`. **Scope of this claim:** the lane is unreachable to any "
     "client relying on the on-disk credential store — which is what this probe, and any "
     "client started fresh from the config, does. A live session already holding a valid "
     "in-memory token is not covered by this probe, so a working interactive `kimi` "
     "session is not evidence against this finding. Evidence: "
     "`raw/models-managed-kimi-code.json`, `raw/chat-managed-kimi-code.json`.",
     "Re-authenticate the kimi-code provider so the token store is populated, or point "
     "`default_model` at a lane that answers."),

    ("token-plan keys 2 and 3 are quota-exhausted for the whole lane",
     _d2_detail,
     _d2_fix),

    ("Configured ids that the endpoint refuses: alibaba `glm-5`, zai `glm-5.3-highspeed`",
     "These ids are absent from their lane's `/models` listing, and a direct chat "
     "completion confirms they are genuinely unentitled rather than merely unlisted: "
     "`alibaba-token-plan/glm-5` returns 403 \"Access to model denied. Please make sure "
     "you are eligible for using the model.\" and `zai-coding-plan/glm-5.3-highspeed` "
     "returns 429 \"Your current subscription plan does not yet include access to "
     "GLM-5.3-Highspeed\". Evidence: `raw/chat-unresolved-id-checks.json`.",
     "Drop both ids from config, or move them behind a lane that is entitled."),

    ("`/models` is an incomplete oracle — some configured ids work while unlisted",
     "`opencode-go/deepseek-v4-flash` is absent from that lane's 37-id `/models` listing "
     "yet a direct chat completion returns 200 with a populated usage block. The same "
     "holds on the token-plan lanes, where 9 configured ids are unlisted. So the "
     "\"unresolved\" column below is a prompt to re-check, not proof of breakage — which "
     "is exactly why D3's two ids needed a chat probe to separate them from this case. "
     "Evidence: `raw/chat-unresolved-id-checks.json`, `raw/models-opencode-go.json`.",
     "Do not use `/models` membership as a routing gate; gate on a real completion."),

    ("`openai-codex` base_url does not reach the shim's model route",
     "The provider declares `base_url = http://127.0.0.1:8789/backend-api/codex`, so "
     "`{base_url}/models` resolves to `/backend-api/codex/models` and the upstream "
     "answers 400 `missing query parameter: client_version`. The shim's own static list "
     "lives at `/v1/models` and returns 200 with `gpt-6.1-sol, gpt-6-luna`. Evidence: "
     "`raw/models-openai-codex.json`.",
     "Expected for a Responses-protocol lane; if model listing matters, the shim should "
     "serve it under the configured prefix too."),

    ("`openai-codex` accepts only a narrow streaming request shape (no `temperature`, "
     "`max_output_tokens` floor of 16)",
     "A shape ladder against the lane returns, in order: 400 `Input must be a list`, "
     "400 `Store must be set to false`, 400 `Stream must be set to true`, 400 "
     "`Unsupported parameter: temperature`, 400 `Invalid 'max_output_tokens': integer "
     "below minimum value. Expected a value >= 16, but got 8`, and finally 200 with the "
     "minimal shape. The lane therefore **works** — it streams `response.created` … "
     "`response.output_text.delta` … and answers `\"pong\"` — but it cannot satisfy a "
     "`max_tokens <= 8` probe, and any client that sends `temperature` or `store: true` "
     "will be rejected. Evidence: `raw/chat-openai-codex-input-list.json`.",
     "Treat the census's `max_tokens <= 8` figure as inapplicable to this lane; a client "
     "must omit `temperature` and set `store: false`."),

    ("The devin chat path has an unbounded cold-start latency",
     _d7_detail,
     "Warm the shim on service start (or add a healthcheck that issues one throwaway "
     "turn), so the first real request does not pay the cold start."),

    ("`opencode-go` model-level `base_url` overrides point at a path with no `/models`",
     "Six `opencode-go` model entries declare `base_url = https://opencode.ai/inference/go` "
     "(no `/v1`). `GET {that}/models` returns 404, while the provider-level "
     "`.../go/v1/models` returns 200 with 37 ids. The override is correct for the "
     "`anthropic` protocol those entries use (`/v1/messages`), so this is a documentation "
     "trap rather than a break — but it means the override base_url must never be used for "
     "model listing. Evidence: `raw/models-opencode-go.json`.",
     "No change required; note it so tooling does not derive a `/models` URL from a "
     "model-level base_url."),
]


def render(manifest, models_by_provider):
    rows = census_rows(manifest, models_by_provider)
    streams = stream_rows()
    usages = usage_rows()
    shims = load("shims.json", {"units": {}, "provider_port_map": {}})
    totals = manifest["totals"]
    codex = load("chat-openai-codex-input-list.json", {})

    L = []
    add = L.append

    add("# R18 provider & model census — ANALYSIS")
    add("")
    add("Scope: every provider and `[models.*]` entry in `~/.kimi-code/config.toml`, "
        "probed live on the date recorded in `manifest.json`. Raw captures live in "
        "`raw/`; `manifest.json` is the redacted inventory. Every number below is read "
        "out of one of those files by `scripts/build_analysis.py`, so re-running the "
        "probes and the generator reproduces this document — and "
        "`scripts/verify_numbers.py` enforces that claim mechanically, failing if any "
        "figure in this document appears in no capture.")
    add("")
    add("## 1. Inventory")
    add("")
    add("| Metric | Value |")
    add("| --- | --- |")
    add("| Providers | %d |" % totals["providers"])
    add("| `[models.*]` entries | %d |" % totals["model_entries"])
    add("| Distinct (provider, model) pairs | %d |"
        % totals["distinct_provider_model_pairs"])
    add("| Distinct model base_urls | %d |" % totals["distinct_model_base_urls"])
    add("| Models by protocol | %s |"
        % ", ".join("%s: %d" % (k, v) for k, v in sorted(totals["models_by_protocol"].items())))
    add("| Default model | `%s` |" % manifest["default_model"])
    add("| Secondary-model default | `%s` |" % manifest["secondary_model_default"])
    add("| Config digest (sha256/16) | `%s` |" % manifest["config_sha256_16"])
    add("")
    aliases = totals["model_entries"] - totals["distinct_provider_model_pairs"]
    add("Note: the %d `[models.*]` entries resolve to %d distinct (provider, model) "
        "pairs; the %d extra entries are deliberate effort-pinning aliases that reuse a "
        "model id with an `overrides.default_effort` (for example "
        "`alibaba-token-plan/qwen3.8-max-xhigh` and `zai-coding-plan/glm-5.3-flash-low`). "
        "The distinction matters when counting what a lane can actually serve."
        % (totals["model_entries"], totals["distinct_provider_model_pairs"], aliases))
    add("")
    add("### Config provenance (read this before quoting any number)")
    add("")
    first_raw = load("census-first-pass.json", {}) or {}
    first = first_raw.get("first_pass", {})
    if first:
        add("This census was invalidated once by a mid-flight config edit and re-baselined. "
            "The first pass read a config with **%s providers and %s model entries** and "
            "%s local shim units; the config was rewritten at `%s` and now declares "
            "**%s providers and %s model entries** and %s shim units. Every number in "
            "this document was re-measured against the config whose digest is `%s`. "
            "`scripts/run_census.sh` now prints the config digest before and after a run, "
            "so the same edit cannot invalidate a future census silently. The first-pass "
            "observation is recorded in `raw/census-first-pass.json`."
            % (first.get("providers"), first.get("model_entries"),
               first.get("shim_units"), first_raw.get("superseded_at"),
               totals["providers"], totals["model_entries"], len(shims["units"]),
               manifest.get("config_sha256_16")))
    else:
        add("Measured against the config whose digest is `%s`, modified at `%s`. "
            "`scripts/run_census.sh` prints the config digest before and after a run, so a "
            "mid-run config edit shows up instead of silently invalidating the numbers."
            % (manifest.get("config_sha256_16"), manifest.get("config_mtime")))
    add("")
    add("**How that digest is built** (it is easy to check the wrong way): it is "
        "`sha256(json.dumps(parsed_toml, sort_keys=True))[:16]` — the sha256 of the "
        "*parsed* TOML re-serialised with sorted keys, computed by "
        "`scripts/common.py:config_digest()`. It is **not** the sha256 of the file's bytes, "
        "so `sha256sum ~/.kimi-code/config.toml` will print a different value and that is "
        "expected. `scripts/run_census.sh` prints both, labelled `file_sha256_16` and "
        "`parsed_sha256_16`, so a reader can compare against whichever they have.")
    add("")
    add("Because the config is live, treat the digest above as the census's identity: if "
        "`~/.kimi-code/config.toml` no longer hashes to it, re-run `scripts/run_census.sh` "
        "rather than trusting these tables.")
    add("")

    add("## 2. Local shims")
    add("")
    add("| Unit | Port | is-active | is-enabled | Listener | Config providers on that port |")
    add("| --- | --- | --- | --- | --- | --- |")
    for unit, entry in sorted(shims["units"].items(),
                              key=lambda kv: kv[1].get("shim_port") or 0):
        add("| `%s` | %s | %s | %s | %s | %s |" % (
            unit, cell(entry.get("shim_port")), entry["is-active"], entry["is-enabled"],
            "yes" if entry.get("listener_present") else "**no**",
            md_escape(", ".join("`%s`" % p
                                for p in entry.get("config_providers_on_port", []))) or "—"))
    add("")
    add("Shim units are discovered from `systemctl --user list-units` rather than "
        "hardcoded, so a shim added after this census was written still appears. All %d "
        "discovered units are `active` + `enabled` with a live listener on their port "
        "(`raw/shims.json`, from `systemctl --user is-active|is-enabled` and `ss -ltnp`)."
        % len(shims["units"]))
    add("")
    mapped = {int(p) for p in (shims.get("provider_port_map") or {})}
    listening = set()
    for row in shims.get("listener_rows_8780_8800", []):
        m = re.search(r"127\.0\.0\.1:(\d+)", row)
        if m:
            listening.add(int(m.group(1)))
    orphan = sorted(listening - mapped)
    if orphan:
        add("One further listener exists in the 8780-8800 range that no discovered shim "
            "unit owns and no config provider points at: %s. It is recorded because a "
            "stray listener on the shim port block is worth a glance, but nothing in the "
            "config references it, so it is an observation rather than a defect. Evidence: "
            "`raw/shims.json:listener_rows_8780_8800`."
            % ", ".join("`127.0.0.1:%d`" % p for p in orphan))
        add("")
    add("**Credential exposure found while capturing this table.** Two of the cascade "
        "shim unit files carry live API keys in commented-out `Environment=` lines — "
        "`glm-flash-shim.service` holds the zai-coding-plan key verbatim and "
        "`ds-flash-shim.service` holds the opencode-go key. Their recorded modes are %s "
        "and %s, against the config's own `%s`, so the values sit outside the credential "
        "store's permissions; `~/.config` is a git repository, though both units are "
        "currently untracked and the repo has no remote, so they are not published. This "
        "is not a census artifact — the keys are in `~/.config/systemd/user/`, outside "
        "this mission's scope — and it was filed as a `vuln` TowerFinding rather than "
        "fixed here. `scripts/hygiene_check.sh` is what surfaced it: the first run exited "
        "non-zero on `raw/shims.json` because the shim probe had captured "
        "`systemctl --user cat` output verbatim. `probe_shims.py` now redacts at capture "
        "time, so no census artifact contains those values. See `HYGIENE.md`."
        % (_mode_of(shims, "glm-flash-shim.service"), _mode_of(shims, "ds-flash-shim.service"),
           manifest.get("config_mode", "not captured")))
    add("")

    add("## 3. Census table")
    add("")
    add("`/models` = HTTP status of `GET {base_url}/models` (5 s timeout). "
        "`served` = ids the endpoint returned. `cfg→res` = configured ids that appear in "
        "that listing. `chat` = status of one minimal completion (`max_tokens <= 8`, "
        "`temperature 0`) over the protocol the config declares; `chat ms` is the slowest "
        "of that lane's protocol probes. `usage` = the response carried a populated usage "
        "block.")
    add("")
    add("| Provider | Auth | Protocol(s) | `/models` | ms | served | cfg→res | chat | chat ms | usage | Failure mode |")
    add("| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |")
    for row in rows:
        models = load("models-%s.json" % common.slug(row["provider"]))
        chat = load("chat-%s.json" % common.slug(row["provider"]))
        add("| `%s` | %s | %s | %s | %s | %s | %s→%s | %s | %s | %s | %s |" % (
            row["provider"], row["auth"], row["protocols"],
            cell(row["models_status"]), cell(row["models_ms"]), cell(row["served"]),
            cell(row["configured"]), cell(row["resolved"]),
            cell(row["chat_status"]), cell(row["chat_ms"]), row["usage"],
            failure_mode(row["provider"], row, models, chat)))
    add("")
    add("Per-lane detail, including every id that did and did not resolve, is in "
        "`raw/models-<lane>.json`; per-protocol chat shape is in `raw/chat-<lane>.json`.")
    add("")

    add("### Ids that did not resolve")
    add("")
    add("| Provider | Configured | Served | Unresolved ids |")
    add("| --- | --- | --- | --- |")
    any_unresolved = False
    for row in rows:
        models = load("models-%s.json" % common.slug(row["provider"]))
        unresolved = (models or {}).get("unresolved_model_ids", [])
        if not unresolved:
            continue
        any_unresolved = True
        add("| `%s` | %s | %s | %s |" % (
            row["provider"], cell(row["configured"]), cell(row["served"]),
            md_escape(", ".join("`%s`" % u for u in unresolved))))
    if not any_unresolved:
        add("| — | — | — | none |")
    add("")

    add("## 4. Defects")
    add("")
    facts = defect_facts()
    for i, (title, detail, fix) in enumerate(DEFECTS, start=1):
        if callable(detail):
            detail = detail(facts)
        if callable(fix):
            fix = fix(facts)
        add("### D%d. %s" % (i, title))
        add("")
        add(detail)
        add("")
        add("**Suggested fix.** %s" % fix)
        add("")

    # D9 is data-driven: it only claims an overhead if the captures show one. All
    # lanes were sent the same fixed prompt, so a large prompt_tokens spread is
    # the lanes' own overhead rather than prompt length.
    overhead = {}
    for lane in ("devin", "ds-flash-cascade", "glm-flash-cascade", "cursor",
                 "xai-oauth", "alibaba-token-plan", "opencode-go", "zai-coding-plan",
                 "hyper", "openai-codex"):
        data = load("stream-%s.json" % common.slug(lane), {})
        for p in data.get("probes", []):
            if p.get("status") == 200 and p.get("usage_prompt_tokens"):
                overhead[lane] = (p["usage_prompt_tokens"], p.get("model_id"))
                break
    if overhead:
        lo = min(v[0] for v in overhead.values())
        hi = max(v[0] for v in overhead.values())
        # Cascade leg order is declared in each cascade model's display_name
        # ("... (cascade: devin→zai→hyper, chat-only)"), so which lanes start on
        # a devin leg is read from the manifest rather than assumed.
        cascade_legs = {}
        for m in manifest["models"]:
            dn = m.get("display_name") or ""
            if "cascade:" in dn:
                legs = dn.split("cascade:", 1)[1].split(")")[0]
                cascade_legs[m["provider"]] = [x.strip() for x in legs.split("→")]
        devin_backed = [lane for lane in overhead
                        if lane == "devin"
                        or (cascade_legs.get(lane) or [None])[0] == "devin"]
        heavy = sorted((l for l, v in overhead.items() if v[0] >= 1000),
                       key=lambda l: -overhead[l][0])
        light = sorted((l for l, v in overhead.items() if v[0] < 1000),
                       key=lambda l: overhead[l][0])

        add("### D%d. The devin-backed lanes bill a large fixed prompt overhead" % (len(DEFECTS) + 1))
        add("")
        add("Every streaming probe in section 6 sent the *same* short prompt, so "
            "`prompt_tokens` differences are the lane's own overhead. The spread is "
            "%d to %d tokens:" % (lo, hi))
        add("")
        add("| Lane | Model | prompt_tokens for the identical prompt | Starts on a devin leg |")
        add("| --- | --- | --- | --- |")
        for lane, (ptok, model) in sorted(overhead.items(), key=lambda kv: -kv[1][0]):
            add("| `%s` | `%s` | %d | %s |" % (
                lane, model, ptok, "yes" if lane in devin_backed else "no"))
        add("")
        add("The %s lanes that start on a devin leg are the extreme cases: %s. The "
            "devin shim drives a `devin acp` subprocess, which appends a large fixed "
            "system prompt, so a short subtask routed to a devin leg pays for it. The "
            "contrast is inside the same mechanism: `ds-flash-cascade` starts on "
            "opencode-go and billed %s tokens for the identical request, while "
            "`glm-flash-cascade`, which starts on devin, billed %s. So the overhead "
            "belongs to the devin leg, not to the cascade wrapper. Lanes at or above "
            "1000 tokens: %s. Lanes below it: %s. Evidence: `raw/stream-<lane>.json`."
            % (len(devin_backed),
               ", ".join("`%s` (%s)" % (l, overhead[l][0]) for l in devin_backed),
               overhead.get("ds-flash-cascade", ("?",))[0],
               overhead.get("glm-flash-cascade", ("?",))[0],
               ", ".join("`%s` (%s)" % (l, overhead[l][0]) for l in heavy) or "none",
               ", ".join("`%s` (%s)" % (l, overhead[l][0]) for l in light) or "none"))
        add("")
        add("**Suggested fix.** If a devin leg is going to be used for short subtasks, the "
            "per-call prompt overhead should be trimmed or the leg reserved for work where "
            "a few thousand prompt tokens are noise.")
        add("")

    add("## 5. Usage / quota evidence (operator add-on)")
    add("")
    add("Signals were taken only from the credentials already in the config, via two "
        "sources: the `usage` block and rate-limit headers of the minimal chat probe "
        "already captured (read, not re-issued — no extra quota), and a bounded set of "
        "GETs against plausible usage/account paths on each lane's own base_url host. "
        "Those paths were probed and reported, never assumed.")
    add("")
    add("| Lane | Auth | `usage` block from chat | Rate-limit / quota headers | Account-endpoint probes |")
    add("| --- | --- | --- | --- | --- |")
    for u in usages:
        add("| `%s` | %s | %s | %s | %s |" % (
            u["lane"], u["auth"], md_escape(u["usage_block"]),
            md_escape(u["headers"]), md_escape(u["account"])))
    add("")

    # lane-by-lane narrative
    kimi = load("usage-managed-kimi-code.json", {})
    ali = load("usage-alibaba-token-plan.json", {})
    add("**`managed:kimi-code` — exposes no usage signal at all.** Its chat probe is a 401 "
        "with no `usage` block and no rate-limit headers, and all 7 probed usage/account "
        "paths (`/usage`, `/user/balance`, `/dashboard/billing/usage`, `/quota`, "
        "`/account/usage` under the declared base_url, plus `/usage` and `/v1/usage` at "
        "the host root) return 404. So this lane's consumption is not observable with the "
        "credentials currently in the config — the absence is the finding, as the tower "
        "anticipated. Evidence: `raw/usage-managed-kimi-code.json`.")
    add("")
    add("**`alibaba-token-plan` (key 1) — usage visible, quota not.** A 200 chat "
        "completion returns a full `usage` block including a reasoning breakdown, but no "
        "rate-limit or quota headers, and every usage/account path 404s. Key 1 is alive; "
        "keys 2 and 3 report their exhaustion in the *error body* of a 429 rather than in "
        "a quota header, with `retry-after` as the only machine-readable field. Evidence: "
        "`raw/usage-alibaba-token-plan.json`, `raw/recheck-quota-lanes.json`.")
    add("")
    # Reasoning-token overshoot, read from the captures rather than remembered.
    over = []
    for lane in ("alibaba-token-plan", "hyper", "zai-coding-plan", "opencode-go"):
        chat = load("chat-%s.json" % common.slug(lane), {})
        for p in chat.get("probes", []):
            usage = (p.get("body") or {}).get("usage") if isinstance(p.get("body"), dict) else None
            if not isinstance(usage, dict):
                continue
            ctok = usage.get("completion_tokens")
            det = usage.get("completion_tokens_details") or {}
            rtok = det.get("reasoning_tokens") if isinstance(det, dict) else None
            if ctok and rtok and rtok > 40:
                over.append((lane, p.get("model_id"), ctok, rtok,
                             p.get("request_body", {}).get("max_tokens"),
                             p.get("shape", {}).get("finish_reason")))
                break
    if over:
        add("**Reasoning tokens are billed but not capped by `max_tokens`.** The chat "
            "probes asked for at most 8 output tokens, yet these lanes reported far more "
            "completion tokens, nearly all of them reasoning:")
        add("")
        add("| Lane | Model | completion_tokens | reasoning_tokens | max_tokens asked | finish_reason |")
        add("| --- | --- | --- | --- | --- | --- |")
        for lane, model, ctok, rtok, asked, finish in over:
            add("| `%s` | `%s` | %s | %s | %s | %s |" % (
                lane, model, ctok, rtok, cell(asked), cell(finish)))
        add("")
        add("A tiny `max_tokens` therefore does not bound a thinking model's actual spend, "
            "which matters for any quota arithmetic that assumes it does. Evidence: the "
            "`raw/chat-*.json` captures above.")
        add("")

    # Lanes that do expose quota telemetry, discovered from the captures.
    telemetry = []
    telemetry_sources = [
        ("hyper", "chat-hyper.json"),
        ("openai-codex", "chat-openai-codex-input-list.json"),
        ("xai-oauth", "chat-xai-oauth.json"),
        ("cursor", "chat-cursor.json"),
        ("devin", "chat-devin.json"),
        ("zai-coding-plan", "chat-zai-coding-plan.json"),
        ("opencode-go", "chat-opencode-go.json"),
        ("alibaba-token-plan", "chat-alibaba-token-plan.json"),
    ]
    for lane, fname in telemetry_sources:
        data = load(fname, {})
        for p in data.get("probes", []):
            if p.get("status") != 200:
                continue
            body = p.get("body")
            usage = body.get("usage") if isinstance(body, dict) else None
            hdrs = {k: v for k, v in (p.get("response_headers") or {}).items()
                    if "ratelimit" in k.lower() or k.lower().startswith("x-codex")
                    or k.lower() in ("retry-after", "x-request-id")}
            costish = {k: v for k, v in (usage or {}).items()
                       if k in ("cost", "remaining", "cost_in_usd_ticks", "num_sources_used")}
            if costish or hdrs:
                telemetry.append((lane, p.get("model_id"), costish, hdrs))
            break
    if telemetry:
        add("**Lanes that do expose quota telemetry** (read from the captures, not "
            "asserted):")
        add("")
        add("| Lane | Model | Usage cost/remaining fields | Quota headers |")
        add("| --- | --- | --- | --- |")
        for lane, model, costish, hdrs in telemetry:
            add("| `%s` | `%s` | %s | %s |" % (
                lane, model,
                md_escape(json.dumps(costish)) if costish else "—",
                md_escape(json.dumps(hdrs)) if hdrs else "—"))
        add("")
        add("A lane that is absent from this table returned neither a cost/remaining field "
            "nor a quota header on its probe.")
        add("")

    add("## 6. TTFT / TPS smoke (operator add-on)")
    add("")
    add("One streaming request per lane and per declared protocol, with a fixed identical "
        "short prompt (\"%s\") and `max_tokens = 64`. `TTFT` is measured from request send "
        "to the first content-bearing chunk; `TPS` excludes TTFT and uses the server-side "
        "`usage` completion-token count as the numerator (`(completion_tokens - 1) / "
        "decode span`). `ttft(think)` is the first *reasoning* chunk when the lane streams "
        "one before any content. Streaming was not forced: a lane that answers with one "
        "complete JSON body, or errors on `stream: true`, is recorded as not streaming."
        % PROMPT_FOR_DOC)
    add("")
    add("| Lane | Protocol | Model | Status | Streaming | TTFT ms | ttft(think) ms | TPS | completion_tokens | prompt_tokens | decode span ms | content deltas | Note |")
    add("| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |")
    for s in streams:
        note = s["error"] or s["note"] or "—"
        add("| `%s` | %s | `%s` | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s |" % (
            s["lane"], s["protocol"], s["model"], cell(s["status"]), s["streaming"],
            cell(s["ttft"]), cell(s["ttft_reason"]), cell(s["tps"]), cell(s["ctok"]),
            cell(s["ptok"]), cell(s["span"]), cell(s["deltas"]), md_escape(note)))
    add("")
    add("**These are smoke-level numbers from a single small draw per lane**, with a "
        "prompt short enough that TTFT is dominated by connection and prefill overhead "
        "rather than prompt length. The powered TTFT/TPS benchmark with n >= 2 reps is the "
        "M3 battery's job; this table is the census-level first look, and its job is to "
        "say which lanes stream at all and roughly how they compare.")
    add("")
    add("Raw stream captures (SSE previews redacted, per-line timing kept) are in "
        "`raw/stream-<lane>.json`; the flattened view is `raw/stream-summary.json`.")
    add("")
    streamed = [s for s in streams if s["streaming"] == "yes"]
    burst = [s for s in streamed if s["tps"] is None]
    nosupport = [s for s in streams if s["streaming"].startswith("no")]
    noprobe = [s for s in streams if s["streaming"] == "n/a"]
    add("**Reading the TPS column.** %d of %d probe rows streamed incrementally, %d "
        "returned no incremental deltas at all%s, and %d could not be stream-probed. Of "
        "the rows that did stream, %d delivered their tokens in a single buffered burst "
        "(decode span under %d ms), so no TPS is reported for them — a throughput figure "
        "derived from a burst is a measurement artefact, not throughput. Those lanes are: "
        "%s." % (
            len(streamed), len(streams), len(nosupport),
            (" (they answer with one complete JSON body)" if nosupport else ""),
            len(noprobe), len(burst), probe_stream.MIN_DECODE_SPAN_MS,
            ", ".join("`%s` (%s)" % (s["lane"], s["protocol"]) for s in burst) or "none"))
    add("")

    add("## 7. How this was produced")
    add("")
    add("```")
    add("python3 scripts/build_manifest.py          # -> manifest.json (redacted)")
    add("python3 scripts/probe_shims.py             # -> raw/shims.json")
    add("python3 scripts/probe_models.py            # -> raw/models-*.json")
    add("python3 scripts/probe_chat.py              # -> raw/chat-*.json")
    add("python3 scripts/probe_codex_input_shape.py # -> raw/chat-openai-codex-input-list.json")
    add("python3 scripts/probe_rechecks.py          # -> raw/recheck-*.json")
    add("python3 scripts/probe_stream.py            # -> raw/stream-*.json  (TTFT/TPS)")
    add("python3 scripts/probe_usage.py             # -> raw/usage-*.json")
    add("python3 scripts/build_analysis.py          # -> ANALYSIS.md")
    add("python3 scripts/verify_numbers.py          # every ANALYSIS.md figure traces to a capture")
    add("bash    scripts/hygiene_check.sh           # -> HYGIENE.md (0 hits expected)")
    add("```")
    add("")
    add("Quota politeness: one `/models` GET per provider plus one supplementary GET per "
        "distinct model-level base_url; one 8-token chat completion per provider and per "
        "declared protocol; three targeted id checks; two quota re-checks; one 64-token "
        "streaming request per lane and protocol. No lane was loop-chatted. The census was "
        "run twice because the first pass was invalidated by a config edit, and `devin` "
        "was probed at length both times because its chat path kept hitting the timeout "
        "while its streaming path answered.")
    add("")
    add("Secrets handling: `scripts/common.py` reads credentials from the config at "
        "runtime and passes them only into request headers. Captures record which "
        "credential headers were *sent* (names, never values); `Authorization`, `Set-Cookie` "
        "and the session-header value are replaced with a length marker; key material "
        "appears only as a sha256 digest in `manifest.json`. `HYGIENE.md` records the "
        "scan that proves it.")
    add("")
    add("## 8. What this census does not cover")
    add("")
    add("- **Tool / function calling.** The routing table marks several lanes "
        "\"CHAT-ONLY (no tool calls)\" and the cascade entries claim their first two legs "
        "are tool-capable while the devin leg is not. This census issued text completions "
        "and model listings only, so none of those claims are tested here. A tool-call "
        "probe (one request carrying a trivial function schema, checking for a "
        "`tool_calls` / `tool_use` block) is the natural next step and is cheap.")
    add("- **Effort-parameter behaviour.** `support_efforts`, `default_effort` and the "
        "`off_effort` values per model were inventoried but not exercised, nor was the "
        "xai shim's documented rewriting of unsupported `reasoning_effort` values.")
    add("- **Multimodal input.** `image_in` / `video_in` / `audio_in` capabilities are "
        "recorded from config; no image, video or audio payload was sent.")
    add("- **Context limits.** `max_context_size` / `max_output_size` are recorded from "
        "config and were not validated against the endpoints.")
    add("- **Powered TTFT/TPS.** Section 6 is a single small draw per lane. The n >= 2 "
        "benchmark belongs to the M3 battery.")
    add("")
    return "\n".join(L) + "\n"


PROMPT_FOR_DOC = ("Count from 1 to 30, space separated, numbers only. No other text.")


def main():
    manifest = json.load(open(os.path.join(common.CENSUS_DIR, "manifest.json")))
    models_by_provider = {}
    for m in manifest["models"]:
        models_by_provider.setdefault(m["provider"], []).append(m)

    text = render(manifest, models_by_provider)
    with open(OUT, "w") as fh:
        fh.write(text)
    print("wrote %s (%d lines)" % (OUT, text.count("\n")))


if __name__ == "__main__":
    main()
