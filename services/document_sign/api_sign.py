import allure
import requests
from config.headers import Headers
from utils.helper import Helper
from services.document_sign.endpoints import Endpoints
from services.document_sign.payloads import Payloads
from services.document_sign.models.sign_model import GetDocumentSignModel



class DocumentSignAPI(Helper):

    def __init__(self) -> None:
        super().__init__()
        self.payloads = Payloads()
        self.endpoints = Endpoints()
        self.headers = Headers()


    @allure.step("Get file to sign document")
    def get_document_sign(self, id):
        headers = {
            **self.headers.basic
        }
        response = requests.get(
            url=self.endpoints.get_sign_document(id),
            headers=headers,
        )
        print(response.json())
        assert response.status_code == 200, response.json()
        self.attach_response(response.json())
        model = GetDocumentSignModel(**response.json())
        return model
    
    

    





  

