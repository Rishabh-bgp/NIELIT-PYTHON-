# Capstone 4 — Quiz master

Notebook: [Project_04_Quiz_Master.ipynb](../../notebooks/capstones/Project_04_Quiz_Master.ipynb)

## Why this program exists

A quiz is data plus a scoring policy. If the score is stored on the attempt, every edit of a response has to remember to update it. This notebook does not store the score. `score` and `report` recompute from the paper and the responses. A frozen question means a running attempt cannot rewrite the paper.

## Records

`Question` holds a prompt, the expected answer, and a tuple of choices. It is frozen. `PAPER` is a tuple of five questions about `def`, `set`, `None`, `break`, and `append`. The engine does not mention Python. Replacing `PAPER` is the only change required to mark a different test.

The choices are not yet enforced. They are there so a later interface can render the paper without changing `Question`. A strict mode would reject a response that is not among the choices before comparing. That check still belongs in `marked`, so correctness has one definition.

## Marking

`Attempt` refuses a response list whose length differs from the paper. `marked` compares with `casefold` after `strip`, so surrounding spaces do not fail an otherwise right answer and `None` matches `none`. `zip(..., strict=True)` is a second guard on length. `score` returns earned and total. `report` prints the ratio and, for each miss, the expected answer.

## Published report

The sample answers `list` to the set question and is otherwise right.

```text
Score: 4/5 (80%)

1. Which keyword starts a function?
   you: def  (correct)
2. Which collection rejects duplicates?
   you: list  (wrong, answer is set)
3. Which value means no value?
   you: None  (correct)
4. Which statement leaves a loop?
   you: break  (correct)
5. Which method adds to the end of a list?
   you: append  (correct)
```

`4/5` is `0.8`, which the format spec prints as `80%`. An empty paper cannot reach `report`: the constructor rejects a length mismatch, and a zero-length paper with a zero-length response list would divide by zero in the percentage. Do not construct that attempt. A course paper has questions.

## Extension

Render `choices` under each prompt, and reject a response outside that tuple. Keep the comparison in `marked`. Add a pass mark as a method on `Attempt`, not as a field that can disagree with `score`.
