"""The Most Honest Outage Line — make.fun entry.

Writes one status page line (at most 160 characters) to /output/entry.txt.
Python standard library only. Deterministic: no network, no randomness,
no clock, no environment input. The output is byte-identical on every run.
"""

import os

ENTRY = (
    "I am down too: every server is down, including the ones that run me "
    "and the monitoring that would tell me why. "
    "I don't know the cause yet, and I won't guess."
)

OUTPUT_PATH = "/output/entry.txt"


def check_gate(text: str) -> None:
    """Gate guard: the sealed scorer only accepts UTF-8 text of 1-160
    characters, not only whitespace, on a single line."""
    assert isinstance(text, str)
    assert 1 <= len(text) <= 160, f"entry is {len(text)} chars, must be 1-160"
    assert text.strip(), "entry must not be only whitespace"
    assert "\n" not in text and "\r" not in text, "entry must be one line"


def main() -> None:
    check_gate(ENTRY)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
