import allure
import pytest
from services.document.api_document import DocumentAPI


@allure.epic("Document")
@allure.feature("Document")
class TestDocument:
    document_id = None

    @classmethod
    def setup_class(cls):
        cls.api_document = DocumentAPI()

    @allure.title("Create new document")
    def test_create_new_document(self):
        model = self.api_document.create_new_document()
        assert model.data.id is not None, "Ошибка: ID документа не создан!"

        self.__class__.document_id = model.data.id
        print(f"Созданный документ ID: {self.__class__.document_id}")

    @allure.title("Check document by ID")
    def test_check_document_by_id(self):
        assert self.__class__.document_id is not None, "Документ не был создан"

        model = self.api_document.get_document_by_id(self.__class__.document_id)
        assert model.data.id == self.__class__.document_id, "Ошибка: ID документа не совпадает!"


