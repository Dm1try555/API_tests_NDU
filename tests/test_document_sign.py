import allure
import pytest
from services.document_sign.api_sign import DocumentSignAPI
from services.document.api_document import DocumentAPI

@allure.epic("Document Sign")
@allure.feature("Document Sign")
class TestDocumentSign:

    @classmethod
    def setup_class(cls):

        cls.api_sign = DocumentSignAPI()
        cls.api_document = DocumentAPI()


    @allure.title("Get file to sign document")
    def test_get_sign_document(self):
        created_document = self.api_document.create_new_document()
        document_id = created_document.data.id
        assert document_id is not None, "Документ не створено, ID відсутній"

        model = self.api_sign.get_document_sign(document_id)
        assert model.message == "Хеші успішно згенеровані."
        assert model.data is not None







