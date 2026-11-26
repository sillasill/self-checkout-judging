"""Self-checkout judge: one smug line about twelve yoghurts."""

import os

OUTPUT_PATH = "/output/entry.txt"

PART_A = "Twelve yoghurts and nothing else. Beep. "
PART_B = "Bold of you to call this a shop, not a cry for help."


def main():
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(PART_A + PART_B)


if __name__ == "__main__":
    main()
