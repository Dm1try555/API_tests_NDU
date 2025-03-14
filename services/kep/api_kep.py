import allure
import requests
from config.headers import Headers
from utils.helper import Helper
from services.kep.endpoints import Endpoints
from services.kep.payloads import Payloads
from services.kep.models.kep_model import KepVerifyModel, GetKepGenerateModel, GetKepIntegrationListModel

class KepAPI(Helper):

    def __init__(self) -> None:
        super().__init__()
        self.endpoints = Endpoints()
        self.headers = Headers()
        self.payloads = Payloads()

    @allure.step("Create KEP verify")
    def create_kep_verify(self):
        response = requests.post(
            url=self.endpoints.create_kep_verify,
            headers=self.headers.basic,
            json=self.payloads.create_kep_verify
        )
        print(response.json())
        assert response.status_code == 200, response.json()
        self.attach_response(response.json())
        model = KepVerifyModel(**response.json())
        return model

    @allure.step("Create KEP verify hash")
    def create_kep_verify_hash(self):
        response = requests.post(
            url=self.endpoints.create_kep_verify_hash,
            headers=self.headers.basic,
            json=self.payloads.create_kep_verify
        )
        print(response.json())
        assert response.status_code == 200, response.json()
        self.attach_response(response.json())
        model = KepVerifyModel(**response.json())
        return model


    @allure.step("Create KEP generate hash")
    def create_kep_generate_hash(self):
        response = requests.post(
            url=self.endpoints.create_kep_generate_hash,
            headers=self.headers.basic,
            json=self.payloads.create_kep_generate_hash
        )
        print(response.text)
        assert response.status_code == 200, response.json()
        assert response.text is not None

    @allure.step("Get KEP generate")
    def get_kep_generate(self):
        response = requests.get(
            url=self.endpoints.get_kep_generate,
            headers=self.headers.basic,
        )
        print(response.json())
        assert response.status_code == 200, response.json()
        self.attach_response(response.json())
        model = GetKepGenerateModel(**response.json())
        return model

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
        return #model
