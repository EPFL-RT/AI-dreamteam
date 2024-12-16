from dataclasses import dataclass
from typing import Literal
import numpy as np

@dataclass
class Passage:
    id: int

@dataclass
class TextPassage(Passage):
    text: str
    length: int

@dataclass
class ImagePassage(Passage):
    image: np.ndarray
    size: tuple[int, int]

@dataclass
class Document:
    id: int
    name: str
    type: Literal['pdf', 'docx', 'txt']
    passages: list[Passage]