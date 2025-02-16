import allure
import requests
from config.headers import Headers
from utils.helper import Helper
from services.collections.endpoints import Endpoints
from services.collections.models.collections_model import CollectionsModel


class CollectionsAPI(Helper):

    def __init__(self) -> None:
        super().__init__()
        self.endpoints = Endpoints()
        self.headers = Headers()



    @allure.step("Get collections")
    def get_collections(self):
        response = requests.get(
            url=self.endpoints.get_collections,
            headers=self.headers.basic,
        )
        print(response.json())
        assert response.status_code == 200, response.json()
        self.attach_response(response.json())
        model = CollectionsModel(**response.json())
        return model









