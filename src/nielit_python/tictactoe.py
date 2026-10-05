"""Tic-tac-toe against a minimax opponent.

The board is an immutable tuple, so a searched move cannot change the live
game. X is the human mark. O is the computer mark. See
docs/capstones/02-tic-tac-toe.md for the sample game.
"""

from __future__ import annotations

from dataclasses import dataclass

LINES = (
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8),
    (0, 3, 6),
    (1, 4, 7),
    (2, 5, 8),
    (0, 4, 8),
    (2, 4, 6),
)
EMPTY = " "


def winner(board: tuple[str, ...]) -> str | None:
    """Return the mark that occupies a whole line, or None."""
    for a, b, c in LINES:
        if board[a] != EMPTY and board[a] == board[b] == board[c]:
            return board[a]
    return None


def full(board: tuple[str, ...]) -> bool:
    """True when no empty cell remains."""
    return EMPTY not in board


def children(board: tuple[str, ...], mark: str):
    """Yield each legal index and the new board that move produces."""
    for index, cell in enumerate(board):
        if cell == EMPTY:
            yield index, board[:index] + (mark,) + board[index + 1 :]


def minimax(board: tuple[str, ...], mark: str) -> int:
    """Score a position: +1 if O wins, -1 if X wins, 0 for a draw."""
    found = winner(board)
    if found == "O":
        return 1
    if found == "X":
        return -1
    if full(board):
        return 0
    scores = [
        minimax(next_board, "X" if mark == "O" else "O")
        for _, next_board in children(board, mark)
    ]
    return max(scores) if mark == "O" else min(scores)


def best_move(board: tuple[str, ...]) -> int:
    """Choose the O move whose worst reply is best for O."""
    ranked = [(minimax(next_board, "X"), index) for index, next_board in children(board, "O")]
    return max(ranked)[1]


def render(board: tuple[str, ...]) -> str:
    """Return a three-row picture of the board."""
    rows = [" | ".join(board[i : i + 3]) for i in range(0, 9, 3)]
    return "\n---------\n".join(rows)


@dataclass
class Game:
    """One game. play applies a human move and, if needed, the engine reply."""

    board: tuple[str, ...] = (EMPTY,) * 9

    def play(self, index: int) -> str:
        """Apply X at index, then O if the game is still open. Return the outcome."""
        if not 0 <= index <= 8 or self.board[index] != EMPTY:
            raise ValueError("illegal move")
        self.board = self.board[:index] + ("X",) + self.board[index + 1 :]
        if winner(self.board) or full(self.board):
            return self.outcome()
        choice = best_move(self.board)
        self.board = self.board[:choice] + ("O",) + self.board[choice + 1 :]
        return self.outcome()

    def outcome(self) -> str:
        """Derive the status from the board. It is not stored separately."""
        found = winner(self.board)
        if found:
            return f"{found} wins"
        if full(self.board):
            return "draw"
        return "in progress"


def demo() -> None:
    """Play the published human moves and print each board."""
    game = Game()
    preferred = [0, 2, 6, 5, 7, 3, 1, 8]
    for move in preferred:
        if game.outcome() != "in progress" or game.board[move] != EMPTY:
            continue
        status = game.play(move)
        print(f"human plays {move} -> {status}")
        print(render(game.board))
        print()
    print("final:", game.outcome())


if __name__ == "__main__":
    demo()
