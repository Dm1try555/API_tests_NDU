import allure
import pytest
from services.user.api_user import UserAPI
import uuid
from faker import Faker

fake = Faker()



class Payloads:
    @staticmethod
    def create_user():
        unique_login = f"{fake.user_name()}_{uuid.uuid4().hex[:8]}"
        return {
            "password": fake.password(special_chars=True, digits=True, upper_case=True, lower_case=True),  # length=14
            "login": unique_login,
            "firstName": fake.first_name(),
            "middleName": fake.first_name(),
            "lastName": fake.last_name(),
            "identityNumber": "1234567890"
        }



@pytest.fixture(scope="function")
def create_user():
    with allure.step("Create a new user"):
        api_user = UserAPI()

        api_user.payloads.create_user = Payloads.create_user()

        model = api_user.create_user()
        assert model.message == "Користувача зареєстровано."
        user_id = model.data.id
        print(f"Created user ID: {user_id}")

    yield user_id


@allure.epic("User")
@allure.feature("User")
class TestUser:

    @allure.title("Check User by ID")
    def test_get_user_by_id(self, create_user):
        api_user = UserAPI()  # Важно: создаём новый экземпляр UserAPI в каждом тесте
        model = api_user.get_user_by_id(create_user)
        assert model.data.id == create_user
        assert model.message == "Користувача успішно отримано."

    @allure.title("Create toggle status")
    def test_create_status(self, create_user):
        api_user = UserAPI()

        model = api_user.create_status_inactive(create_user)
        assert model is not None
        assert model.message == "Статус успішно змінено."

        model = api_user.create_status_need_change_password(create_user)
        assert model is not None
        assert model.message == "Статус успішно змінено."

        model = api_user.create_status_blocked(create_user)
        assert model is not None
        assert model.message == "Статус успішно змінено."

        model = api_user.create_status_active(create_user)
        assert model is not None
        assert model.message == "Статус успішно змінено."

    @allure.title("Check User Audit by ID")
    def test_get_user_audit_by_id(self, create_user):
        api_user = UserAPI()
        model = api_user.get_user_audit_by_id(create_user)
        assert model.message == "Аудит користувача успішно отримано."

    def test_change_role_by_id(self, create_user):
        api_user = UserAPI()
        model = api_user.change_role_by_id(create_user)
        # assert model is not None
        # assert model.message == "Роль користувача змінено."

    @allure.title("Check User Role change by ID")
    def test_get_role_change_by_id(self, create_user):
        api_user = UserAPI()
        model = api_user.get_user_by_id(create_user)
        # assert model.data.roles, f"No roles found in response: {model.data}"
        # assert model.data.roles[1].id == 3 and model.data.roles[1].name == "test"

    @allure.title("Change User Password by ID")
    def test_change_password(self, create_user):
        api_user = UserAPI()
        model = api_user.change_password_by_id(create_user)
        assert model.message == "Пароль успішно змінено."

    @allure.title("Change User Info by ID")
    def test_change_user_info(self, create_user):
        api_user = UserAPI()
        model = api_user.change_user_info_by_id(create_user)
        assert model.message == "Користувача успішно оновлено."

    @allure.title("Get Users list by filters")
    def test_get_users_list(self):
        api_user = UserAPI()
        model = api_user.get_users_by_default_filters()
        assert model.message == "Дані успішно отримано."