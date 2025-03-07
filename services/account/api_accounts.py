import allure
import requests
from utils.helper import Helper
from services.account.endpoints import Endpoints
from services.account.payloads import Payloads
from config.headers import Headers
from services.account.models.account_model import CreateAccountModel


class AccountAPI(Helper):

    def __init__(self):
        super().__init__()
        self.payloads = Payloads()
        self.endpoints = Endpoints()
        self.headers = Headers()


    @allure.step("Create account")
    def create_account(self):
        response = requests.post(
            url=self.endpoints.create_account,
            headers=self.headers.basic,
            json=self.payloads.create_account
        )
        response_json = response.json()
        print(response.json())
        assert "message" in response_json, "Ключ 'message' відсутній у відповіді"
        assert isinstance(response_json["message"], str), f"Очікувався рядок, отримано {type(response_json['message'])}"
        assert response.status_code == 200, response.json()
        self.attach_response(response.json())
        model = CreateAccountModel(**response.json())
        assert model.message == "Дані успішно оновлено."
        return model

    @allure.step("Get account")
    def get_account(self):
        response = requests.get(
            url=self.endpoints.get_account,
            headers=self.headers.basic,
        )
        print(response.json())
        assert response.status_code == 200, response.json()
        self.attach_response(response.json())
        model = CreateAccountModel(**response.json())
        assert model.message == "Дані успішно отримано."
        return model