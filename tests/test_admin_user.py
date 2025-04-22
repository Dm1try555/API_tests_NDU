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
        print(f"Created user with ID: {user.data.id}")
        return user.data.id

    @allure.title("Test user creation")
    def test_create_user_from_admin(self, user_id):
        assert user_id is not None, "Error: User ID not created!"
        model = self.api_adminuser.get_user_by_id(user_id)
        assert model.data.id == user_id, "Error: User IDs do not match!"

    @allure.title("Check new user by ID")
    def test_check_create_user_by_id(self, user_id):
        model = self.api_adminuser.get_user_by_id(user_id)

    @allure.title("Change toggle status and check status")
    def test_change_status(self, user_id):
        model_inactive = self.api_adminuser.create_status_inactive(user_id)
        model_check = self.api_adminuser.get_status_inactive(user_id)
        model_change_pass = self.api_adminuser.create_status_need_change_password(user_id)
        model_check = self.api_adminuser.get_status_need_change_password(user_id)
        model_active = self.api_adminuser.create_status_active(user_id)
        model_check = self.api_adminuser.get_status_active(user_id)


    @allure.title("Get audit log by user ID")
    def test_get_audit_by_id(self, user_id):
        model = self.api_adminuser.get_audit_by_id(user_id)



    @allure.title("Update user details and check details")
    def test_update_details(self, user_id):
        model = self.api_adminuser.update_user_info(user_id)
        check_details = self.api_adminuser.get_user_by_id(user_id)
        assert model.data.firstName == check_details.data.firstName, "Error: First names do not match!"
        assert model.data.lastName == check_details.data.lastName, "Error: Last names do not match!"
        assert model.data.middleName == check_details.data.middleName, "Error: Middle names do not match!"
        assert model.data.identityNumber == check_details.data.identityNumber, "Error: Identity numbers do not match!"
        assert model.data.login == check_details.data.login, "Error: Logins do not match!"



    @allure.title("Change role for user and check role")
    def test_change_role_user(self, user_id):
        model = self.api_adminuser.change_role_user(user_id)
        check_role = self.api_adminuser.get_role_user(user_id)
        
    @allure.title("Change password for user and check password")
    def test_change_password(self, user_id):
        model = self.api_adminuser.update_password(user_id)





@allure.epic("GetAdminUserByFilters")
@allure.feature("GetAdminUserByFilters")
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


