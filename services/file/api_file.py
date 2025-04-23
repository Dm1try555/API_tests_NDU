import allure
import pytest
import requests
from config.headers import Headers
from utils.helper import Helper
from services.file.endpoints import Endpoints
from services.file.models.file_model import CreateFileModel, CheckFileAfterDeleteModel

class FileAPI(Helper):

    def __init__(self) -> None:
        super().__init__()
        self.endpoints = Endpoints()
        self.headers = Headers()

    @allure.step("Upload new file")
    def upload_new_file(self, file_path):
        
        with open(file_path, "rb") as file:
            files = {"file": (file_path, file, "text/plain")}
            response = requests.post(
                url=self.endpoints.file_upload,
                headers=self.headers.basic,
                files=files
            )

        assert response.status_code == 200, response.json()
        self.attach_response(response.json())
        model = CreateFileModel(**response.json())
        return model

    @allure.step("Get file by ID")
    def get_file_by_id(self, id):
        response = requests.get(
            url=self.endpoints.get_file_by_id(id),
            headers=self.headers.basic,
        )
        print(response.url)

    @allure.step("Delete file by ID")
    def delete_file_by_id(self, id):
        response = requests.delete(
            url=self.endpoints.delete_file_by_id(id),
            headers=self.headers.basic,
        )
        print(response.url)
        assert response.status_code == 204, response.json()

    @allure.step("Get file by ID after delete")
    def get_file_by_id_after_delete(self, id):
        response = requests.get(
            url=self.endpoints.get_file_by_id(id),
            headers=self.headers.basic,
        )
        print(response.url)
        assert response.status_code == 404, response.json()
        self.attach_response(response.json())
        model = CheckFileAfterDeleteModel(**response.json())
        return model