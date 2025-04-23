import os
from dotenv import load_dotenv

load_dotenv()
HOST = os.getenv("HOST")

class Endpoints:

    rejection_letter = f"{HOST}/document-receiver/rejection-letter"
    confirmation_letter = f"{HOST}/document-receiver/confirmation-letter"
    status = f"{HOST}/document-receiver/status"
    
    

    




