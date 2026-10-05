"""A monthly expense ledger using Decimal.

Amounts are constructed from strings. A September row can be stored and then
excluded from an October report. See docs/capstones/05-expense-tracker.md.
"""

from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
from datetime import date
from decimal import Decimal


@dataclass(frozen=True)
class Expense:
    """One immutable ledger row. Amount must be positive."""

    spent_on: date
    category: str
    description: str
    amount: Decimal

    def __post_init__(self) -> None:
        if self.amount <= 0:
            raise ValueError("amount must be positive")
        if not self.category.strip():
            raise ValueError("category is required")


class Ledger:
    """An in-memory list of expenses with month and budget queries."""

    def __init__(self) -> None:
        self._entries: list[Expense] = []

    def add(self, entry: Expense) -> None:
        """Append one validated expense."""
        self._entries.append(entry)

    def in_month(self, year: int, month: int) -> list[Expense]:
        """Return entries whose date falls in year and month."""
        return [
            entry
            for entry in self._entries
            if entry.spent_on.year == year and entry.spent_on.month == month
        ]

    def totals(self, year: int, month: int) -> dict[str, Decimal]:
        """Return category totals for one month, sorted by category name."""
        grouped: dict[str, Decimal] = defaultdict(lambda: Decimal("0"))
        for entry in self.in_month(year, month):
            grouped[entry.category] += entry.amount
        return dict(sorted(grouped.items()))

    def alerts(self, year: int, month: int, budgets: dict[str, Decimal]) -> list[str]:
        """Return one message per category that spent more than its budget."""
        messages = []
        spent = self.totals(year, month)
        for category, limit in sorted(budgets.items()):
            used = spent.get(category, Decimal("0"))
            if used > limit:
                messages.append(f"{category}: spent {used} against a budget of {limit}")
        return messages


def sample_ledger() -> Ledger:
    """Build the October sample, including a September row that reports exclude."""
    ledger = Ledger()
    rows = [
        (date(2026, 10, 2), "food", "lunch", "240"),
        (date(2026, 10, 3), "transport", "bus pass", "800"),
        (date(2026, 10, 6), "food", "groceries", "1450.50"),
        (date(2026, 10, 9), "books", "python reference", "699"),
        (date(2026, 10, 18), "food", "dinner", "560"),
        (date(2026, 9, 28), "food", "previous month", "100"),
    ]
    for spent_on, category, description, amount in rows:
        ledger.add(Expense(spent_on, category, description, Decimal(amount)))
    return ledger


def demo() -> None:
    """Print October totals and the budget alerts from the published sample."""
    ledger = sample_ledger()
    print("October totals")
    for category, total in ledger.totals(2026, 10).items():
        print(f"  {category:<12} {total}")
    print("month total:", sum(ledger.totals(2026, 10).values(), Decimal("0")))
    budgets = {"food": Decimal("2000"), "transport": Decimal("700"), "books": Decimal("1000")}
    print("alerts:")
    for alert in ledger.alerts(2026, 10, budgets):
        print(" ", alert)


if __name__ == "__main__":
    demo()
