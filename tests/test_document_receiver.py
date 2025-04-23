import allure
import pytest
from services.document_receiver.api_receiver import DocumentReceiverAPI


@allure.epic("Document Receiver")
@allure.feature("Document Receiver")
class TestAdminUser:

    @classmethod
    def setup_class(cls):

        cls.api_receiver = DocumentReceiverAPI()

   

    @allure.title("Rejection Letter")
    def test_rejection_letter(self, key="super-secret-key-123"):
        model = self.api_receiver.create_rejection_letter(key)
        assert model.message == "Лист-відмова успішно прийнятий"
        assert model.data == "Success"
        






