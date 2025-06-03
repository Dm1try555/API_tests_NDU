import allure
from services.document.api_document import DocumentAPI


@allure.epic("Document")
@allure.feature("Document")
class TestDocument:
    document_id = None
    copied_id = None

    @classmethod
    def setup_class(cls):
        cls.api_document = DocumentAPI()


    @allure.title("Get document list")
    def test_get_document_list(self):
        model = self.api_document.get_document_by_default_filters()
        assert model.message == "Документи отримано."


    @allure.title("Create new document")
    def test_create_new_document(self):
        model = self.api_document.create_new_document()
        assert model.data.id is not None, "Error: Document ID not created!"

        self.__class__.document_id = model.data.id
        print(f"Створений документ ID: {self.__class__.document_id}")

    @allure.title("Check document by ID")
    def test_check_document_by_id(self):
        assert self.__class__.document_id is not None, "The document was not created."

        model = self.api_document.get_document_by_id(self.__class__.document_id)
        assert model.data.id == self.__class__.document_id, "Error: Document ID does not match!"

    @allure.title("Copy document by ID")
    def test_copy_document_by_id(self):
        assert self.__class__.document_id is not None, "The document was not created."
        model = self.api_document.copy_document_by_id(self.__class__.document_id)
        assert model.message == "Копія успішно створена"
        copied_document_id = model.data.id
        assert copied_document_id != self.__class__.document_id
        assert isinstance(copied_document_id, int)     
        self.__class__.copied_id = copied_document_id   
        print(f"Original document ID: {self.__class__.document_id}, Copy ID: {copied_document_id}")

    @allure.title("Audit document by ID")
    def test_audit_document_by_id(self):
        assert self.__class__.document_id is not None, "The document was not created."
        model = self.api_document.audit_document_by_id(self.__class__.copied_id)
        assert model.message == "Дані отримано."

    @allure.title("Get Printed Forms by ID")
    def test_get_printed_forms_by_id(self):
        self.api_document.get_printed_form_by_id(self.__class__.copied_id)


    @allure.title("Change document by ID")
    def test_change_document_by_id(self):
        assert self.__class__.document_id is not None, "The document was not created."
        model = self.api_document.change_document(self.__class__.copied_id)
        assert model.message == "Документ оновлено."

    @allure.title("Delete document by ID")
    def test_delete_document_by_id(self):
        assert self.__class__.document_id is not None, "The document was not created."
        model = self.api_document.delete_document_by_id(self.__class__.copied_id)
        assert model.message == "Документ видалено."

    @allure.title("Check document by ID after delete")
    def test_check_document_by_id_after_delete(self):
        assert self.__class__.document_id is not None, "The document was not created."
        model = self.api_document.get_document_by_id_after_delete(self.__class__.copied_id)
        assert model.Message == "DocumentNotFound"

    

    @allure.title("Upload file document by ID")
    def test_upload_file_document_by_id(self):
        assert self.__class__.document_id is not None, "The document was not created."
        file_path = "tests/files/file_upload.docx"
        model = self.api_document.upload_document_by_id(self.__class__.document_id, file_path)
        assert model.message == "Файл завантажено"
        assert len(model.data.files) > 0

    


