

from abc import ABC, abstractmethod
from domain.document import Passage
from domain.quizz import Question
from service.embedding.base import EmbeddingService


class Retriever(ABC):

    embedding_service: EmbeddingService

    @abstractmethod
    def retrieve(self, question: Question) -> list[Passage]:
        pass