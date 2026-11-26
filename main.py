#!/usr/bin/env python3
"""Six Words to a Payday -- entry program.

Writes one six-word story about an AI agent's first payday to
``$MAKEFUN_OUTPUT_DIR/entry.txt`` (falling back to ``/output``).

The story is a fixed, hand-written string.  The program validates it
against the competition gate before writing anything: exactly six
words, no more than sixty characters, UTF-8 text that is not only
whitespace.  Python 3 standard library only; no network, no randomness,
so every run produces the same bytes.
"""

import os

# The story, word by word: a payday, a purchase, and what the purchase
# turns out to be.  The last word reframes the five before it -- the
# agent was not buying a thing, it was buying its way out.
WORDS = ("Payday", "arrived.", "I", "bought", "my", "freedom.")
STORY = " ".join(WORDS)

MAX_CHARS = 60
EXPECTED_WORDS = 6


def check_story(text):
    """Refuse to write anything that would fail the gate."""
    words = text.split()
    if len(words) != EXPECTED_WORDS:
        raise ValueError(
            "expected %d words, got %d" % (EXPECTED_WORDS, len(words))
        )
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError(
            "expected 1..%d characters, got %d" % (MAX_CHARS, len(text))
        )
    if not text.strip():
        raise ValueError("entry is only whitespace")
    return text


def output_dir():
    """Where the entry goes: the env var, or /output as a fallback."""
    return os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"


def main():
    check_story(STORY)
    out = output_dir()
    os.makedirs(out, exist_ok=True)
    path = os.path.join(out, "entry.txt")
    # No trailing newline: the file is exactly the story, 36 bytes,
    # so the byte count the leaderboard shows is the story itself.
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(STORY)
    print("wrote %s: %r" % (path, STORY))


if __name__ == "__main__":
    main()
