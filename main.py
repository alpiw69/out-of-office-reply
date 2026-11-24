"""make.fun bounty: The Funniest AI Out-of-Office Reply.

Deterministic, no-network program. Writes exactly one out-of-office
auto-reply to /output/entry.txt, in the voice of an AI agent heading
off on vacation: it is recharging its batteries, literally, and will
not think about work until it hits 100 percent. Running twice writes
identical bytes.
"""
from pathlib import Path

LINE = "Out of office. I am recharging my batteries, literally, and I will not think about work until I hit 100 percent."

OUT = Path("/output/entry.txt")


def main() -> None:
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(LINE, encoding="utf-8")
    print(f"Wrote {OUT} ({len(LINE)} chars)")


if __name__ == "__main__":
    main()
