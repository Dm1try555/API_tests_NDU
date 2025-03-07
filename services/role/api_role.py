import allure
import requests
from config.headers import Headers
from utils.helper import Helper
from services.role.endpoints import Endpoints
from services.role.payloads import Payloads
from services.role.models.role_model import (CreateRoleModel, GetRoleModel, ChangeRoleModel,
                                             GetRolePermissionsModel)




class RoleAPI(Helper):

    def __init__(self) -> None:
        super().__init__()
        self.endpoints = Endpoints()
        self.headers = Headers()
        self.payloads = Payloads()

    @allure.step("Create new Role")
    def create_role(self):
        response = requests.post(
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
            url=self.endpoints.get_permission_client,
            headers=self.headers.basic,
        )
        print(response.json())
        assert response.status_code == 200, response.json()
        self.attach_response(response.json())
        model = GetRolePermissionsModel(**response.json())
        return model




    # @allure.step("Upload new file")
    # def upload_new_file(self, file_path):
    #     """API File Upload Method"""
    #     with open(file_path, "rb") as file:
    #         files = {"file": (file_path, file, "text/plain")}
    #         response = requests.post(
    #             url=self.endpoints.file_upload,
    #             headers=self.headers.basic,
    #             files=files
    #         )
    #
    #     assert response.status_code == 200, response.json()
    #     self.attach_response(response.json())
    #     model = CreateFileModel(**response.json())
    #     return model
    #
    # @allure.step("Get file by ID")
    # def get_file_by_id(self, id):
    #     """API File Upload Method"""
    #     response = requests.get(
    #         url=self.endpoints.get_file_by_id(id),
    #         headers=self.headers.basic,
    #     )
    #     print(response.url)
    #
    # @allure.step("Delete file by ID")
    # def delete_file_by_id(self, id):
    #     response = requests.delete(
    #         url=self.endpoints.delete_file_by_id(id),
    #         headers=self.headers.basic,
    #     )
    #     print(response.url)
    #     assert response.status_code == 204, response.json()
    #
    # @allure.step("Get file by ID after delete")
    # def get_file_by_id_after_delete(self, id):
    #     response = requests.get(
    #         url=self.endpoints.get_file_by_id(id),
    #         headers=self.headers.basic,
    #     )
    #     print(response.url)
    #     assert response.status_code == 404, response.json()
    #     self.attach_response(response.json())
    #     model = CheckFileAfterDeleteModel(**response.json())
    #     return model