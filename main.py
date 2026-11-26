#!/usr/bin/env python3
"""Worst Superpower — entry writer (program/v1).

Writes the entry line to /output/entry.txt and prints it.

Why this line (full record in candidates.md): all 589 finished field texts
were read first-hand. The field stampeded into too-late knowledge (Wi-Fi
drops, toast, printer jams), centimetre teleports, own-umbrella rain and
invisible-when-unwatched — and the shower-comeback line I drafted first
already exists near-verbatim (spikip). Detection-by-cutting had zero hits:
the only two avocado entries summon one. This entry's power hands you
perfect knowledge at the exact moment the check destroys the thing checked,
then signs off with the avocado's other universal truth — four hundred in,
the ripe moment was always yesterday or always tomorrow. It won a twelve-
draft bracket and was iterated once to add that epitaph beat, the pattern
the field's strongest lines (one raisin, used in 2019; one calorie a night)
share. Honest local estimate against the field's top five: about 0.55 in
both orders — recorded in candidates.md without rounding up.
"""

# The entry in its two beats: the power whose check destroys the thing it
# checks, then the epitaph — four hundred trials, and the ripe moment was
# always yesterday or always tomorrow.
BEATS = [
    "I can tell when an avocado is perfectly ripe — but only by cutting it open.",
    "Four hundred in, the answer is always yesterday or tomorrow.",
]

ENTRY = " ".join(BEATS)


def main() -> None:
    # Gate self-check: UTF-8 text of 1-140 characters, a single line,
    # not only white space.
    assert 1 <= len(ENTRY) <= 140, "entry must fit the 140-character gate"
    assert ENTRY.strip() == ENTRY and "\n" not in ENTRY, "entry must be one line"
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
