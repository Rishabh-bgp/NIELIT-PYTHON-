# Capstone 4 — Quiz master

Notebook: [Project_04_Quiz_Master.ipynb](../../notebooks/capstones/Project_04_Quiz_Master.ipynb)

## Purpose

Separate the paper from the attempt. Questions are frozen records. An attempt is a list of responses of the same length. The score is computed from those two, not stored, so a later edit of a response cannot leave an old score behind.

## Records

`Question` holds a prompt, the expected answer, and a tuple of choices. It is frozen, so a running attempt cannot rewrite the paper. `PAPER` is a module-level tuple of five Python questions. Replacing that tuple is the only change required to mark a different test; the engine does not mention Python.

## Marking

`Attempt` refuses a response list whose length differs from the paper. `marked` compares with `casefold` after `strip`, so `None` and `none` match and surrounding spaces do not fail an otherwise right answer. `zip(..., strict=True)` is a second guard on length.

`score` returns a pair, earned and total. `report` prints the ratio and, for each miss, the expected answer. The published sample answers `list` to the set question and is marked 4/5.

## What the choices are for

The engine does not yet reject an answer that is not among `choices`. The field is there so a later interface can render the paper without changing `Question`. A strict mode would test membership before comparing, and would still use `marked` as the single place that decides correctness.
