from faker import Faker

fake = Faker()

class Payloads:

    create_new_document= \
        {
            "documentType": "AccountOpeningOrder",
            "memberId": 10,  #this is Іванченко
            "llcId": 25        #this is New LLC
        }
    print(create_new_document)


