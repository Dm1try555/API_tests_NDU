import allure
from services.printed_forms.api_printed import PrintedFormsAPI


@allure.epic("Printed Forms")
@allure.feature("Printed Forms")
class TestPrintedForms:
    


    @classmethod
    def setup_class(cls):
        cls.api_printed_forms = PrintedFormsAPI()




    @allure.title("Get Printed Forms by default filters")
    def test_get_printed_forms(self):
        model = self.api_printed_forms.get_printed_forms()
        assert model.message == "Документи отримано."
        assert model.data is not None, "Printed Forms data is None"
        assert model.data.items is not None, "Printed Forms items are None"
        assert len(model.data.items) > 0, "No printed forms found in response"

  



    @allure.title("Get Placeholder")
    def test_get_placeholder(self):
        model = self.api_printed_forms.get_placeholder()
        assert model.message == "Успішно отримано"
        assert model.data is not None, "Placeholder data is None"


    @allure.title("Get Printed Forms by type")
    def test_get_printed_forms_by_type(self):

        dodatok_9 = self.api_printed_forms.get_printed_forms_by_type("ConsentForPersonalDataProcessing")
        assert "dodatok-9" in dodatok_9.headers.get("content-disposition", ""), "Filename for ConsentForPersonalDataProcessing is incorrect"

        dodatok_14 = self.api_printed_forms.get_printed_forms_by_type("QuestionnaireFormAnnex14")
        assert "dodatok-14" in dodatok_14.headers.get("content-disposition", ""), "Filename for QuestionnaireFormAnnex14 is incorrect"

        dodatok_21 = self.api_printed_forms.get_printed_forms_by_type("QuestionnaireFormAnnex21")
        assert "dodatok-21" in dodatok_21.headers.get("content-disposition", ""), "Filename for QuestionnaireFormAnnex21 is incorrect"

        dodatok_22 = self.api_printed_forms.get_printed_forms_by_type("QuestionnaireForm")
        assert "dodatok-22" in dodatok_22.headers.get("content-disposition", ""), "Filename for QuestionnaireForm is incorrect"
        
        dodatok_23 = self.api_printed_forms.get_printed_forms_by_type("AccountOpeningOrder")
        assert "dodatok-23" in dodatok_23.headers.get("content-disposition", ""), "Filename for AccountOpeningOrder is incorrect"

        dodatok_24 = self.api_printed_forms.get_printed_forms_by_type("AccountProfileStateCommunity")
        assert "dodatok-24" in dodatok_24.headers.get("content-disposition", ""), "Filename for AccountProfileStateCommunity is incorrect"

        dodatok_27 = self.api_printed_forms.get_printed_forms_by_type("AccountProfileLegalResident")
        assert "dodatok-27" in dodatok_27.headers.get("content-disposition", ""), "Filename for AccountProfileLegalResident is incorrect"

        dodatok_28 = self.api_printed_forms.get_printed_forms_by_type("AccountProfileIndividual")
        assert "dodatok-28" in dodatok_28.headers.get("content-disposition", ""), "Filename for AccountProfileIndividual is incorrect"

        dodatok_30 = self.api_printed_forms.get_printed_forms_by_type("AccountProfileLegalNonResident")
        assert "dodatok-30" in dodatok_30.headers.get("content-disposition", ""), "Filename for AccountProfileLegalNonResident is incorrect"




    # @allure.title("Change User Info by ID")
    # def test_change_user_info(self):
    #     value = Payloads.change_info_user
    #     model = self.api_user.change_user_info_by_id(self.__class__.user_id)
    #     assert model.message == "Користувача успішно оновлено."
    #     assert model.data is not None, "User data is None"
    #     assert model.data.id == self.__class__.user_id, "The ID in the response does not match the expected one"
    #     assert model.data.firstName == value["firstName"], "First name does not match"
    #     assert model.data.middleName == value["middleName"], "Middle name does not match"
    #     assert model.data.lastName == value["lastName"], "Last name does not match"
    #     assert model.data.identityNumber == value["identityNumber"], "Identity number does not match"
    #     assert model.data.login == value["login"], "Login does not match"

    # @allure.title("Check User Info by ID after change")
    # def test_get_user_info_by_id(self):
    #     model = self.api_user.get_user_by_id(self.__class__.user_id)
    #     assert model.message == "Користувача успішно отримано."
    #     assert model.data is not None, "User data is None"
    #     assert model.data.id == self.__class__.user_id, "The ID in the response does not match the expected one"
    #     assert model.data.firstName == Payloads.change_info_user["firstName"], "First name does not match"
    #     assert model.data.middleName == Payloads.change_info_user["middleName"], "Middle name does not match"
    #     assert model.data.lastName == Payloads.change_info_user["lastName"], "Last name does not match"
    #     assert model.data.identityNumber == Payloads.change_info_user["identityNumber"], "Identity number does not match"
    #     assert model.data.login == Payloads.change_info_user["login"], "Login does not match"
        


    # @allure.title("Get Users list by filters")
    # def test_get_users_list(self):
    #     model = self.api_user.get_users_by_default_filters()
    #     assert model.message == "Дані успішно отримано."