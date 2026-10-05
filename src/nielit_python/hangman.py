"""Hangman as a small state machine.

The secret stays on the instance. A repeated guess does not cost a life.
The win condition is derived from the found letters. See
docs/capstones/03-hangman.md.
"""

from __future__ import annotations

from dataclasses import dataclass, field

MAX_LIVES = 6


@dataclass
class Hangman:
    """One word, a life count, and the letters already tried."""

    secret: str
    lives: int = MAX_LIVES
    found: set[str] = field(default_factory=set)
    missed: set[str] = field(default_factory=set)

    def __post_init__(self) -> None:
        self.secret = self.secret.lower().strip()
        if not self.secret.isalpha():
            raise ValueError("secret must contain only letters")

    def masked(self) -> str:
        """Display the secret with unfound letters replaced by underscores."""
        return " ".join(ch if ch in self.found else "_" for ch in self.secret)

    def guess(self, letter: str) -> str:
        """Apply one letter. Return hit, miss, won, lost, or a rejection."""
        if self.over:
            return "game over"
        cleaned = letter.lower().strip()
        if len(cleaned) != 1 or not cleaned.isalpha():
            return "enter one letter"
        if cleaned in self.found or cleaned in self.missed:
            return "already guessed"
        if cleaned in self.secret:
            self.found.add(cleaned)
            return "hit" if not self.won else "won"
        self.missed.add(cleaned)
        self.lives -= 1
        return "lost" if self.lost else "miss"

    @property
    def won(self) -> bool:
        """True when every distinct secret letter has been found."""
        return set(self.secret) <= self.found

    @property
    def lost(self) -> bool:
        """True when no lives remain and the word is incomplete."""
        return self.lives == 0 and not self.won

    @property
    def over(self) -> bool:
        """True when the game has been won or lost."""
        return self.won or self.lost

    def status(self) -> str:
        """One-line report used by the demonstration."""
        misses = "".join(sorted(self.missed)) or "-"
        return f"{self.masked()}   lives={self.lives}   misses={misses}"


def play_interactive(secret: str) -> None:
    """Read guesses from standard input until the game ends."""
    game = Hangman(secret)
    while not game.over:
        print(game.status())
        game.guess(input("letter: "))
    print(game.status(), "won" if game.won else "lost")


def demo() -> None:
    """Play the published letter sequence for the secret 'python'."""
    game = Hangman("python")
    for letter in ["a", "p", "p", "y", "t", "z", "h", "o", "n"]:
        result = game.guess(letter)
        print(f"{letter}: {result:16} {game.status()}")
    print("won:", game.won)


if __name__ == "__main__":
    demo()
