# Capstone 2 — Tic-tac-toe

Notebook: [Project_02_Tic_Tac_Toe.ipynb](../../notebooks/capstones/Project_02_Tic_Tac_Toe.ipynb)

## Purpose

A complete two-player game with an opponent that plays optimally. The human mark is `X`. The computer mark is `O`. The search is minimax over the whole remaining tree. A 3 by 3 board does not need alpha-beta pruning; the tree is small once finished games are cut off.

## Board

The board is a tuple of nine strings. Empty cells are a single space. A tuple cannot be mutated, so every imagined move builds a new tuple with slicing. The live game and the search cannot accidentally share a board.

Winning lines are the three rows, three columns, and two diagonals, stored as index triples. `winner` returns the mark if a line is uniform and not empty. `full` is true when no space remains. A draw is a full board with no winner.

## Search

`minimax` returns `+1` if `O` has won, `-1` if `X` has won, and `0` for a draw or a position that leads only to a draw. On `O`'s turn the function takes the maximum child score. On `X`'s turn it takes the minimum, which models a human who also plays the best available reply. `best_move` asks for the index whose resulting position has the highest score for `O`.

## Game object

`Game.play` applies a human index, rejects an occupied or out-of-range cell, and if the game is still open applies `best_move`. `outcome` reports `X wins`, `O wins`, `draw`, or `in progress`.

The published demonstration does not read `input`. It walks a preferred list of human indexes and skips a cell the engine has already taken. In that run the human opens in a corner, the engine takes the centre, and the human's third move leaves a column that `O` completes. The result is `O wins`. That is the expected result of those human moves, not a fault in the search. Optimal play by both sides from an empty board ends in a draw; this sample does not play optimally for `X`.

## Extension

A terminal loop is a `while` around `play` and `input`. Keep the parsing of the typed index outside `Game`, and keep `Game.play` as the only way a mark is written.
