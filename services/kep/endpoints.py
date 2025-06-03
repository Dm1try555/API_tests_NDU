import os
from dotenv import load_dotenv

load_dotenv()
HOST = os.getenv("HOST")

class Endpoints:

    create_kep_integration = f"{HOST}/kep/integration"
    get_kep_send_document = lambda self, id: f"{HOST}/kep/SendDocument/{id}"








