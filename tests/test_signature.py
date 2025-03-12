import allure
import pytest
from services.signature.api_signature import SignatureAPI


@allure.epic("Signature-system")
@allure.feature("Signature")
class TestSignature:
    signature_id = None


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
        assert signature_id, "The received ID cannot be empty"
        self.__class__.signature_id = model.data.items[2].id
        print(f"Extracted id 3 elements: {self.__class__.signature_id}")


    @allure.title("Get signature by ID")
    def test_signature_by_id(self):
        model = self.api_signature.get_signature_by_id(self.__class__.signature_id)
        assert model.data.id == self.__class__.signature_id, "The ID in the response does not match the expected one"


    @allure.title("Change signature by SignatureSystemID")
    def test_change_signature(self):
        model = self.api_signature.change_signature_by_id(self.__class__.signature_id)
        assert model.message == "Успішно оновлено."




