

HOST = "https://llc-cabinet-api-mwt.csd.ua/api/v1"

class Endpoints:

    create_admin_user = f"{HOST}/user/admin"
    get_admin_user_by_id = lambda self, id: f"{HOST}/user/admin/{id}"
    create_status = lambda self, id : f"{HOST}/user/admin/{id}/toggle-status"
    get_audit = lambda self, id : f"{HOST}/user/admin/{id}/audit"


    #update_info = lambda self, id : f"{HOST}/user/admin/{id}"
    change_password = lambda self, id : f"{HOST}/user/admin/{id}/change-password"



