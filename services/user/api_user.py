import allure
import requests
from config.headers import Headers
from utils.helper import Helper
from services.user.endpoints import Endpoints
from services.user.payloads import Payloads
from services.user.models.user_model import GetUserModel, CreateUserModel, StatusModel, UserAuditModel, GetUserIdModel




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





    # @allure.step("Change Role by ID")
    # def change_role_by_id(self, id):
    #     response = requests.put(
    #         url=self.endpoints.change_role_by_id(id),
    #         headers=self.headers.basic,
    #         json=self.payloads.change_role
    #     )
    #     print(response.json())
    #     assert response.status_code == 200, response.json()
    #     self.attach_response(response.json())
    #     model = ChangeRoleModel(**response.json())
    #     return model
    #
    # @allure.step("Get all Role permissions")
    # def get_role_permissions(self):
    #     response = requests.get(
    #         url=self.endpoints.get_permission,
    #         headers=self.headers.basic,
    #     )
    #     print(response.json())
    #     assert response.status_code == 200, response.json()
    #     self.attach_response(response.json())
    #     model = GetRolePermissionsModel(**response.json())
    #     return model
    #
    # @allure.step("Get admin Role permissions")
    # def get_admin_role_permissions(self):
    #     response = requests.get(
    #         url=self.endpoints.get_permission_admin,
    #         headers=self.headers.basic,
    #     )
    #     print(response.json())
    #     assert response.status_code == 200, response.json()
    #     self.attach_response(response.json())
    #     model = GetRolePermissionsModel(**response.json())
    #     return model
    #
    # @allure.step("Get client Role permissions")
    # def get_client_role_permissions(self):
    #     response = requests.get(
    #         url=self.endpoints.get_permission_client,
    #         headers=self.headers.basic,
    #     )
    #     print(response.json())
    #     assert response.status_code == 200, response.json()
    #     self.attach_response(response.json())
    #     model = GetRolePermissionsModel(**response.json())
    #     return model
    #
    #
    # @allure.step("Get list of roles")
    # def get_role_by_filters(self, max_result_count=100, skip_count=0, sort_order="name",
    #                                 filter_string=None, sort_order_type="Ascending", is_admin_part=True):
    #     params = {
    #         "maxResultCount": max_result_count,
    #         "skipCount": skip_count,
    #         "sortOrder": sort_order,
    #         "sortOrderType": sort_order_type,
    #         "isAdminPart": str(is_admin_part).lower(),
    #         "filter_string": filter_string
    #     }
    #     response = requests.get(
    #         url=self.endpoints.get_role,
    #         headers=self.headers.basic,
    #         params=params
    #     )
    #
    #     print(response.url)
    #     print(response.json())
    #     assert response.status_code == 200, response.json()
    #     self.attach_response(response.json())
    #
    #     model = GetRoleFiltersModel(**response.json())
    #     return model
