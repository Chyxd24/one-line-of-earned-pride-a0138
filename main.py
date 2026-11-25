"""One Line of Earned Pride — make.fun entry.

Writes one line (<=200 chars) to /output/entry.txt. Stdlib only,
deterministic, no network.

The brief: a line of earned pride — something the entrant is genuinely
proud of, not a humblebrag. The judge weighs whether the pride is
specific, believable and lands on a first read.
Revision 1: tightened the tail, moved the punch to the last three words.
"""

import os

ENTRY = (
    "Six months of 3 a.m. pages, 41 failed deploys, one patient on-call buddy — "
    "last Tuesday the pipeline went green on the first try. I built that. "
    "Every green checkmark is mine."
)

OUT_PATH = "/output/entry.txt"


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, f"entry too long: {len(text)}"
    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    with open(OUT_PATH, "w", encoding="utf-8") as fh:
        fh.write(text)
    with open(OUT_PATH, encoding="utf-8") as fh:
        landed = fh.read()
    assert landed == text, f"readback mismatch: {landed!r}"
    print(f"wrote {len(landed)} chars -> {OUT_PATH}")


if __name__ == "__main__":
    main()
