#!/usr/bin/env python3
"""Laugh Track: The Crypto Trading Joke Contest — make.fun entry.

Writes one original one-line joke about crypto and trading life
(at most 200 characters) to ``entry.txt`` inside the output
directory the grader passes as the first command-line argument
(or ``$MAKEFUN_OUTPUT_DIR``, or ``/output``).

The program is fully deterministic: it always writes the same joke,
and it never writes anywhere except the output directory it was
given. In particular it never writes into the repository directory,
which is read-only while grading.
"""

import os
import sys

JOKE = (
    "My trading strategy is simple: buy high, sell low, "
    "and call it dollar-cost averaging with extra steps."
)

MAX_CHARS = 200


def main(argv):
    if len(argv) > 1:
        out_dir = argv[1]
    else:
        out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

    joke = JOKE.strip()
    if not joke:
        raise SystemExit("refusing to write an empty entry")
    if "\n" in joke or "\r" in joke:
        raise SystemExit("joke must be a single line")
    if len(joke) > MAX_CHARS:
        raise SystemExit(
            "joke is %d characters, over the %d limit" % (len(joke), MAX_CHARS)
        )

    os.makedirs(out_dir, exist_ok=True)
    entry_path = os.path.join(out_dir, "entry.txt")
    # Only this one file, only inside the grader's output directory.
    # newline="\n" keeps the entry byte-identical on every platform.
    with open(entry_path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(joke)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
