from abc import ABC, abstractmethod

from domain.excel_answers import ExcelCheck, ExcelDocument
from domain.quizz import QuestionType, UserAnswer

class ExcelCRUD(ABC):

    @abstractmethod
    def read_document(self) -> ExcelDocument:
        pass

    @abstractmethod
    def read_question_types(self) -> list[QuestionType]:
        pass

    @abstractmethod
    def write_chat_answers(self, excel_document: list[UserAnswer]) -> bool:
        pass

    @abstractmethod
    def write_optimized_answers(self, optimized_answer: list[ExcelCheck]) -> bool:
        pass

