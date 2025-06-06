import os
from dotenv import load_dotenv

load_dotenv()

class Headers:

    basic = {
        "Authorization": f"Bearer {os.getenv('API_TOKEN')}"
    }

    basic_admin = {
        "Authorization": f"Bearer {os.getenv('API_TOKEN_ADMIN')}"
    }
