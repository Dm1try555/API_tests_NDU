import allure
import pytest
from services.admin_user.api_adminuser import AdminUserAPI


@allure.epic("AdminUser")
@allure.feature("AdminUser")
class TestAdminUser:

    @classmethod
    def setup_class(cls):

        cls.api_adminuser = AdminUserAPI()

    @pytest.fixture(scope="class", autouse=True)
    @allure.title("Create new user from admin portal")
    def user_id(self):
        user = self.api_adminuser.create_user_from_admin()
        print(f"Створений користувач з ID: {user.data.id}")
        return user.data.id

    @allure.title("Test user creation")
    def test_create_user_from_admin(self, user_id):
        assert user_id is not None, "Помилка: ID користувача не створений!"
        get_user_by_id = self.api_adminuser.get_user_by_id(user_id)
        assert get_user_by_id.data.id == user_id, "Помилка: ID користувача не збігається!"

    @allure.title("Check new user by ID")
    def test_check_create_user_by_id(self, user_id):
        self.api_adminuser.get_user_by_id(user_id)

    @allure.title("Create toggle status")
    def test_create_status(self, user_id):
        self.api_adminuser.create_status_inactive(user_id)
        self.api_adminuser.get_status_inactive(user_id)
        self.api_adminuser.create_status_need_change_password(user_id)
        self.api_adminuser.get_status_need_change_password(user_id)
        self.api_adminuser.create_status_active(user_id)
        self.api_adminuser.get_status_active(user_id)

    @allure.title("Change role for user")
    def test_change_role_user(self, user_id):
        change_role = self.api_adminuser.change_role_user(user_id)
        check_role = self.api_adminuser.get_role_user(user_id)
        assert check_role.data.roles is not None and len(check_role.data.roles) > 0
        first_role = check_role.data.roles[0]

        assert first_role.id == 3








@allure.epic("GetAdminUser")
@allure.feature("GetAdminUser")
class TestGetAdminUser:

    @classmethod
    def setup_class(cls):
        cls.api_adminuser = AdminUserAPI()

    @allure.title("Get list of users with filtering and sorting")
    def test_get_users_by_filters(self):
        model_default = self.api_adminuser.get_users_by_filters_default()
        assert model_default.message == "Дані успішно отримано."

        model_active = self.api_adminuser.get_users_by_filters_active()
        assert model_active.data.items[0].status == "Active"

        model_inactive = self.api_adminuser.get_users_by_filters_inactive()
        assert model_inactive.data.items[0].status == "Inactive"

        model_need_change_password = self.api_adminuser.get_users_by_filters_need_change_password()
        assert any(user.status == "NeedChangePassword" for user in model_need_change_password.data.items)


