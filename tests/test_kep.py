import allure
from services.kep.api_kep import KepAPI




@allure.epic("KEP")
@allure.feature("KEP")
class TestKep:

    @classmethod
    def setup_class(cls):
        cls.api_kep = KepAPI()

    @allure.title("Create KEP verify")
    def test_create_kep_verify(self):
        model = self.api_kep.create_kep_verify()
        assert model.message == "Підпис дійний."

    @allure.title("Create KEP verify hash")
    def test_create_kep_verify_hash(self):
        model = self.api_kep.create_kep_verify_hash()
        assert model.message == "Підпис дійний."

    @allure.title("Create KEP generate hash")
    def test_create_kep_generate_hash(self):
        model = self.api_kep.create_kep_generate_hash()

    @allure.title("Get KEP generate")
    def test_get_kep_generate(self):
        model = self.api_kep.get_kep_generate()

    @allure.title("Get KEP integration")
    def test_get_kep_integration(self):
        model = self.api_kep.get_kep_integration()
        assert model is not None


