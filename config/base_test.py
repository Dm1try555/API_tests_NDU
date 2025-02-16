from services.account.api_accounts import AccountAPI
from services.admin_user.api_adminuser import AdminUserAPI

class BaseTest:

    def setup_method(self):
          self.api_account = AccountAPI()
          self.api_adminuser = AdminUserAPI()
