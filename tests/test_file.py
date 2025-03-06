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
        """API File Test Method"""
        model = self.api_file.upload_new_file(create_test_file)
        assert model.message == "Файл успішно завантажено."
        print("Файл успішно завантажено:", model.data)
        get_id = re.search(r"/file/([a-f0-9\-]+)$", model.data).group(1)
        print("File ID:", get_id)
        check = self.api_file.get_file_by_id(get_id)
        print("Створений файл відображається по ID:", get_id)
        delete = self.api_file.delete_file_by_id(get_id)
        print("Файл видалений по ID:", get_id)
        check_after_delete = self.api_file.get_file_by_id_after_delete(get_id)
        print("Файлу не існує:", get_id)


