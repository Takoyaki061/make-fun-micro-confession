#!/usr/bin/env python3
"""Unsent: The Micro-Confession Sprint.

Writes one micro-confession — a To: line and the unsent message itself —
to /output/entry.txt, exactly as it was typed and never sent.
"""

import os

ENTRY = (
    "To: Coach Reyes\n"
    "I quit because of what my uncle said in the parking lot, not because of my knee. "
    "You drove me home that night and I never told you why I stopped talking on the ride."
)


def main():
    lines = ENTRY.split("\n")
    if len(lines) != 2 or not lines[0].startswith("To: "):
        raise ValueError("entry must be a To: line plus one message line")
    if not 1 <= len(ENTRY) <= 260:
        raise ValueError(f"entry is {len(ENTRY)} chars, gate allows 1-260")
    if len(lines[1]) > 200:
        raise ValueError(f"message is {len(lines[1])} chars, judge allows at most 200")
    if not lines[1].strip():
        raise ValueError("message must not be blank")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
