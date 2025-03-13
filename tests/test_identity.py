import allure
from services.identity.api_identity import IdentityAPI


@allure.epic("Identity")
@allure.feature("Identity")
class TestIdentity:

    @classmethod
    def setup_class(cls):

        cls.api_identity = IdentityAPI()


    @allure.title("Auth user and generate token")
    def test_auth_user_and_token(self):
        model = self.api_identity.auth_user_and_token()
        assert model.message and model.data is not None

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

    @allure.title("Get Hash")
    def test_get_hash(self):
        model = self.api_identity.get_hash()
        assert model.message == "Згенеровано унікальний ключ."
        assert model.data is not None



