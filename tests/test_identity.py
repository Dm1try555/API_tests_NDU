import allure
import pytest
from config.base_test import BaseTest
from services.identity.api_identity import IdentityAPI


@allure.epic("Identity")
@allure.feature("Identity")
class TestIdentity:

    @classmethod
    def setup_class(cls):

        cls.api_identity = IdentityAPI()


    @allure.title("Auth user and generate token")
    def test_auth_user_and_token(self):
        auth = self.api_identity.auth_user_and_token()


    @allure.title("Auth user and generate token from admin")
    def test_auth_user_and_token_from_admin(self):
        auth = self.api_identity.auth_user_and_token_from_admin()

    @allure.title("Change password")
    def test_change_password(self):
        change_password = self.api_identity.change_password()



