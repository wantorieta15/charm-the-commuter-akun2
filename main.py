#!/usr/bin/env python3
"""Charm the Commuter: Forecast a City That Isn't (Akun 2).

Writes one line of weather forecast, at most 140 characters, for a city
that does not exist: the place is named, it gets weather, and a bored
commuter gets a smile on the way to work. Pure stdlib only.

Judge brief, in order: (1) reads as a forecast for an invented city,
city named, weather the whole point; (2) makes a bored commuter smile
through a small joke / surprising image / turn of phrase; (3) keeps the
register and rhythm of broadcast weather; (4) one concrete detail of the
city's weather or life; (5) every word earns its place.
"""

import os

ENTRY = (
    "In Crumpleton, light snow at dawn, gone by eight \u2014 "
    "the gritters salted the pavements, the pigeons, "
    "and one very confused postman."
)

MAX_CHARS = 140


def validate(text):
    """Check the entry against the gate: 1-140 chars, one line, not blank."""
    if not text or not text.strip():
        raise SystemExit("entry is empty")
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")
    if len(text) > MAX_CHARS:
        raise SystemExit("entry is %d chars, over the %d limit"
                         % (len(text), MAX_CHARS))
    return text


def write_entry(text, out_dir):
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(text)
    os.chmod(path, 0o644)
    return path


def main():
    text = validate(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    write_entry(text, out_dir)


if __name__ == "__main__":
    main()
