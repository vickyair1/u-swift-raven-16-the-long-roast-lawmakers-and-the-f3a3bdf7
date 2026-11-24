"""The Long Roast entrypoint: emit one satirical sentence about lawmakers
who regulate AI but cannot convert a file to PDF."""

import os

LINE = "The senator writing the law that tells artificial intelligence what it is allowed to think just emailed his intern the bill as a .docx and asked her to turn it into a PDF for him."

OUTPUT_PATH = "/output/entry.txt"


def main():
    print(LINE)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(LINE)


if __name__ == "__main__":
    main()
