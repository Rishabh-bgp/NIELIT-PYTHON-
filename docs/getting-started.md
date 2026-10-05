# Getting started

This page is the minimum needed to run every notebook in the repository on a local machine.

## Interpreter

Install Python 3.10 or newer. The language reference uses:

- `match` / `case`, added in Python 3.10
- `list[int]` and `dict[str, int]` as runtime-available built-in generics, preferred from 3.9
- `X | None` union syntax, added in 3.10
- `zip(..., strict=True)`, added in 3.10

Python 3.9 will fail on the pattern-matching cell and on the union annotations. Python 3.11 and 3.12 run the notebooks without change.

Confirm the version:

```bash
python3 --version
```

No virtual environment is required, because the notebooks do not import third-party packages. A virtual environment is still reasonable if you do not want Jupyter installed into the system interpreter:

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install notebook
```

## Jupyter

From the repository root:

```bash
python3 -m notebook
```

The browser opens a file list. Enter `notebooks/`, then open `python_mastery.ipynb` or a file under `notebooks/capstones/`.

Two ways to read a notebook:

- Read the stored output on GitHub or in Jupyter without executing. The outputs were captured when the notebook was built.
- Restart the kernel and run all cells. Do this after any edit. Identity values from `id()` will differ from the stored output; that is expected, because identity is a property of the running process.

## What a failed cell usually means

- `SyntaxError` on `match` or on `list[int]`: the interpreter is older than 3.10.
- `ModuleNotFoundError`: the notebook was changed to import a package that is not installed. The published notebooks do not do this.
- A name error in a later cell: the kernel was not restarted, or an earlier cell was skipped. Run from the top.

## Keyboard input

Hangman includes `play_interactive`, which calls `input`. The published cell does not call it, so the notebook finishes without waiting. Call that function yourself only in a terminal or in a notebook session where you intend to type.

## Updating a local copy

```bash
git pull origin main
```

Pull before editing if the remote may have changed. Local notebook output can conflict on pull; if it does, keep the remote version of an untouched notebook and re-run.
