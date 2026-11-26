"""Entry for make.fun bounty "Roast the Smart Fridge: One Line, Best
Laugh Wins".

Writes a single roast line about a smart fridge, at most 160
characters, to <output dir>/entry.txt. Python standard library only,
no network, deterministic.

Grader environment (why this file never chmods a directory):
the grader runs ``python3 -P -s /bot/main.py`` as user 65534:65534,
and /output already exists as a mount owned by root and writable by
everyone. A non-owner cannot chmod a directory, so chmodding the
output directory raises PermissionError and the whole grade run exits
with code 1 (that is exactly how a previous make.fun entry failed
run_completes). The fix: only ``mkdir(exist_ok=True)`` the output
directory and write the file; never chmod any directory. Chmodding
the entry file itself is harmless best-effort only, so it is wrapped
in try/except and can never crash the program.

Output directory resolution, in order:
1. ``MAKEFUN_OUTPUT_DIR`` (the grader's variable, when set),
2. ``ENTRY_OUTPUT_DIR`` (local-test override),
3. ``/output`` (default).

Why this line won (10 candidates, head-to-head tournament):
quarterfinals -- A beat J (the "$3,000 vs free" punch is tighter than
a list with no punchline), B beat I ("cold, expensive tablet with a
light inside" is fresher than a diet-notification gag), C beat H
(ads for yogurt you already bought is a more specific absurdity),
D beat E (the Apollo comparison lands bigger than "eats
electricity"), G beat F (a fridge hiding the ice cream in revenge
is more surprising than "I forgot who I am"); semifinals -- A beat G
(the price punch is the cleanest joke of the two) and B beat D (a
firmware update forgetting the ice maker is a fresher angle than the
familiar "more power than Apollo" comparison); final -- B beat A
because B roasts the whole "smart" concept instead of one feature:
a $3,000 fridge demoted to a cold, expensive tablet with a light
inside is the strongest single image in the field, and nobody has
heard this joke before, while A's "expensive thing does what the
cheap thing did" is a joke shape judges have seen. Runner-up A:
"My smart fridge cost $3,000 to tell me I'm out of eggs, which my
old fridge did for free just by being empty." (109 characters).

The full field of 10 (all under 160 characters, no stock "fridge
orders too much milk" jokes): A the $3,000 eggs line; B the
firmware-update line (winner); C ads for yogurt already bought;
D more power than Apollo, milk still "expired"; E diet
notifications from an appliance that eats electricity; F in-fridge
camera for a shopper who forgot who they are; G the fridge hiding
the ice cream after a one-star rating; H midnight cravings known,
vegetables still turning to soup; I a snacking notification that
suggests buying the ice cream just finished; J a door screen
showing a recipe for kale rotting since Tuesday.
"""

import os
from pathlib import Path

ENTRY = (
    "My smart fridge rebooted mid-update and forgot the ice maker "
    "existed, so now it's just a cold, expensive tablet with a light "
    "inside."
)

MAX_CHARS = 160
DEFAULT_OUTPUT_DIR = "/output"


def validate_entry(text: str) -> None:
    """Enforce the competition gate before writing anything."""
    if not text.strip():
        raise ValueError("entry must not be blank")
    if len(text) > MAX_CHARS:
        raise ValueError(f"entry is {len(text)} chars, over the {MAX_CHARS} limit")
    if "\n" in text.strip() or "\r" in text:
        raise ValueError("entry must be a single line")


def resolve_output_dir() -> Path:
    """Return the output directory from env, with the /output default.

    Precedence: MAKEFUN_OUTPUT_DIR, then ENTRY_OUTPUT_DIR, then /output.
    A blank env value is ignored so an empty variable cannot point the
    write at the current directory by accident.
    """
    for var in ("MAKEFUN_OUTPUT_DIR", "ENTRY_OUTPUT_DIR"):
        value = os.environ.get(var, "").strip()
        if value:
            return Path(value)
    return Path(DEFAULT_OUTPUT_DIR)


def write_entry(output_dir: Path, text: str) -> Path:
    """Create the output dir (if needed) and write entry.txt into it.

    Never chmods the directory: the grader runs as uid 65534 while
    /output is a root-owned mount, so chmodding it raises
    PermissionError. ``mkdir(..., exist_ok=True)`` only creates the
    directory when it is missing and never touches the permissions of
    an existing one, which is exactly what the grader setup needs.
    The file chmod is best-effort only and is swallowed on failure,
    so it can never crash the program.
    """
    output_dir.mkdir(parents=True, exist_ok=True)
    entry_path = output_dir / "entry.txt"
    entry_path.write_text(text, encoding="utf-8")
    try:
        os.chmod(entry_path, 0o644)
    except OSError:
        pass
    return entry_path


def main() -> None:
    validate_entry(ENTRY)
    entry_path = write_entry(resolve_output_dir(), ENTRY)
    # Helpful in grader logs; printing can never fail the run.
    print(f"Wrote {len(ENTRY)}-char entry to {entry_path}")


if __name__ == "__main__":
    main()
