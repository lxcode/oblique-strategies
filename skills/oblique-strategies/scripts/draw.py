import argparse
import secrets
import sys
from pathlib import Path

DECKS = Path(__file__).resolve().parent.parent / "decks"
PREFERRED = ("eno", "engineering")


def load(deck: str) -> list[str]:
    lines = (DECKS / f"{deck}.txt").read_text(encoding="utf-8").splitlines()
    return [s for line in lines if (s := line.strip()) and not s.startswith("#")]


def main() -> None:
    p = argparse.ArgumentParser(description="Draw one Oblique Strategies card.")
    p.add_argument(
        "--deck", help="deck name in decks/ (default: eno, else engineering)"
    )
    args = p.parse_args()

    candidates = (args.deck,) if args.deck else PREFERRED
    for deck in candidates:
        try:
            cards = load(deck)
        except FileNotFoundError:
            continue
        if cards:
            print(f"[{deck}] {secrets.choice(cards)}")
            return
    sys.exit(f"no non-empty deck found among {candidates} in {DECKS}")


if __name__ == "__main__":
    main()
