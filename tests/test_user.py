import allure
import pytest
from services.user.api_user import UserAPI


@pytest.fixture(scope="class")
def create_user():
    with allure.step("Create a new user"):
        api_user = UserAPI()
        model = api_user.create_user()
        assert model.message == "Користувача зареєстровано."
        user_id = model.data.id
        print(f"Created user ID: {user_id}")
    return user_id


@allure.epic("User")
@allure.feature("User")
class TestUser:

    def __init__(self):
        self.user_id = None
        self.test_create_user = None

    @classmethod
    def setup_class(cls):
        cls.api_user = UserAPI()

    @allure.title("Check User by ID")
    def test_get_user_by_id(self, create_user):
        model = self.api_user.get_user_by_id(create_user)
        assert model.data.id == create_user
        assert model.message == "Користувача успішно отримано."

    @allure.title("Create toggle status")
    def test_create_status(self, create_user):

        model = self.api_user.create_status_inactive(create_user)
        assert model is not None
        assert model.message == "Статус успішно змінено."

        model = self.api_user.create_status_need_change_password(create_user)
        assert model is not None
        assert model.message == "Статус змінено на need_change_password"

        model = self.api_user.create_status_blocked(create_user)
        assert model is not None
        assert model.message == "Статус змінено на blocked"

        model = self.api_user.create_status_active(create_user)
        assert model is not None
        assert model.message == "Статус змінено на active"

    @allure.title("Check User Audit by ID")
    def test_get_user_audit_by_id(self, create_user):
        model = self.api_user.get_user_audit_by_id(create_user)
        assert model.message == "Аудит користувача успішно отримано."

    def test_change_role_by_id(self, create_user):
        model = self.api_user.change_role_by_id(create_user)
        assert model is not None
        assert model.message == "Роль користувача змінено."

    @allure.title("Check User Role change by ID")
    def test_get_role_change_by_id(self, create_user):
        model = self.api_user.get_user_by_id(create_user)
        assert model.data.roles, f"No roles found in response: {model.data}"
        assert model.data.roles[0].id == 3 and model.data.roles[0].name == "test"

    @allure.title("Change User Password by ID")
    def test_change_password(self, create_user):
        model = self.api_user.change_password_by_id(create_user)
        assert model.message == "Пароль успішно змінено."

    @allure.title("Change User Info by ID")
    def test_change_user_info(self, create_user):
        model = self.api_user.change_user_info_by_id(create_user)
        assert model.message == "Користувача успішно оновлено."

    @allure.title("Get Users list by filters")
    def test_get_users_list(self):
        model = self.api_user.get_users_by_default_filters()
        assert model.message == "Дані успішно отримано."
