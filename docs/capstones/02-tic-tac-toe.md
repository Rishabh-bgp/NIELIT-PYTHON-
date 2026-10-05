# Capstone 2 — Tic-tac-toe

Notebook: [Project_02_Tic_Tac_Toe.ipynb](../../notebooks/capstones/Project_02_Tic_Tac_Toe.ipynb)

## Why this program exists

A board game makes state visible. Tic-tac-toe is small enough that the opponent can search the whole remaining tree. The notebook therefore teaches two ideas at once: an immutable board, and a search that does not need a hand-written strategy table.

The human mark is `X`. The computer mark is `O`. `O` uses minimax. If both sides play perfectly from an empty board, the result is a draw. The published sample does not play perfectly for `X`, and `O` wins. That is evidence the search is punishing a mistake, not evidence that `O` can force a win against optimal play.

## Board

The board is a tuple of nine strings. An empty cell is a single space, not the empty string, so a rendered row keeps its width. A tuple cannot be mutated. Every imagined move builds a new tuple with slicing. The live game and the search cannot share a board by accident.

Winning lines are three rows, three columns, and two diagonals, stored as index triples in `LINES`. `winner` returns the mark if a line is uniform and not empty. `full` is true when no space remains. A draw is a full board with no winner. `children` yields each legal index paired with the board that move produces. It does not play the move.

## Minimax

A finished position scores `+1` if `O` has won, `-1` if `X` has won, and `0` for a draw. On `O`'s turn the function takes the maximum child score. On `X`'s turn it takes the minimum, which models a human who also plays the best reply. `best_move` chooses the index whose resulting position has the highest score for `O`. Equal scores keep the later index, because `max` on pairs compares the score first and the index second. The engine does not prefer the centre by a special case. The centre falls out of the scores when it is the best reply.

No alpha-beta pruning is used. After the first move the tree is at most `8!` leaves, and wins cut it further. Clarity matters more than the pruning at this size.

## The published game

The demonstration does not call `input`. It walks a preferred list and skips a cell the engine has already taken.

1. Human plays index 0. Engine plays 4, the centre. Status: in progress.
2. Human plays index 2. Engine plays 1, blocking the top row. Status: in progress.
3. Human plays index 6. Engine plays 7. The middle column is `O`, `O`, `O`. Status: `O wins`.

`Game.play` rejects an occupied or out-of-range cell with `ValueError` before it asks the engine to move. `outcome` is derived from the board on each call. It is not a stored flag.

## Extension

A terminal loop is a `while` around `input` and `play`. Parse the typed index outside `Game`. Keep `play` as the only method that writes a mark. A draw sample is exercise 14 in [the exercise list](../exercises.md): change the human moves, do not change the search, and record the move list.
