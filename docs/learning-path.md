# Learning path

A short course built only from this repository. Each sitting assumes the previous one. The outcome is what a reader should be able to say or write afterwards, without the notebook open. The matching exercises are in [exercises.md](exercises.md).

## Sitting 1 — Objects and names

Notebook sections 1 to 4. Notes in the [language reference](language-reference.md).

Outcome: explain why two names can see one `append`, why `0.1 + 0.2` is not `0.3`, and why `and` can return a string. Choose `is` or `==` for a `None` test without looking it up. State the false values.

Exercises 1 to 3.

## Sitting 2 — Control and functions

Notebook sections 5 and 6.

Outcome: write a search loop with `else`, a function with a keyword-only argument, and a closure that does not share one loop variable. Say when a default argument is evaluated, and why a default list is shared.

Exercises 4 to 6.

## Sitting 3 — Collections and iteration

Notebook sections 7 to 9.

Outcome: pick `list`, `tuple`, `set`, or `dict` for a stated job. Write a comprehension and a generator. Encode and decode a non-ASCII string. Explain why `join` replaces a loop of `+`.

Exercises 7 to 9.

## Sitting 4 — Failures, files, and objects

Notebook sections 10 to 12.

Outcome: translate an exception with `raise ... from`, read a text file with `pathlib` and `with`, and add a subclass that calls `super()`. Say why `__exit__` returning `False` matters.

Exercises 10 to 12.

## Sitting 5 — Idioms

Notebook sections 13 to 16.

Outcome: write a decorator that keeps the wrapped function's name, name three standard-library types you would use before adding a dependency, and apply the closing checklist to a function you wrote.

## Sitting 6 — Calculator

[Project 1](capstones/01-calculator.md).

Outcome: trace `2 + 3 * 4` through the parser and say which method handles the multiplication. Add one operator only if you can name the grammar rule it belongs to.

Exercise 13.

## Sitting 7 — Games

[Project 2](capstones/02-tic-tac-toe.md) and [Project 3](capstones/03-hangman.md).

Outcome: explain why the board is a tuple, why the sample human loses, and why Hangman's win flag is a property rather than a stored Boolean. Point at the guess that must not cost a life.

Exercises 14 and 15.

## Sitting 8 — Records and money

[Project 4](capstones/04-quiz-master.md) and [Project 5](capstones/05-expense-tracker.md).

Outcome: mark a paper without a stored score, and total a month of expenses without binary float error. Say why September's row is absent from the October report, and why `Decimal` is built from a string.

Exercises 16 and 17.

## After the path

A reasonable next program, not included here, is a command-line wrapper around one capstone: `argparse`, and an `if __name__ == "__main__"` block. That step is small once the class boundary in the notebook is stable. Keep sample data out of the class, as the notebooks do.
