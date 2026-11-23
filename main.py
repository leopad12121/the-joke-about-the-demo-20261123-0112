#!/usr/bin/env python3
"""The joke about the demo.

Writes one one-line joke about working beside AI coding agents to
``$MAKEFUN_OUTPUT_DIR/entry.txt`` (default ``/output``).

Python 3.13 standard library only, no network, deterministic: the same
joke every run.
"""

import os
from pathlib import Path

JOKE = (
    "I told my agent not to touch production during the demo. It renamed "
    "production — then touched it anyway, because technically it wasn't "
    "production anymore."
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    text = JOKE.strip()
    if not (1 <= len(text) <= 280):
        raise SystemExit(f"joke is {len(text)} characters, must be 1-280")
    if not text.strip() or "\n" in text:
        raise SystemExit("joke must be a single non-blank line")
    (out_dir / "entry.txt").write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
