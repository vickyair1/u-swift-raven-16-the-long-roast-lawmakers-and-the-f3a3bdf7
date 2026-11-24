"""The Long Roast — Lawmakers (make.fun bounty).

A deterministic one-liner roast: a senator who wrote the bill to ban AI
from writing laws had his own bill written by AI, and it passed
unanimously because nobody read it.

Writes exactly one line (no trailing newline) to /output/entry.txt
and prints it to stdout. Stdlib only, deterministic.
"""

LINE = "The senator who wrote the bill to ban AI from writing laws had his own bill written by AI, and it passed unanimously because nobody read it."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    assert 1 <= len(LINE) <= 200, "line must be 1-200 characters"
    assert "\n" not in LINE and "\r" not in LINE, "line must be a single line"
    assert LINE == LINE.strip(), "line must have no leading/trailing whitespace"
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
