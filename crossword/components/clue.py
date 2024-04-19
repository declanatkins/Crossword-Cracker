from __future__ import annotations


class Clue:

    def __init__(
        self,
        number: int,
        direction: str,
        text: str,
        answer: str | None = None,
        show_answer: bool = False,
    ):
        self.number = number
        self.direction = direction
        self.text = text
        self.answer = answer
        self.show_answer = show_answer

    def __str__(self):
        if self.show_answer:
            return f"{self.number} {self.direction}: {self.text} ({self.answer})"
        return f"{self.number} {self.direction}: {self.text}"

    def __repr__(self):
        return self.__str__()
