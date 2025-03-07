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


    @allure.title("Get audit user by ID")
    def test_get_audit_by_id(self, user_id):
        self.api_adminuser.get_audit_by_id(user_id)



    @allure.title("Change password from admin")
    def test_change_password(self, user_id):
        self.api_adminuser.change_password_from_admin(user_id)
