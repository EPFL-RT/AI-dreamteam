from abc import ABC, abstractmethod
import numpy as np
from domain.document import Document


class DocumentParser(ABC):
    
    def parse_text(self, text: str) -> Document:
        raise NotImplementedError


    def parse_pdf(self, pdf_path: str) -> Document:
        raise NotImplementedError


    def parse_http(self, url: str) -> Document:
        raise NotImplementedError
