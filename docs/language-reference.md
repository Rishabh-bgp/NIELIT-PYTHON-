# Language reference

Section notes for [notebooks/python_mastery.ipynb](../notebooks/python_mastery.ipynb). Read a section here, then run the matching cells. Each note states the claim the section is making, what the cell is evidence for, and the mistake that section is meant to prevent.

Restart the kernel and run from the top after you edit a cell. Later sections do not need names from earlier ones, but a stale object from an edited cell will confuse a re-run of that cell alone.

## 1. The execution model

**Claim.** CPython compiles source to bytecode and executes that bytecode. You almost never invoke the compiler yourself. Three consequences matter more than the compiler: every value is an object, a name is a binding, and the type system is dynamic and strong.

An object has identity, type, and value. `id(x)` is identity. `type(x)` is the type. The value is what the object means. Assignment binds a name in a namespace to an object. It does not copy the value into a variable-shaped box. Dynamic means a name may later refer to an object of another type. Strong means an operation still refuses a nonsense combination: `"3" + 4` raises `TypeError` rather than producing `"34"` or `7`.

CPython reclaims memory with reference counting and a cyclic garbage collector. You do not free objects. You do have to know when two names share an object, because an in-place change is visible through every name.

**What the cell shows.** The type name of `10`, its identity, and the local names stored on `add`. The identity will differ on your machine. `co_varnames` will still be `('a', 'b')`. `co_consts` contains `None` because a function body has an implicit `None` constant even when every path returns a value.

**Mistake this prevents.** Treating a variable as a box that owns a copy. That model fails as soon as two names refer to one list.

## 2. Names, binding, and mutability

**Claim.** Lookup follows LEGB: local, then enclosing function scopes, then the module global namespace, then builtins. Assignment creates a local name unless `global` or `nonlocal` is declared. Reading a global needs no declaration. Writing one does.

Mutability is a property of the object. Immutable in the examples: `int`, `float`, `complex`, `bool`, `str`, `tuple`, `frozenset`, `bytes`, `None`. Mutable: `list`, `dict`, `set`, `bytearray`, and most user-defined objects.

`a = b` makes an alias. `a.append(4)` mutates the shared list. `a = a + [4]` would rebind `a` and leave `b` alone. `list.copy` is a shallow copy: a new list, same elements. That is enough when the elements are integers. It is not enough when the elements are themselves lists; use `copy.deepcopy` for that case, which this cell does not need.

`is` compares identity. `==` compares value. Use `is` for `None`, `True`, and `False`. Use `==` for data.

**What the cell shows.** After `append`, `b` sees `4` and the copy does not. Small integers and short strings may share identity because CPython interns them. Do not write program logic that depends on that interned identity.

**Mistake this prevents.** Using `is` to compare strings or numbers that you built separately, and using a copy when you meant an alias, or the reverse.

## 3. Scalar types

**Claim.** `int` is arbitrary precision. `10_000_000`, `0b1010`, `0o17`, and `0xFF` are the same kind of object with different literal syntax. `2 ** 100` does not overflow.

`float` is IEEE-754 binary64. `0.1 + 0.2` prints a value that is not exactly `0.3`. Round for display, or use `decimal.Decimal` constructed from a string when the decimal value is the data. Constructing `Decimal` from a float captures the binary error first.

`bool` is a subclass of `int`. `True + True` is `2`. That is occasionally useful and often a trap in an API that should have been Boolean. `None` is the only instance of `NoneType` and means "no value", not zero. `complex` stores a real and an imaginary part; `abs(3 + 4j)` is `5`. Application code rarely needs `complex`. Numeric code sometimes does.

**Mistake this prevents.** Using `float` for money, and treating `None` as a false stand-in for zero in stored data.

## 4. Operators, precedence, and truthiness

**Claim.** `**` binds tightest, then unary plus and minus, then `*`, `/`, `//`, `%`, then `+` and `-`. Comparisons chain: `1 < x < 10` evaluates `x` once.

`/` always returns a float. `//` floors toward negative infinity, so `(-7) // 2` is `-4`, not `-3`. `%` takes the sign of the divisor. Bitwise operators work on the integer representation and are not Boolean operators. `and` and `or` short-circuit and return the last evaluated operand, which may be a string or a number.

An object is false when `__bool__` returns false or, failing that, when `__len__` is zero. The false set to memorise: `None`, `False`, numeric zero, empty `str`, empty containers. `[0]` is true. The list is not empty.

**Mistake this prevents.** Writing `if items` and believing it tests for `None` only, and expecting `//` on negatives to match C truncation.

## 5. Control flow

**Claim.** `if` / `elif` / `else` selects one branch. `for` iterates an iterable; it does not count unless you give it a `range`. `range(10**9)` does not allocate a billion integers. `break` leaves the nearest loop. `continue` skips to the next iteration. A loop `else` runs only if the loop was not left by `break`. That is the clean form of "search failed".

`match` / `case`, from 3.10, matches structure. The cell matches a command tuple and binds `n` and `direction`, with a guard that `n` is positive. The walrus operator assigns inside the condition that needs the assigned value. The cell uses it to strip a string and keep only the non-empty results.

**What the cell shows.** Grade `B` for 86, an enumeration of `"py"`, a search that finds `9` and therefore does not run the loop `else`, a move command, and the cleaned list `['ALPHA', 'BETA', 'GAMMA']`.

**Mistake this prevents.** Using a flag variable for a failed search when `for` / `else` already expresses it, and writing a `match` case that accepts a zero step because the guard was forgotten.

## 6. Functions, scope, and argument forms

**Claim.** `def` binds the function name when the definition executes. Defaults are evaluated then, not at the call. A mutable default is shared across calls. The repair is a `None` sentinel and a new container inside the body.

Argument forms, in order: positional-only before `/`, positional or keyword, `*args`, keyword-only after `*`, `**kwargs`. The sample `scale` has a normal `factor` and a keyword-only `strict`. Returning several values returns one tuple.

A closure looks up the enclosing name when it runs. A loop that builds lambdas without a default captures the final loop value in every function. The cell passes `i=i` so each function keeps its own integer. `lambda` is appropriate as a key function and a poor substitute for `def` once you need a docstring or more than one expression.

**What the cell shows.** Shared state in `bad` (`[1]` then `[1, 2]`) and separate lists in `good`.

**Mistake this prevents.** A default of `[]` or `{}` on a public function.

## 7. Strings and text

**Claim.** `str` is an immutable sequence of Unicode code points, not bytes. Indexing raises on a bad index. Slicing does not. Encoding is text to bytes. Decoding is the reverse. That conversion belongs at the edge of the program. UTF-8 is the default unless a format demands otherwise.

Prefer f-strings for interpolation you can see in the source. Use `str.format` when the template arrives from outside. Use `%` only to match an old interface. Concatenate many strings with `str.join`.

**What the cell shows.** `strip`, `title`, `split`, `join`, membership, UTF-8 round trip of `café`, an f-string with a format spec and `!r`, `removesuffix`, and `casefold` so `αβγ` and `ΑΒΓ` compare equal.

**Mistake this prevents.** Treating a `str` as a sequence of bytes, and building a long line with `+` in a loop.

## 8. Lists, tuples, sets, and dictionaries

**Claim.** These four cover most in-memory records.

| Type | Ordered | Mutable | Hashable | Use |
| --- | --- | --- | --- | --- |
| `list` | yes | yes | no | a sequence you will change |
| `tuple` | yes | no | yes, if items are | a fixed record, a dict key |
| `set` | no | yes | no | membership and uniqueness |
| `dict` | insertion order | yes | no | labelled records, indexes |

Hashability needs a stable hash consistent with `__eq__`. Append on a list is amortised constant time. Insert at the front is linear. `sort` is in place and stable. `sorted` returns a new list. A one-element tuple is `(1,)`. Set operators: `|` union, `&` intersection, `-` difference, `^` symmetric difference. `d[k]` raises `KeyError`. `d.get(k, default)` does not.

**What the cell shows.** A sorted copy that leaves the original unsorted, then an in-place sort, a slice and a reversal, starred unpacking, set algebra printed as three separate results, and a frequency table built with `get`.

**Mistake this prevents.** Using a list as a dict key, and writing `d[k]` for a lookup that is allowed to miss.

## 9. Comprehensions, iterators, and generators

**Claim.** A comprehension is a filter and a transform in one expression. Parentheses produce a generator expression, which does not build the whole collection. The iteration protocol is `__iter__` then `__next__` until `StopIteration`. A generator function uses `yield`. Calling it returns a generator; the body runs on `next`. `yield from` delegates to another iterable.

**What the cell shows.** Even squares, a set of lengths, a word index, a generator that yields one square and then the rest, a countdown, and a flattened list of rows.

**Mistake this prevents.** Building a list of a million rows when the next stage only needs one row at a time.

## 10. Exceptions

**Claim.** An exception is an object, not a special return code. `else` on `try` runs if nothing escaped. `finally` runs on the way out, including on `return`. Catch the narrowest type you can recover from. A bare `except` also catches `KeyboardInterrupt` and `SystemExit`. `raise` with no argument re-raises and keeps the traceback. `raise NewError(...) from exc` chains the cause.

Exceptions are for conditions the immediate block cannot handle. A missing key on a hot lookup may be cheaper as a membership test. A missing file at the boundary is a fair use of `FileNotFoundError`.

**What the cell shows.** `parse_age("30")` returns 30. `parse_age("thirty")` raises `ValueError` whose `__cause__` is the original `ValueError` from `int`.

**Mistake this prevents.** Replacing the cause with a new message and throwing the traceback away.

## 11. Files and context managers

**Claim.** `with` calls `__enter__` before the block and `__exit__` afterwards, including when the block raises. Open text with an encoding. Modes: `"r"`, `"w"` (truncates), `"a"`, `"x"`, and `"b"` for binary. `pathlib.Path` composes paths with `/` and can read or write a small file. Iterate a file object for a large file; `read()` is for a small one.

**What the cell shows.** Three lines written under `/tmp/python_mastery_demo`, read back without newlines, the file size, and a timing context manager whose `__exit__` returns `False` so it does not suppress exceptions.

**Mistake this prevents.** Opening a file and relying on the process exit to close it.

## 12. Object-oriented programming

**Claim.** A class is a blueprint and a namespace. `__init__` initialises. Methods take the instance as `self`. `@classmethod` receives the class and is the right alternative constructor. `@staticmethod` receives neither. `@property` is a derived value or a guarded attribute. Inheritance reuses and overrides. Call the parent with `super()`, not by naming the parent, so multiple inheritance keeps working.

`__repr__` should be unambiguous. If you define `__eq__` and the object is mutable, set `__hash__ = None`. A frozen dataclass can be hashed because it cannot change. Dataclasses do not replace a class whose behaviour dominates its fields. `Account` is that kind of class. `Point` is a record.

**What the cell shows.** A deposit, interest applied to 1250 at 2 percent, and a hashed point.

**Mistake this prevents.** Naming the parent class in every override, and hashing a mutable account.

## 13. Decorators and functional tools

**Claim.** A decorator is a function from function to function. `functools.wraps` copies `__name__` and `__doc__` onto the wrapper so the decorated function still reports `area` and its docstring. `lru_cache` memoises a pure function. `partial` freezes arguments. A comprehension is usually clearer than `map` plus `lambda`. `sorted(..., key=)` is the idiomatic ordering tool.

**What the cell shows.** Traced calls, Fibonacci values 0 through 34 via the cache, `partial(max, 0)` used as a clamp at zero, and words sorted by length.

**Mistake this prevents.** A wrapper that hides the wrapped function's name from tracebacks and help().

## 14. Modules and a curated standard library

**Claim.** A module is a file. A package is a directory of modules. Import executes the module once and stores it in `sys.modules`. `if __name__ == "__main__"` lets a file be both importable and a script.

Reach for the standard library first. The cell uses `Counter`, `defaultdict`, `deque`, `itertools.pairwise`, `math.hypot`, `json`, and a timezone-aware `datetime`. Those cover counting, grouped maps, a double-ended queue, adjacent pairs, a length, text interchange, and civil time.

**Mistake this prevents.** Adding a dependency for a counter or a JSON load.

## 15. Type hints and modern idioms

**Claim.** Annotations are metadata. CPython does not enforce them. A checker such as mypy or pyright does, if you run one. Hints pay off on the public boundary. `list[int]` and `str | None` are the modern forms. A hinted function can still return the wrong type at runtime; the checker is part of the build, not a runtime guarantee.

Prefer unpacking to fixed indexes, comprehensions to `map` plus `lambda`, `enumerate` and `zip(..., strict=True)` to manual indexes, f-strings, `pathlib`, and `logging` once a program has a real runtime.

**What the cell shows.** A mean, an empty-list default of `None`, the annotation dictionary, and a strict zip.

**Mistake this prevents.** `zip` silently stopping at the shorter row when the rows were supposed to be the same length.

## 16. Closing object

`ReadingLog` is the bridge to the capstones. A frozen `Reading`, a classmethod that translates `KeyError` and `ValueError` into one domain error, a file opened with `with`, and a dict of averages. It is smaller than the five project notebooks on purpose. Extend those, not this cell, when you want a program rather than an illustration.

## 17. Checklist

Before calling an exercise finished: are you rebinding or mutating a shared object; are defaults immutable; are exceptions specific and chained; are files inside `with`; do equality and hashing agree; would a reader know the empty case and the failure case without running the code.
