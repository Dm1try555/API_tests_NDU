import os
from dotenv import load_dotenv

load_dotenv()
HOST = os.getenv("HOST")

class Endpoints:

    get_permission = f"{HOST}/role/permission"
    get_permission_admin = f"{HOST}/role/permission/admin"
    get_permission_client = f"{HOST}/role/permission/client"
    get_role_by_id = lambda self, id: f"{HOST}/role/{id}"
    change_role_by_id = lambda self, id: f"{HOST}/role/{id}"
    get_role = f"{HOST}/role"
    create_role = f"{HOST}/role"






