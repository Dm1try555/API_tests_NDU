import allure
from services.collections.api_collections import CollectionsAPI


@allure.epic("Collections")
@allure.feature("Collections")
class TestCollections:

    @classmethod
    def setup_class(cls):
        cls.api_collections = CollectionsAPI()  # Создаем объект API

    @allure.title("Get collections")
    def test_get_collections(self):
        self.api_collections.get_collections()

