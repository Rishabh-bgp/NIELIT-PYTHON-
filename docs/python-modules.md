# Python modules

The notebooks are the narrative form of this course. The same five programs also live as importable modules under `src/nielit_python/`. Use the notebook to read the idea. Use the module when you want to import it, run it from a terminal, or test it.

No third-party package is required. The tests use `unittest` from the standard library.

## Layout

| Module | Public names | Notebook |
| --- | --- | --- |
| `nielit_python.calculator` | `Calculator`, `CalculatorError`, `Lexer`, `Parser` | Project 1 |
| `nielit_python.tictactoe` | `Game`, `minimax`, `best_move`, `render` | Project 2 |
| `nielit_python.hangman` | `Hangman`, `play_interactive` | Project 3 |
| `nielit_python.quiz` | `Question`, `Attempt`, `PAPER` | Project 4 |
| `nielit_python.ledger` | `Expense`, `Ledger`, `sample_ledger` | Project 5 |

`nielit_python/__init__.py` re-exports the names a caller is most likely to import. The version string is `__version__`.

## Run a demonstration

From the repository root, with `src` on the path:

```bash
PYTHONPATH=src python3 -m nielit_python.calculator
PYTHONPATH=src python3 -m nielit_python.tictactoe
PYTHONPATH=src python3 -m nielit_python.hangman
PYTHONPATH=src python3 -m nielit_python.quiz
PYTHONPATH=src python3 -m nielit_python.ledger
```

Each module's `demo` function prints the same sample as the matching notebook. `if __name__ == "__main__"` calls `demo`, so the file is both importable and a script. Hangman's `play_interactive` is not called by `demo`; it waits for keyboard input and is for a terminal session only.

## Import

```python
from nielit_python.calculator import Calculator

calculator = Calculator()
print(calculator.evaluate("2 + 3 * 4"))
```

Run that with `PYTHONPATH=src`, or install the tree in editable form. There are no install requirements:

```bash
python3 -m pip install -e .
```

`pyproject.toml` declares the package, the MIT licence, and Python 3.10 as the floor. It does not declare a dependency.

## Tests

```bash
PYTHONPATH=src python3 -m unittest tests/test_modules.py
```

The tests cover the published samples: calculator precedence and an unrecorded division by zero, the tic-tac-toe loss for those human moves, the Hangman repeat, the 4/5 quiz, and the exact October food total. They are a check, not a specification. The specification is the capstone note beside each module.

## What belongs in a module

A class and its rules belong in the module. Sample rows and the printed demonstration belong in `demo` or `sample_ledger`, not in the class body. That split is why the notebook cell and the module can stay equivalent: the notebook cell is the module followed by the call to `demo`.
