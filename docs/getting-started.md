# Getting started

This page is the full local setup for every notebook in the repository. Nothing here requires an account, a cloud kernel, or a third-party scientific library.

## 1. Confirm the interpreter

The notebooks need Python 3.10 or newer. Four language features in the reference notebook decide that floor:

| Feature | Introduced | Where it appears |
| --- | --- | --- |
| `list[int]`, `dict[str, int]` at runtime | 3.9 | Type-hint section |
| `match` / `case` | 3.10 | Control-flow section |
| `X \| None` union syntax | 3.10 | Type-hint section |
| `zip(..., strict=True)` | 3.10 | Type-hint section |

Python 3.9 fails on the pattern-matching cell and on the union annotations. Python 3.11 and 3.12 run the published notebooks without change. A later 3.x release should also run them; the code does not depend on a removed feature.

```bash
python3 --version
```

If that command is missing, install Python from [python.org](https://www.python.org/downloads/) or from your system packages, then open a new terminal so `PATH` is refreshed. On Windows, `py -3 --version` is the equivalent check. The notebooks themselves are line-ending tolerant; Jupyter writes them as JSON.

## 2. Obtain the files

```bash
git clone https://github.com/Rishabh-bgp/NIELIT-PYTHON-.git
cd NIELIT-PYTHON-
```

A ZIP download from GitHub works as well. You do not need the `.git` directory to read or run the notebooks. You do need it if you intend to pull later corrections.

## 3. Install a Jupyter client

The notebooks do not import Jupyter. Jupyter is only the program that opens them. From the repository root:

```bash
python3 -m pip install notebook
python3 -m notebook
```

If you prefer not to install into the system interpreter:

```bash
python3 -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
python3 -m pip install notebook
python3 -m notebook
```

`.venv/` is listed in `.gitignore` and must not be committed. JupyterLab is an alternative frontend: `python3 -m pip install jupyterlab` and `python3 -m jupyter lab`. VS Code and Cursor open `.ipynb` files directly once a Python kernel is selected. Any of these is sufficient.

## 4. Open the right file

The browser file list is the repository root. Enter `notebooks/`, then open `python_mastery.ipynb` or a file under `notebooks/capstones/`. Do not look for the notebooks at the root. They were moved in the documentation commit so that licence, citation, and guides would not sit in the same list as the course.

## 5. Two ways to read a notebook

Stored output is part of the file. GitHub renders it, and Jupyter shows it before you execute anything. Those outputs were captured when the notebook was built. They are a reading aid, not a promise that `id()` will print the same integer on your machine.

A real run replaces that output:

1. Select the kernel named Python 3.
2. Choose **Restart kernel and run all**.
3. Confirm that the last cell of a capstone finishes without a traceback.

Run from the top after any edit. A later cell that uses a name from an earlier cell will fail if you run it alone after a restart. The capstones are each one code cell, so this mostly matters in the language reference.

## 6. What a failure usually means

| Symptom | Likely cause | What to do |
| --- | --- | --- |
| `SyntaxError` on `match` or on `list[int]` | Interpreter older than 3.10 | Install 3.10+ and point Jupyter at it |
| `Kernel not found` | Jupyter has no Python kernel registered | Run `python3 -m pip install ipykernel` in the environment you want to use |
| `NameError` in a later cell | Kernel was restarted, or an earlier cell was skipped | Restart and run all |
| `ModuleNotFoundError` | A local edit imported a third-party package | Remove the import, or install the package; the published notebooks do not need one |
| Output differs only in `id(...)` or a timestamp | Process identity and clock differ | Treat the rest of the line as the check |

Hangman defines `play_interactive`, which calls `input`. The published cell does not call it. A full run therefore does not wait for the keyboard. Call that function only when you intend to type.

## 7. Stay current

```bash
git pull origin main
```

Pull before editing if the remote may have changed. Notebook output is stored in the file, so a pull can conflict if you re-ran a notebook and the remote copy also changed. For an untouched notebook, keep the remote version and run it again locally.

## 8. Official documentation

This repository does not replace the Python manual. The current manual is <https://docs.python.org/3/>. The tutorial, the language reference, and the library page for each topic in these notebooks are listed in [Further reading](further-reading.md).
