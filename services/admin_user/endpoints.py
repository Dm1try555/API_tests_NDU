import os
from dotenv import load_dotenv

load_dotenv()
HOST = os.getenv("HOST")


class Endpoints:

    get_admin_user = f"{HOST}/user/admin"
    create_admin_user = f"{HOST}/user/admin"
    create_status = lambda self, id: f"{HOST}/user/admin/{id}/toggle-status"
    get_audit = lambda self, id: f"{HOST}/user/admin/{id}/audit"
    get_admin_user_by_id = lambda self, id: f"{HOST}/user/admin/{id}"
    change_info_user = lambda self, id : f"{HOST}/user/admin/{id}"
    change_role_user = lambda self, id : f"{HOST}/user/admin/{id}/role"
    change_password = lambda self, id : f"{HOST}/user/admin/{id}/change-password"



