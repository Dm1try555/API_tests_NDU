import allure
from services.llc.api_llc import LlcAPI
from tests.test_user import create_user


@allure.epic("LLC")
@allure.feature("LLC")
class TestLLC:
    

    @classmethod
    def setup_class(cls):
        cls.api_llc = LlcAPI()
        cls.id_llc = None
        cls.user_id = None




    @allure.title("Create LLC")
    def test_create_llc(self):
        model = self.api_llc.create_llc()
        assert model.Message == "Value cannot be null. (Parameter 'entity')"
        assert model.Data is None
        check = self.api_llc.get_llc_by_filter()
        



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
        self.__class__.user_id = create_user
        model = self.api_llc.add_manager_to_llc(self.__class__.id_llc, self.__class__.user_id)
        assert model.message == "Manager added to llc  successfully"


    @allure.title("Check manager after add manager to LLC")
    def test_check_after_add_manager(self):
        model = self.api_llc.get_llc_by_id(self.__class__.id_llc)
        assert model.message == "LLC retrieved successfully"
        assert model.data is not None
        assert model.data.id == self.__class__.id_llc
        assert model.data.managers, "The managers list is empty, although a manager should have been added."
        for user_ids in model.data.managers:
            print(user_ids)
            assert user_ids is not None

    @allure.title("Get my llc")
    def test_get_my_llc(self):
        model = self.api_llc.get_my_llc()
        assert model.message == "Товариства користувача отримано."
        for item in model.data:
            assert item.members is not None, "Список members пустий"
            assert item.id is not None, "ID пустий"
        
    



    # @allure.title("Add members to LLC")
    # def test_add_members_to_llc(self):
    #     # Use the user_id saved from the previous test
    #     model = self.api_llc.add_manager_to_llc(self.__class__.id_llc, self.__class__.user_id)
    #     assert model.message == "Manager added to llc  successfully"


    # @allure.title("Check members after add members to LLC")
    # def test_check_after_add_members(self):
    #     model = self.api_llc.get_llc_by_id(self.__class__.id_llc)
    #     assert model.message == "LLC retrieved successfully"
    #     assert model.data is not None
    #     assert model.data.id == self.__class__.id_llc
    #     assert model.data.managers, "Список managers пуст, хотя менеджер должен был быть добавлен."
    #     for user_ids in model.data.managers:
    #         print(user_ids)
    #         assert user_ids is not None





