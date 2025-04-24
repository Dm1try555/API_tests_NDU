import allure
from services.kep.api_kep import KepAPI




@allure.epic("KEP")
@allure.feature("KEP")
class TestKep:

    @classmethod
    def setup_class(cls):
        cls.api_kep = KepAPI()



    @allure.title("Get KEP integration")
    def test_get_kep_integration(self):
        model = self.api_kep.get_kep_integration()


