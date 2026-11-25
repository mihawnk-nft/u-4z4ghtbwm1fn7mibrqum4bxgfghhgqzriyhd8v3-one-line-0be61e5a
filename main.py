#!/usr/bin/env python3
"""One Line, One Laugh — make.fun entry.

Writes a single original funny line to /output/entry.txt.
Pure Python standard library; no network, no secrets, no input files.
"""

import os

LINE = "I asked AI to write my wedding vows; it said 'I do' to the terms and conditions."

# The gate: /output/entry.txt must be UTF-8 text of 1 to 140 characters,
# not only white space. Fail loudly instead of shipping an invalid entry.
assert 1 <= len(LINE) <= 140 and LINE.strip(), "entry line violates the gate"


def main() -> None:
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
