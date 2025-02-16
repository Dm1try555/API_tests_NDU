import allure
import requests
from config.headers import Headers
from utils.helper import Helper
from services.signature.endpoints import Endpoints
from services.signature.payloads import Params
from services.signature.models.signature_model import SignatureModel, SignatureByIdModel


class SignatureAPI(Helper):

    def __init__(self) -> None:
        super().__init__()
        #self.payloads = Payloads()
        self.endpoints = Endpoints()
        self.headers = Headers()


    @allure.step("Get signature by filter")
    def get_signature_by_filter(self):
        response = requests.get(
            url=self.endpoints.get_signature,
            headers=self.headers.basic,
            params= Params.signature_params
        )
        assert response.status_code == 200, response.json()
        response_json = response.json()
        self.attach_response(response_json)
        print(response_json)
        model = SignatureModel(**response_json)
        signature_id = response_json.get("data", {}).get("items", [{}])[0].get("id")
        assert signature_id, "ID не знайдено у відповіді API"
        return model, signature_id


    @allure.step("Get signature by ID")
    def get_signature_by_id(self, id):
        assert id, "ID не може бути порожнім або None"

        response = requests.get(
            url=self.endpoints.get_signature_by_id(id),
            headers=self.headers.basic,
        )
        print(response.json())
        assert response.status_code == 200, response.json()
        self.attach_response(response.json())
        model = SignatureByIdModel(**response.json())
        return model

