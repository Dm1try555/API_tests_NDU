import os
from dotenv import load_dotenv

load_dotenv()
HOST = os.getenv("HOST")


class Endpoints:

    get_llc = f"{HOST}/llc"
    create_llc = f"{HOST}/llc"
    get_llc_by_id = lambda self, id: f"{HOST}/llc/{id}"



