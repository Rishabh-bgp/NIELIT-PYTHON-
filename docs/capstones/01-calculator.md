# Capstone 1 — Safe expression calculator

Notebook: [Project_01_Safe_Expression_Calculator.ipynb](../../notebooks/capstones/Project_01_Safe_Expression_Calculator.ipynb)

Python module: `src/nielit_python/calculator.py`. Run it with `PYTHONPATH=src python3 -m nielit_python.calculator`. The public class is `Calculator`.

## Why this program exists

A calculator is the usual first project, and it is usually implemented with `eval`. That works as a demo and becomes a defect as soon as the expression comes from a person. `eval` executes Python, not arithmetic. This notebook builds the smaller machine that a calculator actually needs: a lexer, a parser, a memory register, and a history of successful evaluations.

The teaching point is that precedence is structure. It is not a table consulted at runtime. A lower-precedence rule calls a higher-precedence rule. That is why `2 + 3 * 4` is 14.

## Grammar

```text
expression = term   { (+|-) term }
term       = power  { (*|/|//|%) power }
power      = unary  [ ** power ]          # right associative
unary      = - unary | primary
primary    = number | ( expression ) | memory
```

Power calls itself on the right-hand side, so `2 ** 3 ** 2` is `2 ** (3 ** 2)` and equals 512, matching Python. Parentheses are a primary: they reset the parser to `expression`, which is why `(2 + 3) * 4` is 20.

## Walk through `2 + 3 * 4`

1. `Lexer` yields number `2`, operator `+`, number `3`, operator `*`, number `4`, end.
2. `expression` calls `term`. `term` calls `power`, which reads `2`.
3. The next operator is `+`, which is not a term operator, so `term` returns `2`.
4. `expression` sees `+`, calls `term` again, and that `term` reads `3`, sees `*`, and reads `4`.
5. `3 * 4` is computed inside `term` and returned as `12`.
6. `expression` adds `2 + 12` and returns `14`.

The multiplication never reaches `expression`. That is the whole of precedence for this grammar.

## Types and responsibilities

`CalculatorError` is the only failure type the parser raises. A caller that wants a message catches that type and lets unexpected defects propagate.

`Token` is a frozen pair of kind and text. The lexer does not evaluate. Kinds in use are `NUMBER`, `OP`, `LPAREN`, `RPAREN`, `MEMORY`, and `EOF`.

`Lexer` scans once. Two-character operators are recognised before a single character, because a left-to-right scan would otherwise split `//` into two divisions. A lone `.` is an incomplete number. Any other character is an error at the point it is seen.

`Parser` holds the token list, an index, and the current memory value. It does not update the calculator. Division, floor division, and remainder check for a zero right operand before the operation. The check is in `term`, which is the only rule that performs those operators.

`Calculator` owns memory and history. `evaluate` appends a pair only after a successful parse, so a failed expression does not appear in history. `store` copies the last successful value into memory and raises if history is empty. `clear` drops both. `M` reads memory. It does not write it. Writing is the explicit `store` call, so evaluation has no hidden side effect.

## Published result

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

Memory is `2.0` because `store` runs after `10 % 4`. `M * 2 + 1` is the seventh successful evaluation, which is why the history length is 7. The division by zero is handled and not recorded.

Numbers are parsed as `float`. Floor division therefore follows float floor division. There is no name table beyond the single register, and there are no functions. A name table in `Parser` is the natural extension, still without `eval`.

## Related reference sections

Operators and truthiness, exceptions, and the closing `ReadingLog` example. The calculator is the first place those ideas have to survive a bad input rather than a chosen one.
