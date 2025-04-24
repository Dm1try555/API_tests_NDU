import allure
import requests
from config.headers import Headers
from utils.helper import Helper
from services.kep.endpoints import Endpoints
from services.kep.payloads import Payloads

class KepAPI(Helper):

    def __init__(self) -> None:
        super().__init__()
        self.endpoints = Endpoints()
        self.headers = Headers()
        self.payloads = Payloads()

    
    @allure.step("Get KEP integration")
    def get_kep_integration(self):
        response = requests.get(
            url=self.endpoints.get_kep_integration,
            headers=self.headers.basic,
        )
        # print(response.json())
        assert response.status_code == 200, response.json()
        # self.attach_response(response.json())
        # model = GetKepIntegrationListModel.model_validate(response.json())
        return  #model
