import allure
import requests
from config.headers import Headers
from utils.helper import Helper
from services.user.endpoints import Endpoints
from services.user.payloads import Payloads
from services.user.models.user_model import GetUserModel, CreateUserModel, StatusModel, UserAuditModel, GetUserIdModel, \
    ChangePasswordModel, ChangeUserIdModel


class UserAPI(Helper):

    def __init__(self) -> None:
        super().__init__()
        self.endpoints = Endpoints()
        self.headers = Headers()
        self.payloads = Payloads()

    @allure.step("Create new User")
    def create_user(self):
        response = requests.post(
            url=self.endpoints.create_user,
            headers=self.headers.basic,
            json=self.payloads.create_user
        )
        print(response.json())
        assert response.status_code == 200, response.json()
        self.attach_response(response.json())
        model = CreateUserModel(**response.json())
        return model


    @allure.step("Get User by ID")
    def get_user_by_id(self, id):
        response = requests.get(
            url=self.endpoints.get_user_by_id(id),
            headers=self.headers.basic,
        )
        print(response.json())
        assert response.status_code == 200, response.json()
        self.attach_response(response.json())
        model = GetUserIdModel(**response.json())
        return model




    @allure.step("Create status = Active")
    def create_status_active(self, id):
        response = requests.post(
            url=self.endpoints.change_status(id),
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
            url=self.endpoints.get_user_by_id(id),
            headers=self.headers.basic,
        )
        print(response.json())
        assert response.status_code == 200, response.json()
        self.attach_response(response.json())
        model = GetUserIdModel(**response.json())
        assert model.data.status == "Active"
        return model

    @allure.step("Create status = Inactive")
    def create_status_inactive(self, id):
        response = requests.post(
            url=self.endpoints.change_status(id),
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
            url=self.endpoints.get_user_by_id(id),
            headers=self.headers.basic,
        )
        print(response.json())
        assert response.status_code == 200, response.json()
        self.attach_response(response.json())
        model = GetUserIdModel(**response.json())
        assert model.data.status == "Inactive"
        return model

    @allure.step("Create status = NeedChangePassword")
    def create_status_need_change_password(self, id):
        response = requests.post(
            url=self.endpoints.change_status(id),
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
            url=self.endpoints.get_user_by_id(id),
            headers=self.headers.basic,
        )
        print(response.json())
        assert response.status_code == 200, response.json()
        self.attach_response(response.json())
        model = GetUserIdModel(**response.json())
        assert model.data.status == "NeedChangePassword"
        return model

    @allure.step("Create status = Blocked")
    def create_status_blocked(self, id):
        response = requests.post(
            url=self.endpoints.change_status(id),
            headers=self.headers.basic,
            params={"block": "Blocked"}
        )
        response_json = response.json()
        print(response.json())
        assert response_json.get("data") is None
        assert response.status_code == 200, response.json()
        self.attach_response(response.json())
        model = StatusModel(**response.json())
        assert model.message == "Статус успішно змінено."
        return model

    @allure.step("Check status = Blocked")
    def get_status_blocked(self, id):
        response = requests.get(
            url=self.endpoints.get_user_by_id(id),
            headers=self.headers.basic,
        )
        print(response.json())
        assert response.status_code == 200, response.json()
        self.attach_response(response.json())
        model = GetUserIdModel(**response.json())
        assert model.data.status == "Blocked"
        return model

    @allure.step("Get User Audit by ID")
    def get_user_audit_by_id(self, id):
        response = requests.get(
            url=self.endpoints.get_audit_by_id(id),
            headers=self.headers.basic,
        )
        print(response.json())
        assert response.status_code == 200, response.json()
        self.attach_response(response.json())
        model = UserAuditModel(**response.json())
        return model


    @allure.step("Change User Role by ID")
    def change_role_by_id(self, id):
        response = requests.put(
            url=self.endpoints.change_role_by_id(id),
            headers=self.headers.basic,
            params={"roleId": 2}
        )
        print(response.url)
        assert response.status_code == 200
        self.attach_response(response.url)
        return

    @allure.step("Change User Password by ID")
    def change_password_by_id(self, id):
        print(self.payloads.change_password)
        response = requests.put(
            url=self.endpoints.change_password_by_id(id),
            headers=self.headers.basic,
            json=self.payloads.change_password
        )
        print(response.url)
        print(response.json())
        assert response.status_code == 200, response.json()
        self.attach_response(response.json())
        model = ChangePasswordModel(**response.json())
        return model



    @allure.step("Change User Info by ID")
    def change_user_info_by_id(self, id):
        response = requests.put(
            url=self.endpoints.change_user_by_id(id),
            headers=self.headers.basic,
            json=self.payloads.change_info_user
        )
        print(response.url)
        print(response.json())
        assert response.status_code == 200, response.json()
        self.attach_response(response.json())
        model = ChangeUserIdModel(**response.json())
        return model

    @allure.step("Get Users list by default filters")
    def get_users_by_default_filters(self, max_result_count=None, skip_count=None, sort_order=None,
                                        sort_order_type=None, start_date = None, end_date = None,
                                        filter_data=None, role_filter=None, status_data=None):
        params = {
            "maxResultCount": max_result_count,
            "skipCount": skip_count,
            "startDate": start_date,
            "endDate": end_date,
            "sortOrder": sort_order,
            "filter": filter_data,
            "status": status_data,
            "sortOrderType": sort_order_type,
            "roleFilter": role_filter
        }
        response = requests.get(
            url=self.endpoints.get_user,
            headers=self.headers.basic,
            params=params
        )
        print(response.url)
        print(response.json())
        assert response.status_code == 200, response.json()
        self.attach_response(response.json())
        model = GetUserModel(**response.json())
        return model


