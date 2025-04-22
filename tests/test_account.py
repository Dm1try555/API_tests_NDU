import allure
from services.account.api_accounts import AccountAPI




@allure.epic("Account")
@allure.feature("Account")
class TestAccount:

    @classmethod
    def setup_class(cls):
        cls.api_account = AccountAPI()

    @allure.title("Create new account")
    def test_create_account(self):
        model = self.api_account.create_account()

    @allure.title("Check new account")
    def test_get_account(self):
        model = self.api_account.get_account()
        
        
