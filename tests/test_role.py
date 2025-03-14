import allure
from services.role.api_role import RoleAPI


@allure.epic("Role")
@allure.feature("Role")
class TestRole:
    role_id = None

    @classmethod
    def setup_class(cls):
        cls.api_role = RoleAPI()

    @allure.title("Create new Role")
    def test_create_role(self):
        model = self.api_role.create_role()
        assert model is not None, "Role creation failed, received None"
        assert model.data is not None, "Role data is empty"
        assert model.data.id is not None, "Role ID is missing"
        self.__class__.role_id = model.data.id
        print(f"Create role ID: {self.__class__.role_id}")

    @allure.title("Check Role by ID")
    def test_get_role_by_id(self):
        assert self.__class__.role_id is not None, "Role ID is not set"
        model = self.api_role.get_role_by_id(self.__class__.role_id)
        assert model is not None, "Failed to retrieve role by ID"
        assert model.data.id == self.__class__.role_id, f"Role ID mismatch: {model.data.id} != {self.__class__.role_id}"

    @allure.title("Change Role by ID")
    def test_change_role_by_id(self):
        assert self.__class__.role_id is not None, "Role ID is not set"
        model = self.api_role.change_role_by_id(self.__class__.role_id)
        assert model is not None, "Failed to change role by ID"
        assert model.data.id == self.__class__.role_id, f"Role ID mismatch after change: {model.data.id} != {self.__class__.role_id}"

    @allure.title("Check Role change by ID")
    def test_get_role_change_by_id(self):
        assert self.__class__.role_id is not None, "Role ID is not set"
        model = self.api_role.get_role_by_id(self.__class__.role_id)
        assert model is not None, "Failed to retrieve role by ID after change"
        assert model.data.id == self.__class__.role_id, f"Role ID mismatch after change: {model.data.id} != {self.__class__.role_id}"

    @allure.title("Get all Role permissions")
    def test_get_role_permissions(self):
        model = self.api_role.get_role_permissions()
        assert model.message == "Дані успішно отримано", f"Unexpected message: {model.message}"
        assert model.data is not None, "Role permissions data is empty"

    @allure.title("Get admin Role permissions")
    def test_get_admin_role_permissions(self):
        model = self.api_role.get_admin_role_permissions()
        assert model.message == "Дані успішно отримано", f"Unexpected message: {model.message}"
        assert model.data is not None, "Admin role permissions data is empty"

    @allure.title("Get client Role permissions")
    def test_get_client_role_permissions(self):
        model = self.api_role.get_client_role_permissions()
        assert model.message == "Дані успішно отримано", f"Unexpected message: {model.message}"
        assert model.data is not None, "Client role permissions data is empty"

    @allure.title("Get list of roles")
    def test_get_role_by_filters(self):
        model = self.api_role.get_role_by_filters()
        assert model.data is not None, "Role filter data is empty"

