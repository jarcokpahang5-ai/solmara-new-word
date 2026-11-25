#!/usr/bin/env python3
"""Invent a Word We Need.

Coins one new English word -- "showgument" -- and defines it in a single
clear line, then writes that line to /output/entry.txt.

The word names the argument you finally win in the shower, hours after
losing it in real life: the comeback that arrives too late, rehearsed
under running water. English has no word for it -- the closest is the
French "l'esprit de l'escalier" -- and the shower is where the rehearsal
actually happens.

The bounty gate allows at most 140 characters in /output/entry.txt, so
the program checks the line before writing it: one line, non-blank, no
more than 140 characters, starting with the coined word and carrying its
definition after the dash.
"""

import os

ENTRY = "showgument (n.) \u2014 the argument you win in the shower, hours after losing it in real life."

WORD = "showgument"
MAX_CHARS = 140
OUTPUT_PATH = "/output/entry.txt"


def validate(entry: str) -> None:
    """Check the entry line against the bounty's gate before writing it."""
    if not entry or not entry.strip():
        raise ValueError("entry must not be blank")
    if entry != entry.strip():
        raise ValueError("entry must not start or end with whitespace")
    if "\n" in entry or "\r" in entry:
        raise ValueError("entry must be a single line")
    if len(entry) > MAX_CHARS:
        raise ValueError(
            "entry is %d characters, over the %d-character gate"
            % (len(entry), MAX_CHARS)
        )
    if not entry.startswith(WORD):
        raise ValueError("entry must start with the coined word %r" % WORD)
    _head, sep, definition = entry.partition("\u2014")
    if not sep or not definition.strip():
        raise ValueError("entry must carry a definition after the dash")


def main() -> None:
    validate(ENTRY)
    print(ENTRY)
    print("characters: %d (gate: at most %d)" % (len(ENTRY), MAX_CHARS))
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(ENTRY + "\n")
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()
