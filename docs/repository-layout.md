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
│   ├── getting-started.md
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
```

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

There is no `requirements.txt` and no `pyproject.toml`. Adding either would suggest a dependency that the notebooks do not have. Jupyter is a tool for reading the files, not a library they import.

There is no test suite. Each capstone demonstrates itself at the bottom of the notebook. A later contribution can add tests if a program grows past what a single run can show.
