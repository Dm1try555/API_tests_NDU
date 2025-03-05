import os
from dotenv import load_dotenv

load_dotenv()
HOST = os.getenv("HOST")

class Endpoints:

    create_document = f"{HOST}/document"
    get_document_by_id = lambda self, id: f"{HOST}/document/{id}"





