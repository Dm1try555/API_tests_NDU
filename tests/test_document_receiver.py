import allure
import pytest
from services.document_receiver.api_receiver import DocumentReceiverAPI


@allure.epic("Document Receiver")
@allure.feature("Document Receiver")
class TestDocumentReceiver:

    @classmethod
    def setup_class(cls):

        cls.api_receiver = DocumentReceiverAPI()


    @allure.title("Rejection Letter")
    def test_rejection_letter(self, key="super-secret-key-123"):
        model = self.api_receiver.create_rejection_letter(key)
        assert model.message == "Лист-відмова успішно прийнятий"
        assert model.data == "Success"

    @allure.title("Confirmation Letter")
    def test_confirmation_letter(self, key="super-secret-key-123"):
        model = self.api_receiver.create_confirmation_letter(key)
        assert model.message == "Лист-підтвердження успішно прийнятий"
        assert model.data == "Success"

    @allure.title("Status Letter")
    def test_status_letter(self, key='super-secret-key-123'):
        model = self.api_receiver.create_status_letter(key)
        assert model.message == "Статус документу оновлено успішно"
        assert model.data == "Updated"
        






