from typing import Literal
import numpy as np
from service.answering.base import AnsweringService
from service.excel_CRUD.base import ExcelCRUD
from service.quizz_parser.base import QuizzParser
from src.domain.quizz import Question, Quizz, UserAnswer


class QuizzAnswringApp:

    quizz_parser: QuizzParser
    excel_crud: ExcelCRUD
    answering_service: AnsweringService


    def __init__(self, quizz_parser: QuizzParser, excel_crud: ExcelCRUD, answering_service: AnsweringService):
        self.quizz_parser = quizz_parser
        self.excel_crud = excel_crud
        self.answering_service = answering_service


    def answer_quizz(self, competition: str, quizz_image: np.ndarray, question_type_finder: Literal['excel', 'chat']) -> list[UserAnswer]:

        quizz: Quizz = self.quizz_parser.parse(quizz_image)
        quizz.competition_name = competition

        question_types: list[str]
        if question_type_finder == 'excel':
            question_types = self.excel_crud.read_question_types()
        else:
            question_types = [self.answering_service.get_question_type(q) for q in quizz.questions]

        for i, q in enumerate(quizz.questions):
            q.question_type = question_types[i]
            q.competition = quizz.competition_name


        answers: list[UserAnswer] = [self.answering_service.answer(q) for q in quizz.questions]
        return answers
    

    def write_chat_answers(self, answers: list[UserAnswer]) -> bool:
        return self.excel_crud.write_chat_answers(answers)
    


    def run(self, quizz_image: np.ndarray, question_type_finder: Literal['excel', 'chat']) -> bool:
        answers = self.answer_quizz(quizz_image, question_type_finder)
        return self.write_chat_answers(answers)

        
            






        



