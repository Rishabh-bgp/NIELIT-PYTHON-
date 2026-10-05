# Capstone 1 — Safe expression calculator

Notebook: [Project_01_Safe_Expression_Calculator.ipynb](../../notebooks/capstones/Project_01_Safe_Expression_Calculator.ipynb)

## Purpose

Evaluate arithmetic text without `eval`. `eval` will run any Python expression, which is the wrong tool for a calculator that may later sit behind a text box. The notebook builds a lexer and a recursive-descent parser instead. The grammar is small enough to read in one sitting and strict enough to reject a trailing operator and a division by zero.

## Grammar

```text
expression = term   { (+|-) term }
term       = power  { (*|/|//|%) power }
power      = unary  [ ** power ]
unary      = - unary | primary
primary    = number | ( expression ) | memory
```

Precedence is the call structure. `expression` calls `term`, and `term` calls `power`, so multiplication binds more tightly than addition. Power calls itself on the right, so `2 ** 3 ** 2` is `2 ** (3 ** 2)` and equals 512, matching Python.

## Types

- `CalculatorError` is the only failure type the parser raises. Callers catch that type and leave other exceptions alone.
- `Token` is a frozen pair of kind and text. The lexer does not evaluate.
- `Lexer` walks the source once. `//` and `**` are recognised before a single-character operator, because a left-to-right scan would otherwise split them.
- `Parser` holds the token list, an index, and the current memory value. It does not mutate the calculator.
- `Calculator` owns memory and history. `evaluate` appends a pair only after a successful parse. `store` copies the last value into memory. `clear` drops both.

`M` is a primary. It may appear anywhere a number may appear. It reads memory; it does not update memory. Update is an explicit `store` call, so evaluation has no hidden side effect.

## Sample result

The published run prints:

```text
   2 + 3 * 4 = 14.0
 (2 + 3) * 4 = 20.0
 2 ** 3 ** 2 = 512.0
     -5 + 12 = 7.0
      7 // 2 = 3.0
      10 % 4 = 2.0
stored memory: 2.0
memory reuse: 5.0
handled: division by zero
history length: 7
```

History length is 7 because the memory reuse expression is also recorded. The failed division is not recorded.

## Limits

Numbers are parsed as `float`. Floor division therefore follows float floor division. There is no variable table beyond the single memory register, and there are no functions. Those are the natural extensions: a name table in `Parser`, still without calling `eval`.
