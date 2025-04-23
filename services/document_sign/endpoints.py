import os
from dotenv import load_dotenv

load_dotenv()
HOST = os.getenv("HOST")

class Endpoints:

    get_sign_document = lambda self, id: f"{HOST}/document/{id}/sign"
    create_sign_document = lambda self: f"{HOST}/document/{id}/sign"
    
    
    

    




