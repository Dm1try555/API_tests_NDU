import allure
import requests
from config.headers import Headers
from utils.helper import Helper
from services.document.endpoints import Endpoints
from services.document.payloads import Payloads
from services.document.models.document_model import CreateDocumentModel, GetDocumentModel


class DocumentAPI(Helper):

    def __init__(self) -> None:
        super().__init__()
        self.payloads = Payloads()
        self.endpoints = Endpoints()
        self.headers = Headers()


    @allure.step("Create new document")
    def create_new_document(self):
        response = requests.post(
            url=self.endpoints.create_document,
            headers=self.headers.basic,
            json=self.payloads.create_new_document
        )
        print(response.json())
        assert response.status_code == 200, response.json()
        self.attach_response(response.json())
        model = CreateDocumentModel(**response.json())
        return model

    # @allure.step("Get user by ID")
    # def get_user_by_id(self, id):
    #     response = requests.get(
    #         url=self.endpoints.get_admin_user_by_id(id),
    #         headers=self.headers.basic,
    #     )
    #     print(response.json())
    #     assert response.status_code == 200, response.json()
    #     self.attach_response(response.json())
    #     model = AdminUserModel(**response.json()["data"])
    #     return model


