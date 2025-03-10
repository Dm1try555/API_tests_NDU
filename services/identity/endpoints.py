import os
from dotenv import load_dotenv

load_dotenv()
HOST = os.getenv("HOST")


class Endpoints:

    auth_user_and_token = f"{HOST}/identity/authenticate"
    auth_user_and_token_from_admin = f"{HOST}/identity/admin/authenticate"
    change_password = f"{HOST}/identity/change-password"
    refresh_token = f"{HOST}/identity/refreshtoken"
    get_dropass_by_id = lambda self, id: f"{HOST}/identity/{id}/dropass"
    get_hash = f"{HOST}/identity/hash"
    create_hash = f"{HOST}/identity/authenticate/hash"
    create_hash_base64 = f"{HOST}/identity/authenticate/hash/base64"



