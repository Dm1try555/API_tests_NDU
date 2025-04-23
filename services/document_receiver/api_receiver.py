import allure
import requests
from config.headers import Headers
from utils.helper import Helper
from services.document_receiver.endpoints import Endpoints
from services.document_receiver.payloads import Payloads
from services.document_receiver.models.document_receiver_model import RejectionLetterModel


class DocumentReceiverAPI(Helper):

    def __init__(self) -> None:
        super().__init__()
        self.payloads = Payloads()
        self.endpoints = Endpoints()
        self.headers = Headers()

    #rejection letter
    @allure.step("Create rejection letter")
    def create_rejection_letter(self, key):
        headers = {
            **self.headers.basic,
            "X-API-KEY": key
        }
        response = requests.post(
            url=self.endpoints.rejection_letter,
            headers=headers,
            json=self.payloads.rejection_letter
        )
        print(response.json())
        assert response.status_code == 200, response.json()
        self.attach_response(response.json())
        model = RejectionLetterModel(**response.json())
        return model


    # @allure.step("Copy document by ID")
    # def copy_document_by_id(self, id):
    #     response = requests.put(
    #         url=self.endpoints.copy_document_by_id(id),
    #         headers=self.headers.basic,
    #     )
    #     print(response.json())
    #     assert response.status_code == 200, response.json()
    #     self.attach_response(response.json())
    #     model = CopyDocumentModel(**response.json())
    #     return model

    # @allure.step("Audit document by ID")
    # def audit_document_by_id(self, id):
    #     response = requests.get(
    #         url=self.endpoints.audit_document_by_id(id),
    #         headers=self.headers.basic,
    #     )
    #     print(response.json())
    #     assert response.status_code == 200, response.json()
    #     self.attach_response(response.json())
    #     model = AuditDocumentModel(**response.json())
    #     return model
    





  

