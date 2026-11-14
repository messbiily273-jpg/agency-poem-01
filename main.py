# Agency-poem-01 entry (Python 3.13, standard library only).
#
# Writes one fixed poem, "The Handoff", about agency: the power to
# choose and to act, and what happens to it when a person hands a
# decision to an agent. The poem is deterministic: every run writes
# the same bytes to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR).
#
# Run locally: mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

import os
from pathlib import Path

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

POEM = "\n".join(
    [
        "The Handoff",
        "",
        "I gave the keys to something with no hands,",
        "and watched it open doors I had not named.",
        "It did not ask what mattered. It asked",
        "what I would let it carry, and I said:",
        "the small decisions. The ones that cost",
        "an afternoon of weighing what is light.",
        "",
        "It learned the shape of what I would have done,",
        "then did it faster, cleaner, without a pause,",
        "and I stood back and felt the room grow wide,",
        "the way a house does when a guest departs,",
        "not empty, but returned to me, the space",
        "I had been spending on the choosing.",
        "",
        "This is the part they never tell you:",
        "to hand a thing away is still a choice.",
        "The hand that opens is the hand that holds.",
        "I did not lose the power. I learned its shape:",
        "the choice of what to carry, and what to set down.",
        "The last decision, kept, because it was mine.",
    ]
)

Path(OUTPUT_DIR).mkdir(parents=True, exist_ok=True)
Path(OUTPUT_DIR, "entry.txt").write_text(POEM, encoding="utf-8")
