# Capstone 3 — Hangman

Notebook: [Project_03_Hangman.ipynb](../../notebooks/capstones/Project_03_Hangman.ipynb)

## Purpose

A word game as a small state machine. The secret stays on the object. The caller sees the mask, the remaining lives, and the misses. The interesting rule is not the mask. It is that a repeated guess must not be charged twice, and that the win condition must not be a flag that can disagree with the letters found.

## State

`Hangman` stores the secret in lower case, a life count starting at 6, a set of found letters, and a set of missed letters. The constructor rejects a secret that is not alphabetic, so a later mask does not have to decide what a digit means.

`masked` builds the display from the secret and the found set. It does not store the display. `won` is true when every distinct letter of the secret is in `found`. `lost` is true when lives are zero and the word is not won. `over` is either of those.

## Guess

`guess` rejects a finished game, a value that is not one letter, and a letter already present in either set. A hit adds the letter to `found` and reports `hit` or `won`. A miss adds the letter to `missed`, decreases lives, and reports `miss`, `won`, or `lost`. The `won` branch on a miss is defensive: a miss cannot complete the word. Leaving the check in one place keeps the return values consistent if the rule changes.

## Sample

The published sequence guesses `python` with two misses (`a`, `z`) and one repeated `p`. The repeat does not change the life count. The last guess, `n`, reports `won` and the mask `p y t h o n`.

`play_interactive` is defined for a session that can call `input`. The notebook does not call it, so a full run does not block.

## Extension

A word list belongs outside the class: choose a secret, construct `Hangman`, and keep score in the caller. Putting the list on the class would mix the dictionary with the rules of one game.
