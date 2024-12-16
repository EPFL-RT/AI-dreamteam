

from abc import ABC, abstractmethod
from domain.quizz import Question, QuestionType, UserAnswer
from service.retriever.base import Retriever


class AnsweringService(ABC):

    retriver: Retriever
    
    @abstractmethod
    def answer(self, question: Question) -> UserAnswer:
        pass


    def get_question_type(self, question: Question) -> QuestionType:
        pass
        

