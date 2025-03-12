import allure
import requests
from config.headers import Headers
from utils.helper import Helper
from services.signature.endpoints import Endpoints
from services.signature.payloads import Params, Payloads
from services.signature.models.signature_model import (GetSignatureModel, GetSignatureByIdModel,
                                                       ChangeSignatureModel, CreateSignatureModel,
                                                       DeleteSignatureModel)


class SignatureAPI(Helper):

    def __init__(self) -> None:
        super().__init__()
        self.payloads = Payloads()
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
        self.attach_response(response.json())
        model = GetSignatureModel(**response.json())
        return model


    @allure.step("Get signature by ID")
    def get_signature_by_id(self, id):
        assert id, "ID cannot be empty or None"

        response = requests.get(
            url=self.endpoints.get_signature_by_id(id),
            headers=self.headers.basic,
        )
        print(response.json())
        assert response.status_code == 200, response.json()
        self.attach_response(response.json())
        model = GetSignatureByIdModel(**response.json())
        return model

    @allure.step("Change signature by SignatureSystemID")
    def change_signature_by_id(self, id):
        response = requests.put(
            url=self.endpoints.change_signature_by_id(id),
            headers=self.headers.basic,
            json=self.payloads.change_signature
        )
        print(response.json())
        assert response.status_code == 200, response.json()
        self.attach_response(response.json())
        model = ChangeSignatureModel(**response.json())
        return model

    @allure.step("Create signature")
    def create_signature(self):
        response = requests.post(
            url=self.endpoints.create_signature,
            headers=self.headers.basic,
            json=self.payloads.create_signature
        )
        print(response.json())
        assert response.status_code == 200, response.json()
        self.attach_response(response.json())
        model = CreateSignatureModel(**response.json())
        return model


    @allure.step("Delete signature")
    def delete_signature(self, id):
        response = requests.delete(
            url=self.endpoints.delete_signature_by_id(id),
            headers=self.headers.basic
        )
        print(response.json())
        assert response.status_code == 200, response.json()
        self.attach_response(response.json())
        model = DeleteSignatureModel(**response.json())
        return model

