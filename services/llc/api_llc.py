import allure
import requests
from config.headers import Headers
from utils.helper import Helper
from services.llc.endpoints import Endpoints
from services.llc.payloads import Params
from services.llc.models.llc_model import LlcModel, MyLLCModel, LlcIdModel, LlcSearchModel


class LlcAPI(Helper):

    def __init__(self) -> None:
        super().__init__()
        self.endpoints = Endpoints()
        self.headers = Headers()
        self.params = Params()

    
    @allure.step("Get llc by filter")
    def get_llc_by_filter(self):
        response = requests.get(
            url=self.endpoints.get_llc,
            headers=self.headers.basic,
            params= self.params.llc_params
        )
        print(response.json())
        assert response.status_code == 200, response.json()
        self.attach_response(response.json())
        model = LlcModel(**response.json())
        return model

    @allure.step("Get llc Search")
    def get_llc_search(self):
        response = requests.get(
            url=self.endpoints.get_llc_search,
            headers=self.headers.basic,
            params= self.params.llc_search
        )
        print(response.json())
        assert response.status_code == 200, response.json()
        self.attach_response(response.json())
        model = LlcSearchModel(**response.json())
        return model
    

    @allure.step("Get llc by ID")
    def get_llc_by_id(self, id):
        response = requests.get(
            url=self.endpoints.get_llc_by_id(id),
            headers=self.headers.basic
        )
        print(response.json())
        print(response.url)
        assert response.status_code == 200, response.json()
        self.attach_response(response.json())
        model = LlcIdModel(**response.json())
        return model

    @allure.step("Get my llc")
    def get_my_llc(self):
        response = requests.get(
            url=self.endpoints.get_myllc,
            headers=self.headers.basic,
            params= self.params.myllc_params
        )
        print(response.json())
        assert response.status_code == 200, response.json()
        self.attach_response(response.json())
        model = MyLLCModel(**response.json())
        return model