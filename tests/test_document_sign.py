import allure
import pytest
from services.document_sign.api_sign import DocumentSignAPI


@allure.epic("Document Sign")
@allure.feature("Document Sign")
class TestDocumentSign:

    @classmethod
    def setup_class(cls):

        cls.api_sign = DocumentSignAPI()

   

    @allure.title("Get file to sign document")
    def test_get_sign_document(self, id="1"):  #id document 1
        model = self.api_sign.get_document_sign(id)
        assert model.message == "Хеші успішно згенеровані."
       

    
        






