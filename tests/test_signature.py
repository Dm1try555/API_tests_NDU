import allure
from services.signature.api_signature import SignatureAPI
from services.signature.payloads import Payloads


@allure.epic("Signature-system")
@allure.feature("Signature")
class TestSignature:
    

    @classmethod
    def setup_class(cls):

        cls.api_signature = SignatureAPI()
        cls.signature_id = None


    # @allure.title("Create signature")
    # def test_create_signature(self):
    #     model = self.api_signature.create_signature()
    #     self.__class__.signature_id = model.data.id
    #     print(f"Create signature with ID: {self.__class__.signature_id}")
    #     assert model.message == "Успішно створено."


    @allure.title("Get signature by filter")
    def test_signature_by_filter(self):
        model = self.api_signature.get_signature_by_filter()
        assert model.message == "Дані успішно отримано."
        expected_id = model.data.items[0].id if model.data.items else None # Get the ID 1 element
        self.__class__.signature_id = expected_id
        print(f"Get signature with ID: {self.__class__.signature_id}")


    @allure.title("Get signature by ID")
    def test_signature_by_id(self):
        assert self.__class__.signature_id is not None, "signature_id не задано!"
        model = self.api_signature.get_signature_by_id(self.__class__.signature_id)
        assert model.message == "Успішно отримано."
        if model.data:
            assert model.data.id == self.__class__.signature_id, "The ID in the response does not match the expected one"
        else:
            ValueError("The response data is empty")



    @allure.title("Change signature by SignatureSystemID")
    def test_change_signature(self):
        value = Payloads.change_signature.copy()
        print(value)
        print(self.__class__.signature_id)
        model = self.api_signature.change_signature_by_id(self.__class__.signature_id)
        assert model.message == "Успішно оновлено."
        assert model.data.id == self.__class__.signature_id, "The ID in the response does not match the expected one"
        assert value["countOfSignaturesForDocument"] == model.data.countOfSignaturesForDocument, "The number of signatures in the response does not match the expected one"
        assert value["countOfStampsForDocument"] == model.data.countOfStampsForDocument, "The number of stamps in the response does not match the expected one"


    # @allure.title("Delete signature by SignatureSystemId")
    # def test_delete_signature(self):
    #     model = self.api_signature.delete_signature(self.__class__.signature_id)
    #     assert model.message == "Успішно видалено."


    # @allure.title("Check signature after delete")
    # def test_check_after_delete_signature(self):
    #     model = self.api_signature.get_signature_by_filter()
    #     assert model.message == "Дані успішно отримано."

    #     assert isinstance(model.data.items, list)

    #     ids = [item.id for item in model.data.items]
    #     assert self.__class__.signature_id not in ids, f"ID {self.__class__.signature_id} still on the list: {ids}"








