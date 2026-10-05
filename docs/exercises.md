# Exercises

Practice that is not already solved in a notebook cell. Attempt the exercise before reading the note under it. The note is a direction, not a full solution.

## After sections 1 to 4

1. Bind two names to one list, append through the first, and predict the second before running. Then rebind the first with `+` and predict again.
2. Write a function that returns `Decimal("0.1") + Decimal("0.2")` and the float sum side by side. State which one equals `Decimal("0.3")`.
3. List five values that are false in a Boolean test, and one value that looks empty but is true. `[0]` is the interesting case.

## After sections 5 and 6

4. Search a list for the first multiple of 7. Use `for` / `else` so the failure message runs only when none is found.
5. Write `scale(values, factor=1, *, rounding=None)` and call it positionally and with the keyword-only argument. Confirm that a positional `rounding` is a `TypeError`.
6. Build three lambdas in a loop without a default, and three with `i=i`. Print both results for input `10`.

## After sections 7 to 9

7. Count words in a sentence with a dict and `get`, then again with `collections.Counter`. The counts must match.
8. Write a generator `chunks(text, size)` that yields successive slices and does not build a list of all slices first.
9. Flatten `[[1, 2], [], [3]]` with `yield from`. The empty row must contribute nothing.

## After sections 10 to 12

10. Write `parse_score(raw)` that rejects non-integers and scores outside 0 to 100, chaining the `int` failure with `from`.
11. Write a context manager that appends a line to a log file on exit, including when the block raises. Return `False` from `__exit__`.
12. Subclass `Account` with a withdrawal that refuses an amount above the balance. Call `super` only if you also override `__init__`.

## After the capstones

13. Add a unary plus and a memory-clear primary to the calculator without calling `eval`. Say which grammar rule each belongs to.
14. Change the tic-tac-toe sample so the human plays the replies that lead to a draw. Record the move list in the notebook.
15. Teach Hangman to accept a whole-word guess. A wrong word costs one life. A repeated word is rejected.
16. Reject a quiz response that is not one of `choices`, and add that result to the report.
17. Write the October ledger to JSON lines and read it back. Amounts must survive as `Decimal`, not as floats.

None of these exercises are required to understand the published notebooks. They are the shortest path from reading a cell to owning the idea.
