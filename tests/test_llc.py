import allure
import pytest
from services.llc.api_llc import LlcAPI


@allure.epic("LLC")
@allure.feature("LLC")
class TestLLC:

    @classmethod
    def setup_class(cls):

        cls.api_llc = LlcAPI()

    # @pytest.fixture(scope="class", autouse=True)
    # @allure.title("Create new user from admin portal")
    # def user_id(self):
    #     user = self.api_adminuser.create_user_from_admin()
    #     print(f"Создан пользователь с ID: {user.id}")
    #     return user.id



    @allure.title("Get llc by filter")
    def test_llc_by_filter(self):
        llc = self.api_llc.get_llc_by_filter()



