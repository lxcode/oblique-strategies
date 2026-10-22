import argparse
import os
import secrets
import sys
from pathlib import Path

# The user dir survives plugin updates, which replace the bundled one.
USER_DECKS = (
    Path(os.environ.get("XDG_CONFIG_HOME") or Path.home() / ".config")
    / "oblique-strategies"
)
BUNDLED_DECKS = Path(__file__).resolve().parent.parent / "decks"
SEARCH = (USER_DECKS, BUNDLED_DECKS)
PREFERRED = ("eno", "engineering")


def load(deck: str) -> list[str] | None:
    for d in SEARCH:
        try:
            lines = (d / f"{deck}.txt").read_text(encoding="utf-8").splitlines()
        except FileNotFoundError:
            continue
        return [s for line in lines if (s := line.strip()) and not s.startswith("#")]
    return None


def main() -> None:
    p = argparse.ArgumentParser(description="Draw one Oblique Strategies card.")
    p.add_argument("--deck", help="deck name (default: eno, else engineering)")
    args = p.parse_args()

    candidates = (args.deck,) if args.deck else PREFERRED
    for deck in candidates:
        if cards := load(deck):
            print(f"[{deck}] {secrets.choice(cards)}")
            return
    sys.exit(f"no non-empty deck among {candidates} in {', '.join(map(str, SEARCH))}")


if __name__ == "__main__":
    main()
