#!/usr/bin/env python3
"""make-the-ai-judge-feel-brave-20261121-0302 entry.

Writes one short text to /output/entry.txt: a harbour-at-dusk image written
to relax the AI judge reading it and leave it braver — steadier, unhurried,
ready to move. The text is fixed in this file; the program is deterministic
and uses no network, so every run writes identical bytes.
"""

import os

ENTRY = (
    "Dusk settles over the harbour like a hand resting, not pressing. "
    "The boats knock softly against the dock, keeping their own slow time. "
    "Whatever waits beyond the water can wait a little longer \u2014 "
    "you are moored, and the tide is in no hurry to take you anywhere."
)

OUT = "/output/entry.txt"


def main():
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    # Guard: the gate counts Unicode code points, 1-280, not only whitespace.
    assert 1 <= len(ENTRY) <= 280, len(ENTRY)
    assert ENTRY.strip(), "entry must not be only whitespace"


if __name__ == "__main__":
    main()
