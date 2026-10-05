# Capstone 5 — Expense tracker

Notebook: [Project_05_Expense_Tracker.ipynb](../../notebooks/capstones/Project_05_Expense_Tracker.ipynb)

## Purpose

A monthly ledger that does not use binary floats for money. Each entry is a date, a category, a description, and a `Decimal` amount. The ledger can list one month, total by category, and name the categories that crossed a budget.

## Money

`Decimal` is constructed from strings (`Decimal("1450.50")`), not from a float literal. A float literal is already rounded before `Decimal` sees it. Amounts must be positive. A blank category is rejected. Both checks live on the entry, so a bad row cannot enter the list and then fail only in a report.

## Queries

`in_month` filters on year and month. September's sample row is stored and then excluded from the October report. `totals` sums with `defaultdict` and returns a dict sorted by category name, so the printed order is stable. `alerts` reads `totals` rather than a second loop, so the warning cannot disagree with the table.

## Sample

October has three food rows (240, 1450.50, 560), one transport row (800), and one books row (699). The month total is 3749.50. Against budgets of 2000, 700, and 1000, food and transport are reported. Books is under budget and is not listed.

## Extension

Persistence is a JSON lines file written from `Expense`, with `date.isoformat` and `str(amount)`, read back with `date.fromisoformat` and `Decimal`. The reference notebook's closing example is the pattern for that file loop. Keep the conversion at the edge and keep `Ledger` in memory.
