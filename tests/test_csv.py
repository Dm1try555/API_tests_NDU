import allure
from services.csv.api_csv import CsvAPI


@allure.epic("CSV")
@allure.feature("CSV")
class TestCSV:

    @classmethod
    def setup_class(cls):
        cls.api_csv = CsvAPI()

    @allure.title("Get otg catalog")
    def test_get_otg_catalog(self):
        self.api_csv.get_otg_catalog()
        self.api_csv.get_otg_catalog_by_filter()


