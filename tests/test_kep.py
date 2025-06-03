import allure
from services.kep.api_kep import KepAPI


@allure.epic("KEP")
@allure.feature("KEP")
class TestKep:

    @classmethod
    def setup_class(cls):
        cls.api_kep = KepAPI()



    @allure.title("Create KEP integration")
    def test_create_kep_integration(self):
        model = self.api_kep.create_kep_integration()


