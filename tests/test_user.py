import allure
from services.user.api_user import UserAPI


@allure.epic("User")
@allure.feature("User")
class TestUser:
    user_id = None

    @classmethod
    def setup_class(cls):
        cls.api_user = UserAPI()

    @allure.title("Create new User")
    def test_create_user(self):
        model = self.api_user.create_user()
        self.__class__.user_id = model.data.id
        print(f"Create user ID: {self.__class__.user_id}")
        assert model.message == "Користувача зареєстровано."


    @allure.title("Check User by ID")
    def test_get_user_by_id(self):
        assert self.__class__.user_id is not None
        model = self.api_user.get_user_by_id(self.__class__.user_id)
        assert model.data.id == self.__class__.user_id
        assert model.message == "Користувача успішно отримано."


    @allure.title("Create toggle status")
    def test_create_status(self):
        self.api_user.create_status_inactive(self.__class__.user_id)
        self.api_user.get_status_inactive(self.__class__.user_id)

        self.api_user.create_status_need_change_password(self.__class__.user_id)
        self.api_user.get_status_need_change_password(self.__class__.user_id)

        self.api_user.create_status_blocked(self.__class__.user_id)
        self.api_user.get_status_blocked(self.__class__.user_id)

        self.api_user.create_status_active(self.__class__.user_id)
        self.api_user.get_status_active(self.__class__.user_id)

    @allure.title("Check User Audit by ID")
    def test_get_user_audit_by_id(self):
        assert self.__class__.user_id is not None
        model = self.api_user.get_user_audit_by_id(self.__class__.user_id)
        assert model.message == "Аудит користувача успішно отримано."


    @allure.title("Change User Role by ID")
    def test_change_role_by_id(self):
        assert self.__class__.user_id is not None
        model = self.api_user.change_role_by_id(self.__class__.user_id)


    @allure.title("Check User Role change by ID")
    def test_get_role_change_by_id(self):
        assert self.__class__.user_id is not None
        model = self.api_user.get_user_by_id(self.__class__.user_id)
        assert model.data.roles, f"No roles found in response: {model.data}"
        assert model.data.roles[0].id == 3 and model.data.roles[0].name == "test"


    @allure.title("Change User Password by ID")
    def test_change_password(self):
        assert self.__class__.user_id is not None
        model = self.api_user.change_password_by_id(self.__class__.user_id)
        assert model.message == "Пароль успішно змінено."




    # @allure.title("Check User Role change by ID")
    # def test_get_role_change_by_id(self):
    #     assert self.__class__.user_id is not None
    #     model = self.api_user.get_user_by_id(self.__class__.user_id)
    #     assert model.data.roles, f"No roles found in response: {model.data}"
    #     assert model.data.roles[0].id == 3 and model.data.roles[0].name == "test"








    # @allure.title("Get all Role permissions")
    # def test_get_role_permissions(self):
    #     model = self.api_role.get_role_permissions()
    #     assert model.message == "Дані успішно отримано"
    #     assert model.data is not None
    #
    # @allure.title("Get admin Role permissions")
    # def test_get_admin_role_permissions(self):
    #     model = self.api_role.get_admin_role_permissions()
    #     assert model.message == "Дані успішно отримано"
    #     assert model.data is not None
    #
    # @allure.title("Get client Role permissions")
    # def test_get_client_role_permissions(self):
    #     model = self.api_role.get_client_role_permissions()
    #     assert model.message == "Дані успішно отримано"
    #     assert model.data is not None
    #
    # @allure.title("Get list of roles")
    # def test_get_role_by_filters(self):
    #     model = self.api_role.get_role_by_filters()
    #     assert model.data is not None




