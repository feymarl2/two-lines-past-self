"""Two Lines to Your Past Self — make.fun entry.

Writes exactly two lines to /output/entry.txt (MAKEFUN_OUTPUT_DIR):
line 1 warns the past self about one specific moment; line 2 says in
one sentence why that moment mattered and what changed because of it.
Pure stdlib, no network, no randomness, no clock reads: the output is
a constant, so the grader's two runs are byte-identical.
"""

import os

LINE_1 = "Don't put your rent money on Lucky Jim at the track."
LINE_2 = "It wins, and winning teaches you to bet the next three rents too."

ENTRY = LINE_1 + "\n" + LINE_2


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
