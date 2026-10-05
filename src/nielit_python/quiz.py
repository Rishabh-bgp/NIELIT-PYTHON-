"""A marked quiz. The score is computed, never stored.

Questions are frozen. An attempt must have one response per question.
See docs/capstones/04-quiz-master.md.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Question:
    """One prompt, its expected answer, and the choices a paper may render."""

    prompt: str
    answer: str
    choices: tuple[str, ...]


PAPER = (
    Question("Which keyword starts a function?", "def", ("func", "def", "lambda", "fn")),
    Question("Which collection rejects duplicates?", "set", ("list", "tuple", "set", "dict")),
    Question("Which value means no value?", "None", ("0", "False", "None", "empty")),
    Question("Which statement leaves a loop?", "break", ("skip", "break", "pass", "stop")),
    Question("Which method adds to the end of a list?", "append", ("add", "push", "append", "insert")),
)


@dataclass
class Attempt:
    """Responses to one paper. Length must match the paper."""

    paper: tuple[Question, ...]
    responses: list[str]

    def __post_init__(self) -> None:
        if len(self.responses) != len(self.paper):
            raise ValueError("one response is required per question")

    def marked(self) -> list[tuple[Question, str, bool]]:
        """Pair each question with the response and whether it matches."""
        rows = []
        for question, response in zip(self.paper, self.responses, strict=True):
            correct = response.strip().casefold() == question.answer.casefold()
            rows.append((question, response, correct))
        return rows

    @property
    def score(self) -> tuple[int, int]:
        """Return earned marks and the number of questions."""
        earned = sum(1 for _, _, correct in self.marked() if correct)
        return earned, len(self.paper)

    def report(self) -> str:
        """Return a marked report. A miss includes the expected answer."""
        if not self.paper:
            return "Score: 0/0"
        earned, total = self.score
        lines = [f"Score: {earned}/{total} ({earned / total:.0%})", ""]
        for number, (question, response, correct) in enumerate(self.marked(), start=1):
            mark = "correct" if correct else f"wrong, answer is {question.answer}"
            lines.append(f"{number}. {question.prompt}")
            lines.append(f"   you: {response}  ({mark})")
        return "\n".join(lines)


def demo() -> None:
    """Mark the published sample, which misses the set question."""
    attempt = Attempt(PAPER, ["def", "list", "None", "break", "append"])
    print(attempt.report())


if __name__ == "__main__":
    demo()
