import allure
import requests
from config.headers import Headers
from utils.helper import Helper
from services.llc.endpoints import Endpoints
from services.llc.payloads import Payloads, Params
from services.llc.models.llc_model import LlcModel


class LlcAPI(Helper):

    def __init__(self) -> None:
        super().__init__()
        self.payloads = Payloads()
        self.endpoints = Endpoints()
        self.headers = Headers()
        self.payloads = Payloads()


    @allure.step("Get llc by filter")
    def get_llc_by_filter(self):
        response = requests.get(
            url=self.endpoints.get_llc,
            headers=self.headers.basic,
            params= Params.llc_params
        )
        print(response.json())
        assert response.status_code == 200, response.json()
        self.attach_response(response.json())
        model = LlcModel(**response.json())
        return model

