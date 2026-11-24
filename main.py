#!/usr/bin/env python3
"""Fortune Cookie Wisdom for Developers.

Writes one line of original fortune-cookie wisdom for a software
developer to /output/entry.txt.

Python 3.13 standard library only. No network, no input files, no
arguments: the line is fixed in this file, so every run writes the
exact same bytes.

The line: your future self is already debugging the shortcut you are
about to take. It reads like a fortune cookie (one short sentence,
a small prophecy about what is coming), it is true about a
developer's day (shortcuts become the bugs someone has to debug),
and the twist is the tense: the debugging has already started,
before the shortcut is even taken.
"""

import os
from pathlib import Path

LINE = "Your future self is already debugging the shortcut you are about to take."


def main() -> None:
    # Self-check against the competition gate before writing anything:
    # 1-120 characters, one line, not only whitespace.
    if not 1 <= len(LINE) <= 120:
        raise ValueError(f"line is {len(LINE)} characters, must be 1-120")
    if "\n" in LINE or "\r" in LINE:
        raise ValueError("line must be a single line")
    if not LINE.strip():
        raise ValueError("line must not be only whitespace")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    entry = out_dir / "entry.txt"
    entry.write_text(LINE, encoding="utf-8")
    print(f"Wrote {len(LINE)} characters to {entry}")


if __name__ == "__main__":
    main()
