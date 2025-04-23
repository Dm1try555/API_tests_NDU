import allure
import requests
from config.headers import Headers
from utils.helper import Helper
from services.document_receiver.endpoints import Endpoints
from services.document_receiver.payloads import Payloads
from services.document_receiver.models.document_receiver_model import RejectionLetterModel, ConfirmationLetterModel, StatusLetterModel


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
    
    #confirmation letter
    @allure.step("Сreate confirmation letter")
    def create_confirmation_letter(self, key):
        headers = {
            **self.headers.basic,
            "X-API-KEY": key
        }
        response = requests.post(
            url=self.endpoints.confirmation_letter,
            headers=headers,
            json=self.payloads.confirmation_letter
        )
        print(response.json())
        assert response.status_code == 200, response.json()
        self.attach_response(response.json())
        model = ConfirmationLetterModel(**response.json())
        return model
    
    #status letter
    @allure.step("Сreate status letter")
    def create_status_letter(self, key):
        headers = {
            **self.headers.basic,
            "X-API-KEY": key
        }
        response = requests.post(
            url=self.endpoints.status,
            headers=headers,
            json=self.payloads.status
        )
        print(response.json())
        assert response.status_code == 200, response.json()
        self.attach_response(response.json())
        model = StatusLetterModel(**response.json())
        return model


    





  

