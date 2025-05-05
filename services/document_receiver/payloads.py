from faker import Faker
import base64
from pathlib import Path

fake = Faker()

def get_base64_pdf(path: str) -> str:
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")

class Payloads:
    def __init__(self):
        self.base64_pdf = get_base64_pdf("tests/files/sample.pdf")  

        self.rejection_letter = {
            "document": {
                "externalGuid": fake.uuid4(),
                "outDocKindName": "OutDocRejectLLC",
                "outDocKind": "OutDocKind",
                "outDocType": "OutDocType",
                "outDocTypeName": "Лист-відмова у виконанні Розпорядження на відкриття рахунку учаснику товариства",
                "docNum": "57152",
                "docDate": fake.iso8601(),
                "notes": "Примітки",
                "clientCode": "КОД123",
                "clientName": "ТОВ 'Приклад'"
            },
            "documentFile": self.base64_pdf,
            "fileList": [
                {
                    "name": "Друкована форма.pdf",
                    "contentType": "application/pdf",
                    "fileContent": self.base64_pdf
                }
            ]
        }

        self.confirmation_letter = {
            "document": {
                "externalGuid": fake.uuid4(),
                "outDocKindName": "OutDocRejectLLC",
                "outDocKind": "OutDocKind",
                "outDocType": "OutDocType",
                "outDocTypeName": "Лист-відмова у виконанні Розпорядження на відкриття рахунку учаснику товариства",
                "docNum": "57152",
                "docDate": fake.iso8601(),
                "notes": "Примітки",
                "clientCode": "КОД123",
                "clientName": "ТОВ 'Приклад'"
            },
            "documentFile": self.base64_pdf,
            "fileList": [
                {
                    "name": "Друкована форма.pdf",
                    "contentType": "application/pdf",
                    "fileContent": self.base64_pdf
                }
            ]
        }

        self.status = {
            "externalGuid": fake.uuid4(),
            "document": {
                "status": "Accepted"
            }
        }
