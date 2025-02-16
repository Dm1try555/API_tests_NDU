import allure
import requests
from config.headers import Headers
from utils.helper import Helper
from services.csv.endpoints import Endpoints
from services.csv.models.csv_model import CsvModel, CsvByFilterModel


class CsvAPI(Helper):

    def __init__(self) -> None:
        super().__init__()
        self.endpoints = Endpoints()
        self.headers = Headers()



    @allure.step("Get otg catalog")
    def get_otg_catalog(self):
        response = requests.get(
            url=self.endpoints.get_csv,
            headers=self.headers.basic,
            params={"filter": ""}
        )
        #print(response.json())
        assert response.status_code == 200, response.json()
        self.attach_response(response.json())
        model = CsvModel(**response.json()[0])
        return model

    @allure.step("Get otg catalog by filter")
    def get_otg_catalog_by_filter(self):
        response = requests.get(
            url=self.endpoints.get_csv,
            headers=self.headers.basic,
            params={"filter": "UA74100370070070896"}
        )
        print(response.json())
        assert response.status_code == 200, response.json()
        self.attach_response(response.json())
        model = CsvByFilterModel(**response.json()[0])
        expected_data = [{
            'ctnreG_CODE': 'UA74100370070070896',
            'ctnreG_DESC': 'Чернігівська обл. Чернігівський р-н. Тупичівська тер. громада с.Івашківка '
        }]

        assert response.status_code == 200
        assert response.json() == expected_data
        return model









