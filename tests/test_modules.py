"""Standard-library tests for the five teaching modules."""

from __future__ import annotations

import unittest
from datetime import date
from decimal import Decimal

from nielit_python.calculator import Calculator, CalculatorError
from nielit_python.hangman import Hangman
from nielit_python.ledger import Expense, sample_ledger
from nielit_python.quiz import PAPER, Attempt
from nielit_python.tictactoe import Game


class CalculatorTests(unittest.TestCase):
    def test_precedence_and_power(self) -> None:
        calculator = Calculator()
        self.assertEqual(calculator.evaluate("2 + 3 * 4"), 14)
        self.assertEqual(calculator.evaluate("(2 + 3) * 4"), 20)
        self.assertEqual(calculator.evaluate("2 ** 3 ** 2"), 512)

    def test_division_by_zero_is_not_recorded(self) -> None:
        calculator = Calculator()
        calculator.evaluate("1 + 1")
        with self.assertRaises(CalculatorError):
            calculator.evaluate("10 / 0")
        self.assertEqual(len(calculator.history), 1)

    def test_memory(self) -> None:
        calculator = Calculator()
        calculator.evaluate("10 % 4")
        self.assertEqual(calculator.store(), 2)
        self.assertEqual(calculator.evaluate("M * 2 + 1"), 5)


class TicTacToeTests(unittest.TestCase):
    def test_published_sample_ends_with_computer_win(self) -> None:
        game = Game()
        self.assertEqual(game.play(0), "in progress")
        self.assertEqual(game.play(2), "in progress")
        self.assertEqual(game.play(6), "O wins")

    def test_illegal_move(self) -> None:
        game = Game()
        game.play(0)
        with self.assertRaises(ValueError):
            game.play(0)


class HangmanTests(unittest.TestCase):
    def test_repeat_does_not_cost_a_life(self) -> None:
        game = Hangman("python")
        game.guess("p")
        self.assertEqual(game.guess("p"), "already guessed")
        self.assertEqual(game.lives, 6)

    def test_published_sequence_wins(self) -> None:
        game = Hangman("python")
        for letter in ["a", "p", "y", "t", "z", "h", "o", "n"]:
            game.guess(letter)
        self.assertTrue(game.won)
        self.assertEqual(game.lives, 4)


class QuizTests(unittest.TestCase):
    def test_sample_score(self) -> None:
        attempt = Attempt(PAPER, ["def", "list", "None", "break", "append"])
        self.assertEqual(attempt.score, (4, 5))

    def test_length_mismatch(self) -> None:
        with self.assertRaises(ValueError):
            Attempt(PAPER, ["def"])


class LedgerTests(unittest.TestCase):
    def test_september_is_excluded_and_money_is_exact(self) -> None:
        totals = sample_ledger().totals(2026, 10)
        self.assertEqual(totals["food"], Decimal("2250.50"))
        self.assertNotIn(date(2026, 9, 28), [entry.spent_on for entry in sample_ledger().in_month(2026, 10)])

    def test_rejects_non_positive_amount(self) -> None:
        with self.assertRaises(ValueError):
            Expense(date(2026, 10, 1), "food", "refund", Decimal("0"))


if __name__ == "__main__":
    unittest.main()
