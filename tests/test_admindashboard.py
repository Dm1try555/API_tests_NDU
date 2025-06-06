import allure
import pytest
from services.admin_dashboard.api_admindashboard import AdminDashboardAPI


@allure.epic("Admin Dashboard")
@allure.feature("Admin Dashboard")
class TestAdminDashboard:

    @classmethod
    def setup_class(cls):
        cls.api_admin_dashboard = AdminDashboardAPI()

    @allure.title("Get admin dashboard")
    def test_admin_dashboard(self):
        model = self.api_admin_dashboard.get_admin_dashboard()
        assert model.totalUsersCount and model.activeUsersCount and model.totalSizeOfFiles is not None, "Admin dashboard data is empty"







