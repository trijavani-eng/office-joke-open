"""Write one office joke to /output/entry.txt.

Deterministic: a constant string, no randomness, no time, no network.
"""
import os

JOKE = "I hit reply-all to say thanks, and now 400 people are thanking me for thanking them."

def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)

if __name__ == "__main__":
    main()
