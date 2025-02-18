import os
from dotenv import load_dotenv

load_dotenv()
HOST = os.getenv("HOST")


class Endpoints:

    create_account = f"{HOST}/account"
    get_account = f"{HOST}/account"

