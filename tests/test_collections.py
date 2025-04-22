import allure
from services.collections.api_collections import CollectionsAPI


@allure.epic("Collections")
@allure.feature("Collections")
class TestCollections:

    @classmethod
    def setup_class(cls):
        cls.api_collections = CollectionsAPI()

    @allure.title("Get collections")
    def test_get_collections(self):
        model = self.api_collections.get_collections()
        assert model.message == "Дані успішно отримано."
        data = model.data

        assert data.documentStatus is not None, "Document status is None"
        assert data.llcMemberType is not None, "LLC member type is None"
        assert data.documentType is not None, "Document type is None"
        assert data.userStatusType is not None, "User status type is None"
        assert data.printedFormType is not None, "Printed form type is None"
        assert data.signatureType is not None, "Signature type is None"

        assert len(data.documentStatus) > 0, "Document status list is empty"
        assert len(data.llcMemberType) > 0, "LLC member type list is empty"
        assert len(data.documentType) > 0, "Document type list is empty"
        assert len(data.userStatusType) > 0, "User status type list is empty"
        assert len(data.printedFormType) > 0, "Printed form type list is empty"
        assert len(data.signatureType) > 0, "Signature type list is empty"

