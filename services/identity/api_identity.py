import allure
import requests
from config.headers import Headers
from utils.helper import Helper
from services.identity.endpoints import Endpoints
from services.identity.payloads import Payloads
from services.identity.models.identity_model import AuthModel, ChangePasswordModel #RefreshTokenModel


class IdentityAPI(Helper):

    def __init__(self) -> None:
        super().__init__()
        self.payloads = Payloads()
        self.endpoints = Endpoints()
        self.headers = Headers()


    @allure.step("Auth user and generate token")
    def auth_user_and_token(self):
        response = requests.post(
            url=self.endpoints.auth_user_and_token,
            headers=self.headers.basic,
            json=self.payloads.auth
        )
        print(response.json())
        assert response.status_code == 200, response.json()
        self.attach_response(response.json())
        model = AuthModel(**response.json())
        return model

    @allure.step("Auth user and generate token from admin")
    def auth_user_and_token_from_admin(self):
        response = requests.post(
            url=self.endpoints.auth_user_and_token_from_admin,
            headers=self.headers.basic,
            json=self.payloads.auth
        )
        print(response.json())
        assert response.status_code == 200, response.json()
        self.attach_response(response.json())
        model = AuthModel(**response.json())
        return model


    @allure.step("Change password")
    def change_password(self):
        response = requests.post(
            url=self.endpoints.change_password,
            headers=self.headers.basic,
            json=self.payloads.change_password
        )
        print(response.json())
        assert response.status_code == 200, response.json()
        self.attach_response(response.json())
        model = ChangePasswordModel(**response.json())
        return model

    # @allure.step("Refresh token")
    # def refresh_token(self):
    #     response = requests.post(
    #         url=self.endpoints.refresh_token,
    #         headers=self.headers.basic,
    #         json=self.payloads.refresh_token
    #     )
    #     print(response.json())
    #     assert response.status_code == 200, response.json()
    #     self.attach_response(response.json())
    #     model = RefreshTokenModel(**response.json())
    #     return model

