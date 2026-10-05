# Capstone 3 — Hangman

Notebook: [Project_03_Hangman.ipynb](../../notebooks/capstones/Project_03_Hangman.ipynb)

## Why this program exists

Hangman is a state machine with a small public surface. The secret stays on the object. The caller sees a mask, a life count, and the misses. The rules that are easy to get wrong are the repeated guess and the win condition. A repeated guess must not cost a life. The win condition must not be a Boolean stored separately from the letters found, because those two can drift.

## State

`MAX_LIVES` is 6. The constructor stores the secret in lower case, rejects a secret that is not alphabetic, and starts the found and missed sets empty. A digit or a space in the secret would force the mask to invent a meaning; refusing it keeps the rule to one sentence.

`masked` builds the display from the secret and the found set. It does not store the display. `won` is true when every distinct letter of the secret is contained in `found`. `lost` is true when lives are zero and the word is not won. `over` is either. `status` is the one-line report used by the demonstration and by `play_interactive`.

## Guess

`guess` returns a short status string and changes state only when the guess is new and the game is open.

| Input | Effect |
| --- | --- |
| Game already over | No change. Returns `game over`. |
| Not one letter | No change. Returns `enter one letter`. |
| Already in found or missed | No change. Returns `already guessed`. |
| Letter in the secret | Added to `found`. Returns `hit`, or `won` if the set is now complete. |
| Letter absent | Added to `missed`, lives decrease by one. Returns `miss`, or `lost` if lives are now zero. |

The defensive `won` check on a miss cannot succeed. It keeps the return values in one place if the rule later changes.

## Published sequence

The secret is `python`.

| Guess | Result | Mask | Lives | Misses |
| --- | --- | --- | --- | --- |
| a | miss | `_ _ _ _ _ _` | 5 | a |
| p | hit | `p _ _ _ _ _` | 5 | a |
| p | already guessed | unchanged | 5 | a |
| y, t | hit | `p y t _ _ _` | 5 | a |
| z | miss | unchanged | 4 | az |
| h, o | hit | `p y t h o _` | 4 | az |
| n | won | `p y t h o n` | 4 | az |

The repeated `p` is the check that matters. The life count does not move.

`play_interactive` calls `input` in a loop. The notebook does not call it, so **Run all** does not block. Call it yourself when you want to type.

## Extension

A word list belongs in the caller: choose a secret, construct `Hangman`, keep a score outside the class. Putting the dictionary on the class mixes the lexicon with the rules of one game. A whole-word guess is exercise 15.
