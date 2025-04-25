import allure
from services.signature.api_signature import SignatureAPI


@allure.epic("Signature-system")
@allure.feature("Signature")
class TestSignature:
    

    @classmethod
    def setup_class(cls):

        cls.api_signature = SignatureAPI()
        cls.signature_id = None


    @allure.title("Create signature")
    def test_create_signature(self):
        model = self.api_signature.create_signature()
        self.__class__.signature_id = model.data.id
        print(f"Create signature with ID: {self.__class__.signature_id}")
        assert model.message == "Успішно створено."


    @allure.title("Get signature by filter")
    def test_signature_by_filter(self):
        model = self.api_signature.get_signature_by_filter()
        assert model.data.items[2].id == self.__class__.signature_id
        print(f"Extracted id 3 elements: {self.__class__.signature_id}")


    @allure.title("Get signature by ID")
    def test_signature_by_id(self):
        model = self.api_signature.get_signature_by_id(self.__class__.signature_id)
        assert model.data.id == self.__class__.signature_id, "The ID in the response does not match the expected one"


    @allure.title("Change signature by SignatureSystemID")
    def test_change_signature(self):
        model = self.api_signature.change_signature_by_id(self.__class__.signature_id)
        assert model.message == "Успішно оновлено."
        assert model.data.id == self.__class__.signature_id, "The ID in the response does not match the expected one"


    @allure.title("Delete signature by SignatureSystemId")
    def test_delete_signature(self):
        model = self.api_signature.delete_signature(self.__class__.signature_id)
        assert model.message == "Успішно видалено."


    @allure.title("Check signature after delete")
    def test_check_after_delete_signature(self):
        model = self.api_signature.get_signature_by_filter()
        assert model.message == "Дані успішно отримано."

        assert isinstance(model.data.items, list)

        ids = [item.id for item in model.data.items]
        assert self.__class__.signature_id not in ids, f"ID {self.__class__.signature_id} still on the list: {ids}"








