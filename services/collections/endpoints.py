import os
from dotenv import load_dotenv

load_dotenv()
HOST = os.getenv("HOST")


class Endpoints:

    get_collections = f"{HOST}/collections"
