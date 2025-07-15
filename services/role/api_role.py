import allure
import requests
from config.headers import Headers
from utils.helper import Helper
from services.role.endpoints import Endpoints
from services.role.payloads import Payloads
from services.role.models.role_model import (CreateRoleModel, GetRoleModel, ChangeRoleModel,
                                            GetRolePermissionsModel, GetRoleFiltersModel)




class RoleAPI(Helper):

    def __init__(self) -> None:
        super().__init__()
        self.endpoints = Endpoints()
        self.headers = Headers()
        self.payloads = Payloads()

    @allure.step("Create new Role")
    def create_role(self):
        response = requests.post(
            timeout=10,
            url=self.endpoints.create_role,
            headers=self.headers.basic,
            json=self.payloads.create_new_role
        )
        print(response.json())
        assert response.status_code == 200, response.json()
        self.attach_response(response.json())
        model = CreateRoleModel(**response.json())
        expected_role_name = self.payloads.create_new_role["role"]["name"]
        assert model.message == f"Роль {expected_role_name} успішно створено."
        return model


    @allure.step("Get Role by ID")
    def get_role_by_id(self, id):
        response = requests.get(
            timeout=10,
            url=self.endpoints.get_role_by_id(id),
            headers=self.headers.basic,
        )
        print(response.json())
        assert response.status_code == 200, response.json()
        self.attach_response(response.json())
        model = GetRoleModel(**response.json())
        return model


    @allure.step("Change Role by ID")
    def change_role_by_id(self, id):
        response = requests.put(
            timeout=10,
            url=self.endpoints.change_role_by_id(id),
            headers=self.headers.basic,
            json=self.payloads.change_role
        )
        print(response.json())
        assert response.status_code == 200, response.json()
        self.attach_response(response.json())
        model = ChangeRoleModel(**response.json())
        return model

    @allure.step("Get all Role permissions")
    def get_role_permissions(self):
        response = requests.get(
            timeout=10,
            url=self.endpoints.get_permission,
            headers=self.headers.basic,
        )
        print(response.json())
        assert response.status_code == 200, response.json()
        self.attach_response(response.json())
        model = GetRolePermissionsModel(**response.json())
        return model

    @allure.step("Get admin Role permissions")
    def get_admin_role_permissions(self):
        response = requests.get(
            timeout=10,
            url=self.endpoints.get_permission_admin,
            headers=self.headers.basic,
        )
        print(response.json())
        assert response.status_code == 200, response.json()
        self.attach_response(response.json())
        model = GetRolePermissionsModel(**response.json())
        return model

    @allure.step("Get client Role permissions")
    def get_client_role_permissions(self):
        response = requests.get(
            timeout=10,
            url=self.endpoints.get_permission_client,
            headers=self.headers.basic,
        )
        print(response.json())
        assert response.status_code == 200, response.json()
        self.attach_response(response.json())
        model = GetRolePermissionsModel(**response.json())
        return model


    @allure.step("Get list of roles")
    def get_role_by_filters(self, max_result_count=100, skip_count=0, sort_order="name",
                                    filter_string=None, sort_order_type="Ascending", is_admin_part=True):
        params = {
            "maxResultCount": max_result_count,
            "skipCount": skip_count,
            "sortOrder": sort_order,
            "sortOrderType": sort_order_type,
            "isAdminPart": str(is_admin_part).lower(),
        }
        headers = self.headers.basic.copy()
        headers["Connection"] = "close"
        response = requests.get(
            timeout=10,
            url=self.endpoints.get_role,
            headers=self.headers.basic,
            params=params
        )

        print(response.url)
        print(response.json())
        assert response.status_code == 200, response.json()
        self.attach_response(response.json())

        model = GetRoleFiltersModel(**response.json())
        return model
