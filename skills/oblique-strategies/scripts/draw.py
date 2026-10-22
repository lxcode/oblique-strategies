import secrets
from pathlib import Path

DECK = Path(__file__).resolve().parent.parent / "decks" / "eno.txt"


def main() -> None:
    lines = DECK.read_text(encoding="utf-8").splitlines()
    cards = [s for line in lines if (s := line.strip()) and not s.startswith("#")]
    print(secrets.choice(cards))


if __name__ == "__main__":
    main()
