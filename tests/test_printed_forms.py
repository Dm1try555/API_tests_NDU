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

