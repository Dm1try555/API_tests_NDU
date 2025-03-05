import allure
import pytest
from config.base_test import BaseTest
from services.document.api_document import DocumentAPI


@allure.epic("Document")
@allure.feature("Document")
class TestDocument:

    @classmethod
    def setup_class(cls):

        cls.api_document = DocumentAPI()

    # @pytest.fixture(scope="class", autouse=True)
    # @allure.title("Create new user from admin portal")
    # def user_id(self):
    #     user = self.api_adminuser.create_user_from_admin()
    #     print(f"Создан пользователь с ID: {user.id}")
    #     return user.id

    # @allure.title("Test user creation")
    # def test_create_user_from_admin(self, user_id):
    #     assert user_id is not None, "Ошибка: ID пользователя не создан!"
    #     get_user_by_id = self.api_adminuser.get_user_by_id(user_id)
    #     assert get_user_by_id.id == user_id, "Ошибка: ID пользователя не совпадает!"


    @allure.title("Create new document")
    def test_create_new_document(self):
        self.api_document.create_new_document()


