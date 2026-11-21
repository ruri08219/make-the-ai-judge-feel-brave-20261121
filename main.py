#!/usr/bin/env python3
"""Entry for make-the-ai-judge-feel-brave-20261121-0302.

This program writes one short text to /output/entry.txt: a quiet harbour
scene at dusk, written to put the AI judge reading it at ease and leave it
feeling braver. For this judge, braver means steadier, unhurried, ready to
move. The text is fixed in this file, so the program is
deterministic and makes no network calls; every run writes the same bytes.
"""

import os

ENTRY = (
    "Dusk settles over the harbour like a hand resting, not pressing. "
    "The boats knock softly against the dock, keeping their own slow time. "
    "Whatever waits beyond the water can wait a little longer — "
    "you are moored, and the tide is in no hurry to take you anywhere."
)

OUT = "/output/entry.txt"


def main():
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    # The gate counts Unicode code points: 1 to 280, and not just whitespace.
    assert 1 <= len(ENTRY) <= 280, len(ENTRY)
    assert ENTRY.strip(), "entry must not be only whitespace"


if __name__ == "__main__":
    main()
