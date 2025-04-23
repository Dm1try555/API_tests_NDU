from faker import Faker

fake = Faker()

class Payloads:

    rejection_letter= \
        {
            "document": {
                "externalGuid": "cadb2a1d-e428-4c1b-9313-a02f8b14a94e",
                "outDocKindName": "OutDocRejectLLC",
                "outDocKind": "OutDocKind",
                "outDocType": "OutDocType",
                "outDocTypeName": "Лист-відмова у виконанні Розпорядження на відкриття рахунку учаснику товариства",
                "docNum": "57152",
                "docDate": "2025-04-23T05:17:54.8342712+00:00",
                "notes": "Примітки",
                "clientCode": "КОД123",
                "clientName": "ТОВ 'Приклад'"
            },
            "documentFile": "Base64PDF==",
            "fileList": [
                {
                "name": "Друкована форма.pdf",
                "contentType": "application/pdf",
                "fileContent": "JVBERi0xLjQ...=="
                }
            ]
        }
    print(rejection_letter)

    confirmation_letter= \
        {
            "document": {
                "externalGuid": "7c21a560-1019-495c-b9ac-2ffb7009e719",
                "outDocKindName": "OutDocRejectLLC",
                "outDocKind": "OutDocKind",
                "outDocType": "OutDocType",
                "outDocTypeName": "Лист-відмова у виконанні Розпорядження на відкриття рахунку учаснику товариства",
                "docNum": "57152",
                "docDate": "2025-04-23T05:17:54.8367851+00:00",
                "notes": "Примітки",
                "clientCode": "КОД123",
                "clientName": "ТОВ 'Приклад'"
            },
            "documentFile": "Base64PDF==",
            "fileList": [
                {
                "name": "Друкована форма.pdf",
                "contentType": "application/pdf",
                "fileContent": "JVBERi0xLjQ...=="
                }
            ]
        }
    print(confirmation_letter)

    status= \
        {
            "externalGuid": "9d50d17a-e3f9-47af-8e7d-4673270b07dd",
            "document": {
                "status": "Accepted"
            }
        }
    print(status)


