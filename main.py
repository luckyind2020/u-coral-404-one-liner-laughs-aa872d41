"""One-Liner Laughs entry: print the single joke line from entry.txt."""

from pathlib import Path

MAX_CHARS = 200


def load_line() -> str:
    """Read entry.txt next to this file and validate the joke line."""
    raw = Path(__file__).with_name("entry.txt").read_text(encoding="utf-8")
    line = raw.strip()
    if not line:
        raise ValueError("entry.txt is empty or only whitespace")
    if len(line) > MAX_CHARS:
        raise ValueError(f"joke is {len(line)} chars, over the {MAX_CHARS} limit")
    if "\n" in line or "\r" in line:
        raise ValueError("joke must be a single line")
    if any(ord(ch) < 32 for ch in line):
        raise ValueError("joke contains control characters")
    return line


def render_line(line: str) -> str:
    """Return the exact bytes the judge reads: the line plus one newline."""
    return line + "\n"


def main() -> None:
    print(render_line(load_line()), end="")


if __name__ == "__main__":
    main()
