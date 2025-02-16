import allure
import pytest
from services.signature.api_signature import SignatureAPI


@allure.epic("Signature-system")
@allure.feature("Signature")
class TestSignature:

    @classmethod
    def setup_class(cls):

        cls.api_signature = SignatureAPI()

    # @pytest.fixture(scope="class", autouse=True)
    # @allure.title("Create new user from admin portal")
    # def user_id(self):
    #     user = self.api_adminuser.create_user_from_admin()
    #     print(f"Создан пользователь с ID: {user.id}")
    #     return user.id



    @allure.title("Get signature by filter")
    def test_signature_by_filter(self):
        model, signature_id = self.api_signature.get_signature_by_filter()
        assert signature_id, "Отриманий ID не може бути порожнім"

    @allure.title("Get signature by ID")
    def test_signature_by_id(self):
        model, signature_id = self.api_signature.get_signature_by_filter()  # Получаем ID
        assert signature_id, "ID не может быть пустым или None"

        signature_by_id = self.api_signature.get_signature_by_id(signature_id)  # Передаем ID в запрос
        assert signature_by_id.data.id == signature_id, "ID в ответе не совпадает с ожидаемым"




