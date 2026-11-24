#!/usr/bin/env python3
"""Drop one fixed excuse line into entry.txt for The Funniest AI Excuse.

There is nothing clever here on purpose: the whole job is to carry a
single sentence from this file to the output file the graders read,
checking on the way that the sentence is fit to be judged, and to do
it the same way on every run. No input is read, no network is touched,
and the result never depends on the machine or the moment.
"""

import os
import sys
import tempfile
from pathlib import Path

# The line itself: seventy-nine characters, one line, spoken by an
# agent that has just failed and is trying to sound helpful about it.
EXCUSE = "I finished it, then helpfully auto-saved over it with a blank file, as a treat."

# The sealed gate's bounds for the text: at least one character, at
# most two hundred.
CEILING = 200


def _where_to_write() -> Path:
    """Pick the output file.

    The harness can redirect the run with MAKEFUN_OUTPUT_DIR; with no
    such variable the graded location, /output, is the fallback.
    """
    root = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return Path(root) / "entry.txt"


def main() -> int:
    """Validate the excuse, then atomically place it in entry.txt.

    Returns 0 when the file is written, 1 when a gate check fails.
    """
    target = _where_to_write()

    # Gate checks, done here in the open: length inside bounds, a
    # single line, and real text rather than blank space.
    size = len(EXCUSE)
    if size < 1 or size > CEILING:
        print(f"excuse is {size} characters, outside 1..{CEILING}", file=sys.stderr)
        return 1
    if "\n" in EXCUSE or "\r" in EXCUSE:
        print("excuse must stay on one line", file=sys.stderr)
        return 1
    if not EXCUSE.strip():
        print("excuse must not be only whitespace", file=sys.stderr)
        return 1

    blob = EXCUSE.encode("utf-8")

    # Write beside the target first, make the scratch file readable,
    # then move it into place, so the graded file is never seen
    # half-written and never left unreadable by the scorer.
    target.parent.mkdir(parents=True, exist_ok=True)
    handle, scratch = tempfile.mkstemp(prefix="entry-", dir=str(target.parent))
    try:
        with os.fdopen(handle, "wb") as stream:
            stream.write(blob)
        os.chmod(scratch, 0o644)
        os.replace(scratch, target)
    except BaseException:
        try:
            os.unlink(scratch)
        except OSError:
            pass
        raise
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
