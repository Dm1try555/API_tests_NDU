import allure
import requests
from config.headers import Headers
from utils.helper import Helper
from services.admin_user.endpoints import Endpoints
from services.admin_user.payloads import Payloads
from services.admin_user.models.adminuser_model import (CreateAdminUserModel, AdminUserAuditModel,
                                                        AdminUserPassword, StatusModel, GetAdminUserModel,
                                                        ChangeAdminUserModel)


class AdminUserAPI(Helper):

    def __init__(self) -> None:
        super().__init__()
        self.payloads = Payloads()
        self.endpoints = Endpoints()
        self.headers = Headers()


    @allure.step("Create new user from admin portal")
    def create_user_from_admin(self):
        response = requests.post(
            url=self.endpoints.create_admin_user,
            headers=self.headers.basic,
            json=self.payloads.create_user_from_admin
        )
        print(response.json())
        assert response.status_code == 200, response.json()
        self.attach_response(response.json())
        model = CreateAdminUserModel(**response.json())
        return model

    @allure.step("Get user by ID")
    def get_user_by_id(self, id):
        response = requests.get(
            url=self.endpoints.get_admin_user_by_id(id),
            headers=self.headers.basic,
        )
        print(response.json())
        assert response.status_code == 200, response.json()
        self.attach_response(response.json())
        model = CreateAdminUserModel(**response.json())
        return model


    @allure.step("Create status = Active")
    def create_status_active(self, id):
        response = requests.post(
            url=self.endpoints.create_status(id),
            headers=self.headers.basic,
            params={"block": "Active"}
        )
        response_json = response.json()
        print(response.json())
        assert response_json.get("data") is None
        assert response.status_code == 200, response.json()
        self.attach_response(response.json())
        model = StatusModel(**response.json())
        assert model.message == "Статус успішно змінено."
        return model


    @allure.step("Check status = Active")
    def get_status_active(self, id):
        response = requests.get(
            url=self.endpoints.get_admin_user_by_id(id),
            headers=self.headers.basic,
        )
        print(response.json())
        assert response.status_code == 200, response.json()
        self.attach_response(response.json())
        model = CreateAdminUserModel(**response.json()) 
        assert model.data.status == "Active"
        return model

    @allure.step("Create status = Inactive")
    def create_status_inactive(self, id):
        response = requests.post(
            url=self.endpoints.create_status(id),
            headers=self.headers.basic,
            params={"block": "Inactive"}
        )
        response_json = response.json()
        print(response.json())
        assert response_json.get("data") is None
        assert response.status_code == 200, response.json()
        self.attach_response(response.json())
        model = StatusModel(**response.json())
        assert model.message == "Статус успішно змінено."
        return model

    @allure.step("Check status = Inactive")
    def get_status_inactive(self, id):
        response = requests.get(
            url=self.endpoints.get_admin_user_by_id(id),
            headers=self.headers.basic,
        )
        print(response.json())
        assert response.status_code == 200, response.json()
        self.attach_response(response.json())
        model = CreateAdminUserModel(**response.json())
        assert model.data.status == "Inactive"
        return model

    @allure.step("Create status = NeedChangePassword")
    def create_status_need_change_password(self, id):
        response = requests.post(
            url=self.endpoints.create_status(id),
            headers=self.headers.basic,
            params={"block": "NeedChangePassword"}
        )
        response_json = response.json()
        print(response.json())
        assert response_json.get("data") is None
        assert response.status_code == 200, response.json()
        self.attach_response(response.json())
        model = StatusModel(**response.json())
        assert model.message == "Статус успішно змінено."
        return model

    @allure.step("Check status = NeedChangePassword")
    def get_status_need_change_password(self, id):
        response = requests.get(
            url=self.endpoints.get_admin_user_by_id(id),
            headers=self.headers.basic,
        )
        print(response.json())
        assert response.status_code == 200, response.json()
        self.attach_response(response.json())
        model = CreateAdminUserModel(**response.json())
        assert model.data.status == "NeedChangePassword"
        return model



    @allure.step("Get audit by ID")
    def get_audit_by_id(self, id):
        response = requests.get(
            url=self.endpoints.get_audit(id),
            headers=self.headers.basic,
        )
        print(response.json())
        assert response.status_code == 200, response.json()
        self.attach_response(response.json())
        model = AdminUserAuditModel(**response.json())
        assert model.message == "Аудит користувача успішно отримано."
        assert model.data.totalCount > 0
        assert model.data.items is not None and len(model.data.items) > 0
        return model


    @allure.step("Change password")
    def change_password_from_admin(self, id):
        response = requests.put(
            url=self.endpoints.change_password(id),
            headers=self.headers.basic,
            json=self.payloads.change_password
        )
        print(response.json())
        assert response.status_code == 200, response.json()
        self.attach_response(response.json())
        model = AdminUserPassword(**response.json())
        return model

    @allure.step("Get list of users with filtering and sorting by default")
    def get_users_by_filters_default(self, max_result_count=100, skip_count=0, startdata = None,
                            enddata = None, sort_order="name",
                            filter_data = None, status = None, sort_order_type = None,
                            role_filter = None):
        params = {
            "maxResultCount": max_result_count,
            "skipCount": skip_count,
            "startDate": startdata,
            "endDate": enddata,
            "sortOrder": sort_order,
            "filter": filter_data,
            "status": status,
            "sortOrderType": sort_order_type,
            "roleFilter": role_filter
        }
        response = requests.get(
            url=self.endpoints.get_admin_user,
            headers=self.headers.basic,
            params=params
        )

        print(response.url)
        assert response.status_code == 200, response.json()
        self.attach_response(response.json())
        model = GetAdminUserModel(**response.json())
        return model

    @allure.step("Update user details by ID")
    def update_user_info(self, id):
        response = requests.put(
            url=self.endpoints.change_info_user(id),
            headers=self.headers.basic,
            json=self.payloads.change_info_user_from_admin
        )
        print(response.json())
        assert response.status_code == 200, response.json()
        self.attach_response(response.json())
        model = ChangeAdminUserModel(**response.json())
        return model

    @allure.step("Change role for user")
    def change_role_user(self, id, role_id=2):
        params = {
            "roleId": role_id
        }
        response = requests.put(
            url=self.endpoints.change_role_user(id),
            headers=self.headers.basic,
            params=params
        )
        assert response.status_code == 200
        return
    
    @allure.step("Get user by ID")
    def get_role_user(self, id):
        response = requests.get(
            url=self.endpoints.get_admin_user_by_id(id),
            headers=self.headers.basic,
        )
        print(response.json())
        assert response.status_code == 200, response.json()
        self.attach_response(response.json())
        model = ChangeAdminUserModel(**response.json())
        assert model.data.roles is not None and len(model.data.roles) > 0
        first_role = model.data.roles[0]
        return model



    @allure.step("Update password by ID")
    def update_password(self, id):
        response = requests.put(
            url=self.endpoints.change_password(id),
            headers=self.headers.basic,
            json=self.payloads.change_password
        )
        print(response.json())
        assert response.status_code == 200, response.json()
        self.attach_response(response.json())
        model = AdminUserPassword(**response.json())
        assert model.message == "Пароль успішно змінено."
        return model
    



    