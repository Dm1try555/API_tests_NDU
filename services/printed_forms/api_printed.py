import allure
import requests
from config.headers import Headers
from utils.helper import Helper
from services.printed_forms.endpoints import Endpoints
from services.printed_forms.payloads import Payloads
from services.printed_forms.models.printed_forms_model import PrintedFormsModel, PlaceholderModel
import os

class PrintedFormsAPI(Helper):

    def __init__(self) -> None:
        super().__init__()
        self.endpoints = Endpoints()
        self.headers = Headers()
        self.payloads = Payloads()

    

    @allure.step("Get Printed Forms by default filters")
    def get_printed_forms(self, max_result_count=None, 
                          skip_count=None, 
                          sort_order=None,
                          sort_order_type=None):
        
        params = {
            "maxResultCount": max_result_count,
            "skipCount": skip_count,
            "sortOrder": sort_order,
            "sortOrderType": sort_order_type,
        }
        response = requests.get(
            url=self.endpoints.get_printed_forms,
            headers=self.headers.basic,
            params=params
        )
        print(response.url)
        print(response.json())
        assert response.status_code == 200, response.json()
        self.attach_response(response.json())
        model = PrintedFormsModel(**response.json())
        return model



    @allure.step("Get Printed Forms by type")
    def get_printed_forms_by_type(self, type_id):
        response = requests.get(
            url=self.endpoints.get_printed_forms_type(type_id),
            headers=self.headers.basic,
        )
        print(response.url)
        assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
        assert "application/vnd.openxmlformats-officedocument.wordprocessingml.document" in response.headers.get("content-type", ""), \
            f"Unexpected content-type: {response.headers.get('content-type')}"        

        filename = self._extract_filename(response.headers.get("content-disposition", ""))
        if filename:
            with open(filename, "wb") as f:
                f.write(response.content)
            self._attach_file(response.content, filename)
            os.remove(filename)
        else:
            default_filename = "printed_form.docx"
            with open(default_filename, "wb") as f:
                f.write(response.content)
            self._attach_file(response.content, default_filename)
            os.remove(default_filename)

        return response 


    def _extract_filename(self, content_disposition):
        import re
        match = re.search(r'filename\*?=(?:UTF-8\'\')?"?([^";]+)"?', content_disposition)
        if match:
            from urllib.parse import unquote
            return unquote(match.group(1))
        return None

    def _attach_file(self, content, name):
        allure.attach(content, name=name)




    @allure.step("Get Placeholder")
    def get_placeholder(self):
        response = requests.get(
            url=self.endpoints.get_printed_forms_placeholder,
            headers=self.headers.basic,
        )
        print(response.url)
        print(response.json())
        assert response.status_code == 200, response.json()
        self.attach_response(response.json())
        model = PlaceholderModel(**response.json())
        return model




    # @allure.step("Create new User")
    # def create_user(self):
    #     response = requests.post(
    #         url=self.endpoints.create_user,
    #         headers=self.headers.basic,
    #         json=self.payloads.create_user
    #     )
    #     print(response.json())
    #     assert response.status_code == 200, response.json()
    #     self.attach_response(response.json())
    #     model = CreateUserModel(**response.json())
    #     return model

    # @allure.step("Get Users list by default filters")
    # def get_users_by_default_filters(self, max_result_count=None, skip_count=None, sort_order=None,
    #                                     sort_order_type=None, start_date = None, end_date = None,
    #                                     filter_data=None, role_filter=None, status_data=None):
    #     params = {
    #         "maxResultCount": max_result_count,
    #         "skipCount": skip_count,
    #         "startDate": start_date,
    #         "endDate": end_date,
    #         "sortOrder": sort_order,
    #         "filter": filter_data,
    #         "status": status_data,
    #         "sortOrderType": sort_order_type,
    #         "roleFilter": role_filter
    #     }
    #     response = requests.get(
    #         url=self.endpoints.get_user,
    #         headers=self.headers.basic,
    #         params=params
    #     )
    #     print(response.url)
    #     print(response.json())
    #     assert response.status_code == 200, response.json()
    #     self.attach_response(response.json())
    #     model = GetUserModel(**response.json())
    #     return model


