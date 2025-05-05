import allure
import pytest
from services.user.api_user import UserAPI
import uuid
from faker import Faker
from services.user.payloads import Payloads

fake = Faker()



# class Payloads:
#     @staticmethod
#     def create_user():
#         unique_login = f"{fake.user_name()}_{uuid.uuid4().hex[:8]}"
#         return {
#             "password": fake.password(special_chars=True, digits=True, upper_case=True, lower_case=True),  # length=14
#             "login": unique_login,
#             "firstName": fake.first_name(),
#             "middleName": fake.first_name(),
#             "lastName": fake.last_name(),
#             "identityNumber": "1234567890"
#         }



# @pytest.fixture(scope="function")
# def create_user():
#     with allure.step("Create a new user"):
#         api_user = UserAPI()

#         api_user.payloads.create_user = Payloads.create_user()

#         model = api_user.create_user()
#         assert model.message == "Користувача зареєстровано."
#         user_id = model.data.id
#         print(f"Created user ID: {user_id}")

#     yield user_id


@allure.epic("User")
@allure.feature("User")
class TestUser:


    @classmethod
    def setup_class(cls):
        cls.api_user = UserAPI()
        cls.user_id = None



    @allure.title("Create User")
    def test_create_user(self):
        model = self.api_user.create_user()
        assert model.message == "Користувача зареєстровано."
        assert model.data.id is not None, "User ID is None"
        assert model.data is not None, "User data is None"
        self.__class__.user_id = model.data.id
        print(f"Created user ID: {self.__class__.user_id}")


    @allure.title("Check User by ID")
    def test_get_user_by_id(self):
        assert self.__class__.user_id is not None, "user_id не задано!"
        model = self.api_user.get_user_by_id(self.__class__.user_id)
        assert model.data.id == self.__class__.user_id, "The ID in the response does not match the expected one"
        assert model.message == "Користувача успішно отримано."
        assert model.data is not None, "User data is None"


    @allure.title("Create toggle status")
    def test_create_status(self):
        assert self.__class__.user_id is not None, "user_id не задано!"
        model = self.api_user.create_status_inactive(self.__class__.user_id)
        assert model is not None
        assert model.message == "Статус успішно змінено."

        model = self.api_user.create_status_need_change_password(self.__class__.user_id)
        assert model is not None
        assert model.message == "Статус успішно змінено."

        model = self.api_user.create_status_blocked(self.__class__.user_id)
        assert model is not None
        assert model.message == "Статус успішно змінено."

        model = self.api_user.create_status_active(self.__class__.user_id)
        assert model is not None
        assert model.message == "Статус успішно змінено."

    @allure.title("Check User Audit by ID")
    def test_get_user_audit_by_id(self):
        model = self.api_user.get_user_audit_by_id(self.__class__.user_id)
        assert model.message == "Аудит користувача успішно отримано."

    def test_change_role_by_id(self):
        model = self.api_user.change_role_by_id(self.__class__.user_id)
        
    @allure.title("Check User Role change by ID")
    def test_get_role_change_by_id(self):
        model = self.api_user.get_user_by_id(self.__class__.user_id)
        assert model.message == "Користувача успішно отримано."
        assert model.data is not None, "User data is None"
        assert model.data.roles is not None, "Roles data is None"
        assert len(model.data.roles) > 0, "No roles found in response"
        assert model.data.roles[0].name == "Recruitment consultant"
        

    @allure.title("Change User Password by ID")
    def test_change_password(self):
        model = self.api_user.change_password_by_id(self.__class__.user_id)
        assert model.message == "Пароль успішно змінено."

    @allure.title("Change User Info by ID")
    def test_change_user_info(self):
        value = Payloads.change_info_user
        model = self.api_user.change_user_info_by_id(self.__class__.user_id)
        assert model.message == "Користувача успішно оновлено."
        assert model.data is not None, "User data is None"
        assert model.data.id == self.__class__.user_id, "The ID in the response does not match the expected one"
        assert model.data.firstName == value["firstName"], "First name does not match"
        assert model.data.middleName == value["middleName"], "Middle name does not match"
        assert model.data.lastName == value["lastName"], "Last name does not match"
        assert model.data.identityNumber == value["identityNumber"], "Identity number does not match"
        assert model.data.login == value["login"], "Login does not match"

    @allure.title("Check User Info by ID after change")
    def test_get_user_info_by_id(self):
        model = self.api_user.get_user_by_id(self.__class__.user_id)
        assert model.message == "Користувача успішно отримано."
        assert model.data is not None, "User data is None"
        assert model.data.id == self.__class__.user_id, "The ID in the response does not match the expected one"
        assert model.data.firstName == Payloads.change_info_user["firstName"], "First name does not match"
        assert model.data.middleName == Payloads.change_info_user["middleName"], "Middle name does not match"
        assert model.data.lastName == Payloads.change_info_user["lastName"], "Last name does not match"
        assert model.data.identityNumber == Payloads.change_info_user["identityNumber"], "Identity number does not match"
        assert model.data.login == Payloads.change_info_user["login"], "Login does not match"
        


    @allure.title("Get Users list by filters")
    def test_get_users_list(self):
        model = self.api_user.get_users_by_default_filters()
        assert model.message == "Дані успішно отримано."