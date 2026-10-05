# NIELIT Python

A public teaching repository for the Python language and five small, complete programs. It is written for learners who want the reason for a construct, not only the syntax, and for instructors who want a notebook they can run in class.

The repository is open source under the [MIT Licence](LICENSE). You may use, copy, modify, and redistribute the notebooks and the documentation, including in a course, provided the copyright notice and licence text travel with any substantial copy.

**Author:** Er. Rishabh Aryan  
**Repository:** https://github.com/Rishabh-bgp/NIELIT-PYTHON-

## What is in this repository

| Path | Purpose |
| --- | --- |
| [notebooks/python_mastery.ipynb](notebooks/python_mastery.ipynb) | Language reference: theory, examples, and captured output |
| [notebooks/capstones/](notebooks/capstones) | Five independent programs, from a calculator to a ledger |
| [docs/](docs) | Prose documentation for every notebook and for the learning path |
| [CONTRIBUTING.md](CONTRIBUTING.md) | How to propose a correction or a new notebook |
| [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) | Expected behaviour in issues and reviews |
| [LICENSE](LICENSE) | MIT Licence, copyright 2026 Er. Rishabh Aryan |

The notebooks are the primary material. The documents explain how to run them, what each section is for, and which design choice is worth copying into another program.

## Requirements

- Python 3.10 or newer. The reference notebook uses structural pattern matching and the `X | Y` union form, both of which require 3.10.
- A Jupyter client: JupyterLab, Jupyter Notebook, or VS Code with the Jupyter extension.
- No third-party packages. Every example uses the standard library.

Check the interpreter before opening a notebook:

```bash
python3 --version
```

## Run the notebooks

Clone the repository and start Jupyter from the repository root.

```bash
git clone https://github.com/Rishabh-bgp/NIELIT-PYTHON-.git
cd NIELIT-PYTHON-
python3 -m pip install notebook
python3 -m notebook
```

Open a notebook from `notebooks/`. Use **Restart kernel and run all** so the captured output is replaced by a run on your machine. Each notebook is independent. A capstone does not import the language reference.

If `python3 -m notebook` is not available, install JupyterLab instead and run `python3 -m jupyter lab`. The files are ordinary `.ipynb` documents and do not depend on a particular frontend.

## Suggested order

1. Read [docs/getting-started.md](docs/getting-started.md).
2. Work through [notebooks/python_mastery.ipynb](notebooks/python_mastery.ipynb), using [docs/language-reference.md](docs/language-reference.md) as the section guide.
3. Build the capstones in order. The calculator practises parsing and errors. Tic-tac-toe and Hangman practise state. The quiz practises records. The expense tracker practises dates and exact decimal money.
4. Use [docs/learning-path.md](docs/learning-path.md) if you are teaching the set as a short course.

## Capstone index

| Notebook | Subject | Main ideas |
| --- | --- | --- |
| [Calculator](notebooks/capstones/Project_01_Safe_Expression_Calculator.ipynb) | Arithmetic expressions | Lexer, recursive descent, memory, history |
| [Tic-tac-toe](notebooks/capstones/Project_02_Tic_Tac_Toe.ipynb) | Two-player game | Immutable board, minimax |
| [Hangman](notebooks/capstones/Project_03_Hangman.ipynb) | Word game | State machine, derived win condition |
| [Quiz master](notebooks/capstones/Project_04_Quiz_Master.ipynb) | Marked test | Frozen records, score as a property |
| [Expense tracker](notebooks/capstones/Project_05_Expense_Tracker.ipynb) | Monthly ledger | `Decimal`, filtering, budget alerts |

Detailed notes for each program are in [docs/capstones/](docs/capstones).

## Design rules used in the code

- Names are labels. Mutation and rebinding are kept distinct.
- Mutable default arguments are not used.
- Exceptions are specific, and a translated error keeps its cause.
- Files in the reference notebook are opened with `with` and an explicit encoding.
- Money uses `decimal.Decimal` constructed from strings.
- Public behaviour sits on a class. Demonstration data sits below the class, so the class can be reused without the sample.

## Licence and citation

This project is licensed under the MIT Licence. See [LICENSE](LICENSE).

If you use the material in teaching notes or a dissertation, a suitable citation is in [CITATION.cff](CITATION.cff). Attribution is not required by the MIT Licence beyond retaining the copyright and permission notice, but it is appreciated.

## Contributing

Corrections to an explanation, a failing example, and new capstones are welcome. Read [CONTRIBUTING.md](CONTRIBUTING.md) before opening a pull request. Behaviour in issues and reviews is covered by [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).
