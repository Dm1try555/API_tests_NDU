import os
from dotenv import load_dotenv

load_dotenv()
HOST = os.getenv("HOST")

class Endpoints:

    file_upload = f"{HOST}/file/upload"
    get_file_by_id = lambda self, id: f"{HOST}/file/{id}"
    delete_file_by_id = lambda self, id: f"{HOST}/file/{id}"






