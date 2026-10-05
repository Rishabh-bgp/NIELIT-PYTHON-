# Repository layout

```text
NIELIT-PYTHON-/
├── CITATION.cff
├── CODE_OF_CONDUCT.md
├── CONTRIBUTING.md
├── LICENSE
├── README.md
├── docs/
│   ├── README.md
│   ├── exercises.md
│   ├── faq.md
│   ├── further-reading.md
│   ├── getting-started.md
│   ├── glossary.md
│   ├── language-reference.md
│   ├── learning-path.md
│   ├── repository-layout.md
│   └── capstones/
│       ├── README.md
│       ├── 01-calculator.md
│       ├── 02-tic-tac-toe.md
│       ├── 03-hangman.md
│       ├── 04-quiz-master.md
│       └── 05-expense-tracker.md
└── notebooks/
    ├── README.md
    ├── python_mastery.ipynb
    └── capstones/
        ├── Project_01_Safe_Expression_Calculator.ipynb
        ├── Project_02_Tic_Tac_Toe.ipynb
        ├── Project_03_Hangman.ipynb
        ├── Project_04_Quiz_Master.ipynb
        └── Project_05_Expense_Tracker.ipynb
├── src/
│   └── nielit_python/
│       ├── __init__.py
│       ├── calculator.py
│       ├── tictactoe.py
│       ├── hangman.py
│       ├── quiz.py
│       └── ledger.py
├── tests/
│   └── test_modules.py
└── pyproject.toml
```

The notebooks are the reading form. `src/nielit_python/` is the import form of the five capstones. `tests/test_modules.py` checks the published samples with `unittest`. `pyproject.toml` names the package and declares no third-party dependencies.

## Why the notebooks are not at the root

The first commits placed every notebook at the repository root. That is convenient for a handful of files and awkward once documentation, a licence, and a citation file share the same directory. Notebooks now live under `notebooks/`. Capstones are one level deeper so the language reference stays visible beside them.

GitHub renders a notebook wherever it sits. Links in the README use the new paths.

## What each top-level file is for

- `LICENSE` is the MIT Licence. It is the legal grant. The README only summarises it.
- `CITATION.cff` is a machine-readable citation for the teaching set.
- `CONTRIBUTING.md` is the procedure for a pull request.
- `CODE_OF_CONDUCT.md` is the standard for discussion.
- `.gitignore` excludes checkpoint folders and bytecode, which Jupyter and Python create locally and which should not be committed.

## What is intentionally absent

There is no `requirements.txt`. The notebooks and the modules do not import a third-party package. `pyproject.toml` exists only to name the package, the licence, and the Python version; it does not list dependencies. Jupyter is a tool for reading the notebooks, not a library they import.

The test file covers the published samples. It is not a full specification. The capstone note remains the description of intended behaviour.
