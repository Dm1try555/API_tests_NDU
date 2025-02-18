import allure
import pytest
from config.base_test import BaseTest


@allure.epic("Account")
@allure.feature("Account")
class TestAccount(BaseTest):

    @pytest.mark.account
    @allure.title("Create new account")
    def test_create_account(self):
        acc = self.api_account.create_account()
        get = self.api_account.get_account()




