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
        self.__class__.role_id = model.data.id
        print(f"Create role ID: {self.__class__.role_id}")

    @allure.title("Check Role by ID")
    def test_get_role_by_id(self):
        assert self.__class__.role_id is not None
        model = self.api_role.get_role_by_id(self.__class__.role_id)
        assert model.data.id == self.__class__.role_id

    @allure.title("Change Role by ID")
    def test_change_role_by_id(self):
        assert self.__class__.role_id is not None
        model = self.api_role.change_role_by_id(self.__class__.role_id)
        assert model.data.id == self.__class__.role_id

    @allure.title("Check Role change by ID")
    def test_get_role_change_by_id(self):
        assert self.__class__.role_id is not None
        model = self.api_role.get_role_by_id(self.__class__.role_id)
        assert model.data.id == self.__class__.role_id

    @allure.title("Get all Role permissions")
    def test_get_role_permissions(self):
        model = self.api_role.get_role_permissions()
        assert model.message == "Дані успішно отримано"
        assert model.data is not None

    @allure.title("Get admin Role permissions")
    def test_get_admin_role_permissions(self):
        model = self.api_role.get_admin_role_permissions()
        assert model.message == "Дані успішно отримано"
        assert model.data is not None

    @allure.title("Get client Role permissions")
    def test_get_client_role_permissions(self):
        model = self.api_role.get_client_role_permissions()
        assert model.message == "Дані успішно отримано"
        assert model.data is not None









            # @allure.title("Create KEP verify hash")
    # def test_create_kep_verify_hash(self):
    #     model = self.api_kep.create_kep_verify_hash()
    #     assert model.message == "Підпис дійний."
    #
    # @allure.title("Create KEP generate hash")
    # def test_create_kep_generate_hash(self):
    #     model = self.api_kep.create_kep_generate_hash()
    #
    # @allure.title("Get KEP generate")
    # def test_get_kep_generate(self):
    #     model = self.api_kep.get_kep_generate()


