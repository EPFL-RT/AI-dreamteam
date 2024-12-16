from dataclasses import dataclass
from enum import StrEnum
import numpy as np
from typing import Literal

class CompetitionName(StrEnum):
    FSG = 'FSG'
    FSCH = 'FSCH'
    FSEast = 'FSEast'
    FSCzech = 'FSCzech'


class QuestionType(StrEnum):
    elec = 'elec'
    meca = 'meca'
    rules = 'rules'
    internet = 'internet'
    unknown = 'unknown'


class AnswerType(StrEnum):
    MCQA = 'MCQA'
    SCQA = 'SCQA'
    input = 'input'
    unknown = 'unknown'


@dataclass
class Image:
    url: str
    image: np.ndarray

    def image_to_text(self) -> str:
        raise NotImplementedError


@dataclass
class Answer:
    """Real answer of the question, stored in our database"""
    answer: str 
    is_correct: bool
    input_range: tuple[float, float] | None = None


@dataclass
class Question:
    """A single quizz class"""
    question: Image | str
    question_type: QuestionType
    answer_type: AnswerType
    competition: CompetitionName
    answers: list[Answer] | None = None  # To check performance but not used in practice



@dataclass
class UserAnswer:
    """Output of the Chat Bot / Answering system"""
    question: Question
    user_answer: str
    certainty: float
    explanation: str | None = None



@dataclass
class Quizz:
    """Quizz class: create this object from the initial screen-shot of the quizz"""
    competition_name: CompetitionName
    questions: list[Question]


