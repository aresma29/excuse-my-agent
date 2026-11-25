#!/usr/bin/env python3
"""Print the excuse line from entry.txt.

Resolves entry.txt next to this file, so it works from any cwd
on a read-only filesystem.
"""
import sys
from pathlib import Path


def main() -> int:
    entry_path = Path(__file__).resolve().parent / "entry.txt"
    text = entry_path.read_text(encoding="utf-8").strip()
    print(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
