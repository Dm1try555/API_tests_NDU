import os
from dotenv import load_dotenv

load_dotenv()
HOST = os.getenv("HOST")

class Endpoints:

    get_signature = f"{HOST}/signature-system"
    create_signature = f"{HOST}/signature-system"
    get_signature_by_id = lambda self, id : f"{HOST}/signature-system/{id}"
    change_signature_by_id = lambda self, id : f"{HOST}/signature-system/{id}"
    delete_signature_by_id = lambda self, id : f"{HOST}/signature-system/{id}"



