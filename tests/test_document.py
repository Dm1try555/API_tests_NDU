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

    @allure.title("Copy document by ID")
    def test_copy_document_by_id(self):
        assert self.__class__.document_id is not None, "Документ не был создан"
        model = self.api_document.copy_document_by_id(self.__class__.document_id)
        assert model.message == "Копія успішно створена"
        copied_document_id = model.data.id
        assert copied_document_id == self.__class__.document_id + 1
        print(f"Original document ID: {self.__class__.document_id}, Copy ID: {copied_document_id}")

    @allure.title("Delete document by ID")
    def test_delete_document_by_id(self):
        assert self.__class__.document_id is not None, "Документ не был создан"
        model = self.api_document.delete_document_by_id(self.__class__.document_id)
        assert model.message == "Документ видалено."

    @allure.title("Check document by ID after delete")
    def test_check_document_by_id_after_delete(self):
        assert self.__class__.document_id is not None, "Документ не был создан"
        model = self.api_document.get_document_by_id_after_delete(self.__class__.document_id)
        assert model.Message == "DocumentNotFound"


