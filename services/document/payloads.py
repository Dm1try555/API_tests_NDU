from faker import Faker

fake = Faker()

class Payloads:

    create_new_document= \
        {
            "documentType": "AccountOpeningOrder",
            "memberAccountReference": "string",
            "memberDocumentNumber": "string",
            "llcId": 1,
            "llcMemberType": "CATEGORY110"
        }


