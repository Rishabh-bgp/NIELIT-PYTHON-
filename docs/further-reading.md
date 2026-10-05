# Further reading

The notebooks and modules in this repository are a teaching selection. They are not a substitute for the language specification or the library manual. When a section here is not enough, the official Python documentation is the authority.

The current stable manual is at <https://docs.python.org/3/>. That URL always points at the latest 3.x release. To match the 3.10 floor used by this repository, open the version menu on any page and select 3.10 or newer. A feature introduced after 3.10 is marked on the page.

## Start here

| If you want | Official page |
| --- | --- |
| A guided tour of the language | [The Python Tutorial](https://docs.python.org/3/tutorial/index.html) |
| The meaning of a statement or expression | [The Python Language Reference](https://docs.python.org/3/reference/index.html) |
| A function or type in the standard library | [The Python Standard Library](https://docs.python.org/3/library/index.html) |
| How to install and run Python | [Python Setup and Usage](https://docs.python.org/3/using/index.html) |
| What changed in a release | [What's New in Python](https://docs.python.org/3/whatsnew/index.html) |
| The glossary used by the documentation itself | [Glossary](https://docs.python.org/3/glossary.html) |

The tutorial is the right next page after `notebooks/python_mastery.ipynb`. The language reference is the right page when a note in this repository and an experiment disagree: the reference wins.

## Pages that match this repository

The left column is a section or module in this repository. The right column is the official page that covers the same idea in full.

| This repository | Official documentation |
| --- | --- |
| Execution model, names, objects | [Data model](https://docs.python.org/3/reference/datamodel.html) |
| `import` and modules | [The import system](https://docs.python.org/3/reference/import.html) |
| Expressions, operators, precedence | [Expressions](https://docs.python.org/3/reference/expressions.html) |
| `if`, `for`, `while`, `match` | [Compound statements](https://docs.python.org/3/reference/compound_stmts.html) |
| Functions, arguments, decorators | [Function definitions](https://docs.python.org/3/tutorial/controlflow.html#defining-functions) and [function definitions in the reference](https://docs.python.org/3/reference/compound_stmts.html#function-definitions) |
| `lambda`, `map`, scope | [More on defining functions](https://docs.python.org/3/tutorial/controlflow.html#more-on-defining-functions) and [naming and binding](https://docs.python.org/3/reference/executionmodel.html) |
| Strings and formatting | [Text sequence type](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str) and [Format string syntax](https://docs.python.org/3/library/string.html#format-string-syntax) |
| `list`, `tuple`, `dict`, `set` | [Built-in types](https://docs.python.org/3/library/stdtypes.html) and [Data structures](https://docs.python.org/3/tutorial/datastructures.html) |
| Comprehensions, iterators, generators | [Iterators](https://docs.python.org/3/tutorial/classes.html#iterators) and [Generators](https://docs.python.org/3/tutorial/classes.html#generators) |
| Exceptions | [Errors and exceptions](https://docs.python.org/3/tutorial/errors.html) and [the raise statement](https://docs.python.org/3/reference/simple_stmts.html#the-raise-statement) |
| `with`, files, `pathlib` | [The with statement](https://docs.python.org/3/reference/compound_stmts.html#the-with-statement), [open](https://docs.python.org/3/library/functions.html#open), and [pathlib](https://docs.python.org/3/library/pathlib.html) |
| Classes, `super`, properties | [Classes](https://docs.python.org/3/tutorial/classes.html) |
| Dataclasses | [dataclasses](https://docs.python.org/3/library/dataclasses.html) |
| Decorators and `functools` | [functools](https://docs.python.org/3/library/functools.html) |
| `collections`, `itertools`, `math`, `json`, `datetime` | [collections](https://docs.python.org/3/library/collections.html), [itertools](https://docs.python.org/3/library/itertools.html), [math](https://docs.python.org/3/library/math.html), [json](https://docs.python.org/3/library/json.html), [datetime](https://docs.python.org/3/library/datetime.html) |
| Type hints | [typing](https://docs.python.org/3/library/typing.html) and [PEP 484](https://peps.python.org/pep-0484/) |
| `Decimal` in the ledger | [decimal](https://docs.python.org/3/library/decimal.html) |
| `unittest` in `tests/` | [unittest](https://docs.python.org/3/library/unittest.html) |

`match` was added in 3.10. Its official description is in [PEP 634](https://peps.python.org/pep-0634/), [PEP 635](https://peps.python.org/pep-0635/), and [PEP 636](https://peps.python.org/pep-0636/). The assignment expression `:=` is [PEP 572](https://peps.python.org/pep-0572/).

## How to use a documentation page

Each library page names the version that added a function, the arguments, and the exceptions. Prefer that page to a blog post when the question is "what does this do". Prefer the tutorial when the question is "where does this idea fit". Prefer the language reference when the question is "what is this required to mean".

This repository does not mirror those pages. A link above is an invitation to read them, not a copy.
