# Learning path

A short course built only from this repository. Each sitting assumes the previous one. Times are reading-and-running time, not lecture time.

## Sitting 1 — Objects and names

Notebook sections 1 to 4.

Outcome: explain why two names can see one `append`, why `0.1 + 0.2` is not `0.3`, and why `and` can return a string. Be able to choose `is` or `==` for a `None` test without looking it up.

## Sitting 2 — Control and functions

Notebook sections 5 and 6.

Outcome: write a search loop with `else`, a function with a keyword-only argument, and a closure that does not share one loop variable across every returned function. Be able to say when a default argument is evaluated.

## Sitting 3 — Collections and iteration

Notebook sections 7 to 9.

Outcome: pick `list`, `tuple`, `set`, or `dict` for a stated job. Write a comprehension and a generator. Encode and decode a non-ASCII string.

## Sitting 4 — Failures, files, and objects

Notebook sections 10 to 12.

Outcome: translate an exception with `raise ... from`, read a text file with `pathlib` and `with`, and add a subclass that calls `super()`.

## Sitting 5 — Idioms

Notebook sections 13 to 16.

Outcome: write a decorator that keeps the wrapped function's name, name three standard-library types you would use before adding a dependency, and read the closing checklist against a function you wrote.

## Sitting 6 — Calculator

[Project 1](capstones/01-calculator.md).

Outcome: trace `2 + 3 * 4` through the parser and say which method handles the multiplication. Add one operator only if you can name the grammar rule it belongs to.

## Sitting 7 — Games

[Project 2](capstones/02-tic-tac-toe.md) and [Project 3](capstones/03-hangman.md).

Outcome: explain why the tic-tac-toe board is a tuple, and why Hangman's win flag is a property rather than a stored Boolean.

## Sitting 8 — Records and money

[Project 4](capstones/04-quiz-master.md) and [Project 5](capstones/05-expense-tracker.md).

Outcome: mark a paper without a stored score, and total a month of expenses without binary float error. Be able to say why September's row does not appear in the October report.

## After the path

A reasonable next program, not included here, is a command-line wrapper around one capstone: argument parsing with `argparse`, and a `if __name__ == "__main__"` block. That step is small once the class boundary in the notebook is stable.
