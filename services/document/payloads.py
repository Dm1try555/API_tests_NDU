from faker import Faker

fake = Faker()

class Payloads:

    create_new_document= \
        {
            "documentType": "AccountOpeningOrder",
            "memberId": 10,  #this is Іванченко
            "memberDocumentNumber": "string",
            "llcId": 25,        #this is New LLC
            "llcMemberType": "CATEGORY110"

        }
    print(create_new_document)


