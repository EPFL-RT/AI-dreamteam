from abc import ABC, abstractmethod

import numpy as np

from domain.quizz import Quizz


class QuizzParser(ABC):
    @abstractmethod
    def parse(self, quizz_image: np.ndarray) -> Quizz: # return an image list
        pass



