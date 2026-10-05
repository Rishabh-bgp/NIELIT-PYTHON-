"""Safe arithmetic expressions, memory, and history.

The grammar is documented in docs/capstones/01-calculator.md. Evaluation never
calls eval. Precedence is the call structure of the parser.
"""

from __future__ import annotations

from dataclasses import dataclass


class CalculatorError(Exception):
    """Raised when an expression cannot be tokenised or evaluated."""


@dataclass(frozen=True)
class Token:
    """A single lexical unit. The lexer does not evaluate it."""

    kind: str
    value: str


class Lexer:
    """Turn an expression string into a token list ending in EOF."""

    def __init__(self, source: str) -> None:
        self.source = source
        self.index = 0

    def tokens(self) -> list[Token]:
        produced: list[Token] = []
        while self.index < len(self.source):
            char = self.source[self.index]
            if char.isspace():
                self.index += 1
                continue
            if char.isdigit() or char == ".":
                produced.append(self._number())
                continue
            if self.source.startswith("//", self.index):
                produced.append(Token("OP", "//"))
                self.index += 2
                continue
            if self.source.startswith("**", self.index):
                produced.append(Token("OP", "**"))
                self.index += 2
                continue
            if char in "+-*/%()":
                kind = "LPAREN" if char == "(" else "RPAREN" if char == ")" else "OP"
                produced.append(Token(kind, char))
                self.index += 1
                continue
            if char == "M":
                produced.append(Token("MEMORY", "M"))
                self.index += 1
                continue
            raise CalculatorError(f"unexpected character: {char!r}")
        produced.append(Token("EOF", ""))
        return produced

    def _number(self) -> Token:
        start = self.index
        seen_dot = False
        while self.index < len(self.source):
            char = self.source[self.index]
            if char.isdigit():
                self.index += 1
            elif char == "." and not seen_dot:
                seen_dot = True
                self.index += 1
            else:
                break
        literal = self.source[start : self.index]
        if literal == ".":
            raise CalculatorError("incomplete number")
        return Token("NUMBER", literal)


class Parser:
    """Recursive-descent parser. One method per grammar rule."""

    def __init__(self, tokens: list[Token], memory: float) -> None:
        self.tokens = tokens
        self.memory = memory
        self.index = 0

    def parse(self) -> float:
        value = self._expression()
        self._expect("EOF")
        return value

    def _expression(self) -> float:
        value = self._term()
        while self._peek().kind == "OP" and self._peek().value in {"+", "-"}:
            operator = self._advance().value
            right = self._term()
            value = value + right if operator == "+" else value - right
        return value

    def _term(self) -> float:
        value = self._power()
        while self._peek().value in {"*", "/", "//", "%"}:
            operator = self._advance().value
            right = self._power()
            if operator in {"/", "//", "%"} and right == 0:
                raise CalculatorError("division by zero")
            if operator == "*":
                value *= right
            elif operator == "/":
                value /= right
            elif operator == "//":
                value = value // right
            else:
                value %= right
        return value

    def _power(self) -> float:
        value = self._unary()
        if self._peek().value == "**":
            self._advance()
            return value ** self._power()
        return value

    def _unary(self) -> float:
        if self._peek().kind == "OP" and self._peek().value == "-":
            self._advance()
            return -self._unary()
        return self._primary()

    def _primary(self) -> float:
        token = self._advance()
        if token.kind == "NUMBER":
            return float(token.value)
        if token.kind == "MEMORY":
            return self.memory
        if token.kind == "LPAREN":
            value = self._expression()
            self._expect("RPAREN")
            return value
        raise CalculatorError(f"expected a value, found {token.value or token.kind!r}")

    def _peek(self) -> Token:
        return self.tokens[self.index]

    def _advance(self) -> Token:
        token = self._peek()
        self.index += 1
        return token

    def _expect(self, kind: str) -> Token:
        token = self._advance()
        if token.kind != kind:
            found = token.value or token.kind
            raise CalculatorError(f"expected {kind}, found {found!r}")
        return token


class Calculator:
    """Expression calculator with one memory register and a success history."""

    def __init__(self) -> None:
        self.memory = 0.0
        self.history: list[tuple[str, float]] = []

    def evaluate(self, expression: str) -> float:
        """Evaluate expression. Record it only if parsing and evaluation succeed."""
        value = Parser(Lexer(expression).tokens(), self.memory).parse()
        self.history.append((expression, value))
        return value

    def store(self) -> float:
        """Copy the last successful value into memory."""
        if not self.history:
            raise CalculatorError("nothing to store")
        self.memory = self.history[-1][1]
        return self.memory

    def clear(self) -> None:
        """Drop memory and history."""
        self.memory = 0.0
        self.history.clear()


def demo() -> None:
    """Print the sample used in the notebook and the capstone note."""
    calculator = Calculator()
    samples = ["2 + 3 * 4", "(2 + 3) * 4", "2 ** 3 ** 2", "-5 + 12", "7 // 2", "10 % 4"]
    for sample in samples:
        print(f"{sample:>12} = {calculator.evaluate(sample)}")
    print("stored memory:", calculator.store())
    print("memory reuse:", calculator.evaluate("M * 2 + 1"))
    try:
        calculator.evaluate("10 / 0")
    except CalculatorError as exc:
        print("handled:", exc)
    print("history length:", len(calculator.history))


if __name__ == "__main__":
    demo()
