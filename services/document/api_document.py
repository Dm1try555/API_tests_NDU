# import allure
# import requests
# from config.headers import Headers
# from utils.helper import Helper
# from services.admin_user.endpoints import Endpoints
# from services.admin_user.payloads import Payloads
# from services.admin_user.models.adminuser_model import AdminUserModel, AdminUserAuditModel, AdminUserPassword
#
#
# class AdminUserAPI(Helper):
#
#     def __init__(self) -> None:
#         super().__init__()
#         self.payloads = Payloads()
#         self.endpoints = Endpoints()
#         self.headers = Headers()
#
#
#     @allure.step("Create new user from admin portal")
#     def create_user_from_admin(self):
#         response = requests.post(
#             url=self.endpoints.create_admin_user,
#             headers=self.headers.basic,
#             json=self.payloads.create_user_from_admin
#         )
#         print(response.json())
#         assert response.status_code == 200, response.json()
#         self.attach_response(response.json())
#         model = AdminUserModel(**response.json()["data"])  # Проверка, что респонс соответствует модели
#         return model
#
#     @allure.step("Get user by ID")
#     def get_user_by_id(self, id):
#         response = requests.get(
#             url=self.endpoints.get_admin_user_by_id(id),
#             headers=self.headers.basic,
#         )
#         print(response.json())
#         assert response.status_code == 200, response.json()
#         self.attach_response(response.json())
#         model = AdminUserModel(**response.json()["data"])
#         return model
#
#
