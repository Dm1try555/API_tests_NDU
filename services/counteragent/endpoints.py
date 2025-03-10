import os
from dotenv import load_dotenv

load_dotenv()
HOST = os.getenv("HOST")


class Endpoints:

    get_user = f"{HOST}/user"
    get_counteragent = f"{HOST}/counter-agent"




