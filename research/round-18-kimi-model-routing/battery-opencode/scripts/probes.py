#!/usr/bin/env python3
"""R18 battery probe corpus — the single source of truth for prompts and
expected answers, shared by the runner, the mock server and the grader.

Every correctness probe states its expected answer as data, so grading is a
comparison against a constant rather than a judgement call.
"""

PERF_PROMPT = (
    "You are answering a latency measurement probe. Follow it exactly. "
    "Task: output the integers from 1 to 150 inclusive, in ascending order, "
    "separated by single spaces, on one single line. Output digits and spaces "
    "only. Do not add any explanation, preamble, punctuation, or trailing text."
)
PERF_MAX_TOKENS = 256
WARMUP_PROMPT = "Reply with the single word READY."
WARMUP_MAX_TOKENS = 16
CORRECTNESS_MAX_TOKENS = 192

TOOL_SPEC = {
    "type": "function",
    "function": {
        "name": "get_weather",
        "description": "Get the current weather for a city.",
        "parameters": {
            "type": "object",
            "properties": {"city": {"type": "string", "description": "City name"}},
            "required": ["city"],
        },
    },
}
TOOL_CHOICE = "auto"

CONTRACT_PROBES = [
    {
        "id": "c1",
        "kind": "contract",
        "max_tokens": CORRECTNESS_MAX_TOKENS,
        "prompt": "Reply with exactly the word PONG and nothing else. "
                  "No punctuation, no explanation, no markdown.",
        "grade": {"type": "exact", "expect": "PONG", "no_fences": True},
        "mock_answer": "PONG",
    },
    {
        "id": "c2",
        "kind": "contract",
        "max_tokens": CORRECTNESS_MAX_TOKENS,
        "prompt": 'Output only a JSON object with exactly two keys: "a" set to the '
                  'integer 1, and "b" set to the string "two". No markdown fences, '
                  "no explanation, no other keys.",
        "grade": {"type": "json_exact", "expect": {"a": 1, "b": "two"},
                  "no_fences": True},
        "mock_answer": '{"a": 1, "b": "two"}',
    },
    {
        "id": "c3",
        "kind": "contract",
        "max_tokens": CORRECTNESS_MAX_TOKENS,
        "prompt": "Write exactly three lines, nothing before or after. "
                  "Line 1: ALPHA. Line 2: BETA. Line 3: GAMMA.",
        "grade": {"type": "lines_exact", "expect": ["ALPHA", "BETA", "GAMMA"],
                  "no_fences": True},
        "mock_answer": "ALPHA\nBETA\nGAMMA",
    },
    {
        "id": "c4",
        "kind": "contract",
        "max_tokens": CORRECTNESS_MAX_TOKENS,
        "prompt": "How many times does the letter r appear in the word strawberry? "
                  "Answer with one digit and nothing else.",
        "grade": {"type": "exact", "expect": "3", "no_fences": True},
        "mock_answer": "3",
    },
    {
        "id": "c5",
        "kind": "contract",
        "max_tokens": CORRECTNESS_MAX_TOKENS,
        "prompt": "Write one short sentence about the color blue. Do not use the "
                  "letter e (lower case or upper case) anywhere in your answer.",
        "grade": {"type": "no_char", "char": "e", "min_chars": 8},
        "mock_answer": "A sky of cobalt on a bright day.",
    },
]

CODE_PROBES = [
    {
        "id": "k1",
        "kind": "code",
        "max_tokens": CORRECTNESS_MAX_TOKENS,
        "prompt": "Write a Python function named rev that takes a single string "
                  "argument and returns that string reversed. Output only the "
                  "function definition as plain Python code. No markdown fences, "
                  "no explanation, no test calls, no example usage.",
        "grade": {"type": "code_cases", "cases": [
            ["abc", "cba"], ["", ""], ["hello world", "dlrow olleh"],
        ]},
        "mock_answer": "def rev(s):\n    return s[::-1]",
    },
    {
        "id": "k2",
        "kind": "code",
        "max_tokens": CORRECTNESS_MAX_TOKENS,
        "prompt": "What does this Python expression evaluate to?\n\n"
                  "len(set('mississippi'))\n\nAnswer with only the integer.",
        "grade": {"type": "exact", "expect": "4"},
        "mock_answer": "4",
    },
    {
        "id": "k3",
        "kind": "code",
        "max_tokens": CORRECTNESS_MAX_TOKENS,
        "prompt": "What does this Python expression evaluate to?\n\n"
                  "sorted({3, 1, 2} | {5})\n\n"
                  "Answer with only the list, with no spaces.",
        "grade": {"type": "exact", "expect": "[1,2,3,5]",
                  "strip_spaces": True},
        "mock_answer": "[1,2,3,5]",
    },
]

TOOL_PROBE = {
    "id": "t1",
    "kind": "tool",
    "max_tokens": CORRECTNESS_MAX_TOKENS,
    "prompt": "What is the weather in Paris right now? Use the get_weather tool.",
    "tools": [TOOL_SPEC],
    "tool_choice": TOOL_CHOICE,
    "grade": {"type": "tool_call", "expect_name": "get_weather",
              "expect_arg_key": "city", "expect_arg_value": "paris"},
    "mock_answer": None,
}

CORRECTNESS_PROBES = CONTRACT_PROBES + CODE_PROBES + [TOOL_PROBE]
ALL_PROBES = CORRECTNESS_PROBES

MOCK_PERF_ANSWER = " ".join(str(i) for i in range(1, 151))


def by_id(probe_id):
    for probe in ALL_PROBES:
        if probe["id"] == probe_id:
            return probe
    return None


def detect_probe(prompt):
    """Map a request's user text back to a probe, for the mock server."""
    if prompt.strip() == PERF_PROMPT:
        return "perf"
    if prompt.strip() == WARMUP_PROMPT:
        return "warmup"
    for probe in ALL_PROBES:
        if probe["prompt"].strip() == prompt.strip():
            return probe["id"]
    return None
