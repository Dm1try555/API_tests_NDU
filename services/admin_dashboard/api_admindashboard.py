import allure
import requests
from config.headers import Headers
from utils.helper import Helper
from services.admin_dashboard.endpoints import Endpoints
from services.admin_dashboard.models.admindashboard_model import GetAdminDashboardModel

class AdminDashboardAPI(Helper):

    def __init__(self) -> None:
        super().__init__()
        self.endpoints = Endpoints()
        self.headers = Headers()


    @allure.step("Get admin dashboard")
    def get_admin_dashboard(self):
        response = requests.get(
            url=self.endpoints.get_admin_dashboard,
            headers=self.headers.basic,
        )
        print(response.json())
        assert response.status_code == 200, response.json()
        self.attach_response(response.json())
        model = GetAdminDashboardModel(**response.json())
        return model
