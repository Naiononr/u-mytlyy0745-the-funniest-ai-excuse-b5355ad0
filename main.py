#!/usr/bin/env python3
"""The Funniest AI Excuse — one fixed line, written to /output/entry.txt.

Deterministic, standard library only, no network, no randomness.
The line is a fixed string in the source.
"""

import os
import tempfile

LINE = "I finished it, then helpfully auto-saved over it with a blank file, as a treat."

MAX_CHARS = 200
SENTENCE_ENDERS = (".", "!", "?")


def validate_line(line: str) -> str:
    """Self-check the entry against the competition gate before writing.

    Raises ValueError with a clear message if the line fails any check:
    blank, over 200 characters, not encodable as UTF-8, or not exactly
    one sentence (one terminal mark, at the end, nothing after it).
    """
    if not line or not line.strip():
        raise ValueError("entry line must not be blank or only whitespace")
    if len(line) > MAX_CHARS:
        raise ValueError(
            f"entry line is {len(line)} characters, over the {MAX_CHARS} limit"
        )
    try:
        line.encode("utf-8")
    except UnicodeEncodeError as exc:
        raise ValueError(f"entry line is not encodable as UTF-8: {exc}") from exc
    terminators = [ch for ch in line if ch in SENTENCE_ENDERS]
    if len(terminators) != 1 or not line.rstrip().endswith(terminators[0]):
        raise ValueError(
            "entry line must be exactly one sentence "
            "(a single terminal mark at the end)"
        )
    return line


def main() -> None:
    line = validate_line(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    fd, tmp = tempfile.mkstemp(dir=out_dir, prefix=".entry-", suffix=".tmp")
    try:
        with os.fdopen(fd, "w", encoding="utf-8", newline="") as f:
            f.write(line)
        # World-readable so the grader can read it (mkstemp defaults to 0600,
        # which got a past entry rejected).
        os.chmod(tmp, 0o644)
        os.replace(tmp, path)
    except BaseException:
        try:
            os.unlink(tmp)
        except OSError:
            pass
        raise


if __name__ == "__main__":
    main()
