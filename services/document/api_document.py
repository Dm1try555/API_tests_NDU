import allure
import requests
from config.headers import Headers
from utils.helper import Helper
from services.document.endpoints import Endpoints
from services.document.payloads import Payloads
from services.document.models.document_model import CreateDocumentModel, DeleteDocumentModel, CheckDeleteDocumentModel, \
    CopyDocumentModel, AuditDocumentModel, GetDocumentModel, UploadDocumentModel, ChangeDocumentModel


class DocumentAPI(Helper):

    def __init__(self) -> None:
        super().__init__()
        self.payloads = Payloads()
        self.endpoints = Endpoints()
        self.headers = Headers()

    #Category110
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
    

    @allure.step("Upload file document by ID")
    def upload_document_by_id(self, id:int, file_path:str):
        with open(file_path, 'rb') as f:
            files = {
                'file': (file_path.split('/')[-1], f, 'application/vnd.openxmlformats-officedocument.wordprocessingml.document')
            }
            response = requests.post(
                url=self.endpoints.upload_document_by_id(id),
                headers=self.headers.basic,
                files=files,
            )
        print(response.json())
        assert response.status_code == 200, response.json()
        self.attach_response(response.json())
        model = UploadDocumentModel(**response.json())
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

    @allure.step("Get document list by default filters")
    def get_document_by_default_filters(self, max_result_count=None, skip_count=None, sort_order=None,
                                        sort_order_type= None, document_direction_type=None,
                                        filter_data=None, filter_edrpou=None, filter_llc_name=None,
                                        filter_number=None, filter_username=None, start_cr_date=None,
                                        end_cr_date=None, start_upd_date=None, end_upd_date=None,
                                        status=None, doc_type = None):
        params = {
            "maxResultCount": max_result_count,
            "skipCount": skip_count,
            "sortOrder": sort_order,
            "sortOrderType": sort_order_type,
            "documentDirectionType": document_direction_type,
            "filter": filter_data,
            "filterByLLCEDRPOU": filter_edrpou,
            "filterByLLCName": filter_llc_name,
            "filterByUserIdentityNumber": filter_number,
            "filterByUserName": filter_username,
            "startCreatedDate": start_cr_date,
            "endCreatedDate": end_cr_date,
            "startUpdatedDate": start_upd_date,
            "endUpdatedDate": end_upd_date,
            "documentStatus": status,
            "documentType": doc_type
        }
        response = requests.get(
            url=self.endpoints.get_document,
            headers=self.headers.basic,
            params=params
        )
        print(response.url)
        # print(response.json())
        assert response.status_code == 200, response.json()
        self.attach_response(response.json())
        model = GetDocumentModel(**response.json())
        return model


    @allure.step("Get printed form by ID")
    def get_printed_form_by_id(self, id):
        response = requests.get(
            url=self.endpoints.get_printed_document_by_id(id),
            headers=self.headers.basic,
        )
        print(response.url)
        assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
        assert response.headers.get("accept-ranges") == "bytes", f"Unexpected accept-ranges: {response.headers.get('accept-ranges')}"
        assert response.headers. get("content-disposition") == "inline", f"Unexpected content-disposition: {response.headers.get('content-disposition')}"
        assert response.headers.get("content-type") == "application/pdf", f"Unexpected content-type: {response.headers.get('content-type')}"
        assert response.headers.get("server") == "openresty", f"Unexpected server: {response.headers.get('server')}"
        assert response.headers.get("strict-transport-security") == "max-age=63072000; preload", f"Unexpected strict-transport-security: {response.headers.get('strict-transport-security')}"
        assert response.headers.get("x-served-by") == "llc-cabinet-api-mwt.csd.ua", f"Unexpected x-served-by: {response.headers.get('x-served-by')}"
        self.attach_response(response.url)
        return response
    
    

    @allure.step("Change document by ID")
    def change_document(self, id):
        response = requests.put(
            url=self.endpoints.change_document_by_id(id),
            headers=self.headers.basic,
            json=self.payloads.change_document_by_id
        )
        print(response.json())
        assert response.status_code == 200, response.json()
        self.attach_response(response.json())
        model = ChangeDocumentModel(**response.json())
        return model