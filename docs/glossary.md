# Glossary

Terms used in the notebooks and the capstone notes. Definitions are the ones this repository relies on, not every sense of the word in the wider literature.

**Alias.** A second name bound to an object that already has a name. `b = a` after `a = [1]` makes `a` and `b` aliases. An in-place change is visible through both.

**Binding.** The association of a name with an object in a namespace. Assignment binds. It does not copy the object into a box.

**Bytecode.** The intermediate form CPython produces from a source file or a function body before execution. Visible indirectly through a function's `__code__` object.

**Closure.** A nested function that uses a name from an enclosing function. The name is looked up when the inner function runs.

**Context manager.** An object with `__enter__` and `__exit__`, used by `with`. File objects are context managers. The expense and file sections use them so cleanup does not depend on the block succeeding.

**Decorator.** A callable that accepts a function and returns a replacement. `@trace` above `def` is `fn = trace(fn)` after the definition.

**Dynamic typing.** A name may be rebound to an object of a different type later in the program. The type belongs to the object, not to the name.

**Floor division.** `//`. The quotient rounded toward negative infinity. Not the same as truncating toward zero for negative operands.

**Hashable.** An object that can be a set element or a dict key. It needs a stable hash consistent with equality. Immutable built-ins usually qualify; lists and dicts do not.

**Identity.** The value reported by `id`. Two names with the same identity refer to the same object. Identity is not a value you should store for later comparison across processes.

**Immutable.** An object whose value cannot be changed in place. A new value requires a new object. `int`, `str`, and `tuple` are immutable.

**Iterable.** An object that can produce an iterator, usually by implementing `__iter__`. Lists, dicts, files, and generators are iterable.

**Iterator.** An object with `__next__` that yields items until it raises `StopIteration`. A `for` loop is this protocol plus cleanup.

**LEGB.** The name-lookup order: local, enclosing, global, built-in.

**Method resolution order.** The linear order in which Python searches classes for an attribute. `Class.__mro__` shows it. `super()` follows it rather than a hard-coded parent name.

**Minimax.** A search that assigns a score to a finished game and chooses the move whose worst reply is best for the player about to move. Used by the tic-tac-toe opponent.

**Mutable.** An object that can be changed in place. `list`, `dict`, `set`, and most user-defined instances are mutable. Mutation is visible through every alias.

**Namespace.** A mapping from names to objects. A function has a local namespace. A module has a global namespace.

**Property.** A method exposed as an attribute through `@property`. Used when a value is derived or when assignment must be checked.

**Recursive descent.** A parser whose structure mirrors the grammar: one method per rule, each calling the method for a tighter-binding rule. Used by the calculator.

**Shallow copy.** A new container whose elements are the same objects as the original. Sufficient when the elements are immutable. `list.copy` is shallow.

**Strong typing.** An operation refuses operands of the wrong type instead of silently converting them. `"3" + 4` is a `TypeError`.

**Truthiness.** The value of an object in a Boolean context. False values in this repository's examples: `None`, `False`, numeric zero, and empty containers.

**Walrus operator.** `:=`, an assignment expression. The control-flow cell uses it to strip a string and test the result in one condition.
