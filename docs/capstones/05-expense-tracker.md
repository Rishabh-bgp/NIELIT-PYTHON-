# Capstone 5 — Expense tracker

Notebook: [Project_05_Expense_Tracker.ipynb](../../notebooks/capstones/Project_05_Expense_Tracker.ipynb)

## Why this program exists

The last capstone is a ledger. The new constraint is the number type. Binary `float` cannot represent most decimal fractions. Money in this notebook is `decimal.Decimal`, constructed from strings so the value is the one that was written down.

The second constraint is the query. A September row may be stored and must not appear in an October report. The budget warning must use the same totals as the printed table, or the warning can disagree with the report.

## Entry

`Expense` is frozen. Fields are the date, the category, the description, and the amount. `__post_init__` rejects a non-positive amount and a blank category. A bad row cannot enter the list and fail only when a report is printed. Frozen means a stored expense is not edited in place; a correction is a new entry. That is a reasonable rule for a ledger and a simplifying one for this notebook.

## Queries

`Ledger.add` appends. `in_month` keeps rows whose year and month match. `totals` sums with `defaultdict` and returns a dict sorted by category name, so the printed order does not depend on insertion order. `alerts` calls `totals` and compares each budget. A category with no spending contributes zero and is alerted only if the budget is negative, which the sample budgets are not. An overspend produces one sentence per category.

## Published October

| Date | Category | Description | Amount |
| --- | --- | --- | --- |
| 2026-10-02 | food | lunch | 240 |
| 2026-10-03 | transport | bus pass | 800 |
| 2026-10-06 | food | groceries | 1450.50 |
| 2026-10-09 | books | python reference | 699 |
| 2026-10-18 | food | dinner | 560 |
| 2026-09-28 | food | previous month | 100 |

The September row is stored and excluded. October totals are books 699, food 2250.50, transport 800. The month total is 3749.50. Against budgets of 2000, 700, and 1000, food and transport are reported. Books is under budget and is absent from the alerts.

`1450.50` remains exact because it was parsed from a string. `Decimal(1450.50)` would have been the wrong constructor: the float literal is already rounded.

## Extension

Persistence is a JSON lines file. Write `date.isoformat()` and `str(amount)`. Read them back with `date.fromisoformat` and `Decimal`. Keep that conversion at the edge of `Ledger`. The file loop in the language-reference capstone is the pattern. Exercise 17 is that extension.
