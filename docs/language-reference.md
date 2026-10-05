# Language reference

Guide to [notebooks/python_mastery.ipynb](../notebooks/python_mastery.ipynb). The notebook is the worked text. This page says what each section is trying to establish, and what a reader should be able to do after it.

Run the notebook from the top after a kernel restart. Later sections do not depend on names defined earlier, but a restart avoids a stale object from an edited cell.

## 1. The execution model

CPython compiles source to bytecode and executes that bytecode on a stack machine. You do not manage that step. You do need the three consequences that the section names.

Everything is an object, with an identity, a type, and a value. `id` reports identity. `type` reports the type. Assignment does not copy the object into the name; it binds the name to the object. Typing is dynamic, so a name may later refer to another type, and strong, so `"3" + 4` is an error rather than a silent conversion.

The cell prints the type and identity of an integer and the local names stored on a small function's code object. The identity will not match the stored output on another machine. The type name and the code-object names will.

## 2. Names, binding, and mutability

Lookup follows LEGB: local, enclosing, global, built-in. Assignment is local unless `global` or `nonlocal` says otherwise.

Mutability belongs to the object. `list`, `dict`, and `set` can change in place. `int`, `str`, and `tuple` cannot. Two names bound to one list are aliases: `append` through one name is visible through the other. `list.copy` is a shallow copy, enough when the elements are immutable.

Use `is` for `None`. Use `==` for values. The cell shows an alias, a shallow copy, and the interned identity of a small integer and a short string. Interning is a CPython detail, not a rule to rely on in program logic.

## 3. Scalar types

`int` has arbitrary precision. `float` is binary64, so `0.1 + 0.2` is not exactly `0.3`. `Decimal` constructed from strings is the right tool when the decimal value matters. `bool` is a subclass of `int`, which the cell demonstrates with `True + True`. `None` is a single object. `complex` is included so the numeric tower is complete; most application code will not need it.

## 4. Operators, precedence, and truthiness

`/` is true division and returns a float. `//` is floor division, which for negatives goes toward negative infinity, not toward zero. `%` takes the sign of the divisor. Comparisons chain, and the middle expression is evaluated once.

`and` and `or` return the last evaluated operand. They are not required to return `True` or `False`. An object is false when `__bool__` says so, or when `__len__` is zero. The cell prints the false set: `None`, `False`, numeric zero, and empty containers.

## 5. Control flow

`if` selects a branch. `for` iterates. `range` is lazy. `break` leaves the nearest loop. A loop `else` runs only when the loop was not left by `break`, which is the right tool for a failed search. `match` matches structure, including a guard. The walrus operator `:=` assigns inside an expression; the cell uses it to strip and test a string in one step.

## 6. Functions, scope, and argument forms

Defaults are evaluated once, at definition. A mutable default is therefore shared, and the cell shows both the trap and the `None` sentinel. Argument order is positional-only, then positional-or-keyword, then `*args`, then keyword-only, then `**kwargs`. The sample function uses a keyword-only flag.

A closure looks up the enclosing variable when it runs. The cell captures the loop index with a default argument so each function keeps the value from its own iteration. A returned function is an ordinary object.

## 7. Strings and text

A `str` is a sequence of Unicode code points. Encoding produces `bytes`. The program boundary — files, sockets, subprocesses — is where that conversion belongs. The cell encodes and decodes `café` as UTF-8, formats with an f-string, and uses `casefold` for case-insensitive comparison of non-ASCII text.

Join many strings with `str.join`. Repeated `+` in a loop is the pattern to avoid.

## 8. Lists, tuples, sets, and dictionaries

Lists are ordered and mutable. Tuples are ordered records; a one-element tuple needs a trailing comma. Sets give membership and uniqueness. Dicts preserve insertion order and require hashable keys.

The cell sorts a copy and then sorts in place, slices, unpacks with a starred middle, and builds a frequency table with `dict.get`. Set operations are written with parentheses in mind: union, difference, and intersection are printed separately so precedence cannot hide the result.

## 9. Comprehensions, iterators, and generators

A comprehension builds a list, set, or dict. Parentheses build a generator expression, which yields on demand. `for` is the iterator protocol: `__iter__`, then `__next__` until `StopIteration`. A generator function uses `yield` and does not run until it is advanced. `yield from` delegates to another iterable. The cell flattens a list of rows with that form.

## 10. Exceptions

`try` protects a region. `except` handles a matching type. `else` runs when nothing escaped. `finally` runs on the way out. The sample parses an age, translates `ValueError`, and chains the original with `raise ... from`. The printed cause is the original conversion error, not a lost traceback.

Handle the narrowest type you can recover from. Do not use a bare `except`.

## 11. Files and context managers

`with` calls `__enter__` and `__exit__`. File objects use that protocol so the file closes when parsing fails. Open text with an encoding. `pathlib.Path` composes paths with `/` and can read or write a small file directly. The cell writes three lines under `/tmp`, reads them back, and shows a small timing context manager. `__exit__` returns `False` so it does not suppress an exception.

## 12. Object-oriented programming

Instantiation runs `__init__` after allocation. `@property` exposes a method as an attribute. `@classmethod` is the right place for an alternative constructor; the capstone ledger uses that idea again. `super()` calls the next implementation in the method resolution order.

A frozen dataclass generates `__init__`, `__repr__`, and `__eq__`, and can be hashed because the instance cannot change. The cell builds a savings account, applies interest, and hashes a point.

## 13. Decorators and functional tools

`@decorator` is `fn = decorator(fn)`. `functools.wraps` copies the name and docstring onto the wrapper. `lru_cache` memoises a pure function; the cell uses it for Fibonacci. `partial` freezes an argument. `sorted(..., key=)` is preferred to sorting with a comparison function.

## 14. Modules and a curated standard library

Import executes a module once and caches it on `sys.modules`. The cell does not illustrate that cache; it illustrates the types a small program actually reaches for: `Counter`, `defaultdict`, `deque`, `itertools.pairwise`, `math.hypot`, `json`, and a timezone-aware `datetime`. Prefer these to a third-party package until the standard library is genuinely insufficient.

## 15. Type hints and modern idioms

Annotations are not enforced by CPython. They document the boundary and give a type checker something to verify. The cell annotates a mean function and an optional return, prints the annotation dictionary, and zips two rows with `strict=True` so a length mismatch fails immediately.

## 16. Capstone inside the reference

The closing class, `ReadingLog`, is a bridge to the project notebooks. It uses a frozen dataclass, a classmethod constructor, a generator-style file loop, a context manager, and a dict of averages. It is deliberately smaller than the five capstones. Those notebooks are the place to extend the same ideas.

## 17. Checklist

The final cell is a list of questions, not code. Use it before treating a notebook exercise as finished: shared mutation, default arguments, exception scope, `with`, equality and hashing, and hints on the public boundary.
