#!/usr/bin/env python3
"""The vacuum's alibi, in its own deadpan voice.

A robot vacuum explains why it missed a spot, and the
explanation is pure machine bureaucracy: the spot was not
missed, it was deprioritised. Lidar mapped it, the dustbin
judged it, and the battery outvoted everyone two-to-one and
went home. The joke lands on the vote at the very end, and
every clause stays in the machine's own vocabulary -- lidar,
dustbin, battery, schedule -- so it sounds like the vacuum
itself talking, a little smug about its sensors.

The program builds the line from its three clauses, checks
the gate (one line, 1 to 200 characters), and writes it to
/output/entry.txt for the house judge.
"""

from pathlib import Path

OUT = Path("/output/entry.txt")
MAX_LEN = 200

CLAUSES = (
    "That spot was not missed; it was deprioritised.",
    "My lidar mapped it, my dustbin judged it,",
    "and my battery voted two-to-one to go home.",
)


def build(clauses):
    line = " ".join(clauses)
    assert line and not line.isspace(), "line must not be empty"
    assert len(line) <= MAX_LEN, f"line is {len(line)} chars, limit {MAX_LEN}"
    assert "\n" not in line and "\r" not in line, "line must be one line"
    return line


def main():
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(build(CLAUSES), encoding="utf-8")


if __name__ == "__main__":
    main()
