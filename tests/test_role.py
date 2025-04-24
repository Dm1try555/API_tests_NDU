import allure
import pytest
from services.role.api_role import RoleAPI
from faker import Faker

fake = Faker()



class Payloads:
    @staticmethod
    def create_role():
        return {
            "role": {
                "name": fake.job(),
                "description": fake.sentence(),
                "dependCodes": [
                    fake.uuid4()
                ],
                "isAdminPart": fake.boolean()
            },
            "grantedPermissionNames": [
                fake.word()
            ]
        }


@allure.epic("Role")
@allure.feature("Role Management")
class TestRole:

    @classmethod
    def setup_class(cls):
        cls.api_role = RoleAPI()
        cls.id_role = None

    @allure.title("Create new Role")
    def test_create_role(self):
        model = self.api_role.create_role()
        assert model and model.data, "Role creation failed or returned empty data"
        assert model.data.id is not None, f"Role ID is missing or None, received: {model.data}"
        self.__class__.id_role = model.data.id
        print(f"Created role ID: {self.__class__.id_role}")

    @allure.title("Check Role by ID")
    def test_get_role_by_id(self):
        assert self.__class__.id_role is not None, "Role ID is None, cannot proceed with test"
        model = self.api_role.get_role_by_id(self.__class__.id_role)
        assert model and model.data, "Failed to retrieve role by ID"
        assert model.data.id == self.__class__.id_role, f"Role ID mismatch: {model.data.id} != {create_role}"

    @allure.title("Change Role by ID")
    def test_change_role_by_id(self):
        model = self.api_role.change_role_by_id(self.__class__.id_role)
        assert model and model.data, "Failed to change role by ID"
        assert model.data.id == self.__class__.id_role, f"Role ID mismatch after change: {model.data.id} != {create_role}"

    @allure.title("Verify Role change by ID")
    def test_get_role_change_by_id(self):
        change = self.api_role.change_role_by_id(self.__class__.id_role)
        model = self.api_role.get_role_by_id(self.__class__.id_role)
        assert model and model.data, "Failed to retrieve role by ID after change"
        assert model.data.id == self.__class__.id_role, f"Role ID mismatch after change: {model.data.id} != {create_role}"

    @allure.title("Get all Role permissions")
    def test_get_role_permissions(self):
        model = self.api_role.get_role_permissions()
        assert model and model.data, "Role permissions data is empty"
        assert model.message == "Дані успішно отримано", f"Unexpected message: {model.message}"

    @allure.title("Get admin Role permissions")
    def test_get_admin_role_permissions(self):
        model = self.api_role.get_admin_role_permissions()
        assert model and model.data, "Admin role permissions data is empty"
        assert model.message == "Дані успішно отримано", f"Unexpected message: {model.message}"

    @allure.title("Get client Role permissions")
    def test_get_client_role_permissions(self):
        model = self.api_role.get_client_role_permissions()
        assert model and model.data, "Client role permissions data is empty"
        assert model.message == "Дані успішно отримано", f"Unexpected message: {model.message}"

    @allure.title("Get list of roles")
    def test_get_role_by_filters(self):
        model = self.api_role.get_role_by_filters()
        assert model and model.data, "Role filter data is empty"