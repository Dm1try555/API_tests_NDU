from faker import Faker

fake = Faker()



class Params:
   signature_params = \
    {
        "maxResultCount": 100, #int
        "skipCount": 0,   #int
        "searchFilter": "",   #str
        "orderBy": "",   #str
        "sortOrderType": "Ascending",   #str: Ascending or Descending
    }
   print(signature_params)



