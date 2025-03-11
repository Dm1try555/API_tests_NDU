import os
from dotenv import load_dotenv

load_dotenv()
HOST = os.getenv("HOST")

class Endpoints:

    get_user = f"{HOST}/user"
    create_user = f"{HOST}/user"
    change_status = lambda self, id: f"{HOST}/user/{id}/toggle-status"
    get_audit_by_id = lambda self, id: f"{HOST}/user/{id}/audit"
    get_user_by_id = lambda self, id: f"{HOST}/user/{id}"
    change_user_by_id = lambda self, id: f"{HOST}/user/{id}"
    change_role_by_id = lambda self, id: f"{HOST}/user/{id}/role"
    change_password_by_id = lambda self, id: f"{HOST}/user/{id}/change-password"







