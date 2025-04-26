from faker import Faker

fake = Faker()

class Payloads:

   llc= \
    {
        "edrpou": "TestEdrpou", 
        "name": "TestName",
    }


class Params:
   llc_params = \
    {
        "maxResultCount": 100, #int
        "skipCount": 0,   #int
        "sortOrder": "",   #str
        "filter": "",   #str
        "sortOrderType": "Ascending",   #str: Ascending or Descending
    }
   



