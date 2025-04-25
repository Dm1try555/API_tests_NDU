import random

from faker import Faker

fake = Faker()


class Params:
    signature_params = \
        {
            "maxResultCount": 100,  # int
            "skipCount": 0,  # int
            "searchFilter": "",  # str
            "orderBy": "",  # str
            "sortOrderType": "Ascending",  # str: Ascending or Descending
        }
    


class Payloads:
    create_signature = \
        {
            "llcId": ,
            "countOfSignaturesForDocument": random.randint(1, 4),
            "countOfStampsForDocument": random.randint(1, 2)
        }


    change_signature = \
    {
        "countOfSignaturesForDocument": random.randint(1, 4),
        "countOfStampsForDocument": random.randint(1, 2)
    }
