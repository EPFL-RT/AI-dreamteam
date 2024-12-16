from abc import ABC, abstractmethod

from domain.excel_answers import ExcelDocument, ExcelCheck

class ExcelOptimizer(ABC):
    
    @abstractmethod
    def optimize(self, excel_document: ExcelDocument) -> list[ExcelCheck]:
        pass