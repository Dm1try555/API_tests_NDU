import re
import allure
import pytest
from services.file.api_file import FileAPI
import os

FILE_PATH = "text_file.txt"


@pytest.fixture
def create_test_file():
    """Create test file before test and delete after completing"""
    with open(FILE_PATH, "w") as f:
        f.write("Test file content")
    yield FILE_PATH
    os.remove(FILE_PATH)


@allure.epic("File")
@allure.feature("File")
class TestFile:

    @classmethod
    def setup_class(cls):
        cls.api_file = FileAPI()

    @allure.title("Upload, check and delete new file")
    def test_file(self, create_test_file):
        
        model = self.api_file.upload_new_file(create_test_file)
        assert model.message == "Файл успішно завантажено."
        print("File successfully uploaded:", model.data)
        assert model.data is not None

        file_url = model.data.url
        file_name = model.data.fileName

        get_id_match = re.search(r"/file/([a-f0-9\-]+)$", file_url)
        assert get_id_match, "Failed to extract file ID!"
        get_id = get_id_match.group(1)
        print("File ID:", get_id)
        print("File name:", file_name)

        check = self.api_file.get_file_by_id(get_id)
        assert check.headers.get("content-disposition") == "attachment; filename=text_file.txt; filename*=UTF-8''text_file.txt"
        print("The created file is displayed by ID:", get_id)

        delete = self.api_file.delete_file_by_id(get_id)
        print("File deleted by ID:", get_id)

        check_after_delete = self.api_file.get_file_by_id_after_delete(get_id)
        assert check_after_delete.title == "Not Found"
        print("The file does not exist:", get_id)
