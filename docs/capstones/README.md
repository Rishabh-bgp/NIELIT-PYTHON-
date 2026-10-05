# Capstone notes

Each note matches one notebook under [notebooks/capstones](../../notebooks/capstones). The same program is also a module under `src/nielit_python/`. The note is longer than the notebook introduction: it walks the sample, names the responsibility of each type, and states the limit of the published program. The notebook remains the reading form. The module is the import form. Commands are in [the module guide](../python-modules.md).

| Note | Notebook | What the note adds |
| --- | --- | --- |
| [01 — Calculator](01-calculator.md) | `Project_01_Safe_Expression_Calculator.ipynb` | Grammar and a step trace of `2 + 3 * 4` |
| [02 — Tic-tac-toe](02-tic-tac-toe.md) | `Project_02_Tic_Tac_Toe.ipynb` | Search rules and the three-move sample |
| [03 — Hangman](03-hangman.md) | `Project_03_Hangman.ipynb` | Guess table and the repeated-letter check |
| [04 — Quiz master](04-quiz-master.md) | `Project_04_Quiz_Master.ipynb` | Why the score is not stored |
| [05 — Expense tracker](05-expense-tracker.md) | `Project_05_Expense_Tracker.ipynb` | Row table, exact money, excluded September |

Shared rules:

- The program is one cell, so it can be copied out as a module.
- Sample input sits under the class and prints a result. That result is the check against the note.
- No notebook imports another notebook.
- Extensions that are not implemented are listed as exercises in [docs/exercises.md](../exercises.md).
