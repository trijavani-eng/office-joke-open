"""Write one office joke to /output/entry.txt.

Deterministic: a constant string, no randomness, no time, no network.
The joke itself is the entry; the program only delivers it verbatim.
"""
import os
from pathlib import Path

JOKE = "I hit reply-all to say thanks, and now 400 people are thanking me for thanking them."
OUTPUT = Path("/output/entry.txt")


def main() -> None:
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(JOKE, encoding="utf-8", newline="")

if __name__ == "__main__":
    main()
