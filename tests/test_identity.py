import allure
from services.identity.api_identity import IdentityAPI


@allure.epic("Identity")
@allure.feature("Identity")
class TestIdentity:

    @classmethod
    def setup_class(cls):
        cls.api_identity = IdentityAPI()
        cls.login = "141245"

    def setup_method(self):
        # Авторизація та отримання refresh_token перед кожним тестом
        model = self.api_identity.auth_user_and_token()
        assert model.message and model.data is not None
        self.refresh_token = model.data.refreshToken
        print(f"Refresh token: {self.refresh_token}")

    @allure.title("Auth user and generate token")
    def test_auth_user_and_token(self):
        model = self.api_identity.auth_user_and_token()
        assert model.message and model.data is not None
        print(f"Refresh token: {self.refresh_token}")

    @allure.title("Refresh token")
    def test_refresh_token(self):
        print(f"Refresh token before test: {self.refresh_token}")
        model = self.api_identity.refresh_token(
            login=self.__class__.login, 
            refresh_token=self.refresh_token)
        print(f"Refresh token after test: {model.data.refreshToken}")
        assert model.message == "Authenticated mike"

    @allure.title("Auth user code(token)")
    def test_auth_user_code(self):
        model = self.api_identity.auth_user_code()
        assert model.token is not None

    @allure.title("Auth user and generate token from admin")
    def test_auth_user_and_token_from_admin(self):
        model = self.api_identity.auth_user_and_token_from_admin()
        assert model.message and model.data is not None

    @allure.title("Change password")
    def test_change_password(self):
        model = self.api_identity.change_password()
        assert model.message is not None