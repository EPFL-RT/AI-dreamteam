from abc import ABC, abstractmethod
import numpy as np

from domain.document import Passage, ImagePassage



class EmbeddingService(ABC):

    def encode(self, passage: Passage) -> np.array:
        pass


    def encode_image(self, image_passage: ImagePassage) -> np.array:
        pass