# Contributing

Thank you for considering an improvement to this repository. The material is teaching code. A change should make an explanation more accurate, an example easier to run, or a program easier to extend. It should not add a dependency unless the notebook cannot teach the idea without one.

## Before you start

- The project requires Python 3.10 or newer.
- Notebooks live in `notebooks/`. The importable form of a capstone lives in `src/nielit_python/`. Prose lives in `docs/`. Keep the three in agreement: if a class or a sample result changes, update the module, the notebook, and the matching document.
- Run `PYTHONPATH=src python3 -m unittest tests/test_modules.py` before opening a pull request that changes a module.
- Do not commit `.ipynb_checkpoints/`, virtual environments, or `__pycache__/`.

## How to propose a change

1. Fork the repository and create a branch from `main`.
2. Make the change in the notebook and, if the behaviour or the explanation changed, in `docs/`.
3. Restart the kernel and run the notebook from the top. Leave the captured output in the file so a reader on GitHub can see the result.
4. Open a pull request against `main`. Describe what changed and why a learner needs it.

A correction of a factual error, a broken cell, or a misleading sentence does not need a large design note. A new capstone does. Say what the program teaches that the existing five do not.

## Notebook conventions

- State the idea before the code.
- Keep each notebook runnable on its own. Do not import another notebook.
- Prefer the standard library.
- Use `Decimal` for money and an explicit encoding for text files.
- Raise a specific exception for bad input. Do not catch `Exception` unless the cell is demonstrating that pattern.
- Sample data belongs at the bottom of the program, not inside the class as a hidden global.

## Documentation conventions

- Write in complete sentences.
- Name the file and the class you are describing.
- If you claim an output, it must match a run of the current notebook.
- Relative links should work on GitHub from the file that contains them.

## Reporting a problem

Open an issue if a cell fails, an explanation disagrees with the code, or a requirement is missing. Include the Python version, the notebook path, and the traceback or the sentence you believe is wrong.

Security reports are unlikely to apply: this repository does not run a service and does not accept user data. If you believe a notebook teaches a dangerous pattern, open an issue and describe the pattern.
