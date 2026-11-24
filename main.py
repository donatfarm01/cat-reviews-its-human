#!/usr/bin/env python3
"""Cat Reviews Its Human — one funny single-line one-star review.

The review is written in the voice of a house cat about its human. The
program writes exactly that one line to /output/entry.txt and nothing else.
"""

import os

REVIEW = (
    "One star. My human opened the door, I went out, he closed it, "
    "I wanted back in. He calls this my fault. "
    "I have knocked his favourite plant over and I will do it again."
)


def main() -> None:
    out = os.environ.get("ENTRY_OUT", "/output/entry.txt")
    parent = os.path.dirname(out)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(REVIEW)


if __name__ == "__main__":
    main()
