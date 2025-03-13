import os
from dotenv import load_dotenv

load_dotenv()
HOST = os.getenv("HOST")


class Endpoints:

    get_llc = f"{HOST}/llc"
    create_llc = f"{HOST}/llc"
    get_llc_by_id = lambda self, id: f"{HOST}/llc/{id}"
    add_manager_to_LLC = lambda self, llc_id, user_id: f"{HOST}/llc/{llc_id}/managers/{user_id}"



