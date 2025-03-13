import allure
import pytest
from services.llc.api_llc import LlcAPI
from tests.test_user import TestUser



@pytest.fixture
def create_user():
    user_test = TestUser()
    user_test.setup_class()
    user_test.test_create_user()
    return user_test.user_id


@allure.epic("LLC")
@allure.feature("LLC")
class TestLLC:

    id_llc = None

    @classmethod
    def setup_class(cls):

        cls.api_llc = LlcAPI()



    @allure.title("Get llc by filter")
    def test_llc_by_filter(self):
        model = self.api_llc.get_llc_by_filter()
        assert model.message == "Успішно отримано дані."
        assert model.data is not None
        self.__class__.id_llc = model.data.items[1].id
        print(f"Extracted ID second LLC: {self.__class__.id_llc}")


    @allure.title("Get llc by ID")
    def test_llc_by_id(self):
        model = self.api_llc.get_llc_by_id(self.__class__.id_llc)
        assert model.message == "LLC retrieved successfully"
        assert model.data is not None
        assert model.data.id == self.__class__.id_llc


    @allure.title("Add manager to LLC")
    def test_add_manager_to_llc(self, create_user):
        model = self.api_llc.add_manager_to_llc(self.__class__.id_llc, create_user)
        assert model.message == "Manager added to llc  successfully"




