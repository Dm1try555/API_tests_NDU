import allure
import requests
from config.headers import Headers
from utils.helper import Helper
from services.kep.endpoints import Endpoints
from services.kep.payloads import Payloads
from services.kep.models.kep_model import KepVerifyModel, GetKepGenerateModel

class KepAPI(Helper):

    def __init__(self) -> None:
        super().__init__()
        self.endpoints = Endpoints()
        self.headers = Headers()
        self.payloads = Payloads()

    @allure.step("Create KEP verify")
    def create_kep_verify(self):
        response = requests.post(
            url=self.endpoints.create_kep_verify,
            headers=self.headers.basic,
            json=self.payloads.create_kep_verify
        )
        print(response.json())
        assert response.status_code == 200, response.json()
        self.attach_response(response.json())
        model = KepVerifyModel(**response.json())
        return model

    @allure.step("Create KEP verify hash")
    def create_kep_verify_hash(self):
        response = requests.post(
            url=self.endpoints.create_kep_verify_hash,
            headers=self.headers.basic,
            json=self.payloads.create_kep_verify
        )
        print(response.json())
        assert response.status_code == 200, response.json()
        self.attach_response(response.json())
        model = KepVerifyModel(**response.json())
        return model


    @allure.step("Create KEP generate hash")
    def create_kep_generate_hash(self):
        response = requests.post(
            url=self.endpoints.create_kep_generate_hash,
            headers=self.headers.basic,
            json=self.payloads.create_kep_generate_hash
        )
        print(response.text)
        assert response.status_code == 200, response.json()
        assert response.text is not None

    @allure.step("Get KEP generate")
    def get_kep_generate(self):
        response = requests.get(
            url=self.endpoints.get_kep_generate,
            headers=self.headers.basic,
        )
        print(response.json())
        assert response.status_code == 200, response.json()
        self.attach_response(response.json())
        model = GetKepGenerateModel(**response.json())
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