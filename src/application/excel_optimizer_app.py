

from service.excel_CRUD.base import ExcelCRUD
from service.excel_optimizer.base import ExcelOptimizer


class ExcelOptimizerApp:

    excel_optimizer: ExcelOptimizer
    excel_crud: ExcelCRUD

    def __init__(self, excel_optimizer: ExcelOptimizer, excel_crud: ExcelCRUD):
        self.excel_optimizer = excel_optimizer
        self.excel_crud = excel_crud

    def run(self) -> bool:
        excel_document = self.excel_crud.read_document()
        optimized_answers = self.excel_optimizer.optimize(excel_document)
        return self.excel_crud.write_optimized_answers(optimized_answers)