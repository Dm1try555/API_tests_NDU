from faker import Faker

fake = Faker()

class Payloads:

   auth= \
    {
        "login": "8888888888", #Tenko Paolo KEP
        "password": "kcme12!.xYez"
    }
   print(auth)

   auth_code = \
       {
           "login": "8888888888", #Tenko Paolo KEP
           "password": "kcme12!.xYez"
       }
   print(auth_code)

   change_password = \
       {
           "newPassword": "kcme12!.xYez",
           "oldPassword": "kcme12!.xYez"
       }
   print(change_password)

#    refresh_token = \
#        {
#            "login": "13579",
#            "refreshToken": "string"
#        }
#    print(refresh_token)


