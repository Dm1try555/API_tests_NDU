import allure
import requests
from config.headers import Headers
from utils.helper import Helper
from services.counteragent.endpoints import Endpoints
from services.counteragent.models.counteragent_model import GetUserModel, CounterAgentModel


class CounterAgentAPI(Helper):

    def __init__(self) -> None:
        super().__init__()
        self.endpoints = Endpoints()
        self.headers = Headers()


    @allure.step("Get user list")
    def get_user_list(self):
        response = requests.get(
            url=self.endpoints.get_user,
            headers=self.headers.basic
        )
        # print(response.json())
        assert response.status_code == 200, response.json()
        self.attach_response(response.json())
        model = GetUserModel(**response.json())
        return model


    @allure.step("Get counter agent by identity number")
    def get_counter_agent_by_id(self, identity_number = None):
        params = {
            "identityNumber": identity_number
        }
        response = requests.get(
            url=self.endpoints.get_counteragent,
            headers=self.headers.basic,
            params=params
        )
        print(response.url)
        assert response.status_code == 200, response.json()
        self.attach_response(response.json())
        model = CounterAgentModel(**response.json())
        return model









