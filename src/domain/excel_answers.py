from typing import Literal

class ExcelAnswer:
    answer: list[Literal['A', 'B', 'C', 'D']]
    score: int


class ExcelCheck:
    answer: Literal['A', 'B', 'C', 'D']
    confidence: float


class ExcelDocument:
    history: list[ExcelAnswer]
    question_checks = list[list[ExcelCheck]]
    


