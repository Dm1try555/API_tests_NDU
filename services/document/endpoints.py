import os
from dotenv import load_dotenv

load_dotenv()
HOST = os.getenv("HOST")

class Endpoints:

    get_document = f"{HOST}/document"
    create_document = f"{HOST}/document"
    get_document_by_id = lambda self, id: f"{HOST}/document/{id}"
    delete_document_by_id = lambda self, id: f"{HOST}/document/{id}"
    copy_document_by_id = lambda self, id: f"{HOST}/document/{id}/copy"
    audit_document_by_id = lambda self, id: f"{HOST}/document/{id}/audit"
    
    change_document_by_id = lambda self, id: f"{HOST}/document/{id}"
    send_document_by_id = lambda self, id: f"{HOST}/document/{id}/send"
    get_printed_document_by_id = lambda self, id: f"{HOST}/document/{id}/printed"
    upload_document_by_id = lambda self, id: f"{HOST}/document/{id}/upload"





