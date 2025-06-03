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
        assert model.message == "Дані успішно оновлено."
        assert isinstance(model.message, str), f"Очікувався рядок, отримано {type(model.message)}"


    @allure.title("Check new account")
    def test_get_account(self):
        model = self.api_account.get_account()
        assert model.message == "Дані успішно отримано."
        assert isinstance(model.data.id, int), f"Очікувався тип 'int', але отримано {type(model.data.id)}"
        
        
