import allure
import requests
from config.headers import Headers
from utils.helper import Helper
from services.document.endpoints import Endpoints
from services.document.payloads import Payloads
from services.document.models.document_model import CreateDocumentModel, DeleteDocumentModel, CheckDeleteDocumentModel, \
    CopyDocumentModel, AuditDocumentModel #GetDocumentModel


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

    @allure.step("Get document by ID")
    def get_document_by_id(self, id):
        response = requests.get(
            url=self.endpoints.get_document_by_id(id),
            headers=self.headers.basic,
        )
        print(response.json())
        assert response.status_code == 200, response.json()
        self.attach_response(response.json())
        model = CreateDocumentModel(**response.json())
        return model

    @allure.step("Copy document by ID")
    def copy_document_by_id(self, id):
        response = requests.put(
            url=self.endpoints.copy_document_by_id(id),
            headers=self.headers.basic,
        )
        print(response.json())
        assert response.status_code == 200, response.json()
        self.attach_response(response.json())
        model = CopyDocumentModel(**response.json())
        return model

    @allure.step("Audit document by ID")
    def audit_document_by_id(self, id):
        response = requests.get(
            url=self.endpoints.audit_document_by_id(id),
            headers=self.headers.basic,
        )
        print(response.json())
        assert response.status_code == 200, response.json()
        self.attach_response(response.json())
        model = AuditDocumentModel(**response.json())
        return model

    @allure.step("Delete document by ID")
    def delete_document_by_id(self, id):
        response = requests.delete(
            url=self.endpoints.delete_document_by_id(id),
            headers=self.headers.basic,
        )
        print(response.json())
        assert response.status_code == 200, response.json()
        self.attach_response(response.json())
        model = DeleteDocumentModel(**response.json())
        return model

    @allure.step("Check document by ID after delete")
    def get_document_by_id_after_delete(self, id):
        response = requests.get(
            url=self.endpoints.get_document_by_id(id),
            headers=self.headers.basic,
        )
        print(response.json())
        assert response.status_code == 404, response.json()
        self.attach_response(response.json())
        model = CheckDeleteDocumentModel(**response.json())
        return model


