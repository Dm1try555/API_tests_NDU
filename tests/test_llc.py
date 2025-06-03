import allure
from services.llc.api_llc import LlcAPI



@allure.epic("LLC")
@allure.feature("LLC")
class TestLLC:
    

    @classmethod
    def setup_class(cls):
        cls.api_llc = LlcAPI()
        cls.id_llc = None
        cls.user_id = None


    @allure.title("Get llc by filter")
    def test_llc_by_filter(self):
        model = self.api_llc.get_llc_by_filter()
        assert model.message == "Успішно отримано дані."
        assert model.data is not None
        self.__class__.id_llc = model.data.items[0].id
        print(f"Extracted ID LLC: {self.__class__.id_llc}")

    @allure.title("Get llc search")
    def test_llc_search(self):
        model = self.api_llc.get_llc_search()
        assert model.message == "Успішно отримано дані."
        assert model.data is not None


    @allure.title("Get llc by ID")
    def test_llc_by_id(self):
        model = self.api_llc.get_llc_by_id(self.__class__.id_llc)
        assert model.message == "LLC retrieved successfully"
        assert model.data is not None
        assert model.data.id == self.__class__.id_llc


    @allure.title("Get my llc")
    def test_get_my_llc(self):
        model = self.api_llc.get_my_llc()
        assert model.message == "Товариства користувача отримано."
        for item in model.data:
            assert item.members is not None, "Список members пустий"
            assert item.id is not None, "ID пустий"



