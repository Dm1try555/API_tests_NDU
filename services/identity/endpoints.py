import os
from dotenv import load_dotenv

load_dotenv()
HOST = os.getenv("HOST")


class Endpoints:

    auth_user_and_token = f"{HOST}/identity/authenticate"
    auth_code = f"{HOST}/identity/authenticate/code"
    #auth_kep = f"{HOST}/identity/authenticate/kep"
    auth_user_and_token_from_admin = f"{HOST}/identity/admin/authenticate"
    change_password = f"{HOST}/identity/change-password"
    refresh_token = f"{HOST}/identity/refreshtoken"
    get_dropass_by_id = lambda self, id: f"{HOST}/identity/{id}/dropass"


