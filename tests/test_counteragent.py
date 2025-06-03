import allure
import pytest
from services.counteragent.api_counteragent import CounterAgentAPI


@allure.epic("CounterAgent")
@allure.feature("CounterAgent")
class TestCounterAgent:

    @classmethod
    def setup_class(cls):
        cls.api_counteragent = CounterAgentAPI()

    @pytest.fixture(scope="class")
    @allure.title("Get identity number from user list")
    def get_identity_number(self):
        user = self.api_counteragent.get_user_list()
        first_user = user.data.items[0]
        identity_number = first_user.identityNumber  # get identityNumber first user
        print(f"Received number: {identity_number}")
        return identity_number

    @allure.title("Get counter agent by identity number")
    def test_counter_agent(self, get_identity_number):
        identity_number = get_identity_number
        model = self.api_counteragent.get_counter_agent_by_id(identity_number=identity_number)
        print(model)
        assert get_identity_number == model.data[0].identityNumber
        assert model.message == "Успішно отримано."







